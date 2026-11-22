# Headscale production package delta

Status: ratified
Ratified: 2026-11-22 by Brett Heap. [Ratification record](../../review/ratification.md)

## MODIFIED Requirements

### Requirement: Supported release and truthful qualification

**Modified over `commission-headscale-production`'s addition by qualify-private-headscale-without-sonarcloud (2026-11-22):** — the ratified package commissioning change adds this requirement. This amendment carries it forward for private T023 release qualification.

Publication SHALL retain actual collected source and CI evidence and immutable supported candidate and provenance readback. Before publishing the private T023 package, the owner SHALL supply evaluated, independently accepted quality results that cover the reviewed source, exact test collection and execution, and measured code coverage. The producer SHALL retain the guarded runner case population and report eligible files with zero hits. After immutable publication and readback, the coordinator SHALL verify the authenticated release evidence through default T023 verification before admitting consumer pins. The coordinator SHALL preserve private source custody throughout. Source or fixture evidence MUST NOT satisfy actual-client or target observations required by rollout gates.

#### Scenario: Supported release and truthful qualification succeeds within scope

- **WHEN** the exact source candidate is released through the accepted process
- **THEN** its artifact and dependency identity can be independently verified

#### Scenario: Supported release and truthful qualification refuses invalid scope or proof

- **WHEN** only a pilot fixture or source pass exists
- **THEN** no customer or production qualification is inferred

#### Scenario: Private release source proof is mismatched

- **WHEN** analysis or coverage omits eligible source, the source or test identities mismatch, or the source results lack actual independent acceptance
- **THEN** the private package SHALL remain unpublished under T023

#### Scenario: Private release readback is incomplete

- **WHEN** publication lacks matching immutable readback or authenticated release evidence fails default T023 verification
- **THEN** T023 SHALL remain incomplete and dependent consumer pins SHALL remain unadmitted
