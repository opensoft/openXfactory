"""Bounded attestor regressions; every provider and activation is synthetic."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

import pytest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRODUCER = HERE.parent / "attest-delegated-evidence.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


a = load(PRODUCER, "attestor_043_under_test")
h = load(HERE / "test_evidence.py", "attestor_043_reader_test_helpers")


def test_provider_uses_only_fixed_github_get_and_never_echoes_error_body():
    calls = []
    def runner(args, **kwargs):
        calls.append((args, kwargs))
        return subprocess.CompletedProcess(args, 1, b"private provider body", b"private token-like error")
    provider = a.GitHub(runner)
    with pytest.raises(a.AttestationError, match="GET unavailable"):
        provider.get("repos/opensoft/openxfactory/actions/runs/1")
    args, kwargs = calls[0]
    assert args[:7] == ["gh", "api", "--hostname", "github.com", "--method", "GET",
                       "repos/opensoft/openxfactory/actions/runs/1"]
    assert kwargs["env"]["GH_HOST"] == "github.com"
    assert kwargs["env"]["GH_PROMPT_DISABLED"] == "1"
    assert kwargs["timeout"] == 45


@pytest.mark.parametrize("path", ["https://foreign.invalid", "/repos/x/y", "repos/x/y\nAuthorization:value", "repos/x/y#fragment"])
def test_provider_rejects_nonfixed_resource_without_running_process(path):
    def runner(*args, **kwargs):
        pytest.fail("unsafe provider path reached a process")
    with pytest.raises(a.AttestationError, match="fixed GitHub"):
        a.GitHub(runner).get(path)


@pytest.mark.parametrize("raw", [b'{"a":1,"a":2}', b'{"n":NaN}', b'{"n":Infinity}'])
def test_provider_json_rejects_ambiguous_or_nonfinite_input(raw):
    with pytest.raises(a.AttestationError):
        a.decode(raw)


def base_provider(checks, revision="a" * 40, protected=True):
    provider = a.GitHub()
    def get(path, **kwargs):
        if path.endswith("/branches/main"):
            return dict(protected=protected, commit=dict(sha=revision))
        if path.endswith("/actions/jobs/30"):
            return dict(head_sha="a" * 40, status="completed", conclusion="success",
                        steps=[dict(name=name, conclusion="success") for name in
                               ("Analyze and wait for the existing quality gate",
                                "Verify evaluated conditions and exact main source", "Publish evaluated gate receipt")])
        assert path.endswith("/check-runs?per_page=100")
        return dict(total_count=len(checks), check_runs=checks)
    provider.get = get
    return provider


@pytest.mark.parametrize("mutation", [None, "wrong-main", "unprotected", "pending", "failed", "neutral",
                                      "missing-core", "missing-sonar", "unknown-skip", "allowed-skip"])
def test_selected_base_requires_current_protected_main_and_fully_evaluated_checks(mutation):
    revision = "a" * 40
    checks = [dict(name=name, head_sha=revision, status="completed", conclusion="success")
              for name in ("pytest-suite", "doc-health-py314", "sonar-analysis")]
    checks[-1]["details_url"] = "https://github.com/opensoft/openXfactory/actions/runs/10/job/30"
    if mutation == "pending": checks[0]["status"] = "in_progress"
    if mutation in ("failed", "neutral"): checks[2]["conclusion"] = mutation
    if mutation == "missing-core": checks.pop(0)
    if mutation == "missing-sonar": checks.pop()
    if mutation in ("allowed-skip", "unknown-skip"):
        checks.append(dict(name="Sourcery review" if mutation == "allowed-skip" else "required-new-check",
                           head_sha=revision, status="completed", conclusion="skipped"))
    provider = base_provider(checks, revision="b" * 40 if mutation == "wrong-main" else revision,
                             protected=mutation != "unprotected")
    if mutation not in (None, "allowed-skip"):
        with pytest.raises(a.AttestationError):
            provider.qualified_base(revision)
    else:
        provider.qualified_base(revision)


def observation_provider(log, attempt=1):
    provider = a.GitHub()
    run = dict(id=10, head_sha="a" * 40, run_attempt=1)
    job = dict(id=20, head_sha="a" * 40, run_id=10, run_attempt=attempt)
    def get(path, **kwargs):
        if path.endswith("/runs/10"): return deepcopy(run)
        if path.endswith("/jobs/20"): return deepcopy(job)
        assert path.endswith("/jobs/20/logs") and kwargs == {"raw": True}
        return log
    provider.get = get
    return provider


@pytest.mark.parametrize("mutation", [None, "missing", "duplicate", "wrong-head", "wrong-count", "unknown-field", "stale-attempt"])
def test_observation_requires_actual_log_collection_marker(mutation):
    suites = {a.FEATURE + "/tests/test_evidence.py": 709}
    marker = dict(schema="043-collected-suites-v1", source_revision="a" * 40, suites=suites)
    if mutation == "wrong-head": marker["source_revision"] = "b" * 40
    if mutation == "wrong-count": marker["suites"] = {next(iter(suites)): 1}
    if mutation == "unknown-field": marker["waiver"] = True
    line = ("2026-11-18T00:01:00Z " + a.MARKER + json.dumps(marker) + "\n").encode()
    log = b"unrelated log only" if mutation == "missing" else line + (line if mutation == "duplicate" else b"")
    provider = observation_provider(log, attempt=2 if mutation == "stale-attempt" else 1)
    if mutation:
        with pytest.raises(a.AttestationError):
            provider.observation(a.COORDINATOR, 10, 20, suites)
    else:
        observed = provider.observation(a.COORDINATOR, 10, 20, suites)
        assert observed["log_sha256"] == a.sha(log)
        assert observed["suites"] == suites


@pytest.mark.parametrize("repository,run_id,job_id", [("foreign.invalid/path/x", 1, 2), ("Opensoft/openXfactory", 1, 2),
                                                      (a.COORDINATOR, True, 2), (a.COORDINATOR, 1, -1)])
def test_observation_rejects_noncanonical_ids_before_provider_call(repository, run_id, job_id):
    provider = a.GitHub()
    provider.get = lambda *args, **kwargs: pytest.fail("bad identity reached provider")
    with pytest.raises(a.AttestationError):
        provider.observation(repository, run_id, job_id, {})


@pytest.fixture
def source_fixture(monkeypatch):
    return h.delegated_world.__wrapped__(monkeypatch)


def test_source_attestation_captures_actual_metadata_but_does_not_register_it(source_fixture):
    world, proof, panel, _ = source_fixture
    v = h.v
    manifest = v.reference(proof["subject"]["reviewed_manifest"])
    review = proof["independent_review"]
    primary, secondary = deepcopy(proof["provider_observations"])
    calls = []
    class Provider:
        def observation(self, repository, run_id, job_id, suites):
            calls.append(("primary", repository, run_id, job_id))
            assert suites == primary["suites"]
            return primary
        def secondary(self, revision, suites):
            calls.append(("secondary", revision))
            assert suites == secondary["suites"]
            return secondary
    result = a.attest(v, h.TASKS, world.store, manifest, review, Provider(), h.DELEGATION_TIME.replace(day=19))
    assert result["subject"] == proof["subject"]
    assert result["actor"] == "Codex" and result["accountable_owner"] == "Brett Heap"
    assert len(calls) == 2
    assert v.DELEGATED_ATTESTATIONS == {}
    ref = world.store.put(result, "reviews/new-actual-output.json")
    with pytest.raises(v.EvidenceError, match="not independently qualified"):
        v.require_delegated_review(world.store, ref, result["subject"], h.DELEGATION_TIME.replace(day=19))


@pytest.mark.parametrize("mutation", ["inactive", "expired", "missing-review", "failed-ci", "wrong-source", "missing-secondary"])
def test_source_attestor_refuses_missing_authority_or_actual_readback(source_fixture, monkeypatch, mutation):
    world, proof, _, _ = source_fixture
    v = h.v
    manifest = proof["subject"]["reviewed_manifest"]
    primary, secondary = deepcopy(proof["provider_observations"])
    if mutation == "inactive": monkeypatch.setattr(v, "DELEGATION_PRODUCER_REF", None)
    if mutation == "failed-ci": primary["job"]["conclusion"] = "failure"
    if mutation == "wrong-source": primary["run"]["head_sha"] = "b" * 40
    review = dict(proof["independent_review"], sha256="a" * 64) if mutation == "missing-review" else proof["independent_review"]
    class Provider:
        def observation(self, *args): return primary
        def secondary(self, *args):
            if mutation == "missing-secondary": raise a.AttestationError("missing secondary")
            return secondary
    now = v.timestamp("2026-12-18T00:00:00Z") if mutation == "expired" else h.DELEGATION_TIME.replace(day=19)
    with pytest.raises((v.EvidenceError, a.AttestationError)):
        a.attest(v, h.TASKS, world.store, manifest, review, Provider(), now)


def test_cli_help_and_missing_input_never_need_provider_credentials():
    help_result = subprocess.run([sys.executable, str(PRODUCER), "--help"], text=True, capture_output=True)
    assert help_result.returncode == 0
    refused = subprocess.run([sys.executable, str(PRODUCER), "--base", "a" * 40], text=True, capture_output=True)
    assert refused.returncode == 2
    assert "--root" in refused.stderr


@pytest.mark.parametrize("mutation", [None, "changed-attestor", "changed-reader", "inactive", "wrong-digest",
                                      "wrong-path", "foreign-repo", "non-commit", "not-history"])
def test_only_selected_protected_bytes_are_loaded_before_provider_use(tmp_path, mutation):
    script = tmp_path / "attest-delegated-evidence.py"
    script.write_bytes(b"# Synthetic attestor bytes; never executed\n")
    ref = dict(repository=a.COORDINATOR, commit="6" * 40, path=a.FEATURE + "/attest-delegated-evidence.py",
               sha256=a.sha(script.read_bytes()))
    if mutation == "wrong-digest": ref["sha256"] = "a" * 64
    if mutation == "wrong-path": ref["path"] = "arbitrary.py"
    if mutation == "foreign-repo": ref["repository"] = "foreign/repository"
    if mutation == "non-commit": ref["commit"] = "branch-name"
    companion = script.with_name("verify-evidence.py")
    companion.write_text("DELEGATION_PRODUCER_REF = " + repr(None if mutation == "inactive" else ref) + "\n")
    protected_script, protected_reader = script.read_bytes(), companion.read_bytes()
    marker = tmp_path / "untrusted-import-ran"
    if mutation == "changed-attestor": script.write_bytes(b"# Candidate copy, not protected bytes\n")
    if mutation == "changed-reader":
        companion.write_text("from pathlib import Path\nPath(" + repr(str(marker)) + ").write_text('unsafe')\n")
    class Provider:
        def qualified_base(self, base): assert base == "a" * 40
        def content(self, path, base):
            return protected_reader if path.endswith("/verify-evidence.py") else protected_script
        def get(self, path):
            assert path == "repos/" + a.COORDINATOR + "/compare/" + "6" * 40 + "..." + "a" * 40
            return dict(status="diverged" if mutation == "not-history" else "ahead",
                        merge_base_commit=dict(sha="6" * 40))
    if mutation:
        with pytest.raises(a.AttestationError):
            a.load_protected_reader(Provider(), "a" * 40, script)
    else:
        loaded = a.load_protected_reader(Provider(), "a" * 40, script)
        assert loaded.DELEGATION_PRODUCER_REF == ref
    assert not marker.exists()


@pytest.mark.parametrize("conclusion", ["skipped", "neutral", "failure"])
def test_successful_sonar_job_requires_evaluated_gate_step(conclusion):
    checks = [dict(name=name, head_sha="a" * 40, status="completed", conclusion="success")
              for name in ("pytest-suite", "doc-health-py314", "sonar-analysis")]
    checks[-1]["details_url"] = "https://github.com/opensoft/openXfactory/actions/runs/10/job/30"
    provider = base_provider(checks)
    original = provider.get
    def get(path, **kwargs):
        value = original(path, **kwargs)
        if path.endswith("/actions/jobs/30"): value["steps"][1]["conclusion"] = conclusion
        return value
    provider.get = get
    with pytest.raises(a.AttestationError, match="not actually evaluated"):
        provider.qualified_base("a" * 40)


@pytest.mark.parametrize("mutation", [None, "latest-failed", "latest-pending", "wrong-head", "incomplete-runs",
                                      "incomplete-jobs", "missing-job", "duplicate-job"])
def test_secondary_requires_latest_exact_source_lane_and_one_measured_job(mutation):
    revision = "a" * 40
    runs = [dict(id=10, head_sha=revision, run_attempt=1, status="completed", conclusion="success"),
            dict(id=11, head_sha=revision, run_attempt=2, status="completed", conclusion="success")]
    if mutation == "latest-failed": runs[-1]["conclusion"] = "failure"
    if mutation == "latest-pending": runs[-1]["status"] = "in_progress"
    if mutation == "wrong-head":
        for run in runs: run["head_sha"] = "b" * 40
    jobs = [dict(id=20, name="doc-health-py314")]
    if mutation == "missing-job": jobs = []
    if mutation == "duplicate-job": jobs *= 2
    provider = a.GitHub()
    def get(path, **kwargs):
        if "/workflows/" in path:
            assert path.endswith("?head_sha=" + revision + "&per_page=100")
            return dict(total_count=len(runs) + int(mutation == "incomplete-runs"), workflow_runs=runs)
        assert path.endswith("/runs/11/attempts/2/jobs?per_page=100")
        return dict(total_count=len(jobs) + int(mutation == "incomplete-jobs"), jobs=jobs)
    provider.get = get
    calls = []
    provider.observation = lambda *args: calls.append(args) or {"qualified": True}
    suites = {a.FEATURE + "/tests/test_delegated_evidence.py": 1}
    if mutation:
        with pytest.raises(a.AttestationError):
            provider.secondary(revision, suites)
        assert calls == []
    else:
        assert provider.secondary(revision, suites) == {"qualified": True}
        assert calls == [(a.COORDINATOR, 11, 20, suites)]


@pytest.mark.parametrize("mode", ["manifest", "source-decision"])
def test_main_reads_candidate_only_as_data_and_emits_unregistered_review(source_fixture, tmp_path, monkeypatch, capsys, mode):
    world, proof, _, _ = source_fixture
    v = h.v
    primary, secondary = deepcopy(proof["provider_observations"])
    class Provider:
        def observation(self, *args): return primary
        def secondary(self, *args): return secondary
    class Clock:
        @staticmethod
        def now(tz):
            return h.DELEGATION_TIME.replace(day=19)
    monkeypatch.setattr(a, "datetime", Clock)
    monkeypatch.setattr(a, "GitHub", Provider)
    monkeypatch.setattr(a, "load_protected_reader", lambda *args: v)
    monkeypatch.setattr(v, "GitStore", lambda roots: world.store)
    monkeypatch.setattr(v, "load_contract", lambda root: h.TASKS)
    roots = tmp_path / "roots.json"
    roots.write_text(json.dumps({a.COORDINATOR: str(ROOT)}))
    if mode == "manifest":
        selected = ["--manifest", json.dumps(proof["subject"]["reviewed_manifest"]),
                    "--independent-review", json.dumps(proof["independent_review"])]
        expected = proof["subject"]
    else:
        _, decision, review, evidence, expected = source_decision_fixture(source_fixture)
        selected = ["--source-decision", json.dumps(decision), "--independent-review", json.dumps(review)]
        for ref in evidence:
            selected.extend(("--evidence", json.dumps(ref)))
    monkeypatch.setattr(sys, "argv", [str(PRODUCER), "--base", "a" * 40, "--root", str(ROOT),
                                     "--roots", str(roots), *selected])
    a.main()
    result = json.loads(capsys.readouterr().out)
    assert result["subject"] == expected
    assert result["actor"] == "Codex"
    assert v.DELEGATED_ATTESTATIONS == {}


@pytest.mark.parametrize("workflow", ["pytest-suite.yml", "doc-health-py314.yml"])
@pytest.mark.parametrize("mutation", [None, "missing", "extra", "duplicate", "failure", "error", "skipped"])
def test_actual_ci_formatter_emits_only_fully_measured_unique_passing_suites(tmp_path, workflow, mutation):
    import ast
    import os
    import xml.etree.ElementTree as ET
    import yaml
    value = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    steps = value["jobs"][workflow.removesuffix(".yml")]["steps"]
    step = next(item for item in steps if item.get("name") in {
        "Run private-connectivity production source suites (043)", "Exercise source proof under Python 3.14 (043)"})
    command = "python3" if workflow == "pytest-suite.yml" else "python"
    program = step["run"].split(command + " - <<'PY'\n", 1)[1].split("\nPY", 1)[0]
    tree = ast.parse(program)
    expected = next(ast.literal_eval(node.value) for node in tree.body
                    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "expected"
                                                          for target in node.targets))
    xml = ET.Element("testsuites")
    suite = ET.SubElement(xml, "testsuite", tests=str(sum(expected.values())), failures="0", errors="0", skipped="0")
    for classname, count in expected.items():
        for index in range(count):
            ET.SubElement(suite, "testcase", classname=classname, name="case-" + str(index))
    cases = list(suite)
    if mutation == "missing": suite.remove(cases[0])
    if mutation == "extra": ET.SubElement(suite, "testcase", classname="unknown.suite", name="case-0")
    if mutation == "duplicate": cases[1].set("name", cases[0].get("name"))
    if mutation in ("failure", "error", "skipped"): ET.SubElement(cases[0], mutation)
    filename = "private-connectivity-043-source.xml" if workflow == "pytest-suite.yml" else "pc043-py314.xml"
    ET.ElementTree(xml).write(tmp_path / filename)
    result = subprocess.run([sys.executable, "-c", program], cwd=ROOT,
                            env={"PATH": os.environ["PATH"], "RUNNER_TEMP": str(tmp_path),
                                 "PC043_EXPECTED_REVISION": "a" * 40},
                            text=True, capture_output=True, timeout=20)
    if mutation:
        assert result.returncode != 0
        assert a.MARKER not in result.stdout
    else:
        assert result.returncode == 0, result.stderr
        markers = [line for line in result.stdout.splitlines() if line.startswith(a.MARKER)]
        assert len(markers) == 1
        marker = json.loads(markers[0][len(a.MARKER):])
        assert marker == dict(schema="043-collected-suites-v1", source_revision="a" * 40,
                              suites={a.FEATURE + "/tests/" + name.rsplit(".", 1)[-1] + ".py": count
                                      for name, count in expected.items()})


def source_decision_fixture(source_fixture, kind="C-02", mutation=None):
    world, _, panel, _ = source_fixture
    v = h.v
    scope = deepcopy(world.trust["bindings"]["T007"]["scope"])
    body = dict(schema="043-delegated-source-decision-v1", id="synthetic-source-choice", kind=kind,
                decision="accepted", owner="Codex", actor="Codex", accountable_owner="Brett Heap",
                scope=scope, valid_from="2026-11-17T09:00:00Z", valid_until="until-superseded",
                reviewed_at="2026-11-18T01:01:00Z")
    output = world.store.put(dict(scope=scope, exit_code=0, ended_at="2026-11-18T00:01:00Z"),
                             "exports/completed-source-output.json")
    evidence = [output]
    if kind == "source-authority":
        body.update(mode="source", roles=["synthetic-source-owner"], decisions={})
    elif kind == "evidence-admission":
        authority = world.store.put(dict(scope=scope, mode="source", decision="accepted"), "source/authority.json")
        body.update(roles=["synthetic-source-custodian"], authority=authority, reviewed_output_sha256=output["sha256"])
    else:
        body["details"] = {"source_only": True}
        if kind == "C-13": body["reruns"] = [output]
    if mutation == "runtime": body["scope"]["phase"] = "production"
    if mutation == "external": body["scope"]["customer"] = "external customer"
    if mutation == "human-actor": body["owner"] = "Brett Heap"
    if mutation == "extra-field": body["waiver"] = True
    if mutation == "bad-time": body["reviewed_at"] = "2026-11-17T08:00:00Z"
    if mutation == "future": body["reviewed_at"] = "2026-11-20T00:00:00Z"
    if mutation == "bad-validity": body["valid_until"] = body["valid_from"]
    if mutation == "missing-evidence": evidence = []
    if mutation == "duplicate-evidence": evidence *= 2
    if mutation == "foreign-evidence":
        evidence = [world.store.put(b"Synthetic unknown owner", "source/plan.md", repository="foreign/source")]
    if mutation == "effect-channel": body["mode"] = "managed-push"
    if mutation == "unreviewed-output": body["reviewed_output_sha256"] = "a" * 64
    if mutation == "missing-rerun": body["reruns"] = []
    if mutation == "late-rerun":
        late = world.store.put(dict(scope=scope, exit_code=0, ended_at="2026-11-18T02:00:00Z"), "exports/late-output.json")
        evidence = body["reruns"] = [late]
    subject = dict(kind="decision", definition=v.DEFINITION, record_sha256=v.digest(v.canonical_json(body)))
    panel = deepcopy(panel)
    panel["subject"] = subject
    panel["reviewed_at"] = "2026-11-18T01:00:00Z"
    review = world.store.put(panel, "reviews/source-choice-panel.json")
    ref = world.store.put(body, "reviews/source-choice.json")
    return world, ref, review, evidence, subject


def _assert_original_t010_scope_carry(tmp_path):
    successor = h.v
    store = successor.GitStore({successor.COORDINATOR: str(ROOT)})
    predecessor = successor.QA_EDGE_PREDECESSOR
    reader_path = tmp_path / "predecessor_reader.py"
    reader_path.write_bytes(store.blob(predecessor["reader"]))
    v = load(reader_path, "exact_t010_custody_reader")
    assert v.DEFINITION == predecessor["definition"]
    ref = v.T010_ORIGINAL_SCOPE_PROOF
    stored_proof = v.decode(v._pinned_blob(store, ref))
    decision = v.decode(v._pinned_blob(store, stored_proof["evidence"][0]))
    decision["delegation"] = ref
    reader = SimpleNamespace(definition=v.DEFINITION, store=store, now=h.DELEGATION_TIME.replace(day=19),
                             trust={"revoked_authorities": []})
    binding = {"task": "T010", "scope": decision["scope"]}
    v.Verifier.delegated_decision(reader, decision, binding)
    original_grant_id = reader.delegated_root_id

    current = SimpleNamespace(definition=successor.DEFINITION, store=store, now=reader.now,
                              trust={"revoked_authorities": []})
    with pytest.raises(successor.EvidenceError, match="delegated output is not independently qualified"):
        successor.Verifier.delegated_decision(current, decision, binding)

    mismatches = (
        ({**decision, "id": decision["id"] + "-changed"}, binding, False),
        ({**decision, "delegation": {**ref, "commit": "f" * 40}}, binding, False),
        (decision, {**binding, "task": "T015"}, False),
        (decision, {**binding, "scope": {**binding["scope"], "phase": "staging",
                                        "customer": "Opensoft Inc"}}, False),
        (decision, binding, True),
    )
    for altered, task_binding, post_run in mismatches:
        with pytest.raises(v.EvidenceError, match="delegated output is not independently qualified"):
            v.Verifier.delegated_decision(reader, altered, task_binding, post_run=post_run)
    reader.definition = "f" * 64
    with pytest.raises(v.EvidenceError, match="delegated output is not independently qualified"):
        v.Verifier.delegated_decision(reader, decision, binding)
    reader.definition = v.DEFINITION
    reader.trust["revoked_authorities"] = [original_grant_id]
    with pytest.raises(v.EvidenceError, match="revoked"):
        v.Verifier.delegated_decision(reader, decision, binding)

    predecessor = v.T010_CUSTODY_PREDECESSOR["reference"]
    v.validate_historical_binding("T010", predecessor)
    with pytest.raises(v.EvidenceError, match="unaccepted historical task"):
        v.validate_historical_binding("T015", predecessor)
    with pytest.raises(v.EvidenceError, match="wrong commissioning manifest"):
        v.make_verifier(h.TASKS, store, predecessor, reader.now)


def _assert_protected_predecessor_transition(monkeypatch):
    v = h.v
    ref = v.T010_CUSTODY_PREDECESSOR["reference"]
    store = v.GitStore({v.COORDINATOR: str(ROOT)})
    active = v._pinned_blob(store, ref)
    base = "a" * 40
    events = []

    def read_base(expected):
        assert expected == base
        events.append("protected base")

    def read_control(path, expected):
        assert (path, expected) == (v.COMMISSIONING_PATH, base)
        events.append("active control")
        return active

    def verify(key):
        assert key == "T010"
        events.append("T010")

    def previous(selected_store, selected_ref, now):
        assert selected_store is store and selected_ref == ref
        return SimpleNamespace(verify=verify)

    def branch_readback(path):
        assert path == "repos/" + v.COORDINATOR + "/branches/main"
        events.append("final branch readback")
        return {"protected": True, "commit": {"sha": base}}

    monkeypatch.setattr(v, "historical_verifier", previous)
    provider = SimpleNamespace(qualified_base=read_base, content=read_control, get=branch_readback)
    v.verify_t010_transition_predecessor(provider, store, base)
    assert events == ["protected base", "active control", "T010", "protected base", "final branch readback"]

    events.clear()
    provider.content = lambda *_: b"changed active control"
    with pytest.raises(v.EvidenceError, match="no longer selects the T010 predecessor"):
        v.verify_t010_transition_predecessor(provider, store, base)
    assert events == ["protected base"]

    def moving_base(expected):
        read_base(expected)
        if events.count("protected base") == 2:
            raise a.AttestationError("selected base is not current protected main")

    events.clear()
    provider.content = read_control
    provider.qualified_base = moving_base
    with pytest.raises(a.AttestationError, match="not current protected main"):
        v.verify_t010_transition_predecessor(provider, store, base)
    assert events == ["protected base", "active control", "T010", "protected base"]

    checks = [dict(name=name, head_sha=base, status="completed", conclusion="success")
              for name in ("pytest-suite", "doc-health-py314", "sonar-analysis")]
    checks[-1]["details_url"] = "https://github.com/opensoft/openXfactory/actions/runs/10/job/30"
    for stale in ({"protected": True, "commit": {"sha": "e" * 40}},
                  {"protected": False, "commit": {"sha": base}}):
        live = base_provider(checks)
        read_provider = live.get
        branch = {"protected": True, "commit": {"sha": base}}
        branch_reads = []

        def get(path, **kwargs):
            if path.endswith("/branches/main"):
                branch_reads.append(deepcopy(branch))
                return deepcopy(branch)
            response = read_provider(path, **kwargs)
            if path.endswith("/actions/jobs/30") and len(branch_reads) == 2:
                branch.update(stale)
            return response

        events.clear()
        live.content = read_control
        live.get = get
        with pytest.raises(v.EvidenceError, match="protected main changed during T010"):
            v.verify_t010_transition_predecessor(live, store, base)
        original = {"protected": True, "commit": {"sha": base}}
        assert branch_reads == [original, original, stale]
        assert events == ["active control", "T010"]


@pytest.mark.parametrize("kind", ["C-01", "C-02", "C-08", "C-13", "source-authority", "evidence-admission"])
def test_source_decisions_are_reviewed_data_and_remain_unregistered(source_fixture, kind, monkeypatch, tmp_path):
    world, ref, review, evidence, subject = source_decision_fixture(source_fixture, kind)
    result = a.attest_source_decision(h.v, world.store, ref, review, evidence, h.DELEGATION_TIME.replace(day=19))
    assert result["subject"] == subject
    assert result["provider_observations"] == []
    assert result["evidence"] == [ref, *evidence]
    assert h.v.DELEGATED_ATTESTATIONS == {}
    if kind == "C-01":
        v = h.v
        signed = world.store.put(result, "reviews/fresh-source-attestation.json")
        monkeypatch.setitem(v.DELEGATED_ATTESTATIONS, v.digest(v.canonical_json(subject)), signed)
        fresh = v.decode(world.store.blob(ref))
        fresh["delegation"] = signed
        reader = SimpleNamespace(definition=v.DEFINITION, store=world.store, now=h.DELEGATION_TIME.replace(day=19),
                                 trust={"revoked_authorities": []})
        v.Verifier.delegated_decision(reader, fresh, {"task": "T010", "scope": fresh["scope"]})
        assert reader.delegated_root_id
        _assert_original_t010_scope_carry(tmp_path)
        _assert_protected_predecessor_transition(monkeypatch)


@pytest.mark.parametrize("kind,mutation", [
    ("C-02", "runtime"), ("C-02", "external"), ("C-02", "human-actor"), ("C-02", "extra-field"),
    ("C-02", "bad-time"), ("C-02", "future"), ("C-02", "bad-validity"), ("C-02", "missing-evidence"),
    ("C-02", "duplicate-evidence"), ("C-02", "foreign-evidence"), ("source-authority", "effect-channel"),
    ("evidence-admission", "unreviewed-output"), ("C-13", "missing-rerun"), ("C-13", "late-rerun"),
    ("C-09", None), ("C-10", None), ("C-11", None), ("C-12", None), ("grant", None),
])
def test_source_decision_entry_point_cannot_supply_runtime_or_unreviewed_authority(source_fixture, kind, mutation):
    world, ref, review, evidence, _ = source_decision_fixture(source_fixture, kind, mutation)
    with pytest.raises((a.AttestationError, h.v.EvidenceError)):
        a.attest_source_decision(h.v, world.store, ref, review, evidence, h.DELEGATION_TIME.replace(day=19))


def test_verified_reader_snapshot_wins_over_ordinary_stale_cache(tmp_path):
    import os
    import py_compile
    script = tmp_path / "attest-delegated-evidence.py"
    script.write_bytes(b"# Synthetic selected attestor\n")
    ref = dict(repository=a.COORDINATOR, commit="6" * 40, path=a.FEATURE + "/attest-delegated-evidence.py",
               sha256=a.sha(script.read_bytes()))
    companion = script.with_name("verify-evidence.py")
    prefix = "DELEGATION_PRODUCER_REF = " + repr(ref) + "\n"
    companion.write_text(prefix + 'SOURCE_VERSION = "old"\n')
    metadata = companion.stat()
    py_compile.compile(str(companion), doraise=True, invalidation_mode=py_compile.PycInvalidationMode.TIMESTAMP)
    companion.write_text(prefix + 'SOURCE_VERSION = "new"\n')
    os.utime(companion, ns=(metadata.st_atime_ns, metadata.st_mtime_ns))
    selected_source = companion.read_bytes()
    class Provider:
        def qualified_base(self, base): assert base == "a" * 40
        def content(self, path, base):
            return selected_source if path.endswith("/verify-evidence.py") else script.read_bytes()
        def get(self, path):
            return dict(status="ahead", merge_base_commit=dict(sha="6" * 40))
    reader = a.load_protected_reader(Provider(), "a" * 40, script)
    assert reader.SOURCE_VERSION == "new"


def test_primary_decision_reference_requires_an_accepted_source_owner(source_fixture):
    world, ref, review, evidence, _ = source_decision_fixture(source_fixture)
    foreign = world.store.put(world.store.blob(ref), ref["path"], repository="foreign/source")
    with pytest.raises(a.AttestationError, match="owner"):
        a.attest_source_decision(h.v, world.store, foreign, review, evidence, h.DELEGATION_TIME.replace(day=19))
