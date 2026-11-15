## Purpose

Define source requirements for authenticated hosting, credential issuance and
independent factual readback so a later authorized protected machine qualification
cannot substitute portable fixtures, metadata labels or source acceptance for deployment evidence.

## ADDED Requirements

### Requirement: Source planning and operational authority stay separate

The proposal SHALL treat the T013 recommendations as a design basis, not actual
appointments, resources, credentials, capacity or grants. Source implementation
MUST require explicit owner acceptance/commissioning. Setup, dispatch, actual-run
authority, cleanup and live acceptance MUST remain separately scoped owner gates.
The default operational entrypoint SHALL remain unselected until those gates exist.

#### Scenario: Proposal or isolated checks are complete
- **WHEN** planning, source review or isolated tests pass without later operational authorization
- **THEN** no token, issuer, permission, environment, provider resource or protected run is created or inferred

### Requirement: Credential boundaries reflect real host authority

Hosting SHALL independently authenticate each service and prove actual worker
exclusion from keys, policy, broker/issuer and provider capabilities. VM managed
identities MUST NOT be represented as process isolation. Host-root/platform
administrators and trusted services SHALL remain an explicit TCB. Unproved effective
UID/network/IMDS/key-file restrictions MUST make the deployment ineligible.

#### Scenario: Worker has a valid service request but lacks role authority
- **WHEN** the worker submits the known-good protected request through its actual channel
- **THEN** the selected service explicitly denies it while the independently authenticated allowed caller succeeds

#### Scenario: Extra identity or token capability reaches a worker
- **WHEN** a mutation exposes privileged managed identity, token resolution, signer credentials or observation policy
- **THEN** the denial qualification fails rather than counting service outage as isolation

### Requirement: Current enrollment and least-scope issuance

Credential issuance SHALL bind independently corroborated host/incarnation, source,
service principal, nonce, public fingerprint and role to the selected issuer/key
version and bounded scope. It MUST validate actual returned credential scope and
expiry and independently retire or revoke issued capabilities. A CSR, source label,
App actor or requested permission set MUST NOT approve itself. Tokens and private
material MUST remain outside worker configuration, logs and retained reports.

#### Scenario: Approved service enrolls through the selected issuer
- **WHEN** actual provider/guest/bootstrap facts and public fingerprint match current approved service scope
- **THEN** only that role's bounded credential can be returned over its private authenticated channel

#### Scenario: Scope is overbroad, expired, replayed or revocation is uncertain
- **WHEN** an enrollment nonce/key/host changes or returned capability exceeds scope or cannot be retired
- **THEN** issuance/use or cleanup qualification refuses without exporting secret material

### Requirement: Current software custody is described accurately

The pilot SHALL preserve the owning Ed25519 proof/custody interfaces and identify
its current trusted-host software custody boundary. Key/secret storage MUST NOT
be reported as native Key Vault Ed25519 signing, HSM protection or non-exportable
wallet custody. A stronger hardware custody requirement MUST require an upstream decision.

#### Scenario: Wallet signing uses the accepted owning service
- **WHEN** a later authorized bounded proof uses the existing Ed25519 key/service
- **THEN** the evidence states actual software custody and worker denial without an HSM or algorithm-promotion claim

### Requirement: Callback facts have independent authoritative provenance

Source, protection, deployment, guest-policy, issuer, state and lifecycle callbacks
SHALL obtain current facts from the selected authenticated provider/guest/authority
source. They MUST NOT echo the candidate, trust labels, default missing security
fields or treat provider installation commands as read-only observation. Unsupported
fields or provenance SHALL refuse before readiness. Required protection includes
explicit typed admin-bypass/self-review/reviewer and branch-type restrictions.

#### Scenario: One independent observed fact differs
- **WHEN** a provider, guest, issuer, source, protection, initialization or scheduler observation is changed independently of the candidate
- **THEN** approval/readiness refuses instead of projecting the candidate value as observed truth

#### Scenario: Provider omits a security field or exposes a tag/wildcard
- **WHEN** complete current protection or exact branch semantics cannot be established
- **THEN** the adapter refuses without synthesizing a safe value or silently relaxing the policy

### Requirement: Coordinated main updates retain their real limit

The selected coordinated policy SHALL require accountable current source/window/control
scope, actual supporting readback and refusal on expiry/drift. It MUST NOT claim an
atomic SHA-pinned provider dispatch or proof that administrators can never change
main. No hold, ruleset, tag, bypass or provider permission SHALL be changed by planning.

#### Scenario: Coordination evidence expires or source changes
- **WHEN** current hold/control/source facts cease to match before dispatch/start/finalization/use
- **THEN** authority refuses and consumed scope remains without automatic redispatch

### Requirement: Cleanup survives the claimed failure domain

Cleanup SHALL register durable exact-generation ownership before effects, use an
independently authenticated janitor/scheduler and require separate actual absence/
revocation plus retained/shared preservation readback. Control-host janitor evidence
MUST NOT claim control-host-loss survival. Automatic infrastructure expiry or that
failure guarantee MUST require an independently administered watchdog outside all
three hosts. Unsupported generation-safe retirement MUST remain incomplete rather
than fall back to a broad resource-group deletion or spend-cap claim.

#### Scenario: Worker, gate or orchestration runner dies
- **WHEN** a later authorized case loses one of those processes/hosts
- **THEN** its acknowledged independent janitor reconciles only the registered generation and independent audit establishes cleanup/preservation

#### Scenario: Control-host cleanup or infrastructure retirement is unsupported
- **WHEN** no independent surviving scheduler or required conditional generation semantics exist
- **THEN** expiry/setup/cleanup acceptance stays blocked or incomplete and no protected success receipt is produced

### Requirement: Isolated evidence and protected reports remain distinct

Source acceptance SHALL require substantive isolated positive controls and independent
single-field/privilege/provenance/deadline/crash mutations with actual owning proof
and cleanup. The fixed conformance matrix MUST reject missing/skipped/deselected
cases. A separately versioned protected report MUST require actual approved sources,
provider/guest/issuance facts, case/run and fresh independent cleanup. Existing
source/fixture reports MUST NOT be relabeled or treated as human/domain acceptance.

#### Scenario: Fixtures or copied reports are offered as live evidence
- **WHEN** keys, host observations, case results or cleanup are synthetic, missing, stale or scope-mismatched
- **THEN** protected-machine reporting refuses while retaining honest source/fixture scope
