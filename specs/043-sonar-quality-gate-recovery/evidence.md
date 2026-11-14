# Sonar recovery evidence — 2026-11-14

The project has ten retained main analyses. Sonar way ID 9 is already selected;
new-code settings are absent and the current gate is NONE. The earliest retained
analysis is d20bb52c-64fd-4090-986a-fd993f44ff86 at source
8480378acd806b112ebd0462e18a86a9026ab155 (2026-09-09T19:37:08-04:00).
The inspected current source is 3432baf6d929112be283d3daa1a4330a4130ab64.
Overall findings before repair are 17 bugs, 116 vulnerabilities and 2,499 code
smells; those totals are not a passing gate or a set of accepted findings.
No coverage metric is available in the automatic analysis snapshot.

The next checkpoint records service mutation and fresh computation. Nothing is
claimed as a completed gate repair at this preparation checkpoint.


## Historical reference restored

The supported project_analyses/set_baseline operation selected exactly the
earliest retained analysis above. Readback marks only that analysis as the
manual new-code reference. The six-condition Sonar way definition and all
project profiles compare unchanged; all ten retained analysis IDs remain.
The prior saved snapshot still has NONE until a fresh analysis processes.
No issue, rule, threshold, source scope, visibility or billing change occurred.

A direct GitHub check rerequest returned HTTP 404. It is not successful
analysis evidence. The normal repository publication path will trigger fresh
analysis; no assertion is made about the cause of that generic API response.


## Governance qualification

Strict content-addressed OpenSpec 1.12.0 validation passed for this change.
The focused governed corpus/floor/reader suites passed 641 tests and 75 subtests
with the actual pinned ce923636 review core supplied; no skips. The canonical
seeder added exactly one corpus-ledger row for this change under real PR #1315
and preserved every existing row and provenance field.


## Fresh main computation and unresolved findings

Fresh main analysis cf95559d-ec71-4dff-9e6f-54f18227d283 processed source
3432baf6d929112be283d3daa1a4330a4130ab64 after the definition repair.
The gate is now computed ERROR rather than NONE. Its manual period is exactly
2026-09-09T19:37:08-04:00, the retained reference chosen above. Reliability and
security ratings on new code are D (4) against A (1). Maintainability A,
duplication 0.5% against 3%, and reviewed hotspots 100% against 100% pass.
The existing gate's six-condition definition and profiles remain unchanged.

The automatic analysis supplies no overall/new coverage metric. Accordingly
the configured 80% coverage condition is absent from the computed result;
ignoredConditions=false does not prove coverage was measured. No coverage
acceptance is claimed. Providing real CI-measured coverage requires its own
governed analysis-workflow repair, retaining the existing test commands and
production scope.

The supported sinceLeakPeriod=true issue query returns exactly three bugs and
eight vulnerabilities, matching the gate metrics. Five findings are in the
historical feature-034 at-r1 evidence script; the other six are in existing
validator, attestation, census, carve and dashboard tools. The
[acceptance/triage receipt](acceptance.json) retains all eleven issue keys,
locations and unresolved statuses. Those source findings were not introduced
by this service-only change and have not been waived, suppressed or marked
fixed. Historical evidence was not rewritten to make a quality gate green.

T003's computation/measurement readback is complete. The restoration exposes
the existing debt; it does not claim that the complete project is accepted.


## Full-suite metadata correction

The first complete PR run at fbbb5fc1 reported 10,439 passed, one failed,
six expected skips, 338 existing PostgreSQL deselections and 751 subtests.
The only failure was the new proposal's unsupported target_release token
deferred. The house vocabulary permits implemented, a named estate release
or deferred-allocation. The service operation and fresh main computation are
now verified, so the proposal uses implemented with an explicit service-only
gloss. No validator, vocabulary, check, threshold or source behavior changed.
The failed run is retained; a fresh complete run is required at the final head.


## Corrected candidate verification

The corrected target_release/corpus/floor/reader suites pass 739 tests and
75 subtests without skips. Strict content-addressed OpenSpec 1.12.0 validation
and the canonical ledger-diff check pass. All seven operating checkout heads,
statuses and staged/unstaged hashes, original registered worktree paths and
cloud session/pane identities match the fresh maintenance baseline.

The implementation and service-recovery receipts are complete; the final
documentation head must still pass the repository's full mandatory CI and its
own Codex review before publication. Earlier failed CI is retained and does
not substitute for that qualification. The computed main gate remains red for
the recorded existing findings, with coverage unmeasured.
