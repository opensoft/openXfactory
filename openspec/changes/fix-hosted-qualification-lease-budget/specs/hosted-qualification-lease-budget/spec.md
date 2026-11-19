## Purpose

Bound the currently measured qualification composition while preserving every
per-use lease observation, original authority window and independent cleanup.

## ADDED Requirements

### Requirement: Qualification-only fixed private allocation

A separately source-accepted trusted qualification operation SHALL have at most39
private observations. Every required observation MUST execute and be accounted for.
Worker, callback, dispatch or environment data MUST NOT select or enlarge that cap.

#### Scenario: Complete qualified source path after acceptance
- **WHEN** accepted source executes the actual hosted proof, exact replay and approved negative controls
- **THEN** every required observation SHALL fit the fixed allocation and original window or qualification SHALL refuse

#### Scenario: Private allocation exhaustion
- **WHEN** a qualification attempts its40th private observation
- **THEN** it SHALL refuse before that I/O and SHALL NOT reset, omit, transfer or renew authority

### Requirement: Entry precedes all use and retains one original authority

The qualification allocation MUST be selected before the original operation's first
read or API/correlation use. The entire operation SHALL share that identical original
Decision and one ledger member. Late/repeated entry, phase reuse or joining another
Decision MUST refuse. All original wall/monotonic deadlines and earliest expiries
SHALL remain authoritative.

#### Scenario: Previously consumed or differently scoped operation
- **WHEN** an operation already has a read ledger, correlation use or another phase allocation
- **THEN** qualification entry SHALL refuse without altering its existing state or clocks

#### Scenario: Slow or regressed operation
- **WHEN** any reader exceeds the original time window, earliest expiry or monotonic floor
- **THEN** qualification SHALL refuse even if private capacity remains

### Requirement: Other phase limits and independent cleanup remain unchanged

Ordinary/private12, protected-staging/private16, finalization/private12 and independent
cleanup/private12 SHALL remain unchanged, together with every accepted GitHub,
per-reader, role, source and input limit. The report SHALL perform no I/O. Cleanup
SHALL retain its original registered scope, generation, timeout and cleanup_until.

#### Scenario: Non-qualification operation
- **WHEN** ordinary, staging, finalization or cleanup code executes
- **THEN** its existing limits SHALL apply and no qualification allowance SHALL be available

#### Scenario: Failed or cancelled operation
- **WHEN** qualification fails, is cancelled or loses a mutation response
- **THEN** independent original-scope cleanup SHALL remain required and success SHALL NOT be inferred or a consumed action retried

### Requirement: Honest validation and separate operational acceptance

Source realization MUST independently qualify the actual hosted positive under the
new allocation and unchanged window. Portable component measurements, private
encoder vectors or failed hosted positives MUST NOT clear that gate. Source acceptance
SHALL grant no setup, dispatch, live report or human/domain/consumer authority.

#### Scenario: Component passes while hosted operation is unavailable
- **WHEN** source component controls pass but the actual hosted positive cannot complete
- **THEN** hosted qualification SHALL remain incomplete and further changes SHALL require separate governance
