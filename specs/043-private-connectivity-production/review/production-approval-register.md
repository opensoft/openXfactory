# Production approval preparation register

Status: draft
Kind: review-packet
Prepared: 2026-11-14

This is a review index for the remaining owner and operating decisions. It does not replace the frozen task contract, authenticate unseen output or advance a gate. The sole implementation list is [043 tasks](../tasks.md); T001–T010 are complete, while full Q0 remains pending. Brett accepted the five exact component source scopes and source-only custody on 2026-11-14; their consumed operating choices and actual evidence remain required for T011–T015. All three PRs remain draft.

## Prepared source decisions

| Owner | Reviewable scope | State |
| --- | --- | --- |
| E | [Accepted evidence commissioning](../../../openspec/changes/commission-private-connectivity-production-evidence/design.md) | Accepted at T006; T007-T010 complete after actual source authentication and successful required CI |
| E amendment | [Exact source-only bootstrap records and T010 refinement](../../../openspec/changes/amend-private-connectivity-evidence-bootstrap/design.md) | Ratified 2026-11-14; exact refinement realized; actual source/CI packet authenticated and T010 verified |
| Neutral publication | [Exact neutral publication and release scope](../../../openspec/changes/publish-private-connectivity-production-contract/design.md) | Brett accepted as neutral publication/release owner; exact scope ratified 2026-11-14; T016 and actual cut remain pending, with no version allocated |
| L | [Supported Headscale package](../../../openspec/changes/commission-headscale-production/design.md) | Brett Heap accepted as source/package/release owner and source-evidence custodian; exact scope ratified 2026-11-14; T011 remains pending |
| I | [Local and managed installer](../../../openspec/changes/commission-connectivity-installer-production/design.md) | Brett Heap accepted as installer source/release owner and source-evidence custodian; exact scope ratified 2026-11-14; T012 remains pending |
| H | [Standalone hosted service and hosted-factory product](../../../openspec/changes/commission-hosted-headscale-production/design.md) | Brett Heap accepted as hosted-product source/release owner and source-evidence custodian; exact scope ratified 2026-11-14; T013 remains pending |
| D | [Actual hosted MCP domain/profile](../../../openspec/changes/commission-hosted-domain-production/design.md) | Brett Heap accepted as domain/profile source/release owner and source-evidence custodian; coordinating and [owner-local PR #583](https://github.com/codeXfactory/codeXfactory/pull/583) source scopes ratified; T014 remains pending |
| O | [Current-authority execution, recovery and operations](../../../openspec/changes/commission-connectivity-operations-production/design.md) | Brett Heap accepted as Ops source/release owner and source-evidence custodian; coordinating and [owner-local PR #628](https://github.com/opensoft/opsXfactory/pull/628) source scopes ratified; T015 remains pending |

Source consent is recorded in each component packet's review/ratification.md before T010, but does not complete T011–T016 without their dependencies and actual authenticated outputs. Proposed task-file refinements must be reconciled into the reviewed freeze before use. Source approval does not create target credentials, paid resources, enrollment, customer eligibility or an automatic merge grant.

## Operating decisions still to consume

The [frozen decisions register](../commissioning.md), [task evidence contract](../contracts/task-evidence.md) and individual gate requirements remain authoritative.

| Decision | Preparation direction or actual gap | Acceptance boundary |
| --- | --- | --- |
| C-01 | Exact named E/L/I/H/D/O and neutral scopes above | Actual owner acceptance and required refreeze before source consumers; no approval inferred from drafting |
| C-02 | Inspect existing Azure QA in West US and production in Central US; real MCP workload and Linux Docker with Windows/macOS/Linux clients proposed | Exact provider/subscription/target/residency/domain/platform identities still require acceptance |
| C-03 | Existing Ops accepted-request/channel and request-scoped grant lifecycle | Each bounded preparation/staging/canary operation needs current target authority; source ratification is insufficient |
| C-04 | Reuse suitable Opensoft services; QA has an observed two-ready-replica Keycloak service at keycloak.opensoft.dev and a Ready letsencrypt-prod issuer | Exact realms/clients/audiences, entitlement and current-revocation sources, DNS/TLS/relay services and accountable owners remain unaccepted; public DNS nameservers do not establish Azure DNS authority |
| C-05 | Proposed supported released Headscale/package/client/service/workload/profile matrix | Exact immutable compatible content and distribution choices require owner review and actual release/readback; an upstream candidate is not qualified |
| C-06 | Availability/error, capacity/spend, revocation, backup/data-loss, recovery/rollback and observation objectives | Exact finite numeric bounds, units, event anchors, sampling, allowed gaps and minimum observed windows require owner approval before Q1; production objectives are confirmed at Q3 |
| C-07 | Existing QA capacity, two synthetic customer boundaries and synthetic data; USD 10 storage-only financial envelope accepted, with provisioning still gated | No available dedicated persistent volume or qualified Mac target identified; numeric resources/objectives/faults/window/cleanup require a concrete approved envelope |
| C-08 | Source-only reviewed/redacted Git policy accepted for E; matching component source custody accepted 2026-11-14 | Protected live/customer/provider custody, retention, access, original output authentication and custodian decisions remain separate |
| C-09 | Internal Opensoft canary first | Exact offering/site/customer/candidate/targets, finite observation/rollback bounds and current authority must be accepted before each activation |
| C-10 | Q4 acceptance follows actual observation | Human acceptance of unseen results cannot be recorded now; gaps, incidents and affected-owner reviews remain mandatory |
| C-11 | Then one named customer per offering proposed | Actual named offer/customer, commercial terms, support and eligible scope need their own decision; no paid launch or eligibility inferred |
| C-12 | Gated expansion after admitted offers | Every wave requires exact bounds and authority; a canary or another offering supplies no inherited pass |
| C-13 | Failure-dependent containment and resumption | Preserve failed attempts, current revocations and neighbors; actual remediation/reruns and fresh affected authority before resume |

The operating rows are preparation status, not approved acceptance inputs. Actual result-dependent Q2/Q4 sign-offs and incident/resume decisions must remain later reviews. Missing storage, platforms, identity or custody does not permit weakening durability, substituting a lab result or skipping an offering/platform.

## Current infrastructure questions

The [operating service candidates](operating-service-candidates.md) record current Azure/OIDC candidates, the real MCP signing compatibility gap, identity-versus-authority constraints and remaining DNS/TLS/relay/custody choices. These are preparation inputs, not accepted operating decisions.

All 23 observed QA persistent volumes are Bound, and the inspected QA node resource group reports no unattached disk. No dedicated available service volume has been identified. Brett approved preparing a minimal dedicated-storage budget for review on 2026-11-14. He subsequently approved the exact USD 10 storage-only financial envelope at the reviewed packet. Provisioning, protected custody, execution and Q1 remain unaccepted; no Azure resource was created.

Brett approved investigating GitHub macOS runners within included capacity, with paid overages prohibited, on 2026-11-14. The investigation must establish exact runner/image/architecture, current allowance and an effective zero-overage stop before a bounded job can be proposed. No runner job, enrollment or live test is authorized by this preparation choice.

The [storage budget for review](staging-storage-budget.md) proposes a USD 10 storage-only ceiling for a bounded 14-day QA run with separately reserved retained capacity. The [Mac runner packet](macos-runner-options.md) proposes standard macos-15 arm64/Intel clients, finite job limits and an exact repository-scoped USD 0 actions_macos hard budget. Brett accepted the storage financial envelope and separately authorized the exact one-time billing-owner guard action. The repository-scoped USD 0 actions_macos guard was created and independently read back, with all four existing budgets unchanged. The organization-wide guard still permits positive paid spend; the new repository guard supplies the tighter Mac constraint. No runner job or Azure provisioning is authorized by those decisions.

## Decisions supplied on 2026-11-14

Brett selected: "Prepare a minimal dedicated-storage budget for review (Recommended)"; "Investigate GitHub macOS runners within included capacity, with paid overages prohibited (Recommended)"; and "Approve all five roles and ratify the matching source scopes (Recommended)". That answer accepted the five coordinating component packets, matching native Ops/domain packets, exact listed source refinements and private source-only custody. At that point the E bootstrap amendment and neutral publication scope remained pending, and the original 16-input freeze was unchanged. The later decision below accepts those remaining scopes and their reconciled freeze. T010 was incomplete at that earlier decision.

## Financial and Mac guard decisions supplied later on 2026-11-14

Brett reviewed the exact packets at the immutable source linked within each and answered: "Approve the USD 10 financial envelope (Recommended)" and "Approve the one-time zero-paid Mac guard (Recommended)". The first accepts only the bounded QA storage financial envelope. The second authorized a one-time direct billing-owner exception outside the Ops workflow's billing prohibition; the existing authenticated active owner session created the exact repository actions_macos budget and verified amount 0/prevent_further_usage true. Other budgets were preserved. No ongoing factory billing authority, target credential, runner dispatch, enrollment, Azure provisioning, Q1 or production permission follows. The source-only bootstrap amendment and neutral publication scope were still unratified at that earlier financial decision; their later acceptance is recorded below.

## E bootstrap and neutral publication decisions

Brett explicitly ratified both remaining proposals, accepted the neutral publication/release-owner role for the exact scope, and directed continuation in dependency order with all three PRs draft and Q0-Q5 honored. Their ratification records preserve the reviewed source and actual supplied instruction. The accepted exact task-file refinements are reconciled into the new review freeze. Actual bootstrap/source/CI authentication remained a separate required review; neither T010 nor T016 completed from consent alone. The later actual authentication below completes T010 after verification.

## Source bridge preparation after ratification

The accepted contained-object reader, original-output provenance checks and exact
commissioning-path inventory are implemented. Source commands are repeated at
their committed revisions; the original imports and failed development or
prerequisite observations remain inspectable. Real source pins are retained
under their computed published refs, without changing the observations. The
required shared suite also checks inventories in the actual committed data.

The exact-head GitHub Codex review identified an offer/wave ordering defect.
Its source repair requires offer completion and any separate actual admission
before wave execution, with red regressions and a passing admission control.
The affected source suites pass 287 verifier and 40 inventory tests; the shared
pin/sentinel suite passes 175 tests. Required GitHub CI for the final source is
tracked independently and cannot be inferred from these local runs.

Brett supplied actual [custodian authentication](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) at 2026-11-14T15:55:48.576Z for the exact reviewed manifest/core. The accepted review is bound at [authenticated anchor de9637eb7](https://github.com/opensoft/openXfactory/blob/de9637eb7215f2f11b98bd7a874420c8692d03aa/specs/043-private-connectivity-production/evidence/commissioning.json), with the reviewed core SHA-256 unchanged at 0645f3e7f31b9b4c708c94b8ff2298fe530b0d18928355201d9f54cab60b770f. The default T010 verification command passes against that independent anchor, and T010 is complete.

Required source CI passed at c4e70f66d, with actual run 43608762372/job 132489023068 and explicit 287/40 zero-skip source collection. The separate receipt, reviewed manifest, actual review and authenticated control are different immutable identities. Source data inventory and reachability remain independently checked.

T011-T068, full Q0 and Q1-Q5 remain incomplete. T011-T015 still need their actual consumed support/provider/integration/authority/custody/limit choices; their accepted source roles do not fill those choices. T016's neutral role and scope consent are accepted. Its distinct [actual source-evidence review packet](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md#exact-neutral-review-target) is now prepared, with a new extended control and the original observations preserved at separate immutable identities. Actual authentication and default verification remain due before T016 is checked. The prior authenticated E anchor and completed T010 remain intact.

The [local support candidates](local-support-candidates.md) propose exact first server/client versions, platforms and channels for T011–T012. This is a pending owner choice for source preparation; upstream availability does not establish compatibility or qualification. GUI-capable Mac targets, actual package identities and execution authority remain required before their consuming qualification gates. The accepted zero-paid Mac guard grants no runner dispatch or enrollment. All three PRs remain draft.
