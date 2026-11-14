# Proposal preparation evidence

Status: draft
Kind: evidence

Prepared on 2026-11-14 from factory main
`c283547b3490c5f3a29b0c800c5c63da361c7da7` and adapter #66 merge
`5498a9b27d7a61daf8f4088ce85906cb436a2033`. The user commissioned this source
proposal and existing feature 017 Speckit plan using the recommended T013 basis.
This is no acceptance or commissioning of the proposed implementation.

Pinned OpenSpec strict validation passes for this change and all five adapter
OpenSpec items. Factory code-surface/estate membership, proposal origin,
sequenced-after and former-ID corpus checks pass. Former-ID history arrival is
not yet judged: no new commit range was supplied in that preparation check.
Document checks preserve the factory README OpenSpec Records block and the
adapter portable feature pointer; proposed T012N-V and T001/T013/T014/T015 remain
unchecked. Only Markdown and the new OpenSpec metadata change; no executable,
workflow, pin, contract bundle or dependency-lock change is made.

## Publication verification and correction

The initial local preparation used raw CLI diagnostics and incorrectly called the
chain-attestation finding a publication blocker. The governed corpus verdict is
`python3 scripts/validate-openspec-cli-pin.py --all`, in its default pinned-artifact
form, as required by `require-adjudicated-validation-entrypoint`. That command
passes with zero undispositioned failures. It reports raw totals 128 passed / one
failed (129 items), then applies the existing ratified chain-attestation exception
from `contracts/openspec-cli-pin.yaml`, citing its reason and Brett Heap's
2026-09-05 “take exit 2” authority. This is a passing adjudicated gate with one
accepted exception, not a clean raw corpus. The disposition, frozen packet,
canonical requirements, validator and pin remain unchanged. No new exception or
restoration of the deliberately reconditioned scenario is needed.

The user subsequently commissioned publication-gate resolution, both candidate
PRs, hosted CI and local Codex review, followed by presentation of v2 for
ratification. This authorizes source publication/review only; it does not ratify
v2, commission its implementation or grant any operational stage.

The generated ledger row is initially pending the actual draft proposal PR number.
After that number exists, use
`python3 scripts/validate-sequenced-after.py . --seed-ledger --moved-by '#<PR>'`,
review the generated diff and rerun the gate. No invented PR is stamped and the
ledger is not edited by hand.

Unchanged checkout limitations, not new publication refusals:

- Two existing factory README links point to absent files in this checkout:
  contracts/private-connectivity/README.md and
  docs/ideation-dashboard-session-runbook.md. Those link spellings predate this
  draft; no new relative link is broken.

Research closure covers API/source provenance, security/credential boundaries and
runtime/cleanup staging. The API budget finding was corrected: correlation keeps
its four-read/two-job-page limit; added protection/source/hold groups have explicit
three/four/two limits under the same parent deadline, with aggregate thirteen and
a complete positive acceptance control. This is planning review, not implementation
qualification or a hosted Codex review. No new runtime tests or hosted CI run was
claimed for the initial documentation preparation; publication results follow later.

The private security research artifact write was rejected with only “blocked by
policy”; it was not retried or recreated. Research findings returned in chat
informed the authorized proposal/plan. Setup, dispatch, actual credential/token
issuance and live qualification remain unauthorized. Feedback stays deferred;
neither historical blocked write nor the earlier optional PR-description update
was replayed.
