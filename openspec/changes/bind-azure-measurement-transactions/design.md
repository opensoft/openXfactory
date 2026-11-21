# Direct measurement transaction binding

Status: draft; source decision unratified, dependent implementation pending.

## Context

See [proposal](proposal.md). Existing P3 source owns a direct v1 measurement body,
real local measurement and unchanged budgets. Actual eligibility probes establish
one fitting complete-body/local-derivation positive but cannot obtain explicit
request binding from the old current-observation wrapper or discarded HTTP headers.
The proposal preserves those accepted sources and introduces an additive profile.

## Goals / Non-Goals

Supply one reviewed source grammar that a dedicated P05 operation can implement
using the existing bounded mTLS transport. Keep actual local manager/namespace,
independent observations, complete-byte control derivation and old phase accounting.
This is no new neutral protocol, source role, dispatch input, operational builder,
credential enrollment, live target or consumer acceptance. P06-P09 remain separate.

## Decisions

### D1: A separate direct v2 body carries its request binding

The [closed grammar](supporting-docs/measurement-transactions.md) is authoritative
for this candidate. v2 retains the complete v1 fields and adds one request_nonce.
The direct complete UTF8 response remains at most 16,384 bytes. No fallback accepts
v1 where the v2 transaction capability is required. v1 remains immutable for its
existing source scope; no predecessor operation, wrapper or invocation field is
repurposed. A response-header alternative would need a new verified transport
contract because the existing helper intentionally returns no headers. The direct
v2 field permits reuse of unchanged PrivateHttps without that broader change.

### D2: Nonce equality binds a transaction, not a self-reported fact

The control capability selects a fresh nonce before the authenticated request.
The service authenticates the actual selected peer/role/source/incarnation and
full effective scope; request identity strings cannot appoint it. An existing
independently initialized protected nonce ledger consumes the attempt before
local reads. Failure/cancellation cannot reset it. The service performs actual
current local observations per request, rather than copying a stored result or
merely rewriting its nonce. The client accepts only exact fresh nonce and selected
peer/scope/generation/expiry matches after the actual bounded TLS exchange.

No server can establish observer independence by returning two labels. Control
selects two independently authenticated observers before the request, each with
independent credential/approval provenance and actual local observations. Complete
configuration/policy and current generation must agree, while the control authority
separately derives all expected bytes from approved roots/templates. Provider/
admin facts remain explicit isolated doubles until separately qualified deployment.

### D3: Keep the original caller's authority and local ownership

Charge each authenticated observer exchange once to the original private budget
before use; retain existing current-source/protection/state reads and count every
nested network read against that same operation. Server processing is local
kernel/file/nonce-state work only. The server clips an independent local timer
to original absolute deadline and caller remaining milliseconds; it cannot allocate
proof/admission authority, reset a ledger, join clocks across hosts or renew expiry.
Real ProcessLaunch, MeasurementBindings and manager/lifecycle checks remain on the
worker kernel. A remote PID/JSON is never a control-host local capability.

### D4: One existing implementation handoff

openXwallet feature017 T013P05 owns the later dedicated client/local adapters and
substantive tests. Keep that row unchecked until full isolated qualification and
cleanup pass. The paired source decision must precede dependent v2 code. Actual
enrollment/issuance, retirement, activation, full P3 qualification, operational
selections/setup/dispatch and consumer/human acceptance retain their separate gates.

## Risks / Trade-offs

- A trusted service could return stale facts with a fresh nonce: require per-request
  real local remeasurement, independently selected observers and late current-scope
  checks. Nonce echo is not evidence of those checks.
- Additional metadata or two remote observers could exceed body/time/read bounds:
  measure the actual complete positive; refuse and seek governance if it cannot fit.
- Same-host privileged administrators can subvert observers: retain the accepted
  trusted-admin boundary and qualify effective worker exclusion independently.
- Retained nonce state unavailable or rolled back: refuse; no runtime initialization,
  reset, retry or restored-backup guarantee is introduced.

## Migration Plan

There is no deployed migration. After exact paired source acceptance, implement
only the existing isolated P05 row with a dedicated source-selected v2 client.
Keep old paths/default refusal and all predecessor positives intact. Publish and
review source through their normal gates; rollback leaves the selected v2 path
unavailable and retained attempts consumed. No workflow or operational activation
occurs through this candidate.
