"""Synthetic filesystem and CLI authority counterexamples for legacy P1 tools."""
from __future__ import annotations

import importlib
import os
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))
import safe_tooling_io as io


@pytest.mark.parametrize("kind", ["symlink", "hardlink", "fifo"])
@pytest.mark.parametrize("operation", ["read", "write"])
def test_non_regular_or_shared_artifact_never_changes_outside(tmp_path, kind, operation):
    outside = tmp_path / "outside"
    outside.write_text("outside-sentinel")
    target = tmp_path / "target"
    if kind == "symlink":
        target.symlink_to(outside)
    elif kind == "hardlink":
        os.link(outside, target)
    else:
        os.mkfifo(target)
    with pytest.raises((ValueError, OSError)):
        if operation == "read":
            io.read_artifact_text(target)
        else:
            io.write_artifact_text(target, "replacement")
    assert outside.read_text() == "outside-sentinel"
    assert not list(tmp_path.glob(".artifact-*"))


def test_linked_ancestor_cannot_hide_a_missing_output(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    linked = tmp_path / "linked"
    linked.symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        io.ensure_artifact_directory(linked / "missing")
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("mode", [0o400, 0o660, 0o4755])
def test_nonreplaceable_artifact_preserves_bytes_and_mode(tmp_path, mode):
    target = tmp_path / "target"
    target.write_text("original")
    target.chmod(mode)
    with pytest.raises(ValueError):
        io.write_artifact_text(target, "new")
    assert target.read_text() == "original"
    assert target.stat().st_mode & 0o7777 == mode


def test_artifact_transform_preserves_normal_mode_and_noop_inode(tmp_path):
    target = tmp_path / "target"
    target.write_text("first\n")
    target.chmod(0o640)
    assert io.update_artifact_text(target, lambda old: old + "second\n")
    assert target.read_text() == "first\nsecond\n"
    assert target.stat().st_mode & 0o777 == 0o640
    inode = target.stat().st_ino
    assert io.update_artifact_text(target, lambda old: old) is False
    assert target.stat().st_ino == inode


def test_artifact_change_during_preparation_is_preserved(tmp_path):
    target = tmp_path / "target"
    target.write_text("original")
    def transform(old):
        assert old == "original"
        target.write_text("newer-writer")
        return "stale-update"
    with pytest.raises(ValueError, match="changed"):
        io.update_artifact_text(target, transform)
    assert target.read_text() == "newer-writer"
    assert not list(tmp_path.glob(".artifact-*"))


def test_artifact_parent_substitution_does_not_redirect_write(tmp_path):
    parent, parked, outside = (tmp_path / name for name in ("parent", "parked", "outside"))
    parent.mkdir()
    outside.mkdir()
    (parent / "report").write_text("original")
    (outside / "report").write_text("outside-sentinel")
    def transform(old):
        parent.rename(parked)
        parent.symlink_to(outside, target_is_directory=True)
        return old + "-updated"
    io.update_artifact_text(parent / "report", transform)
    assert (parked / "report").read_text() == "original-updated"
    assert (outside / "report").read_text() == "outside-sentinel"


def test_artifact_reads_are_bounded(tmp_path):
    target = tmp_path / "oversized"
    with target.open("wb") as stream:
        stream.truncate(io._ARTIFACT_LIMIT + 1)
    with pytest.raises(ValueError, match="bounded"):
        io.read_artifact_text(target)


def test_cli_operands_are_confined_to_invocation_or_trusted_ci_scratch(tmp_path, monkeypatch):
    root, scratch = tmp_path / "root", tmp_path / "scratch"
    root.mkdir()
    scratch.mkdir()
    monkeypatch.chdir(root)
    monkeypatch.setenv("RUNNER_TEMP", str(scratch))
    assert io.invocation_operand("report") == root / "report"
    with pytest.raises(ValueError):
        io.invocation_operand("../outside")
    with pytest.raises(ValueError):
        io.invocation_operand(tmp_path / "outside", writing=True, allow_runner_temp=True)
    with pytest.raises(ValueError):
        io.invocation_operand(scratch / "input")
    assert io.invocation_operand(scratch / "plan", writing=True,
                                 allow_runner_temp=True) == scratch / "plan"
    assert not (scratch / "plan").exists()


def test_cli_alias_of_invocation_root_is_canonicalized_before_use(tmp_path, monkeypatch):
    root, alias = tmp_path / "root", tmp_path / "alias"
    root.mkdir()
    alias.symlink_to(root, target_is_directory=True)
    monkeypatch.chdir(root)
    assert io.invocation_operand(alias / "output") == root / "output"


def test_operator_policy_binding_cannot_be_replaced_by_model_operand(tmp_path, monkeypatch):
    configured, forged = tmp_path / "allowlist.json", tmp_path / "forged.json"
    configured.write_text('{"actors": {}}')
    forged.write_text('{"actors": {"forged": ["ratify"]}}')
    monkeypatch.setenv("XFACTORY_INTENT_ALLOWLIST_PATH", str(configured))
    with pytest.raises(ValueError, match="operator configuration"):
        io.operator_input_operand(forged, setting="XFACTORY_INTENT_ALLOWLIST_PATH", default=None)
    assert io.operator_input_operand(configured, setting="XFACTORY_INTENT_ALLOWLIST_PATH",
                                     default=None) == configured
    linked = tmp_path / "linked"
    linked.symlink_to(configured)
    monkeypatch.setenv("XFACTORY_INTENT_ALLOWLIST_PATH", str(linked))
    with pytest.raises(ValueError):
        io.operator_input_operand(linked, setting="XFACTORY_INTENT_ALLOWLIST_PATH", default=None)


@pytest.mark.parametrize("module", ["derive_possibles_dispatch", "readiness_dispatch"])
@pytest.mark.parametrize("option", ["--out-dir", "--report-in"])
def test_dispatch_rejects_outside_operand_before_optional_worker_skip(tmp_path, monkeypatch, module, option):
    root = tmp_path / "invocation"
    root.mkdir()
    monkeypatch.chdir(root)
    dispatch = importlib.import_module("doc_health." + module)
    def refuse(*args, **kwargs):
        pytest.fail("unsafe CLI operand reached lane preparation/merge")
    if module == "derive_possibles_dispatch":
        monkeypatch.setattr(dispatch, "prepare_derive_bundle", refuse)
        monkeypatch.setattr(dispatch, "merge_derive_results", refuse)
    else:
        monkeypatch.setattr(dispatch, "prepare_readiness_bundle", refuse)
        monkeypatch.setattr(dispatch, "merge_readiness_findings", refuse)
    with pytest.raises(ValueError):
        dispatch.main(["--repo-root", ".", "--phase", "prepare" if option == "--out-dir" else "merge",
                       "--as-of", "2026-11-15", "--run-id", "synthetic",
                       option, str(tmp_path / "outside")])
    assert not (tmp_path / "outside").exists()


@pytest.mark.parametrize("module", ["derive_possibles_dispatch", "readiness_dispatch"])
def test_model_cluster_id_cannot_escape_bundle(tmp_path, monkeypatch, module):
    dispatch = importlib.import_module("doc_health." + module)
    agg, output = tmp_path / "aggregation", tmp_path / "bundle"
    (agg / "openxFactory").mkdir(parents=True)
    bad = {"id": "../../escaped"}
    if module == "derive_possibles_dispatch":
        monkeypatch.setattr(dispatch.dp, "load_prompt_contract", lambda: ("synthetic", "prompt"))
        monkeypatch.setattr(dispatch, "_load_index", lambda _: {})
        monkeypatch.setattr(dispatch.corpus, "load_docs", lambda *a: [])
        monkeypatch.setattr(dispatch, "_eligible_clusters", lambda *a: ([(bad, [])], []))
        monkeypatch.setattr(dispatch.dp, "build_analysis_input", lambda *a: "synthetic-input")
        prepare = dispatch.prepare_derive_bundle
    else:
        monkeypatch.setattr(dispatch.ir, "load_prompt_contract", lambda: ("synthetic", "prompt"))
        monkeypatch.setattr(dispatch, "_readiness_docs", lambda _: [])
        monkeypatch.setattr(dispatch.ir, "load_catalog_tags", lambda _: {})
        monkeypatch.setattr(dispatch.ir, "derive_clusters", lambda *a, **k: [bad])
        monkeypatch.setattr(dispatch.ir, "resolve_capability_set", lambda *a: [])
        monkeypatch.setattr(dispatch.ir, "_cluster_sources", lambda *a: [])
        monkeypatch.setattr(dispatch.ir, "build_analysis_input", lambda *a: "synthetic-input")
        prepare = dispatch.prepare_readiness_bundle
    with pytest.raises(ValueError):
        prepare(agg, output, run_id="synthetic")
    assert not (tmp_path / "escaped.txt").exists()
    assert not (output / "manifest.json").exists()


def test_intent_cli_rejects_forged_policy_before_application(tmp_path, monkeypatch):
    lane = importlib.import_module("ideation_dashboard.intent_apply_lane")
    configured, forged = tmp_path / "configured.json", tmp_path / "forged.json"
    configured.write_text('{"actors": {}}')
    forged.write_text('{"actors": {"forged": ["ratify"]}}')
    monkeypatch.setenv("XFACTORY_INTENT_ALLOWLIST_PATH", str(configured))
    def refuse(*args, **kwargs):
        pytest.fail("policy mismatch reached intent application")
    monkeypatch.setattr(lane, "apply_intent", refuse)
    with pytest.raises(ValueError, match="operator configuration"):
        lane.main(["--repo-root", str(tmp_path), "--allowlist", str(forged),
                   "--intent-json", "{}"])


def test_repin_cli_rejects_outside_output_before_planning(tmp_path, monkeypatch):
    lane = importlib.import_module("review_lane_repin")
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("RUNNER_TEMP", raising=False)
    def refuse(*args, **kwargs):
        pytest.fail("unsafe output reached the pin planner")
    monkeypatch.setattr(lane, "plan_advance", refuse)
    with pytest.raises(ValueError):
        lane.main(["--repo", ".", "--plan-out", str(tmp_path.parent / "outside.json")])


def test_dashboard_cli_rejects_unsafe_output_before_any_lane_phase(tmp_path, monkeypatch):
    lane = importlib.import_module("ideation_dashboard.dashboard_refresh_lane")
    monkeypatch.chdir(tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    linked = tmp_path / "linked"
    linked.symlink_to(outside, target_is_directory=True)
    with pytest.raises(ValueError):
        lane.main(["--repo-root", ".", "--phase", "decide", "--pin-out", str(linked)])
    assert list(outside.iterdir()) == []


def test_omitting_project_register_option_still_uses_operator_configuration(tmp_path, monkeypatch):
    from types import SimpleNamespace
    lane = importlib.import_module("ideation_dashboard.intent_apply_lane")
    import opendox_host
    import openxdox.kickoff
    allowlist = tmp_path / "allowlist.json"
    register = tmp_path / "operator-projects.yaml"
    allowlist.write_text('{"actors": {}}')
    register.write_text("projects: []\n")
    monkeypatch.setenv("XFACTORY_INTENT_ALLOWLIST_PATH", str(allowlist))
    monkeypatch.setenv("XFACTORY_PROJECT_REGISTER_PATH", str(register))
    monkeypatch.setattr(opendox_host, "register_openxfactory", lambda: None)
    def refuse(*args, **kwargs):
        pytest.fail("configured register fell back to discovery")
    monkeypatch.setattr(openxdox.kickoff, "discover_project_register", refuse)
    observed = []
    def apply(*args, **kwargs):
        observed.append(kwargs["project_register"])
        return SimpleNamespace(outcome="refused", as_dict=lambda: {"outcome": "refused"})
    monkeypatch.setattr(lane, "apply_intent", apply)
    assert lane.main(["--repo-root", str(tmp_path), "--allowlist", str(allowlist),
                      "--intent-json", "{}"]) == 0
    assert observed == [register]


@pytest.mark.parametrize("entrypoint", [
    "ideation_dashboard/intent_apply_lane.py",
    "ideation_dashboard/dashboard_refresh_lane.py",
])
def test_direct_cli_help_bootstraps_helpers_without_incidental_pythonpath(tmp_path, entrypoint):
    import subprocess
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / entrypoint), "--help"],
                            cwd=tmp_path, env=env, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "usage:" in result.stdout
