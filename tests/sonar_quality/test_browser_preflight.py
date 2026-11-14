"""Synthetic replay-driver boundaries: no server, browser or real credential."""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
HELPER = ROOT / "specs/034-opendox-standalone-operation/evidence/at-r1/preflight.py"
PORT = 8123
SYNTHETIC_TOKEN = "synthetic-test-token"


@pytest.fixture
def preflight():
    spec = importlib.util.spec_from_file_location("_at_r1_preflight", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def private_copy(tmp_path, monkeypatch):
    state = tmp_path / "state"
    console = state / "console"
    console.mkdir(parents=True)
    state.chmod(0o700)
    console.chmod(0o700)
    copy = console / f"{PORT}.html"
    copy.write_text('<meta http-equiv="refresh" content="0;url='
                    f'http://127.0.0.1:{PORT}/index.html#console_token={SYNTHETIC_TOKEN}">')
    copy.chmod(0o600)
    monkeypatch.setenv("OPENDOX_STATE_DIR", str(state))
    monkeypatch.chdir(tmp_path)
    return copy


def test_private_copy_validates_fixed_state_identity(preflight, private_copy):
    assert preflight.read_private_copy(str(private_copy), PORT) == SYNTHETIC_TOKEN
    assert preflight.opened_through(str(private_copy), private_copy.as_uri()) == private_copy.as_uri()
    assert preflight.opened_through(str(private_copy), None) == private_copy.as_uri()


@pytest.mark.parametrize("change", ["file-mode", "console-mode", "state-mode",
                                   "file-symlink", "console-symlink", "wrong-port",
                                   "query-token", "token-outside-fragment", "missing-token",
                                   "missing-redirect", "invalid-url"])
def test_private_copy_refuses_invalid_identity(preflight, private_copy, change, tmp_path):
    if change == "file-mode":
        private_copy.chmod(0o644)
    elif change == "console-mode":
        private_copy.parent.chmod(0o755)
    elif change == "state-mode":
        private_copy.parent.parent.chmod(0o755)
    elif change == "file-symlink":
        other = tmp_path / "other.html"
        private_copy.rename(other)
        private_copy.symlink_to(other)
    elif change == "console-symlink":
        console = private_copy.parent
        other = console.with_name("other-console")
        console.rename(other)
        console.symlink_to(other, target_is_directory=True)
    else:
        text = private_copy.read_text()
        if change == "wrong-port":
            text = text.replace(str(PORT), str(PORT + 1))
        elif change == "query-token":
            text = text.replace("#console_token=", "?console_token=")
        elif change == "token-outside-fragment":
            text = "console_token=decoy\n" + text
        elif change == "missing-token":
            text = text.replace(SYNTHETIC_TOKEN, "")
        elif change == "missing-redirect":
            text = "no redirect"
        else:
            text = '<meta http-equiv="refresh" content="0;url=http://[invalid/">'
        private_copy.write_text(text)
    with pytest.raises(preflight.PreflightError):
        preflight.read_private_copy(str(private_copy), PORT)


def test_private_copy_cannot_be_repointed_by_cli(preflight, private_copy, tmp_path):
    outside = tmp_path / "unrelated.html"
    outside.write_bytes(private_copy.read_bytes())
    outside.chmod(0o600)
    with pytest.raises(preflight.PreflightError, match="declared"):
        preflight.read_private_copy(str(outside), PORT)


def test_private_copy_requires_declared_state(preflight, private_copy, monkeypatch):
    monkeypatch.delenv("OPENDOX_STATE_DIR")
    with pytest.raises(preflight.PreflightError, match="OPENDOX_STATE_DIR"):
        preflight.read_private_copy(str(private_copy), PORT)


@pytest.mark.parametrize("url", ["https://example.invalid/", "file:///outside.html",
                                "file://untrusted/path", "file:///any?console_token=x"])
def test_printed_url_cannot_change_private_copy(preflight, private_copy, url):
    with pytest.raises(preflight.PreflightError):
        preflight.opened_through(str(private_copy), url)


@pytest.mark.parametrize("label", ["../outside", "a/../../outside", "a\\outside", "", "c"])
def test_label_refuses_path_injection(preflight, tmp_path, monkeypatch, label):
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "out"
    with pytest.raises(preflight.PreflightError):
        preflight.prepare_output_directory(str(out), label)
    assert not out.exists()


def test_output_directory_stays_inside_invocation(preflight, tmp_path, monkeypatch):
    root = tmp_path / "root"
    root.mkdir()
    monkeypatch.chdir(root)
    outside = tmp_path / "root-sibling"
    with pytest.raises(preflight.PreflightError, match="invocation"):
        preflight.prepare_output_directory(str(outside), "a")
    assert not outside.exists()


def test_output_escape_symlink_refuses(preflight, tmp_path, monkeypatch):
    root = tmp_path / "root"
    outside = tmp_path / "outside"
    root.mkdir()
    outside.mkdir()
    (root / "linked").symlink_to(outside, target_is_directory=True)
    monkeypatch.chdir(root)
    with pytest.raises(preflight.PreflightError, match="invocation"):
        preflight.prepare_output_directory("linked", "a")


def test_output_is_private_and_never_overwrites_evidence(preflight, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    out = preflight.prepare_output_directory("out", "a")
    path = preflight.write_output(out, "a-result.json", b'{"synthetic":true}')
    assert path.read_bytes() == b'{"synthetic":true}'
    assert path.stat().st_mode & 0o777 == 0o600
    with pytest.raises(preflight.PreflightError):
        preflight.write_output(out, "a-result.json", b"overwritten")
    assert path.read_bytes() == b'{"synthetic":true}'
    with pytest.raises(preflight.PreflightError):
        preflight.write_output(out, "../escape.json", b"escape")


@pytest.mark.parametrize("flags", [[], ["-O"]])
def test_optimization_cannot_remove_private_mode_check(private_copy, flags):
    private_copy.chmod(0o644)
    code = (
        "import importlib.util,sys\n"
        "s=importlib.util.spec_from_file_location('preflight',sys.argv[1])\n"
        "m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\n"
        "try:m.read_private_copy(sys.argv[2],int(sys.argv[3]))\n"
        "except m.PreflightError:sys.exit(0)\n"
        "sys.exit(1)\n"
    )
    proc = subprocess.run([sys.executable, *flags, "-c", code, str(HELPER),
                           str(private_copy), str(PORT)], env=os.environ.copy(),
                          capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr


@pytest.mark.parametrize("flags", [[], ["-O"]])
def test_driver_refusal_precedes_oracle_and_browser_import(private_copy, tmp_path, flags):
    private_copy.chmod(0o644)
    oracle_root = tmp_path / "oracle"
    tests = oracle_root / "tests"
    tests.mkdir(parents=True)
    marker = tmp_path / "oracle-imported"
    (tests / "smoke_signals.py").write_text(
        "from pathlib import Path" + chr(10)
        + "Path(" + repr(str(marker)) + ").write_text('executed')" + chr(10))
    driver = HELPER.with_name("at_r1_browser.py")
    proc = subprocess.run([sys.executable, *flags, str(driver), "--port", str(PORT),
                           "--label", "a", "--out", str(tmp_path / "out"),
                           "--odc", str(oracle_root), "--copy", str(private_copy)],
                          cwd=tmp_path, env=os.environ.copy(), capture_output=True,
                          text=True, timeout=5)
    assert proc.returncode == 2, proc.stdout + proc.stderr
    assert "ERROR before the drive" in proc.stdout + proc.stderr
    assert not marker.exists()


def test_existing_record_is_refused_before_harness_runs(tmp_path):
    out = tmp_path / "prior"
    out.mkdir()
    receipt = out / "verdict.txt"
    receipt.write_text("original dated verdict")
    env = {**os.environ, "OUT": str(out)}
    proc = subprocess.run(["bash", str(HELPER.with_name("run-at-r1.sh")), "HEAD"],
                          env=env, cwd=tmp_path, capture_output=True, text=True, timeout=5)
    assert proc.returncode == 2
    assert "already holds evidence" in proc.stderr
    assert receipt.read_text() == "original dated verdict"
    assert not (out / "run.log").exists()


def test_broken_result_symlink_is_not_reused(preflight, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "out"
    out.mkdir(mode=0o700)
    (out / "a-result.json").symlink_to(tmp_path / "not-created")
    with pytest.raises(preflight.PreflightError, match="already holds"):
        preflight.prepare_output_directory(str(out), "a")
