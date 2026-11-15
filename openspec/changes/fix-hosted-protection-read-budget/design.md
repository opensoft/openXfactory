## Context

The T012Q candidate at adapter 3ba2d5550952 preserves D7's three protection
reads/thirteen total. `_derive` calls `current_plan` twice. The caller derives
before and after independent acceptance; that authority also derives once.
Six complete observations require twelve successful environment/policy GETs,
with an allocation of eighteen when each permits two bounded policy pages.

## Goals / Non-Goals

Preserve six independent current observations and complete-byte recomputation.
Correct accounting, not freshness, is changed. No setup, dispatch, staging, public
listener, runtime activation, neutral profile, contract/pin or credential widening.
This source candidate requires later owner ratification before landing.

## Decisions

### D1 — Explicit allocation at the trusted finalizer entrypoint

Ordinary admission/correlation retains protection/source/control/correlation
3/4/2/4 (thirteen total). The trusted `finalize` entrypoint selects a separate
finalization allocation on its fresh Decision before any callback: at most six
protection observations and 18/4/2/4 reads (twenty-eight total). Each protection
observation still has one environment GET and at most two 32-entry policy pages;
all required typed fields, explicit branch type and exact main policy remain.
There is no worker input, CLI switch, late upgrade or caller-supplied limit.
The eighteen-read limit alone is insufficient: a seventh observation refuses
before I/O even if earlier observations used only two reads each.

### D2 — One enclosing accounting ledger

The independent authority retains its own selected observers, clocks and complete
byte derivation. It joins the caller's existing ledger before any read rather
than starting fresh counters. At most caller and one authority may join; existing
ledgers, spent/expired decisions, third members and counter regression refuse.
Per-member correlation high-water is retained, with four correlation reads across
both members, never four per member. All clients reference the same group counts
and observation count. Default standalone authority use does not gain the larger
allocation. All unchanged ARM/key/private limits remain 24/3/12; requests cannot
reset the shared twelve plan-fact observations in a complete finalization.

### D3 — No time expansion or observation reuse

Each member must satisfy its original wall and monotonic deadline at every shared
checkpoint. Propagate the earliest wall expiry to all members. The authority's
monotonic end is capped to the caller's remaining time; checking both clocks
prevents a new local clock/end from extending the caller. Existing 5-second
connect/10-second enclosing decision, no retry/redirect, fixed-origin reads,
response limits and stale/revoked-fact refusal remain unchanged. No snapshots are
reused between phases, no field is omitted and no copied candidate is evidence.
A coordinated hold still does not establish atomic main pinning.

## Risks / Trade-offs

This explicitly raises only finalization's maximum total reads. It does not
increase available time or promise six remote observations finish in ten seconds;
real provider latency/semantics and hosting remain future qualification gates.
The exact six-check call graph is bounded: adding a phase requires a governed
allocation change. This amendment does not qualify future staging/guest services
or expand their private-operation allowance. No automatic retries or migration.

## Migration Plan

Keep the original frozen proposal byte-identical. Review/ratify this amendment
with the adapter source candidate. Feature017 remains the sole task owner. Source
landing must follow the governance PR, and both are separate from T013 operations.

## Open Questions

None for this bounded source candidate. All operational selections remain gated.
