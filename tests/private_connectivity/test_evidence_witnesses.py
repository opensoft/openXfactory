"""Collect feature 040's existing refusal witnesses in the required root suite.

Keep their maintained source and independent invocation paths intact. The
required workflow invokes only tests/, so leaving them solely under specs/
silently omits the evidence dependency/ownership/field-refusal behaviors.
"""
from pathlib import Path
import runpy

WITNESSES = Path(__file__).resolve().parents[2] / "specs/040-private-connectivity/tests"
PinInventoryTests = runpy.run_path(str(WITNESSES / "test_pin_inventory.py"))["PinInventoryTests"]
EvidenceTests = runpy.run_path(str(WITNESSES / "test_verify_evidence.py"))["EvidenceTests"]
