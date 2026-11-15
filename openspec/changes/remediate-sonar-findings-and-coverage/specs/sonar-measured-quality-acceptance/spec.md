## ADDED Requirements

### Requirement: Repair findings through source behavior

The maintainer SHALL fix the identified reliability and security boundaries
with deterministic positive and refusal tests, retaining valid supported use.

#### Scenario: An agent supplies an unsafe operand
- **WHEN** a CLI file operand escapes the trusted invocation root, a Git operand changes option interpretation, or a private browser copy fails its ownership or identity checks
- **THEN** execution SHALL refuse before unsafe reads, writes, imports or browser actions
- **AND** optimization SHALL NOT remove security checks

### Requirement: Preserve historical acceptance meaning

The maintainer SHALL retain dated verdicts, logs and the immutable original
driver source, and identify the maintained replacement separately.

#### Scenario: A replay driver is repaired
- **WHEN** the driver changes after a recorded acceptance run
- **THEN** a new provenance record SHALL identify the original revision and digest
- **AND** previous PASS records SHALL remain claims about their own dated executions

### Requirement: Import genuine complete coverage

The CI analysis SHALL import real line and branch execution from the existing
complete test suite and its Python subprocesses at the exact analyzed commit.

#### Scenario: A source file or report is absent
- **WHEN** an owned production file is missing from coverage inventory, a report cannot resolve to source, or coverage is not evaluated
- **THEN** qualification SHALL fail
- **AND** the maintainer SHALL NOT fabricate hits, omit production or loosen a threshold to pass

### Requirement: Preserve acceptance strength and operational state

The maintainer SHALL keep the existing baseline, six gate conditions, profiles,
test census, exact skip budget and named freshness check, with unchanged
billing, permissions, operating checkouts, sessions and historical identities.

#### Scenario: Main is declared accepted
- **WHEN** the change lands
- **THEN** fresh analysis of the published revision SHALL report OK with all six conditions evaluated, including new-code coverage at least 80 percent
- **AND** repository workflows and preservation readback SHALL pass
