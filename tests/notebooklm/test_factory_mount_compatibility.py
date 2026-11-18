"""Canonical checkout paths preserve projection and workbench identities."""

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture
def sync(monkeypatch):
    script = Path(__file__).resolve().parents[2] / "scripts/sync-notebooklm-books.py"
    monkeypatch.syspath_prepend(str(script.parent))
    spec = importlib.util.spec_from_file_location("test_factory_mount_sync", script)
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    return module


def test_canonical_projection_preserves_keys_titles_and_session_ids(tmp_path, sync):
    mounts = (
        ("openxFactory", "openXfactory"),
        ("xFactories/codexFactory", "xFactories/codeXfactory"),
    )
    for legacy, _ in mounts:
        document = tmp_path / legacy / "ideation/staging/idea.md"
        document.parent.mkdir(parents=True)
        document.write_text("# Idea\n\nStatus: staged\n", encoding="utf-8")
    gitmodules = tmp_path / ".gitmodules"
    original = "".join(f'[submodule "{legacy}"]\n\tpath = {legacy}\n'
                       for legacy, _ in mounts)
    gitmodules.write_text(original, encoding="utf-8")

    before = sync.scan(tmp_path)
    assert {"ideation-openxfactory", "ideation-codexfactory"} <= before[0].keys()
    for legacy, canonical in mounts:
        (tmp_path / legacy).rename(tmp_path / canonical)
        original = original.replace(f"path = {legacy}", f"path = {canonical}")
    gitmodules.write_text(original, encoding="utf-8")

    assert sync.scan(tmp_path) == before
    assert sync.session_repositories(tmp_path) == [
        ("openxFactory", tmp_path / "openXfactory"),
        ("codexFactory", tmp_path / "xFactories/codeXfactory"),
    ]
    assert sync.repo_path(tmp_path, "codexFactory") == tmp_path / "xFactories/codeXfactory"


def test_orphan_sweep_reads_the_canonical_workbench(tmp_path, monkeypatch, sync):
    manifest_dir = tmp_path / "openXfactory/ideation/workbench"
    manifest_dir.mkdir(parents=True)
    manifest = manifest_dir / "bound.workbench.yaml"
    manifest.write_text("alias: xf-wb-bound\n", encoding="utf-8")
    adapter = SimpleNamespace(available=lambda: True)
    seen = []

    def sweep(root, supplied_adapter, *, workbench_dir):
        assert supplied_adapter is adapter
        seen.extend((root / workbench_dir).glob("*.workbench.yaml"))
        return SimpleNamespace(skipped=False, detail="fixture",
                               deleted=[], kept=["xf-wb-bound"])

    workbench = SimpleNamespace(orphan_sweep=sweep)
    monkeypatch.setattr(sync, "_dashboard_module", lambda name: workbench)
    sync.workbench_orphan_sweep(tmp_path, True, adapter)
    assert seen == [manifest]
