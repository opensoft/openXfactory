## Purpose

Bound every physical first-pilot remote lifecycle request without granting a new
run, resetting an original attempt or hiding nested credential observations.

## ADDED Requirements

### Requirement: Only exact accepted source selects the finite lifecycle policy

The adapter SHALL select only the policy and schedules in supporting-docs/policy.json
from its immutable original registered RunPlan credential manifest before I/O,
with one through three credentials. It MUST preserve old routes, private12,
staging16, qualification39, GitHub/protection/body limits, roles, inputs and default
refusal. The new policy MUST NOT authorize setup, dispatch or additional resources.

#### Scenario: Source preparation is present without owner acceptance
- **WHEN** this candidate inventory and paired subplan exist without exact paired source ratification
- **THEN** dependent runtime implementation remains stopped and T013P08 remains unchecked

#### Scenario: A caller selects a policy or omits registered checks
- **WHEN** a worker, environment, profile, callback or changed manifest selects a cap or removes credential observations
- **THEN** selection refuses before I/O and the original route and limits remain intact

### Requirement: Caller prepayment conserves all physical work and original authority

The adapter SHALL debit each RPC and its fixed maximum nested private work before
send under the selected per-manifest limit: handoff12+2N, original runtime cleanup
with independent audit2+5N, separately authorized audit-only1+N. It MUST retain
original consumption, scope, registration, exact types and deadline clipping.
It MUST NOT refund, retry, borrow, reconstruct, transfer or start fresh authority.

#### Scenario: A nested call would exceed original private12
- **WHEN** the unamended route prepays complete prepare or acknowledgement work
- **THEN** it refuses before send without takeover acknowledgement, release or proof and retains consumed original state

#### Scenario: A selected original request loses its response
- **WHEN** a prepaid call fails or has an ambiguous outcome
- **THEN** the original debit remains consumed, mutation is not resent and only separately authorized original-scope observation may proceed without renewal

### Requirement: Source arithmetic and runtime qualification remain distinct

The packet SHALL reproduce all measured N1/N3 physical totals and label N2 as
derived only. It MUST retain failed independent-audit diagnostics. Later runtime
qualification MUST independently observe complete physical work, old full/native
identities, deadlines, refusal/crash behavior and clean final fixture state.

#### Scenario: The offline reproducer passes
- **WHEN** the frozen policy and measurement digests and inventory arithmetic match
- **THEN** only the source model is validated and no runtime, live or operational qualification is asserted

#### Scenario: The connected route needs another accounting or authority change
- **WHEN** a complete owning-proof positive exceeds any remaining accepted cap or requires a new type, journal or grant
- **THEN** implementation stops for a governed amendment without raising limits or deleting checks
