"""Exercise frozen-record integrity, measured accounting and CLI evidence boundaries."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import pytest

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "openspec/changes/bound-remote-lifecycle-accounting/supporting-docs"
MODULE = PACKET / "derive-inventory.py"
POLICY = "policy.json"
MEASUREMENTS = "measurements.json"
INPUTS = "inventory-inputs.json"
PHYSICAL = "p08-physical-accounting.json"
FIXTURE = "p08-fixture-cleanup.json"
REFUSAL = "p08-fixed-cap-refusal.json"
spec = importlib.util.spec_from_file_location("remote_lifecycle_inventory", MODULE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def working_copy(tmp_path):
    target = tmp_path / "inputs"
    shutil.copytree(PACKET, target)
    return target


def edit_record(target, filename, trail, value):
    path = target / filename
    record = json.loads(path.read_bytes())
    node = record
    for step in trail[:-1]:
        node = node[step]
    node[trail[-1]] = value
    path.write_bytes((json.dumps(record) + "\n").encode())
    inputs = json.loads((target / INPUTS).read_bytes())
    inputs["sha256"][filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    (target / INPUTS).write_bytes(json.dumps(inputs).encode())


def test_frozen_inventory_keeps_measured_and_derived_distinct():
    result = module.reproduce(PACKET)
    assert result["measured_n"] == [1, 3]
    assert result["unmeasured_derived_n"] == [2]
    assert result["runtime_qualification"] is False
    assert result["operational_authorization"] is False
    assert result["derived_per_n"][3] == {"handoff": 18, "original-runtime-cleanup": 17, "audit-only": 4}


def test_changed_record_cannot_reuse_old_attestation(tmp_path):
    target = working_copy(tmp_path)
    path = target / MEASUREMENTS
    path.write_bytes(path.read_bytes() + b" ")
    with pytest.raises(ValueError, match="input digest mismatch"):
        module.reproduce(target)


@pytest.mark.parametrize("mutation", ["omit-nested-work", "claim-runtime-positive", "erase-original-refusal"])
def test_rehashed_false_claim_still_refuses(tmp_path, mutation):
    target = working_copy(tmp_path)
    changes = {
        "omit-nested-work": (("observations", PHYSICAL, 0, "nested_server_private"), 0),
        "claim-runtime-positive": (("qualification", "p08_complete"), True),
        "erase-original-refusal": (("observations", REFUSAL, 0, "proof_performed"), True),
    }
    trail, value = changes[mutation]
    edit_record(target, MEASUREMENTS, trail, value)
    with pytest.raises(ValueError):
        module.reproduce(target)


@pytest.mark.parametrize("filename,trail,value,error", [
    (POLICY, ("runtime_qualification",), True, "source-only policy"),
    (POLICY, ("operational_authorization",), True, "source-only policy"),
    (POLICY, ("credential_count", "minimum"), 0, "manifest bound"),
    (POLICY, ("credential_count", "maximum"), True, "manifest bound"),
    (POLICY, ("schedules", "handoff", 1, "operation"), "p05-independent-observers", "repeated operation"),
    (POLICY, ("schedules", "handoff", 0, "fixed"), True, "invalid call quantity"),
    (POLICY, ("schedules", "handoff", 0, "per_credential"), -1, "invalid call quantity"),
    (POLICY, ("maxima", "handoff"), 19, "whole bound"),
    (MEASUREMENTS, ("qualification",), {}, "source-only evidence"),
    (MEASUREMENTS, ("observations", PHYSICAL, 0, "tokens"), 1, "N1/N3 closure"),
    (MEASUREMENTS, ("observations", PHYSICAL, 0, "tokens"), True, "N1/N3 closure"),
    (MEASUREMENTS, ("observations", PHYSICAL, 0, "physical_private"), 12, "physical total"),
    (MEASUREMENTS, ("observations", REFUSAL, 0, "released"), 0, "original refusal"),
    (MEASUREMENTS, ("observations", FIXTURE, 0, "mutating_rpc_sent"), True, "fixture cleanup"),
    (MEASUREMENTS, ("observations", FIXTURE, 0, "nested_server_private"), 0, "fixture cleanup"),
    (MEASUREMENTS, ("observations", FIXTURE, 1, "nested_server_private"), 0, "fixture cleanup"),
    (MEASUREMENTS, ("observations", FIXTURE, 1, "credentials_retired"), False, "fixture cleanup"),
    (MEASUREMENTS, ("observations", FIXTURE, 1, "mode"), "unknown", "fixture mode closure"),
    (MEASUREMENTS, ("observations", FIXTURE, 3, "tokens"), 3, "N1/N3 closure"),
])
def test_rehashed_accounting_or_authority_tamper_refuses(tmp_path, filename, trail, value, error):
    target = working_copy(tmp_path)
    edit_record(target, filename, trail, value)
    with pytest.raises(ValueError, match=error):
        module.reproduce(target)


def test_frozen_input_closure_cannot_drop_a_file(tmp_path):
    target = working_copy(tmp_path)
    inputs = json.loads((target / INPUTS).read_bytes())
    del inputs["sha256"][MEASUREMENTS]
    (target / INPUTS).write_bytes(json.dumps(inputs).encode())
    with pytest.raises(ValueError, match="input closure"):
        module.reproduce(target)


def test_duplicate_json_keys_refuse_before_arithmetic(tmp_path):
    target = working_copy(tmp_path)
    (target / INPUTS).write_bytes(b'{"sha256": {}, "sha256": {}}')
    with pytest.raises(ValueError, match="duplicate input key"):
        module.reproduce(target)


def test_cli_prints_only_source_inventory(capsys):
    module.main(["--inputs", str(PACKET)])
    result = json.loads(capsys.readouterr().out)
    assert result["record_arithmetic_valid"] is True
    assert result["runtime_qualification"] is False
    assert result["operational_authorization"] is False


def test_cli_refuses_invalid_record_without_traceback(tmp_path, capsys):
    target = working_copy(tmp_path)
    (target / INPUTS).write_bytes(b"not-json")
    with pytest.raises(SystemExit) as failure:
        module.main(["--inputs", str(target)])
    assert failure.value.code == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.startswith("source inventory refused:")
    assert "Traceback" not in captured.err


def test_real_cli_process_preserves_source_only_boundary():
    result = subprocess.run([sys.executable, "-I", "-B", str(MODULE)],
                            capture_output=True, text=True, check=False, timeout=15)
    assert result.returncode == 0
    record = json.loads(result.stdout)
    assert record["runtime_qualification"] is False
    assert record["operational_authorization"] is False


def test_changed_audit_schedule_cannot_hide_observed_totals(tmp_path):
    target = working_copy(tmp_path)
    edit_record(target, POLICY, ("schedules", "audit-only", 0, "fixed"), 4)
    edit_record(target, POLICY, ("schedules", "audit-only", 0, "per_credential"), 0)
    with pytest.raises(ValueError, match="fixture physical total"):
        module.reproduce(target)
