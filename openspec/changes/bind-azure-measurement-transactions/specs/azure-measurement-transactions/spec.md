## Purpose

Bind complete authenticated local measurement bytes to one selected fresh transaction while preserving actual worker-host provenance, independent derivation and the original runtime authority limits.

## ADDED Requirements

### Requirement: Direct measurement responses bind a selected fresh request

The composition SHALL use the closed direct v2 request and response grammar in supporting-docs/measurement-transactions.md. Every response MUST carry the exact fresh request_nonce selected for that authenticated operation, retain complete canonical configuration/policy bytes and fit the unchanged 16,384-byte total response cap. Missing or changed correlation MUST refuse before private verified provenance is constructed.

#### Scenario: Current complete bytes arrive for the selected transaction
- **WHEN** the independently selected peer returns the complete canonical v2 body for the exact fresh request and selected scope within original bounds
- **THEN** the dedicated operation can continue to independent complete-byte verification without treating the response as a local control-host process

#### Scenario: Another response or correlation value is substituted
- **WHEN** a copied response has another nonce, a nonce is missing/malformed, a header alone claims correlation, or a wrapper/extra field changes the body
- **THEN** acceptance refuses without changing predecessor field sets or extending body limits

### Requirement: Actual peer authority and local observation precede response emission

The measurement service SHALL authenticate independently selected actual peer/role/source/incarnation/fingerprint and effective scope/expiry, consume initialized protected nonce state before measurement, and perform current local kernel/process/file observations for that request. A fresh echoed nonce MUST NOT substitute for those actual observations or independently selected observer provenance. Missing state, changed scope, consumed nonce or valid worker authority MUST refuse.

#### Scenario: Approved service and worker submit valid requests
- **WHEN** an available service accepts its selected authenticated peer and the worker submits the corresponding valid request with its own valid certificate
- **THEN** the service succeeds for the approved peer and explicitly denies the worker without treating outage or malformed input as denial

#### Scenario: A service reuses a snapshot or lost attempt
- **WHEN** copied local facts, shared observer provenance, unavailable initialized state or a previously consumed request are supplied
- **THEN** the operation refuses without restarting measurement authority or resetting consumed state

### Requirement: Independent derivation and original budgets remain mandatory

The control authority SHALL independently derive complete expected bytes from approved templates and worker-host roots and compare them against two independently selected actual observer results and current scope. Every nested exchange MUST consume its original phase slot and preserve the earliest original wall/monotonic deadline. Server local work MUST use an independently clipped timer without new proof authority, hidden provider reads, clock joining or budget renewal. Sensitive material MUST remain absent from retained errors/reports.

#### Scenario: Complete remote verification fits its original operation
- **WHEN** both selected observations and independently derived complete bytes match within the measured original charges/deadlines
- **THEN** only the private verified-byte/provenance handoff becomes eligible and full admission remains separately required

#### Scenario: A required bound or current fact cannot be preserved
- **WHEN** a body/read/clock limit is exceeded, current authority changes, private material escapes or full byte derivation is unavailable
- **THEN** source eligibility refuses without truncation, a new ledger/member, late upgrade or copied digest approval

### Requirement: New source semantics preserve existing acceptance boundaries

The v2 profile SHALL remain additive and source-selected, preserving v1, all predecessor/neutral/static/full/report contracts, existing role/input counts and default operational refusal. Exact paired source acceptance MUST precede dependent implementation. Isolated qualification MUST preserve old cases and verify owned cleanup; it MUST NOT establish deployed setup/dispatch, human assurance or consumer acceptance.

#### Scenario: Only a proposal or isolated probe passes
- **WHEN** planning or compatibility diagnostics succeed without accepted complete runtime qualification
- **THEN** P05 stays incomplete and operational/human/consumer gates remain open

#### Scenario: A caller requests automatic activation or old-profile fallback
- **WHEN** configuration, environment, a v1 body or an unrelated operation attempts to select the v2 runtime route
- **THEN** the request refuses and the unchanged default route gains no capability
