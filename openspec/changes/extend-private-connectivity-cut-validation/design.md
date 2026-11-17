# Design: close the private-connectivity cut validation gap

Status: draft
Kind: design

## Context

See proposal.md. Brett authorized contract-v4.3 candidate preparation only at
2026-11-17T00:30:45.368Z (original user-record SHA-256
6173401c794ae06cb260c859b00a1663742599c12ce7d1c4c7c621554d0a56d9).
Independent candidate source 535272c7c60ec42d7dbd6088b85f3ed5903b59e0
contains the normal atomic manifest/changelog/generated inventory.
Its exact inventory and pre-merge tag obligation verify; 189 manifest digests
match. Actual regression: 141 passed, 52 subtests passed, two failures in the
closed intent-compliance release-state enum. T018 remains incomplete.

The additional test is not in T018's frozen allowlist. The existing coordinating
definition is 2a46a5420c9f90f5ace72e8482b0fa0541b55f733bd6ad7a8e53ebb99215d796.
Refreshing it also requires preserving the actually authenticated original
controls through their exact original reader, rather than relabeling old outputs.

## Goals / Non-Goals

Complete the normal narrowly bounded cut regression and owner/file handoff.
Retain six source components and one executable 043 task list. This is no
publication, target-operation, identity, spend, protected-lock or Q0-Q5 grant.

## Decisions

### N: one normal closed-version test advance

Add only tests/intent-compliance/test_release_boundary.py to T018. Advance
its explicit enum/match arms for contract-v4.3 using measured cut membership;
retain existing intent membership/schema-pin checks and unknown-future refusal.
Do not replace the closed states with an open-ended version comparison or skip.
This release member and the regenerated contract-v4.3 inventory stay in the
actual atomic cut. Historical inventories/tags remain byte-identical.

### Exact E source surfaces

| Path | Bounded purpose |
| --- | --- |
| specs/043-private-connectivity-production/verify-evidence.py | Read-only exact prior-definition/control/reader compatibility and current-source freeze identity |
| specs/043-private-connectivity-production/tests/test_evidence.py | Actual prior-control positives; changed control/core/reader/definition/task/scope, pending/live and authority-propagation refusals |
| specs/043-private-connectivity-production/tests/test_evidence_pins.py | Only directly affected current-definition/immutable inventory expectations and read-only checks |
| specs/043-private-connectivity-production/tests/test_source_roots.py | Only directly affected explicit suite-count/freeze expectations; privacy and trusted-base guards unchanged |
| .github/workflows/pytest-suite.yml | Only measured explicit feature source-suite counters/obligations required by those regressions |
| .github/workflows/doc-health-py314.yml | Matching measured explicit source-suite collection; retain all existing obligations |
| specs/043-private-connectivity-production/tasks.md | Only the T018/T043/T047 file additions below; no other task field changes |
| specs/043-private-connectivity-production/owner-scopes.md | Matching N/O source and separately governed Tenant target-data handoff |
| specs/043-private-connectivity-production/contracts/task-evidence.md | Complete 16-input/68-task freeze refresh; original definitions remain pinned history |
| specs/043-private-connectivity-production/evidence/T010.json | New actual E output/receipt identities, with failures and actual CI preserved |
| specs/043-private-connectivity-production/evidence/commissioning.json | New pending/authenticated control with fixed prior anchors and exact generated inventories |
| openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md | Separate review of actual new source/CI output and genuine later custodian decision |
| tests/doc-health/test_sentinel_vocabulary.py | Only directly measured census deltas, with all membership/reachability assertions retained |

Use already owned E T007-T010 source/helper/test/CI scopes; no T010 file-envelope
addition or parallel task list is proposed. The inventory helper and authenticated
source-proof producer remain unchanged. There is no new token/secret/App scope,
billing/permission setting, generic discovery, floor, skip or threshold waiver.
An actually necessary unlisted path returns for owner review.

### Fixed 2a46 source controls and original reader

Add only these exact accepted whole controls. Equality covers canonical
repository, commit, path and whole-file SHA-256, not a caller's matching core.
The reader is the original source at 8ac068510936c97d21ace2b923ad00c0a6238b68,
path specs/043-private-connectivity-production/verify-evidence.py,
SHA-256 e2aae8286af91d0ae04b99498da52ace1da69e3adfd0adc8df45437d8079ac6f.

| Accepted whole control | Whole-file SHA-256 | Authenticated content SHA-256 |
| --- | --- | --- |
| 8ac068510936c97d21ace2b923ad00c0a6238b68 | e42735845944bb5c36d46a4648c56ab9bd4b0dfd82d4bc3a5b7128b08c6b89bf | e49a5a8eb773dadd05ac345baf7eaf9ba5d019f6fb4d128580667a4b617577db |
| 1fb3a6a8188a4b051693ac2cd93920f4e69b0d0b | 02158d50df76a25eed4b1cd046bef3bf724aa21c0e9763b3352a02a60ac9a326 | f91b58db2fe5302a9c08e9fc2bafbeb3f9947ce4351dcadf5e450bd6eeb6bdc6 |

Both paths are specs/043-private-connectivity-production/evidence/commissioning.json.
The first closes the 16 actually accepted source tasks T001-T012, T016,
T020-T022. The second adds actually authenticated T013. Limit any historical
mapping to those exact source bindings; pending tasks, production instances and
new task/case/file changes receive no acceptance. Require the original complete
2a46 freeze and actual accepted authentication. Current revocations/completion
closures propagate through every nested reader and cache recheck.

In particular, reviewed manifest 53c2b0700e342b77196980a617dea7fc2fa33512
still has a pending review pointer in its own immutable bytes. It is not an
accepted historical anchor merely because it shares the authenticated core.
Changed-ref copies and unaccepted preparations refuse. Existing legacy/C37
anchors remain independently usable; original observations/readers are unmodified.

### Matching Ops task/file refinements

Subject to the separate actual Ops owner approval of Ops #637, add all seventeen
exact Ops-native paths below to T043. Source, tests, fixture/discovery/census
metadata and normal canonical-spec promotion are one coupled owned change.

| T043 additional source path |
| --- |
| workflows/aks-administration.yaml |
| docs/aks-administration.md |
| scripts/aks_administration.py |
| tenants/opensoft-private-connectivity-qa-plan.yaml |
| scripts/private_connectivity_qa_target.py |
| tests/test_private_connectivity_qa_target.py |
| tests/test_private_connectivity_qa_workload_sets.py |
| tests/fixtures/aks-administration/private-connectivity-qa/control.yaml |
| tests/fixtures/aks-administration/private-connectivity-qa/customer-a.yaml |
| tests/fixtures/aks-administration/private-connectivity-qa/customer-b.yaml |
| tests/fixtures/aks-administration/private-connectivity-qa/cross-set.yaml |
| tests/fixtures/aks-administration/private-connectivity-qa/foreign-namespace.yaml |
| tests/fixtures/aks-administration/private-connectivity-qa/changed-generation.yaml |
| tests/shards.yaml |
| tests/shard-timings/private-connectivity-qa-source.json |
| tests/test_opsx_validation_workflow.py |
| openspec/specs/aks-administration-workflow/spec.md |

Also add only tests/shards.yaml and
tests/shard-timings/private-connectivity-qa-source.json to T047, for its later
actual CI timing/collection settlement. Its already owned required workflow
and collection test remain the entry points. Preserve every task identity,
owner, class, dependency, case, verification command and Q0-Q5 gate.

This coordinating packet grants no independent Ops code surface: the exact
matching Ops proposal and affected owner acceptance are both prerequisites.
Never use a new file envelope before the accepted complete freeze is refreshed.

### Tenant target data stays under operating authority

Subject to the matching Tenant #350 owner review, its exact declarative
configuration/runbook paths are operational targets of the later accepted
T050 C-03 plan. The producer's source/evidence owner remains C; the managing
factory uses its existing governed GitOps channel. Feature-specific validation
is Ops-owned through T043/T047, alongside existing Tenant platform validation.
No seventh source component, Tenant executable validator/test/workflow, or
cross-repository source prefix is introduced. Unexpected executable needs
return for concrete owning source/task review.

## Risks / Trade-offs

- A future version bypasses existing assertions -> advance one explicit known
  candidate state, retain unknown-version and schema/membership failures.
- A scope refresh destroys old evidence -> fixed whole controls/readers and
  original freezes, with actual authority propagation and mutation refusals.
- Target data is mistaken for an operating grant -> matching owner plan,
  released Ops validation, full Q0/T049 and current C-03/C-07/C-08 before T050.
- Source corrections are mistaken for accepted results -> separate actual new
  output authentication and default verification; T018 stays open until publication.

## Migration Plan

1. Obtain exact N/E and matching Ops/Tenant owner decisions before using these
   refinements. The sole executable list remains 043.
2. Qualify E compatibility/freeze/source-CI work in an independent source branch
   with the existing published contract-v4.2 tree. Keep the incomplete N cut
   separate, so its intentional release-boundary failure cannot block the
   prerequisite E qualification. Preserve accepted T013 and every original anchor.
3. Present the actual new E source/CI packet for separate custodian authentication;
   admit expanded T010 only after its genuine decision/default pass.
4. Only then apply the one N test advance with the cut and regenerate its
   inventory. Requalify exact source/CI and independently review the actual
   candidate. Recheck merge order, version/floor and source ancestry before landing.
5. Keep all PRs draft. Landing, final version allocation, annotated publication,
   T019 readback, target effects, full Q0 and Q1-Q5 remain their own decisions.
