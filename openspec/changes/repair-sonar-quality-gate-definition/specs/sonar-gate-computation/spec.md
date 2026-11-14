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


### Requirement: Retain reachability obligations for receipt anchors

The maintainer SHALL declare the exact recovery receipt's revision fields as
a standing, repo-local, must-resolve member of the existing pin class. Existing
class semantics, populations and reachability requirements SHALL remain intact.

#### Scenario: An audit anchor is not reachable from the allowed refs

- **WHEN** a receipt anchor exists only in an unrelated branch or loose object
- **THEN** the existing reachability guard SHALL refuse passing verification
- **AND** the new member SHALL NOT cover other receipt paths or gain a historical exemption
