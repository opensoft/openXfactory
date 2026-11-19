# Production qualification owner scopes

Status: draft
Created: 2026-11-13
Feature: [043-private-connectivity-production](spec.md)

## Authority recorded by this feature creation

Brett Heap requested the coordinating feature, implementation plan, task generation and cross-artifact analysis/remediation in this session. The current authorized artifact scope is openXfactory's specification/plan/task packet and its analysis/remediation record under specs/043-private-connectivity-production, its feature selector, managed agent-context plan reference and its governance/index handoff links.

This authorizes specification, plan, task-list and analysis/remediation preparation. Q0 is not accepted by this document. The ratified policy approves ownership boundaries, not new runtime code, workflow, schema or deployment path grants. Owner acceptance and concrete realization authority remain required before implementation. The single [tasks.md](tasks.md) represents each implementation item once.

## Responsibility boundaries for Q0 commissioning

| Owner class / repository | Owned production outcome | Scope to make concrete and approve before implementation | Authority not inherited from this draft |
| --- | --- | --- | --- |
| Neutral coordinator / opensoft/openXfactory | Production qualification policy, feature coordination, neutral contract publication if separately required | Named maintainer; exact documentation, contract, schema, validator/test and CI surfaces if commissioned; existing publication/release process and verification commands | Hosted runtime, provider operation, an unallocated contract version, consumer-pin updates or paid resources |
| Package / opensoft/Headscale-Install | Supported package, HTTPS identity and renewal, isolated instance/state lifecycle, backup, upgrade and quarantined recovery | Named maintainer; supported platforms/server/clients, exact package/state and conformance surfaces, release custody and verification commands | Cross-customer operation, entitlement decisions or execution on a registered managed target without handoff |
| Installer / opensoft/xFactory-Installer | Supported setup/distribution for install-new, connect-existing, managed selection and unbound compatibility | Named maintainer; exact selection/setup/distribution and validation surfaces, supported packaging matrix and verification commands | The unrelated workstation-intake application, Store submission, service entitlement or operational administration |
| Hosted product / opensoft/openXsoft-Hosted-Services | Actual provider/identity/entitlement integrations, durable managed operations, factory onboarding, catalog and exact-profile eligibility | Named maintainer; intended platform/provider first, then exact adapter/service/profile/catalog and required-check surfaces, releases and verification commands | Approval of another owner's domain, deployment credentials, provider spend or expansion by declaration |
| Operational executor / opensoft/opsXfactory and the target's managing factory | Managed-subject handoff, custody, monitoring, operational acceptance, emergency containment, recovery and rollback | Named operational owner; registered target subjects, governed channel, exact operating/monitoring surfaces, scoped requests/grants where required, run evidence and commands | A standing builder credential, execution outside accepted target scope, or consent for an unmanaged customer target |
| Actual production DomainxFactory owner / repository selected at Q0 | Actual workload, minimum access, application authorization, exact profile and lifecycle acceptance | Named domain maintainer and actual repository/profile; exact definition-time protection, required validation and workload/access/CI surfaces; release evidence and commands | Another domain/profile's acceptance, feature 040 synthetic-profile eligibility or blanket catalog launch |

Every row is a responsibility boundary, not an approved file allowlist. Concrete repository, file/code/CI/schema surfaces, commands, approver, decision reference and validity are mandatory commissioning fields. Where an owning governance change is required, its acceptance precedes the dependent work. A missing scope remains uncommissioned.

## Human roles and decisions

The commissioning record names the rollout lead and accountable neutral, package, installer, hosted-product, operational and domain owners. It also names customer authority where consent or customer operation is required, evidence/backup/credential custodians, support/on-call and rollback operators for the relevant gates.

One person may hold several roles, but each role and scope is explicit. Brett's request to create this feature does not sign for every runtime owner or customer. The five feature 040 lab-role approvals do not approve these production decisions.

## Execution boundary

For a registered managed target, the producing owner ends at its supported release and realization evidence. Deployment crosses as an accepted client_infrastructure_request, executed through the managing factory's governed channel. A grant-required channel uses a valid scoped grant and closes it on completion. A reviewed governed merge applied by pull reconciliation does not acquire an additional push credential.

An unmanaged customer-operated target remains under its current authorized customer operator and required consent. Environment tier never chooses the executor. Q0 commissioning, target execution, gate acceptance and commercial release are separate authorities.

## Current disposition

T001-T009 are complete. The original T006 E scope and source-only custody remain recorded in their historical ratification. Brett has now ratified the E bootstrap amendment, all five component scopes and matching native Ops/domain packets, and the separate neutral publication/release scope. The accepted file refinements are reconciled into tasks.md and the current review freeze; source consent does not complete T010-T017 or full Q0. T010 still requires actual original evidence and custodian authentication. All three PRs remain draft.

| Accepted source role | Named owner/custodian | Exact governing scope |
| --- | --- | --- |
| E evidence controls | Brett Heap | [Original E scope](../../openspec/changes/commission-private-connectivity-production-evidence/design.md) plus [ratified bootstrap amendment](../../openspec/changes/amend-private-connectivity-evidence-bootstrap/review/ratification.md) |
| N neutral publication/release | Brett Heap | [Accepted publication scope](../../openspec/changes/publish-private-connectivity-production-contract/review/ratification.md); normal atomic cut and late version/inventory allocation |
| L package/source/release | Brett Heap | [Accepted package scope](../../openspec/changes/commission-headscale-production/review/ratification.md) |
| I installer/source/release | Brett Heap | [Accepted installer scope](../../openspec/changes/commission-connectivity-installer-production/review/ratification.md) |
| H hosted product/source/release | Brett Heap | [Accepted hosted-product scope](../../openspec/changes/commission-hosted-headscale-production/review/ratification.md) |
| D domain/profile/source/release | Brett Heap | [Accepted actual MCP source scope](../../openspec/changes/commission-hosted-domain-production/review/ratification.md), with matching native packet |
| O operations/source/release | Brett Heap | [Accepted Ops source scope](../../openspec/changes/commission-connectivity-operations-production/review/ratification.md), with matching native packet |

Component source custody is reviewed/redacted original source/CI and genuine decision provenance retained in each private owning Git repository for project lifetime under existing permissions, bound to exact commits/content, actual run/job/command identities and actual owner review. Coordinator E keeps its accepted public secret-free source Git policy. Neutral publication follows its accepted existing versioning/release custody and verification process. None selects protected live/customer/provider custody.

The accepted source repositories and exact file lists grant no target operation. Actual provider/target/service choices, supported version/distribution matrix and consumed integration/limit/custody decisions must be accepted before their consumers. No source or release role supplies an operator/customer grant, a standing deployment credential or commercial admission. The approved USD 10 QA storage financial envelope and separately applied repository Mac zero-paid guard retain their exact limits; they authorize no provisioning or runner job.

## Candidate implementation and verification surfaces

These are inspected source anchors and proposed new areas for C-01 review, not an accepted allowlist. Close each scope to exact files/commands under the owning decision before edits. Some inspected owner primary checkouts are stale; verify the selected owner revision and accepted release rather than assuming a local main is current.

| Commissioning boundary | Existing source anchors / proposed new work | Existing verification and required production extension |
| --- | --- | --- |
| Neutral publication | scripts/validate-private-connectivity.py and tests/private_connectivity currently consume the feature 040 draft schema. Proposed supported publication is contracts/private-connectivity with contracts/manifest.yaml, contracts/CHANGELOG.md and generated contracts/releases inventories | Existing binding conformance plus normal release build/commit/promotion/tag verification. Accept exact publication/reader/test scope first, allocate version at the approved cut, then verify published consumer content pins |
| Coordinator evidence | Proposed new specs/043-private-connectivity-production/verify-evidence.py, register-evidence-pins.py, tests/test_evidence.py and tests/test_evidence_pins.py. Shared scripts/doc_health/pin_class.py, tests/doc-health/test_pin_reachability.py and test_sentinel_vocabulary.py census, plus .github/workflows/pytest-suite.yml if required wiring changes, are separate governed surfaces | Commission verifier/case/command/dependency tests and an explicit required invocation of the new feature suite. Obtain narrow owning OpenSpec authority before shared-reader, census or workflow edits; 040 registration does not cover 043 |
| Headscale-Install | deploy/pilot.py, workloads.py, application.py and preflight.py are fixed lab controls; deploy/recovery.py provides backup/quarantine rehearsal. packaging, release, docs/runbooks and tests/qualification anchor supported packaging/renewal/state/recovery work. Exact distinct production files are selected by the owner | make validate and make test are existing source/fixture commands under .github/workflows/qualification.yml. Commission actual supported-client/TLS-renewal/recovery/platform qualification before Q1; preserve lab guards and release helper provenance |
| xFactory-Installer | src/private_connectivity/selection.py, pilot_provider.py and managed_provider.py; existing contract/headscale pins, vendor/requirements and runtime inventory; tests/private_connectivity and docs/private-connectivity.md. Exact production adapter/setup/distribution files require accepted scope | make validate and make test under .github/workflows/validate.yml, with the declared schema dependency. Qualify new/existing/unbound and managed production choices plus current authority/retry/migration/rollback. No workstation-intake or Store scope is inherited |
| Hosted product | services/network-provisioning/service.py, operations.py, attachments.py and supervisor.py; synthetic docker_pilot.py/docker_nodes.py; services/factory-onboarding/onboarding.py and pilot_binder.py; services/catalog/qualification.py and release inventories/pins | make validate and make test under .github/workflows/qualification.yml. Actual provider/authentication/entitlement/custody/workload adapters and strict production catalog semantics need exact newly accepted paths. Preserve durable original-subject state and derive privacy from the trusted profile |
| Ops/managing factory | workflows/client-infrastructure-execution.yaml, scripts/client_infrastructure_execution.py, deployment/custody interfaces, workflows/private-connectivity/recovery.py and docker_recovery.py, docs/private-connectivity and tests/private_connectivity | Existing intake/correlation self-checks and explicit python3 -m pytest tests/private_connectivity -q. Commission actual operational adapters, monitoring/custody and required CI invocation. Generic shard discovery omits this nested suite; changing scripts/run_test_shards.py is only necessary if that discovery solution is selected, otherwise use an accepted explicit required entry point |
| Actual domain | Selection and exact production paths are blocked on C-02. Historical codeXfactory anchors are profiles/hosted/private-connectivity.yaml, schemas/hosted-connectivity-profile.schema.json, tests/private_connectivity, scripts/merge_master/council_clearance.py and required doc/CI wiring | The historical profile is test/synthetic/customer-ineligible and its protection is exact to that file. A selected production owner must accept actual workload/profile/schema, exact definition-time protection and fail-closed required validation/dependencies. Equivalent owner mechanisms are acceptable; copying a directory prefix or another profile's evidence is not |

The plan's E/N/L/H/I/D/O workstreams and [validation matrix](validation-matrix.md) use these boundaries. This source-anchor table does not enlarge the exact ratified per-task scopes above. Ops uses the accepted separate private-connectivity-validation workflow; scripts/run_test_shards.py and the existing opsx-validation workflow are excluded from that source grant.
## Accepted cut-validation and QA handoff refinements

Brett Heap accepted the exact N/E design at 2026-11-17T02:55:36.438Z and the
matching Ops and Tenant owner plans at 2026-11-17T03:01:06.114Z. The actual
owner decisions and source-only limits are recorded in their immutable review
packets:

- [N/E four-path T018 refinement, bounded 2a46 compatibility and complete freeze](https://github.com/opensoft/openXfactory/blob/55e3cafd3c2d44a9933de20708fad6d46e9d7573/openspec/changes/extend-private-connectivity-cut-validation/design.md).
- [Ops seventeen coupled T043 paths and two T047 timing/manifest paths](https://github.com/opensoft/opsXfactory/blob/91c080220fd1acbd6b602883c93e177fb92a5218/openspec/changes/admit-private-connectivity-qa-operations/design.md).
- [Tenant declarative target-data/runbook handoff](https://github.com/opensoft/Opensoft-Tenant/blob/71475785c0ef838e4c04c989a232f1a8f7d2b49a/openspec/changes/prepare-private-connectivity-qa-target/design.md).

Only the accepted T018/T043/T047 file lists change. All 68 task identities,
owners, classes, required cases, dependencies and verification commands remain
unchanged. The T043 shard manifest/timing paths are coupled discovery/census
metadata, not permission to change the generic shard runner or its required
workflow. T047 may settle only their actual later CI measurement metadata.
Three exact isolated workload sets remain behind their reviewed managing-factory
channel, full release dependencies and current operating authority.

Tenant is a later declarative operating target, not a seventh executable source
component. Feature-specific validation remains Ops-owned and existing Tenant
validation stays in place. No new Tenant validator, test or workflow is granted.
Actual target writes/reconciliation remain a separately accepted T050/C-03
operation after released dependencies, full Q0 and T049.

Qualify the E compatibility/freeze/CI changes against the independent published
contract-v4.2 tree before consuming N conformance/classification changes. Actual
new E output requires separate custodian authentication and default admission.
Original 2a46 controls/readers retain their exact accepted source-task closures;
no pending or live task gains acceptance. All PRs stay draft. No merge, final
version allocation, annotated publication, target effect, spend, enrollment,
protected retention lock or Q0-Q5 acceptance is granted.

### Accepted companion-prose coupling

At 2026-11-17T03:40:50.580Z Brett accepted the exact additional four active
Ops requirement-copy paths in the [reviewed N/E amendment](https://github.com/opensoft/openXfactory/blob/0576faced67b015bf07d054814ae0d96147aa320/openspec/changes/extend-private-connectivity-cut-validation/review/ops-prose-parity-scope.md)
and its [matching Ops amendment](https://github.com/opensoft/opsXfactory/blob/657b02d0e6a4f01d6fcbef8453a1937131331550/openspec/changes/admit-private-connectivity-qa-operations/review/prose-parity-scope.md).
Only T043 adds these four exact OpenSpec paths, bringing its coupled Ops
additions to twenty-one. N's four paths, T047's two paths and every other task
field stay unchanged. Existing MCP placement/fallback/history and all previous
rules are preserved. Normal single-newline EOF formatting is recorded with the
actual identical block hash in the owner-local implementation evidence.

The source-only 4f963e0f candidate was never authenticated and supplies no
accepted historical control. Preserve its actual observations under their
original source identity; qualify this complete refreshed E source and CI anew.
The fixed accepted 2a46 controls/readers remain the only added historical
anchors. Actual new output authentication/default admission and all release,
operating and Q0-Q5 gates remain separate.

## Approved internal execution amendment

Brett directly accepted the exact [root policy and record](../../openspec/changes/authorize-private-connectivity-internal-production/review/ratification.md) at
2026-11-17T08:38:55.473Z, valid for new agent actions until
2026-12-17T08:38:55.473Z. He remains accountable for all initial component,
rollout, release, operational/rollback, identity/DNS/TLS and custody roles.
Codex is the distinct delegate; it never records a future human sign-off.

The directly reviewed E refinement adds only
specs/043-private-connectivity-production/attest-delegated-evidence.py to T010.
The directly reviewed C-10 refinement adds only
specs/043-private-connectivity-production/review/internal-production-handoff.md
to T061 and the conditional aggregate-only case internal-program-handoff.
All existing child cases, task identities, owners, classes, dependencies and
commands remain. Existing exact E source/CI/test paths support the closed
root/delegated-form, qualification, measured census and refusal regressions
listed in the ratified policy. Newly necessary unlisted files still need their
own exact independently reviewed amendment; the delegate cannot expand the
root policy or its numeric/financial/target boundary.

The human-root record is authority for qualifying the mechanism and conditional
landings, not acceptance of the new E outputs. Original accepted controls stay
immutable and independently usable. New actual source and operating outputs
remain unaccepted until the qualified mechanism verifies them.

### Reviewed attestor test refinement

Codex recorded the independently reviewed C-01 source-scope decision at 2026-11-17T10:18:51.198109+00:00
under the genuine human root, as preserved in the owning attestor-test-scope.md
record at 052ec0d4fd963dbd4f6c4b8e8054b9805f08dded. It adds only the one
T010 test_delegated_evidence.py path and a fourth mandatory measured current
source suite. All original suites, historical readers, task dependencies and
commands remain. This source permission is distinct from pending output
acceptance and qualified producer activation.

## T015 one-file Ops source-custody scope

The independently reviewed scope bodies apply to the existing private
Ops repository with ID 1284702188 and the single designated archive
file. C-01 limits the parent permission to that file. C-08 retains
Brett Heap as source custodian under existing repository permissions
and project-lifetime retention. Current access controls and original
source observations remain unchanged.

evidence/private-connectivity-production/T015-source-custody.json

- C-01 canonical body SHA-256: d22e859c9ab379c4e60b089dc75ed4cd7a79b41285747feaae426b8b81e25b98.
- C-08 canonical body SHA-256: d997309a3c2d28e6fbb941856889e238beaac93ce7cb9c07c15ba58e84ca2ecc.
- Exact source-scope review input SHA-256: 33b963e03540fd6e511a4a24362b518c9e3f693829a6b59c09e1a0a0a386bd1b.
- Independent scope review SHA-256: 450b601d74261b036267c19c98e24a1109ef3bd09a8404aecb8dc809f106b270.

This record binds the reviewed bodies into the successor definition.
Codex records the scope review under the finite human-root delegation.
The Ops owner must separately qualify both exact source decisions under
the successor and obtain review of the actual destination bytes before
the archive write. T015 consumes only the immutable external custody
reference and retains its coordinator-only files and T010 prerequisite.
Neither the scope review nor these source records authorize runtime.
