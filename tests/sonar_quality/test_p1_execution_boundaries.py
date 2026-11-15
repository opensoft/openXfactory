"""Trusted executable/template authority and non-option operands; no providers."""
from __future__ import annotations

import argparse
import importlib.util
import os
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def openspec():
    return load("p1_openspec_execution", "validate-openspec-cli-pin.py")


@pytest.fixture
def postgres():
    return load("p1_postgres_execution", "validate-hermes-runtime-postgres.py")


def test_npm_operand_uses_only_operator_selected_executable(openspec, tmp_path, monkeypatch):
    trusted, forged = tmp_path / "npm", tmp_path / "forged"
    for path in (trusted, forged):
        path.write_text("#!/bin/sh\nexit 0\n")
        path.chmod(0o700)
    monkeypatch.setenv("XFACTORY_NPM_BINARY", str(trusted))
    assert openspec.trusted_npm_executable("npm") == str(trusted)
    assert openspec.trusted_npm_executable(str(trusted)) == str(trusted)
    with pytest.raises(openspec.PinRefusal):
        openspec.trusted_npm_executable(str(forged))


@pytest.mark.parametrize("name", ["--help", "-a", "../outside", "a/b", "", "a\nb", "a" * 129])
def test_change_id_cannot_become_a_child_option_or_path(openspec, name):
    with pytest.raises(openspec.PinRefusal):
        openspec.validation_targets(argparse.Namespace(all=False, change=[name]))


def test_all_legitimate_targets_still_run_strictly(openspec):
    assert openspec.validation_targets(argparse.Namespace(
        all=False, change=["one-change", "second-change"])) == [
        ["validate", "one-change", "--strict"],
        ["validate", "second-change", "--strict"]]


def test_psql_cli_requires_independent_target_configuration(postgres, monkeypatch):
    monkeypatch.delenv("XFACTORY_PSQL_COMMAND", raising=False)
    def refuse(*args, **kwargs):
        pytest.fail("unapproved template reached database validation")
    monkeypatch.setattr(postgres, "run_validation", refuse)
    assert postgres.main(["--psql-command", "unapproved {database}", "--database",
                          "synthetic", "--profile", "fresh-v2", "--json"]) == 2


def test_psql_cli_rejects_other_container_or_executable(postgres, monkeypatch):
    approved = "docker exec -i disposable-owned psql -d {database}"
    monkeypatch.setenv("XFACTORY_PSQL_COMMAND", approved)
    for selected in ("docker exec -i other-container psql -d {database}",
                     "unapproved {database}"):
        with pytest.raises(postgres.ToolError):
            postgres.trusted_psql_template(selected)


def test_trusted_psql_template_is_the_one_executed_with_stdin(postgres, tmp_path, monkeypatch):
    wrapper = tmp_path / "approved-wrapper"
    wrapper.write_text("#!/bin/sh\nexit 0\n")
    wrapper.chmod(0o700)
    approved = str(wrapper) + " -d {database}"
    monkeypatch.setenv("XFACTORY_PSQL_COMMAND", approved)
    selected = postgres.trusted_psql_template(approved)
    calls = []
    def run(argv, **kwargs):
        calls.append((argv, kwargs))
        return subprocess.CompletedProcess(argv, 0, "synthetic-result", "")
    monkeypatch.setattr(postgres.subprocess, "run", run)
    result = postgres.PsqlRunner(selected).run("synthetic_db", "select 1;")
    assert result.returncode == 0
    assert calls[0][0] == [str(wrapper), "-d", "synthetic_db"]
    assert calls[0][1]["input"] == "select 1;"
    assert "shell" not in calls[0][1]


@pytest.mark.parametrize("database", ["--help", "../db", "db\nnext", "", "a" * 64])
def test_database_operand_refuses_before_subprocess(postgres, monkeypatch, database):
    def refuse(*args, **kwargs):
        pytest.fail("invalid database reached a subprocess")
    monkeypatch.setattr(postgres.subprocess, "run", refuse)
    with pytest.raises(postgres.ToolError):
        postgres.PsqlRunner("psql -d {database}").run(database, "select 1;")


def test_database_placeholder_cannot_choose_the_executable(postgres):
    with pytest.raises(postgres.ToolError):
        postgres.PsqlRunner("{database} --version")
