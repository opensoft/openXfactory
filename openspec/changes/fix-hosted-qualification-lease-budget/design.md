# Bounded qualification lease-read source amendment

Status: draft
Kind: design
Scope: proposed source decision; allocation unimplemented and unratified

## Context

See [proposal](proposal.md). Factory #1332 and adapter #76 are source accepted and
landed; only isolated T012T is commissioned. Its actual hosted positive refuses
inside the unchanged private-read ledger before returning the owning proof.
The accepted report design D3 explicitly requires this separate amendment.

## Goals / Non-Goals

**Goals:** preserve every live per-use lease check, the earliest authority expiry,
exact run/generation binding and independent cleanup while bounding the currently
measured qualification composition. Make late upgrades and scope reuse impossible
through normal source entrypoints.

**Non-Goals:** live authority, a new service/role, generalized budget relaxation,
new report fields, a new proof/MFA contract, callback-selected limits, omission or
caching of lease checks, retrying mutations, operational provider/key/host selection,
or assuming the measured component proves actual hosted timing feasibility.

## Decisions

### D1 — Keep the original fail-closed result until source acceptance

The candidate's real hosted regression runs plan approval, actual worker launch,
measured finalization and immutable lifecycle takeover, actual supervisor observation
and full admission. It reaches twelve consumed private reads and refuses the next
lease request in ReadBudget.consume. Its independent cleanup still verifies and
retained/shared resources survive. This is a failed hosted positive, not a passing
qualification. Do not skip, deselect or relabel that unavailable positive as accepted.

### D2 — A fixed qualification-only private39 allocation

The existing accepted IPC lifecycle component exercises the same RuntimeBridge and
RunLifecycle call graph with real owning TLS registry/custody and every lease check.
It measures34 lease observations and4 private worker-probe calls. It is a component
transport, never an operational fallback or substitute for the hosted positive.

| Current bounded path | Lease observations |
| --- | ---: |
| Lifecycle construction | 1 |
| One run entry | 1 |
| Full admission checkpoint | 1 |
| One actual proof, including before/after checks | 20 |
| Exact original-input replay refusal | 8 |
| Valid-signed audience/environment negative gate entries | 2 |
| Closing lifecycle check | 1 |
| Total | 34 |

Worker availability/denial contributes4 further private calls: worker registry
resolve, allowed gate signature, and explicit worker refusal of the same valid
preimage, followed by a valid signature over that same preimage using the same
loaded worker credential at a separately selected disposable excess-policy control.
The control is exercised in the same qualification run; a separate pytest mutation
or a generic service outage never substitutes for it. If the selected service cannot
provide attributable denial plus this control, the evidence remains unperformed.
No production policy is widened. The gate remains sign-only; no resolve permission is added. One optional
existing operator-origin lookup contributes1. The proposed maximum is39 private
observations. All capacity is bounded; no configurable limit or unused budget is
transferable to another run, phase or action.

This measured component count and static call accounting are lower-level evidence.
They do not prove the accepted hosted client can complete under39 and the unchanged
real10-second Decision window. Source realization must test that actual positive;
if it still cannot fit, stop for another governed decision, not an adjustment in a
fixture, local environment, CI invocation or source default.

### D3 — Trusted entry before any read, one original Decision

Future source realization adds a trusted qualification entry adjacent to the existing
staging/finalization entries. It must refuse an existing hosted-read ledger, any
consumed correlation/API count, a prior or different phase mode, or a repeated entry.
Select it before constructing FinalLifecyclePorts/RunLifecycle and their first read.

Qualification, its full admission, proof, replay, negative controls and operator
lookup share that identical original operation Decision. No fresh parallel budget,
late upgrade, join, copied/reconstructed ledger or reset is allowed. A callback or
worker/body/dispatch value cannot select or enlarge the allocation. Qualification
member count is one; existing independent finalization semantics stay unchanged.

Preserve the original wall/monotonic10-second window, each reader's current checks,
earliest clipped expiry, ordinary GitHub protection3/total13, all other per-reader
and non-GitHub caps, seven service roles, eight source roles and three dispatch inputs.
Do not extend the underlying grant, lifecycle lease, journal capacity or cleanup time.
The extra capacity applies only to this trusted qualification's private group.

### D4 — Every other allocation and cleanup remains unchanged

Ordinary/private12, protected-staging/private16 with its existing26 GitHub total,
finalization/private12 with six observations/protection18/GitHub28, and independent
cleanup/private12 remain exactly as accepted. Mutation failure still consumes its
original attempt; missing actual/audit facts remain unverified. Independent cleanup
uses its original registered cleanup_until/timeout and exact plan/scope/generation.
Report assembly remains pure and cannot allocate reads, retry cleanup or upgrade a
failed/cancelled operation. Fixture execution remains fixture scoped.

### D5 — Source gates precede any application or operational use

The sole implementation tasks remain adapter feature017 T012T02-T012T06. Obtain
explicit owner source acceptance of this new allocation before applying it. Then
implement the bounded ledger entry, preserve every original anchor/node/fingerprint,
qualify actual hosted success and refusal at the new boundary, independent clock/
expiry/exhaustion mutations, exact replay, claim/worker negatives and all cleanup
outcomes. Run ordered/full/native gates and external fixture audits on frozen inputs.
No proposed count of future tests is a committed matrix expectation.

## Risks / Trade-offs

- A larger private allowance could conceal duplicate work -> fixed39 plus measured
  per-operation accounting; no caching/omission of required checks and no configurable cap.
- Late mode selection could revive consumed authority -> reject before any prior ledger
  or API/correlation use; use one unchanged Decision with no joining or extension.
- Legacy component timing could be mistaken for hosted feasibility -> require actual
  hosted positive after source acceptance; preserve current blocking guard and evidence.
- Actual T013 connectors need more observations -> leave that integration unqualified
  and return for governance rather than silently changing this allocation.

## Migration Plan

Review and source-ratify this separate packet. Apply only through the existing
isolated T012T commission after owner acceptance, preserving all unchanged defaults
and predecessor packet bytes. No deployment or rollback procedure is commissioned;
the unselected operational resolver remains refusing. T012U/V, T001/T013-T015,
provider setup, protected dispatch, live reports and human/domain/consumer gates
remain separate. Feedback deferred; neither historical blocked write replayed.
