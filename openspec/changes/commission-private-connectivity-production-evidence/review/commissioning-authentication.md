# Authentication review: Bounded evidence and local Headscale source

Status: draft

## Exact combined source review target

This packet requests actual source-output authentication by Brett Heap in the accepted E and Headscale package source-evidence custodian roles. Source-scope approval, unit tests, CI and Codex review do not authenticate these new outputs.

| Item | Exact immutable identity |
| --- | --- |
| Proposed reviewed manifest | [736e8f8dbd347e145638a1eb12bfe58d49bbeaf1](https://github.com/opensoft/openXfactory/blob/736e8f8dbd347e145638a1eb12bfe58d49bbeaf1/specs/043-private-connectivity-production/evidence/commissioning.json) |
| Whole manifest file SHA-256 | `13874618554f322c66dc78acdbf953921ceb0e2bff3e550b791b6def4004260c` |
| Canonical content SHA-256 | `e49a5a8eb773dadd05ac345baf7eaf9ba5d019f6fb4d128580667a4b617577db` |
| Complete current definition SHA-256 | `2a46a5420c9f90f5ace72e8482b0fa0541b55f733bd6ad7a8e53ebb99215d796` |
| Actual E source | `479750c62efad1bf803b6d1bec566c8ac07c5565`; base `fe79bc90783195d088ba8bfad42183631a909597` |
| Distinct E original/receipt | [original](https://github.com/opensoft/openXfactory/blob/7e05bb7adb190d608f654c4888a4edd4c0552758/specs/043-private-connectivity-production/evidence/T010.json) / [receipt](https://github.com/opensoft/openXfactory/blob/fd4f23037ab3fd0465cf870d9526e313085f25b6/specs/043-private-connectivity-production/evidence/T010.json) |
| Root source CI | [actual run/job](https://github.com/opensoft/openXfactory/actions/runs/43775758307/job/133001554391) |
| Python 3.14 source proof | [actual run](https://github.com/opensoft/openXfactory/actions/runs/43775758027) |

## Actual E source and CI observations

The accepted T018 refinement adds only scripts/hermes_runtime_validation/release.py and tests/hermes_runtime_contracts/test_release_inventory.py. All sixteen frozen input files and all other fields of the 68-task registry remain unchanged. The new complete definition is fixed above; the original T005 c37 footer remains historical. The new reader accepts only the fixed c8/c4 whole controls, the original c37 definition/reader and the already accepted historical task closure. Pending/live tasks, changed control/core/reader/freeze and substitutions refuse. Current revocations and completion closures propagate through nested original readers and cache rechecks.

The actual root lane collected and passed all 694 explicit source cases: 557 evidence, 40 inventory and 97 source-proof cases, with no skips, errors or failures. The existing Python 3.14 lane passed all 97 explicit proof cases. Both used the original authenticated producer 94caf6717ece69af66dfde121bf4b868a6c3abdf through the existing read-only repository-scoped App channel; private commit-only proof succeeded, tokens were revoked before tests and temporary proof stores were removed. No App, token-scope, permission, secret or producer change was made. Exact-revision Sonar passed without threshold/floor/skip waivers.

The local run preserved eight initial missing-bridge failures. All 694 affected feature cases then passed; two additional documentation tests initially lacked uninitialized pinned dependencies. After initializing those exact gitlinks without changing a gitlink, all 143 source-proof/documentation cases passed. The union covers all 740 affected cases. The original failures and subsequent outputs remain in the E original export by digest. Actual old source observations and failures remain immutable in prior controls; their old test counts are not relabeled as new results.

Brett accepted the exact neutral/E refinement at 2026-11-15T21:17:57.195Z, native session 01a1c061-ee6e-7e61-9db4-280a724e05c2, line 36318, raw JSONL SHA-256 09dea317a799634d504758517731bd500e37aef96881edb51f38813cd7c892ac. The immutable ratification 73d05439931863befb47326e505220f8f057b5b9 preserves that actual decision and exact reviewed design. This scope approval is separate from the requested output authentication.

## Actual local source observations

T021 and T022 each ran in a separate clean immutable-source worktree. Before either collection the collector passed full default T020 verification against accepted control c4e380b43e27093a2a3b99264a3fb52a6cf36c21, core f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332, using the fixed original c37 reader. No pending new E output or unaccepted task was consumed as a predecessor. Original creation provenance remains separate from current operation authority. Initial unadmitted preparations used a different scope.run label; the exact authority check caught that metadata mismatch. Fresh actual collections now preserve the accepted package scope unchanged and check both authority and exact per-task file permission before execution; the old observations remain immutable and are not relabeled.

| Task | Actual source | Original output | Distinct receipt | Actual result |
| --- | --- | --- | --- | --- |
| T021 | `713773698089a2edd0f3ddc1f4044fff62d990e6` | [fdb926547dfa166661d5b57f7fa15ff54331f4b3](https://github.com/opensoft/Headscale-Install/blob/fdb926547dfa166661d5b57f7fa15ff54331f4b3/evidence/private-connectivity-production/T021.json) | [6e3ca9c623b5ecc24d57e45e19154f6f04176552](https://github.com/opensoft/Headscale-Install/blob/6e3ca9c623b5ecc24d57e45e19154f6f04176552/evidence/private-connectivity-production/T021.json) | 64 source tests; 19 task controls; no skips |
| T022 | `c4b5af5515cf4a5f80c63860fcaa3905a788103f` | [b3c3bd01bc3f50d62b475dda81a58d5538b86fbd](https://github.com/opensoft/Headscale-Install/blob/b3c3bd01bc3f50d62b475dda81a58d5538b86fbd/evidence/private-connectivity-production/T022.json) | [394fe5cccfcde1ab97cc20550c1756bc126d0759](https://github.com/opensoft/Headscale-Install/blob/394fe5cccfcde1ab97cc20550c1756bc126d0759/evidence/private-connectivity-production/T022.json) | 90 source tests; 26 task controls; no skips |

T021 tests actual Python TLS chain/name/fingerprint validation and bounded Headscale health handling against generated temporary synthetic TLS fixtures, current owner-channel renewal, refusal of invalid or revoked authority, plan-only local operation without a hosted subscription, and candidate-client archive/device-input checks. Its 64-test original run includes 19 endpoint controls. This does not qualify an actual Headscale endpoint or Windows/macOS/Linux client.

T022 tests protected backup coordination, original-subject single-writer fencing, safe closed archive membership, new-generation import into network-none quarantine, independent current network identity/policy/revocations, removal of restored API/preauth credentials and revoked nodes, retention of legitimate snapshot/current intersection, lost-start containment, explicit unresolved rollback denial and separately qualified sequential upgrades. It returns unqualified/quarantined state and never activates ingress. Its corrected original run passed 90 tests including 26 recovery controls.

Codex found that initial recovery containment ran after the operation context closed. The current-session fixture reproduced 13 failures, including failed containment and an uncertain session exit. The repair handles partials inside the still-open operation/writer-fence context, while entry/exit uncertainty remains unresolved. The original 85-test and 86-test observations and receipts remain immutable as superseded preparation, with the findings and red/green digests in the corrected private originals. A second review found that upgrades rejected older source input provenance and restore refused a definitively absent original. Their red controls and the distinct old-image readback regression were preserved. The current compatibility channel binds source inputs/version/original image separately from target inputs/image; old credentials and current identity controls remain enforced. Confirmed absence is accepted only with empty writer observations under the current fence; unavailable inspection and unexpected writers still refuse. A final local interruption audit reproduced SystemExit bypassing containment; both process interrupts now receive in-session containment, and provider exits are normalized to secret-safe recovery errors. Its red controls and 90-test green output are retained. No acceptance transfers from those earlier observations.

Hosted Codex cleared the three reported recovery repairs at source 9d1e60dcb1 and receipt head 8f8b7b0cec ([actual receipt](https://github.com/opensoft/Headscale-Install/pull/2#issuecomment-6903833755)). Later explicit requests reached the hosted review usage limit; the interruption patch and final receipt changes have local regression/CI validation but no fresh hosted clearance. This remains an explicit review limitation, not an approval or a passing hosted review. The E source 479750c62e has its own exact Codex clearance.\n\nThe private owner repository retains all private source, original stdout and distinct original/receipt commits. Public coordinator Git carries only typed immutable private references and closed source expectations; it does not contain private source objects, commit headers or raw private output. Actual intended-platform, custody/provider and client qualification remain separate.

## Admission and rollout boundary

The original accepted c37/c8 and T020 control/review graphs remain independently usable and unmodified. Initial unauthenticated control core 502ad786b1d3326ba2438b20c43fc5f794e92b065d5e19a0d1a149bc975f14b4 omitted the two local binding class labels. Strict preparation caught this before admission; the new labels are copied from the frozen source-L task definitions and match the unchanged actual receipts. That withdrawn control remains immutable in prior_containers; no actual output or approval is relabeled. This manifest is a new complete content target. Default verification of its new tasks must refuse while the following actual authentication decision remains pending. Preparation checks and exact pin inventories supply no admission. T021/T022 and T018 remain unchecked; the prior 14 task completions retain their original accepted anchors.

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

All source PRs remain draft, including coordinator #1325/#1327, private package #2, Ops #628 and codeXfactory #583. The one-time CI-only #1328 exception is already merged. No release version, inventory cut or tag is allocated. A separate lane published contract-v4.2; the next actual version must be rechecked when a concrete cut is authorized. Full Q0 is unaccepted, Q1-Q5 have not been entered, and deployment, spend, enrollment and commercial rollout retain their separate decisions.
