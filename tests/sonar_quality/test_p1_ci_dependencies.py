"""Privileged installer controls retain fixed artifacts and functional fallback."""
from pathlib import Path
import json
import shlex
import re
import os
import shutil
import subprocess

import pytest

import yaml

ROOT = Path(__file__).resolve().parents[2]


def workflow(name):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


def steps(doc):
    return [step for job in doc["jobs"].values() for step in job.get("steps", [])]



def npm_install_command(script):
    commands = []
    for line in script.replace(chr(92) + chr(10), " ").splitlines():
        argv = shlex.split(line, comments=True)
        if argv[:2] == ["npm", "ci"]:
            commands.append(argv)
    assert len(commands) == 1
    argv = commands[0]
    assert "--ignore-scripts" in argv
    assert "--no-audit" in argv and "--no-fund" in argv
    assert "--prefix" in argv and "-g" not in argv and "--global" not in argv
    return argv


def test_privileged_python_installs_require_hashes_and_wheels():
    installs = []
    for name in ("doc-health-reusable.yml", "merge-master-approval.yml"):
        for step in steps(workflow(name)):
            script = step.get("run", "").replace(chr(92) + chr(10), " ")
            for line in script.splitlines():
                if re.match(r"^\s*(?:python[0-9.]*\s+-m\s+)?pip\s+install\b", line) is None:
                    continue
                argv = shlex.split(line)
                assert "--require-hashes" in argv
                binary = argv.index("--only-binary")
                assert argv[binary + 1] == ":all:"
                lock = argv[argv.index("-r") + 1]
                local = lock.removeprefix("openxFactory/")
                assert (ROOT / local).is_file()
                assert "--hash=sha256:" in (ROOT / local).read_text()
                installs.append((name, step["name"]))
    assert len(installs) == 3


def test_both_doc_health_phases_use_the_same_fixed_compatible_closure():
    doc = workflow("doc-health-reusable.yml")
    for job in ("prepare", "finalize"):
        install = next(s for s in doc["jobs"][job]["steps"]
                       if s.get("name") == "Install suite dependencies")
        assert "openxFactory/.github/requirements/privileged-ci.lock" in install["run"]
    lock = (ROOT / ".github/requirements/privileged-ci.lock").read_text()
    assert "cryptography==50.0.0" in lock
    assert "cryptography==50.0.0" in (ROOT / "requirements/hermes-runtime-contracts.in").read_text()
    for package in ("pyyaml==", "pytest==", "jsonschema==", "rfc3339-validator=="):
        assert package in lock


def test_worker_fallback_is_still_enrolled_and_has_no_global_or_unlocked_install():
    doc = workflow("doc-health-reusable.yml")
    assert doc["jobs"]["finalize"]["env"]["DISABLE_AUTOUPDATER"] == "1"
    fallback = next(s for s in steps(doc)
                    if s.get("name") == "Install analysis worker CLI (inline fallback)")
    assert fallback["if"] == "needs.prepare.outputs.omnigent != 'true' && env.HAS_ANTHROPIC_KEY == 'true'"
    assert fallback["run"] == "bash openxFactory/.github/worker-cli/install.sh"
    script = (ROOT / ".github/worker-cli/install.sh").read_text()
    npm_install_command(script)
    assert "npm install" not in script and " -g " not in script
    assert "--version" in script and "env -i" in script
    assert "GITHUB_PATH" in script
    assert "ANTHROPIC_API_KEY:" in (ROOT / ".github/workflows/doc-health-reusable.yml").read_text()


def test_worker_binary_manifest_and_integrity_lock_agree_without_install_hooks():
    base = ROOT / ".github/worker-cli"
    manifest = json.loads((base / "package.json").read_text())
    lock = json.loads((base / "package-lock.json").read_text())
    dependencies = manifest["dependencies"]
    assert lock["packages"][""]["dependencies"] == dependencies
    assert len(dependencies) == 1
    for name, version in dependencies.items():
        assert version[0].isdigit() and not any(c in version for c in "^~*<>=| ")
        package = lock["packages"]["node_modules/" + name]
        assert package["version"] == version
        assert package["integrity"].startswith("sha512-")
        assert package["resolved"].startswith("https://registry.npmjs.org/")
        assert not package.get("hasInstallScript")
        assert not package.get("dependencies")
    assert not manifest.get("scripts")


def test_privileged_job_permissions_and_trusted_core_are_preserved():
    doc = workflow("doc-health-reusable.yml")
    assert doc["jobs"]["finalize"]["permissions"] == {
        "actions": "write", "contents": "write", "issues": "write",
        "pull-requests": "write"}
    review = workflow("merge-master-approval.yml")
    core = next(s for s in steps(review) if s.get("id") == "core")
    assert core["with"]["persist-credentials"] is False
    assert core["with"]["ref"] == "ce9236363d044bc6d8cf9b9f7a5bd15ecaff9559"


def test_comment_cannot_mask_missing_lifecycle_protection():
    script = (ROOT / ".github/worker-cli/install.sh").read_text()
    mutated = script.replace(" --ignore-scripts", "") + "\n# --ignore-scripts"
    with pytest.raises(AssertionError):
        npm_install_command(mutated)


def test_worker_launcher_enforces_updates_after_real_worker_env_scrub(tmp_path, monkeypatch):
    from scripts.doc_health.semantic import _scrubbed_env
    install = tmp_path / "worker"
    bindir = install / "bin"
    native = install / "node_modules/@anthropic-ai/claude-code-linux-x64/claude"
    bindir.mkdir(parents=True)
    native.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / ".github/worker-cli/launcher.sh", bindir / "claude")
    (bindir / "claude").chmod(0o700)
    native.write_text('#!/bin/sh\nprintf \'%s|%s|%s\' "$DISABLE_UPDATES" "$DISABLE_AUTOUPDATER" "$*"\n')
    native.chmod(0o700)
    monkeypatch.setenv("DISABLE_UPDATES", "0")
    monkeypatch.setenv("DISABLE_AUTOUPDATER", "0")
    env = _scrubbed_env()
    result = subprocess.run([str(bindir / "claude"), "--version", "synthetic"], env=env,
                            capture_output=True, text=True, check=True)
    assert result.stdout == "1|1|--version synthetic"


def test_dependency_acceptance_uses_the_actual_aggregation_provider_layout():
    doc = workflow("privileged-dependencies.yml")
    checkout = next(s for s in steps(doc) if "actions/checkout@" in s.get("uses", ""))
    assert checkout["with"]["path"] == "openxFactory"
    scripts = [s["run"] for s in steps(doc) if "run" in s]
    assert any("bash openxFactory/.github/worker-cli/install.sh" in s for s in scripts)
    assert all("-r .github/" not in s for s in scripts)
