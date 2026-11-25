#!/usr/bin/env python3
"""Offline source-record arithmetic only; no runtime/service qualification."""
import argparse
import hashlib
import json
from pathlib import Path

POLICY_FILE = "policy.json"
MEASUREMENTS_FILE = "measurements.json"
QUALIFICATION_FIELDS = {"full", "native", "hosted", "p08_complete"}
CONTROLLER_PRIVATE = "controller_private"
NESTED_PRIVATE = "nested_server_private"
PHASES = {"handoff", "original-runtime-cleanup", "audit-only"}


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate input key")
        result[key] = value
    return result


def read(path):
    return json.loads(path.read_bytes(), object_pairs_hook=unique)


def frozen_inputs(root):
    inputs = read(root / "inventory-inputs.json")["sha256"]
    if set(inputs) != {POLICY_FILE, MEASUREMENTS_FILE}:
        raise ValueError("input closure mismatch")
    for name, expected in inputs.items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError("input digest mismatch: " + name)
    return inputs


def exact_fields(row, expected, error):
    if any(type(row[key]) is not type(value) or row[key] != value
           for key, value in expected.items()):
        raise ValueError(error)


def source_only(policy, measurements):
    boundary = {"runtime_qualification": False, "operational_authorization": False}
    exact_fields(policy, boundary, "source-only policy boundary mismatch")
    flags = measurements["qualification"]
    if set(flags) != QUALIFICATION_FIELDS or any(value is not False for value in flags.values()):
        raise ValueError("source-only evidence boundary mismatch")


def phase_cost(rows, n):
    if len({row["operation"] for row in rows}) != len(rows):
        raise ValueError("repeated operation")
    if any(type(row[key]) is not int or row[key] < 0
           for row in rows for key in ("fixed", "per_credential")):
        raise ValueError("invalid call quantity")
    return sum(row["fixed"] + n * row["per_credential"] for row in rows)


def derive_totals(policy):
    exact_fields(policy["credential_count"], {"minimum": 1, "maximum": 3}, "manifest bound mismatch")
    totals = {n: {phase: phase_cost(rows, n) for phase, rows in policy["schedules"].items()}
              for n in (1, 2, 3)}
    if set(totals[3]) != PHASES or totals[3] != policy["maxima"]:
        raise ValueError("whole bound mismatch")
    return totals


def measured_n(rows):
    values = [row["tokens"] for row in rows]
    if any(type(n) is not int for n in values) or sorted(values) != [1, 3]:
        raise ValueError("measured N1/N3 closure mismatch")


def verify_measured(observations, totals):
    groups = (("p08-physical-accounting.json", "handoff"),
              ("p08-runtime-cleanup-accounting.json", "original-runtime-cleanup"))
    for name, phase in groups:
        rows = observations[name]
        measured_n(rows)
        for row in rows:
            physical = row[CONTROLLER_PRIVATE] + row[NESTED_PRIVATE]
            if row["physical_private"] != physical or physical != totals[row["tokens"]][phase]:
                raise ValueError("physical total mismatch")


def verify_refusals(rows):
    measured_n(rows)
    expected = {"cap": 12, "private_debits_at_refusal": 12, "attempted_next_debit": 13,
                "proof_performed": False, "released": False, "takeover_acknowledged": False,
                "original_nonce_consumed": True, "same_original_decision": True, "budget_reset": False}
    for row in rows:
        exact_fields(row, expected, "original refusal evidence mismatch")


def verify_fixture_mode(rows, mode, totals):
    selected = [row for row in rows if row["mode"] == mode]
    measured_n(selected)
    audit = mode == "audit-only-no-resend"
    for row in selected:
        n = row["tokens"]
        expected = {CONTROLLER_PRIVATE: 1 if audit else 2,
                    NESTED_PRIVATE: n if audit else 4 * n,
                    "mutating_rpc_sent": not audit, "credentials_retired": True,
                    "observed_kind": "final" if audit else "stage"}
        exact_fields(row, expected, "fixture cleanup evidence mismatch")
        physical = row[CONTROLLER_PRIVATE] + row[NESTED_PRIVATE]
        bound = totals[n]["audit-only"] if audit else 2 + 4 * n
        if physical != bound:
            raise ValueError("fixture physical total mismatch")


def verify_fixture_cleanup(rows, totals):
    modes = {"audit-only-no-resend", "original-scope-cleanup"}
    if len(rows) != 4 or {row["mode"] for row in rows} != modes:
        raise ValueError("fixture mode closure mismatch")
    for mode in modes:
        verify_fixture_mode(rows, mode, totals)


def reproduce(root):
    inputs = frozen_inputs(root)
    policy = read(root / POLICY_FILE)
    measurements = read(root / MEASUREMENTS_FILE)
    source_only(policy, measurements)
    totals = derive_totals(policy)
    observations = measurements["observations"]
    verify_measured(observations, totals)
    verify_refusals(observations["p08-fixed-cap-refusal.json"])
    verify_fixture_cleanup(observations["p08-fixture-cleanup.json"], totals)
    return {"kind": "non-product-source-inventory", "policy_sha256": inputs[POLICY_FILE],
            "derived_per_n": totals, "measured_n": [1, 3], "unmeasured_derived_n": [2],
            "record_arithmetic_valid": True, "runtime_qualification": False,
            "operational_authorization": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(reproduce(args.inputs), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, "source inventory refused: " + str(error) + "\n")


if __name__ == "__main__":
    main()
