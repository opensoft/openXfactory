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
                                     b"not-an-object", b"\xff", b"",
                                     b"a" * 40 + b" tree\n",
                                     b"a" * 40 + b" commit extra\n",
                                     b"a" * 40 + b" commit\n" + b"b" * 40 + b" commit\n"])
def test_git_revision_rejects_malformed_resolver_output(invocation, monkeypatch, output):
    module = load_script("validate-carve-manifest.py")
    monkeypatch.setattr(module, "_git",
                        Mock(return_value=subprocess.CompletedProcess([], 0, output, b"")))
    with pytest.raises(module.CarveRefusal):
        module.resolve_revision(invocation, "HEAD")


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


@pytest.fixture
def attester(invocation, monkeypatch):
    module = load_script("attest-openspec-cli-pin-lockfile.py")
    monkeypatch.setattr(module, "ROOT", invocation)
    (invocation / "docs").mkdir()
    return module


@pytest.mark.parametrize("record", ["../../outside", '{"path":"../escape"}', "synthetic attestation\n"])
def test_attestation_content_cannot_select_path_or_overwrite(attester, invocation, record):
    destination = attester.checked_destination(
        str(invocation / "docs" / "record.md"), invocation / "docs" / "default.md")
    attester.write_record(destination, record)
    assert destination.read_text() == record
    assert destination.stat().st_mode & 0o777 == 0o600
    with pytest.raises(attester.Refusal):
        attester.write_record(destination, "replacement")
    assert destination.read_text() == record
    assert not (invocation / "escape").exists()


def test_attestation_default_obeys_repository_boundary(attester, invocation):
    outside = invocation.parent / "outside"
    outside.mkdir()
    (invocation / "docs").rmdir()
    (invocation / "docs").symlink_to(outside, target_is_directory=True)
    with pytest.raises(attester.Refusal, match="--write"):
        attester.checked_destination("", invocation / "docs" / "default.md")
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("kind", ["file", "directory", "symlink", "broken-symlink"])
def test_attestation_existing_destination_is_never_reused(attester, invocation, kind):
    destination = invocation / "docs" / "record.md"
    if kind == "file":
        destination.write_text("dated evidence")
    elif kind == "directory":
        destination.mkdir()
    else:
        target = invocation / ("original" if kind == "symlink" else "not-created")
        if kind == "symlink":
            target.write_text("dated evidence")
        destination.symlink_to(target)
    with pytest.raises(attester.Refusal, match="--write"):
        attester.checked_destination(str(destination), invocation / "docs" / "default.md")
    if kind == "file":
        assert destination.read_text() == "dated evidence"
    elif kind == "symlink":
        assert target.read_text() == "dated evidence"
    elif kind == "broken-symlink":
        assert not target.exists()


def test_attestation_parent_swap_after_validation_cannot_escape(attester, invocation):
    destination = attester.checked_destination(
        str(invocation / "docs" / "record.md"), invocation / "docs" / "default.md")
    outside = invocation.parent / "outside"
    outside.mkdir()
    (invocation / "docs").rename(invocation / "original-docs")
    (invocation / "docs").symlink_to(outside, target_is_directory=True)
    with pytest.raises(attester.Refusal):
        attester.write_record(destination, "not an outside record")
    assert list(outside.iterdir()) == []
    assert list((invocation / "original-docs").iterdir()) == []


def test_attestation_parent_swap_during_open_is_refused(attester, invocation, monkeypatch):
    destination = attester.checked_destination(
        str(invocation / "docs" / "record.md"), invocation / "docs" / "default.md")
    outside = invocation.parent / "outside"
    outside.mkdir()
    original_open = attester.os.open
    swapped = False

    def swap_then_open(path, flags, *args, **kwargs):
        nonlocal swapped
        if Path(path) == invocation and kwargs.get("dir_fd") is None and not swapped:
            swapped = True
            (invocation / "docs").rename(invocation / "original-docs")
            (invocation / "docs").symlink_to(outside, target_is_directory=True)
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(attester.os, "open", swap_then_open)
    with pytest.raises(attester.Refusal):
        attester.write_record(destination, "not an outside record")
    assert swapped
    assert list(outside.iterdir()) == []
    assert list((invocation / "original-docs").iterdir()) == []


def test_attestation_bad_default_refuses_before_verifier_or_registry(
        attester, invocation, monkeypatch):
    outside = invocation.parent / "outside"
    outside.mkdir()
    (invocation / "docs").rmdir()
    (invocation / "docs").symlink_to(outside, target_is_directory=True)
    verifier = Mock(side_effect=attester.Refusal("verifier must not be loaded"))
    monkeypatch.setattr(attester, "checked_npm", lambda raw: "/usr/bin/npm")
    monkeypatch.setattr(attester, "load_verifier", verifier)
    assert attester.main(["--write"]) == 2
    verifier.assert_not_called()
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("spelling", ["HEAD", "branch", "annotated", "abbreviated",
                                      "full", "expression", "unicode"])
def test_real_git_revision_is_data_not_a_command_argument(
        invocation, monkeypatch, spelling):
    module = load_script("validate-carve-manifest.py")
    env = module.carved_reach._sanitized_git_environment()

    def setup_git(*args):
        return subprocess.check_output(
            ["git", "-C", str(invocation), *args], env=env, stderr=subprocess.PIPE).decode().strip()

    setup_git("init", "-q", "-b", "main")
    setup_git("-c", "user.name=synthetic-test", "-c", "user.email=test@example.invalid",
              "commit", "--allow-empty", "-q", "-m", "synthetic source")
    setup_git("-c", "user.name=synthetic-test", "-c", "user.email=test@example.invalid",
              "tag", "-a", "measured-label", "-m", "synthetic annotation")
    setup_git("branch", "révision")
    oid = setup_git("rev-parse", "HEAD")
    ref = {"HEAD": "HEAD", "branch": "main", "annotated": "measured-label",
           "abbreviated": oid[:8], "full": oid, "expression": "HEAD~0",
           "unicode": "révision"}[spelling]
    original_run = subprocess.run
    calls = []

    def observed_run(argv, **kwargs):
        calls.append((argv, kwargs))
        return original_run(argv, **kwargs)

    monkeypatch.setattr(module.subprocess, "run", observed_run)
    assert module.resolve_revision(invocation, ref) == oid
    assert len(calls) == 1
    argv, options = calls[0]
    assert ref not in argv
    assert ref + "^{commit}" not in argv
    assert options["input"] == (ref + "^{commit}\n").encode("utf-8")
