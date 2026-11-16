# Protected runtime report requirements

Status: draft
Kind: specification

## Purpose

Define a separate factual protected-machine report whose eligibility is established
by authenticated actual-run evidence, while preserving source/fixture reporting
and keeping machine facts distinct from human, consumer and domain authority.

## ADDED Requirements

### Requirement: Operational provenance is independently established

The system SHALL permit protected-report construction only after authenticating
actual approved operational source, run/attempt, phase, generation and issuance
facts through selected independent channels. Payload labels, Python types, supplied
pass booleans and offline results MUST NOT establish that eligibility.

#### Scenario: Actual approved operational run is observed
- **WHEN** authenticated same-run phase/generation/issuance facts satisfy the accepted scope
- **THEN** the report projection is eligible for case and cleanup validation without granting another operation

#### Scenario: Fixture or copied evidence is offered
- **WHEN** source/fixture output, constructor labels or a claimed live flag is offered as operational evidence
- **THEN** protected emission refuses and honest source/fixture evidence retains its original scope

### Requirement: Protected reporting has a separate closed vocabulary

The system SHALL use the separate internal profile and exact bounded projection
specified in design D2. Existing source/fixture profile semantics and vocabulary
MUST remain compatible. Unknown/duplicate keys, unsupported types, missing required
provenance or output above 16,384 canonical bytes MUST refuse without truncation.

#### Scenario: New report and existing callers coexist
- **WHEN** a valid source/fixture caller uses the existing profile
- **THEN** its old scoped behavior and fixed authority flags are unchanged

#### Scenario: Unrecognized data is supplied
- **WHEN** a protected candidate includes extra fields, invalid digests or excessive canonical output
- **THEN** construction refuses with a fixed safe error and emits no raw fallback

### Requirement: Proof and negative controls measure the owning boundary

The system SHALL derive protected proof evidence from an actual owning-verifier
positive, same-proof replay refusal, valid-signed audience-only/environment-only
negatives and an available explicit worker-denial control. Outages, invalid
signatures and excess-permission exposure MUST NOT count as successful barriers.

#### Scenario: Bounded owning proof and replay are verified
- **WHEN** one approved proof is accepted and its exact replay is independently refused
- **THEN** evidence records the bound result digests for that same run without minting another grant

#### Scenario: A specific barrier is removed
- **WHEN** an audience/environment check or worker restriction is independently removed
- **THEN** its source qualification fails despite the other claims remaining valid

### Requirement: Cleanup and time remain independently verified

The system SHALL bind the protected report to the immutable actual RunScope,
RunPlan, generation and fresh independent cleanup attempt. Successful qualification
requires actual run-resource retirement and preservation of retained/shared
generations. Reporting MUST NOT retry mutations, renew deadlines, reset budgets
or repair an exhausted/corrupt journal.

#### Scenario: Operation fails or is cancelled
- **WHEN** the operation fails or is cancelled and independent cleanup succeeds
- **THEN** the report preserves failure/cancellation and cannot upgrade to passed

#### Scenario: Privacy is evaluated after cleanup
- **WHEN** privacy and cleanup-derived case results are finalized from fresh verified cleanup before report issuance
- **THEN** they are accepted as report-only observations without requiring cleanup to observe a later privacy check or granting further runtime use

#### Scenario: Cleanup is stale or incomplete
- **WHEN** a cleanup result has the wrong scope, attempt, generation, expired window or preserved-resource mismatch
- **THEN** protected-machine qualification remains false and reporting cannot perform corrective mutations

### Requirement: Status and authority are distinct

The system SHALL derive status and qualification from all required case/proof/live
and cleanup facts according to design D2. Missing live facts MUST remain
not-performed/incomplete. Human approval, domain effect and consumer dependency
acceptance MUST remain false regardless of machine qualification.

#### Scenario: Every protected fact is established
- **WHEN** all 27 required semantic/live slots pass with authenticated operational provenance and fresh successful cleanup
- **THEN** the report records machine qualification only and grants no human, consumer or domain authority

#### Scenario: A required fact is missing
- **WHEN** any required live case or proof/cleanup observation is absent
- **THEN** the report cannot claim protected-machine qualification from offline conformance

### Requirement: Privacy and content addressing do not create authority

The system SHALL emit only the closed redacted projection and fixed safe errors.
Raw credentials, private keys, proof/challenge bodies, provider payloads and
exception details MUST NOT enter reports. Privacy-case evidence MUST NOT depend
on a digest of the final report containing that digest. An unauthenticated report
hash MUST NOT authenticate a host or authorize an operation.

#### Scenario: Sensitive data reaches a failure path
- **WHEN** an exception or provider response contains a private canary
- **THEN** the report contains only the allowed safe code and bounded digests, with no canary or raw payload

#### Scenario: A report is replayed as a grant
- **WHEN** report bytes or their content hash are submitted as a wallet proof, MFA receipt or approval token
- **THEN** no operation authority or consumer/human acceptance follows

### Requirement: Source preparation cannot activate the pilot

The system SHALL preserve the current refusing operational default, seven service
roles, eight source roles, three dispatch inputs and existing budgets. Protected
setup/dispatch, live qualification and delivery require separate owner authority;
artifact completion MUST NOT supply it.

#### Scenario: Source preparation is complete
- **WHEN** the proposal and isolated implementation plan are generated or source tests pass
- **THEN** setup/dispatch and live acceptance remain ungranted and no service is initialized
