## ADDED Requirements

### Requirement: Operation-specific bounded protection observations

The trusted finalizer SHALL allocate at most six fresh complete protection
observations, eighteen protection reads and twenty-eight aggregate GitHub reads.
Ordinary admission/correlation SHALL retain three protection/thirteen aggregate
reads. Each observation SHALL retain required typed fields, explicit branch type,
fixed routes and at most two bounded policy pages. No worker field, late budget
upgrade, retry or stale fallback SHALL select or increase these limits.

#### Scenario: Complete finalization within the allocated envelope

- **WHEN** the caller and independent authority perform the accepted six checks
- **THEN** all six current environment/policy observations occur and complete
  canonical configuration/policy bytes are independently recomputed

#### Scenario: Additional observation or request exceeds the allocation

- **WHEN** a seventh observation, nineteenth protection read, twenty-ninth total
  read or changed source/control/correlation limit is attempted
- **THEN** the operation refuses before the excess I/O without restarting counters

### Requirement: Independent authority shares enclosing accounting and time

The authority SHALL retain independent observers and recomputation while sharing
one accounting ledger with its caller before any read. Correlation high-water
SHALL be tracked per member with four total reads; group/snapshot counts SHALL
persist across clients and both decisions. Both original monotonic/wall bounds
and earliest expiry SHALL apply at checkpoints and before return.

#### Scenario: A nested client or authority cannot obtain a fresh budget

- **WHEN** either member recreates a client or requests another joined decision
- **THEN** consumed reads persist and an unapproved third member or late upgrade
  refuses; ordinary admission does not receive finalization authority

#### Scenario: Late protection drift or deadline failure

- **WHEN** an independently observed protection/source/hold fact changes or either
  member expires/regresses during a blocking phase
- **THEN** no finalized readiness/proof is returned and failure does not renew time

### Requirement: Source acceptance and operations remain separate

The amendment SHALL own internal allocation semantics only, preserving neutral
APIs/pins, v1/default activation and all setup/dispatch/live qualification gates.

#### Scenario: Isolated candidate succeeds

- **WHEN** local or hosted source qualification passes
- **THEN** it supplies review evidence only; owner ratification, T013 selections,
  setup/dispatch and live acceptance remain separate
