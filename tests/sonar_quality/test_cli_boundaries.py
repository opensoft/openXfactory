"""Behavioral witnesses for the existing CLI trust boundaries."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
from unittest.mock import Mock

import pytest

ROOT = Path(__file__).resolve().parents[2]


def load_script(filename):
    name = "_sonar_" + Path(filename).stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def invocation(tmp_path, monkeypatch):
    root = tmp_path / "invocation"
    root.mkdir()
    monkeypatch.chdir(root)
    return root


@pytest.mark.parametrize("spelling", ["absolute", "relative", "sibling", "symlink"])
def test_declaration_outside_invocation_is_not_read(invocation, spelling):
    target = invocation.parent / ("invocation-sibling" if spelling == "sibling" else "outside")
    target.mkdir()
    secret = target / "declaration.json"
    secret.write_text('{"private":"not authorized"}')
    if spelling == "relative":
        path = Path("../outside/declaration.json")
    elif spelling == "symlink":
        path = invocation / "linked.json"
        path.symlink_to(secret)
    else:
        path = secret
    module = load_script("validate-factory-mcp.py")
    value, code = module.read_declaration(path)
    assert value is None
    assert code == "input_unreadable"


def test_regular_in_root_declaration_still_reads(invocation):
    module = load_script("validate-factory-mcp.py")
    path = invocation / "declaration.json"
    path.write_text('{"kind":"synthetic"}')
    assert module.read_declaration(path) == ({"kind": "synthetic"}, None)


def test_nonregular_declaration_refuses_before_reader(invocation, monkeypatch):
    module = load_script("validate-factory-mcp.py")
    reader = Mock(return_value=b"{}")
    monkeypatch.setattr(module, "bounded_read", reader)
    value, code = module.read_declaration(invocation)
    assert value is None
    assert code == "input_unreadable"
    reader.assert_not_called()


@pytest.mark.parametrize("spelling", ["absolute", "relative", "sibling", "symlink"])
def test_census_output_cannot_escape_invocation(invocation, spelling):
    module = load_script("measure_opendox_css_census.py")
    outside = invocation.parent / ("invocation-sibling" if spelling == "sibling" else "outside")
    outside.mkdir()
    target = outside / "census.json"
    target.write_text("unchanged")
    if spelling == "relative":
        operand = "../outside/census.json"
    elif spelling == "symlink":
        linked = invocation / "census.json"
        linked.symlink_to(target)
        operand = str(linked)
    else:
        operand = str(target)
    with pytest.raises(ValueError, match="invocation"):
        module.checked_output_path(operand)
    assert target.read_text() == "unchanged"


def test_census_output_inside_invocation_is_preserved(invocation):
    module = load_script("measure_opendox_css_census.py")
    assert module.checked_output_path("census.json") == invocation / "census.json"


@pytest.mark.parametrize("operand", ["--show-toplevel", "-q", "HEAD\n--all", "HEAD\x00", ""])
def test_git_revision_rejects_unsafe_operands_before_spawn(invocation, monkeypatch, operand):
    module = load_script("validate-carve-manifest.py")
    git = Mock(return_value=subprocess.CompletedProcess([], 0, b"a" * 40 + b"\n", b""))
    monkeypatch.setattr(module, "_git", git)
    with pytest.raises(module.CarveRefusal, match="revision"):
        module.resolve_revision(invocation, operand)
    git.assert_not_called()


@pytest.mark.parametrize("output", [b"--show-toplevel\n", b"a" * 40 + b"\n" + b"b" * 40,
                                     b"not-an-object", b"\xff", b""])
def test_git_revision_rejects_malformed_resolver_output(invocation, monkeypatch, output):
    module = load_script("validate-carve-manifest.py")
    monkeypatch.setattr(module, "_git",
                        Mock(return_value=subprocess.CompletedProcess([], 0, output, b"")))
    with pytest.raises(module.CarveRefusal):
        module.resolve_revision(invocation, "HEAD")


@pytest.mark.parametrize("operand", ["HEAD", "main", "refs/heads/main", "abc1234", "a" * 40])
def test_git_revision_has_an_operand_boundary(invocation, monkeypatch, operand):
    module = load_script("validate-carve-manifest.py")
    oid = "a" * 40
    git = Mock(return_value=subprocess.CompletedProcess([], 0, (oid + "\n").encode(), b""))
    monkeypatch.setattr(module, "_git", git)
    assert module.resolve_revision(invocation, operand) == oid
    git.assert_called_once_with(invocation, "rev-parse", "--verify", "--quiet",
                                "--end-of-options", operand + "^{commit}")


def test_unknown_carved_module_refuses_before_install_or_import(monkeypatch):
    module = load_script("carved_reach.py")
    monkeypatch.setattr(module, "_rows", lambda: {})
    monkeypatch.setattr(module, "source", lambda key: Path("not-a-row"))
    install = Mock()
    importer = Mock()
    monkeypatch.setattr(module, "install", install)
    monkeypatch.setattr(module.importlib, "import_module", importer)
    with pytest.raises(module.NotACarvedPath, match="in no row"):
        module.module("scripts/not-declared.py")
    install.assert_not_called()
    importer.assert_not_called()
