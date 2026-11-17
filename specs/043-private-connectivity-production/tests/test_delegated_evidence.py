"""Bounded attestor regressions; every provider and activation is synthetic."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

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


def test_main_reads_candidate_only_as_data_and_emits_unregistered_review(source_fixture, tmp_path, monkeypatch, capsys):
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
    monkeypatch.setattr(sys, "argv", [str(PRODUCER), "--base", "a" * 40, "--root", str(ROOT),
                                     "--roots", str(roots), "--manifest", json.dumps(proof["subject"]["reviewed_manifest"]),
                                     "--independent-review", json.dumps(proof["independent_review"])])
    a.main()
    result = json.loads(capsys.readouterr().out)
    assert result["subject"] == proof["subject"]
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
