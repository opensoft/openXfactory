"""Offline checks for the proposal's analysis helper, not P07 runtime tests."""
import contextlib
import copy
from collections import Counter
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SUPPORT = ROOT / "openspec/changes/bound-infrastructure-retirement-accounting/supporting-docs"
SPEC = importlib.util.spec_from_file_location(
    "retirement_inventory_analysis", SUPPORT / "derive-inventory.py")
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class TestRetirementInventory(unittest.TestCase):
    def setUp(self):
        self.inputs = json.loads((SUPPORT / "inventory-inputs.json").read_text())
        self.records = inventory.load_records(SUPPORT / "fixtures")

    def test_derived_artifact_reproduces_exactly(self):
        emitted = json.dumps(inventory.derive(self.inputs, self.records), indent=2) + "\n"
        self.assertEqual(emitted, (SUPPORT / "call-inventory.json").read_text())

    def test_cli_default_emits_the_same_complete_artifact(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SUPPORT / "derive-inventory.py")],
            capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, (SUPPORT / "call-inventory.json").read_text())
        self.assertEqual(result.stderr, "")

    def test_main_default_and_failure_are_bounded(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(inventory.main([]), 0)
        self.assertEqual(output.getvalue(), (SUPPORT / "call-inventory.json").read_text())
        with tempfile.TemporaryDirectory() as name:
            error = io.StringIO()
            with patch.object(inventory, "HERE", Path(name)):
                with contextlib.redirect_stderr(error):
                    self.assertEqual(inventory.main([]), 2)
            self.assertEqual(error.getvalue(), "inventory-refused\n")

    def test_graph_has_exact_kinds_closed_dependencies_and_no_cycle(self):
        nodes = inventory.graph_resources()
        self.assertEqual(Counter(x["kind"] for x in nodes),
                         {"vm": 3, "os_disk": 3, "nic": 3, "public_ip": 1,
                          "vnet": 1, "nsg": 3})
        paths = {x["resource_path"] for x in nodes}
        self.assertEqual(len(paths), 14)
        self.assertEqual(sum(len(x["dependency_paths"]) for x in nodes), 16)
        pending = {x["resource_path"]: set(x["dependency_paths"]) for x in nodes}
        self.assertTrue(all(deps <= paths for deps in pending.values()))
        while pending:
            ready = {path for path, deps in pending.items() if not deps}
            self.assertTrue(ready, "dependency cycle")
            pending = {path: deps - ready for path, deps in pending.items()
                       if path not in ready}
        self.assertTrue(all(x["disposition"] == "ephemeral" for x in nodes))

    def test_core_formula_reconciles_measured_six_kind_trace(self):
        trace = json.loads((SUPPORT / "eligibility.json").read_text())
        measured = trace["results"]["per-resource-cost"]["sum_of_separate_decision_costs"]
        core = inventory.schedule_rows(6, 6)["cleanup"][1]
        self.assertEqual((core["private"], core["arm"], core["namespace"]),
                         (measured["private"], measured["arm"],
                          measured["namespace_calls"]))

    def test_fixed_caps_agree_with_normative_policy_table(self):
        policy = (SUPPORT / "accounting-policy.md").read_text().splitlines()
        prefixes = {"Registration, including": "registration",
                    "One original cleanup": "cleanup",
                    "One independently authorized": "observation"}
        found = {}
        for line in policy:
            cells = [part.strip() for part in line.split("|")]
            for prefix, pool in prefixes.items():
                if len(cells) >= 7 and cells[1].startswith(prefix):
                    found[pool] = dict(zip(inventory.GROUPS, map(int, cells[2:6])))
        self.assertEqual(found, self.inputs["selected_limits"])
        result = inventory.derive(self.inputs, self.records)
        for pool, values in result["modeled_totals"].items():
            facade = result["rows"][pool][-1]["private"]
            self.assertEqual(facade, values["namespace"] + values["journal"])

    def test_insufficient_or_malformed_pool_cannot_emit_a_fitting_inventory(self):
        for mutation in ("low", "missing-pool", "missing-group", "boolean"):
            with self.subTest(mutation=mutation):
                changed = copy.deepcopy(self.inputs)
                limits = changed["selected_limits"]
                if mutation == "low":
                    limits["cleanup"]["private"] = 699
                elif mutation == "missing-pool":
                    del limits["cleanup"]
                elif mutation == "missing-group":
                    del limits["cleanup"]["private"]
                else:
                    limits["cleanup"]["private"] = True
                with self.assertRaises(ValueError):
                    inventory.derive(changed, self.records)

    def test_every_recorded_fixture_detects_a_single_changed_bound_value(self):
        for name in self.records:
            with self.subTest(name=name):
                changed = dict(self.records)
                value = json.loads(changed[name])
                value["profile"] = "changed-profile"
                changed[name] = inventory.canonical(value)
                with self.assertRaisesRegex(ValueError, "recorded-fixture-mismatch"):
                    inventory.derive(self.inputs, changed)

    def test_missing_or_extra_record_is_not_silently_omitted(self):
        for extra in (False, True):
            with self.subTest(extra=extra):
                changed = dict(self.records)
                if extra:
                    changed["extra"] = b"{}"
                else:
                    del changed["reservation"]
                with self.assertRaisesRegex(ValueError, "fixture-set"):
                    inventory.derive(self.inputs, changed)

    def test_fixture_loader_rejects_oversize_noncanonical_duplicate_and_wrong_root(self):
        bad = (b" " + self.records["reservation"], b"x" * 16385,
               b'{"profile":"duplicate",' + self.records["reservation"][1:],
               b"[]")
        for raw in bad:
            with self.subTest(length=len(raw)):
                with tempfile.TemporaryDirectory() as name:
                    directory = Path(name)
                    for record, body in self.records.items():
                        (directory / (record + ".json")).write_bytes(body)
                    (directory / "reservation.json").write_bytes(raw)
                    with self.assertRaises(ValueError):
                        inventory.load_records(directory)

    def test_source_hash_guard_checks_real_bytes_before_project_imports(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            path = directory / "input.py"
            body = b"raise AssertionError('must never be imported')"
            path.write_bytes(body)
            hashes = {"input.py": hashlib.sha256(body).hexdigest()}
            inventory.verify_source_files(directory, hashes)
            path.write_bytes(body + b"\n")
            with self.assertRaisesRegex(ValueError, "inventory-source-mismatch"):
                inventory.verify_baseline(directory, self.records, hashes)

    def test_baseline_cli_option_refuses_an_unapproved_root(self):
        with tempfile.TemporaryDirectory() as name:
            error = io.StringIO()
            with contextlib.redirect_stderr(error):
                self.assertEqual(inventory.main(["--adapter-root", name]), 2)
            self.assertEqual(error.getvalue(), "inventory-refused\n")


if __name__ == "__main__":
    unittest.main()
