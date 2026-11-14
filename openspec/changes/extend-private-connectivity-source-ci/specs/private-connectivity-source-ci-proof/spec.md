## Purpose

Allow coordinator CI to verify the immutable private-owner commit references in actual feature 043 evidence without publishing private source or treating inventory proof as task acceptance.

## ADDED Requirements

### Requirement: Private source proof is bounded by actual references and existing authority

The system SHALL prepare proof only for actual full immutable commit identities in registered feature 043 records, using the fixed accepted component repositories and existing App installations. It MUST use repository-scoped contents-read-only credentials and an accepted reviewed producer, and MUST NOT change App access, secrets, approval policy or a rollout gate.

#### Scenario: Actual package references require one owner

- **WHEN** committed registered data contains private Headscale package references and no other private owner references
- **THEN** preparation obtains only the required package commit proof with contents-read-only repository scope, and grants no source, deployment or gate acceptance.

#### Scenario: No private references exist

- **WHEN** registered data contains only coordinator references
- **THEN** no private credential/fetch is required and the unpopulated foreign member remains FUTURE.

#### Scenario: Credential or producer scope is unavailable

- **WHEN** private references exist but the expected App/installation, repository scope or reviewed producer provenance cannot be established
- **THEN** preparation fails before private admission without a fallback credential, access-setting change, skip or trust bypass.

### Requirement: Private proof custody is ephemeral and contains no source trees

The system SHALL keep private commit-presence proof in separate temporary owner stores outside the public coordinator checkout. It MUST verify the required immutable commit objects and exact repository provenance, prohibit lazy/full source fetching and private source publication, revoke credentials before tests, and remove private proof stores after the job. It MUST NOT emit private commit contents or credentials to public logs, Git, artifacts or caches.

#### Scenario: Required commit metadata is available

- **WHEN** bounded filtered preparation retrieves the required commits from their exact private owner repositories
- **THEN** offline inventory verification can use those separate roots without receiving source trees or live credentials.

#### Scenario: Fetch would contain private source or incomplete proof

- **WHEN** filtering is unavailable, unexpected tree/blob objects arrive, or a required commit/origin is missing or mismatched
- **THEN** the job fails and cleans up instead of fetching full source, uploading proof or reporting success.

### Requirement: Both CI lanes reject incomplete or aliased owner proof

The system SHALL require explicit fixed-owner proof roots for actual private data in both existing pytest-suite and doc-health-py314 entry points. It MUST reject unknown, duplicate, missing or aliased roots, coordinator overrides and wrong ownership, and preserve all existing check identities, floors, skip obligations and named verdicts.

#### Scenario: A private commit happens to exist in the coordinator object store

- **WHEN** an actual private-owner reference lacks its independent owner root but the same object is locally available in the coordinator
- **THEN** both inventory checks fail without reclassifying the reference as coordinator-owned or discovering an implicit root.

#### Scenario: One entry point lacks its proof precondition

- **WHEN** private data is introduced while either existing CI lane cannot establish the required independent proof
- **THEN** readiness fails even if the other lane passes, and no standing obligation is waived or changed to rolling.

### Requirement: Scope review and actual evidence admission remain separate

The system SHALL apply the exact T009/T010 and source-CI custody refinement only after actual affected-owner acceptance and a complete new definition freeze. It MUST preserve historical accepted observations/readers/anchors, require actual new source/CI evidence and custodian authentication for a new control, and require full default task verification before completion. Metadata inventory proof MUST NOT supply source conformance, owner authentication, release or Q0–Q5 acceptance.

#### Scenario: The CI scope is ratified before actual source output exists

- **WHEN** the owner ratifies this proposal and the bounded definition refinement
- **THEN** source implementation may proceed in dependency order but no unseen output is authenticated and no dependent task or live gate is completed by that consent.

#### Scenario: New definition consumes historical accepted evidence

- **WHEN** a new control depends on previously accepted observations with an earlier definition
- **THEN** their exact original identities and matching immutable readers remain verifiable, while the new control requires its own actual authentication and default admission.
