"""Preserve dated acceptance claims while repairing their maintained driver."""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = "c283547b3490c5f3a29b0c800c5c63da361c7da7"
PREFIX = "specs/034-opendox-standalone-operation/evidence/at-r1/"


def test_dated_acceptance_artifacts_are_unchanged():
    names = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", BASE, "--", PREFIX],
        text=True).splitlines()
    protected = [name for name in names
                 if Path(name).name not in {"at_r1_browser.py", "run-at-r1.sh"}]
    assert PREFIX + "oracle-verdict.md" in protected
    proc = subprocess.run(["git", "-C", str(ROOT), "diff", "--exit-code",
                           BASE, "--", *protected], capture_output=True, text=True)
    assert proc.returncode == 0, "a dated acceptance artifact was rewritten: " + proc.stdout


def test_maintained_source_and_original_preimage_match_provenance():
    record = (ROOT / PREFIX / "sonar-remediation-provenance.md").read_text()
    assert "Original source commit: " + BASE in record
    for name, label in [("at_r1_browser.py", "driver"), ("run-at-r1.sh", "runner")]:
        before = subprocess.check_output(
            ["git", "-C", str(ROOT), "show", BASE + ":" + PREFIX + name])
        expected = hashlib.sha256(before).hexdigest()
        assert "Original " + label + " SHA-256: " + expected in record
        expected = hashlib.sha256((ROOT / PREFIX / name).read_bytes()).hexdigest()
        assert "Maintained " + label + " SHA-256: " + expected in record
    helper = hashlib.sha256((ROOT / PREFIX / "preflight.py").read_bytes()).hexdigest()
    assert "Preflight helper SHA-256: " + helper in record


def test_replay_security_checks_do_not_use_optimization_sensitive_asserts():
    driver = (ROOT / PREFIX / "at_r1_browser.py").read_text()
    assert not re.search(r"^\s*assert\s", driver, re.MULTILINE)
    runner = (ROOT / PREFIX / "run-at-r1.sh").read_text()
    assert not re.search(r"^\s*assert\s", runner, re.MULTILINE)
    assert 'from preflight import read_private_copy, require' in runner
