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
are outside the release inventory. This does not exempt the conformance
example from the broad contracts/ rule; its marker still requires a cut.
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
both exclude this negative example. AGENTS.md nevertheless requires a release
cut for its changed conformance bytes. The earlier no-cut conclusion based
only on membership is superseded before landing. Original history is retained;
no liveness test or rotation occurs. The next minor carries the marker,
manifest, changelog and generated inventory atomically.

A matching stamp does not make an incomplete cached tree reusable. Missing
owned install files bypass that retained generation and allow a healthy later
generation or a fresh exclusive install. Linked/unsafe state still refuses
rather than being reclassified as absence. Both cases are exercised through
the real CLI path with a synthetic registry before consumer re-vending.

The wallet duplication gate identified the old copied refusal-code block in
the pinned neutral spec. The provider now maintains one described refusal
catalog and derives the unchanged fixed vocabulary and CLI help from it.
This removes the parallel comment/tuple catalog, documents machine refusals
at the entrypoint and keeps every existing code, check and exception rule.
All consumers re-vendor these provider bytes; no local fork or exclusion is
introduced and no threshold changes.

## Review correction: broad contract rule controls release
The 342-member digest membership audit is accurate but does not exempt a
conformance example from AGENTS.md's broader contracts/ rule. The earlier
no-cut interpretation is superseded. The marker is realized through the next
available minor after final integration/claim readback, with atomic manifest,
changelog, fixture and new inventory changes; all old inventories/tags remain.
The existing 30-second CLI guard and all domain regression cases still run.

## Allocated realization
contract-v4.2 is allocated after #1321/#1323 landed, at main
5b636c767fccf253165b36b6aed4fe04eb8cd27b. Row-4 claim:
opensoft/openXfactory#630 comment 6901128126. The manifest, changelog,
fixture declaration and generated contract-v4.2 inventory form one forward
candidate; old release objects remain immutable. Verify exact candidate,
supported-domain regression and post-merge promotion before publishing its
annotated tag, then verify independent tag readback.

Forward-only candidate refresh after main #1326/#1328:
a3bef00d503176c55660fb2e1bc9133a9a510686 is integrated normally, retaining
both the workflow-wide qualified-runtime assertion and the upstream per-job
lock-ABI assertion. No history is rewritten. The 10,762-pass full cut CI
exposed two failures in the intentionally closed intent-compliance release
enum. T009 also advances tests/intent-compliance/test_release_boundary.py to
explicitly classify contract-v4.2 on the existing registered side; unknown
future versions still fail, and the membership/schema-pin assertions remain.
Rebuild the new inventory after that release-member test changes. The
supported-domain denominator and PostgreSQL source footprint remain required.


## Final execution-boundary verification (2026-11-16)

Published main fefb5ae4ad7227a53469d5f1c711632d993b0dcf passed the unchanged
six-condition gate, but three original injection findings remain open.
Retain the original 40-key snapshot and all prior receipts. Complete the existing
P1 repair by revalidating every target at the execution boundary, reconstructing
only fixed strict commands and bounded change identifiers, and holding the
operator-selected npm path separately from the mutable parser namespace.
Test invalid direct-call target batches before any child process starts.
No exclusions, issue waivers, baseline changes, dependency or billing changes.
