## Purpose

Carry authenticated original lifecycle registration facts into the first-pilot
companion while conserving its original retained state and handoff attempt.

## ADDED Requirements

### Requirement: Only original owner facts establish the descriptor

The companion SHALL capture the complete original credential-resource projection
from the authenticated primary registration and independent stage acknowledgement.
The descriptor MUST bind registration, scope, unit, resource epoch and original
lifecycle-store identity. It MUST contain every original credential row and no
caller-supplied count. Existing owning-resource equality checks MUST remain.

#### Scenario: Genuine original exchanges agree
- **WHEN** both original owner replies authenticate and agree on the descriptor
- **THEN** the source-owned capture can retain those facts under the original controller scope

#### Scenario: One reply, resource row or owner binding differs
- **WHEN** provenance is absent or registration, scope, unit, store, epoch or credential rows differ
- **THEN** capture refuses before host-start or dependent handoff and existing original-scope cleanup remains separate

### Requirement: Closed companion wire preserves ordinary behavior

The new internal descriptor wire SHALL be source-selected and closed. Ordinary
v1 traffic and companion traffic MUST NOT negotiate or activate each other.
Existing request operations and physical RPCs MUST remain; no new lookup is
introduced. No environment, file, profile field, callback string or manual input
may choose a source constructor or ceiling.

#### Scenario: Old and companion source paths are crossed
- **WHEN** a v1 peer is given companion facts or a companion peer receives v1 facts
- **THEN** it refuses without activating another route or weakening either closed grammar

### Requirement: Original controller retention preserves provenance

Capture SHALL live in a source-selected v2 grammar of the existing original private
controller store, bound to its original identity, UID, scope, unit, lease and clock
high-water. Only authenticated owner-module capture may populate it. Readers MUST
NOT initialize, copy, migrate, repair, restore or recompute a replacement store.

#### Scenario: A later phase uses the same original store
- **WHEN** its trusted bindings reopen the existing store at the original identity and scope
- **THEN** it can materialize the same captured owner facts without another network lookup or new authority

#### Scenario: Store or capture continuity is missing
- **WHEN** the directory, database, kind, schema, scope, capture or original identity is absent or changed
- **THEN** materialization refuses without creating or accepting a replacement backend

### Requirement: Caller materialization precedes selected handoff I/O

Trusted source SHALL materialize a sealed original-registration view locally before
per-manifest selection or dependent handoff I/O. N MUST be derived from all original
credential rows and remain bound before/after blocking work. A future final plan,
fixture-private owner pointer, serialized caller assertion or extra unbudgeted read
MUST NOT substitute. A remote-only controller lacking original local access is ineligible.

#### Scenario: Original view is unavailable at construction
- **WHEN** the caller cannot demonstrate access to the genuine retained capture
- **THEN** eligibility refuses before selected accounting or handoff RPCs and returns to governance

### Requirement: One original handoff claim is consumed before authority I/O

The existing controller row SHALL durably reserve one consumed handoff claim under
its original launch reference before returning an attempt capability or sending
subsequent authority I/O. The claim MUST bind the descriptor, approved source/plan,
run/attempt scope, original store and clipped deadline. It confers no approval.
No new nonce backend, replacement attempt or copied approval may provide it.

#### Scenario: Original claims race
- **WHEN** two callers try to reserve the same original handoff slot
- **THEN** at most one receives a capability and the other performs no dependent authority I/O

#### Scenario: Claim or response is lost or ambiguous
- **WHEN** a claim is consumed, its capability is lost or a reservation is unconfirmed
- **THEN** no replacement approval or mutating retry is created and only existing separately authorized resolution/cleanup may proceed

### Requirement: Existing identity and authority gates remain independent

A descriptor or claim SHALL NOT replace current actual-run authority, independent
complete-byte acceptance, generation binding, exact existing full admission or
original lifecycle prepare/acknowledge/release checks. Cleanup and audit MUST retain
their original disjoint authorization, deadlines and no-resend behavior.

#### Scenario: Valid manifest exists without current authority
- **WHEN** the view is valid but current authority or the full owning-proof route is unavailable
- **THEN** proof/effect refuses and the manifest grants no permission or renewed interval

### Requirement: Bounds and qualification remain explicit

The accepted remote-lifecycle accounting commitment and all ordinary budgets,
body caps, source/role/input counts, managed resources and default operational
refusal SHALL remain unchanged. The descriptor MUST fit its8192-byte canonical
bound within existing65536-byte envelopes. Actual full transport, local retention,
clock, refusal/crash, old/new identity and cleanup evidence MUST precede qualification.

#### Scenario: The connected route does not fit
- **WHEN** genuine complete work needs another RPC, resource, authority, body size, deadline or pool
- **THEN** implementation stops for governance without raising a cap or omitting a check

### Requirement: Source acceptance does not confer operational authority

Exact paired source ratification SHALL precede the new wire/record implementation.
The existing adapter T013P08 task remains owner and incomplete until qualified.
P09, live/human/consumer acceptance, setup and protected dispatch remain separate.

#### Scenario: Only this source proposal is present
- **WHEN** artifacts or local source checks pass without owner acceptance and later operational grants
- **THEN** no new wire is implemented or activated and no live qualification is claimed
