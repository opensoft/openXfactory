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

At this first pending review context, Python 3.14/doc-health and consumer CI pass and Codex has cleared the corrected head. The full pytest source step is still pending. No successful source-CI receipt is manufactured from that pending run. Its actual original output, both run/job identities, unchanged source and closed required cases must be captured before an exact new review anchor is presented.

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
