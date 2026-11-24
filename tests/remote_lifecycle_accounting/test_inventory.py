"""Protect evidence integrity and source/runtime distinctions in this proposal."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import pytest

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "openspec/changes/bound-remote-lifecycle-accounting/supporting-docs"
spec = importlib.util.spec_from_file_location("remote_lifecycle_inventory", PACKET / "derive-inventory.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_frozen_inventory_keeps_measured_and_derived_distinct():
    result = module.reproduce(PACKET)
    assert result["measured_n"] == [1, 3] and result["unmeasured_derived_n"] == [2]
    assert result["runtime_qualification"] is False and result["operational_authorization"] is False
    assert result["derived_per_n"][3] == {"handoff":18,"original-runtime-cleanup":17,"audit-only":4}

def test_changed_record_cannot_reuse_old_attestation(tmp_path):
    shutil.copytree(PACKET, tmp_path / "inputs")
    path = tmp_path / "inputs" / "measurements.json"
    path.write_bytes(path.read_bytes() + b" ")
    with pytest.raises(ValueError, match="input digest mismatch"):
        module.reproduce(path.parent)

@pytest.mark.parametrize("mutation", ["omit-nested-work", "claim-runtime-positive", "erase-original-refusal"])
def test_rehashed_false_claim_still_refuses(tmp_path, mutation):
    target = tmp_path / "inputs"
    shutil.copytree(PACKET, target)
    path = target / "measurements.json"
    record = json.loads(path.read_bytes())
    if mutation == "omit-nested-work":
        record["observations"]["p08-physical-accounting.json"][0]["nested_server_private"] = 0
    elif mutation == "claim-runtime-positive":
        record["qualification"]["p08_complete"] = True
    else:
        record["observations"]["p08-fixed-cap-refusal.json"][0]["proof_performed"] = True
    path.write_bytes((json.dumps(record) + "\n").encode())
    inputs = json.loads((target / "inventory-inputs.json").read_bytes())
    inputs["sha256"][path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    (target / "inventory-inputs.json").write_bytes(json.dumps(inputs).encode())
    with pytest.raises(ValueError):
        module.reproduce(target)
