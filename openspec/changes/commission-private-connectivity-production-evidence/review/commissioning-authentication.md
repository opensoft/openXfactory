# Source commissioning authentication: CI proof refinement

Status: draft
Created: 2026-11-14

## Existing authenticated controls

The accepted E, neutral, package and installer source observations remain immutable. T012 completed after Brett's actual authentication at 2026-11-14T22:31:50.896Z and successful default T012/T010/T011/T016 commands against [accepted control 35e98a276](https://github.com/opensoft/openXfactory/blob/35e98a276fbd51c7cdfe89203a3eecbff1266f4f/specs/043-private-connectivity-production/evidence/commissioning.json). Its actual review is [9af6e00e7](https://github.com/opensoft/openXfactory/blob/9af6e00e76e25fd1ace915645f419d5787fe735f/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md); installer core b34071e4b290a4e5f58e5bb7bce9b2dee0a16cd18b40d51563c0d9f480c28beb is unchanged.

Earlier accepted E/N/L anchors remain in their exact Git history with matching immutable readers and frozen inputs. The new bounded compatibility bridge fixes the accepted historical control and reader content identities, verifies their original authentication, and preserves current authentication/revocation checks when a new control consumes historical dependencies. This pending context authenticates no new output and does not revoke those prior observations.

## Accepted additional source scope

Brett separately ratified the exact additional source-CI/custody/file/refreeze scope at the same actual input. The [scope ratification](../../extend-private-connectivity-source-ci/review/ratification.md) retains the original user timestamp, individual raw-record digest and accepted design revision. Scope consent does not authenticate subsequent outputs.

The new complete definition is e912507dfe7a136879f786e1ca5ccbdf62556b3f3fc179398af0bd8e730fd298. All 68 task IDs, owners, classes, dependencies, cases and commands remain unchanged. Only the accepted T009/T010 file refinements and one frozen custody clarification changed.

## New source CI candidate

The corrected source is [746e9316c](https://github.com/opensoft/openXfactory/commit/746e9316cfe7dbed7fac3ecc0104fb5bfdec15a7), with a T010 source baseline of a845c30eff6cf0385e3d21ab4640b9e62554e1e3. Both existing workflow artifacts are retained at that tested revision. Local source collection is 298 evidence, 40 inventory and 42 proof-root tests, all passing with no skips. The two repaired shared regressions also pass.

The initial Python 3.14 run at 3a53fc7f53c3cfe86ee895edec8887c2614cd283 failed because a test read the rewritten remote URL rather than the stored SSH configuration. The exact failed GitHub run, source and original step output are retained during export. A controlled local URL rewrite reproduced the failure; the corrected assertion checks the stored origin without changing it. Python 3.14 qualification now runs the explicit PR revision and checks all 42 JUnit cases.

Both entry points completed successfully at the exact corrected source revision. Root pytest-suite run 43653058553/job 132625600781 explicitly collected and passed 298 evidence, 40 inventory and 42 proof-root cases, with no source-suite skips, failures or errors. Its original source step ran from 2026-11-14T23:54:28Z through 2026-11-14T23:54:41Z. Python 3.14/doc-health run 43653058532/job 132625527820 passed its existing doc-health run and all 42 explicitly pinned proof cases at that same PR head. Required root floors, exact skip obligations and named verdicts passed unchanged. Codex cleared source 746e9316cfe7dbed7fac3ecc0104fb5bfdec15a7.

## Custody and admission boundary

Private token creation/fetch is not needed or exercised while no foreign records exist. The qualified producer must be available from an authenticated trusted-base control before either existing CI lane can mint a token for private preparation. Candidate scripts never execute before those credentials; proof roots contain commits only, credentials are revoked before tests, and temporary stores are removed. A synthetic source test is not live GitHub credential/fetch qualification or full source/task admission.

The new packet requires actual custodian authentication after its original outputs exist, followed by default T010 verification. The previous accepted control remains separately usable. T020 remains unchecked; subsequent private admission still requires the trusted producer, actual owner Git stores and its own accepted evidence/dependency timing.

```json
{
  "schema": "043-source-authentication-v1",
  "decision": "pending",
  "custodian": "Brett Heap",
  "reviewed_manifest": null,
  "content_sha256": null,
  "reviewed_at": null
}
```

Full Q0 and Q1–Q5 remain pending. All four PRs remain draft. No merge, version/tag, release publication, target operation, deployment, enrollment, paid resource or commercial gate is granted. Actual provider/domain/integration, live custody, staging and canary decisions retain their own gates.


## Withdrawn source-CI review target

The c49a6a5e packet below was withdrawn before authentication. Codex review of packet head 507b1b4fb6d076b7b36b7379286021eec6b9568d found that the reader could admit a production child that ran before Q2 completed or its separately recorded admission was reviewed. The original observations remain preserved; they do not qualify the corrected reader. Corrected source, exact-head CI and a new actual authentication target are required before the expanded T010 control is accepted. No earlier approval transfers to that new target.

Follow-up review at 360e2dad3bc10395518133a6af73c4ab8eea8cf8 identified the same missing ordering at Q1. The corrected source now checks completion and any admission review of every accepted predecessor before consuming execution at T050–T064, plus the complete program Q2, same-scope managed-service eligibility and corresponding offer admission. This applies the existing dependency and rollout requirements without changing the frozen task definitions. Synthetic regressions reproduce 28 additional wrongly accepted predecessor cases before repair and retain positive boundary controls. The source-CI packet remains withdrawn until the complete repair has fresh actual qualification and review.

| Item | Immutable review identity |
| --- | --- |
| New-definition control | [02be87d2b](https://github.com/opensoft/openXfactory/blob/02be87d2bdd40abb92f3f232d84f667b661aa10e/specs/043-private-connectivity-production/evidence/commissioning.json) |
| Manifest file SHA-256 | 8b18f3ef78031e2d7cb2fd4060e141f05fa8daf4275762ff5441c461914c9b43 |
| Authenticated content SHA-256 | c49a6a5ec2dfab98d76a9dd407afbcc4d0eabb0e7acfc0151083f63b03e1e854 |
| Definition SHA-256 | e912507dfe7a136879f786e1ca5ccbdf62556b3f3fc179398af0bd8e730fd298 |
| Tested source | [746e9316c](https://github.com/opensoft/openXfactory/commit/746e9316cfe7dbed7fac3ecc0104fb5bfdec15a7) |
| Original two-lane output | [17f4bbe5e](https://github.com/opensoft/openXfactory/blob/17f4bbe5ef950d2ee8e9f41c6959c031fc85cb18/specs/043-private-connectivity-production/evidence/T010.json) |
| Distinct receipt | [731fee366](https://github.com/opensoft/openXfactory/blob/731fee366ee2b47f0e32d6d0cc907bb2f4c78df6/specs/043-private-connectivity-production/evidence/T010.json) |
| Required source CI | [run 43653058553/job 132625600781](https://github.com/opensoft/openXfactory/actions/runs/43653058553/job/132625600781) |
| Python 3.14 source CI | [run 43653058532/job 132625527820](https://github.com/opensoft/openXfactory/actions/runs/43653058532/job/132625527820) |
| Preserved failed preparation | [Python 3.14 run 43652162290](https://github.com/opensoft/openXfactory/actions/runs/43652162290) at source 3a53fc7f53c3cfe86ee895edec8887c2614cd283 |

The actual CI output remains separately immutable and is also copied exactly into the permitted T010 E container so its original references are visible to the closed shared sweep. Their decoded values are checked equal; no original observation or command/output identity is changed. The earlier unreviewed preparation control is retained in prior_containers. The actual failed Python 3.14 source step remains in the original export, including its one failure and 41 passes; it supplies no passing dependency.

Committed data measure 1245 standing sites across 36 members with no uncovered site. The foreign member remains FUTURE: this packet introduces no private evidence binding. Exact computed retention references are published and independently read back without changing earlier refs.

Binding/source/closed cases/CI, actual authority, immutable artifacts and all historical dependencies pass preparation. The default new T010 command correctly refuses pending actual custodian authentication. The prior accepted T012 anchor remains separately usable with its exact fixed historical reader. No source/CI control is treated as a live or commercial acceptance.

Authenticate this actual source-only E packet and its original human/CI provenance. Acceptance permits recording the new immutable accepted review/control pair and default T010 verification only after those checks pass. It does not authenticate a new package run, activate private fetching, put the producer on a trusted base, authorize a merge, or advance full Q0/Q1–Q5. All four PRs stay draft.
