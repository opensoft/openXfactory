# Production approval preparation register

Status: draft
Kind: review-packet
Prepared: 2026-11-14

This is a review index for the remaining owner and operating decisions. It does not replace the frozen task contract, authenticate unseen output or advance a gate. The sole implementation list is [043 tasks](../tasks.md); T001–T012, T016 and T020 are complete, while full Q0 remains pending. Brett accepted the five exact component source scopes and source-only custody on 2026-11-14; their consumed operating choices and actual evidence remain required at their consumers. Coordinator #1310 has landed source-only with all actual post-merge checks passed. The actual T020 packet is authenticated and default-verified; Ops #628, codeXfactory #583, Headscale-Install #2 and the new coordinator evidence PR remain draft.

## Hosted source decision and QA preparation, 2026-11-16

Brett's actual source-choice approval at 22:16:06.872Z is recorded in
[the Hosted commissioning review](../../../openspec/changes/commission-hosted-headscale-production/review/qa-commissioning.md).
The actual T013 source audit passed all three frozen cases and pinned strict
validation; [its new authentication review](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md)
is pending. T013 remains unchecked. The accepted 16 prior source tasks retain
their immutable controls and actual authentication.

The [QA dossier](qa-q1-approval-packet.md) links draft Ops #637 and Tenant #350
for exact source/target scope review. These proposals do not change the 68-task
definition. The [release preflight](release-prerequisites.md) supplies actual
refreshed tests and preview/readback results, with T018/T019/T023 publication
and all live gates still incomplete. Existing component and all preparation
PRs remain draft.

## Current preparation handoff — 2026-11-16

T001-T012, T016 and T020-T022 are complete as authenticated source tasks
(16/68). Coordinator #1327 landed source-only; GitHub recorded #1325 indirectly
merged through its already-contained head. Headscale-Install #2, Ops #628 and
codeXfactory #583 remain open drafts.

Brett approved the exact private Hosted plan and Q0-H source choices at
2026-11-16T22:16:06.872Z. The immutable reviewed private plan is linked from
the [Hosted decision record](../../../openspec/changes/commission-hosted-headscale-production/review/qa-commissioning.md).
Actual T013 source-output authentication/default admission remains due; no
T013 completion or full Q0 pass is inferred from this source decision.

The [release preflight](release-prerequisites.md) and
[QA Q1 dossier](qa-q1-approval-packet.md) prepare the remaining exact decisions.
The private Hosted Services planning PR also remains draft. No target,
resource, identity, DNS, retention or staging operation is authorized.
The earlier tables and chronology below preserve prior handoff states and
must not be treated as current release, draft-state or gate acceptance.

## Earlier source handoff (historical)


| Item | Current state and next acceptance |
| --- | --- |
| T010 E, T016 N, T011 L | Actual packets authenticated, default commands passed and tasks complete; exact historical anchors are recorded below |
| T012 I | Actual installer packet authenticated at 2026-11-14T22:31:50.896Z; default T012/T010/T011/T016 commands passed against accepted control 35e98a276fbd51c7cdfe89203a3eecbff1266f4f, preserving core b34071e4b290a4e5f58e5bb7bce9b2dee0a16cd18b40d51563c0d9f480c28beb |
| T020 package source | [Headscale-Install draft #2](https://github.com/opensoft/Headscale-Install/pull/2) at 9b4c6106633d5d28b777ef00f1d9bd695588efcf has a fresh 45-test source run (19 package regressions, zero skips), green exact-head owner CI and both real coordinator private-proof lanes passed. Brett authenticated manifest 991ebfc0e5/core f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332 at 2026-11-15T21:23:43.887Z. [Accepted actual review](https://github.com/opensoft/openXfactory/blob/dec5161531d71c3cbe41b55e0e7b3c52c91c0bf7/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) and [accepted control](https://github.com/opensoft/openXfactory/blob/c4e380b43e27093a2a3b99264a3fb52a6cf36c21/specs/043-private-connectivity-production/evidence/commissioning.json) passed full default T020 and prerequisite/inventory verification; T020 is complete |
| Private CI/custody scope | [Ratified source-CI extension](../../../openspec/changes/extend-private-connectivity-source-ci/proposal.md) accepts bounded commit-metadata proof in both coordinator CI lanes. Brett authenticated manifest 95abc40b8e and default expanded T010 passed. Subsequent source repairs have independent CI/review observations; the authenticated control is unchanged. The authenticated producer is now available on trusted main at 6e2f829b16275827a0b73308623164fa099a7ae9. Actual new private-proof CI and authentication/default admission remain required |
| T013–T015 / T017 | Concrete consumed provider/domain/integration/operating choices and actual per-owner evidence remain due; full Q0 remains pending |
| Release and Q1–Q5 | Actual cut/publication authority, runtime qualification, target operations and rollout acceptances remain separate and ungranted |

The four source PRs are coordinator #1310, Ops #628, codeXfactory #583 and Headscale-Install #2. On 2026-11-15 Brett authorized preparing only #1310 for source-only landing, marking it ready, requesting the required approval and merging after its check/review prerequisites. All post-merge checks and trusted-base readback passed at 6e2f829b16275827a0b73308623164fa099a7ae9 before the fresh T020 source run. The standing author-owned approval override was used only for missing review after all checks cleared; no independent approval is recorded. Ops #628, codeXfactory #583 and Headscale-Install #2 remain draft. T020's new actual packet has now received separate human authentication and passed default admission; its coordinator evidence PR stays draft. The chronology below preserves earlier preparation states and failed attempts; the current handoff table governs the status reported by this index.

## Prepared source decisions

| Owner | Reviewable scope | State |
| --- | --- | --- |
| E | [Accepted evidence commissioning](../../../openspec/changes/commission-private-connectivity-production-evidence/design.md) | Accepted at T006; T007-T010 complete after actual source authentication and successful required CI |
| E amendment | [Exact source-only bootstrap records and T010 refinement](../../../openspec/changes/amend-private-connectivity-evidence-bootstrap/design.md) | Ratified 2026-11-14; exact refinement realized; actual source/CI packet authenticated and T010 verified |
| Neutral publication | [Exact neutral publication and release scope](../../../openspec/changes/publish-private-connectivity-production-contract/design.md) | Brett accepted as neutral publication/release owner; exact scope ratified 2026-11-14; T016 complete after actual neutral source authentication/default verification; actual cut pending, with no version allocated |
| L | [Supported Headscale package](../../../openspec/changes/commission-headscale-production/design.md) | Brett Heap accepted as source/package/release owner and source-evidence custodian; exact scope ratified 2026-11-14; T011 complete after actual corrected source authentication/default verification |
| I | [Local and managed installer](../../../openspec/changes/commission-connectivity-installer-production/design.md) | Brett Heap accepted as installer source/release owner and source-evidence custodian; exact scope ratified 2026-11-14; T012 complete after actual source authentication/default verification |
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

Brett supplied actual [custodian authentication](https://github.com/opensoft/openXfactory/blob/73a8be34dcabc0b2d9b3329ca07be0708027b7b3/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) at 2026-11-14T15:55:48.576Z for the exact reviewed manifest/core. The accepted review is bound at [authenticated anchor de9637eb7](https://github.com/opensoft/openXfactory/blob/de9637eb7215f2f11b98bd7a874420c8692d03aa/specs/043-private-connectivity-production/evidence/commissioning.json), with the reviewed core SHA-256 unchanged at 0645f3e7f31b9b4c708c94b8ff2298fe530b0d18928355201d9f54cab60b770f. The default T010 verification command passes against that independent anchor, and T010 is complete.

Required source CI passed at c4e70f66d, with actual run 43608762372/job 132489023068 and explicit 287/40 zero-skip source collection. The separate receipt, reviewed manifest, actual review and authenticated control are different immutable identities. Source data inventory and reachability remain independently checked.

At the neutral handoff, T011–T015 and T017–T068 were incomplete. T016 completed after Brett authenticated the exact neutral source packet at 2026-11-14T16:57:52.719Z and the default T016/T010 commands passed against [accepted control efafaf9b6](https://github.com/opensoft/openXfactory/blob/efafaf9b6edb02166d2ee3bc445741f681f7b59a/specs/043-private-connectivity-production/evidence/commissioning.json). Its reviewed content SHA-256 remains 2f168946e83e9f272ff440754630e1fbfd44b3b0b295b72ca7a30d226ecb2b93. Prior accepted E objects and the historical E anchor remain unchanged. No version, tag or pin was allocated or advanced.

Brett also accepted the exact [local qualification candidates](local-support-candidates.md) at the same actual input. That records a C-05 source-preparation choice; it does not authenticate unseen local test output or establish compatibility. The package and installer packets retain the consumed choice and their remaining prerequisites. GUI-capable Mac targets, actual immutable artifact identities and current execution authority remain required before their qualification consumers. At that handoff the installer's own Python/package channel was unselected; the later actual decision below selects it separately from the Tailscale MSI/PKG/Debian channels.

The current affected regression run passed 593 tests (327 feature source and 266 shared pin/shape/sentinel tests), with zero skips or failures. Three tarfile deprecation warnings are preserved. The 125 proposal-governance regressions and pinned strict validation of all three E/N proposals passed. Current-head CI and Codex review remain independent. All three PRs remain draft.

## Package acceptance preparation after the matrix decision

T011's actual read-only source command passed at cd13fe4bc03a050d3ad2169b3795e05a3a8bf24d. It independently checked ratified owner/origin, the accepted design against all four frozen package-task scopes, the actual support choice and consumed source-only custody/limits. Its [exact package review packet](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md#exact-package-review-target) retained the original source/output and later new receipt separately. Authentication/default verification were still due at preparation and were subsequently supplied below. Earlier accepted E/N controls remain usable; a newly extended pending control does not revoke them.

The first candidate's real committed data measured 1103 standing sites across 35 members, without an uncovered site. Its command was subsequently refused by the unchanged self-verification guard; it supplies no admitted dependency. The corrected candidate retains that refusal and failed direct-parser development output, with a successful direct-text rerun at unchanged source. Its final committed census is measured separately. No foreign production member is populated and no standing obligation is converted to rolling.

The separately prepared [installer runtime/distribution choice](../../../openspec/changes/commission-connectivity-installer-production/review/distribution-candidates.md) proposed the isolated Ubuntu/CPython CLI and private owner-release/offline artifact channel for internal qualification only. The later actual decision below accepts this input. The Tailscale client channels remain distinct. No installer artifact publication or public/customer delivery is authorized by preparation.

The corrected T011 control was prepared at [1ce855daa](https://github.com/opensoft/openXfactory/blob/1ce855daae8d8f88d8e2fe663a87714f17836799/specs/043-private-connectivity-production/evidence/commissioning.json), with content SHA-256 18f3642fafcd12ca5bd9d4a74cdce97377ffdcd3f2d35004a4f64c2c1f0b30c6. Its unchanged-source direct-text check passed at 17:14:32–17:14:35 UTC; the receipt preserves the original self-verification refusal, failed direct parser and absent-coverage wrapper refusal. Source-only coverage is explicitly null. That committed packet measured 1118 standing sites across 35 members with no uncovered site. Source/case/original-provenance/artifact/dependency-order preparation passed before the actual authentication/default admission recorded below. The verifier and its guards were unchanged.

## Package authentication and installer channel acceptance

Brett authenticated the exact corrected T011 source packet at 2026-11-14T17:25:29.544Z. Its [actual review 88b7fecb4](https://github.com/opensoft/openXfactory/blob/88b7fecb41753e466c2555c8bdd6ed45902a8c2e/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) is bound in [accepted control 76517519c](https://github.com/opensoft/openXfactory/blob/76517519c4adf3372ff779bab40b6ab1a432ec0a/specs/043-private-connectivity-production/evidence/commissioning.json), preserving content SHA-256 18f3642fafcd12ca5bd9d4a74cdce97377ffdcd3f2d35004a4f64c2c1f0b30c6. Default T011, T010 and T016 commands pass. T011 is complete, and T020's package source dependency is satisfied; actual package implementation/release/qualification remains separate.

The same actual input accepted the exact internal installer runtime/channel/names in the reviewed distribution packet. This is a consumed T012 source/qualification choice, not actual output authentication, artifact publication, installation or customer delivery. T012's actual acceptance evidence remains due.

Current task completion is T001–T011 and T016. T012–T015 and T017–T068, full Q0 and Q1–Q5 remain pending. All three current PRs remain draft. The accepted package source scope may now progress in dependency order without a target execution or release grant.

## Installer acceptance preparation

T012's actual source check passed at 81a84b5e00e1873737a1e2b0d3b381b9253ffaa6 after checking the consumed internal runtime/channel choice, exact frozen source scope and actual exclusions in the ratified proposal. The distinct original output and later receipt preserve the first failed assertion and successful unchanged-source rerun. Its new control is prepared for actual authentication and default verification; T012 remains unchecked. Prior E/N/L accepted anchors remain usable and T020 may progress under its already satisfied source dependencies.

The prepared installer control is [9672e1b82](https://github.com/opensoft/openXfactory/blob/9672e1b8219ca30f5add1349a968ebeedd742fd4/specs/043-private-connectivity-production/evidence/commissioning.json), core SHA-256 b34071e4b290a4e5f58e5bb7bce9b2dee0a16cd18b40d51563c0d9f480c28beb. Actual original/receipt identities are separate. Source/cases/original-authority/provenance/artifact/dependency-order preparation passes; final data measure 1167 standing sites/35 members with no uncovered site. T012 remains pending actual authentication/default verification. No foreign production site is populated.

## Installer authentication and source-CI scope acceptance

Brett authenticated the actual T012 packet and separately ratified the exact private-source CI/custody/file/refreeze scope at 2026-11-14T22:31:50.896Z. Actual review 9af6e00e7 and accepted control 35e98a276fbd51c7cdfe89203a3eecbff1266f4f preserve the reviewed installer core. Default T012/T010/T011/T016 commands pass. T012 is complete; the preceding installer preparation paragraphs preserve their earlier pending state.

The original coordinator head 22f60937adee1c3563b8113f28a6c0de4cb11630 completed all 14 reported CI checks successfully, including pytest-suite run 43634538945/job 132568331325, and had an exact-head Codex no-major-issues receipt. These actual results do not qualify subsequent source changes. All four PRs remain draft. The new CI refinement must preserve historical accepted readers/anchors, qualify its actual producer and obtain separate output authentication. T020 remains unchecked; full Q0 and Q1–Q5 remain pending.


## Historical source-CI qualification packet (withdrawn)

The accepted source-CI implementation is qualified at 746e9316cfe7dbed7fac3ecc0104fb5bfdec15a7: 298 evidence, 40 inventory and 42 proof-root cases passed in required CI, and Python 3.14 independently passed all 42 proof cases. Both entry points and the exact-head Codex review passed. The failed first Python 3.14 run is preserved; its URL-rewrite fixture assumption was reproduced and corrected without changing the stored origin or weakening a guard.

The new pending control is 02be87d2bdd40abb92f3f232d84f667b661aa10e, file SHA-256 8b18f3ef78031e2d7cb2fd4060e141f05fa8daf4275762ff5441c461914c9b43, core c49a6a5ec2dfab98d76a9dd407afbcc4d0eabb0e7acfc0151083f63b03e1e854. Its [exact authentication packet](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md#exact-source-ci-review-target) separates original output, later receipt, control and actual review identities. Actual E output is retained verbatim as a decoded object in the permitted source container and by its original immutable Git reference. Preparation passes; default T010 admission remains pending actual custodian authentication.

The committed population is 1245 standing sites/36 members with zero uncovered sites. Exact retention refs are published/read back; earlier refs remain. No foreign record is introduced and its population remains FUTURE. The previous accepted installer anchor remains valid. These records authenticate no new T020 run or live result. The producer and original public Git proof must be available from the authenticated trusted base before private preparation. All four PRs remain draft; full Q0 and Q1–Q5 remain pending.

## Corrected source-CI authentication and expanded T010 completion

Brett authenticated reviewed manifest 95abc40b8e and core c8be9c1d56f7fd7dbbaca5ca4c3f416ae03f7e1855722fb4aa0e54e5a6f3ef54 at 2026-11-15T11:47:39.004Z. The [actual authentication record](../../../openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md#actual-custodian-decision) records his exact native input, timestamp, session/line and individual raw-record digest, separately from scope/role/definition ratification. Accepted review 24c3292df is bound by control 698bf8367 with that reviewed core unchanged. Default expanded T010, receipt/control inventory checks and historical T011/T012/T016 verification pass against the independent accepted control before completion is recorded.

Qualified implementation source 94caf6717e passed root/Sonar run 43682139006 and Python 3.14/doc-health run 43682138887: 584 feature cases, including 69 proof cases, with no feature-suite skips. All 723 affected local regressions and the 330 packet/inventory/governance checks passed. The prepared packet head 2d1d816490 completed all 15 reported checks and fresh Codex review before this actual authentication. Source and packet changes remain separately identifiable; these results do not claim CI for subsequent commits.

Expanded T010 is now complete. The earlier c49a6a5e and d37b1834 targets remain withdrawn immutable history, including all actual successful and failed observations. T001-T009/T011/T012/T016 retain their historical accepted anchors; total completed task IDs remain 13. No private binding is introduced. All four PRs remain draft; T020, full Q0, Q1-Q5, protected provider/customer custody, source promotion/landing, version/tag allocation, publication, deployment, enrollment, paid resources and commercial acceptance retain separate gates.

## Subsequent source review repair

Codex's review of the authentication/status head identified a missing T050 preparation-decision floor. The [review finding](https://github.com/opensoft/openXfactory/pull/1310#discussion_r4578296440) was reproduced: omitting C-03, C-07 or both from the binding and its authority let staging-preparation evidence pass. The existing accepted E verifier/test surfaces now require both decisions at T050, before Q1. Existing decision validation checks their scope, acceptance and validity over the actual execution window; the new regressions cover both current execution and independently admitted historical evidence.

All 1,021 affected local regressions passed, including 596 feature cases (487 evidence, 40 inventory and 69 source-proof cases), with no skips. Required CI's feature count is increased only by the 12 observed regression cases; other counts, skips and floors are retained. Pinned strict validation of the three affected E proposals and the 263-row corpus-ledger check pass. Default T010/T011/T012/T016 verification, both T010 inventory checks and the full frozen definition pass after the repair.

This later source repair does not alter the authenticated c8 core, its original source/CI outputs, review or accepted control. Brett's actual authentication continues to cover the exact reviewed packet and source 94caf6717e; it supplies no authentication of future outputs. The repair's current-head CI and fresh Codex review remain separate observations. T050 and all later live tasks remain unchecked, full Q0 and Q1-Q5 remain gated, and all four PRs stay draft.

## CI compatibility for heads predating feature 043

The owner-requested T009/T010 implementation repair addresses the remaining [older-head finding](https://github.com/opensoft/openXfactory/pull/1310#discussion_r4576888200). The original literal steps in both CI lanes were reproduced failing on missing feature paths. Both lanes now retain exact-head testing when the feature tree exists. An older head can use the complete merge checkout only when its common ancestor has no feature tree and its subsequent history never changed that tree. Full commit identity, checkout identity, parent ancestry and all three source-suite paths are checked. Partial, removed, previously created-and-removed, unavailable or foreign source inputs are refused. Compatibility runs print the selected revision and explicitly supply no qualification of the older PR head.

All 1,049 affected local regressions passed, including 624 feature cases: 487 evidence, 40 inventory and 97 source-proof cases. The increase is exactly 28 actual selection cases across both workflow definitions; CI's source-proof count moves from 69 to 97, with every other count, skip rule, named verdict, credential boundary and required check retained. Both complete revised workflow steps also passed against an isolated clone with an actual pre-feature parent, a synthetic unrelated head and a real merge commit. Those local executions used CPython 3.12; actual Python 3.14 and current-head CI remain separate qualification observations.

Default T010/T011/T012/T016 verification, both T010 inventory checks, the three pinned strict OpenSpec checks and the 263-row corpus ledger pass. The authenticated c8 core, original source/CI exports, accepted review/control and frozen definition remain unchanged; the previous human authentication supplies no authentication of future outputs. This is an implementation-only source-CI compatibility repair within the accepted files. No further task or rollout gate is completed. All four PRs remain draft; full program Q0 and Q1-Q5, source promotion, release/publication, target execution, deployment, enrollment, spend and commercial acceptance remain separately gated.

## Source-only landing instruction

Brett's current instruction is: "Go ahead and prepare PR #1310 for source-only landing, mark it ready, request the required approval, and merge once checks and approval are satisfied. Verify post-merge CI, then resume T020 and present its actual evidence packet for authentication. Keep the other three PRs draft and honor Q0–Q5."

Landing preparation incorporates current main while preserving the accepted control, actual original outputs, historical source anchors and complete frozen definition. This changes the earlier draft-only restriction for #1310 alone. It grants no new output authentication, task completion, neutral release cut, version/tag, private source publication, target operation, deployment, enrollment, spend or commercial acceptance. The managing source/CI producer must be independently available on the trusted base before a private T020 binding is introduced. Full program Q0 and Q1-Q5 remain pending.

## Actual T020 authentication and default admission — 2026-11-15

Brett authenticated the exact T020 packet at 2026-11-15T21:23:43.887Z after the 1,197 affected local regressions, both actual private-proof CI lanes, Sonar and exact-head Codex review had passed. The accepted authentication record preserves the original user decision, its record digest and the actual public CI run/job observations; private source/output remains exclusively in its private owner Git. The accepted control c4e380b43e27093a2a3b99264a3fb52a6cf36c21, file SHA-256 902903efb19398d014ef2c84acd6afa227c0cc97ee4df87f5d9cecf56fd29816, preserves core f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332. No source_container, historical binding, original receipt or complete task definition changed.

The full default T020 command passed after that actual decision, using the independently pinned control and the actual private owner Git root. Default T010/T011/T012/T016 and exact commissioning/T020 inventories also passed. T020 is checked only after these passes; current completed total is 14 of 68. T021/T022 may proceed as the next local source tasks under their already accepted exact scopes. The separately ratified register-private-connectivity-release-members scope may now prepare its bounded definition refinement with this accepted historical control fixed before any refresh. Its changed E source/CI outputs still need separate actual authentication before use.

No supported version, cut, tag, deployment, live host, enrollment, paid execution, full Q0, Q1-Q5 or commercial acceptance is supplied by this decision. All source PRs remain draft. The earlier chronology retains the observations and pending boundaries that applied at each earlier point.
