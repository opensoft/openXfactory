# Planned task evidence and execution binding

Status: draft
Created: 2026-11-13
Feature: [043-private-connectivity-production](../spec.md)

This supplements [qualification evidence](qualification-evidence.md) and [owner handoff](owner-handoff.md). It is a draft implementation design, not a published schema, deployment request kind, executable verifier or approval. The only executable task list is [tasks.md](../tasks.md); the registry below is an acceptance contract with no actions or completion checkboxes.

The reviewed T005 packet identified the [E evidence scope](../../../openspec/changes/commission-private-connectivity-production-evidence/proposal.md) for T006 and the separately proposed [neutral publication scope](../../../openspec/changes/publish-private-connectivity-production-contract/proposal.md) for T016, both published in draft PR #1310. E scope and source-only C-08 choices are now accepted in the [T006 ratification record](../../../openspec/changes/commission-private-connectivity-production-evidence/review/ratification.md); the [bootstrap amendment](../../../openspec/changes/amend-private-connectivity-evidence-bootstrap/review/ratification.md), five component source scopes/native packets and [neutral publication owner/scope](../../../openspec/changes/publish-private-connectivity-production-contract/review/ratification.md) are now ratified. Exact source-file refinements are reconciled in the current freeze; actual task evidence and consumed choices remain separate. The review freeze identifies the task contract, while the actual owner decision supplies authority.

## Bootstrap and verifier availability

T001–T006 use their listed existing tools/inline checks. T002 stores only a historical-lab content digest and production-authority=false, not a supported release pin or new runtime grant. T003/T004 draft specific governance packets; strict validation cannot ratify them. T006 requires a real named-owner acceptance, approved origin metadata, a cited ratification record under the evidence proposal and the C-08 custody/authentication choices consumed by E. Neither generated text nor a structural command invents human consent.

Only accepted E scope permits T007/T008 implementation, T009 narrow shared registration and T010 required-CI wiring. T007 provides the planned command shape:

    python3 specs/043-private-connectivity-production/verify-evidence.py --task TNNN specs/043-private-connectivity-production/evidence/TNNN.json

TNNN denotes the concrete closed task ID from the table, not a literal file name or open registry. For an external owner, use that task's listed command from its accepted code tree with machine-local PC_COORDINATOR selecting the same verified coordinator. The environment variable must be set; no guessed host path or unverified repository is trusted.

The verifier must not execute owner commands, deployments, probes or providers. It verifies their immutable actual outputs, required case/command/revision identity, current scope/authority, dependencies and measurements. Human/owner review remains necessary to establish that protected outputs and approvals are authentic and support the observed result.

### Bootstrap evidence bridge

T001–T009 do not require new TNNN.json receipts: their listed file scopes contain the original checklist/baseline, governance packets and source/tests rather than those receipts. Preserve actual command/output/revision identities and original owner approvals as bootstrap evidence. Before importing them at T010, T006 must have accepted the E custody/authentication scope; the custodian then freezes immutable authenticated references to the original artifacts and outputs. Later custody acceptance never retroactively grants an earlier action.

T007 implements a closed adapter for these nine specific tasks. It checks the original task-specific command, required cases and expected outcomes against actual source/governance artifacts, authenticated output and current owner ratification. T007/T008/T009 require their real exact-revision test outputs and exact-scope diffs. Missing provenance, a generic verdict or a fabricated JSON replacement fails import. T010 verifies these dependencies through that adapter and its exact-head CI results, without requiring nonexistent bootstrap receipts or trusting the verifier as its own approving authority. Tasks from T010 onward use their listed receipts; no new pin-bearing bootstrap JSON is published before T009 registration.

### Accepted source-only container

The exact coordinator commissioning path is specs/043-private-connectivity-production/evidence/commissioning.json. Its operator-supplied independent trust anchor remains its complete Git commit/path/SHA-256. A closed contained-object reference carries only an opaque object identity; it resolves solely inside that anchored object table. Unique JSON/object keys, existence and acyclic references are mandatory. Original source/governance artifacts remain exact Git references. Tested source, output, receipt and manifest identities stay distinct, with no self-containing receipt hash.

Contained data is limited to E bootstrap/source/CI material; it cannot satisfy provider/customer/staging/production proof through a changed class or scope. Original output, command/source/exit/time identities and redaction provenance remain inspectable. The exact commissioning-authentication.md record under the E proposal remains draft until Brett reviews the actual immutable exports and human provenance. Scope ratification does not authenticate those outputs.

T010 owns the complete accepted six-file first-record transition in tasks.md. Add only the exact commissioning JSON to existing closed production pin paths. Empty members remain FUTURE until actual committed sites exist; promote and measure only their actual population, preserving local/foreign reachability, all unknown-path refusals and 040 behavior. Accepted observations remain immutable; a corrected commissioning control is a new reviewed revision preserving prior history.

### Accepted private source CI proof

The ratified extend-private-connectivity-source-ci scope adds exactly the feature's prepare-source-roots.py and tests/test_source_roots.py to T009 and the existing doc-health-py314 workflow to T010. Both existing CI jobs prepare independent fixed-owner commit-metadata roots before inventory checks; no private source tree is published. PC_SOURCE_PROOF_ROOTS is an explicit CI metadata map, distinct from PC_EVIDENCE_ROOTS for full source/task admission. Missing credentials, reviewed producer provenance, owner identity or required commits fail closed. Credentialed code comes only from an authenticated producer selected by the trusted base, never an unreviewed PR script; credentials are revoked before tests and temporary proof is removed afterwards.

Temporary commit presence cannot authenticate outputs or establish source conformance, a release or Q0–Q5 acceptance. Full actual owner Git stores, immutable source/artifact/dependency verification and separate custodian authentication remain mandatory. Historical accepted packets retain their matching frozen definitions, immutable readers and anchors; the new definition does not rewrite or retroactively authenticate their observations. The bounded compatibility bridge accepts only the fixed previously authenticated control/reader content identities and verifies current authority as well as historical evidence. Caller-selected definitions/readers remain refused.

## Owner, file and command binding

C-01 freezes the actual canonical repository/worktree/revision, exact per-task file allowlist, approved owner command and required-case definitions before runtime work. The task's candidate file envelope is an additional upper bound, not a permission grant. Validate the strict intersection and fail if a diff, selected domain layout or needed file falls outside it; replan before expanding scope.

One task writes one owner tree. From T010 onward its acceptance receipt is in that tree: coordinator feature evidence/TNNN.json or external-owner evidence/private-connectivity-production/TNNN.json. T001–T009 use the closed bootstrap bridge above. Source implementation must run the approved owner suite and retain red/green regression identity and exact collected CI results; passing a generic or uncollected suite is insufficient.

The exact E/N/L/I/H/D/O source layouts are now accepted through their named packets and reconciled file fields. T011–T016 must still establish actual authenticated acceptance after T010 and their consumed choices. If an owner requires another canonical governance store or layout, revise the precise task/file scope before writing. No production domain/provider/platform is selected by the aliases.

## Record and instance semantics

For tasks using the new verifier, require task ID, owner alias/canonical repository, evidence class, scope/candidate/profile and attempt references, current decision/authority references, closed required cases with expected/observed subchecks, actual approved command and exit/result, immutable protected output and revision/content references, timestamps/event anchors, limit decisions and incident/sign-off links as applicable.

Only genuine pass for the required dependency scope satisfies a dependency. Fail and blocked outcomes remain preserved, not converted to pass for missing input. Source/CI, supported publication, commissioning, target readback, staging, production and commercial decisions are distinct classes. A draft, lab or wrong-scope record cannot substitute for the required class.

Final receipts may reference several immutable per-offering/attempt child records, each validated against its own accepted scope, candidate, matrix and decision. No flattened cross-customer/profile/candidate aggregate can manufacture a pass. Each commissioned required instance must have its applicable observations and acceptance; missing instances remain blocked/ineligible.

Failed/blocked attempts and their remediation are immutable in C-08 custody. The acceptance receipt links the completed attempt and history; do not overwrite an accepted observation. Later changes/waves create distinct protected attempts and renewed gate/authority records. A checked task is historical completion, not continuing or cross-scope permission.

### Per-instance Q3–Q5 dependencies

T057–T064 have a scoped child DAG as well as their aggregate completion DAG. C-01/C-09/C-11/C-12 freeze the required first-offering/site/profile/candidate and offer/wave instance identities and their applicable dependencies before use. Store immutable redacted child references in each task's listed instances/TNNN/ area, intersected with its exact accepted C-01 file list. New attempts get new identities; an accepted child is never rewritten.

T007 must support the planned read-only shape verify-evidence.py --task TNNN --instance INSTANCE_ID CHILD_RECORD. It validates a child against that frozen instance manifest and the correctly scoped accepted child predecessors. A missing parent aggregate does not block a genuinely passed predecessor child for the same approved scope. No child can consume another offering's pass, bypass the complete program Q2 at T056, skip managed-service eligibility for the same phase/scope, or acquire a later wave's authority. A new commercial offer uses its C-11 decision; a wave additionally uses its own C-12 decision. The corresponding offer must already be admitted before a wave can execute.

The verify command listed on each task checks the final aggregate receipt against all required commissioned children. Only that complete check permits marking the task checkbox. Until then the task remains unchecked while individually verified, approved children may advance through their own DAG on independent track/site schedules. T065 and later handoff tasks require aggregate completion. Additional waves and material changes remain new governed instances/refinements, never permission inferred from a checked aggregate.

### Final candidate closure before target preparation

T049 joins the completed component releases after T041 and the operational release at T048. C-05 must close the exact consumer/service/profile/harness matrix and retain actual final-candidate source integration and collected CI results. This is source/interface/release validation; it authorizes no provider call, deployment or live probe and cannot replace Q2 intended-platform observations. Multiple service variants are acceptable only if each actual path and consumer pin is explicitly supported and tested; an earlier release receipt alone cannot establish compatibility with a later service revision. Stale pins, changed harnesses, unsupported combinations or needed owner edits block T049 and therefore T050/Q1. Refine the exact owner tasks/scopes, republish/reverify affected releases and refresh the closure before any staging target preparation; do not repair source during observed qualification.

## Frozen acceptance registry

These cases are identifiers for the detailed outcomes in the task descriptions, [validation matrix](../validation-matrix.md), [policy coverage](../policy-coverage.md) and [qualification evidence rules](qualification-evidence.md). T005 reviews the registry; T006 accepts its runtime implementation scope. T007 must freeze actual expected outcomes and class/scope/command/dependency checks in reviewed code, not accept arbitrary caller cases or verdicts.

| Task | Owner | Required evidence / decision class | Dependencies | Required case IDs |
| --- | --- | --- | --- | --- |
| T001 | C | setup | none | feature-context, prior-work-preserved |
| T002 | C | historical-source | T001 | historical-lab-only, content-identity, no-production-grant |
| T003 | C | governance-draft | T001, T002 | exact-evidence-scope, shared-reader-scope, publication-index |
| T004 | C | governance-draft | T003 | neutral-publication-scope, atomic-release-process, publication-index |
| T005 | C | design-freeze | T003, T004 | closed-task-registry, complete-coverage, no-authority-by-draft |
| T006 | C | Q0-E | T005 | actual-owner-acceptance, exact-partial-scope, no-live-grant |
| T007 | C | source-E | T006 | frozen-cases, class-scope-dependencies, limits-authority-rejection, read-only-verifier |
| T008 | C | source-E | T006 | exact-043-inventory, owner-reachability, read-only-check-mode |
| T009 | C | source-E | T007, T008 | only-043-coverage, uncovered-path-refusal, census-regressions |
| T010 | C | CI-E | T009 | explicit-suite-collection, exact-head-required-ci, no-skips-or-waivers |
| T011 | C | Q0-L | T010 | package-owner-scope, local-platform-support, consumed-decisions |
| T012 | C | Q0-I | T010 | installer-owner-scope, setup-distribution-scope, no-workstation-intake |
| T013 | C | Q0-H | T010 | actual-provider-platform, identity-entitlement-custody, product-owner-scope |
| T014 | C | Q0-D | T010 | actual-domain-selection, exact-profile-protection-scope, owner-and-inventory-authority |
| T015 | C | Q0-O | T010 | target-channel-custody, operational-owner-scope, explicit-ci-scope |
| T016 | C | Q0-N | T010, T004 | neutral-owner-acceptance, publication-reader-scope, late-version-allocation |
| T017 | C | Q0-program | T011, T012, T013, T014, T015, T016 | all-owner-scopes, consumed-choices-accepted, later-gates-still-pending |
| T018 | C | release-N | T016, T010 | supported-contract, atomic-cut, conformance, publication-authority |
| T019 | C | release-N-verified | T018 | tag-readback, compatible-content-pins, no-pilot-import |
| T020 | L | source-L | T011, T010 | supported-package-foundation, real-release-inputs, lab-preserved |
| T021 | L | source-L | T020 | verified-endpoint, renewal-reachability, no-tls-bypass |
| T022 | L | source-L | T020 | protected-state, fenced-quarantine-restore, current-revocations |
| T023 | L | release-L | T021, T022 | package-ci, supported-artifact, guarded-qualification-command |
| T024 | I | source-I-local | T012, T019, T023 | install-new-existing, unbound-opt-in, published-contract-package-pins |
| T025 | I | source-I-local | T024 | durable-cleanup-subjects, cutover-order, revoked-prior-refusal |
| T026 | I | release-I-local | T025 | accepted-distribution-matrix, local-ci, guarded-local-runner |
| T027 | C | source-local-ready | T019, T023, T026 | local-source-release-chain, independent-customer-operation, live-proof-not-claimed |
| T028 | H | source-H | T013, T019, T023 | actual-provider, dedicated-boundaries, no-docker-fallback |
| T029 | H | source-H | T013, T019 | trusted-identity, actual-entitlement, credential-custody |
| T030 | H | source-H | T028, T029 | restart-durability, original-subjects, current-authorization, concurrency |
| T031 | H | source-H | T030 | standalone-without-factory, scoped-attachments-routes, independent-cancellation |
| T032 | H | source-H-catalog | T013, T019 | strict-production-semantics, trusted-release-authority, no-caller-eligibility |
| T033 | H | release-H-network | T031, T032 | explicit-source-ci, guarded-network-runner, supported-service-release |
| T034 | I | source-I-managed | T012, T026, T033 | actual-service-integration, current-entitlement-attachment, original-retry-scope |
| T035 | I | release-I-managed | T034 | managed-source-ci, guarded-managed-runner, supported-sdk-release |
| T036 | D | source-D | T014, T019 | actual-workload-profile, strict-schema, application-authority |
| T037 | D | CI-D | T036 | exact-definition-protection, required-validation-collected, missing-dependency-fails |
| T038 | D | release-D | T037, T033, T035 | compatible-domain-release, guarded-actual-domain-runner, profile-pins |
| T039 | H | source-H-domain | T038, T035 | trusted-profile-privacy, actual-workload-binding, application-denial, partial-cleanup |
| T040 | H | source-H-domain | T039, T032 | exact-profile-catalog-integration, wrong-scope-refusal, no-premature-eligibility |
| T041 | H | release-H-domain | T040 | domain-capable-service-ci, compatible-pin-set, supported-release |
| T042 | C | source-domain-ready | T038, T041, T035 | actual-domain-source-release-chain, profile-protection-proof, live-proof-not-claimed |
| T043 | O | source-O | T015, T023, T033 | managed-handoff, fenced-recovery, authoritative-revocations |
| T044 | O | source-O | T015, T023, T033 | independent-monitoring, clock-limit-coverage, custody-and-neighbors |
| T045 | O | source-O | T043, T044 | partial-target-revoked, prior-binding-rechecked, rollback-refusal |
| T046 | O | source-O | T045 | bounded-halt-containment, neighbors-preserved, fresh-resume-authority |
| T047 | O | CI-O | T043, T044, T045, T046 | private-suite-collected, required-ci-entrypoint, existing-gates-preserved |
| T048 | O | release-O | T047 | guarded-drill-runner, qualified-operational-pins, support-runbook |
| T049 | C | source-candidate-ready | T017, T019, T027, T035, T042, T048 | operational-source-release-chain, collection-proven, final-consumer-matrix, final-harness-candidate, live-proof-not-claimed |
| T050 | O | Q0-preparation-C03 | T017, T019, T027, T035, T042, T049 | accepted-staging-preparation, bounded-spend-targets, probes-custody-ready |
| T051 | C | Q1 | T050 | complete-current-inputs, immutable-candidate-matrix, scoped-execution, numeric-limits |
| T052 | I | Q2-observation | T051 | new-existing-unbound, real-tls-client-controls, no-hosted-credentials |
| T053 | H | Q2-observation | T051 | standalone-and-local-managed, two-customer-environment-controls, direct-relay-retry-lifetimes |
| T054 | H | Q2-observation | T053 | actual-private-new-existing, qualified-unbound, application-and-public-ingress-denial |
| T055 | O | Q2-observation | T052, T053, T054 | revocation-direct-relay-disconnected, backup-upgrade-fenced-restore, cutover-neighbor-limits |
| T056 | C | Q2 | T052, T053, T054, T055 | four-path-case-union, same-run-candidate, positive-controls, reviewed-incidents |
| T057 | C | Q3 | T056 | separate-canary-decision, customer-consent-bounds, current-target-authority, monitor-support-rollback |
| T058 | O | Q3-activation | T057 | bounded-current-activation, managed-or-customer-authority, observed-readback |
| T059 | O | Q4-observation | T058 | actual-approved-window, coverage-and-gaps, operating-and-application-results |
| T060 | O | Q4-observation | T059 | approved-fault-targets-windows, cleanup-and-neighbors, current-revocations-resume |
| T061 | C | Q4 | T059, T060 | observed-objectives-met, incidents-reviewed-closed, fresh-owner-acceptance |
| T062 | C | Q5-decisions | T061 | named-commercial-offer, separate-bounded-wave, exact-profiles-and-current-owners |
| T063 | H | Q5-admission | T062 | trusted-eligibility, only-named-offer-wave, bounded-admission-readback |
| T064 | C | Q5-change-control | T063 | material-change-invalidates, affected-requalification, fresh-resume-or-wave-authority |
| T065 | C | handoff | T064 | as-built-owner-scopes, current-release-matrix, support-and-incident-handoff |
| T066 | C | landing-audit | T064 | all-owner-landings, reviewed-integrated-pins, required-ci-and-advisory-status |
| T067 | C | governance-handoff | T065, T066 | only-proved-tasks-closed, remaining-promotion-archive-obligations, no-new-live-permission |
| T068 | C | final-validation | T067 | complete-coverage-and-scope, secret-safe-immutable-evidence, no-unresolved-blocker |

## Rejection and publication rules

Reject unknown/duplicate/missing cases, a nonzero/missing owner result, mismatched scope/candidate/profile/customer/environment/run, stale/expired authority, an unapproved changed command, missing exact required CI collection or wrong evidence class. Require actual positive controls for denial cases.

Numeric limits come from current accepted decisions and must be finite and valid for their metric, with real event/clock anchors and monitoring gaps accounted for. No 040 threshold or sign-off list is a production default. A waiver cannot manufacture observation.

Q0 per-owner acceptance permits only its exact preparation/implementation; T017 is the program join. T050 separately needs current staging preparation/spend authority. Q1 then bounds the run; Q2 accepts all four paths; Q3 separately admits each canary; Q4 accepts actually observed scope; Q5 separately admits the named offer/wave. Current managed request/channel-required grant or unmanaged customer authority is always enforced before effects.

Task/registry changes after approval require reviewed scope/contract updates and affected re-verification. New shared pin classes, census, workflow or protected surfaces need their owning authority. Preserve 040, existing validation floors and current revocations; no silently widened prefix, skip, waiver or customer eligibility flag is allowed.



## Private T023 release qualification

Keep the existing three T023 cases and exact verification command. Require the
two exact protected owner CI suite identities and an independently reviewed
zero-spend source result covering all six criteria against the immutable
pre-production baseline. Bind the evaluated summary, independent quality and
hotspot disposition, and authorized release readback to the same source and
immutable CI run/job. Check the exact release tag, artifact digest, provenance
and positive publication readback. A local result, cancelled provider
analysis or unevaluated criterion cannot admit T023. Custody remains under the
source-only decision and downstream pins require the normal verified receipt.

The package input-manifest change is limited to the existing helper digest
field. The release candidate inventory binds the resulting input bytes and the
reviewed executable helper bytes to the same package candidate.

The predecessor continues to select the actual accepted Q0 record until new
E outputs are separately qualified, reviewed, authenticated and selected.
This definition refresh does not activate successor evidence or reopen any
runtime authorization. The exact predecessor control retains its original
definition, reader and SHA-256 anchors.

## Opt-in internal delegated authority

The actual human root is immutable policy a66cfe60 and its genuine recorded
decision d2528306, under the ratified authorize-private-connectivity-internal-production
packet. These abbreviated references identify the reviewed records; executable
trust uses their complete exact repository/commit/path/SHA-256 references.
Human legacy forms and accepted historical readers remain unchanged.

A distinct closed delegated authentication/decision form names Codex as actor,
Brett as accountable owner, the exact known root, actual review time, immutable
candidate/core/output references, qualified producer and independent review.
A separate bounded attestor authenticates actual provider run/job/head/step
readback and actual protected command/output provenance. Generic receipt-written
success, quota responses, arbitrary roots/producers or missing evidence cannot
authenticate a packet. The read-only verifier executes no operator/probe action.
Keep the original private-proof producer and App boundary byte-identical.

First qualify and land the attestor/reader with acceptance inactive. Activate
only the independently reviewed exact protected-base producer afterward; no
caller flag can activate a PR copy. New decisions require the active, unrevoked
thirty-day human root and stay inside its fixed customer/support/target/
financial bounds. Current target/channel grants remain independently required.
Source-only custody never becomes provider/live custody. Actual new E output
authentication is separate from this source-scope amendment.

### Conditional T061 internal aggregate case

The additional aggregate-only case is internal-program-handoff. It applies
only to the selected internal-program endpoint under the fixed human root.
The T061 child registry cases and child dependencies below remain unchanged.
An independently valid child may pass while other canaries remain pending.

For internal-program completion, the T061 aggregate additionally requires the
one exact review/internal-production-handoff.md reference, all three actual
accepted offering children, actual released/integrated required CI and usable
onboarding/monitoring/support/rollback/custody handoff. A child never depends on
the completed aggregate or another offering's future result. The closed reader
must test this child/aggregate distinction. This adjunct cannot satisfy
T062-T068, whose dependencies and external commercial meaning remain unchanged.


### Current T010 attestor regression collection

The independently reviewed source-scope amendment adds only
tests/test_delegated_evidence.py to T010's exact envelope. Current T010 evidence
requires four explicitly collected suites: test_evidence.py,
test_evidence_pins.py, test_source_roots.py and test_delegated_evidence.py.
Every original suite remains mandatory, all measured identities/counts are
checked and no failure/error/skip is permitted. Original accepted human
historical readers retain their original three-suite contract. No task
dependency, verification command, token scope or workflow identity changes.

### T015 reviewed source-custody scope

The owner-scope record binds the exact C-01 and C-08 bodies for the one
private Ops source archive. The source authority and actual new archive
evidence remain separate. T015 retains its original three cases, listed
coordinator files and T010 prerequisite. The Ops archive stays a
read-only external custody input to the coordinator.

Activate this definition only after preserving the original T010
proof, requalifying both source lanes, and independently authenticating
the successor commissioning manifest. Confirm both actual source lanes
used a trusted base selecting that exact successor before the archive
write. The exact owner-local C-01 and C-08 on that definition and review
of the actual private bytes are required before archive custody changes.

## T005 review freeze

### Reviewed T023 successor definition candidate

The exact C-01 acceptance and its L/E scope are recorded in the
[T023 decision record](../../../openspec/changes/qualify-private-headscale-without-sonarcloud/review/t023-c01-scope.md).
Only the T023 file field and the two corresponding definition inputs change.
The successor freeze awaits actual protected E qualification and separate
authentication. The original selected T017/Q0 control remains active.

### Retained T015 successor definition history

Brett's original root approval at 2026-11-17T08:38:55.473Z accepted the exact
T010 attestor and conditional T061 aggregate-only handoff scopes, initial
Windows/Linux support and finite internal delegation. Those historical
decisions retain their original authority, source and time.

For T015 the previous freeze bound two refreshed scope inputs and all 68
unchanged task lines. Registry child cases, owners, classes, file envelopes,
dependencies and verification commands retained their definitions. The
predecessor remained active until the successor commissioning manifest
was independently authenticated, verified by default and selected.

The prior unauthenticated 6b406630 and 4f963e0f source candidates retain their
original observations and are not added as accepted historical controls.
Historical source-scope note, retained without changing its old facts:

> ### Current accepted source-scope definition
>
> The four-path companion-prose refinement was separately accepted at
> 2026-11-17T03:40:50.580Z. The earlier unauthenticated 4f963e0f source candidate
> and its actual passing tests remain observations at their original commits;
> they are not accepted history and are not relabeled as this qualification.
>
> Brett Heap accepted the exact N/E refinement at 2026-11-17T02:55:36.438Z and
> the matching Ops/Tenant owner plans at 2026-11-17T03:01:06.114Z. Only the four
> T018, twenty-one T043 and two T047 source paths and matching owner-scopes.md
> handoff are refined. All 68 registry rows and all other task fields remain
> unchanged. Fifteen input bodies remain byte-identical; only the accepted owner
> handoff input changes. Original freezes, controls, readers and actual accepted
> observations remain immutable at their exact historical source references.

Review packet SHA-256: 1e5d1a03b2d7cfab1bea57d838cbc080bc62b0951661b7508c901b432484ec11

This digest covers canonical UTF-8 JSON keys inputs, registry and tasks,
sorted keys, compact comma/colon separators, ensure_ascii=false and no terminal
newline. All 68 task lines are included with only checkboxes normalized.
Inputs include all sixteen hashes below; this file contributes only its complete
body before the T005 heading. No partial task/input freeze is accepted.

| Input | SHA-256 |
| --- | --- |
| spec.md | c8bebd78c2f1e919874fdf385796557c577d1d55aba2740bc498e906ec274134 |
| plan.md | 2edb9ad4eb75621218dadbeefedf961cdb64221f51d20c84bd281564cefc9818 |
| research.md | 295751853b252eafabbcaf64933a577df88370f7c457f01fe69a479c9df7f9d2 |
| data-model.md | 16a1351ef27a1924be4ce4e1c77197adfc48a40391b3e4ea20d5f849a72c4391 |
| owner-scopes.md | 386e1b1c39f775fafbdab25f9746c08d13066ead9c98939c4b16bdef886bec7d |
| commissioning.md | 8f5917f9bdbee09a8fd6f93bbe53f34b371213196b6e38611a3a6850373f829c |
| rollout-gates.md | 0815198f6c67e4eaf02d18efbd9558821747c8560ed338b626de34f993c9b32d |
| validation-matrix.md | 7ebee6a87bee75ea50ca70d30a64ae50460ef6081a5489dd75d5c83a4f481f53 |
| policy-coverage.md | e30154c88b29ce5a21b23d235d0ec863a105a433d7ea23e7fb6937cba928f37b |
| local-headscale.md | aa764a126e7b1d2c12c257e9d2d1ef2416fb49a47dffeddf93de6a901882c481 |
| standalone-hosted-headscale.md | b25c3d8ab2642912d1dcbe557b51f9820df8986906c3d1ccb950146efd8ee479 |
| hosted-domainxfactories.md | c0b94352f89013a28dbc1008d988e7aca94c58b05511a14f52c9cf81cf2b9cc6 |
| contracts/owner-handoff.md | d8fec9881a390420c41d6bc1dfef8fb44ab35457054611ae3751a8a98ca9fd78 |
| contracts/product-interfaces.md | 5643be4adba7bb0ac5413a1ddb74bab863af981c945d92c4fde14d97fd0d94e7 |
| contracts/qualification-evidence.md | 8d7d4ab79a6bb456a2dabef0d6ec4d5ba40da296e5ba19ceab2c7e907df31e92 |
| contracts/task-evidence.md | d6c679b7d38e6927fcb1d9b8c7d6cb733af4f246c5fae1d63ca970f144703931 |

Source-scope approval does not authenticate new actual E source/CI output.
That separate review/default admission is required before consuming N changes.
T018 remains incomplete; all PRs stay draft and Q0-Q5 remain unentered.

### Historical freeze discussion

The quotation below preserves the prior discussion for context. Its original
bytes and frozen definitions remain governed by the fixed historical controls
and readers; quoted input rows are not the current input table.

> Brett Heap ratified classify-private-connectivity-source-tests at 2026-11-15T01:34:50.899Z. This refinement adds only its three exact shared paths to T010. All 16 frozen input bodies, all 68 registry rows and every other task field retain their previous bytes. The earlier source-CI definition e912507dfe7a136879f786e1ca5ccbdf62556b3f3fc179398af0bd8e730fd298 remains historical; its withdrawn control receives no new authentication. The refreshed definition below permits the accepted source work only. Actual new CI outputs, full Q0 and Q1-Q5 remain separately gated; all four PRs stay draft.
>
> The initial definitions and later T006 acceptance-state freeze remain historical decisions. Original accepted identity: 547e398b615d08186719674774f379038740292e2472488010151a5f03bbba6d. On 2026-11-14 Brett ratified the exact bootstrap amendment, all five component source scopes/native packets and neutral publication scope. The prior source-scope definition 66db63ec98e366f141230d22e6e4e159916bb997f159916159dcc7b6ae3f32d0 remains historical. Brett subsequently ratified extend-private-connectivity-source-ci at 2026-11-14T22:31:50.896Z. This refreshed freeze adds only its T009/T010 files and source-CI custody clarification. All 68 identities, owners, classes, required cases, dependencies and verification commands are preserved. T001–T012 and T016 are complete under their historical authenticated anchors; the additional source-CI refinement is now accepted. Full Q0 remains incomplete.
>
> Review packet SHA-256: c37f19af3ebe6340ce417286d54875f40a201f86e41d22077b676044f7f44431
>
> The digest covers canonical UTF-8 JSON keys inputs, registry and tasks, sorted keys, compact comma/colon separators, ensure_ascii=false and no terminal newline. Tasks are all 68 literal task lines with only checkboxes normalized to unchecked; registry is all 68 literal rows. Inputs contains each SHA-256 below. This file's input is only its complete body before this freeze heading. Footer status and task completion checkboxes do not alter the definition.
>
> | Input | SHA-256 |
> | --- | --- |
> | spec.md | 901ed9fff1c99c088522db9d66786a3550fd5a55c228bc9eb625e150fb470cae |
> | plan.md | 5fc1550dd8988e2d32288176c9f4b62c22592e4c583c8106b506fbe9fd22bdee |
> | research.md | 295751853b252eafabbcaf64933a577df88370f7c457f01fe69a479c9df7f9d2 |
> | data-model.md | a2201bc094da3a05567194cbbff5622950f3f8aa17b8a9d978d3eb693ea02f05 |
> | owner-scopes.md | 2cae7c370e4afe5801e5ff5fc7206f03c2193c1c5cc050eacf35d4a477efe6c0 |
> | commissioning.md | 11c05e374c68ee9f8fa0b8e790a47381f56aea63fe37141a4a4a6f17d232ec50 |
> | rollout-gates.md | f667ed2e6f8c5f1b4e75651b1aa5bdb671074fe2dcf74f8f3f722250084d2fc8 |
> | validation-matrix.md | 53688287673d29e5d58604eee0ec27e5f134de241032d514edfa5e41a9472d39 |
> | policy-coverage.md | e30154c88b29ce5a21b23d235d0ec863a105a433d7ea23e7fb6937cba928f37b |
> | local-headscale.md | aa764a126e7b1d2c12c257e9d2d1ef2416fb49a47dffeddf93de6a901882c481 |
> | standalone-hosted-headscale.md | b25c3d8ab2642912d1dcbe557b51f9820df8986906c3d1ccb950146efd8ee479 |
> | hosted-domainxfactories.md | c0b94352f89013a28dbc1008d988e7aca94c58b05511a14f52c9cf81cf2b9cc6 |
> | contracts/owner-handoff.md | d8fec9881a390420c41d6bc1dfef8fb44ab35457054611ae3751a8a98ca9fd78 |
> | contracts/product-interfaces.md | 5643be4adba7bb0ac5413a1ddb74bab863af981c945d92c4fde14d97fd0d94e7 |
> | contracts/qualification-evidence.md | 8d7d4ab79a6bb456a2dabef0d6ec4d5ba40da296e5ba19ceab2c7e907df31e92 |
> | contracts/task-evidence.md | c7734b52520b6ad6ccad75cd32f4e49b395877fb926dffc03c3e85e34c854247 |
>
> Further task/owner/class/case/dependency/file/command or frozen-input changes still require affected owner review and a new freeze before use. Source consent supplies no actual output authentication, target authority or rollout acceptance. The exact generated neutral inventory filename remains allocated and closed at the actual authorized cut; no version is reserved here. Corrected source/CI exports are qualified at source 94caf6717e, with 584 feature cases and exact-head measured CI/Python 3.14/Codex clearance. Brett authenticated the c8be9c1d source packet at 2026-11-15T11:47:39.004Z; expanded T010 default verification passes against accepted control 698bf8367. This is actual source-output review, separate from source-scope consent; full Q0/Q1-Q5 and private trusted-base activation remain pending. All four PRs stay draft and Q1-Q5 remain unentered.
