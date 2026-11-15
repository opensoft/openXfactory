"""The negative credential property still refuses with a nonissued value."""
from copy import deepcopy
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "contracts/identity-brokering/examples/negative/idp-credential-committed-in-manifest.yaml"


@pytest.fixture
def validator():
    spec = importlib.util.spec_from_file_location(
        "p1_identity_validator", ROOT / "scripts/validate-identity-brokering.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_negative_marker_retains_the_exact_forbidden_property_refusal(validator):
    document = yaml.safe_load(FIXTURE.read_text())
    assert document["federated_providers"][0]["client_secret"] == "NOT_ISSUED"
    findings = validator.Findings()
    validator.check_no_credential_material(findings, "synthetic-fixture", document)
    assert validator.codes_of(findings.errors) == {"credential-value-embedded"}
    assert len(findings.errors) == 1
    assert "'federated_providers[0].client_secret' is credential-shaped" in findings.errors[0]


def test_closed_world_still_refuses_the_forbidden_credential_property(validator):
    document = yaml.safe_load(FIXTURE.read_text())
    schemas = validator.load_schemas()
    schema = schemas[validator.KIND_TO_SCHEMA[document["kind"]]]
    findings = validator.Findings()
    validator.check_closed_world(findings, "synthetic-fixture", document["kind"],
                                 document, schema, schema)
    assert "closed-world-property" in validator.codes_of(findings.errors)


def test_nonissued_marker_does_not_supply_the_credential_name_refusal(validator):
    document = deepcopy(yaml.safe_load(FIXTURE.read_text()))
    del document["federated_providers"][0]["client_secret"]
    findings = validator.Findings()
    validator.check_no_credential_material(findings, "synthetic-fixture", document)
    assert findings.errors == []
