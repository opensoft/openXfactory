"""Real miniature execution and refusal tests for transferable coverage evidence."""
from __future__ import annotations

import importlib.util
import json
import os
import hashlib
import sys
from pathlib import Path
import runpy
import subprocess
import xml.etree.ElementTree as ET

import coverage
import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/validate-sonar-coverage.py"


@pytest.fixture
def tool():
    spec = importlib.util.spec_from_file_location("_sonar_coverage", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True)


@pytest.fixture
def repository(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    root.mkdir()
    for name in ("scripts", "xfactory", "experiments", "specs", "openspec", "tests"):
        (root / name).mkdir()
    (root / "scripts/covered.py").write_text(
        "def choose(value):\n    if value:\n        return 1\n    return 2\nchoose(True)\n")
    (root / "scripts/namespace").mkdir()
    (root / "scripts/namespace/unreached.py").write_text(
        "def untouched(value):\n    if value:\n        return 3\n    return 4\n")
    (root / "tests/test_fixture.py").write_text("def test_fixture():\n    assert True\n")
    for name in (".coveragerc", "sonar-project.properties", ".gitignore"):
        (root / name).write_bytes((ROOT / name).read_bytes())
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Synthetic")
    git(root, "config", "user.email", "synthetic@example.invalid")
    git(root, "add", ".")
    git(root, "commit", "-qm", "synthetic source")
    monkeypatch.chdir(root)
    return root


def measured(tool, root):
    directory = tool.prepare(root, ".coverage-reports")
    cov = coverage.Coverage(data_file=str(directory / ".coverage"),
                            data_suffix=True, branch=True, config_file=False)
    cov.set_option("run:relative_files", True)
    cov.set_option("run:include", [str(root / "scripts/*")])
    cov.start()
    try:
        runpy.run_path(str(root / "scripts/covered.py"))
    finally:
        cov.stop()
        cov.save()
    (root / "pytest-report.xml").write_text(
        '<testsuites><testsuite tests="1" failures="0" errors="0" skipped="0">'
        '<testcase classname="synthetic" name="executed"/></testsuite></testsuites>')
    tool.generate_report(root, directory)
    return directory


def test_real_execution_keeps_zero_hit_namespace_files(tool, repository):
    directory = measured(tool, repository)
    report = ET.parse(directory / "coverage.xml")
    files = {c.attrib["filename"]: c for c in report.findall(".//class")}
    assert set(files) == {"scripts/covered.py", "scripts/namespace/unreached.py"}
    assert any(int(line.attrib["hits"]) > 0
               for line in files["scripts/covered.py"].findall("lines/line"))
    assert all(int(line.attrib["hits"]) == 0
               for line in files["scripts/namespace/unreached.py"].findall("lines/line"))
    assert any(line.attrib.get("branch") == "true"
               for line in files["scripts/namespace/unreached.py"].findall("lines/line"))
    receipt = tool.check_report(repository, directory)
    assert len(receipt["sources"]) == 2
    assert receipt["test_counts"]["failures"] == 0


def test_missing_production_file_in_xml_refuses(tool, repository):
    directory = measured(tool, repository)
    report = ET.parse(directory / "coverage.xml")
    package = report.find(".//classes")
    package.remove(package.findall("class")[-1])
    report.write(directory / "coverage.xml")
    with pytest.raises(tool.Refusal):
        tool.check_report(repository, directory)


def test_source_edit_after_measurement_refuses(tool, repository):
    directory = measured(tool, repository)
    (repository / "scripts/covered.py").write_text("different = 1\n")
    with pytest.raises(tool.Refusal):
        tool.check_report(repository, directory)


def test_report_directory_cannot_escape_root(tool, repository, tmp_path):
    outside = tmp_path / "outside"
    with pytest.raises(tool.Refusal):
        tool.prepare(repository, str(outside))
    assert not outside.exists()


def test_existing_measurement_is_not_reused(tool, repository):
    tool.prepare(repository, ".coverage-reports")
    with pytest.raises(tool.Refusal):
        tool.prepare(repository, ".coverage-reports")


def test_unclassified_python_is_not_silently_omitted(tool, repository):
    (repository / "unclassified.py").write_text("value = 1\n")
    git(repository, "add", "unclassified.py")
    git(repository, "commit", "-qm", "new unclassified source")
    with pytest.raises(tool.Refusal, match="unclassified"):
        tool.prepare(repository, ".coverage-reports")


def test_failed_test_report_cannot_qualify_coverage(tool, repository):
    directory = tool.prepare(repository, ".coverage-reports")
    (repository / "pytest-report.xml").write_text(
        '<testsuite tests="1" failures="1" errors="0" skipped="0"/>')
    with pytest.raises(tool.Refusal):
        tool.generate_report(repository, directory)


def valid_gate():
    limits = {
        "new_security_rating": ("GT", "1", "1"),
        "new_reliability_rating": ("GT", "1", "1"),
        "new_maintainability_rating": ("GT", "1", "1"),
        "new_coverage": ("LT", "80", "82.5"),
        "new_duplicated_lines_density": ("GT", "3", "0.3"),
        "new_security_hotspots_reviewed": ("LT", "100", "100"),
    }
    definition = {"id": 9, "name": "Sonar way", "conditions": [
        {"metric": metric, "op": op, "error": threshold}
        for metric, (op, threshold, _) in limits.items()]}
    status = {"status": "OK", "ignoredConditions": False,
              "periods": [{"index": 1, "mode": "manual_baseline",
                           "date": "2026-09-09T23:37:08Z"}],
              "conditions": [
                  {"metricKey": metric, "comparator": op, "errorThreshold": threshold,
                   "actualValue": actual, "status": "OK"}
                  for metric, (op, threshold, actual) in limits.items()]}
    return status, definition


def test_main_requires_all_existing_evaluated_conditions(tool):
    status, definition = valid_gate()
    tool.validate_gate(status, definition, main=True)


@pytest.mark.parametrize("change", ["missing-coverage", "low-coverage", "different-period",
                                   "lower-threshold", "ignored", "neutral", "nonfinite"])
def test_incomplete_or_weakened_gate_refuses(tool, change):
    status, definition = valid_gate()
    if change == "missing-coverage":
        status["conditions"] = [c for c in status["conditions"] if c["metricKey"] != "new_coverage"]
    elif change == "low-coverage":
        next(c for c in status["conditions"] if c["metricKey"] == "new_coverage")["actualValue"] = "79.9"
    elif change == "different-period":
        status["periods"][0]["date"] = "2026-11-14T00:00:00Z"
    elif change == "lower-threshold":
        next(c for c in definition["conditions"] if c["metric"] == "new_coverage")["error"] = "70"
    elif change == "ignored":
        status["ignoredConditions"] = True
    elif change == "nonfinite":
        status["conditions"][0]["actualValue"] = "NaN"
    else:
        status["status"] = "NONE"
    with pytest.raises(tool.Refusal):
        tool.validate_gate(status, definition, main=True)

def test_subprocess_startup_records_real_child_execution(tool, repository):
    directory = tool.prepare(repository, ".coverage-reports")
    env = dict(os.environ, COVERAGE_PROCESS_START=str(repository / ".coveragerc"),
               COVERAGE_ROOT=str(repository), COVERAGE_FILE=str(directory / ".coverage"))
    subprocess.run([sys.executable, str(repository / "scripts/covered.py")],
                   cwd=repository, env=env, check=True)
    (repository / "pytest-report.xml").write_text(
        '<testsuite tests="1" failures="0" errors="0" skipped="0"/>')
    tool.generate_report(repository, directory)
    detail = json.loads((directory / "coverage.json").read_text())["files"]
    assert 3 in detail["scripts/covered.py"]["executed_lines"]
    assert 4 in detail["scripts/covered.py"]["missing_lines"]
    assert detail["scripts/namespace/unreached.py"]["executed_lines"] == []


def test_matching_forged_reports_cannot_remove_executable_source(tool, repository):
    directory = measured(tool, repository)
    detail = json.loads((directory / "coverage.json").read_text())
    detail["files"]["scripts/namespace/unreached.py"]["missing_lines"].remove(4)
    (directory / "coverage.json").write_text(json.dumps(detail))
    xml = ET.parse(directory / "coverage.xml")
    for entry in xml.findall(".//class"):
        if entry.get("filename") == "scripts/namespace/unreached.py":
            lines = entry.find("lines")
            lines.remove(next(line for line in lines if line.get("number") == "4"))
    xml.write(directory / "coverage.xml")
    receipt = json.loads((directory / "receipt.json").read_text())
    for name in ("coverage.xml", "coverage.json"):
        receipt["artifacts"][name] = hashlib.sha256((directory / name).read_bytes()).hexdigest()
    (directory / "receipt.json").write_text(json.dumps(receipt))
    with pytest.raises(tool.Refusal, match="executable source omitted"):
        tool.check_report(repository, directory)
