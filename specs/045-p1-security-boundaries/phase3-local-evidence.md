# Phase 3 execution boundaries
Status: draft

The standalone OpenSpec verifier binds CLI npm selection to the operator's
XFACTORY_NPM_BINARY or npm from trusted PATH and executes that selection.
Named changes are bounded identifiers rather than child options or paths.
The full content-addressed artifact and locked dependency closure remain
verified; lifecycle scripts remain disabled; every requested target remains
strict and every target runs.

The PostgreSQL readiness CLI binds its command template to the independently
configured XFACTORY_PSQL_COMMAND. Database names cannot become child options
or executable paths, and the database placeholder cannot select an executable.
The committed disposable-cluster controllers supply their generated template
through that environment. Trusted library composition retains the injected
runner API; no live deployment target or existing credential is modified.

Local validation:
- 191 execution-boundary and OpenSpec pin tests passed.
- The real pinned OpenSpec CLI 1.12.0 ran the entire corpus through the modified
  verifier with its actual integrity-checked npm installation. It reported
  130 passing items and one existing, explicitly reported accepted exception,
  with zero undispositioned failures and exit zero. This is not a clean-tree
  assertion and no disposition was added or changed.
- 101 real PostgreSQL tests passed using the unchanged digest-pinned 15 and 16
  images and the harness's disposable databases/containers. The modified
  readiness CLI, clean-apply and drift paths ran with operator-bound templates.
  The existing harness completed its teardowns; no active bench/session or
  existing database was restarted, targeted or reconfigured.

Provider publication, exact consumer-byte coordination, CI and main readback
remain required. The negative fixture's issuance provenance remains unknown;
its original history is retained, and no token exchange or rotation was tried.

## Pin, artifact and retained-cache boundaries
Both entrypoints now bind source selection to independent operator authority.
Pin, lockfile and tarball reads are bounded, regular, single-link and no-follow.
Materialization retains directory descriptors through npm; a substituted parent
cannot redirect writes and is refused before publishing the resulting path.
Cache generations are owned and not shared-writable. Incomplete or invalid
generations and unique fetch workspaces are retained; concurrent runs do not
clear shared install state. Escaping cached executable links refuse.

The expanded pin/execution suite passed 205 tests. The real pinned CLI 1.12.0
was then installed twice through the changed installer and returned the same
verified executable. Both cached and fresh no-cache strict full-corpus runs
completed with zero undispositioned failures and the same one retained accepted
exception. The new filesystem execution path is qualified in the declared Linux
bench; unavailable safe descriptor/proc support refuses instead of falling back.

## Complete PostgreSQL source-bound acceptance
The unchanged complete matrix runner passed all 171 required nodes on each
unchanged pinned PostgreSQL 15 and 16 image: 342 real cases, zero missing,
skipped, deselected-in-scope or non-passing nodes. Its execution-report checker
verified actual node results before emitting either record. Both reports bind
the repaired 78-input digest
sha256:532945ef596214b429b2e2fc1112e313276587fbb06311180b2c69147d52b33b,
which independently matches the current source. Node digests and matrix digest
are unchanged. Each task-owned Compose stack completed its scoped teardown.

The earlier canonical records are preserved byte-identically under
tests/hermes_runtime_contracts/postgres/evidence/history/pre-p1-security-20261115/.
Only the current canonical reports are refreshed from actual runner output.
The fixture index, all release members/inventories/tags and image lock remain
unchanged. Exact release membership disproved the earlier blanket assumption
that the marker example or these acceptance reports required a new cut.

## Consumer review and duplication correction
Three new missing-tree cases failed before the cache correction; missing
manifest, binary and node_modules now bypass retained stamped generations.
Linked and hardlinked manifests still refuse. With the catalog/help correction,
302 pin/execution/citation tests pass. The real 1.12.0 installer also recovered
from an intentionally incomplete task-owned generation entirely offline,
selected the retained healthy generation, and passed the complete strict corpus
with zero undispositioned failures and the same one accepted exception.

The refusal catalog now supplies both the unchanged ten machine codes and
their operator help descriptions, replacing the parallel tuple/comment table.
Physical condition citations were updated with their exact guard assertions
retained. No source exclusion, threshold, code waiver or billing change occurs.

The broader local correction run passed 325 cases with one unchanged
30-second realization-mode timeout; its candidate companion passed on retry
and realization again timed out locally. The original unmeasured 30-second
CI guard is unchanged and must pass on the hosted candidate before landing.


### Final argument-boundary candidate (2026-11-16)

Main fefb5ae4ad7227a53469d5f1c711632d993b0dcf passed the unchanged
six-condition gate with 37/40 original findings fixed. Remaining keys:
AaCIimK91WTeVOIYRV0e, AaCIimK91WTeVOIYRV0f, AaCIimK91WTeVOIYRV0g.
This correction holds trusted npm separately from the mutable parser namespace,
reconstructs each named target inside its validation loop, and validates the
whole target batch again before either public execution path starts.
An invalid later target prevents earlier targets from running.
Focused execution-boundary and OpenSpec pin suites: 232 passed.
Exact-head CI/review, consumer publication and all-40 main readback are pending.
No issue statuses or gate configuration were changed.
