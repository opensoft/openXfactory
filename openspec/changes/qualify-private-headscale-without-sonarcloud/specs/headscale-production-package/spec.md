## MODIFIED Requirements

### Requirement: Supported release and truthful qualification

Publication SHALL retain actual collected source and CI evidence and immutable supported candidate and provenance readback. For the private T023 package, the owner SHALL supply evaluated, independently accepted quality results that cover the reviewed source, exact test collection and execution, and measured code coverage. The producer SHALL retain the guarded runner case population and report eligible files with zero hits. The coordinator SHALL verify the bound results and preserve private source custody. Source or fixture evidence MUST NOT satisfy actual-client or target observations required by rollout gates.

#### Scenario: Supported release and truthful qualification succeeds within scope

- **WHEN** the exact source candidate is released through the accepted process
- **THEN** its artifact and dependency identity can be independently verified

#### Scenario: Supported release and truthful qualification refuses invalid scope or proof

- **WHEN** only a pilot fixture or source pass exists
- **THEN** no customer or production qualification is inferred

#### Scenario: Private release proof is mismatched

- **WHEN** analysis or coverage omits eligible source, the source or test identities mismatch, or results lack actual independent acceptance
- **THEN** the private package SHALL remain unpublished under T023
