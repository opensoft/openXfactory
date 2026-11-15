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
there is no parity exception. Contract release members move through a proper release cut. Live readback
confirmed contract-v4.1 is already published and #1298 is an archive-only PR.
The next minor is allocated only at realization after merge order is known;
an open proposal cannot reserve a number. Historical inventories stay intact.

OpenSpec execution repair also binds alternative pin authority independently,
bounds tarball and cache locations, uses descriptor-relative bounded reads and
refuses linked or substituted state. Invalid cache generations and fetch
evidence remain intact; a new verified generation replaces destructive cache
rebuilds. Both maintained verifier and installer entrypoints use the same
standalone verifier logic. Existing strictness, hash checks and installed
package/version assertions remain enforced.

The source-bound PostgreSQL records must be regenerated by the full existing
matrix runner after changed indexed inputs; selected live-test results do not
replace the exact complete node census. Archive the original canonical reports
byte-identically under a dated history subdirectory before replacing the
current reports with actual runner output. Keep the release-member fixture index
and its result references unchanged. A membership audit of all 342 recorded
members confirms that reports, changed tooling/tests and the negative fixture
are outside the release inventory. No contract cut is needed for these changes.
Source-line citations move with the verifier, retaining identical condition
quotes and guard equivalence assertions.

## Fixture marker and verified membership
The historical Entra-shaped literal has unknown issuance provenance. Its
forbidden client_secret property is independently rejected by the unchanged
closed schema and credential-name scanner, including with a plain NOT_ISSUED
marker. Replace only the current fixture value and explanatory comments;
retain expected_failure and expected_failure_detail exactly. Other packaged
negative fixtures continue to exercise value-class detection.

Exact current catalog membership and the published contract-v4.1 inventory
both exclude this negative example. No contract, manifest, changelog, inventory
or tag needs to change for this marker repair. Original history is retained;
no liveness test or rotation occurs. The original assumption that every
contracts/ example was a release member was disproved before any cut was made.

A matching stamp does not make an incomplete cached tree reusable. Missing
owned install files bypass that retained generation and allow a healthy later
generation or a fresh exclusive install. Linked/unsafe state still refuses
rather than being reclassified as absence. Both cases are exercised through
the real CLI path with a synthetic registry before consumer re-vending.
