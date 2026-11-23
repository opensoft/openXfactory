# Whole-registration infrastructure accounting

Status: draft; no replacement numeric policy selected or accepted.

## Context

The accepted P3 boundary already separates setup rollback/run cleanup authority
and current read-only late observation from expired setup/proof grants. Existing
adapter methods implement setup-bound per-resource provider operations. The
[diagnostics](supporting-docs/eligibility.md) show both the expected expiry refusal
and an actual ordinary private-budget exhaustion before completing the second of
six resources. Separately traced namespace calls are unmetered. The accepted P07
plan expressly requires a governed amendment before dependent code in this case.

## Goals / Non-Goals

Define an accountable original infrastructure scope for the complete first-pilot
registration, reconciliation and result. Keep original identity, one-send claims,
independent current observations and retained state across host loss.

This draft supplies no new cap, deadline, phase identifier, receipt field, neutral
API, dependency, service role, public endpoint, credential or operational input.
P08 packaging, P09 integration, live target setup/dispatch, human and consumer
acceptance remain separately gated. No existing allowance is raised.

## Decisions

### D1: Separate infrastructure accounting, selected only by governed source

A future accepted policy must name its exact source-selected registration/cleanup
scope and finite limits. It must not repurpose a proof phase or increase ordinary
ReadBudget defaults. Setup rollback and actual-run cleanup keep their genuine
registered authority; neither can be reconstructed from an expired creation grant.

The policy must specify which counters are cumulative over registration/recovery
and which belong to one bounded observation. Original mutation consumption and
absolute cleanup expiry survive process loss and duplicate triggers. A recovered
process may establish a local timer only within retained original authority; it
cannot restore a consumed send, reset cumulative charges or join remote clocks to
renew proof. Separately current read-only observation cannot spend mutation scope.

Rejected alternatives: a fresh Decision per resource, borrowing qualification or
finalization limits, and ignoring nested state calls. Each can hide the actual
whole-graph cost or change the accepted authority without an owner decision.
Raising only the existing private-read number leaves namespace I/O unaccounted.

### D2: Account at real call boundaries before effects

The complete inventory must distinguish authenticated private exchanges, namespace
reads/conditional writes, retained registration/trigger/action state, ARM sends
and operation observations, fences, immutable receipts, independent absence,
credential revocation, preservation and final audit. Charge actual nested I/O
once before each call; include every callback, retry, poll, pagination and
reconstruction in the selected finite allowance. Pure parsing and a cache hit
need no invented exchange, but a cache label cannot authenticate aggregate facts.
Backend write attempts and losing conditional claims must be represented honestly.

The source policy must define the accounting trust boundary for injected ports.
Hidden remote work cannot be treated as free local work; an explicitly local
SQLite fixture cannot establish that deployed services make no hidden calls.
Durable consumption before side effects is necessary; a failed acknowledgement
cannot replenish a slot. No runtime initialization, reset or repair is introduced.

### D3: A complete measured graph precedes any numeric selection

Use the exact first-pilot S1 reservation and approved retained/shared scope, not a
six-resource substitute. Preserve the existing resource maximum of 24 and complete
canonical 16,384-byte receipt cap. Measure reservation-only partial setup, genuine
post-P7 scope, original pending/ambiguous operations, duplicate/crash boundaries,
late failure and current-observer refusal. Every positive must start from working
authenticated ports and independently observed effects.

The cost record must include original wall and monotonic clocks, exact charge
events and actual complete serialized bytes. Frozen-clock scope diagnostics are
ineligible for elapsed-deadline claims. The old fixture's eager timeout comparison
must not obscure the intended boundary; new timing fixtures must distinguish the
caller's sampled interval from a later decreasing remaining-time sample without
weakening the product's original deadline enforcement.

The measured six-kind per-resource sum of 60 private / 24 ARM / 96 namespace calls
is diagnostic only: it uses distinct Decisions and omits full registration and
observers. It selects no limit. Until the complete inventory and finite numeric
policy are reviewed and accepted, dependent product implementation stays blocked.

### D4: Preserve the cleanup and observation authority distinction

The owning adapter may later add source-selected cleanup paths to namespace and
provider code without rewriting original reservation/window/profile fields. Bind
original exact set/incarnations, authentic authority, consumed attempts and current
sole-writer fence. Keep all setup-only refusals unchanged. A separately current
observer reads original operations and actual absence/revocation/preservation;
it has no admission or mutation route. Observation at/after original exclusive
cleanup expiry derives failed, even if absence is now known. Absent observer
authority refuses emission; no claimed authenticated failure is invented.

No new Azure atomic delete precondition, retry, force/cascade, retained target or
API fallback is proposed. Keep genuine original operation and current dependency
checks. Outcome bytes retain the accepted closed setup/run receipt union.

### D5: One implementation handoff after exact paired acceptance

The sole executable list remains openXwallet feature017 T013P07. Its paired
accounting subplan records the failed gate and proposed measurement/decision
sequence. All old runtime/test/matrix/profile/pin/workflow bytes remain unchanged
during this local preparation. No task closes from diagnostic passes.

## Risks / Trade-offs

- Incomplete call inventory: retain raw traces and independent state audit; refuse
  selection of limits until registration, observers and recovery are included.
- A new allowance leaks into runtime proof: use source-selected typed ownership
  and regress every old phase/default refusal; no ambient activation.
- Retry/recovery resets consumption: require retained original charges and action
  attempts; lost state means incomplete/quarantine, not initialization.
- A feasible call count misses latency/body constraints: require complete real-time
  and byte measurements under the same declared policy, not a counter-only pass.
- Deployed support differs from doubles: retain provider/RBAC/service qualification
  and live human/consumer gates; do not label source isolation as deployed proof.

## Migration Plan

No deployed migration is authorized. Finish the complete call inventory and
numeric policy proposal using separately bounded diagnostic work; publish/review
the paired source decision only when concrete. Exact owner source acceptance must
precede dependent code. Later isolated implementation must requalify the full
positive, refusals, previous cases and independent teardown. Failure leaves the
existing operational refusal and consumed original scopes in force.

## Open Questions

1. What exact finite per-scope and per-operation charge limits cover the full
   selected first-pilot graph, including registration/state and independent
   observers? The current smaller graph is only a lower-bound diagnostic.
2. How are durable cumulative call/attempt charges represented and authenticated
   across process reconstruction without adding a receipt field or hidden service
   work? Specify the closed internal policy before coding it.
3. What exact operation timer and original absolute cleanup expiry binding fit the
   full measured positive? No clock duration increase is selected in this draft.

These are blocking source selections, not optional runtime configuration. The
packet is structurally prepared but is not ready for ratification of a replacement
budget or for dependent implementation.
