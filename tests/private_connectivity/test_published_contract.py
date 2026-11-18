"""Proposed supported neutral publication; no provider/runtime proof."""
import importlib.util
import json
from pathlib import Path
import runpy
import shutil
import subprocess
import sys

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
FAMILY = ROOT / "contracts/private-connectivity"
MEMBERS = ("contracts/private-connectivity/binding.schema.json",
           "contracts/private-connectivity/README.md",
           "contracts/private-connectivity/conformance.json",
           "scripts/validate-private-connectivity.py")


def test_publication_preserves_schema_v1_semantics():
    supported = json.loads((FAMILY / "binding.schema.json").read_text())
    historical = json.loads((ROOT / "specs/040-private-connectivity/contracts/private-connectivity/binding.schema.json").read_text())
    Draft202012Validator.check_schema(supported)
    assert supported["$id"] == "https://xforge.us/schemas/openxfactory/private-connectivity/binding.schema.json"
    assert {key:value for key,value in supported.items() if key != "$id"} == historical
    assert supported["schema_version"] == 1
    assert set(supported["properties"]["state"]["enum"]) == {"requested","approved","enrolled","ready","unready","revoked"}


def test_four_member_consumer_replays_corpus_without_pilot_or_provider_code(tmp_path, monkeypatch, capsys):
    consumer = tmp_path / "neutral-consumer";consumer.mkdir()
    for member in MEMBERS:
        destination = consumer / member;destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/member,destination)
    assert not (consumer/"specs").exists()
    spec = importlib.util.spec_from_file_location("independent_neutral_reader",consumer/"scripts/validate-private-connectivity.py")
    reader = importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
    corpus = json.loads((consumer/"contracts/private-connectivity/conformance.json").read_text())
    from datetime import datetime
    now = datetime.fromisoformat(corpus["now"].replace("Z","+00:00"))
    assert corpus["authorizes_runtime"] is False
    assert len({case["id"] for case in corpus["cases"]}) == len(corpus["cases"])
    assert any(not case["expected_findings"] for case in corpus["cases"])
    assert any(case["expected_findings"] for case in corpus["cases"])
    monkeypatch.chdir(consumer)
    manifest = consumer / "manifest.json"
    cli_args = ["manifest.json", "--now", corpus["now"]]
    for case in corpus["cases"]:
        expected = case["expected_findings"]
        assert reader.validate(case["manifest"], now) == expected, case["id"]
        manifest.write_text(json.dumps(case["manifest"]), encoding="utf-8")
        assert reader.main(cli_args) == (1 if expected else 0), case["id"]
        output = capsys.readouterr()
        assert output.err.splitlines() == [f"FAIL: {finding}" for finding in expected]

    for invalid in (
        '{"private_connectivity":null,"private_connectivity":null}',
        '{"unrelated":NaN}',
        '{"unrelated":Infinity}',
        '{"unrelated":-Infinity}',
    ):
        manifest.write_text(invalid, encoding="utf-8")
        assert reader.main(cli_args) == 2
        assert capsys.readouterr().err == "FAIL: unreadable or invalid input\n"

    (consumer / "alias.json").symlink_to(manifest)
    assert reader.main(["alias.json"]) == 2

    # Verify the shipped script's process entry point on success and refusal.
    command = [sys.executable, str(consumer / MEMBERS[3]), *cli_args]
    for text, expected_code in (("{}", 0), ('{"unrelated":NaN}', 2)):
        manifest.write_text(text, encoding="utf-8")
        assert subprocess.run(command, cwd=consumer, capture_output=True).returncode == expected_code

    ready = next(case for case in corpus["cases"] if case["id"] == "managed-ready-declaration")
    manifest.write_text(json.dumps(ready["manifest"]), encoding="utf-8")
    repository_reader = runpy.run_path(str(ROOT / MEMBERS[3]))
    with monkeypatch.context() as isolated:
        isolated.delitem(repository_reader["FormatChecker"].checkers, "date-time")
        assert repository_reader["main"](cli_args) == 2
        assert repository_reader["validate"]({}, now) == []
