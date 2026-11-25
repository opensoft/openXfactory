# Proposed descriptor and original-controller records

Status: draft; internal factory/adapter contract only.

## Wire ownership

The fixed companion lifecycle profile is
openxfactory-hosted-lifecycle-companion-internal-v2. Ordinary
openxfactory-hosted-lifecycle-internal-v1 is unchanged. A source-selected pair of
companion transports adds registration_manifest only to the existing register
and ack-stage fact objects. Their other original fields, outer scope/nonce/peer
checks, operations and body limits remain. No selector negotiation or new staging RPC. The separate acquisition port below
is explicitly new and separately budgeted.

The descriptor profile is openxfactory-registration-manifest-internal-v1. Its
closed structural schema is registration-manifest.schema.json. Normative semantics
also require existing handle validation, unique refs/instances, canonical bytes,
actual owner derivation and completeness; schema validation is not authentication.
Canonical descriptor bytes must be at most8192, including all one-to-three
credential rows, within existing65536-byte envelopes. Never trim rows to fit.

| Field | Binding |
| --- | --- |
| registration_digest | Digest of the actual original complete registration |
| scope_digest | Exact original scope already authenticated by the channel |
| unit_digest | Actual original registered unit |
| lifecycle_store_binding | Owner-issued commitment to the original LifecycleStore identity and registration/scope; no freshly initialized store |
| resource_epoch | Exact original64hex resource epoch, not a new nonce |
| credentials | Every original RunResource whose kind is credential; existing ref/instance_ref/kind/retention fields, kind=credential and retention=run |
| issued_at / expires_at / cleanup_until | Original registration bounds; no renewal |

The primary and independent acknowledgement each derive the same descriptor from
actual retained owner state. The latter reuses its current host/inventory checks;
no second inventory is added solely for this response. The server origins, principals and server-certificate bindings are distinct.
Both checked descriptor values and registration digests must agree. A supplied list/count is never attested.

## Capture record

The original controller stores a fixed capture purpose plus canonical descriptor
bytes, primary/audit verifier-produced principal and peer-certificate bindings,
request-nonce digests, reply digests and original capture bounds. No bearer token,
private key or raw factor material is retained. No new signer/custody operation is
required. Only a sealed authenticated transport result can enter capture. The canonical
capture record is at most16384 bytes and the claim record at most4096; never
raise the existing outer or original value limits to fit.

Durable authenticity is the existing source-owned private-controller store and
original identity/UID boundary; the record is not independently portable signed
evidence. A public descriptor JSON document cannot recreate the sealed capability.
Readers retain existing high-water clock-accounting semantics and change no
capture, handoff claim or business state.

## Controller schema v2

Use the same original controller database and namespace resource with an explicit
fixed schema version2. Add bounded nullable capture and handoff-claim BLOBs to its
existing per-launch stage row. Leave old v1 controller and host-store classes,
SQL schema, wire and defaults unchanged. V1/v2 source mismatches refuse; no ALTER,
automatic migration, new side database, fallback directory or create-on-open.

Capture becomes immutable in the existing transition to start-consumed before
possible host start. Materialization validates the original running/stopped state
appropriate to its separately authorized purpose, original unit/generation/scope,
lease, descriptor commitment and original controller/store identity. Missing or
inconsistent state refuses. Only the controller service must have that original local store capability. The
runner caller receives authenticated facts through the explicit acquisition below,
never database access or a replacement identity.

## Handoff slot

Under the original launch_ref row, a null slot can atomically become consumed once.
Its bounded record binds descriptor/claim commitments, approved plan/source and
run/attempt scope, original controller identity, claim time and original deadline.
Return a sealed local attempt only after known commit. No finalization NonceStore
is initialized. A claim is accounting/consumption state, not independent approval.

There is no reset, refund, takeover, replay grant or cross-process capability
reconstruction. Concurrent callers cannot both receive a capability. Failed or
unconfirmed reservation yields none and source does not retry; pre-commit failure
performs no authority I/O. Consumed or lost claims remain consumed. Original-scope
resolution and cleanup remain separately authorized and preserve actual state.

The initial source packet does not declare runtime success: tests must exercise
actual original-store reopen, source ownership, mTLS exchanges, copies/tampering,
crash boundaries, one-send outcomes and whole unchanged admission/qualification.

## Closed retained-record grammar

All objects reject extra/missing/duplicate fields and noncanonical bytes. The new
record grammar is defined here for future source implementation; none is written
by this proposal. Existing reference/handle, integer, digest and source validators
remain normative. A schema or dictionary alone cannot create a sealed capture.

The closed capture fields are profile, descriptor, controller_store_binding,
primary, audit and captured_at. Profile is
openxfactory-controller-registration-capture-internal-v1. Descriptor is the complete
inline descriptor above, without trimming. Each closed primary/audit object has
operation, principal_ref, origin, server_certificate_digest, request_nonce_digest
and reply_digest. Operations are register and ack-stage respectively. Origins,
principals and verified server-certificate pins must equal the original trusted
source bindings and be distinct between the two services. The private HTTPS
helper already enforces the selected pin during the actual exchange; record that
verified binding only after successful intrinsic transport and reply checks, not
an unverified claim that a peer supplied a certificate. No extra TLS connection during staging capture,
credential read or independent inventory is introduced solely for capture.

Nonce digests commit to each actual original request nonce; reply digests commit
to complete authenticated canonical response bytes, including descriptor and
scope/time/nonce checks. Captured_at uses the original Decision clock after both
replies, within their clipped bounds and original registration expiry. The fixed
capture purpose cannot be reused as a plan, receipt, lease or authority grant.

Lifecycle_store_binding is the canonical digest of a closed object with profile
openxfactory-lifecycle-store-binding-internal-v1, kind=primary, identity (the complete
original LifecycleStore expected identity including its witness, journal lock and
file-pins identities), registration_digest and scope_digest. Obtain that identity
from the existing original owner capability, never a fresh path stat. The audit
reply corroborates that same primary owner binding through its existing original
HostedLifecycle; it does not substitute the different audit backend identity.
Controller_store_binding similarly commits to profile
openxfactory-controller-store-binding-internal-v1, kind=controller, version=2,
the complete original expected StageStore identity, launch_ref and scope_digest.
Only commitments cross the wire; raw local paths/identities do not become inputs.
Both stores retain their existing current-identity/witness checks independently.

The closed consumed-claim fields are profile, launch_ref, scope_digest,
descriptor_digest, capture_digest, controller_store_binding, approved_plan_digest, accepted_commit,
source_commit, run_id, run_attempt, claimed_at and deadline. Profile is
openxfactory-original-handoff-claim-internal-v1. Descriptor_digest commits to the
exact retained canonical descriptor; capture_digest commits to the immutable
canonical capture containing it. Source/plan/run/attempt values come from the
original validated scope/plan, not a replacement argument. Claim time uses the
original clock; deadline is no later than every applicable original registration,
lease, controller bound and the original qualifying caller request deadline. Missing/expired original authority refuses;
a new Decision cannot extend it. The record has no new nonce or approval field.
The original launch row is the one durable slot; hashing its exact record supplies
a commitment, not another attempt identity. Capture/claim byte limits are16384/4096.

## Explicit runner acquisition and claim contract

Route A is superseded: the preserved workflow runs an exact local Qualifier on
the GitHub runner. The existing /v2/plan and /v2/protected StageAdmission APIs
cannot invoke or return that proof. Do not move proof to the controller or grant
the runner local store access. Route B adds the following explicit internal port
on the existing trusted controller service, with a separately fixed companion
constructor and no activation through request profile/env/file/CLI selectors.

Method/path: POST /v2/registration/claim. Request canonical body<=16384 bytes,
response canonical body<=16384, within the existing65536 transport envelope.
Closed request fields: profile, nonce, deadline, arguments. Profile is
openxfactory-original-registration-claim-internal-v1; nonce is64 lowercase hex;
deadline is the original qualifying Decision's clipped integer deadline.
Closed arguments: launch_ref, scope_digest, approved_plan_digest, accepted_commit,
source_commit, run_id, run_attempt. Use existing handle, SHA, numeric-string and
digest validators; every value must equal the actual original retained scope/plan.
These values locate/bind facts and are not credentials or approval assertions.

Server requires pinned mTLS, its preselected trusted qualifier/staging-observation
principal and exact original scope authorization. This source proposal adds that
narrow operation permission, not an assertion that current deployed credentials
already have it. No worker authorization or new runtime grammar role is added.
The server uses only its already selected original controller store and capture;
no remote lookup, signing, provider or credential inventory runs in this handler.
Local current identity, high-water clock, schema, scope/unit/generation/lease and
applicable expiry checks remain. Missing/wrong/expired/ambiguous state refuses.
The server clips its one request Decision to caller deadline and all original
registration/lease/controller bounds, with no new valid interval.

Only after a known atomic null-to-consumed claim commit may the closed success
reply be emitted. Fields: profile, nonce, scope_digest, launch_ref, principal_ref,
observed_at, expires_at, facts. Profile is the same fixed claim profile; nonce and
scope/launch match the actual request, principal equals the selected server,
observed_at is fresh original clock time and observed_at<=now<expires_at<=every
applicable request/original bound. Closed facts: descriptor, controller_store_binding,
capture_digest, claim_digest. Both digests commit to exact retained canonical
capture/claim records. The descriptor is the exact complete8192-byte owner-derived
original. Raw local store paths/identities, factor material, credentials, generation
approvals and proof/report values are never returned.

The client checks actual transport pin/principal/origin, complete reply/nonce/
source scope/time/descriptor semantics and original selected server binding before
materializing its sealed view/attempt. A JSON document or digest alone supplies no
capability. The slot receipt is identity/accounting, not independent approval.
No retry follows any failure, timeout, cancellation, lost/ambiguous response or
consumed claim. At most one claimant receives a capability; response loss cannot
reissue one. Existing separately authorized original-scope resolution and cleanup
remain and never reset the slot or resend its mutation. Fixed refusals disclose
no credential/factor state; ordinary phase and lifecycle v1 responses stay exact.

The staged capture's reply freshness is historical provenance, not a later grant.
The fresh qualifying request has its own one original10-second Decision; keep it
unchanged through acquisition and handoff and clip it to retained original bounds.
The acquisition is one newly budgeted RPC with no nested network/credential call.
Its source-fixed compound policy and physical qualification obligations are in
acquisition-policy.json and design.md. It must not be hidden in the prior totals.

## Fixed companion transport ownership

The ordinary PrivateHttps admission/lifecycle allowlists and credential helper
policies do not currently allow /v2/registration/claim. Future source code must
provide a separate exact RegistrationTransport owner for that one method/path,
using the existing bounded private HTTPS helper's separately fixed claim mode.
Amend only that internal helper's literal mode table; preserve every ordinary
constructor/default/allowlist and reject cross-mode traffic. No generic arbitrary
path, environment choice or public CLI flag can activate it. Existing original
certificate/CA/key drift and TLS-to-send, no-proxy, no-redirect, child-reaping,
body/time and error-sanitization checks remain mandatory. This is source work in
the declared P08 footprint, not an assertion that the existing transport already
supports the endpoint. The companion server similarly has a distinct fixed owner;
ordinary StageAdmission method/path/response behavior remains unchanged.
