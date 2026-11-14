# Verification
Status: draft

Run in the declared development bench from this isolated feature checkout.

1. Install the existing runtime test lock and separate hash-pinned analysis
   lock into an isolated environment. Retain normal required test selection.
2. Run focused source counterexample tests, including optimized private-copy
   preflight, canonical/symlink path boundaries, Git operands and sealed CWD.
3. Run the complete required test command with coverage startup enabled;
   combine the real subprocess data and generate XML plus source inventory.
4. Require all owned production Python files and resolvable source lines in
   the report; retain zero-hit code and the exact existing skip/freshness
   assertions. Add behavioral tests for measured gaps instead of exclusions.
5. Validate this OpenSpec change through the pinned strict CLI and seed/check
   the corpus ledger with the actual PR identity.
6. Qualify all PR checks and exact-head Codex review. Once CI analysis is
   concrete and ready, switch this project's automatic analysis off, run the
   scanner and require a real computed gate.
7. Land through the existing rules/holds, verify the published tree, repeat
   all declared main workflows and read the exact main analysis: six evaluated
   passing conditions, including coverage at least 80 and the same period.
8. Compare operating checkout/worktree/session fingerprints and retain all
   historical verdicts, source preimages, analysis identities and billing.

## Measured local execution

The working tree must match the selected commit. Use a fresh output directory;
keep previous report directories as external evidence before another attempt.
The runtime lock remains independent from the analysis-only lock.

~~~sh
python3 -m venv .venv
.venv/bin/pip install --require-hashes -r requirements/hermes-runtime-contracts.lock --only-binary=:all:
.venv/bin/pip install --require-hashes -r requirements/sonar-analysis.lock --only-binary=:all:
export PATH="$PWD/.venv/bin:$PATH"
python3 -m pytest tests/sonar_quality/test_coverage_evidence.py::test_subprocess_startup_records_real_child_execution -q
unset COVERAGE_PROCESS_START COVERAGE_PROCESS_CONFIG
python3 -m pytest tests/hermes_runtime_contracts/test_validator_cli.py::test_release_mode_field_is_preserved_on_the_real_repository -q
python3 scripts/validate-sonar-coverage.py prepare
export COVERAGE_ROOT="$(pwd -P)"
export COVERAGE_FILE="$COVERAGE_ROOT/.coverage-reports/.coverage"
export COVERAGE_PROCESS_START="$COVERAGE_ROOT/.coveragerc"
python3 -m pytest tests/ -q -m "not postgres" --junitxml=pytest-report.xml
unset COVERAGE_PROCESS_START
python3 scripts/validate-sonar-coverage.py report
python3 scripts/validate-sonar-coverage.py check
~~~

Initialize the same three public providers and pinned decision core that the
required workflow initializes; set PINNED_CORE_CHECKOUT to that runtime-resolved
checkout. The CI census, exact skip budget and two named verdicts remain the
acceptance authority. Generating a report alone does not satisfy them.

The CI scanner receives only the verified XML, JSON, JUnit and receipt from
the successful test job. Its clean source-only checkout has no provider
submodules. All root-owned production languages remain analyzed. The only
test classification additions are the real avatar-broker tests/support and
feature 040's two test modules; maintained evidence tools remain source.

For main, the final CI gate command is
~~~sh
python3 scripts/validate-sonar-coverage.py gate
~~~
It consumes the scanner task receipt and an environment-held analysis
credential, requires the same project/gate/reference identity, and writes a
secret-free evaluated receipt. It does not alter server settings or issue state.

The root suite now collects feature 040's original evidence refusal classes
through tests/private_connectivity/test_evidence_witnesses.py. Their original
files and independent invocation paths stay intact. This closes the measured
collection gap without duplicating or rewriting the witnesses. Runtime coverage
paths use the physical checkout root so symlink aliases cannot hide execution.
