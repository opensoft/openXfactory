# Implementation Plan: P1 security boundaries
Branch: 045-p1-security-boundaries
Date: 2026-11-15
Status: draft

## Summary
Implement the directly authorized P1 backlog through one task list and phased
PRs: private profile safety and privileged CI installers first; remaining P1
writers/executables and release/vendor dependencies follow. Preserve 044 and
PR #1320 as their original evidence.

## Technical Context
Python 3.12/POSIX in py-bench, Git/GH in cloud-bench, pytest, actionlint,
existing coverage pipeline and pinned providers. New CI-only locks live under
.github so the existing runtime release lock remains byte-identical.

## Constitution Check
OpenSpec precedes implementation, draft authority is not ratification, neutral
ownership and current governance remain. User's direct request authorizes this
repair and main verification; no credential rotation, session interruption,
runtime activation or billing mutation. Existing exact skip/census/freshness,
coverage inventory, gate conditions and historical reference are retained.

## Project Structure
openspec/changes/remediate-p1-security-boundaries/ governs the decision.
specs/045-p1-security-boundaries/ owns requirements, tasks, analysis and receipts.
Owning scripts/tests and CI-only locks implement the repair. Contract/release
and vendor-byte updates obey existing owner/consumer ordering.

## Governed invariants
- .github/workflows/ — privileged dependency behavior; check names/participation intact.
- .github/requirements/ — fixed tooling-only dependency artifacts.
- .github/worker-cli/ — fixed lifecycle-free worker installation closure.
- scripts/safe_tooling_io.py — trusted filesystem boundary.
- scripts/nlm_auth.py — private credential identity/ownership/write boundary.
- scripts/validate-openspec-cli-pin.py — pinned verifier byte parity and integrity.
- contracts/ — published versioned corpus; only legitimate release changes.
- specs/045-p1-security-boundaries/ — current feature decisions and measured evidence.

## Verification
Meaningful pre-fix counterexamples and valid controls; focused changed-child
suites; offline hash/wheel and CLI version installation; actionlint; complete
unchanged required CI and measured coverage; exact-head hosted Codex review;
actual merged-main gate/analysis/issue readback; preservation fingerprints.

## Landing Strategy
Phase 1 credentials + privileged installers, then remaining P1 repair families.
Each phase has independent reviewed exact-head CI/main acceptance. Do not
advance foreign pins before children publish or hand-edit historical inventories.

## Phase 2 authority and I/O refinement
CLI working directory is trusted controller scope, independent from model
operands. Resolve verified aliases of that same root, then validate every
untrusted component without following links. Explicit output operands are
checked before business/build/write work. Existing Python APIs still receive
their explicitly trusted roots/paths; intrinsic file operations always refuse
linked/non-regular/hardlinked targets, honor read-only state and use held
directory descriptors plus atomic updates.

Worker bundle child names are confined to their declared output directory.
Read-modify-write operations retain the opened original and compare identity/
metadata before publication, preserving concurrent changes.

The intent allowlist is an operator-selected input, not a model-selected policy.
XFACTORY_INTENT_ALLOWLIST_PATH binds the exact expected path; the default
allowlist.json at invocation root preserves the existing controller fetch.
An explicit project-register operand must match XFACTORY_PROJECT_REGISTER_PATH
or the provider's existing discovered register. These trusted launch settings
must not be exposed as model parameters. Direct trusted library callers retain
their existing data interfaces; CLI callers cannot redirect policy inputs.

CI-generated plan/body outputs may also use RUNNER_TEMP, independently selected
by the trusted runner environment. Model operands cannot grant a new scratch
root. Artifact input reads remain bounded, regular/single-link and no-follow.
Existing non-secret modes are retained; special-mode/shared-write/read-only
targets refuse. Descriptor-held compare-and-replace detects changes during
preparation without claiming exclusion of arbitrary same-UID native writers.

## Phase 3 execution boundaries
The maintained OpenSpec verifier stays standalone for byte-identical vending.
CLI-selected npm executables must match the independently operator-configured
XFACTORY_NPM_BINARY (default: npm resolved from trusted PATH); subsequent
execution uses that trusted selection. Change identifiers are bounded single
identifiers and cannot become options or paths. Existing content addresses,
closure validation, strict flags, complete-target iteration and reported
findings/disposition predicates remain enforced.

The PostgreSQL readiness CLI requires its template to match the independently
operator-configured XFACTORY_PSQL_COMMAND. The committed synthetic PostgreSQL
harness supplies its generated disposable-cluster template through that
environment setting, before invoking the CLI. Database operands are bounded
names, never child options; no live database or running workload is targeted.
Direct trusted library composition retains its explicit injected runner API.

Provider publication must precede vendored consumer-byte and exact-pin movement;
there is no parity exception. Contract release members move through a proper
release cut; the currently open #1298 reserves contract-v4.1, so no competing
cut or historical inventory rewrite is authorized by this plan.
