"""Synthetic source regressions. These fixtures are never qualification evidence."""

from copy import deepcopy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "specs/043-private-connectivity-production/verify-evidence.py"
SPEC = importlib.util.spec_from_file_location("production_evidence_043", MODULE)
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)
TASKS = v.load_contract(ROOT)
NOW = datetime(2030, 1, 2, tzinfo=timezone.utc)
START = "2030-01-01T00:00:00Z"
END = "2030-01-01T00:01:00Z"
AUTHORITY_START = "2029-01-01T00:00:00Z"
AUTHORITY_END = "2031-01-01T00:00:00Z"


def shifted(value, seconds):
    return (v.timestamp(value) + timedelta(seconds=seconds)).isoformat().replace("+00:00", "Z")


@pytest.fixture(scope="module")
def accepted_historical_control():
    manifest = v.decode(subprocess.check_output(["git", "show", "HEAD:" + v.COMMISSIONING_PATH], cwd=ROOT))
    anchor = manifest["historical_controls"]["T012"]
    # Retention keeps exact objects available independently of a merge's ancestry.
    # The bridge checks both fixed digests and the complete matching frozen inputs.
    v.historical_verifier(v.GitStore({v.COORDINATOR: str(ROOT)}), anchor)
    return anchor


def test_actual_historical_control_uses_matching_frozen_reader(accepted_historical_control):
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    prior = v.make_verifier(TASKS, store, accepted_historical_control)
    predecessor = v.T023_PREDECESSOR["reference"]
    selected = v.make_verifier(TASKS, store, predecessor)
    assert selected.definition == v.T010_CUSTODY_SUCCESSOR
    assert selected.trust["authorizes_production"] is False
    with pytest.raises(ValueError, match="uncommissioned task"):
        selected.binding("T023")
    assert prior.definition == v.LEGACY_DEFINITION
    for task in ("T010", "T011", "T012", "T016"):
        prior.verify(task)


def test_historical_fixture_resolves_retained_objects_after_squash(tmp_path, monkeypatch):
    root = tmp_path / "synthetic-squash"
    root.mkdir()
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/" + v.COORDINATOR + ".git"], cwd=root, check=True)
    objects = subprocess.check_output(["git", "rev-parse", "--git-path", "objects"], cwd=ROOT, text=True).strip()
    (root / ".git/objects/info/alternates").write_text(str((ROOT / objects).resolve()) + "\n")
    tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip()
    squash = subprocess.check_output(["git", "-c", "user.name=Synthetic squash", "-c", "user.email=squash@example.invalid",
                                      "commit-tree", tree, "-m", "Synthetic root, with retained immutable objects"],
                                     cwd=root, text=True).strip()
    subprocess.run(["git", "update-ref", "HEAD", squash], cwd=root, check=True)
    manifest = v.decode(subprocess.check_output(["git", "show", "HEAD:" + v.COMMISSIONING_PATH], cwd=root))
    anchor = manifest["historical_controls"]["T012"]
    assert subprocess.run(["git", "merge-base", "--is-ancestor", anchor["commit"], "HEAD"], cwd=root).returncode == 1
    monkeypatch.setitem(globals(), "ROOT", root)
    resolved = accepted_historical_control.__wrapped__()
    assert resolved == anchor
    reader = v.make_verifier(TASKS, v.GitStore({v.COORDINATOR: str(root)}), resolved)
    for task in ("T010", "T011", "T012", "T016"):
        reader.verify(task)


@pytest.fixture
def current_historical_world(accepted_historical_control, monkeypatch):
    """Synthetic current custody review over immutable real historical bytes."""
    git_store = v.GitStore({v.COORDINATOR: str(ROOT)})
    world = World()
    original_blob = world.store.blob
    def blob(ref):
        identity = (ref["repository"], ref["commit"], ref["path"])
        return original_blob(ref) if identity in world.store.objects else git_store.blob(ref)
    monkeypatch.setattr(world.store, "blob", blob)
    monkeypatch.setattr(world.store, "changed", git_store.changed)
    monkeypatch.setattr(world.store, "git", git_store.git, raising=False)
    monkeypatch.setattr(world.store, "root", git_store.root, raising=False)
    world.trust = v.decode(git_store.blob(accepted_historical_control))
    world.trust["definition"] = v.DEFINITION
    world.trust["historical_controls"] = {task: accepted_historical_control for task in ("T011", "T012", "T016")}
    return world


@pytest.mark.parametrize("task", ["T011", "T012", "T016"])
@pytest.mark.parametrize("state", ["revoked-authority", "revoked-decision", "closed-authority"])
@pytest.mark.parametrize("cached", [False, True])
def test_historical_prerequisites_use_current_authority_state(current_historical_world, task, state, cached):
    world = current_historical_world
    binding = world.trust["bindings"]["T007"]
    authority = world.trust["source_container"]["objects"][binding["authority"]["object"]]["value"]
    anchor = source_anchor(world)
    reader = v.Verifier(TASKS, world.store, anchor, now=NOW)
    if cached:
        reader.verify(task)
    identity = authority["id"]
    if state == "revoked-decision":
        ref = authority["decisions"]["C-01"]
        identity = world.trust["source_container"]["objects"][ref["object"]]["value"]["id"]
    if state == "closed-authority":
        reader.trust["completed_authorities"] = {identity: world.store.put(
            dict(kind="authority-closure", authority_id=identity, scope=binding["scope"],
                 disposition="completed", closed_at=START, owner="Synthetic Owner"), "closures/current.json")}
    else:
        reader.trust["revoked_authorities"].append(identity)
    with pytest.raises(v.EvidenceError, match="revoked|closed"):
        reader.verify("T007")
    with pytest.raises(v.EvidenceError, match="revoked|closed"):
        reader.verify(task)


@pytest.mark.parametrize("task", ["T011", "T012", "T016"])
def test_historical_dependencies_keep_their_actual_prior_ci(current_historical_world, task):
    world = current_historical_world
    # This child consumed the old accepted T010, not a later replacement's command.
    world.trust["bindings"]["T010"]["command"] = "synthetic later CI awaiting qualification"
    reader = v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)
    reader.verify(task)


@pytest.mark.parametrize("mutation", ["control", "definition", "reader", "frozen-input"])
def test_historical_bridge_rejects_unaccepted_content(accepted_historical_control, monkeypatch, mutation):
    ref = dict(accepted_historical_control)
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    if mutation == "control": ref["sha256"] = "a" * 64
    if mutation == "definition": monkeypatch.setattr(v, "LEGACY_DEFINITION", "a" * 64)
    if mutation == "reader": monkeypatch.setattr(v, "LEGACY_READER_SHA256", "a" * 64)
    if mutation == "frozen-input":
        original = store.git
        def changed(root, *args):
            data = original(root, *args)
            return data + b"\nchanged input" if args[0] == "show" and args[1].endswith("/spec.md") else data
        monkeypatch.setattr(store, "git", changed)
    with pytest.raises(v.EvidenceError): v.historical_verifier(store, ref)


@pytest.mark.parametrize("mutation", [None, "binding", "revoked", "pending"])
def test_historical_dependency_retains_current_authentication_and_authority(monkeypatch, mutation):
    world = World(); world.add("T012")
    binding = world.trust["bindings"]["T012"]
    original = deepcopy(binding)
    world.trust["historical_controls"] = {"T012": dict(repository=v.COORDINATOR, commit="a" * 40,
                                                      path=v.COMMISSIONING_PATH, sha256=v.LEGACY_CONTROL_SHA256)}
    calls = []
    if mutation == "binding": original["command"] += " changed"
    if mutation == "revoked": world.trust["revoked_authorities"].append(json.loads(world.store.blob(binding["authority"]))["id"])
    monkeypatch.setattr(v, "historical_verifier", lambda *a: SimpleNamespace(binding=lambda key: original,
                                                                            verify=lambda *a: calls.append(True),
                                                                            trust=deepcopy(world.trust), objects={}))
    verifier = world.verifier()
    if mutation == "pending": verifier.authenticated = False
    if mutation:
        with pytest.raises(v.EvidenceError): verifier.verify("T012")
        assert calls == []
    else:
        verifier.verify("T012"); assert calls == [True]
        verifier.trust["revoked_authorities"].append(json.loads(world.store.blob(binding["authority"]))["id"])
        with pytest.raises(v.EvidenceError): verifier.verify("T012")


class MemoryObjects:
    """Content-addressed immutable objects; no provider or actual customer data."""

    def __init__(self):
        self.objects = {}
        self.diffs = {}

    def put(self, data, path="exports/output.json", repository=v.COORDINATOR, revision=None):
        data = data if isinstance(data, bytes) else json.dumps(data, sort_keys=True).encode()
        sha = v.digest(data)
        revision = revision or sha[:40]
        key = (repository, revision, path)
        assert key not in self.objects or self.objects[key] == data
        self.objects[key] = data
        return dict(repository=repository, commit=revision, path=path, sha256=sha)

    def blob(self, ref):
        v.reference(ref)
        data = self.objects[(ref["repository"], ref["commit"], ref["path"])]
        v.require(v.digest(data) == ref["sha256"], "immutable content digest mismatch")
        return data

    def changed(self, source):
        return self.diffs[(source["repository"], source["revision"])]


class World:
    def __init__(self):
        self.store = MemoryObjects()
        self.review = self.store.put(b"SYNTHETIC independent test review", "reviews/source.txt")
        self.trust = dict(schema="043-reviewed-trust-v1", feature=v.FEATURE, definition=v.DEFINITION,
                          custodian="Brett Heap", review=self.review, custody=dict(kind="source-git"),
                          repositories={"C": v.COORDINATOR, "L": "opensoft/headscale-install", "I": "opensoft/xfactory-installer",
                                        "H": "opensoft/openxsoft-hosted-services", "O": "opensoft/opsxfactory", "D": "test/domain"},
                          revoked_authorities=[], bindings={}, instances={}, aggregates={})
        self.records, self.outputs = {}, {}

    def decision(self, kind, scope):
        return self.store.put(dict(id=kind + "-" + v.digest(json.dumps(scope, sort_keys=True).encode()), kind=kind,
                                   decision="accepted", scope=scope, owner="Synthetic Owner",
                                   valid_from=AUTHORITY_START, valid_until=AUTHORITY_END), "decisions/" + kind + ".json")

    def add(self, task, instance=None, scope_changes=None, dependencies=None, decisions=None):
        if task in v.INSTANCE_TASKS and instance is None:
            if task not in self.trust["aggregates"]:
                self.child(task)
                self.aggregate(task)
            return task
        key = task + ("@" + instance if instance else "")
        if key in self.trust["bindings"]:
            return key
        definition = TASKS[task]
        repo = self.trust["repositories"][definition["owner"]]
        changes = set()
        for envelope in definition["files"]:
            changes.add(envelope + "synthetic.txt" if envelope.endswith("/") else envelope)
        source = dict(repository=repo, base="a" * 40, revision=v.digest(key.encode())[:40])
        self.store.diffs[(repo, source["revision"])] = changes
        scope = {field: "not-applicable" for field in v.SCOPE_FIELDS}
        scope.update(run="synthetic-run", candidate="synthetic-candidate", environment="source", phase="source", offering="hosted-headscale")
        if 50 <= int(task[1:]) <= 64:
            scope["phase"] = "staging" if int(task[1:]) <= 56 else "production"
        scope.update(scope_changes or {})
        dependencies = dependencies or {dep: self.add(dep) for dep in definition["dependencies"]}
        binding = dict(task=task, instance=instance, owner=definition["owner"], scope=scope, source=source,
                       files=sorted(changes), command=definition["command"], roles=["synthetic-owner"], decisions=decisions or [],
                       incidents=[], cases={name: [dict(id="actual-identity", kind="equal", expected="observed-original-subject")]
                              for name in definition["cases"]}, dependencies=dependencies, history=[], remediation=None,
                       metrics={}, observation=None, ci={}, artifacts=[], **{"class": definition["class"]})
        if int(task[1:]) >= 10:
            binding["command"] = "synthetic-owner-tool --task " + task
        if definition["class"].startswith("CI-"):
            binding["ci"] = {"tests/synthetic.py": 3}
        if task == "T010":
            binding["ci"] = {v.FEATURE_PATH + "/tests/" + name: 3 for name in ("test_evidence.py", "test_evidence_pins.py", "test_source_roots.py", "test_delegated_evidence.py")}
        if task == "T023":
            binding["ci"] = {"package-owner-qualification": 171, "package-production-runner": 49}
        if task == "T050":
            binding["decisions"] = ["C-03", "C-07"]
        if task == "T051":
            binding["decisions"] = [f"C-{i:02}" for i in range(3, 9)]
        if scope["phase"] in ("staging", "production"):
            if "C-08" not in binding["decisions"]:
                binding["decisions"].append("C-08")
            self.trust["live_custody"] = dict(kind="protected", decision="C-08")
            binding["metrics"] = {"synthetic-latency": dict(minimum=0, maximum=10, unit="seconds", event="probe")}
            binding["observation"] = dict(window=[START, END], max_gap_seconds=0, minimum_observed_seconds=60)
        self.trust["bindings"][key] = binding
        if instance:
            self.trust["instances"].setdefault(task, []).append(instance)
        decision = dict(id="authority-" + key, owner="Synthetic Owner", roles=binding["roles"], decision="accepted", scope=scope,
                        valid_from=AUTHORITY_START, valid_until=AUTHORITY_END, mode="source",
                        decisions={d: self.decision(d, scope) for d in binding["decisions"]})
        if scope["phase"] != "source":
            decision.update(mode="customer", consent=self.decision("consent", scope))
        binding["authority"] = self.store.put(decision, "decisions/" + key + ".json")
        artifact_path = next(iter(changes))
        paths = set(changes)
        if int(task[1:]) < 10:
            for envelope in definition["files"]:
                if envelope.endswith("/") and envelope.startswith("openspec/"):
                    paths.update((envelope + "proposal.md", envelope + ".openspec.yaml"))
        binding["artifacts"] = [] if task == "T002" else [self.store.put(b"SYNTHETIC source artifact", path, repo, source["revision"]) for path in paths
                                                         if task != "T006" or not path.startswith("openspec/")]
        if task == "T002":
            old = self.store.put(dict(verdict="pass"), "specs/040-private-connectivity/evidence/T021.json", repo, source["revision"])
            baseline = self.store.put(dict(evidence_class="historical-lab", authorizes_production=False, evidence_sha256=old["sha256"]),
                                      v.FEATURE_PATH + "/evidence/baseline.json", repo, source["revision"])
            binding["artifacts"] = [old, baseline]
        if task == "T006":
            base = "openspec/changes/commission-private-connectivity-production-evidence/"
            binding["artifacts"] += [self.store.put(data, base + name, repo, source["revision"]) for name, data in
                                    (("proposal.md", b"Status: ratified"), ("review/ratification.md", b"Ratified: by test owner"),
                                     (".openspec.yaml", b"origin:\n  approved_by: Synthetic Owner"))]
        record = dict(schema="043-bootstrap-import-v1" if int(task[1:]) < 10 else "043-task-evidence-v1",
                      task=task, instance=instance, owner=binding["owner"], evidence_class=binding["class"], scope=scope,
                      attempt="attempt-1", verdict="pass", source=source, command=binding["command"], authority=binding["authority"],
                      artifacts=binding["artifacts"], incidents=[], history=[], dependencies={d: self.ref(k) for d, k in dependencies.items()})
        output = {field: deepcopy(record[field]) for field in ("task", "instance", "scope", "source", "command")}
        output.update(exit_code=0, started_at=START, ended_at=END, events={}, metrics={}, coverage=None,
                      cases=[dict(id=name, scope=deepcopy(scope), source=deepcopy(source), checks=[dict(id="actual-identity", observed="observed-original-subject")]) for name in definition["cases"]],
                      ci={suite: dict(repository=repo, revision=source["revision"], conclusion="success", required=True,
                                      collected=count, passed=count, skipped=0, run_id=101, job_id=201) for suite, count in binding["ci"].items()})
        if scope["phase"] != "source":
            output.update(events=dict(probe=START), metrics={"synthetic-latency": dict(value=1, unit="seconds", event="probe")},
                          coverage=dict(window=[START, END], intervals=[[START, END]]))
        if task == "T023":
            proof, approval = synthetic_t023_proof(repo, source["revision"], 101, 201, scope)
            proof["readback"]["provenance"] = next(item for item in binding["artifacts"]
                if item["path"] == "release/private-connectivity-production.json")
            proof["authorization"] = self.store.put(approval, "decisions/t023-publication.json")
            output["t023_release"] = proof
            binding["t023_release_sha256"] = v.digest(v.canonical_json(proof))
        self.records[key], self.outputs[key] = record, output
        self.publish(key)
        if 50 <= int(task[1:]) <= 64:
            # Source completes first; preparation and each runtime task have a
            # separate synthetic minute, with a minute between adjacent tasks.
            offset = 3600 + (int(task[1:]) - 50) * 120
            move_live_observation(self, key, shifted(START, offset), shifted(END, offset))
        return key

    def ref(self, key):
        if key in v.INSTANCE_TASKS:
            return self.trust["aggregates"][key]
        return self.trust["bindings"][key]["record"]

    def publish(self, key):
        record = self.records[key]
        binding = self.trust["bindings"][key]
        record["output"] = self.store.put(self.outputs[key], "outputs/" + key + ".json")
        if key == "T023":
            binding["admission_roles"] = ["synthetic-release-admission"]
            binding["admission"] = self.store.put(dict(kind="evidence-admission", decision="accepted",
                id="synthetic-T023-admission", owner="Synthetic Admitter", scope=binding["scope"],
                roles=binding["admission_roles"], authority=binding["authority"],
                reviewed_output_sha256=record["output"]["sha256"], valid_from=AUTHORITY_START,
                valid_until=AUTHORITY_END, reviewed_at=shifted(END, 2)), "decisions/t023-admission.json")
            record["admission"] = binding["admission"]
        number = int(binding["task"][1:])
        owner = binding["owner"]
        prefix = v.FEATURE_PATH + "/evidence/" if owner == "C" else "evidence/private-connectivity-production/"
        path = "exports/" + key + ".import.json" if number < 10 else prefix + binding["task"] + ".json"
        if binding["instance"]:
            path = prefix + "instances/" + binding["task"] + "/" + binding["instance"] + ".json"
            if path not in binding["files"]: binding["files"].append(path)
        repository = self.trust["repositories"][owner] if number >= 10 else v.COORDINATOR
        binding["record"] = self.store.put(record, path, repository)

    def verifier(self):
        anchor = self.store.put(self.trust, "commissioning/reviewed-manifest.json")
        return v.Verifier(TASKS, self.store, anchor, now=NOW)

    def check(self, key):
        self.publish(key)
        self.verifier().verify(key)

    def child(self, task, instance="service", scope_changes=None, decisions=None):
        deps = {}
        for dep in TASKS[task]["dependencies"]:
            deps[dep] = self.child(dep, instance, scope_changes) if dep in v.INSTANCE_TASKS else self.add(dep)
        defaults = {"T057": ["C-09"], "T058": ["C-09"], "T061": ["C-10"],
                    "T062": ["C-11"], "T063": ["C-11"], "T064": ["C-11"]}
        selected = list(decisions if decisions is not None else defaults.get(task, []))
        if decisions is None and task in ("T062", "T063", "T064") and (scope_changes or {}).get("wave", "not-applicable") != "not-applicable":
            selected.append("C-12")
        return self.add(task, instance, scope_changes, deps, selected)

    def aggregate(self, task):
        data = dict(schema="043-instance-aggregate-v1", task=task,
                    children={i: self.ref(task + "@" + i) for i in self.trust["instances"][task]})
        owner = TASKS[task]["owner"]
        prefix = v.FEATURE_PATH + "/evidence/" if owner == "C" else "evidence/private-connectivity-production/"
        self.trust["aggregates"][task] = self.store.put(data, prefix + task + ".json", self.trust["repositories"][owner])
        return self.store.blob(self.trust["aggregates"][task])


@pytest.fixture
def world():
    return World()


def source_container_world():
    """New commissioning format, built only from synthetic original Git blobs."""
    world = World()
    world.add("T010")
    objects = {}
    def contain(name, task, value):
        objects[name] = dict(tasks=[task], evidence_class="source", value=deepcopy(value))
        return {"object": name}
    for task in sorted(world.trust["bindings"]):
        binding, record = world.trust["bindings"][task], world.records[task]
        authority = v.decode(world.store.blob(binding["authority"]))
        for kind, ref in authority["decisions"].items():
            authority["decisions"][kind] = contain(task + "-" + kind, task, v.decode(world.store.blob(ref)))
        binding["authority"] = contain(task + "-authority", task, authority)
        record["authority"] = binding["authority"]
        output = deepcopy(world.outputs[task])
        raw = "SYNTHETIC original command output\n"
        output["original"] = dict(command=binding["command"], repository=binding["source"]["repository"],
            source_revision=binding["source"]["revision"], started_at=output["started_at"], ended_at=output["ended_at"],
            exit_code=output["exit_code"], stdout=raw, original_sha256=v.digest(raw.encode()),
            export_sha256=v.digest(raw.encode()), redaction_method="none")
        record["output"] = contain(task + "-output", task, output)
        record["dependencies"] = {dep: world.ref(selected) for dep, selected in binding["dependencies"].items()}
        if int(task[1:]) < 10:
            binding["record"] = contain(task + "-import", task, record)
        else:
            binding["record"] = world.store.put(record, v.FEATURE_PATH + "/evidence/T010.json")
    world.trust["source_container"] = dict(schema="043-source-container-v1", objects=objects)
    return world


def source_anchor(world, *, accepted=True, mutate_review=None):
    pending = dict(schema="043-source-authentication-v1", decision="pending", custodian="Brett Heap",
                   reviewed_manifest=None, content_sha256=None, reviewed_at=None)
    def publish_review(value):
        fence = bytes([96]) * 3
        return world.store.put(b"# SYNTHETIC custody review\n\n" + fence + b"json\n" + v.canonical_json(value) + b"\n" + fence + b"\n",
                               v.AUTHENTICATION_PATH)
    world.trust["review"] = publish_review(pending)
    first = world.store.put(world.trust, v.COMMISSIONING_PATH)
    if accepted:
        review = dict(pending, decision="accepted", reviewed_manifest=first,
                      content_sha256=v.commissioning_digest(world.trust), reviewed_at="2030-01-01T01:00:00Z")
        if mutate_review:
            mutate_review(review)
        world.trust["review"] = publish_review(review)
    return world.store.put(world.trust, v.COMMISSIONING_PATH)


def test_contained_bootstrap_and_distinct_git_receipt_verify_without_self_hash():
    world = source_container_world()
    anchor = source_anchor(world)
    reader = v.Verifier(TASKS, world.store, anchor, now=NOW)
    before = deepcopy(world.store.objects)
    reader.verify("T010")
    assert reader.cache == {f"T{i:03}" for i in range(1, 11)}
    assert world.store.objects == before
    assert all(set(world.ref(f"T{i:03}")) == {"object"} for i in range(1, 10))
    assert set(world.ref("T010")) == v.REF_FIELDS
    assert world.ref("T010")["commit"] != anchor["commit"]


@pytest.mark.parametrize("prepare", [False, True])
def test_pending_container_never_satisfies_task_or_aggregate(prepare):
    world = source_container_world()
    anchor = source_anchor(world, accepted=False)
    with pytest.raises(v.EvidenceError, match="authentication pending"):
        reader = v.Verifier(TASKS, world.store, anchor, now=NOW, prepare=prepare)
        reader.verify("T010")
    if prepare:
        reader = v.Verifier(TASKS, world.store, anchor, now=NOW, prepare=True)
        with pytest.raises(v.EvidenceError, match="authentication pending"):
            reader.aggregate("T057", b"{}")


@pytest.mark.parametrize("mutation", ["missing", "cycle", "self-cycle", "extra-ref-field", "bad-id",
                                      "unknown-task", "duplicate-task", "live-task", "foreign-owner",
                                      "wrong-class", "array-value", "unused-missing"])
def test_contained_table_is_closed_and_source_only(mutation):
    world = source_container_world()
    objects = world.trust["source_container"]["objects"]
    entry = objects["T007-output"]
    if mutation == "missing": del objects["T007-output"]
    if mutation == "cycle":
        entry["value"]["nested"] = {"object": "T007-authority"}
        objects["T007-authority"]["value"]["nested"] = {"object": "T007-output"}
    if mutation == "self-cycle": entry["value"]["nested"] = {"object": "T007-output"}
    if mutation == "extra-ref-field": world.trust["bindings"]["T007"]["record"]["path"] = "elsewhere"
    if mutation == "bad-id": objects["../escape"] = deepcopy(entry)
    if mutation == "unknown-task": entry["tasks"] = ["T999"]
    if mutation == "duplicate-task": entry["tasks"] *= 2
    if mutation == "live-task": entry["tasks"] = ["T052"]
    if mutation == "foreign-owner": entry["tasks"] = ["T011"]
    if mutation == "wrong-class": entry["evidence_class"] = "staging"
    if mutation == "array-value": entry["value"] = []
    if mutation == "unused-missing":
        objects["unused"] = dict(tasks=["T007"], evidence_class="source", value={"nested": {"object": "absent"}})
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)


@pytest.mark.parametrize("mutation", ["task", "scope", "source", "command", "case", "exit"])
def test_authenticated_container_still_checks_original_output_identity(mutation):
    world = source_container_world()
    output = world.trust["source_container"]["objects"]["T007-output"]["value"]
    if mutation == "task": output["task"] = "T008"
    if mutation == "scope": output["scope"]["customer"] = "other-customer"
    if mutation == "source": output["source"]["revision"] = "f" * 40
    if mutation == "command": output["command"] = "echo pass"
    if mutation == "case": output["cases"] = []
    if mutation == "exit": output["exit_code"] = 1
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, source_anchor(world), now=NOW).verify("T007")


def test_contained_object_cannot_be_borrowed_by_different_task_or_live_scope():
    world = source_container_world()
    reader = v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)
    binding = deepcopy(world.trust["bindings"]["T007"])
    with pytest.raises(v.EvidenceError, match="task substitution"):
        reader.read({"object": "T008-output"}, binding)
    for field, value in [("owner", "L"), ("task", "T011"), ("scope", dict(binding["scope"], phase="staging"))]:
        altered = dict(binding, **{field: value})
        with pytest.raises(v.EvidenceError, match="outside E source"):
            reader.read({"object": "T007-output"}, altered)
    with pytest.raises(v.EvidenceError, match="outside E source"):
        reader.read({"object": "T007-output"})


@pytest.mark.parametrize("mutation", ["missing", "command", "source", "time", "exit", "export", "raw-digest", "redaction"])
def test_container_import_requires_original_provenance(mutation):
    world = source_container_world()
    output = world.trust["source_container"]["objects"]["T007-output"]["value"]
    original = output["original"]
    if mutation == "missing": del output["original"]
    if mutation == "command": original["command"] = "echo pass"
    if mutation == "source": original["source_revision"] = "f" * 40
    if mutation == "time": original["started_at"] = "2029-01-01T00:00:00Z"
    if mutation == "exit": original["exit_code"] = False
    if mutation == "export": original["stdout"] = "substituted"
    if mutation == "raw-digest": original["original_sha256"] = "0" * 64
    if mutation == "redaction": original["redaction_method"] = ""
    with pytest.raises((v.EvidenceError, KeyError)):
        v.Verifier(TASKS, world.store, source_anchor(world), now=NOW).verify("T007")


def test_redacted_original_retains_raw_digest_and_actual_method():
    world = source_container_world()
    original = world.trust["source_container"]["objects"]["T007-output"]["value"]["original"]
    original.update(original_sha256="0" * 64, redaction_method="SYNTHETIC fixture: replaced machine path with placeholder")
    v.Verifier(TASKS, world.store, source_anchor(world), now=NOW).verify("T007")


@pytest.mark.parametrize("field,value", [
    ("decision", "pending"), ("custodian", "Other Owner"), ("content_sha256", "0" * 64),
    ("reviewed_at", "2040-01-01T00:00:00Z"), ("reviewed_at", "2029-01-01T00:00:00Z"),
    ("reviewed_manifest", dict(repository=v.COORDINATOR, commit="f" * 40, path="other.json", sha256="f" * 64)),
])
def test_actual_authentication_must_match_concrete_manifest_and_run(field, value):
    world = source_container_world()
    anchor = source_anchor(world, mutate_review=lambda review: review.update({field: value}))
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, anchor, now=NOW).verify("T010")


def test_changing_authenticated_payload_or_binding_requires_new_human_review():
    world = source_container_world()
    anchor = source_anchor(world)
    world.trust["source_container"]["objects"]["T007-output"]["value"]["exit_code"] = 1
    substituted = world.store.put(world.trust, v.COMMISSIONING_PATH)
    with pytest.raises(v.EvidenceError, match="authentication content mismatch"):
        v.Verifier(TASKS, world.store, substituted, now=NOW)
    # The original immutable anchor remains usable.
    v.Verifier(TASKS, world.store, anchor, now=NOW).verify("T010")


def test_derived_inventory_can_change_without_rewriting_authenticated_observations():
    world = source_container_world()
    source_anchor(world)
    world.trust["pin_inventory"] = [{"openxfactory_commit": "a" * 40}]
    # Inventory correctness is independently checked by T008/doc-health.
    anchor = world.store.put(world.trust, v.COMMISSIONING_PATH)
    v.Verifier(TASKS, world.store, anchor, now=NOW).verify("T010")


def test_container_cannot_downgrade_to_legacy_nonempty_review():
    world = World()
    world.add("T007")
    anchor = world.store.put(world.trust, v.COMMISSIONING_PATH)
    with pytest.raises(v.EvidenceError, match="source commissioning container required"):
        v.Verifier(TASKS, world.store, anchor, now=NOW)
    with pytest.raises(v.EvidenceError, match="immutable reference"):
        v.reference({"object": "caller-selected"})


def test_container_duplicate_json_object_names_fail_before_authentication():
    world = source_container_world()
    anchor = source_anchor(world)
    raw = world.store.blob(anchor).replace(b'"objects": {', b'"objects": {"dup": {}, "dup": {}, ', 1)
    assert raw != world.store.blob(anchor)
    bad = world.store.put(raw, v.COMMISSIONING_PATH)
    with pytest.raises(v.EvidenceError, match="duplicate JSON key"):
        v.Verifier(TASKS, world.store, bad, now=NOW)


@pytest.mark.parametrize("task", [f"T{i:03}" for i in range(1, 69)])
def test_each_frozen_task_and_case_has_acceptance_and_rejection(world, task):
    if task in v.INSTANCE_TASKS:
        key = world.child(task)
    else:
        if int(task[1:]) >= 65:
            for predecessor in ("T064",):
                world.child(predecessor)
                world.aggregate(predecessor)
        key = world.add(task)
    world.check(key)
    for case in world.outputs[key]["cases"]:
        original = case["checks"][0]["observed"]
        case["checks"][0]["observed"] = "copied pass"
        with pytest.raises(v.EvidenceError, match="expected/observed"):
            world.check(key)
        case["checks"][0]["observed"] = original


@pytest.mark.parametrize("field", sorted(v.SCOPE_FIELDS))
def test_wrong_record_or_output_scope_rejected(world, field):
    key = world.add("T007")
    world.outputs[key]["scope"][field] = "foreign"
    with pytest.raises(v.EvidenceError, match="scope"):
        world.check(key)


@pytest.mark.parametrize("mutation", ["duplicate", "missing", "unknown", "subcheck-duplicate", "subcheck-missing"])
def test_closed_cases_and_subchecks(world, mutation):
    key = world.add("T007")
    cases = world.outputs[key]["cases"]
    if mutation == "duplicate": cases.append(deepcopy(cases[0]))
    if mutation == "missing": cases.pop()
    if mutation == "unknown": cases[0]["id"] = "invented"
    if mutation == "subcheck-duplicate": cases[0]["checks"].append(deepcopy(cases[0]["checks"][0]))
    if mutation == "subcheck-missing": cases[0]["checks"] = []
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("field,value", [("evidence_class", "Q2"), ("owner", "L"), ("command", "echo pass"), ("verdict", "blocked"), ("verdict", "fail")])
def test_wrong_record_class_owner_command_or_result(world, field, value):
    key = world.add("T007")
    world.records[key][field] = value
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("field,value", [("command", "echo pass"), ("exit_code", 1), ("exit_code", False), ("source", {}), ("ended_at", "2040-01-01T00:00:00Z")])
def test_actual_output_must_match_command_revision_and_time(world, field, value):
    key = world.add("T007")
    world.outputs[key][field] = value
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("mutation", ["expired", "future", "revoked", "scope", "roles", "missing-human", "later-approval"])
def test_current_actual_authority(world, mutation):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    decision = v.decode(world.store.blob(binding["authority"]))
    if mutation == "expired": decision["valid_until"] = START
    if mutation == "future": decision["valid_from"] = "2030-02-01T00:00:00Z"
    if mutation == "later-approval": decision["valid_from"] = "2030-01-01T00:00:30Z"
    if mutation == "revoked": world.trust["revoked_authorities"].append(decision["id"])
    if mutation == "scope": decision["scope"]["customer"] = "foreign"
    if mutation == "roles": decision["roles"] = []
    if mutation == "missing-human": decision["owner"] = ""
    binding["authority"] = world.store.put(decision, "decisions/revised.json")
    world.records[key]["authority"] = binding["authority"]
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("missing", [("C-03",), ("C-07",), ("C-03", "C-07")])
def test_staging_preparation_requires_separate_preparation_and_spend_decisions(world, missing):
    key = world.add("T050")
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    for kind in missing:
        binding["decisions"].remove(kind)
        authority["decisions"].pop(kind)
    binding["authority"] = world.store.put(authority, "decisions/preparation-missing.json")
    world.records[key]["authority"] = binding["authority"]
    with pytest.raises(v.EvidenceError, match="staging preparation decisions incomplete"):
        world.check(key)


@pytest.mark.parametrize("kind", ["C-03", "C-07"])
@pytest.mark.parametrize("field", ["valid_from", "valid_until"])
@pytest.mark.parametrize("historical", [False, True])
def test_staging_preparation_decisions_cover_actual_execution(world, kind, field, historical):
    key = world.add("T050")
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    decision = v.decode(world.store.blob(authority["decisions"][kind]))
    output = world.outputs[key]
    decision[field] = shifted(output["started_at"], 1) if field == "valid_from" else output["ended_at"]
    authority["decisions"][kind] = world.store.put(decision, "decisions/preparation-invalid-period.json")
    binding["authority"] = world.store.put(authority, "decisions/preparation-invalid-authority.json")
    world.records[key]["authority"] = binding["authority"]
    if historical:
        admit_run(world, key)
    with pytest.raises(v.EvidenceError, match="earlier run|not current|retroactively authorize"):
        world.check(key)


def test_staging_preparation_with_separate_current_decisions_passes(world):
    key = world.add("T050")
    assert set(world.trust["bindings"][key]["decisions"]) == {"C-03", "C-07", "C-08"}
    world.check(key)


def test_dependencies_are_immutable_and_failed_predecessor_cannot_pass(world):
    key = world.add("T007")
    original = world.records[key]["dependencies"]["T006"]
    world.records[key]["dependencies"]["T006"] = world.review
    with pytest.raises(v.EvidenceError, match="dependency"): world.check(key)
    world.records[key]["dependencies"]["T006"] = original
    world.records["T006"]["verdict"] = "fail"
    world.publish("T006")
    world.records[key]["dependencies"]["T006"] = world.ref("T006")
    with pytest.raises(v.EvidenceError, match="failed/blocked"): world.check(key)


@pytest.mark.parametrize("field", ["cases", "dependencies", "command", "files", "source-owner"])
def test_trusted_manifest_cannot_waive_frozen_floor(world, field):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    if field == "cases": binding["cases"] = {}
    if field == "dependencies": binding["dependencies"] = {}
    if field == "command": binding["command"] = "echo pass"
    if field == "files": binding["files"] = ["scripts/unaccepted.py"]
    if field == "source-owner": binding["source"]["repository"] = "foreign/repo"
    with pytest.raises(v.EvidenceError): world.check(key)


def test_source_diff_must_stay_inside_exact_accepted_scope(world):
    key = world.add("T007")
    source = world.records[key]["source"]
    world.store.diffs[(source["repository"], source["revision"])].add(".github/workflows/pytest-suite.yml")
    with pytest.raises(v.EvidenceError, match="diff"): world.check(key)


@pytest.mark.parametrize("task", [f"T{i:03}" for i in range(1, 10)])
def test_bootstrap_requires_original_authenticated_output_not_new_receipt(world, task):
    key = world.add(task)
    world.records[key]["schema"] = "043-task-evidence-v1"
    with pytest.raises(v.EvidenceError, match="import kind"): world.check(key)
    world.records[key]["schema"] = "043-bootstrap-import-v1"
    world.publish(key)
    binding = world.trust["bindings"][key]
    binding["record"] = world.store.put(world.records[key], "evidence/" + task + ".json")
    with pytest.raises(v.EvidenceError, match="fabricated bootstrap"): world.verifier().verify(key)


def metric(world):
    key = world.add("T007")
    binding, output = world.trust["bindings"][key], world.outputs[key]
    binding["metrics"] = {"revocation": dict(minimum=0, maximum=10, unit="seconds", event="revoke")}
    output["events"] = dict(revoke=START)
    output["metrics"] = {"revocation": dict(value=5, unit="seconds", event="revoke")}
    return key, binding, output


@pytest.mark.parametrize("value", [True, False, -1, float("nan"), float("inf"), -float("inf"), "5", None, 11])
def test_numeric_finite_field_and_bound_rejections(world, value):
    key, _, output = metric(world)
    output["metrics"]["revocation"]["value"] = value
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("mutation", ["unit", "event", "missing", "boolean-limit", "nonfinite-limit", "negative-limit"])
def test_approved_metric_identity_and_limits(world, mutation):
    key, binding, output = metric(world)
    if mutation in ("unit", "event"): output["metrics"]["revocation"][mutation] = "wrong"
    if mutation == "missing": output["metrics"] = {}
    if mutation == "boolean-limit": binding["metrics"]["revocation"]["maximum"] = True
    if mutation == "nonfinite-limit": binding["metrics"]["revocation"]["maximum"] = float("inf")
    if mutation == "negative-limit": binding["metrics"]["revocation"]["minimum"] = -1
    with pytest.raises(v.EvidenceError): world.check(key)


def test_positive_metric_and_missing_monitoring_is_not_observed_time(world):
    key, binding, output = metric(world)
    binding["observation"] = dict(window=[START, END], max_gap_seconds=10, minimum_observed_seconds=50)
    output["coverage"] = dict(window=[START, END], intervals=[[START, "2030-01-01T00:00:25Z"], ["2030-01-01T00:00:30Z", END]])
    world.check(key)
    binding["observation"]["minimum_observed_seconds"] = 60
    with pytest.raises(v.EvidenceError, match="omitted monitoring"): world.check(key)


@pytest.mark.parametrize("intervals", [[], [[START, START]], [[START, END], [START, END]], [["2030-01-01T00:00:30Z", END]], [[START, "2030-01-01T00:00:20Z"]]])
def test_monitoring_gaps_overlap_and_omission(world, intervals):
    key, binding, output = metric(world)
    binding["observation"] = dict(window=[START, END], max_gap_seconds=5, minimum_observed_seconds=50)
    output["coverage"] = dict(window=[START, END], intervals=intervals)
    with pytest.raises(v.EvidenceError): world.check(key)


def test_denial_requires_actual_legitimate_control_and_neighbor(world):
    key = world.add("T007")
    name = TASKS[key]["cases"][0]
    binding = world.trust["bindings"][key]
    binding["cases"][name] = [dict(id="control", kind="equal", expected="allowed"), dict(id="neighbor", kind="equal", expected="available"),
                              dict(id="denial", kind="deny", expected="denied", control="control", neighbor="neighbor")]
    checks = [dict(id="control", observed="allowed"), dict(id="neighbor", observed="available"), dict(id="denial", observed="denied")]
    world.outputs[key]["cases"][0]["checks"] = checks
    world.check(key)
    checks[0]["observed"] = "denied"
    with pytest.raises(v.EvidenceError): world.check(key)
    checks[0]["observed"] = "allowed"
    checks[1]["observed"] = "missing"
    with pytest.raises(v.EvidenceError): world.check(key)


@pytest.mark.parametrize("mutation", ["wrong-head", "not-required", "no-collection", "skipped", "failed", "no-job"])
def test_required_ci_proves_actual_collection_exact_head_and_job(world, mutation):
    key = world.add("T010")
    suite = next(iter(world.outputs[key]["ci"].values()))
    if mutation == "wrong-head": suite["revision"] = "b" * 40
    if mutation == "not-required": suite["required"] = False
    if mutation == "no-collection": suite["collected"] = 0
    if mutation == "skipped": suite["skipped"] = 1
    if mutation == "failed": suite["conclusion"] = "failure"
    if mutation == "no-job": suite["job_id"] = 0
    with pytest.raises(v.EvidenceError): world.check(key)


def test_individual_child_advances_without_unrelated_aggregate(world):
    key = world.child("T058")
    world.child("T057", "other-offering")
    assert "T057" not in world.trust["aggregates"]
    world.check(key)
    data = world.aggregate("T057")
    world.verifier().aggregate("T057", data)
    bad = v.decode(data)
    del bad["children"]["other-offering"]
    with pytest.raises(v.EvidenceError, match="aggregate child|immutable reference"):
        world.verifier().aggregate("T057", json.dumps(bad).encode())


@pytest.mark.parametrize("task", ["T065", "T066"])
@pytest.mark.parametrize("inventory", ["complete", "missing-required"])
def test_handoff_cannot_select_one_child_instead_of_aggregate(world, task, inventory):
    child = world.child("T064")
    world.aggregate("T064")
    if inventory == "missing-required":
        world.child("T064", "required-second", {"profile": "another-required-profile"})
        with pytest.raises(v.EvidenceError, match="aggregate child"):
            world.verifier().verify("T064")
    key = world.add(task, dependencies={"T064": child})
    with pytest.raises(v.EvidenceError, match="requires aggregate"):
        world.check(key)


@pytest.mark.parametrize("task", ["T065", "T066"])
def test_handoff_accepts_complete_multiple_instance_aggregate(world, task):
    world.child("T064")
    world.child("T064", "required-second", {"profile": "another-required-profile"})
    world.aggregate("T064")
    key = world.add(task)
    world.check(key)


def test_canary_still_requires_complete_program_q2(world):
    key = world.child("T058")
    world.records["T056"]["verdict"] = "blocked"
    world.publish("T056")
    predecessor = "T057@service"
    world.records[predecessor]["dependencies"]["T056"] = world.ref("T056")
    world.publish(predecessor)
    world.records[key]["dependencies"]["T057"] = world.ref(predecessor)
    with pytest.raises(v.EvidenceError, match="failed/blocked"): world.check(key)


def test_child_cannot_borrow_foreign_offering_or_wave_authority(world):
    key = world.child("T058")
    world.child("T057", "foreign", {"profile": "other-profile"})
    world.trust["bindings"][key]["dependencies"]["T057"] = "T057@foreign"
    world.records[key]["dependencies"]["T057"] = world.ref("T057@foreign")
    with pytest.raises(v.EvidenceError, match="scope transition|foreign offering"): world.check(key)
    wave = world.child("T062", "wave", {"wave": "first-wave"}, decisions=["C-11"])
    with pytest.raises(v.EvidenceError, match="C-12"): world.check(wave)


def test_wave_requires_corresponding_previously_admitted_offer(world):
    key = world.child("T063", "wave", {"wave": "wave-1"}, decisions=["C-11", "C-12"])
    # Rejects the absent offer before any caller-selected output could grant it.
    with pytest.raises((v.EvidenceError, KeyError)): world.check(key)
    offer = world.child("T063", "offer")
    world.trust["bindings"][key]["offer_admission"] = offer
    move_live_observation(world, key, shifted(world.outputs[offer]["ended_at"], 60), shifted(world.outputs[offer]["ended_at"], 120))
    world.check(key)


def move_live_observation(world, key, start, end):
    output, binding = world.outputs[key], world.trust["bindings"][key]
    output.update(started_at=start, ended_at=end)
    if binding["observation"] is not None:
        output.update(events={"probe": start}, coverage=dict(window=[start, end], intervals=[[start, end]]))
        binding["observation"]["window"] = [start, end]
    world.publish(key)


@pytest.mark.parametrize("task", sorted(v.INSTANCE_TASKS))
@pytest.mark.parametrize("start,end", [
    ("2029-12-31T23:57:00Z", "2029-12-31T23:58:00Z"),
    ("2029-12-31T23:59:30Z", "2030-01-01T00:00:30Z"),
])
def test_each_production_child_rejects_incomplete_q2_at_execution(world, task, start, end):
    key = world.child(task)
    # Its predecessors retain valid times, so each selected child must enforce Q2 itself.
    move_live_observation(world, key, start, end)
    with pytest.raises(v.EvidenceError, match="Q2 acceptance must precede production execution"):
        world.check(key)


def refresh_dependency_records(world):
    """Republish synthetic immutable dependencies in their construction order."""
    for key, record in world.records.items():
        binding = world.trust["bindings"][key]
        record["dependencies"] = {dep: world.ref(selected) for dep, selected in binding["dependencies"].items()}
        world.publish(key)


@pytest.mark.parametrize("task", [f"T{i:03}" for i in range(50, 65)])
@pytest.mark.parametrize("timing", ["late-completion", "late-admission", "completion-boundary", "admission-boundary"])
def test_runtime_predecessor_acceptance_precedes_consuming_execution(world, task, timing):
    key = world.child(task) if task in v.INSTANCE_TASKS else world.add(task)
    deps = world.trust["bindings"][key]["dependencies"]
    predecessor = deps[max(deps)]
    start = world.outputs[key]["started_at"]
    if "completion" in timing:
        end = shifted(start, 30) if timing == "late-completion" else start
        move_live_observation(world, predecessor, shifted(end, -60), end)
    else:
        reviewed = shifted(start, 30) if timing == "late-admission" else start
        admit_run(world, predecessor, reviewed_at=reviewed, valid_from=world.outputs[predecessor]["ended_at"])
    refresh_dependency_records(world)
    if timing.startswith("late-"):
        with pytest.raises(v.EvidenceError, match="must precede.*execution"):
            world.check(key)
    else:
        world.check(key)


@pytest.mark.parametrize("task", sorted(v.INSTANCE_TASKS))
def test_each_production_child_rejects_late_q2_admission(world, task):
    key = world.child(task)
    admit_run(world, "T056", reviewed_at=shifted(world.outputs[key]["started_at"], 30),
              valid_from=world.outputs["T056"]["ended_at"])
    for predecessor in world.records:
        if predecessor != key and world.trust["bindings"][predecessor]["task"] in v.INSTANCE_TASKS:
            number = int(world.trust["bindings"][predecessor]["task"][1:])
            move_live_observation(world, predecessor, shifted(START, 7200 + number * 120), shifted(END, 7200 + number * 120))
    refresh_dependency_records(world)
    with pytest.raises(v.EvidenceError, match="Q2 acceptance must precede production execution"):
        world.check(key)


@pytest.mark.parametrize("task", sorted(v.INSTANCE_TASKS))
@pytest.mark.parametrize("admitted", [False, True])
def test_each_production_child_accepts_prior_q2(world, task, admitted):
    key = world.child(task)
    if admitted:
        admit_run(world, "T056", reviewed_at=world.outputs["T056"]["ended_at"], valid_from=world.outputs["T056"]["ended_at"])
        refresh_dependency_records(world)
    world.check(key)


@pytest.mark.parametrize("offset", [60, -30])
def test_wave_rejects_later_or_overlapping_offer_execution(world, offset):
    wave = world.child("T063", "wave", {"wave": "wave-1"})
    offer = world.child("T063", "offer")
    world.trust["bindings"][wave]["offer_admission"] = offer
    offer_start = shifted(world.outputs[wave]["started_at"], offset)
    move_live_observation(world, offer, offer_start, shifted(offer_start, 60))
    with pytest.raises(v.EvidenceError, match="offer admission must precede wave execution"):
        world.check(wave)


def test_wave_rejects_later_human_admission_even_when_offer_execution_finished_earlier(world):
    wave = world.child("T063", "wave", {"wave": "wave-1"})
    offer = world.child("T063", "offer")
    world.trust["bindings"][wave]["offer_admission"] = offer
    move_live_observation(world, wave, shifted(world.outputs[offer]["ended_at"], 60), shifted(world.outputs[offer]["ended_at"], 120))
    admit_run(world, offer)
    world.publish(offer)
    with pytest.raises(v.EvidenceError, match="offer admission must precede wave execution"):
        world.check(wave)


def test_wave_accepts_offer_with_actual_admission_before_execution(world):
    wave = world.child("T063", "wave", {"wave": "wave-1"})
    offer = world.child("T063", "offer")
    world.trust["bindings"][wave]["offer_admission"] = offer
    move_live_observation(world, wave, shifted(world.outputs[offer]["ended_at"], 180), shifted(world.outputs[offer]["ended_at"], 240))
    admit_run(world, offer)
    world.publish(offer)
    world.check(wave)


def test_source_only_custody_and_source_authority_do_not_admit_live_observations(world):
    key = world.child("T057", scope_changes={"phase": "production"})
    del world.trust["live_custody"]
    with pytest.raises(v.EvidenceError): world.check(key)


def test_failed_history_requires_reviewed_remediation_and_fresh_resume(world):
    key = world.add("T007")
    failed = deepcopy(world.records[key]); failed.update(verdict="fail", attempt="earlier")
    history = [world.store.put(failed, "history/earlier.json")]
    world.records[key]["history"] = history
    world.trust["bindings"][key]["history"] = history
    with pytest.raises((v.EvidenceError, KeyError)): world.check(key)


@pytest.mark.parametrize("path", ["../secret", "/etc/passwd", "a/../b", "a//b", "./a", "a\\b", "C:/secret", "a/./b"])
def test_reference_path_traversal_rejected(path):
    with pytest.raises(v.EvidenceError): v.relative(path)


def test_duplicate_json_and_nonfinite_json_rejected():
    for data in (b'{"verdict":"fail","verdict":"pass"}', b'{"value":NaN}', b'{"value":Infinity}', b'{"value":1e999}'):
        with pytest.raises(v.EvidenceError): v.decode(data)


def test_immutable_digest_and_unreviewed_input_rejected(world):
    key = world.add("T007")
    verifier = world.verifier()
    with pytest.raises(v.EvidenceError, match="independently reviewed"):
        verifier.verify(key, b'{"verdict":"pass"}')
    ref = world.trust["bindings"][key]["record"]
    ref["sha256"] = "0" * 64
    with pytest.raises(v.EvidenceError, match="digest"):
        world.verifier().verify(key)


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=True)
    return result.stdout.decode().strip()


def test_git_store_reads_immutable_blob_and_rejects_symlink(tmp_path):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Synthetic Test")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    git(tmp_path, "remote", "add", "origin", "https://github.com/Opensoft/openXfactory.git")
    (tmp_path / "output").write_bytes(b"actual committed bytes")
    (tmp_path / "link").symlink_to("output")
    git(tmp_path, "add", "output", "link")
    git(tmp_path, "commit", "-qm", "synthetic fixture")
    revision = git(tmp_path, "rev-parse", "HEAD")
    ref = dict(repository=v.COORDINATOR, commit=revision, path="output", sha256=v.digest(b"actual committed bytes"))
    before = git(tmp_path, "status", "--porcelain=v1")
    store = v.GitStore({v.COORDINATOR: tmp_path})
    assert store.blob(ref) == b"actual committed bytes"
    with pytest.raises(v.EvidenceError, match="symlink"):
        store.blob(dict(ref, path="link"))
    assert git(tmp_path, "status", "--porcelain=v1") == before
    with pytest.raises(v.EvidenceError, match="origin"):
        v.GitStore({"other/repo": tmp_path})


def test_source_authentication_uses_distinct_real_git_commits_read_only(tmp_path):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Synthetic Test")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    git(tmp_path, "remote", "add", "origin", "https://github.com/opensoft/openXfactory.git")
    def commit(path, data):
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        raw = data if isinstance(data, bytes) else v.canonical_json(data)
        target.write_bytes(raw)
        git(tmp_path, "add", path)
        git(tmp_path, "commit", "-qm", "synthetic commissioning revision")
        return dict(repository=v.COORDINATOR, commit=git(tmp_path, "rev-parse", "HEAD"),
                    path=path, sha256=v.digest(raw))
    def review_bytes(data):
        fence = bytes([96]) * 3
        return fence + b"json\n" + v.canonical_json(data) + b"\n" + fence + b"\n"
    review = dict(schema="043-source-authentication-v1", decision="pending", custodian="Brett Heap",
                  reviewed_manifest=None, content_sha256=None, reviewed_at=None)
    trust = World().trust
    trust["review"] = commit(v.AUTHENTICATION_PATH, review_bytes(review))
    trust["source_container"] = dict(schema="043-source-container-v1",
        objects={"original": dict(tasks=["T007"], evidence_class="source", value={"original": "synthetic bytes"})})
    first = commit(v.COMMISSIONING_PATH, trust)
    review.update(decision="accepted", reviewed_manifest=first, content_sha256=v.commissioning_digest(trust),
                  reviewed_at="2030-01-01T01:00:00Z")
    auth = commit(v.AUTHENTICATION_PATH, review_bytes(review))
    trust["review"] = auth
    final = commit(v.COMMISSIONING_PATH, trust)
    before = git(tmp_path, "status", "--porcelain=v1")
    reader = v.Verifier(TASKS, v.GitStore({v.COORDINATOR: tmp_path}), final, now=NOW)
    assert reader.authenticated
    assert len({first["commit"], auth["commit"], final["commit"]}) == 3
    assert git(tmp_path, "status", "--porcelain=v1") == before


def test_verifier_never_executes_evidence_commands_or_writes(world, monkeypatch):
    key = world.add("T007")
    def forbidden(*args, **kwargs):
        pytest.fail("verifier attempted a mutation or owner command")
    monkeypatch.setattr(subprocess, "run", forbidden)
    monkeypatch.setattr(Path, "write_bytes", forbidden)
    monkeypatch.setattr(Path, "write_text", forbidden)
    verifier = world.verifier()
    before = deepcopy(world.store.objects)
    verifier.verify(key)
    assert world.store.objects == before


def test_cli_fails_closed_without_custody_anchor(tmp_path):
    result = subprocess.run(["python3", str(MODULE), "--task", "T007", str(tmp_path / "invented.json")],
                            capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"})
    assert result.returncode == 1
    assert "PC_EVIDENCE_TRUST is required" in result.stderr


def synthetic_t023_proof(repo, revision, run_id, job_id, scope):
    sha = "b" * 64
    summary = {name: sha for name in v.T023_DIGESTS}
    criteria = {
        "new_reliability_rating": {"state": "automatic-pass", "new": 0},
        "new_maintainability_rating": {"state": "automatic-pass", "new": 0},
        "new_security_rating": {"state": "independent-review-required", "new_ruff": 0},
        "new_security_hotspots_reviewed": {"state": "independent-review-required", "subjects_sha256": sha},
        "new_coverage": {"state": "automatic-pass", "hit": 80, "possible": 100},
        "new_duplicated_lines_density": {"state": "automatic-pass", "hit": 3, "possible": 100},
    }
    summary.update(schema="043-t023-local-quality-v1", repository=repo, repository_id=1452848226,
                   source_revision=revision, baseline=v.T023_BASE, criteria=criteria, released=False, runtime_qualified=False,
                   owner_suite={"count": 171, "sha256": sha}, guarded_suite={"count": 49, "sha256": sha})
    guard = dict(inventory_sha256=sha, subjects_sha256=sha, discovery=["ruff", "independent-boundary-review"],
                 total=0, reviewed=0)
    review = dict(schema="043-t023-quality-review-v1", reviewer="Independent Reviewer", implementer="Implementer",
                  approved=True, summary_sha256=v.digest(v.canonical_json(summary)), source_revision=revision,
                  criteria={name: "accepted" for name in v.T023_METRICS}, security_unresolved=0, guard_identity="verified-source-budget",
                  zero_charge_guard_verified=True, ci_compute_usd=0, ci_artifact_storage_usd=0,
                  hotspots=guard, run_id=run_id, job_id=job_id, reviewed_at=START)
    review_sha = v.digest(v.canonical_json(review))
    readback = dict(schema="043-t023-release-readback-v1", published=True, draft=False, repository=repo, tag="reviewed-tag",
                    tag_commit=revision, source_revision=revision, review_sha256=review_sha, release_id=333,
                    artifact=dict(id=444, name="immutable-package", sha256=sha), published_at=END,
                    observed_at=shifted(END, 1), provenance=dict(repository=repo, commit=revision,
                    path="release/private-connectivity-production.json", sha256=sha))
    approval = dict(kind="package-release-publication", decision="accepted", source_revision=revision,
                    tag=readback["tag"], review_sha256=review_sha, owner="Package Owner", approved_at=START,
                    id="synthetic-T023-publication", scope=deepcopy(scope), valid_from=START, valid_until=shifted(END, 2))
    proof = dict(summary=summary, review=review, readback=readback, authorization="selected-source-decision")
    return proof, approval


def assert_t023_release_boundary():
    revision, repo = "a" * 40, v.FIXED_REPOSITORIES["L"]
    world = World()
    key = world.add("T023")
    scope = world.trust["bindings"][key]["scope"]
    proof, approval = synthetic_t023_proof(repo, revision, 111, 222, scope)
    review, criteria = proof["review"], proof["summary"]["criteria"]
    guard = review["hotspots"]
    reader = world.verifier()
    reader.store = SimpleNamespace(blob=lambda ref: b"source inventory")
    reader.read = lambda ref, binding: approval
    runs = {name: {"run_id": 111, "job_id": 222, "revision": revision} for name in v.T023_CI}
    binding = dict(task="T023", scope=scope, source={"repository": repo, "revision": revision},
                   ci={"package-owner-qualification": 171, "package-production-runner": 49},
                   admission="selected-actual-admission")

    def check(candidate):
        selected = {**binding, "t023_release_sha256": v.digest(v.canonical_json(candidate))}
        v.Verifier.t023_release(reader, {"t023_release": candidate, "ci": runs}, selected)

    with pytest.raises(v.EvidenceError, match="release readback required"):
        v.Verifier.t023_release(reader, {"ci": runs}, binding)
    check(proof)
    for field, value, message in (
        ("baseline", revision, "immutable baseline"),
        ("source_revision", "c" * 40, "candidate"),
        ("criteria", {key: item for key, item in criteria.items() if key != "new_security_rating"}, "criteria"),
    ):
        altered = deepcopy(proof)
        altered["summary"][field] = value
        with pytest.raises(v.EvidenceError, match=message):
            check(altered)
    for field, value, message in (
        ("zero_charge_guard_verified", False, "zero-charge"),
        ("hotspots", {**guard, "discovery": ["ruff"]}, "hotspot review incomplete"),
        ("reviewer", review["implementer"], "independent"),
    ):
        altered = deepcopy(proof)
        altered["review"][field] = value
        with pytest.raises(v.EvidenceError, match=message):
            check(altered)
    altered = deepcopy(proof)
    altered["readback"]["tag_commit"] = "c" * 40
    with pytest.raises(v.EvidenceError, match="readback differs"):
        check(altered)
    for field, value, message in (
        ("kind", "C-01", "required decision is not accepted"),
        ("valid_until", END, "authority cannot retroactively authorize effects"),
        ("valid_from", shifted(END, 1), "authority cannot retroactively authorize effects"),
        ("owner", "Codex", "distinct delegated decision actor required"),
        ("scope", {**scope, "environment": "other"}, "required decision scope mismatch"),
    ):
        original = approval[field]
        approval[field] = value
        with pytest.raises(v.EvidenceError, match=message):
            check(proof)
        approval[field] = original
    reader.trust["revoked_authorities"].append(approval["id"])
    with pytest.raises(v.EvidenceError, match="revoked authority without completion closure"):
        check(proof)


def test_registry_has_all_68_tasks_and_current_freeze():
    assert set(TASKS) == {f"T{i:03}" for i in range(1, 69)}
    assert all(set(d["dependencies"]) < set(TASKS) for d in TASKS.values())
    assert TASKS["T057"]["dependencies"] == ["T056"]
    assert TASKS["T050"]["dependencies"][-1] == "T049"
    assert TASKS["T023"]["dependencies"] == ["T021", "T022"]
    assert TASKS["T023"]["class"] == "release-L"
    assert len(TASKS["T023"]["files"]) == 15
    assert "packaging/production-images.json" in TASKS["T023"]["files"]
    assert_t023_release_boundary()


@pytest.mark.parametrize("mode", ["managed-pull", "managed-push", "customer"])
def test_authorized_channels_and_missing_or_expired_carriers(world, mode):
    key = world.child("T058")
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    authority["mode"] = mode
    fields = ["consent"] if mode == "customer" else ["request", "grant" if mode == "managed-push" else "reviewed_merge"]
    for field in fields:
        authority[field] = world.decision(field, binding["scope"])
    binding["authority"] = world.store.put(authority, "decisions/channel.json")
    world.records[key]["authority"] = binding["authority"]
    world.check(key)
    bad = v.decode(world.store.blob(authority[fields[-1]]))
    bad["valid_until"] = START
    authority[fields[-1]] = world.store.put(bad, "decisions/expired-carrier.json")
    binding["authority"] = world.store.put(authority, "decisions/expired-channel.json")
    world.records[key]["authority"] = binding["authority"]
    with pytest.raises(v.EvidenceError, match="not current"): world.check(key)


def prepare_managed_attachment(world, task, offering):
    key = world.child(task, "domain", {"offering": offering})
    service = world.child(task, "service")
    for child, binding in world.trust["bindings"].items():
        if binding["instance"] == "domain":
            binding["eligibility"] = binding["task"] + "@service"
            output = world.outputs[child]
            move_live_observation(world, child, shifted(output["started_at"], 60), shifted(output["ended_at"], 60))
    refresh_dependency_records(world)
    return key, service


@pytest.mark.parametrize("task", sorted(v.INSTANCE_TASKS))
@pytest.mark.parametrize("offering", ["local-managed", "hosted-domain"])
@pytest.mark.parametrize("timing", ["late-completion", "late-admission", "admission-boundary"])
def test_managed_service_eligibility_precedes_each_attachment(world, task, offering, timing):
    key, service = prepare_managed_attachment(world, task, offering)
    world.check(key)  # Actual service completion is exactly at attachment start.
    start = world.outputs[key]["started_at"]
    if timing == "late-completion":
        move_live_observation(world, service, shifted(start, -30), shifted(start, 30))
    else:
        reviewed = shifted(start, 30) if timing == "late-admission" else start
        admit_run(world, service, reviewed_at=reviewed, valid_from=start)
    refresh_dependency_records(world)
    if timing.startswith("late-"):
        with pytest.raises(v.EvidenceError, match="eligibility must precede attachment execution"):
            world.check(key)
    else:
        world.check(key)


@pytest.mark.parametrize("offering", ["local-managed", "hosted-domain"])
def test_managed_attachment_needs_service_eligible_for_same_phase_and_scope(world, offering):
    key = world.child("T058", "domain", {"offering": offering})
    with pytest.raises((v.EvidenceError, KeyError)): world.check(key)
    key, service = prepare_managed_attachment(world, "T058", offering)
    world.check(key)
    foreign = world.child("T058", "foreign", {"customer": "another-customer"})
    world.trust["bindings"][key]["eligibility"] = foreign
    with pytest.raises(v.EvidenceError, match="phase/scope"): world.check(key)


def test_explicit_reviewed_scope_transition_allows_new_cohort_without_borrowing(world):
    key = world.child("T062", "offer", {"customer": "new-cohort"})
    old = world.child("T061", "canary", {"customer": "internal-canary"})
    binding = world.trust["bindings"][key]
    binding["dependencies"]["T061"] = old
    world.records[key]["dependencies"]["T061"] = world.ref(old)
    with pytest.raises(v.EvidenceError, match="scope transition"): world.check(key)
    binding["transitions"] = {"T061": deepcopy(world.trust["bindings"][old]["scope"])}
    world.check(key)


@pytest.mark.parametrize("field", ["scope", "source"])
def test_case_cannot_import_foreign_observations(world, field):
    key = world.add("T007")
    world.outputs[key]["cases"][0][field] = {}
    with pytest.raises(v.EvidenceError, match="mixed case"): world.check(key)


def test_mixed_staging_runs_and_changed_canary_candidates_rejected(world):
    key = world.add("T056")
    world.trust["bindings"]["T052"]["scope"]["run"] = "other-run"
    with pytest.raises(v.EvidenceError, match="mixed staging run"): world.check(key)
    world.trust["bindings"]["T052"]["scope"]["run"] = "synthetic-run"
    canary = world.child("T057", scope_changes={"candidate": "untested-candidate"})
    with pytest.raises(v.EvidenceError, match="candidate changed"): world.check(canary)


def test_source_classes_cannot_be_relabelled_staging_or_production(world):
    key = world.add("T007")
    world.trust["bindings"][key]["scope"]["phase"] = "production"
    with pytest.raises(v.EvidenceError, match="evidence phase"): world.check(key)


def test_real_cli_reads_committed_evidence_and_leaves_tree_unchanged(tmp_path):
    import os
    import shutil
    target = tmp_path / v.FEATURE_PATH
    shutil.copytree(ROOT / v.FEATURE_PATH, target, ignore=shutil.ignore_patterns("__pycache__", "tests"))
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Synthetic Test")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    git(tmp_path, "remote", "add", "origin", "https://github.com/opensoft/openXfactory.git")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "synthetic source")
    revision = git(tmp_path, "rev-parse", "HEAD")
    world = World(); key = world.add("T001")
    binding, record, output = world.trust["bindings"][key], world.records[key], world.outputs[key]
    source = dict(repository=v.COORDINATOR, base=revision, revision=revision)
    for value in (binding, record, output): value["source"] = source
    for case in output["cases"]: case["source"] = source
    output.update(started_at="2020-01-01T00:00:00Z", ended_at="2020-01-01T00:01:00Z")
    authority = v.decode(world.store.blob(binding["authority"]))
    authority.update(valid_from="2019-01-01T00:00:00Z", valid_until="2100-01-01T00:00:00Z")
    binding["authority"] = world.store.put(authority, "decisions/long-lived-source.json")
    record["authority"] = binding["authority"]
    artifact = v.FEATURE_PATH + "/checklists/requirements.md"
    binding["artifacts"] = record["artifacts"] = [dict(repository=v.COORDINATOR, commit=revision, path=artifact, sha256=v.digest((tmp_path / artifact).read_bytes()))]
    # Export actual fixture objects, commit each layer, and rebind references to
    # their real Git commits. Source and receipt commits are deliberately distinct.
    def export(data, path):
        destination = tmp_path / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        git(tmp_path, "add", path)
        git(tmp_path, "commit", "-qm", "synthetic reviewed export")
        return dict(repository=v.COORDINATOR, commit=git(tmp_path, "rev-parse", "HEAD"), path=path, sha256=v.digest(data))
    binding["authority"] = record["authority"] = export(json.dumps(authority).encode(), "decisions/source.json")
    record["output"] = export(json.dumps(output).encode(), "outputs/T001.json")
    binding["record"] = export(json.dumps(record).encode(), "exports/T001.import.json")
    world.trust["review"] = export(b"SYNTHETIC independently reviewed fixture", "reviews/fixture.txt")
    trust_ref = export(json.dumps(world.trust).encode(), "commissioning/fixture.json")
    environment = {name: value for name, value in os.environ.items() if not name.startswith("PC_EVIDENCE_")}
    environment.update(PC_EVIDENCE_TRUST=trust_ref["commit"] + ":" + trust_ref["path"], PC_EVIDENCE_TRUST_SHA256=trust_ref["sha256"])
    before = git(tmp_path, "status", "--porcelain=v1")
    result = subprocess.run(["python3", str(target / "verify-evidence.py"), "--task", key, str(tmp_path / binding["record"]["path"])],
                            capture_output=True, text=True, env=environment)
    assert result.returncode == 0, result.stderr
    assert "structurally verified" in result.stdout
    assert git(tmp_path, "status", "--porcelain=v1") == before


def test_failed_attempts_are_preserved_with_reviewed_reruns_and_fresh_resume(world):
    key = world.add("T007")
    binding, record = world.trust["bindings"][key], world.records[key]
    earlier = deepcopy(record); earlier.update(verdict="blocked", attempt="prior-attempt")
    binding["history"] = record["history"] = [world.store.put(earlier, "history/blocked.json")]
    binding["decisions"] = ["C-13"]
    reruns = [record["output"]]
    decision = v.decode(world.store.blob(world.decision("C-13", binding["scope"])))
    decision["reruns"] = reruns
    authority = v.decode(world.store.blob(binding["authority"]))
    authority["decisions"] = {"C-13": world.store.put(decision, "decisions/resume-reruns.json")}
    resumed = world.store.put(authority, "decisions/fresh-resume.json")
    binding["authority"] = record["authority"] = binding["remediation"] = record["remediation"] = resumed
    binding["resume_outputs"] = reruns
    world.check(key)
    binding["resume_outputs"] = []
    with pytest.raises(v.EvidenceError, match="rerun"): world.check(key)


def test_incidents_cannot_be_omitted_and_need_reviewed_closure(world):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    closure = v.decode(world.store.blob(world.decision("incident-closure", binding["scope"])))
    closure["reruns"] = [world.records[key]["output"]]
    ref = world.store.put(closure, "incidents/closed.json")
    binding["incidents"] = [ref]
    with pytest.raises(v.EvidenceError, match="incident history"): world.check(key)
    world.records[key]["incidents"] = [ref]
    world.check(key)


def test_self_verification_is_not_exact_ci_or_owner_execution(world):
    key = world.add("T010")
    world.trust["bindings"][key]["command"] = TASKS[key]["command"]
    with pytest.raises(v.EvidenceError, match="self-verification"): world.check(key)


def test_frozen_definitions_reject_changed_task_command(tmp_path):
    import shutil
    target = tmp_path / v.FEATURE_PATH
    shutil.copytree(ROOT / v.FEATURE_PATH, target, ignore=shutil.ignore_patterns("__pycache__", "tests"))
    task_path = target / "tasks.md"
    task_path.write_text(task_path.read_text().replace("cases=frozen-cases,", "cases=caller-cases,"))
    with pytest.raises(v.EvidenceError, match="unreviewed"):
        v.load_contract(tmp_path)


def test_manifest_cannot_substitute_fixed_component_owner(world):
    world.add("T007")
    world.trust["repositories"]["L"] = "other/headscale"
    with pytest.raises(v.EvidenceError, match="canonical component owner"):
        world.verifier()


def test_aggregate_permits_only_reviewed_inventory_metadata(world):
    world.child("T057")
    record = v.decode(world.aggregate("T057"))
    record["pin_inventory"] = []
    original = world.trust["aggregates"]["T057"]
    world.trust["aggregates"]["T057"] = world.store.put(record, original["path"], original["repository"])
    world.verifier().aggregate("T057", world.store.blob(world.trust["aggregates"]["T057"]))
    record["caller_waiver"] = True
    world.trust["aggregates"]["T057"] = world.store.put(record, original["path"], original["repository"])
    with pytest.raises(v.EvidenceError, match="aggregate child"):
        world.verifier().aggregate("T057", world.store.blob(world.trust["aggregates"]["T057"]))


def completed_run(world, key, mode="managed-push"):
    """Synthetic grants close after the original run, never actual authority."""
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    authority["mode"] = mode
    end = world.outputs[key]["ended_at"]
    fields = ["consent"] if mode == "customer" else ["request", "grant" if mode == "managed-push" else "reviewed_merge"]
    for field in fields:
        carrier = v.decode(world.store.blob(world.decision(field, binding["scope"])))
        carrier["valid_until"] = shifted(end, 60)
        authority[field] = world.store.put(carrier, "closed/" + field + ".json")
        if field == "grant":
            world.trust["revoked_authorities"].append(carrier["id"])
            closure = dict(kind="authority-closure", authority_id=carrier["id"], scope=binding["scope"],
                           closed_at=shifted(end, 1), disposition="completed", owner="Synthetic Ops Owner")
            world.trust.setdefault("completed_authorities", {})[carrier["id"]] = world.store.put(closure, "closed/proof.json")
    authority["valid_until"] = shifted(end, 60)
    binding["authority"] = world.store.put(authority, "closed/authority.json")
    world.records[key]["authority"] = binding["authority"]
    return binding


def admit_run(world, key, **changes):
    binding = world.trust["bindings"][key]
    world.publish(key)
    end = world.outputs[key]["ended_at"]
    admission = dict(kind="evidence-admission", id="admission-" + key, decision="accepted",
                     scope=binding["scope"], owner="Synthetic Evidence Owner", roles=["synthetic-evidence-owner"],
                     authority=binding["authority"], reviewed_output_sha256=world.records[key]["output"]["sha256"],
                     reviewed_at=shifted(end, 120), valid_from=shifted(end, 60),
                     valid_until="2031-01-01T00:00:00Z")
    admission.update(changes)
    binding["admission_roles"] = ["synthetic-evidence-owner"]
    binding["admission"] = world.store.put(admission, "reviews/" + key + ".json")
    world.records[key]["admission"] = binding["admission"]
    return admission


@pytest.mark.parametrize("mode", ["managed-push", "managed-pull", "customer"])
def test_completed_execution_uses_current_independent_admission(world, mode):
    key = world.child("T058")
    completed_run(world, key, mode)
    admit_run(world, key)
    world.check(key)


def test_expired_execution_without_admission_stays_rejected(world):
    key = world.child("T058")
    completed_run(world, key)
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("changes", [
    {"valid_until": START}, {"reviewed_at": START}, {"reviewed_at": "2040-01-01T00:00:00Z"},
    {"roles": []}, {"owner": ""}, {"decision": "rejected"}, {"kind": "request"},
    {"reviewed_output_sha256": "f" * 64}, {"authority": {}},
])
def test_independent_admission_cannot_waive_scope_time_roles_or_output(world, changes):
    key = world.child("T058")
    completed_run(world, key)
    admit_run(world, key, **changes)
    with pytest.raises(v.EvidenceError):
        world.check(key)


def test_admission_must_have_exact_scope_and_reviewed_record_reference(world):
    key = world.child("T058")
    completed_run(world, key)
    scope = deepcopy(world.trust["bindings"][key]["scope"])
    scope["site"] = "foreign-site"
    admit_run(world, key, scope=scope)
    with pytest.raises(v.EvidenceError):
        world.check(key)
    admit_run(world, key)
    world.records[key].pop("admission")
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("changes", [
    {"valid_until": START}, {"valid_until": END}, {"valid_from": END},
])
def test_admission_does_not_retroactively_authorize_execution(world, changes):
    key = world.child("T058")
    binding = completed_run(world, key)
    authority = v.decode(world.store.blob(binding["authority"]))
    authority.update({field: world.outputs[key]["started_at" if value == START else "ended_at"]
                      for field, value in changes.items()})
    binding["authority"] = world.store.put(authority, "closed/invalid-period.json")
    world.records[key]["authority"] = binding["authority"]
    admit_run(world, key)
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("mutation", ["missing", "early", "foreign", "rejected", "other-authority", "future"])
def test_post_run_revocation_needs_authenticated_completion_closure(world, mutation):
    key = world.child("T058")
    completed_run(world, key)
    admit_run(world, key)
    closures = world.trust["completed_authorities"]
    identity, ref = next(iter(closures.items()))
    proof = v.decode(world.store.blob(ref))
    if mutation == "missing":
        closures.pop(identity)
    else:
        if mutation == "early": proof["closed_at"] = START
        if mutation == "future": proof["closed_at"] = "2040-01-01T00:00:00Z"
        if mutation == "foreign": proof["scope"] = {**proof["scope"], "customer": "foreign"}
        if mutation == "rejected": proof["disposition"] = "incident"
        if mutation == "other-authority": proof["authority_id"] = "another"
        closures[identity] = world.store.put(proof, "closed/invalid-proof.json")
    with pytest.raises(v.EvidenceError):
        world.check(key)


def test_admission_cannot_reuse_closed_grant_for_a_new_operation(world):
    key = world.child("T058")
    binding = completed_run(world, key)
    admit_run(world, key)
    world.check(key)
    verifier = world.verifier()
    with pytest.raises(v.EvidenceError):
        verifier.authority(binding["authority"], binding)


def test_current_admission_is_rechecked_for_cached_evidence(world):
    key = world.child("T058")
    completed_run(world, key)
    admission = admit_run(world, key)
    world.publish(key)
    verifier = world.verifier()
    verifier.verify(key)
    verifier.trust["revoked_authorities"].append(admission["id"])
    with pytest.raises(v.EvidenceError, match="revoked"):
        verifier.verify(key)


@pytest.mark.parametrize("mutation", ["during-run", "source-mode", "changed-output", "uncommissioned-admission"])
def test_historical_admission_keeps_execution_and_content_floors(world, mutation):
    key = world.child("T058")
    binding = completed_run(world, key)
    if mutation in ("during-run", "source-mode"):
        authority = v.decode(world.store.blob(binding["authority"]))
        if mutation == "during-run":
            grant = v.decode(world.store.blob(authority["grant"]))
            grant["valid_until"] = END
            authority["grant"] = world.store.put(grant, "closed/early-expiry.json")
        else:
            authority["mode"] = "source"
        binding["authority"] = world.store.put(authority, "closed/invalid-execution.json")
        world.records[key]["authority"] = binding["authority"]
    admit_run(world, key)
    if mutation == "changed-output":
        world.outputs[key]["exit_code"] = 1
    if mutation == "uncommissioned-admission":
        binding.pop("admission")
    with pytest.raises(v.EvidenceError):
        world.check(key)


def test_source_scope_approval_can_last_until_superseded(world):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    authority["valid_until"] = "until-superseded"
    binding["authority"] = world.store.put(authority, "decisions/source-lifetime.json")
    world.records[key]["authority"] = binding["authority"]
    world.check(key)
    world.trust["revoked_authorities"].append(authority["id"])
    with pytest.raises(v.EvidenceError, match="revoked"):
        world.check(key)


def test_source_admission_can_persist_without_reopening_completed_grants(world):
    key = world.add("T007")
    binding = completed_run(world, key)
    admission = admit_run(world, key, valid_until="until-superseded")
    world.check(key)
    with pytest.raises(v.EvidenceError):
        world.verifier().authority(binding["authority"], binding)
    world.trust["revoked_authorities"].append(admission["id"])
    with pytest.raises(v.EvidenceError, match="revoked"):
        world.check(key)


def test_source_custody_decision_can_last_until_superseded(world):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    binding["decisions"] = ["C-08"]
    authority = v.decode(world.store.blob(binding["authority"]))
    decision = v.decode(world.store.blob(world.decision("C-08", binding["scope"])))
    decision["valid_until"] = "until-superseded"
    authority["decisions"] = {"C-08": world.store.put(decision, "decisions/source-custody.json")}
    binding["authority"] = world.store.put(authority, "decisions/source-custody-authority.json")
    world.records[key]["authority"] = binding["authority"]
    world.check(key)
    world.trust["revoked_authorities"].append(decision["id"])
    with pytest.raises(v.EvidenceError, match="revoked"):
        world.check(key)


@pytest.mark.parametrize("field", ["authority", "grant", "request", "decision", "admission"])
def test_live_authority_and_admission_require_finite_validity(world, field):
    key = world.child("T058")
    binding = completed_run(world, key)
    authority = v.decode(world.store.blob(binding["authority"]))
    if field == "admission":
        admit_run(world, key, valid_until="until-superseded")
    else:
        if field == "authority":
            authority["valid_until"] = "until-superseded"
        else:
            ref = authority["decisions"]["C-09"] if field == "decision" else authority[field]
            value = v.decode(world.store.blob(ref))
            value["valid_until"] = "until-superseded"
            updated = world.store.put(value, "decisions/live-unbounded.json")
            if field == "decision": authority["decisions"]["C-09"] = updated
            else: authority[field] = updated
        binding["authority"] = world.store.put(authority, "decisions/live-unbounded-authority.json")
        world.records[key]["authority"] = binding["authority"]
        admit_run(world, key)
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("mode", ["managed-push", "managed-pull", "customer"])
def test_source_phase_does_not_make_execution_channels_unbounded(world, mode):
    key = world.add("T007")
    binding = completed_run(world, key, mode)
    authority = v.decode(world.store.blob(binding["authority"]))
    authority["valid_until"] = "until-superseded"
    binding["authority"] = world.store.put(authority, "decisions/unbounded-source-channel.json")
    world.records[key]["authority"] = binding["authority"]
    admit_run(world, key)
    with pytest.raises(v.EvidenceError):
        world.check(key)


def test_source_lifetime_cannot_authorize_a_run_before_approval(world):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    authority = v.decode(world.store.blob(binding["authority"]))
    authority.update(valid_from=END, valid_until="until-superseded")
    binding["authority"] = world.store.put(authority, "decisions/late-source-approval.json")
    world.records[key]["authority"] = binding["authority"]
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("mode", ["managed-push", "managed-pull", "customer"])
def test_source_policy_lifetime_is_independent_of_finite_execution_channel(world, mode):
    key = world.add("T007")
    binding = completed_run(world, key, mode)
    binding["decisions"] = ["C-08"]
    authority = v.decode(world.store.blob(binding["authority"]))
    policy = v.decode(world.store.blob(world.decision("C-08", binding["scope"])))
    policy["valid_until"] = "until-superseded"
    authority["decisions"] = {"C-08": world.store.put(policy, "decisions/source-policy.json")}
    binding["authority"] = world.store.put(authority, "decisions/source-policy-channel.json")
    world.records[key]["authority"] = binding["authority"]
    admit_run(world, key, valid_until="until-superseded")
    world.check(key)


@pytest.mark.parametrize("mode,field", [
    ("managed-push", "request"), ("managed-push", "grant"),
    ("managed-pull", "request"), ("managed-pull", "reviewed_merge"),
    ("customer", "consent"),
])
def test_source_policy_never_makes_request_grant_or_consent_unbounded(world, mode, field):
    key = world.add("T007")
    binding = completed_run(world, key, mode)
    authority = v.decode(world.store.blob(binding["authority"]))
    carrier = v.decode(world.store.blob(authority[field]))
    carrier["valid_until"] = "until-superseded"
    authority[field] = world.store.put(carrier, "decisions/unbounded-carrier.json")
    binding["authority"] = world.store.put(authority, "decisions/source-unbounded-carrier.json")
    world.records[key]["authority"] = binding["authority"]
    admit_run(world, key, valid_until="until-superseded")
    with pytest.raises(v.EvidenceError):
        world.check(key)


def test_source_wrapper_cannot_make_a_production_policy_indefinite(world):
    key = world.add("T007")
    binding = world.trust["bindings"][key]
    binding["decisions"] = ["C-08"]
    live_scope = {**binding["scope"], "phase": "production"}
    binding["decision_scopes"] = {"C-08": live_scope}
    authority = v.decode(world.store.blob(binding["authority"]))
    policy = v.decode(world.store.blob(world.decision("C-08", live_scope)))
    policy["valid_until"] = "until-superseded"
    authority["decisions"] = {"C-08": world.store.put(policy, "decisions/production-policy.json")}
    binding["authority"] = world.store.put(authority, "decisions/wrapped-production-policy.json")
    world.records[key]["authority"] = binding["authority"]
    with pytest.raises(v.EvidenceError):
        world.check(key)


@pytest.mark.parametrize("kind", ["C-03", "C-08", "C-09", "C-10", "C-11", "C-12", "C-13"])
def test_source_decision_scope_override_cannot_satisfy_a_live_gate(world, kind):
    key = world.child("T058")
    binding = world.trust["bindings"][key]
    source_scope = {**binding["scope"], "phase": "source"}
    binding["decision_scopes"] = {kind: source_scope}
    ref = world.decision(kind, source_scope)
    with pytest.raises(v.EvidenceError, match="phase"):
        world.verifier().decision(ref, binding, kind)


@pytest.mark.parametrize("mutation", ["missing-proof-suite", "extra-suite"])
def test_current_t010_requires_exactly_the_commissioned_four_suites(mutation):
    world = World(); world.add("T010")
    binding = world.trust["bindings"]["T010"]
    if mutation == "missing-proof-suite": binding["ci"].pop(v.FEATURE_PATH + "/tests/test_source_roots.py")
    else: binding["ci"]["uncommissioned.py"] = 1
    with pytest.raises(v.EvidenceError, match="feature suites"):
        world.verifier().ci(world.outputs["T010"], binding)


# Synthetic reviews of actual immutable source controls. No private owner bytes
# are copied into this test tree; the selected C-only closures use public Git.
def c37_control(kind):
    return deepcopy(v.C37_CONTROLS[kind]["reference"])


@pytest.mark.parametrize("kind", ["source-ci", "package"])
@pytest.mark.parametrize("task", ["T010", "T011", "T012", "T016"])
def test_fixed_c37_reader_retains_actual_source_closures(kind, task):
    reader = v.make_verifier(TASKS, v.GitStore({v.COORDINATOR: str(ROOT)}), c37_control(kind))
    assert reader.definition == v.C37_DEFINITION
    reader.verify(task)


def c37_world(kind, monkeypatch):
    return historical_source_world(c37_control(kind), monkeypatch)


def historical_source_world(prior, monkeypatch):
    git_store = v.GitStore({v.COORDINATOR: str(ROOT)})
    world = World()
    original_blob = world.store.blob
    def blob(ref):
        identity = (ref["repository"], ref["commit"], ref["path"])
        return original_blob(ref) if identity in world.store.objects else git_store.blob(ref)
    monkeypatch.setattr(world.store, "blob", blob)
    monkeypatch.setattr(world.store, "changed", git_store.changed)
    monkeypatch.setattr(world.store, "git", git_store.git, raising=False)
    monkeypatch.setattr(world.store, "root", git_store.root, raising=False)
    world.trust = v.decode(git_store.blob(prior))
    world.trust["definition"] = v.DEFINITION
    world.trust["historical_controls"] = {task: prior for task in ("T011", "T012", "T016")}
    return world


@pytest.mark.parametrize("kind", ["source-ci", "package"])
@pytest.mark.parametrize("task", ["T011", "T012", "T016"])
@pytest.mark.parametrize("state", ["revoked-authority", "revoked-decision", "closed-authority"])
@pytest.mark.parametrize("cached", [False, True])
def test_current_state_reaches_nested_c37_history(kind, task, state, cached, monkeypatch):
    world = c37_world(kind, monkeypatch)
    binding = world.trust["bindings"]["T007"]
    authority = world.trust["source_container"]["objects"][binding["authority"]["object"]]["value"]
    reader = v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)
    if cached:
        reader.verify(task)
    identity = authority["id"]
    if state == "revoked-decision":
        ref = authority["decisions"]["C-01"]
        identity = world.trust["source_container"]["objects"][ref["object"]]["value"]["id"]
    if state == "closed-authority":
        reader.trust["completed_authorities"] = {identity: world.store.put(
            dict(kind="authority-closure", authority_id=identity, scope=binding["scope"],
                 disposition="completed", closed_at=START, owner="Synthetic Owner"), "closures/c37-current.json")}
    else:
        reader.trust["revoked_authorities"].append(identity)
    with pytest.raises(v.EvidenceError, match="revoked|closed"):
        reader.verify(task)


@pytest.mark.parametrize("kind", ["source-ci", "package"])
@pytest.mark.parametrize("task", ["T011", "T012", "T016"])
def test_c37_children_keep_the_original_consumed_ci(kind, task, monkeypatch):
    world = c37_world(kind, monkeypatch)
    world.trust["bindings"]["T010"]["command"] = "synthetic replacement CI awaiting its own admission"
    v.Verifier(TASKS, world.store, source_anchor(world), now=NOW).verify(task)


@pytest.mark.parametrize("kind", ["source-ci", "package"])
@pytest.mark.parametrize("field,value", [
    ("commit", "a" * 40), ("path", "evidence/unaccepted.json"),
    ("repository", "opensoft/another-factory"), ("sha256", "a" * 64),
])
def test_fixed_c37_control_does_not_accept_reference_substitution(kind, field, value):
    ref = c37_control(kind)
    ref[field] = value
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    with pytest.raises(v.EvidenceError):
        v.historical_verifier(store, ref)


@pytest.mark.parametrize("kind", ["source-ci", "package"])
@pytest.mark.parametrize("mutation", ["core", "reader", "definition", "frozen-input"])
def test_fixed_c37_history_checks_all_immutable_inputs(kind, mutation, monkeypatch):
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    ref = c37_control(kind)
    if mutation == "core":
        controls = deepcopy(v.C37_CONTROLS)
        controls[kind]["content_sha256"] = "a" * 64
        monkeypatch.setattr(v, "C37_CONTROLS", controls)
    elif mutation == "reader":
        monkeypatch.setattr(v, "C37_READER", dict(v.C37_READER, sha256="a" * 64))
    elif mutation == "definition":
        monkeypatch.setattr(v, "C37_DEFINITION", "a" * 64)
    else:
        original = store.git
        def changed(root, *args):
            raw = original(root, *args)
            return raw + b"\nsynthetic drift" if args[0] == "show" and args[1].endswith("/spec.md") else raw
        monkeypatch.setattr(store, "git", changed)
    with pytest.raises(v.EvidenceError):
        v.historical_verifier(store, ref)


@pytest.mark.parametrize("task", ["T018", "T021", "T052"])
def test_c37_history_cannot_admit_a_pending_or_live_task(task, monkeypatch):
    world = c37_world("package", monkeypatch)
    world.trust["historical_controls"] = {task: c37_control("package")}
    anchor = source_anchor(world)
    with pytest.raises(v.EvidenceError, match="unaccepted historical task"):
        v.Verifier(TASKS, world.store, anchor, now=NOW)


def test_t020_history_requires_its_actual_package_control(monkeypatch):
    world = c37_world("source-ci", monkeypatch)
    world.trust["historical_controls"] = {"T020": c37_control("source-ci")}
    anchor = source_anchor(world)
    with pytest.raises(v.EvidenceError, match="unaccepted historical control"):
        v.Verifier(TASKS, world.store, anchor, now=NOW)


# Actual accepted 2a46 controls, exercised as history under the new source freeze.
# Synthetic current reviews below authenticate no project qualification output.
def control_2a46(kind):
    return deepcopy(v.CONTROLS_2A46[kind]["reference"])


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("task", ["T010", "T011", "T012", "T016"])
def test_2a46_accepted_controls_verify_original_public_source_closures(kind, task):
    reader = v.make_verifier(TASKS, v.GitStore({v.COORDINATOR: str(ROOT)}), control_2a46(kind))
    assert reader.definition == v.DEFINITION_2A46
    reader.verify(task)


def test_2a46_hosted_control_preserves_actual_t013_authentication():
    reader = v.make_verifier(TASKS, v.GitStore({v.COORDINATOR: str(ROOT)}), control_2a46("hosted"))
    reader.verify("T013")
    assert reader.authenticated is True
    assert reader.trust["bindings"]["T013"]["scope"]["phase"] == "source"


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("task", ["T020", "T021", "T022"])
def test_2a46_private_package_bindings_stay_original_without_importing_private_source(kind, task):
    # Full private-owner qualification stays in the actual read-only proof lane.
    reader = v.make_verifier(TASKS, v.GitStore({v.COORDINATOR: str(ROOT)}), control_2a46(kind))
    binding = reader.binding(task)
    assert binding == reader.trust["bindings"][task]
    assert binding["owner"] == "L" and binding["scope"]["phase"] == "source"
    assert reader.authenticated is True


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("field,value", [
    ("repository", "opensoft/unaccepted-owner"), ("commit", "a" * 40),
    ("path", "evidence/copied-control.json"), ("sha256", "a" * 64),
])
def test_2a46_whole_reference_substitution_refuses(kind, field, value):
    ref = control_2a46(kind); ref[field] = value
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    expected = {"commit": "local Git object or repository unavailable",
                "sha256": "immutable content digest mismatch"}.get(field, v.HISTORICAL_CONTROL_ERROR)
    with pytest.raises(v.EvidenceError, match=expected):
        v.historical_verifier(store, ref)


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("mutation", ["core", "reader", "definition", "frozen-input"])
def test_2a46_original_core_reader_and_complete_freeze_are_required(kind, mutation, monkeypatch):
    ref = control_2a46(kind)
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    if mutation == "core":
        controls = deepcopy(v.CONTROLS_2A46); controls[kind]["content_sha256"] = "a" * 64
        monkeypatch.setattr(v, "CONTROLS_2A46", controls)
    elif mutation == "reader":
        monkeypatch.setattr(v, "READER_2A46", dict(v.READER_2A46, sha256="a" * 64))
    elif mutation == "definition":
        monkeypatch.setattr(v, "DEFINITION_2A46", "a" * 64)
    else:
        original = store.git
        def changed(root, *args):
            raw = original(root, *args)
            return raw + b"\nsynthetic drift" if args[0] == "show" and args[1].endswith("/owner-scopes.md") else raw
        monkeypatch.setattr(store, "git", changed)
    with pytest.raises(v.EvidenceError):
        v.historical_verifier(store, ref)


def test_2a46_pending_reviewed_manifest_is_not_an_accepted_control():
    pending = dict(repository=v.COORDINATOR, commit="53c2b0700e342b77196980a617dea7fc2fa33512",
                   path=v.COMMISSIONING_PATH, sha256="e3fce83cce9f9c6597fd82d00e4fabc6934ae30e6e06a49c52bded4ed4b1146f")
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    assert v.commissioning_digest(v.decode(store.blob(pending))) == v.CONTROLS_2A46["hosted"]["content_sha256"]
    with pytest.raises(v.EvidenceError, match="unaccepted historical control"):
        v.historical_verifier(store, pending)


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("state", ["revoked-authority", "revoked-decision", "closed-authority"])
@pytest.mark.parametrize("cached", [False, True])
def test_2a46_nested_and_cached_reads_apply_current_authority(kind, state, cached, monkeypatch):
    world = historical_source_world(control_2a46(kind), monkeypatch)
    binding = world.trust["bindings"]["T007"]
    authority = world.trust["source_container"]["objects"][binding["authority"]["object"]]["value"]
    reader = v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)
    if cached: reader.verify("T012")
    identity = authority["id"]
    if state == "revoked-decision":
        ref = authority["decisions"]["C-01"]
        identity = world.trust["source_container"]["objects"][ref["object"]]["value"]["id"]
    if state == "closed-authority":
        reader.trust["completed_authorities"] = {identity: world.store.put(
            dict(kind="authority-closure", authority_id=identity, scope=binding["scope"],
                 disposition="completed", closed_at=START, owner="Synthetic Owner"), "closures/2a46-current.json")}
    else:
        reader.trust["revoked_authorities"].append(identity)
    with pytest.raises(v.EvidenceError, match="revoked|closed"):
        reader.verify("T012")


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
@pytest.mark.parametrize("task", ["T014", "T015", "T017", "T018", "T019", "T023", "T028", "T051"])
def test_2a46_source_anchor_cannot_admit_pending_or_live_tasks(kind, task, monkeypatch):
    world = historical_source_world(control_2a46(kind), monkeypatch)
    world.trust["historical_controls"] = {task: control_2a46(kind)}
    with pytest.raises(v.EvidenceError, match="unaccepted historical task"):
        v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)


def test_2a46_earlier_control_does_not_acquire_later_t013(monkeypatch):
    world = historical_source_world(control_2a46("source-ci"), monkeypatch)
    world.trust["historical_controls"] = {"T013": control_2a46("source-ci")}
    with pytest.raises(v.EvidenceError, match="unaccepted historical task"):
        v.Verifier(TASKS, world.store, source_anchor(world), now=NOW)


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
def test_2a46_children_keep_the_actual_original_ci(kind, monkeypatch):
    world = historical_source_world(control_2a46(kind), monkeypatch)
    world.trust["bindings"]["T010"]["command"] = "synthetic replacement awaiting separate source authentication"
    v.Verifier(TASKS, world.store, source_anchor(world), now=NOW).verify("T012")


@pytest.mark.parametrize("kind", ["source-ci", "hosted"])
def test_2a46_identical_bytes_at_a_new_actual_commit_are_not_accepted(kind, tmp_path):
    # A positive object/read baseline makes this about exact identity, not absence.
    ref = control_2a46(kind)
    copied = tmp_path / "synthetic-unaccepted-copy"; copied.mkdir()
    subprocess.run(["git", "init", "-q", str(copied)], check=True)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/" + v.COORDINATOR + ".git"],
                   cwd=copied, check=True)
    objects = subprocess.check_output(["git", "rev-parse", "--git-path", "objects"], cwd=ROOT, text=True).strip()
    (copied / ".git/objects/info/alternates").write_text(str((ROOT / objects).resolve()) + "\n")
    tree = subprocess.check_output(["git", "rev-parse", ref["commit"] + "^{tree}"], cwd=ROOT, text=True).strip()
    other = subprocess.check_output(
        ["git", "-c", "user.name=Synthetic control copy", "-c", "user.email=copy@example.invalid",
         "commit-tree", tree, "-p", ref["commit"], "-m", "Synthetic identical but unaccepted source control"],
        cwd=copied, text=True).strip()
    clone_ref = dict(ref, commit=other)
    store = v.GitStore({v.COORDINATOR: str(copied)})
    assert other != ref["commit"]
    assert store.blob(clone_ref) == v.GitStore({v.COORDINATOR: str(ROOT)}).blob(ref)
    with pytest.raises(v.EvidenceError, match="unaccepted historical control"):
        v.make_verifier(TASKS, store, clone_ref)


# The real root supplies immutable authority only; these tests accept no output.
DELEGATION_ROOT_FIXTURE = {
    "repository": "opensoft/openxfactory",
    "commit": "d2528306ab6fe95c9235073f10c9150822b3f86e",
    "path": "openspec/changes/authorize-private-connectivity-internal-production/review/human-root-grant.json",
    "sha256": "57d5d91c35a7db3bf6030572841cd836137749aff4c27a29e8081d8d201704aa",
}
DELEGATION_TIME = datetime(2026, 11, 18, tzinfo=timezone.utc)


def test_delegation_root_is_the_actual_human_choice():
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    root = v.load_delegation_root(store, deepcopy(DELEGATION_ROOT_FIXTURE), DELEGATION_TIME)
    assert root["human"] == "Brett Heap" and root["delegate"]["actor"] == "Codex"
    assert root["production_storage"]["monthly_ceiling"] == 20
    assert root["support"]["macos"] == "deferred and unqualified"
    assert len(root["policy"]["members"]) == 8


@pytest.mark.parametrize("field,value", [
    ("repository", "opensoft/other"), ("commit", "a" * 40),
    ("path", "review/copied-grant.json"), ("sha256", "a" * 64),
])
def test_delegation_root_rejects_substituted_whole_reference(field, value):
    ref = dict(DELEGATION_ROOT_FIXTURE); ref[field] = value
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    with pytest.raises(v.EvidenceError, match="root"):
        v.load_delegation_root(store, ref, DELEGATION_TIME)


@pytest.mark.parametrize("at", [
    datetime(2026, 11, 17, 8, 38, 55, 472000, tzinfo=timezone.utc),
    datetime(2026, 12, 17, 8, 38, 55, 473000, tzinfo=timezone.utc),
    datetime(2027, 1, 1, tzinfo=timezone.utc),
    datetime(2026, 11, 18),
])
def test_delegation_root_rejects_outside_or_naive_decision_time(at):
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    with pytest.raises(v.EvidenceError, match="root"):
        v.load_delegation_root(store, DELEGATION_ROOT_FIXTURE, at)


def test_delegation_root_current_revocation_refuses():
    with pytest.raises(v.EvidenceError, match="revoked"):
        v.load_delegation_root(v.GitStore({v.COORDINATOR: str(ROOT)}), DELEGATION_ROOT_FIXTURE,
                               DELEGATION_TIME, revoked=["pc043-internal-20261117-e995d2290328"])


def test_delegation_root_authenticates_each_original_policy_blob():
    real = v.GitStore({v.COORDINATOR: str(ROOT)})
    def blob(ref):
        data = real.blob(ref)
        return data + b"\nsynthetic corruption" if ref["commit"] == "a66cfe601407818dbd04f294bbaf92af15246e22" else data
    with pytest.raises(v.EvidenceError, match="digest"):
        v.load_delegation_root(SimpleNamespace(blob=blob), DELEGATION_ROOT_FIXTURE, DELEGATION_TIME)


def test_delegation_producer_uses_qualified_pin_and_refuses_inactive_state(monkeypatch):
    ref = v.DELEGATION_PRODUCER_REF
    assert ref["repository"] == v.COORDINATOR
    assert ref["commit"] == "ba911daab0ed791641e19d7954f5b625a9b3c81c"
    assert ref["path"] == v.FEATURE_PATH + "/attest-delegated-evidence.py"
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    raw = store.blob(ref)
    assert v.digest(raw) == ref["sha256"]
    assert v.require_delegation_producer(store, dict(ref)) == raw
    assert sorted(v.DELEGATED_ATTESTATIONS) == [
        "08dc067d95a6199571d26983e1cd0d289329e8fde58fa338853961a68b365fea",
        "9b521406a9c221269c9332b6852579ea26135a723547f8e4720988e2d8ae5bdb",
        "a8fe2c36d22fc1a08bdac7619aa84122ba23fa22d6728db5c7dccf19211aca2f",
        "b131505270619a34adbc9eb0208460a93ab37b3b5b9492296f671a7db9b7fb04",
        "bb6d9c4f29f55f7c633dbadd71c56907fa297800395d4dec961d9f529341990d",
        "ed53795c4d54152860abd38a15338449a24e3069dff3ec0483d66f741fbb2acd",
    ]
    kinds = set()
    for subject_sha256, evidence_ref in v.DELEGATED_ATTESTATIONS.items():
        record = v.decode(store.blob(evidence_ref))
        task = {
            "9b521406a9c221269c9332b6852579ea26135a723547f8e4720988e2d8ae5bdb": "T015",
            "b131505270619a34adbc9eb0208460a93ab37b3b5b9492296f671a7db9b7fb04": "T015",
            "bb6d9c4f29f55f7c633dbadd71c56907fa297800395d4dec961d9f529341990d": "T018",
        }.get(subject_sha256, "T010")
        assert evidence_ref['path'] == v.FEATURE_PATH + f'/evidence/{task}.json'
        assert record['schema'] == '043-delegated-attestation-v1'
        assert record['producer'] == ref
        assert v.digest(v.canonical_json(record['subject'])) == subject_sha256
        kinds.add(record['subject']['kind'])
    assert kinds == {'decision', 'source-authentication'}
    monkeypatch.setattr(v, "DELEGATION_PRODUCER_REF", None)
    with pytest.raises(v.EvidenceError, match="not activated"):
        v.require_delegation_producer(SimpleNamespace(blob=lambda value: b""), {})


def test_delegation_producer_accepts_only_the_exact_activated_bytes(monkeypatch):
    data = b"Synthetic test producer, never an actual qualification"
    ref = dict(repository=v.COORDINATOR, commit="6" * 40,
               path=v.FEATURE_PATH + "/attest-delegated-evidence.py", sha256=v.digest(data))
    monkeypatch.setattr(v, "DELEGATION_PRODUCER_REF", ref)
    store = SimpleNamespace(blob=lambda value: data)
    assert v.require_delegation_producer(store, dict(ref)) == data
    with pytest.raises(v.EvidenceError, match="producer"):
        v.require_delegation_producer(store, dict(ref, commit="7" * 40))
    with pytest.raises(v.EvidenceError, match="digest"):
        v.require_delegation_producer(SimpleNamespace(blob=lambda value: b"tampered"), ref)


@pytest.fixture
def delegated_world(monkeypatch):
    # Actual root/policy bytes, synthetic producer/review/provider metadata.
    # No real output is accepted or delegate activated by these unit tests.
    monkeypatch.setitem(globals(), "START", "2026-11-18T00:00:00Z")
    monkeypatch.setitem(globals(), "END", "2026-11-18T00:01:00Z")
    monkeypatch.setitem(globals(), "AUTHORITY_START", "2026-11-17T09:00:00Z")
    monkeypatch.setitem(globals(), "AUTHORITY_END", "2026-12-17T08:38:55.473Z")
    world = source_container_world()
    monkeypatch.setattr(v, "DELEGATED_ATTESTATIONS", {})
    real = v.GitStore({v.COORDINATOR: str(ROOT)})
    original = world.store.blob
    def blob(ref):
        identity = (ref["repository"], ref["commit"], ref["path"])
        return original(ref) if identity in world.store.objects else real.blob(ref)
    monkeypatch.setattr(world.store, "blob", blob)
    producer = world.store.put(b"Synthetic qualified producer", v.FEATURE_PATH + "/attest-delegated-evidence.py")
    monkeypatch.setattr(v, "DELEGATION_PRODUCER_REF", producer)
    pending = source_anchor(world, accepted=False)
    subject = dict(kind="source-authentication", definition=v.DEFINITION,
                   reviewed_manifest=pending, content_sha256=v.commissioning_digest(world.trust))
    panel = dict(schema="043-independent-review-v1", subject=subject,
                 reviewed_at="2026-11-18T01:00:00Z",
                 roles={role: dict(reviewer="synthetic-" + role, verdict="clear",
                                   report="Synthetic focused independent report") for role in v.REVIEW_ROLES})
    grouped = {}
    for output in world.outputs.values():
        for suite, run in output["ci"].items():
            identity = (run["repository"], run["run_id"], run["job_id"], run["revision"])
            grouped.setdefault(identity, {})[suite] = run["collected"]
    observations = [dict(
        run=dict(id=run_id, head_sha=revision, status="completed", conclusion="success", run_attempt=1,
                 created_at="2026-11-18T00:00:00Z", updated_at="2026-11-18T00:06:00Z",
                 repository=dict(full_name=repository)),
        job=dict(id=job_id, run_id=run_id, head_sha=revision, status="completed", conclusion="success", run_attempt=1,
                 started_at="2026-11-18T00:01:00Z", completed_at="2026-11-18T00:05:00Z",
                 steps=[dict(name="Synthetic collected suites", conclusion="success")]),
        log_sha256=v.digest(b"Synthetic actual provider log"), suites=suites)
        for (repository, run_id, job_id, revision), suites in grouped.items()]
    for item in observations:
        item["run"]["path"] = ".github/workflows/pytest-suite.yml"
        names = ["Require the commissioned App identity (043)", "Mint scoped Opensoft source read token (043)",
                 "Prepare commit-only owner roots with the reviewed producer (043)",
                 "Revoke source tokens before any tests (043)",
                 "Run private-connectivity production source suites (043)", "Remove ephemeral source proof (043)"]
        item["job"]["steps"] = [dict(name=name, number=number, conclusion="success") for number, name in enumerate(names, 1)]
    secondary = deepcopy(observations[0])
    secondary["run"]["id"] += 1
    secondary["run"]["path"] = ".github/workflows/doc-health-py314.yml"
    secondary["job"]["id"] += 1
    secondary["job"]["run_id"] = secondary["run"]["id"]
    secondary["job"]["steps"][4]["name"] = "Exercise source proof under Python 3.14 (043)"
    secondary["suites"] = {path: count for path, count in secondary["suites"].items()
                          if path.endswith(("test_source_roots.py", "test_delegated_evidence.py"))}
    observations.append(secondary)
    attestation = dict(schema="043-delegated-attestation-v1", actor="Codex", accountable_owner="Brett Heap",
                       root=deepcopy(DELEGATION_ROOT_FIXTURE), producer=producer,
                       reviewed_at="2026-11-18T01:01:00Z", subject=subject,
                       independent_review=world.store.put(panel, "reviews/independent.json"),
                       provider_observations=observations, evidence=[pending])
    def anchor():
        ref = world.store.put(attestation, "reviews/delegated-attestation.json")
        v.DELEGATED_ATTESTATIONS[v.digest(v.canonical_json(attestation["subject"]))] = ref
        record = dict(schema="043-delegated-source-authentication-v1", decision="accepted", actor="Codex",
                      accountable_owner="Brett Heap", reviewed_manifest=pending,
                      content_sha256=subject["content_sha256"], attestation=ref)
        fence = bytes([96]) * 3
        world.trust["review"] = world.store.put(
            b"# SYNTHETIC delegated review\n" + fence + b"json\n" + v.canonical_json(record)
            + b"\n" + fence + b"\n", v.AUTHENTICATION_PATH)
        return world.store.put(world.trust, v.COMMISSIONING_PATH)
    return world, attestation, panel, anchor


def test_delegated_source_form_verifies_actual_root_and_all_original_checks(delegated_world):
    world, _, _, anchor = delegated_world
    trust = anchor()
    expiry = v.timestamp(AUTHORITY_END)
    for now in (expiry - timedelta(seconds=1), expiry + timedelta(seconds=1)):
        reader = v.Verifier(TASKS, world.store, trust, now=now)
        reader.verify("T010")
        assert reader.cache == {f"T{i:03}" for i in range(1, 11)}

    binding = reader.binding("T010")
    with pytest.raises(v.EvidenceError, match="authority expired or not current"):
        reader.authority(binding["authority"], binding)


@pytest.mark.parametrize("mutation", [
    "actor", "owner", "root", "producer", "expired", "future", "subject", "missing-evidence",
    "extra-field", "missing-ci", "extra-ci", "failed-run", "wrong-job-head", "failed-step",
    "wrong-count", "missing-log", "duplicate-ci", "duplicate-evidence",
])
def test_delegated_authentication_rejects_incomplete_or_substituted_proof(delegated_world, mutation):
    world, proof, _, anchor = delegated_world
    if mutation == "actor": proof["actor"] = "Brett Heap"
    if mutation == "owner": proof["accountable_owner"] = "someone else"
    if mutation == "root": proof["root"]["commit"] = "a" * 40
    if mutation == "producer": proof["producer"] = dict(proof["producer"], commit="b" * 40)
    if mutation == "expired": proof["reviewed_at"] = "2026-12-17T08:38:55.473Z"
    if mutation == "future": proof["reviewed_at"] = "2026-11-20T00:00:00Z"
    if mutation == "subject": proof["subject"] = dict(proof["subject"], definition="a" * 64)
    if mutation == "missing-evidence": proof["evidence"] = []
    if mutation == "extra-field": proof["waiver"] = True
    if mutation == "missing-ci": proof["provider_observations"] = []
    if mutation == "extra-ci": proof["provider_observations"][0]["run"]["id"] += 1
    if mutation == "failed-run": proof["provider_observations"][0]["run"]["conclusion"] = "failure"
    if mutation == "wrong-job-head": proof["provider_observations"][0]["job"]["head_sha"] = "a" * 40
    if mutation == "failed-step": proof["provider_observations"][0]["job"]["steps"][0]["conclusion"] = "failure"
    if mutation == "wrong-count": proof["provider_observations"][0]["suites"][next(iter(proof["provider_observations"][0]["suites"]))] += 1
    if mutation == "missing-log": proof["provider_observations"][0]["log_sha256"] = None
    if mutation == "duplicate-ci": proof["provider_observations"] *= 2
    if mutation == "duplicate-evidence": proof["evidence"] *= 2
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))


@pytest.mark.parametrize("mutation", ["missing-role", "same-reviewer", "unresolved", "missing-report", "subject", "late"])
def test_delegated_authentication_requires_actual_distinct_independent_review(delegated_world, mutation):
    world, proof, panel, anchor = delegated_world
    if mutation == "missing-role": panel["roles"].pop("security")
    if mutation == "same-reviewer":
        for result in panel["roles"].values(): result["reviewer"] = "one-reviewer"
    if mutation == "unresolved": panel["roles"]["security"]["verdict"] = "findings"
    if mutation == "missing-report": panel["roles"]["security"]["report"] = ""
    if mutation == "subject": panel["subject"] = {}
    if mutation == "late": panel["reviewed_at"] = "2026-11-19T00:00:00Z"
    proof["independent_review"] = world.store.put(panel, "reviews/changed-independent.json")
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))


def test_delegated_source_authentication_rechecks_current_root_revocation(delegated_world):
    world, _, _, anchor = delegated_world
    world.trust["revoked_authorities"].append("pc043-internal-20261117-e995d2290328")
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))


@pytest.mark.parametrize("mutation", ["missing-secondary", "wrong-secondary-head", "skipped-prepare", "late-revocation", "wrong-secondary-count"])
def test_delegated_source_requires_both_real_proof_lanes(delegated_world, mutation):
    world, proof, _, anchor = delegated_world
    observations = proof["provider_observations"]
    if mutation == "missing-secondary": observations.pop()
    if mutation == "wrong-secondary-head": observations[-1]["job"]["head_sha"] = "a" * 40
    if mutation == "skipped-prepare": observations[-1]["job"]["steps"][2]["conclusion"] = "skipped"
    if mutation == "late-revocation": observations[-1]["job"]["steps"][3]["number"] = 99
    if mutation == "wrong-secondary-count":
        key = next(iter(observations[-1]["suites"]))
        observations[-1]["suites"][key] += 1
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))


def test_delegated_root_revocation_is_rechecked_after_cache(delegated_world):
    world, _, _, anchor = delegated_world
    reader = v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))
    reader.verify("T007")
    reader.trust["revoked_authorities"].append("pc043-internal-20261117-e995d2290328")
    with pytest.raises(v.EvidenceError, match="root revoked"):
        reader.verify("T007")


def bind_synthetic_delegated_subject(world, proof, panel, subject):
    proof["subject"] = subject
    proof["provider_observations"] = []
    panel["subject"] = subject
    proof["independent_review"] = world.store.put(panel, "reviews/subject-panel.json")
    ref = world.store.put(proof, "reviews/subject-proof.json")
    v.DELEGATED_ATTESTATIONS[v.digest(v.canonical_json(subject))] = ref
    return ref


@pytest.mark.parametrize("mutation", [None, "human-actor", "external", "Q5", "expiry", "late-decision", "mutated-record"])
def test_delegated_runtime_decisions_keep_actor_customer_time_and_Q5_limits(delegated_world, mutation):
    world, proof, panel, anchor = delegated_world
    reader = v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))
    binding = deepcopy(world.trust["bindings"]["T007"])
    binding["task"] = "T058"
    binding["scope"].update(phase="production", customer="Opensoft Inc")
    decision = dict(id="synthetic-runtime-grant", kind="grant", actor="Codex", owner="Codex",
                    accountable_owner="Brett Heap", decision="accepted", scope=binding["scope"],
                    valid_from="2026-11-18T01:01:00Z", valid_until="2026-11-19T00:00:00Z")
    if mutation == "human-actor": decision["owner"] = "Brett Heap"
    if mutation == "external": binding["scope"]["customer"] = "external customer"
    if mutation == "Q5": decision["kind"] = "C-11"
    if mutation == "expiry": decision["valid_until"] = "2027-01-01T00:00:00Z"
    subject = dict(kind="decision", definition=v.DEFINITION, record_sha256=v.digest(v.canonical_json(decision)))
    decision["delegation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    if mutation == "mutated-record": decision["id"] = "different"
    start = v.timestamp("2026-11-18T00:00:00Z" if mutation == "late-decision" else "2026-11-18T01:02:00Z")
    end = v.timestamp("2026-11-18T01:03:00Z")
    if mutation:
        with pytest.raises(v.EvidenceError):
            reader.delegated_decision(decision, binding, start, end)
    else:
        reader.delegated_decision(decision, binding, start, end)


@pytest.fixture
def internal_handoff_world(delegated_world, monkeypatch):
    world, proof, panel, _ = delegated_world
    # This tests aggregate admission in isolation. Child verification is tracked,
    # not replaced in the executable reader; full child/canary cases stay above.
    expected = {}
    groups = {}
    for instance, offering, group in (("local", "local-local", "local-headscale"),
                                    ("service", "hosted-headscale", "hosted-headscale"),
                                    ("domain", "hosted-domain", "hosted-domain")):
        key = world.child("T061", instance, {"customer": "Opensoft Inc", "offering": offering})
        expected[instance] = world.ref(key)
        groups[group] = {instance: expected[instance]}
    releases = {owner: world.ref(task) for owner, task in
                (("C", "T019"), ("L", "T023"), ("I", "T027"), ("H", "T033"), ("D", "T042"), ("O", "T048"))}
    operations = {name: world.store.put(b"Synthetic usable operator instructions", "operations/" + name + ".md")
                  for name in ("onboarding", "monitoring", "support", "rollback", "custody")}
    proof["reviewed_at"] = "2026-11-18T02:00:00Z"
    panel["reviewed_at"] = "2026-11-18T01:59:00Z"
    handoff = dict(schema="043-internal-program-handoff-v1", root=deepcopy(DELEGATION_ROOT_FIXTURE),
                   accepted_at=proof["reviewed_at"], offerings=groups, releases=releases, operations=operations)
    subject = dict(kind="internal-program-handoff", definition=v.DEFINITION,
                   content_sha256=v.digest(v.canonical_json(handoff)))
    handoff["attestation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    reader = object.__new__(v.Verifier)
    reader.tasks, reader.store, reader.trust = TASKS, world.store, world.trust
    reader.definition, reader.now = v.DEFINITION, DELEGATION_TIME.replace(day=19)
    reader.objects = world.trust["source_container"]["objects"]
    reader.authenticated, reader.authenticated_at = True, v.timestamp(proof["reviewed_at"])
    reader.delegated_root_id = "pc043-internal-20261117-e995d2290328"
    calls = []
    monkeypatch.setattr(reader, "verify", lambda key: calls.append(key))
    def publish():
        fence = bytes([96]) * 3
        ref = world.store.put(b"# Synthetic handoff\n" + fence + b"json\n" + v.canonical_json(handoff)
                              + b"\n" + fence + b"\n", v.FEATURE_PATH + "/review/internal-production-handoff.md")
        reader.trust["internal_program"] = dict(root=deepcopy(DELEGATION_ROOT_FIXTURE), handoff=ref)
    return world, reader, handoff, expected, calls, publish


@pytest.mark.parametrize("mutation", [None, "missing-offering", "foreign-customer", "wrong-release",
                                      "missing-support", "wrong-path", "wrong-root", "wrong-time", "unreviewed-change"])
def test_internal_handoff_requires_all_three_actual_offerings_and_operator_packet(internal_handoff_world, mutation):
    world, reader, handoff, expected, calls, publish = internal_handoff_world
    if mutation == "missing-offering": handoff["offerings"].pop("hosted-domain")
    if mutation == "foreign-customer": reader.trust["bindings"]["T061@domain"]["scope"]["customer"] = "someone else"
    if mutation == "wrong-release": handoff["releases"]["H"] = handoff["releases"]["C"]
    if mutation == "missing-support": handoff["operations"].pop("support")
    if mutation == "wrong-root": handoff["root"]["commit"] = "a" * 40
    if mutation == "wrong-time": handoff["accepted_at"] = "2026-11-18T02:00:01Z"
    if mutation == "unreviewed-change":
        handoff["operations"]["support"] = world.store.put(b"Changed after review", "operations/new-support.md")
    publish()
    if mutation == "wrong-path":
        ref = reader.trust["internal_program"]["handoff"]
        reader.trust["internal_program"]["handoff"] = world.store.put(
            world.store.blob(ref), v.FEATURE_PATH + "/review/copied-handoff.md")
    if mutation:
        with pytest.raises(v.EvidenceError):
            reader.internal_handoff(list(expected), expected)
    else:
        reader.internal_handoff(list(expected), expected)
        assert calls == ["T061@local", "T061@service", "T061@domain",
                         "T019", "T023", "T027", "T033", "T042", "T048"]


def test_internal_handoff_is_aggregate_only_and_does_not_widen_child_cases():
    assert TASKS["T061"]["cases"] == ["observed-objectives-met", "incidents-reviewed-closed", "fresh-owner-acceptance"]
    assert "internal-program-handoff" not in TASKS["T061"]["cases"]
    assert TASKS["T062"]["dependencies"] == ["T061"]


@pytest.mark.parametrize("mutation", ["unregistered", "other-subject", "copied-commit", "fabricated"])
def test_delegated_output_requires_exact_protected_base_qualification(delegated_world, mutation):
    world, proof, _, anchor = delegated_world
    anchor()
    subject = deepcopy(proof["subject"])
    approved = v.DELEGATED_ATTESTATIONS[v.digest(v.canonical_json(subject))]
    ref = approved
    if mutation == "unregistered": v.DELEGATED_ATTESTATIONS.clear()
    if mutation == "other-subject": subject["kind"] = "decision"
    if mutation == "copied-commit":
        ref = world.store.put(world.store.blob(approved), approved["path"], revision="7" * 40)
    if mutation == "fabricated":
        changed = deepcopy(proof); changed["actor"] = "claimed-qualified-producer"
        ref = world.store.put(changed, approved["path"])
    with pytest.raises(v.EvidenceError, match="not independently qualified"):
        v.require_delegated_review(world.store, ref, subject, DELEGATION_TIME.replace(day=19))


def test_codex_admission_cannot_use_legacy_human_path():
    world = World()
    key = world.child("T058")
    completed_run(world, key)
    admit_run(world, key, owner="Codex", actor="Codex", accountable_owner="Brett Heap")
    with pytest.raises(v.EvidenceError, match="delegated decision actor"):
        world.check(key)


@pytest.mark.parametrize("mutation", [None, "inactive", "missing-attestation", "wrong-root",
                                      "expired", "revoked", "wrong-subject", "before-run"])
def test_delegated_admission_is_post_run_and_qualified(delegated_world, monkeypatch, mutation):
    world, proof, panel, _ = delegated_world
    key = world.child("T058", scope_changes={"customer": "Opensoft Inc"})
    completed_run(world, key)
    reviewed_at = "2026-11-18T00:00:00Z" if mutation == "before-run" else "2026-11-18T02:00:00Z"
    proof["reviewed_at"] = reviewed_at
    panel["reviewed_at"] = "2026-11-17T23:59:00Z"
    if mutation == "expired":
        proof["reviewed_at"] = reviewed_at = "2026-12-18T00:00:00Z"
    if mutation == "wrong-root": proof["root"]["commit"] = "a" * 40
    admission = admit_run(world, key, owner="Codex", actor="Codex", accountable_owner="Brett Heap",
                          reviewed_at=reviewed_at)
    subject = dict(kind="decision", definition=v.DEFINITION,
                   record_sha256=v.digest(v.canonical_json(admission)))
    admission["delegation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    if mutation == "missing-attestation": admission.pop("delegation")
    if mutation == "wrong-subject": admission["id"] = "substituted-admission"
    ref = world.store.put(admission, "reviews/delegated-admission.json")
    world.trust["bindings"][key]["admission"] = world.records[key]["admission"] = ref
    world.publish(key)
    control = source_anchor(world, mutate_review=lambda review: review.update(reviewed_at="2026-11-18T03:00:00Z"))
    reader = v.Verifier(TASKS, world.store, control, now=v.timestamp("2026-12-19T00:00:00Z")
                        if mutation == "expired" else DELEGATION_TIME.replace(day=19))
    if mutation == "inactive": monkeypatch.setattr(v, "DELEGATION_PRODUCER_REF", None)
    if mutation == "revoked": reader.trust["revoked_authorities"].append("pc043-internal-20261117-e995d2290328")
    binding = reader.binding(key)
    record = reader.read(binding["record"], binding)
    if mutation:
        with pytest.raises(v.EvidenceError):
            reader.evidence_authority(binding, record)
    else:
        reader.evidence_authority(binding, record)


@pytest.mark.parametrize("after_expiry", [False, True])
def test_delegated_source_permission_cannot_extend_execution_window(delegated_world, after_expiry):
    world, proof, panel, anchor = delegated_world
    reader = v.Verifier(TASKS, world.store, anchor(), now=v.timestamp("2026-12-19T00:00:00Z"))
    binding = deepcopy(world.trust["bindings"]["T007"])
    decision = dict(id="source-scope", kind="C-01", owner="Codex", actor="Codex",
                    accountable_owner="Brett Heap", decision="accepted", scope=binding["scope"],
                    valid_from="2026-11-17T09:00:00Z", valid_until="until-superseded")
    subject = dict(kind="decision", definition=v.DEFINITION,
                   record_sha256=v.digest(v.canonical_json(decision)))
    decision["delegation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    start = v.timestamp("2026-12-18T00:00:00Z" if after_expiry else "2026-11-18T02:00:00Z")
    end = start + timedelta(minutes=1)
    if after_expiry:
        with pytest.raises(v.EvidenceError, match="expiry"):
            reader.delegated_decision(decision, binding, start, end)
    else:
        reader.delegated_decision(decision, binding, start, end)
        reader.validity(decision, binding["scope"], start, end, source_lifetime=True, binding=binding)


def test_internal_root_cannot_omit_aggregate_handoff(internal_handoff_world):
    world, reader, _, _, _, _ = internal_handoff_world
    reader.authenticated = True
    data = world.aggregate("T061")
    with pytest.raises(v.EvidenceError, match="requires program handoff"):
        reader.aggregate("T061", data)


@pytest.mark.parametrize("later", ["child-output", "child-admission", "release-readback"])
def test_internal_handoff_follows_actual_dependency_acceptance(internal_handoff_world, monkeypatch, later):
    world, reader, _, expected, _, publish = internal_handoff_world
    publish()
    key = "T019" if later == "release-readback" else "T061@domain"
    binding = reader.binding(key)
    record = reader.read(binding["record"], binding)
    end = v.timestamp("2026-11-18T02:00:01Z")
    if later == "child-admission":
        admission = dict(reviewed_at=end.isoformat())
        binding["admission"] = world.store.put(admission, "reviews/later-child.json")
        # Isolate prior_acceptance chronology; admission verification itself has
        # separate full positive/negative coverage above.
        monkeypatch.setattr(reader, "evidence_authority",
                            lambda actual, receipt: (None, None, v.timestamp("2026-11-18T01:23:00Z"), None))
    else:
        original = reader.evidence_authority
        def authority(actual, receipt):
            result = original(actual, receipt)
            return (*result[:2], end, result[3]) if actual is binding else result
        monkeypatch.setattr(reader, "evidence_authority", authority)
    with pytest.raises(v.EvidenceError, match="must precede internal handoff"):
        reader.internal_handoff(list(expected), expected)


def test_internal_handoff_can_be_read_after_root_expiry_with_current_underlying_acceptance(internal_handoff_world, monkeypatch):
    _, reader, _, expected, _, publish = internal_handoff_world
    publish()
    reader.now = v.timestamp("2026-12-18T00:00:00Z")
    # Existing accepted records still have their own current admission policy;
    # root expiry must not be substituted for that independent policy.
    monkeypatch.setattr(reader, "prior_acceptance", lambda *args: None)
    reader.internal_handoff(list(expected), expected)


@pytest.mark.parametrize("mutation", ["late-job", "late-run", "reversed-job", "old-attempt"])
def test_delegated_review_follows_actual_provider_completion(delegated_world, mutation):
    world, proof, _, anchor = delegated_world
    actual = proof["provider_observations"][0]
    if mutation == "late-job": actual["job"]["completed_at"] = "2026-11-18T02:00:00Z"
    if mutation == "late-run": actual["run"]["updated_at"] = "2026-11-18T02:00:00Z"
    if mutation == "reversed-job": actual["job"]["started_at"] = "2026-11-18T00:10:00Z"
    if mutation == "old-attempt": actual["job"]["run_attempt"] = 2
    control = anchor()
    with pytest.raises(v.EvidenceError):
        v.Verifier(TASKS, world.store, control, now=DELEGATION_TIME.replace(day=19))


def test_internal_handoff_accepts_dependency_equality_boundary(internal_handoff_world, monkeypatch):
    _, reader, handoff, expected, _, publish = internal_handoff_world
    publish()
    accepted = v.timestamp(handoff["accepted_at"])
    monkeypatch.setattr(reader, "evidence_authority", lambda *args: (None, None, accepted, None))
    reader.internal_handoff(list(expected), expected)


@pytest.mark.parametrize("resume", [False, True])
def test_source_resume_review_is_post_run_but_never_an_execution_grant(delegated_world, resume):
    world, proof, panel, anchor = delegated_world
    reader = v.Verifier(TASKS, world.store, anchor(), now=DELEGATION_TIME.replace(day=19))
    binding = deepcopy(world.trust["bindings"]["T007"])
    binding["decisions"] = ["C-13"]
    common = dict(decision="accepted", owner="Codex", actor="Codex", accountable_owner="Brett Heap",
                  scope=binding["scope"], valid_from=AUTHORITY_START, valid_until="until-superseded",
                  reviewed_at=proof["reviewed_at"])
    repair = dict(common, id="actual-source-rerun-review", kind="C-13",
                  reruns=[reader.read(binding["record"], binding)["output"]])
    subject = dict(kind="decision", definition=v.DEFINITION, record_sha256=v.digest(v.canonical_json(repair)))
    repair["delegation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    repair_ref = world.store.put(repair, "reviews/source-rerun.json")
    authority = dict(common, id="source-resume-review", kind="source-authority",
                     roles=binding["roles"], mode="source", decisions={"C-13": repair_ref})
    subject = dict(kind="decision", definition=v.DEFINITION, record_sha256=v.digest(v.canonical_json(authority)))
    authority["delegation"] = bind_synthetic_delegated_subject(world, proof, panel, subject)
    authority_ref = world.store.put(authority, "reviews/source-resume-authority.json")
    start, end = v.timestamp(START), v.timestamp(END)
    if resume:
        reader.authority(authority_ref, binding, start, end, resume=True)
    else:
        with pytest.raises(v.EvidenceError, match="before grant"):
            reader.authority(authority_ref, binding, start, end)
