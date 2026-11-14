## ADDED Requirements

### Requirement: Preserve the existing acceptance gate

The operator SHALL retain the existing Sonar way conditions, profiles, source
scope, exclusions, permissions, history and issue dispositions while restoring
the missing new-code definition.

#### Scenario: A historical reference is selected

- **WHEN** the existing project has no configured new-code definition
- **THEN** the earliest retained successful main analysis SHALL anchor the assessment
- **AND** the current analysis SHALL NOT be selected to hide existing changes

### Requirement: Verify computation rather than upload

The operator SHALL observe a fresh actual-main analysis and record its computed
gate status and every condition without weakening checks or claiming neutral
or ignored results as successful acceptance.

#### Scenario: The computed gate reports failure

- **WHEN** fresh server processing computes an ERROR condition
- **THEN** the result SHALL remain a failure requiring its own evidenced repair
- **AND** the operator SHALL NOT change the reference, threshold or issue status to turn it green
