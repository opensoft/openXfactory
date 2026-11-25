# Original registration acquisition design v2

Status: proposed route B; source acceptance and dependent implementation pending.
Date:2026-11-25. The earlier route-A draft is superseded after local architecture review.

## Goals and boundaries

Supply the runner caller's authentic original descriptor before per-N handoff;
conserve one original durable attempt across real runner/controller boundaries.
Keep the existing runner-local exact Qualifier, full admission, phase responses,
report, old lifecycle/store grammars,14 resources,3 inputs and7/8 role/source counts.
No setup, dispatch, actual principal/credential grant or live acceptance is selected.

## Decisions

### D1. Original owner capture stays on existing staging calls

Source-fixed openxfactory-hosted-lifecycle-companion-internal-v2 adds the descriptor
only to register/ack-stage facts. Primary derives it from its actual committed
registration; the independent acknowledgement reuses its existing host/resource
checks, with no added inventory/credential operation. Distinct original origins,
principals and verified server pins must agree on complete descriptor bytes.
Use existing mTLS and outer checks/body caps, no negotiation or data selector.
The descriptor supplies facts, never proof authority or a new lease interval.

### D2. Retain inside the original controller trust boundary

A separate fixed controller-store schema v2 adds immutable capture and nullable
handoff-claim BLOBs to the existing original per-launch row/database. Original host
store and ordinary controller v1 remain exact. Capture commits in the existing
start-consumed transition, after both checked replies/lease/refresh and before
host start. Retain original expected identity, UID/private modes, kind/schema,
scope/unit/generation, high-water clock, one-second SQLite transaction bound and
256-row cap. No copying/migration/repair/restore/create-on-open or side database.
Only original staging setup can initialize the fresh selected v2 fixture/store.
Live setup remains held. Privileged controller/host writers remain trusted.

### D3. Preserve runner placement with an explicit claim exchange

The existing runner qualify process calls one new fixed controller endpoint,
POST /v2/registration/claim, under a separately source-selected companion server/
client. It is not added to ordinary v1 or current StageAdmission routes/responses.
The server opens its own original store at its original expected identity and
validates the original capture/scope/unit/generation/lease. It consumes one same-row
claim before replying with the exact original descriptor and binding commitment.
The runner gets no database access and reconstructs no local store identity.

The endpoint requires the preselected trusted qualifier/staging-observation
principal over pinned mTLS, exact source/run/attempt/scope and closed request nonce/
deadline. The original server scope/certificate authorization is authoritative;
request fields alone confer no permission. This is a new narrow source permission
for existing-principal metadata/slot use, not a new runtime grammar role. Actual
credential/principal compatibility is unqualified and later gated. Worker, missing/
wrong principal, unregistered or non-running/mismatched original state refuse.
No provider REST, authority query, signing, token mint or credential inventory runs
inside this acquisition; local identity/SQLite/time accounting still counts.

### D4. Retain provenance and conserve the consumed attempt

The runner's sealed OriginalRegistration/OriginalHandoff are created only by the
owner-module client after the actual pinned-mTLS exchange and complete nonce,
scope/source/time/descriptor/claim checks. Generic JSON/files/counts cannot create
them. The server's private original store retains staging transport provenance;
the fresh claim reply authenticates that retained fact binding to the runner.
Neither is a portable signed approval. No new signer or factor key is introduced.

One original launch_ref slot atomically changes null to consumed, binding exact
capture/descriptor, scope/source/run/attempt/plan, original controller identity and
original registration/lease/controller limits plus the caller request deadline.
Return a capability only after known commit. Concurrent claimants yield at most
one. Lost request/reply, unconfirmed commit, consumed or lost capability never
allows claim replay, reconstruction or another approval. Separate original-scope
resolution/cleanup remains authorized independently and does not resend mutation.
A pre-commit failure grants no authority or handoff I/O. Record durable outcomes.

Staging reply freshness is checked at capture and is historical provenance.
The later qualifying attempt uses its own one original10-second Decision and
fresh request nonce; it cannot renew original registration/lease/controller bounds.
The old staging Decision is neither reconstructed nor promoted into later authority.

### D5. Explicit compound accounting; no hidden bridge

The trusted source constructor selects the new compound policy before its first
I/O. Its first subphase permits exactly one acquisition RPC and no handoff/other
network work. After authenticated N1..3, the same original ledger enters its fixed
handoff subphase12+2N, retaining the acquisition debit in cumulative13+2N (max19).
This is a newly governed compound policy, not an upgrade of an ordinary/private12
or existing finalization ledger. Never reset, refund, borrow, transfer, retry or
replace clocks/counters/members. Prepay the acquisition before transport, including
failed sends; every later RPC retains original fixed nested prepayment.

supporting-docs/acquisition-policy.json records the proposed source arithmetic,
not a new physical measurement. Parent policyfd198b7d7e8e786b5d5f64257ec0e276e881ea5364b265cb9ccb519208f77fa7
stays byte-identical. Cleanup2+5N max17, audit-only1+N max4, staging16,
qualification39, ordinary private12, GitHub28/protection18,2 members/3 passes/
6 protection observations, outer caps and all original clocks remain hard bounds.
Measure the entire actual owning-proof graph and local capture/claim work after
source acceptance. If another RPC, nested lookup, role, resource or qualification39
mismatch appears, stop for governance. Arithmetic is not runtime qualification.

### D6. Keep full proof authority independent

OriginalRegistration yields identity/accounting facts and an original consumed
slot only. Existing VerifiedRemote, independent actual-run authority, exact
FinalizationBinding/FinalizedPlan, resource equality, prepare/ack/release, unchanged
full admission, RuntimeBridge and runner-local Qualifier remain mandatory.
The new endpoint never returns a passed proof/report or manufacturing approval.
Existing static/full/report/StageAdmission grammars and default refusal stay closed.

## Migration and validation

Source proposal/paired plan/actual ledger/CI/local Codex review and exact owner
ratification precede new wire/store/endpoint/accounting implementation. All later
code is isolated first. Prove original capture, real separate runner/controller
phases, endpoint authorization/old-new crossover, atomic claims/loss, N1..3 full
physical accounting, both eligibility gates, unchanged full proof, original test
identities/full/native qualification and independent cleanup. Operator roles,
credentials, setup/dispatch and live/human/consumer acceptance remain later gates.
