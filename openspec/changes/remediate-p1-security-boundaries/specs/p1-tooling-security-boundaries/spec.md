## ADDED Requirements

### Requirement: Profile writes preserve authority and private state
The harness SHALL validate profile identity and private filesystem authority
before browser or credential side effects, refuse unsafe links/types/ownership,
retain account-mismatch and metadata-merge semantics, stage private output
before replacement and serialize cooperating writes.

#### Scenario: Unsafe profile or substituted credential target
- **WHEN** a profile escapes its store or a target is linked/non-regular
- **THEN** the harness refuses without modifying credential or outside bytes

#### Scenario: Legitimate same-account refresh
- **WHEN** a valid private profile receives matching or absent captured identity
- **THEN** captured credentials update and stored identity/unknown keys survive

#### Scenario: Occupied browser state
- **WHEN** a persistent browser profile has an ownership marker
- **THEN** launch refuses and leaves the existing browser/session untouched

### Requirement: Privileged installers use verified fixed dependencies
CI SHALL install reviewed hash-locked binary Python artifacts and a locked
worker CLI closure with package lifecycle scripts disabled, retaining the
existing worker/fallback behavior and all security/validation checks.

#### Scenario: Dependency drift or unavailable binary
- **WHEN** package bytes or lock/manifest disagree or no approved binary exists
- **THEN** installation fails instead of rebuilding source or resolving a range

#### Scenario: Functional offline worker CLI
- **WHEN** the pinned closure installs without lifecycle scripts
- **THEN** its worker command is executable and reports the pinned version
- **AND** no provider request, global installation or active profile is used

### Requirement: Remaining P1 boundaries retain explicit trusted roots
Maintained P1 writers and policy readers SHALL validate authority independently
from untrusted operands and fail closed before unsafe I/O; executables and child
option operands SHALL satisfy their declared trusted contracts.

#### Scenario: Escaping or option-shaped model input
- **WHEN** a model-selected operand exceeds the trusted root or command contract
- **THEN** the operation refuses without outside writes or unintended execution

### Requirement: Main acceptance preserves original evidence and checks
Each landed phase SHALL retain original issue identities and historical evidence,
run relevant full existing gates, and verify the actual merged revision against
the unchanged Sonar gate/reference, coverage and issue readback.

#### Scenario: Published phase
- **WHEN** a phase reaches main
- **THEN** exact-commit CI and Sonar evidence are reconciled and unresolved P1 keys
  remain explicit without waivers, exclusions, baseline reset or billing changes
