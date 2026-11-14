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
