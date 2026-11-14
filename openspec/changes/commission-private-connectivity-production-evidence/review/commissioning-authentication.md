# Source commissioning authentication

Status: draft

Brett Heap is the accepted source-evidence custodian. Actual authentication is
pending review of the immutable commissioning container and the separate T010
receipt. Ratifying E, its bootstrap amendment and N did not authenticate unseen
outputs. This record grants no deployment, spend, enrollment, release or Q0–Q5
acceptance, and all three PRs remain draft.

The prepared container preserves the original T001–T005 commands and source
observations, actual T006 owner/custody decisions, exact committed T007–T009
regression outputs, original human-message timestamps and individual raw-record
digests. The failed development regression remains visible. Source/governance
artifacts retain their real Git references. No T001.json–T009.json is created.

Before acceptance, review the actual command, source, exit, timing, original
stdout, original/export digests and stated redaction method for each import.
Confirm the source-only scope and original human provenance; successful source
tests and synthetic fixtures supply no provider/customer/live qualification.
T010 additionally requires the actual successful exact-head required GitHub
run/job and explicit zero-skip collection of both feature suites.

The final decision must name the reviewed immutable manifest and its canonical
content SHA-256. That core excludes only the review pointer and derived pin
inventory, so authentication and the final control manifest can occupy distinct
commits without a self-containing hash. A payload/binding/authority change needs
new review. Until the actual decision exists, the verifier refuses admission.

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

## Immutable packet for actual authentication

This is the prepared, concrete review target. The decision above is still pending; preparation, source ratification and successful CI do not authenticate it.

| Identity | Exact reviewed value |
| --- | --- |
| Manifest | [commissioning.json](https://github.com/opensoft/openXfactory/blob/6faaba5ab387d37e13c9c96a797ff7612f883647/specs/043-private-connectivity-production/evidence/commissioning.json) |
| Manifest commit | `6faaba5ab387d37e13c9c96a797ff7612f883647` |
| Manifest file SHA-256 | `0b77c70d66420d4d582ac4806f29b4ee43d00057c14057678b1075d9dc2fe554` |
| Authenticated core SHA-256 | `0645f3e7f31b9b4c708c94b8ff2298fe530b0d18928355201d9f54cab60b770f` |
| Task-definition freeze | `66db63ec98e366f141230d22e6e4e159916bb997f159916159dcc7b6ae3f32d0` |
| Distinct CI receipt | [T010.json](https://github.com/opensoft/openXfactory/blob/73ea5d8e646f754088733099ef1680ac6d8605d9/specs/043-private-connectivity-production/evidence/T010.json) |
| Actual tested source | `c4e70f66d0d0ca8ca50668a318ce1360fe53b443` |
| Actual required CI | [pytest-suite run 43608762372 / job 132489023068](https://github.com/opensoft/openXfactory/actions/runs/43608762372/job/132489023068), success |
| Explicit source collection | 287 verifier tests and 40 inventory tests, all passed; zero source-suite skips, failures or errors |

The actual source-suite step ran from 2026-11-14 15:40:30Z through 15:40:39Z. Its complete labelled step output, original/export digests, full job-log digest, source identity and required-check readback are retained in the T010-output object. Existing root-suite skip policy is separate from the zero-skip feature collection.

| Original import | Tested source | Actual execution result |
| --- | --- | --- |
| T001 | `b1896c4719dedee4d2f02bc7534c73c4df9fbbb5` | exit 0; completed 2026-11-13T16:28:22.421179+00:00 |
| T002 | `b1896c4719dedee4d2f02bc7534c73c4df9fbbb5` | exit 0; completed 2026-11-13T16:28:22.487254+00:00 |
| T003 | `b1896c4719dedee4d2f02bc7534c73c4df9fbbb5` | exit 0; completed 2026-11-13T16:28:25.623787+00:00 |
| T004 | `b1896c4719dedee4d2f02bc7534c73c4df9fbbb5` | exit 0; completed 2026-11-13T16:28:28.870446+00:00 |
| T005 | `b1896c4719dedee4d2f02bc7534c73c4df9fbbb5` | exit 0; completed 2026-11-13T16:28:28.919270+00:00 |
| T006 | `cdf5e16be467c38c49a2991663d9cec76b71c53d` | exit 0; completed 2026-11-14T06:54:24.704567+00:00 |
| T007 | `1427b581493e660e9e5e1e84bbfdee13eab109be` | exit 0; 287 tests passed; completed 2026-11-14T14:50:37.424306+00:00 |
| T008 | `de1fc5640b4074b0e61ef4b0b54b04fc5f4a9b86` | exit 0; 40 tests passed; completed 2026-11-14T14:19:04.534581+00:00 |
| T009 | `ae7e13b40887d9d13cf8d9f4dbdd0dea2396405d` | exit 0; 175 tests passed; completed 2026-11-14T15:06:59.916701+00:00 |
| T010 | `c4e70f66d0d0ca8ca50668a318ce1360fe53b443` | exit 0; required GitHub job and both feature suites passed; completed 2026-11-14T15:40:39Z |

Review the retained original human messages and individual raw-record digests against this Codex session. T001-T005 used their original coordinator source-owner preparation instruction before E custody acceptance; the import-role clarification explicitly avoids backdating the later E custodian role. E owner and source-only custody acceptance occurred before their consumers. All nine original imports retain their actual commands, source artifacts, exit/timing, stdout/redaction identities and dependency order.

The failed development regression, missing nested-checkout refusal, earlier retention failure and superseded cancelled CI remain inspectable; none supplies a passed dependency. Prior containers and original observations remain immutable in Git. The current actual source checks and current required CI provide their own results.

The exact commissioning inventory passes its read-only check. Source/case/CI/original-authority and dependency-order preparation checks pass for T001-T010. The default evidence verifier still refuses admission with actual custodian authentication pending. The measured standing census is 1017 sites across 35 populated members, with zero uncovered sites; foreign production evidence remains FUTURE because no such site exists.

Brett's requested decision is authentication of this exact source-only packet and its original human provenance under the accepted C-08 policy. After that actual decision, record the reviewed manifest/core and actual review time in the decision block, bind the new review reference in a later control revision, verify the same authenticated core, run the default verifier and only then complete T010. This supplies no later operating decision or acceptance of unseen results. Full Q0 and Q1-Q5 remain pending, and all three PRs remain draft.
