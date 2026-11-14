"""Synthetic Git/HTTP controls for bounded source proof; no live credentials."""

import importlib.util
import hashlib
import json
import os
from pathlib import Path
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "specs/043-private-connectivity-production/prepare-source-roots.py"
spec = importlib.util.spec_from_file_location("source_roots_043", HELPER)
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)
LOCAL = "opensoft/openxfactory"
FOREIGN = "opensoft/headscale-install"


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def repo(path, name=LOCAL):
    path.mkdir()
    git(path, "init", "-q")
    git(path, "config", "user.name", "Synthetic source proof")
    git(path, "config", "user.email", "source-proof@example.invalid")
    git(path, "remote", "add", "origin", "https://github.com/" + name + ".git")
    return path


def commit(path, value):
    target = path / s.COMMISSIONING
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value))
    git(path, "add", ".")
    git(path, "commit", "-qm", "Synthetic record")
    return git(path, "rev-parse", "HEAD")


def record(owner=FOREIGN, pin="a" * 40):
    return {"source": {"repository": owner, "revision": pin},
            "pin_inventory": [{"repository": owner, "foreign_commit": pin}]}


def test_closed_record_discovery_uses_committed_data_only(tmp_path):
    root = repo(tmp_path / "coordinator")
    commit(root, record())
    (root / s.COMMISSIONING).write_text(json.dumps(record("unknown/repo")))
    assert s.discover(root) == {FOREIGN: ["a" * 40]}


def test_read_only_coordinator_discovery_preserves_an_existing_ssh_origin(tmp_path):
    root = repo(tmp_path / "coordinator")
    commit(root, record())
    git(root, "remote", "set-url", "origin", "git@github.com:Opensoft/openXfactory.git")
    git(root, "config", "url.https://example.invalid/github/.insteadOf", "git@github.com:")
    assert s.discover(root) == {FOREIGN: ["a" * 40]}
    assert git(root, "config", "--get", "remote.origin.url") == "git@github.com:Opensoft/openXfactory.git"


@pytest.mark.parametrize("mutation", ["unknown", "short", "duplicate", "wrong-field", "missing", "extra-key"])
def test_discovery_refuses_unbounded_or_incomplete_inventory(tmp_path, mutation):
    root = repo(tmp_path / "coordinator")
    value = record()
    row = value["pin_inventory"][0]
    if mutation == "unknown": row["repository"] = "unknown/repo"
    if mutation == "short": row["foreign_commit"] = "a" * 7
    if mutation == "duplicate": value["pin_inventory"].append(dict(row))
    if mutation == "wrong-field": row["openxfactory_commit"] = row.pop("foreign_commit")
    if mutation == "missing": value.pop("pin_inventory")
    if mutation == "extra-key": row["url"] = "https://example.invalid"
    commit(root, value)
    with pytest.raises(ValueError): s.discover(root)


def test_no_foreign_data_requires_neither_credentials_nor_trusted_producer(tmp_path):
    root = repo(tmp_path / "coordinator")
    commit(root, {"source": {"repository": LOCAL, "revision": "b" * 40},
                  "pin_inventory": [{"repository": LOCAL, "openxfactory_commit": "b" * 40}]})
    assert s.discover(root) == {}
    assert s.producer(root, "HEAD", tmp_path / "unused.py", {}) is None
    assert s.validate_roots(root, {}, "{}") == {}


def test_unreviewed_producer_is_refused_before_credentials(tmp_path):
    root = repo(tmp_path / "coordinator")
    commit(root, record())
    with pytest.raises(ValueError, match="producer"):
        s.producer(root, "HEAD", tmp_path / "producer.py", {FOREIGN: ["a" * 40]})
    assert not (tmp_path / "producer.py").exists()


def write_commit(root, path, data):
    target = root / path; target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    git(root, "add", "."); git(root, "commit", "-qm", "Synthetic producer custody")
    return {"repository": LOCAL, "commit": git(root, "rev-parse", "HEAD"), "path": path,
            "sha256": hashlib.sha256(data).hexdigest()}


@pytest.mark.parametrize("mutation", [None, "pending", "changed-core", "changed-code", "wrong-owner"])
def test_producer_comes_from_authenticated_base_content(tmp_path, mutation):
    root = repo(tmp_path / "coordinator")
    code = b"# synthetic reviewed producer, never invoked with real credentials\n"
    code_ref = write_commit(root, s.SELF, code)
    value = {"schema": "043-reviewed-trust-v1", "feature": "043-private-connectivity-production",
             "source_ci_producer": code_ref, "review": {}}
    manifest = write_commit(root, s.COMMISSIONING, json.dumps(value).encode())
    auth = {"schema": "043-source-authentication-v1", "decision": "accepted", "custodian": "Brett Heap",
            "reviewed_manifest": manifest, "content_sha256": s._core(value), "reviewed_at": "2026-01-01T00:00:00Z"}
    if mutation == "pending": auth["decision"] = "pending"
    if mutation == "changed-core": auth["content_sha256"] = "a" * 64
    if mutation == "wrong-owner": code_ref["repository"] = "unaccepted/repo"
    value["review"] = write_commit(root, s.AUTHENTICATION, ("```json\n" + json.dumps(auth) + "\n```\n").encode())
    base = write_commit(root, s.COMMISSIONING, json.dumps(value).encode())["commit"]
    if mutation == "changed-code":
        git(root, "replace", code_ref["commit"], base)
        # A replacement cannot change which immutable bytes the reader uses.
        code_ref["sha256"] = "b" * 64
        value["source_ci_producer"] = code_ref
        base = write_commit(root, s.COMMISSIONING, json.dumps(value).encode())["commit"]
    destination = tmp_path / "selected.py"
    if mutation:
        with pytest.raises(ValueError): s.producer(root, base, destination, {FOREIGN: ["a" * 40]})
        assert not destination.exists()
    else:
        assert s.producer(root, base, destination, {FOREIGN: ["a" * 40]}) == str(destination)
        assert destination.read_bytes() == code


@pytest.mark.parametrize("failure", ["unfiltered", "missing", "timeout"])
def test_failed_fetch_never_leaves_private_proof(tmp_path, failure):
    root = repo(tmp_path / "coordinator"); commit(root, record())
    proof = tmp_path / "proof"
    def transport(directory, args, token=None):
        if args[:1] == ["fetch"]:
            if failure == "timeout": raise ValueError("synthetic bounded timeout")
            if failure == "unfiltered":
                subprocess.run(["git", "-C", str(directory), "hash-object", "-w", "--stdin"], input=b"synthetic private blob", check=True, capture_output=True)
            return b""
        return s.run_git(directory, args, token)
    with pytest.raises(ValueError):
        s.prepare(root, {FOREIGN: ["a" * 40]}, proof, {"opensoft": "synthetic-token"},
                  identities={"app_id": "4253636", "app_slug": "openxfactory", "opensoft": "145372182"},
                  api=lambda token: [{"full_name": FOREIGN, "id": s.REPOSITORIES[FOREIGN]}], runner=transport)
    assert not proof.exists()


def test_credentialed_http_redirect_is_refused():
    with pytest.raises(ValueError): s.NoRedirect().redirect_request(None, None, 302, "redirect", {}, "https://example.invalid")


@pytest.mark.parametrize("workflow", ["pytest-suite.yml", "doc-health-py314.yml"])
@pytest.mark.parametrize("private,accepted", [(False, False), (True, False), (True, True)])
def test_workflow_bootstrap_never_executes_candidate_code(tmp_path, workflow, private, accepted):
    import yaml
    root = repo(tmp_path / "coordinator")
    code_ref = write_commit(root, s.SELF, HELPER.read_bytes())
    value = {"schema": "043-reviewed-trust-v1", "feature": "043-private-connectivity-production",
             "source_ci_producer": code_ref, "review": {}, "pin_inventory": []}
    manifest = write_commit(root, s.COMMISSIONING, json.dumps(value).encode())
    auth = {"schema": "043-source-authentication-v1", "decision": "accepted" if accepted else "pending",
            "custodian": "Brett Heap", "reviewed_manifest": manifest, "content_sha256": s._core(value),
            "reviewed_at": "2026-01-01T00:00:00Z"}
    review = "```json\n" + json.dumps(auth) + "\n```\n"
    value["review"] = write_commit(root, s.AUTHENTICATION, review.encode())
    base = write_commit(root, s.COMMISSIONING, json.dumps(value).encode())["commit"]
    value["pin_inventory"] = [{"repository": LOCAL, "openxfactory_commit": code_ref["commit"]},
                              {"repository": LOCAL, "openxfactory_commit": value["review"]["commit"]}]
    if private:
        value["source"] = {"repository": FOREIGN, "revision": "a" * 40}
        value["pin_inventory"].append({"repository": FOREIGN, "foreign_commit": "a" * 40})
    write_commit(root, s.SELF, b"from pathlib import Path\nPath('CANDIDATE_EXECUTED').touch()\nraise SystemExit(99)\n")
    write_commit(root, s.COMMISSIONING, json.dumps(value).encode())
    runner = tmp_path / "runner"; runner.mkdir()
    out = runner / "output"; envfile = runner / "env"
    definition = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    steps = definition["jobs"][workflow.removesuffix(".yml")]["steps"]
    script = next(step["run"] for step in steps if step.get("id") == "pc043_plan")
    result = subprocess.run(["bash", "-eu", "-c", script], cwd=root, capture_output=True, text=True,
                            env={**os.environ, "RUNNER_TEMP": str(runner), "GITHUB_OUTPUT": str(out),
                                 "GITHUB_ENV": str(envfile), "PC_SOURCE_BASE": base})
    assert not (root / "CANDIDATE_EXECUTED").exists()
    if private and not accepted:
        assert result.returncode != 0 and not out.exists()
    else:
        assert result.returncode == 0, result.stderr
        assert ("required=true" if private else "required=false") in out.read_text()
        if private: assert (runner / "pc043-reviewed-producer.py").read_bytes() == HELPER.read_bytes()


def test_real_filtered_commit_store_contains_no_source_or_credentials(tmp_path):
    source = repo(tmp_path / "private", FOREIGN)
    pin = commit(source, {"synthetic": "private bytes never copied into proof"})
    root = repo(tmp_path / "coordinator")
    commit(root, record(pin=pin))
    calls = []

    def transport(directory, args, token=None):
        calls.append((args, token))
        if args[:1] == ["fetch"]:
            args = ["-c", "protocol.file.allow=always", *("file://" + str(source) if a == "origin" else a for a in args)]
        return s.run_git(directory, args, token)

    git(source, "config", "uploadpack.allowFilter", "true")
    proof = tmp_path / "proof"
    roots = s.prepare(root, {FOREIGN: [pin]}, proof, {"opensoft": "synthetic-token"},
                      identities={"app_id": "4253636", "app_slug": "openxfactory", "opensoft": "145372182"},
                      api=lambda token: [{"full_name": FOREIGN, "id": s.REPOSITORIES[FOREIGN]}], runner=transport)
    assert s.validate_roots(root, {FOREIGN: [pin]}, json.dumps(roots)) == roots
    objects = git(Path(roots[FOREIGN]), "cat-file", "--batch-all-objects", "--batch-check=%(objecttype)")
    assert set(objects.splitlines()) == {"commit"}
    assert "synthetic-token" not in (Path(roots[FOREIGN]) / "config").read_text()
    assert [token for args, token in calls if token] == ["synthetic-token"]
    s.cleanup(proof)
    assert not proof.exists()


@pytest.mark.parametrize("mutation", ["missing", "unknown", "coordinator", "alias", "wrong-origin", "full-tree"])
def test_explicit_roots_never_borrow_coordinator_or_full_private_tree(tmp_path, mutation):
    root = repo(tmp_path / "coordinator")
    pin = commit(root, {"synthetic": True})
    other = repo(tmp_path / "other", FOREIGN)
    commit(other, {"synthetic": True})
    mapping = {FOREIGN: str(other)}
    if mutation == "missing": mapping = {}
    if mutation == "unknown": mapping["unknown/repo"] = str(other)
    if mutation == "coordinator": mapping[LOCAL] = str(root)
    if mutation == "alias": mapping[FOREIGN] = str(root)
    if mutation == "wrong-origin": git(other, "remote", "set-url", "origin", "https://github.com/unknown/repo")
    with pytest.raises(ValueError): s.validate_roots(root, {FOREIGN: [pin]}, json.dumps(mapping))


@pytest.mark.parametrize("mutation", ["token", "app", "slug", "installation", "repo-id", "scope"])
def test_preparation_refuses_identity_scope_or_missing_credentials_before_fetch(tmp_path, mutation):
    root = repo(tmp_path / "coordinator")
    commit(root, record())
    identities = {"app_id": "4253636", "app_slug": "openxfactory", "opensoft": "145372182"}
    tokens = {"opensoft": "synthetic-token"}
    available = [{"full_name": FOREIGN, "id": s.REPOSITORIES[FOREIGN]}]
    if mutation == "token": tokens = {}
    if mutation == "app": identities["app_id"] = "1"
    if mutation == "slug": identities["app_slug"] = "other-app"
    if mutation == "installation": identities["opensoft"] = "1"
    if mutation == "repo-id": available[0]["id"] = 1
    if mutation == "scope": available.append({"full_name": "opensoft/xfactory-installer", "id": s.REPOSITORIES["opensoft/xfactory-installer"]})
    with pytest.raises(ValueError):
        s.prepare(root, {FOREIGN: ["a" * 40]}, tmp_path / "proof", tokens, identities=identities,
                  api=lambda token: available, runner=lambda *args: pytest.fail("identity failure reached Git"))
    assert not (tmp_path / "proof").exists()


def test_duplicate_root_json_and_symlink_cleanup_are_refused(tmp_path):
    root = repo(tmp_path / "coordinator")
    commit(root, {"pin_inventory": []})
    with pytest.raises(ValueError): s.validate_roots(root, {}, '{"x":"one","x":"two"}')
    target = tmp_path / "unowned"; target.mkdir()
    link = tmp_path / "proof"; link.symlink_to(target, target_is_directory=True)
    with pytest.raises(ValueError): s.cleanup(link)
    assert target.is_dir()


def test_git_environment_removes_ambient_credentials_and_disables_lazy_reads(monkeypatch):
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", "secret")
    monkeypatch.setenv("GH_TOKEN", "secret")
    env = s.git_environment()
    assert "GH_TOKEN" not in env and "GIT_CONFIG_VALUE_0" not in env
    assert env["GIT_NO_LAZY_FETCH"] == "1" and env["GIT_TERMINAL_PROMPT"] == "0"


@pytest.mark.parametrize("workflow", ["pytest-suite.yml", "doc-health-py314.yml"])
def test_both_ci_lanes_revoke_before_tests_and_cleanup_afterwards(workflow):
    import yaml
    value = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    steps = value["jobs"][workflow.removesuffix(".yml")]["steps"]
    named = {step.get("id"): index for index, step in enumerate(steps) if step.get("id")}
    assert named["pc043_plan"] < named["pc043_opensoft_token"] < named["pc043_prepare"] < named["pc043_revoke"]
    tests = [i for i, step in enumerate(steps) if "pytest " in step.get("run", "")]
    assert tests and named["pc043_revoke"] < min(tests) < named["pc043_cleanup"]
    for name in ("pc043_opensoft_token", "pc043_domain_token"):
        step = steps[named[name]]
        assert step["with"]["permission-contents"] == "read"
        assert step["with"]["repositories"]
        assert "MERGE_MASTER" not in json.dumps(step)
    assert steps[named["pc043_revoke"]]["if"] == "always()"
    assert steps[named["pc043_cleanup"]]["if"] == "always()"
    if workflow == "doc-health-py314.yml":
        qualification = next(step for step in steps if step.get("name") == "Exercise source proof under Python 3.14 (043)")
        assert "PC043_EXPECTED_REVISION" in qualification["env"]
        assert "worktree add --detach" in qualification["run"] and "--junitxml=" in qualification["run"]
