#!/usr/bin/env python3
"""Offline source-record arithmetic only; no runtime/service qualification."""
import argparse
import hashlib
import json
from pathlib import Path

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate input key")
        result[key] = value
    return result

def read(path):
    return json.loads(path.read_bytes(), object_pairs_hook=unique)

def reproduce(root):
    inputs = read(root / "inventory-inputs.json")
    if set(inputs["sha256"]) != {"policy.json", "measurements.json"}:
        raise ValueError("input closure mismatch")
    for name, expected in inputs["sha256"].items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError("input digest mismatch: " + name)
    p = read(root / "policy.json")
    m = read(root / "measurements.json")
    if p["runtime_qualification"] is not False or p["operational_authorization"] is not False or any(m["qualification"].values()):
        raise ValueError("source-only evidence boundary mismatch")
    if p["credential_count"]["minimum"] != 1 or p["credential_count"]["maximum"] != 3:
        raise ValueError("manifest bound mismatch")
    totals = {}
    for n in (1, 2, 3):
        totals[n] = {}
        for phase, rows in p["schedules"].items():
            if len({row["operation"] for row in rows}) != len(rows):
                raise ValueError("repeated operation")
            if any(type(row[k]) is not int or row[k] < 0 for row in rows for k in ("fixed", "per_credential")):
                raise ValueError("invalid call quantity")
            totals[n][phase] = sum(row["fixed"] + n * row["per_credential"] for row in rows)
    if set(totals[3]) != {"handoff", "original-runtime-cleanup", "audit-only"} or totals[3] != p["maxima"]:
        raise ValueError("whole bound mismatch")
    observations = m["observations"]
    for file, phase in (("p08-physical-accounting.json", "handoff"), ("p08-runtime-cleanup-accounting.json", "original-runtime-cleanup")):
        rows = observations[file]
        if sorted(row["tokens"] for row in rows) != [1, 3]:
            raise ValueError("measured N1/N3 closure mismatch")
        for row in rows:
            n = row["tokens"]
            if row["physical_private"] != row["controller_private"] + row["nested_server_private"] or row["physical_private"] != totals[n][phase]:
                raise ValueError("physical total mismatch")
    refused = observations["p08-fixed-cap-refusal.json"]
    if sorted(row["tokens"] for row in refused) != [1, 3] or any(row["cap"] != 12 or row["private_debits_at_refusal"] != 12 or row["attempted_next_debit"] != 13 or row["proof_performed"] or row["released"] or row["takeover_acknowledged"] or not row["original_nonce_consumed"] or not row["same_original_decision"] or row["budget_reset"] for row in refused):
        raise ValueError("original refusal evidence mismatch")
    return {"kind":"non-product-source-inventory", "policy_sha256":inputs["sha256"]["policy.json"], "derived_per_n":totals, "measured_n":[1,3], "unmeasured_derived_n":[2], "record_arithmetic_valid":True, "runtime_qualification":False, "operational_authorization":False}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        print(json.dumps(reproduce(args.inputs), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, "source inventory refused: " + str(error) + "\n")

if __name__ == "__main__":
    main()
