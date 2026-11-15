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
