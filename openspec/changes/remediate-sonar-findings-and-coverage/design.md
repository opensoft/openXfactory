## Context

Main has ten active reliability/security findings and no coverage measurement.
The original eleven-finding receipt is dated evidence; the attestation finding
is currently auto-closed and has repeated close/reopen cycles on unchanged
source. The September manual baseline and six-condition Sonar way gate stand.

## Goals / Non-Goals

Deliver source fixes with counterexample tests and measured coverage, then
verify all six conditions on actual merged main. Preserve the existing test
commands, collection floors, exact skip budgets, provider/freshness checks,
source ownership, active sessions and historical executions. Existing bugs
outside the new-code period remain visible; no global issue disposition,
baseline reset, production exclusion or billing change is part of this work.

## Decisions

Use the invocation working directory as the trusted boundary for ordinary
CLI file operands. The private browser copy has an independently declared
OPENDOX_STATE_DIR and a fixed console/port filename; owner/mode, regular-file,
descriptor and URL checks stay fail-closed under optimized Python as well.
Use positive Git operand/OID validation and a read-only judged container CWD.
Keep the replay harness maintained; preserve its immutable old Git preimage
and all original verdict/log bytes in a new provenance companion.

Keep the literal full pytest invocation. An analysis-only hash-pinned coverage
dependency and process-start configuration collect parent and subprocess
branch execution. Include namespace packages and audit every owned Python
source in the report, including zero-hit files. Genuine tests are classified
by an explicit inventory; the replay/maintenance tools stay production source.
All tracked production languages remain analyzed. The single unchanged
JavaScript file predates the fixed baseline; no fabricated LCOV is introduced.

A separate clean-checkout scanner job consumes only generated report evidence
from the successful test job at the same commit. Its checkout omits materialized
foreign gitlinks, matching the original root-owned analysis scope. The existing
organization SONAR_TOKEN is available to this repository; no credential copy,
permission grant or new token is needed. Pin the scanner action immutably and
declare any new foreign pin through the existing strict pin class.

## Risks / Trade-offs

Subprocesses can clear instrumentation: measure actual hits and add behavioral
tests where coverage is missing; never invent hits. Instrumentation can change
test timing: retain all existing failures/skip guards and adjust implementation
rather than suppressing tests. Automatic and CI analysis conflict: disable
automatic analysis only when the concrete scanner pipeline is ready, then
observe actual server processing. Missing coverage or an unevaluated condition
is refusal even if the server reports a nominal OK.

## Migration Plan

Qualify source fixes and genuine reports locally, publish through the existing
review/check process, switch this project to CI analysis, and qualify the PR.
Land only after exact-head tests/review and ownership holds allow it. Verify
published-tree equality, actual-main CI and an OK result with all six existing
conditions, including evaluated coverage at least 80 percent and the original
manual period. Preserve project/issue/history identities and all evidence.
A technical scan failure is repaired in CI; rollback must not waive a gate or
advance its historical reference merely to obtain green.

## Open Questions

No product choice is unresolved. The baseline coverage run determines which
additional behavioral tests the measured gaps require.

## Original deadline and measurement cost

The complete CLI test module retains its normal 30-second subprocess limit
in a required uninstrumented preflight, before coverage measurement starts.
The fully instrumented suite repeats all the same cases and assertions with
a separate bounded 90-second measurement budget; tracing complete release
inventories otherwise exceeds the normal limit on some runners. No original
functional or timing check disappears.

Their published-ref transport is a local bare Git repository exposing the
actual annotated bundle tag object and checkout's published-main object.
The implementation still validates the canonical real repository, object
ancestry, release inventories and domain-dependency error through real Git.
A command-scoped URL rewrite in a test-only executable redirects transport;
no active repository configuration is modified and no Git results are faked.
The independent live release-tag workflow remains unchanged.
