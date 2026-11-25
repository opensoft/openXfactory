# Original registration handoff design

Status: draft route-A source design; source acceptance and implementation pending.
Date: 2026-11-25.

## Context

See proposal.md for the measured missing port. The lifecycle owner already retains
registration.resources, its resource epoch and original store binding. The original
controller already owns a private StageStore with per-launch scope, unit, generation,
lease, clock high-water and consume-before-start state. The caller currently receives
neither the original credential projection nor a capability to that retained state.
A fixture's private life/store pointer is not a production caller port.

## Goals / Non-Goals

**Goals:** give the first-pilot companion a genuine original descriptor before
per-manifest accounting; retain authenticated provenance across its real phase/
process boundary; consume one original handoff claim; preserve existing RPCs,
authority checks and ordinary APIs.

**Non-Goals:** no new backend/file/resource, generic manifest lookup, extra service/
role/input, approval signer, neutral profile, cap increase, deployed binding or
operational grant. This source packet supplies no live registration or credential.

## Decisions

### D1. Carry facts on the existing owner exchanges

Use a distinct, source-fixed companion lifecycle profile:
`openxfactory-hosted-lifecycle-companion-internal-v2`. Its register and ack-stage
facts carry the descriptor defined in supporting-docs/contract.md. All existing
operations, request argument sets, mTLS permissions and outer body bounds remain
constraints; add no manifest operation or lookup. Ordinary v1 server/client/fact
parsers remain unchanged and reject companion traffic. Constructor selection is
trusted source; request/profile text cannot select a constructor or negotiate it.

The primary derives the complete credential projection from the registration it
actually committed. The independent stage acknowledgement observes that same
original registration and its existing resource/host checks. Reuse those existing
observations; do not add another inventory, credential exchange or authority pass.
Their server origins, principals and certificate bindings must be distinct; caller
client-certificate reuse remains governed by the existing selected permissions.
Both validated replies must agree on descriptor bytes, registration/scope/unit,
resource epoch and lifecycle-store binding. This changes a closed internal wire
contract and therefore needs exact source ratification before dependent code.

### D2. Retain provenance in the original controller store

Introduce a fixed companion controller-store schema v2 in the existing controller
backend. Keep the existing host store and ordinary controller schema v1 unchanged.
The v2 stage row adds a bounded capture record and a handoff-claim record. Capture
is committed with the existing original transition to start-consumed, after both
owner replies and the original lease checks, before the first possible host-start
send. Keep existing stage states/edges and consume-before-send behavior.

The capture is at most16384 canonical bytes and the handoff claim at most4096.
The capture contains descriptor bytes and verifier-produced primary/audit peer,
certificate, request-nonce-digest and reply-digest provenance. Only the owning
transport capture can create its sealed input. A generic dict, file or caller
assertion cannot populate it. This is authentication retained by the existing
private controller ownership/identity boundary, not a portable signed receipt.
No new signing key, factor operation or shared-worker authority is introduced.

Use the original directory/database identity, private UID/modes, exact kind/schema,
launch/scope, unit and original high-water clock. Never discover a replacement
identity by restatting an arbitrary supplied path. Readers open only that existing
store; no create-on-open, migration, copying, repair or restore. Original staging
setup alone may initialize a fresh selected v2 controller store within its already
selected namespace. Live setup remains unauthorized. Ordinary v1 stores are not
upgraded in place. Worker access to the controller's private store remains excluded;
privileged controller/host writers retain the existing POSIX trust boundary.

### D3. Materialize locally at the trusted caller

The companion's trusted caller/controller must retain access to the same original
controller store and original identity across phase/process boundaries. Its fixed
source bindings materialize an owner-module OriginalRegistration view from the
captured row before any selected handoff I/O or per-N policy selection. The view
binds that controller-store identity as well as the owner's lifecycle-store binding.
N is the length of every original credential row; no separate count is accepted.

This is an explicit composition constraint. A topology with a remote-only controller
and no original local retained-store capability is ineligible. Do not replace the
view with an extra network fetch, copied SQLite file, new local ledger, environment
switch or caller-supplied reference. That would need a separate governed design.
Concrete operator locations/identities remain T013 decisions, not new inputs.

### D4. Consume the original handoff slot durably

Within the original v2 stage row, atomically move a null handoff slot to consumed,
keyed by its original launch_ref. Bind the claim to the exact descriptor commitment,
source/run/attempt scope, approved plan, original controller identity and original
clipped deadline. Return a sealed in-process attempt only after a known committed
claim; no authority I/O occurs before that point. This adds a record grammar in an
existing backend, not a separate finalization NonceStore or fresh attempt ID.

Concurrent claims yield at most one capability. A consumed, lost or ambiguous
original attempt cannot mint a replacement capability or approval; only separately
authorized original-scope resolution/cleanup remains. An unconfirmed reservation
returns no capability and the fixed source workflow does not retry it. A pre-commit
crash supplies no approval or authority I/O; record the actual durable outcome.
A source-private one-shot object is not itself advertised as cross-process state.
The claim never substitutes for the independent actual-run authority, original
FinalizationBinding/FinalizedPlan checks, or original owner prepare/ack/release.

### D5. Keep observation and authority distinct

A registration view supplies identity and accounting facts only. Handoff requires
the claimed original attempt and all existing current authority checks. Cleanup
and audit require their separately authorized original scopes and remain disjoint;
a view does not renew them or resend mutation. View reads change no capture, claim
or business state; retain existing time-accounting/high-water transaction semantics.
The final RunPlan must still equal resources_for(original state). It cannot be the
source of the earlier manifest or a replacement for its provenance.

### D6. Preserve the accepted physical policy

The commitment fd198b7d7e8e786b5d5f64257ec0e276e881ea5364b265cb9ccb519208f77fa7
is unchanged: handoff12+2N (max18), original cleanup plus audit2+5N (max17),
separate authorized audit-only1+N (max4), with1<=N<=3. No new private RPC,
credential read, observation, authority pass or pool is budgeted by this design.
Record local capture/materialization/claim transactions separately with their
original store timeouts and clocks; they are not free authority or a new window.

The future implementation must measure the complete actual transport graph and
whole owning-proof route, including callbacks and retention work. The no-new-RPC
intent does not prove a bound. Any extra I/O, deadline/body mismatch or qualification39
failure returns to governance; do not alter totals or delete checks to pass.

## Risks / Trade-offs

- Cross-phase store access is required: make original caller/controller placement
  and identity an eligibility gate; remote-only deployments do not silently fall back.
- Capture could be confused with approval: distinct sealed types and purpose checks;
  original live authority, full admission and human/consumer gates remain separate.
- Storage integrity could be mistaken for portable attestation: retain actual
  transport provenance only under the existing original controller trust boundary.
- Capture/claim commit or response can be lost: consume-before-send, original-state
  inspection and no retry/reconstruction; exercise each real crash boundary.
- Schema/transport coexistence can drift: fixed v1/v2 constructors, exact closed
  grammars, explicit mismatch refusals and preserved prior test identities.

## Migration Plan

Source proposal and paired feature017 plan first; exact owner source ratification
precedes the new wire/record code. Implement only in isolated original fixtures,
repeat both eligibility gates, whole connected proof/full/native qualification and
independent cleanup. Do not migrate a live v1 store or select endpoints/roles here.
Operator setup, dispatch and live acceptance retain their existing later gates.
