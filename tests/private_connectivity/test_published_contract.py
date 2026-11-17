"""Proposed supported neutral publication; no provider/runtime proof."""
import importlib.util
import json
from pathlib import Path
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


def test_four_member_consumer_replays_corpus_without_pilot_or_provider_code(tmp_path):
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
    for case in corpus["cases"]:
        assert reader.validate(case["manifest"],now) == case["expected_findings"],case["id"]
        manifest = consumer/"manifest.json";manifest.write_text(json.dumps(case["manifest"]))
        result = subprocess.run([sys.executable,str(consumer/"scripts/validate-private-connectivity.py"),"manifest.json","--now",corpus["now"]],
                                cwd=consumer,capture_output=True,text=True)
        assert result.returncode == (1 if case["expected_findings"] else 0),case["id"]
        assert "synthetic-value" not in result.stderr
    # Real CLI ordinary-input behavior remains enforced in the isolated consumer.
    manifest.write_text('{"private_connectivity":null,"private_connectivity":null}')
    assert subprocess.run([sys.executable,str(consumer/"scripts/validate-private-connectivity.py"),"manifest.json"],cwd=consumer,capture_output=True).returncode==2
    (consumer/"alias.json").symlink_to(manifest)
    assert subprocess.run([sys.executable,str(consumer/"scripts/validate-private-connectivity.py"),"alias.json"],cwd=consumer,capture_output=True).returncode==2
