# P1 security boundary implementation
Status: draft

- [x] T001 [O] Record authorized scope and design before code — files: `openspec/changes/remediate-p1-security-boundaries/`, `specs/045-p1-security-boundaries/` — verify: `python3 scripts/validate-code-surface.py`
- [x] T002 [US1] [O] Prove credential/browser counterexamples and implement safe writes — files: `scripts/nlm_auth.py`, `scripts/safe_tooling_io.py`, `tests/notebooklm/test_nlm_auth.py`, `tests/sonar_quality/test_p1_boundaries.py` — verify: `python3 -m pytest tests/notebooklm tests/sonar_quality/test_p1_boundaries.py -q`
- [x] T003 [US2] [O] Lock privileged Python/CLI installs with real offline functional acceptance — files: `.github/requirements/`, `.github/worker-cli/`, `.github/workflows/doc-health-reusable.yml`, `.github/workflows/merge-master-approval.yml`, `.github/workflows/privileged-dependencies.yml`, `tests/sonar_quality/test_p1_ci_dependencies.py` — verify: `python3 -m pytest tests/sonar_quality/test_p1_ci_dependencies.py tests/review_lane_pin -q`
- [ ] T004 [US4] [O] Review/publish phase 1 and verify actual main — files: `README.md`, `specs/045-p1-security-boundaries/` — verify: `python3 -m pytest tests/sonar_quality tests/notebooklm -q`
- [ ] T005 [US3] [O] Repair worker/report output boundaries — files: `scripts/safe_tooling_io.py`, `scripts/doc_health/derive_possibles_dispatch.py`, `scripts/doc_health/readiness_dispatch.py`, `scripts/ideation_dashboard/dashboard_refresh_lane.py`, `tests/sonar_quality/test_p1_boundaries.py` — verify: `python3 -m pytest tests/doc-health tests/ideation-dashboard tests/sonar_quality/test_p1_boundaries.py -q`
- [ ] T006 [US3] [O] Repair policy/pin/plan file boundaries — files: `scripts/ideation_dashboard/intent_apply_lane.py`, `scripts/review_lane_repin.py`, `scripts/set-domain-openxfactory-pin.py`, `tests/sonar_quality/test_p1_boundaries.py` — verify: `python3 -m pytest tests/sonar_quality/test_p1_boundaries.py tests/review_lane_pin -q`
- [ ] T007 [US3] [O] Repair OpenSpec executable/operands and coordinate consumer parity — files: `scripts/validate-openspec-cli-pin.py`, `tests/openspec_cli_pin/`, `specs/045-p1-security-boundaries/` — verify: `python3 -m pytest tests/openspec_cli_pin -q`
- [ ] T008 [US3] [O] Constrain PostgreSQL trusted executable/template boundary — files: `scripts/validate-hermes-runtime-postgres.py`, `tests/hermes_runtime_contracts/`, `specs/045-p1-security-boundaries/` — verify: `python3 -m pytest tests/hermes_runtime_contracts -q -m "not postgres"`
- [ ] T009 [US4] [O] Establish negative fixture provenance and legitimate owner/release disposition — files: `specs/045-p1-security-boundaries/` — verify: `python3 -m pytest tests/sonar_quality/test_p1_boundaries.py -q`
- [ ] T010 [US4] [O] Reconcile all 40 keys and final actual-main/preservation evidence — files: `README.md`, `specs/045-p1-security-boundaries/` — verify: `python3 -m pytest tests/sonar_quality tests/notebooklm -q`

Cross-repository consumer or release implementation adds exact owning files and
verification here before any dependent edit; no speculative task tick grants
release authority. Each landing also requires real exact-head review and CI,
published-main Sonar and unchanged-state readback beyond these local commands.
