## Purpose

Define source-only requirements for a versioned preapproved hosting plan that can
be finalized with real run/process facts without predicting values or weakening
full protected runtime admission and one-use wallet proof checks.

## ADDED Requirements

### Requirement: Explicit versioned static plan

The hosted selection SHALL use a new closed v2 profile. It MUST commit the exact
immutable configuration, policy and measurement templates, derivation algorithm,
staging/cleanup policy, hosting selection and current source-hold reference.
Only launch.run_id, launch.run_attempt, composition_digest and
authority.policy_digest SHALL be absent from the full configuration template.
Every other field MUST remain present and preapproved. V1 behavior and the
unselected default MUST remain unchanged; preparation grants no implementation.

#### Scenario: Plan exists before run or process assignment
- **WHEN** a plan is prepared without a run ID, PID or final composition
- **THEN** its digest commits all static template/scope bytes without placeholders, fabricated hashes or worker-selected omissions

#### Scenario: V1 or a static template is silently widened
- **WHEN** a caller adds an unapproved late field, changes static bytes or sends v2 through the v1 route
- **THEN** validation refuses rather than changing v1 semantics or accepting a generic patch

### Requirement: Read-only plan admission before environment approval

Pre-environment admission SHALL authenticate purpose/phase identity and independently
corroborate the consumed dispatch, actual first run, selected plan, hold, protection
and cleanup capability. It SHALL return only plan readiness and the approved existing
environment. It MUST NOT start a worker or issue full runtime/proof/grant readiness.
The exactly three dispatch inputs and seven runtime service roles MUST be preserved.

#### Scenario: Valid unprotected identity and current plan
- **WHEN** independent current facts agree on the approved plan and assigned first run
- **THEN** only plan-bound environment readiness is returned without a full configuration digest or worker launch

#### Scenario: Wrong phase or unavailable observation
- **WHEN** identity is wrong, a required read fails/expires, source moves or the environment is unprotected/missing
- **THEN** admission refuses before output, launch, issuance or custody use

### Requirement: Protected staging under separate narrow authority

Staging SHALL require actual environment approval, current eligible-human review,
protected bootstrap identity, exact source/plan/run/host scope and a separate current
launch authorization. A durable independently acknowledged cleanup registration
MUST precede start. Token possession, plan readiness or approval alone SHALL NOT
issue launch/signing authority. A staged worker MUST have no signing/control capability.

#### Scenario: Protected approval and staging registration are complete
- **WHEN** independent launch scope and cleanup responsibility are acknowledged for the approved run/host/template
- **THEN** only one inert controlled generation may start under the accepted template

#### Scenario: Janitor registration or launch result is ambiguous
- **WHEN** acknowledgement is lost, a start response is lost or the launcher dies before PID persistence
- **THEN** scope remains consumed/indeterminate for exact-generation reconciliation without a second launch or reused reference

### Requirement: Observed generation and independently derived final binding

The complete configuration SHALL be reconstructed from immutable plan bytes plus
only the four enumerated late fields. Run facts MUST be independently corroborated;
composition MUST derive from actual controlled process/artifact observations;
full policy digest MUST derive from the accepted template and measured composition.
A separate current authority MUST compare complete canonical derived bytes before
accepting the full config digest. Worker hashes or a launcher-supplied digest alone
MUST NOT approve finalization. Existing full runtime/proof validators SHALL remain mandatory.

#### Scenario: Actual measured launch finalizes the approved plan
- **WHEN** actual first run and immutable host process/source facts match the approved measurement/policy rules
- **THEN** a single final binding authenticates exact plan/run/host/generation/policy/full configuration with no authority extension

#### Scenario: A final field or measured generation is substituted
- **WHEN** any static byte, run/attempt, PID/start/boot/source, policy byte or unsupported derived field changes
- **THEN** finalization refuses before full readiness or custody use

### Requirement: Gap-free immutable cleanup promotion

Staging cleanup SHALL remain responsible until a distinct immutable full-config-bound
plan/lease for the same generation has durable registration and independent takeover
readback. Promotion MUST NOT delete consumed state, overwrite scope, replace generation
or extend expiry implicitly. Failure or cancellation at every intermediate state
MUST retain a cleanup owner and prevent proof readiness.

#### Scenario: Final plan takeover succeeds
- **WHEN** full plan and independent readback acknowledge the same target/generation with no later deadline
- **THEN** staging ownership can retire while the final plan remains independently actionable

#### Scenario: Failure during promotion or final admission
- **WHEN** registration, readback or full admission fails, expires or is interrupted
- **THEN** the acknowledged prior owner retains cleanup and no machine proof success is reported

### Requirement: Current bounded authority and compatibility

Every decision SHALL enforce current revocation, non-regressing time, the earliest
applicable expiry and bounded authenticated I/O. No retry/reset, stale fallback,
opaque callback label or automatic lease renewal SHALL extend scope. Existing
bootstrap/proof audience and protected-environment checks MUST remain independent.
No neutral contract, consumer lock, domain or human acceptance SHALL follow.

#### Scenario: Expiry occurs during issuance or measurement
- **WHEN** a blocking operation crosses an enclosing or returned deadline
- **THEN** readiness/use refuses, consumed scope remains and cleanup responsibility survives

#### Scenario: Bootstrap identity reaches the proof gate
- **WHEN** a signature-valid bootstrap-purpose token or unprotected proof-audience token is supplied for proof
- **THEN** unchanged protected proof policy refuses before custody with independent known-good controls
