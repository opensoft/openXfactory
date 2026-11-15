# Tasks: Measured Sonar quality acceptance
Status: draft

## Phase 1: Governed setup

- [x] T001 [O] Record and strictly validate the authorized decision and single-feature plan — files: `openspec/changes/remediate-sonar-findings-and-coverage/`, `specs/044-sonar-quality-remediation/`, `AGENTS.md`, `README.md` — verify: `python3 scripts/validate-openspec-cli-pin.py --change remediate-sonar-findings-and-coverage --strict`

## Phase 2: Safe maintained tools (US1)

- [x] T002 [US1] [O] Prove and repair ordinary path, data-only Git revision, exclusive attestation output, missing-row and sealed-CWD boundaries — files: `scripts/validate-factory-mcp.py`, `scripts/measure_opendox_css_census.py`, `scripts/validate-carve-manifest.py`, `scripts/attest-openspec-cli-pin-lockfile.py`, `scripts/carved_reach.py`, `scripts/ideation_dashboard/dashboard_refresh_lane.py`, `tests/factory-mcp/test_factory_mcp_conformance.py`, `tests/carve_manifest/`, `tests/ideation-dashboard/test_dashboard_source_seal.py`, `tests/sonar_quality/` — verify: `python3 -m pytest tests/factory-mcp tests/carve_manifest tests/sonar_quality tests/ideation-dashboard/test_dashboard_source_seal.py -q`
- [x] T003 [US1] [O] Make replay preflight explicit and descriptor-safe under optimization; preserve dated proof with new provenance — files: `specs/034-opendox-standalone-operation/evidence/at-r1/at_r1_browser.py`, `specs/034-opendox-standalone-operation/evidence/at-r1/preflight.py`, `specs/034-opendox-standalone-operation/evidence/at-r1/run-at-r1.sh`, `specs/034-opendox-standalone-operation/evidence/at-r1/sonar-remediation-provenance.md`, `tests/sonar_quality/` — verify: `python3 -m pytest tests/sonar_quality/test_browser_preflight.py -q`

## Phase 3: Measured quality acceptance (US2)

- [x] T004 [US2] [O] Add isolated analysis lock, whole-source measurement, artifact checks and credential-separated CI scanning — files: `requirements/sonar-analysis.in`, `requirements/sonar-analysis.lock`, `.coveragerc`, `sonar-project.properties`, `.gitignore`, `.github/workflows/pytest-suite.yml`, `scripts/validate-sonar-coverage.py`, `tests/sonar_quality/`, `tests/conftest.py`, `scripts/doc_health/pin_class.py`, `tests/doc-health/test_sentinel_vocabulary.py`, `tests/doc-health/test_pin_reachability.py` — verify: `python3 -m pytest tests/sonar_quality tests/clearing/test_clearing_gate_wiring.py tests/council_convening/test_gate_wiring.py tests/review_lane_pin -q`
- [ ] T005 [US2] [O] Measure full-suite gaps, retain original bounded release-mode checks before measurement, and add meaningful behavioral coverage without omissions or new skips — files: `tests/`, `specs/044-sonar-quality-remediation/evidence.md` — verify: `python3 -m pytest tests/ -q -m "not postgres" --junitxml=pytest-report.xml`
- [ ] T006 [US2] [O] Validate complete resolvable coverage inventory and genuine subprocess data at the candidate source — files: `scripts/validate-sonar-coverage.py`, `tests/sonar_quality/`, `specs/044-sonar-quality-remediation/evidence.md` — verify: `python3 -m pytest tests/sonar_quality -q`

## Phase 4: Evidence and publication (US3)

- [x] T007 [US3] [O] Qualify source/preimage evidence and unchanged provider/runtime contracts — files: `specs/034-opendox-standalone-operation/evidence/at-r1/sonar-remediation-provenance.md`, `tests/sonar_quality/`, `specs/044-sonar-quality-remediation/evidence.md` — verify: `python3 -m pytest tests/sonar_quality -q`
- [ ] T008 [US3] [O] Publish canonical ledger row using actual PR ID; qualify exact-head CI and Codex review — files: `tests/sequenced_after/corpus-ledger.yaml`, `specs/044-sonar-quality-remediation/`, `README.md` — verify: `python3 scripts/validate-sequenced-after.py --ledger-diff`
- [ ] T009 [US3] [O] Cut over prepared CI analysis, land under existing rules and verify all six conditions on actual main — files: `specs/044-sonar-quality-remediation/evidence.md` — verify: `python3 scripts/validate-sonar-coverage.py gate`
- [ ] T010 [US3] [O] Record final preservation, billing/configuration identity and main acceptance readback — files: `specs/044-sonar-quality-remediation/`, `README.md` — verify: `python3 scripts/validate-sonar-coverage.py gate` plus exact-main history/configuration and preservation readback


## Dependencies and execution

T001 precedes source changes. T002 and T003 are independent source slices;
T004 follows their interface decisions. T005 and T006 use the real measured
baseline and candidate reports. T007 preserves original proof before
publication. T008 precedes T009; T010 closes only after actual main qualifies.

Within each slice, write counterexample tests before implementation and run
its verify command before completion. An initial measurement can run over the
frozen prior maintenance tree while this separate worktree is developed.
The scanner credential is not available to test subprocesses. No archive,
contract cut, billing change or foreign-session mutation is part of the list.
