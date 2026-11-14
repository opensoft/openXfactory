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

Publication gates remain explicit:

- Full factory OpenSpec validation returns 128 passes and one failure, in the
  pre-existing add-chain-attestation packet: its MODIFIED requirement omits the
  canonical scenario “a tranche-two link does not exist yet”. Both involved files
  are byte-identical to factory base HEAD. This proposal neither edits nor
  dispositions that unrelated packet. Full-corpus success is not claimed.
- The generated corpus ledger is stale only for this new packet and its derived
  totals. Before publication, use the actual new proposal PR number with
  `python3 scripts/validate-sequenced-after.py . --seed-ledger --moved-by '#<PR>'`,
  then review the generated diff and rerun the gate. No unrelated or invented
  PR number is stamped during local preparation. The ledger is not edited by hand.
- Two existing factory README links point to absent files in this checkout:
  contracts/private-connectivity/README.md and
  docs/ideation-dashboard-session-runbook.md. Those link spellings predate this
  draft; no new relative link is broken.

Research closure covers API/source provenance, security/credential boundaries and
runtime/cleanup staging. The API budget finding was corrected: correlation keeps
its four-read/two-job-page limit; added protection/source/hold groups have explicit
three/four/two limits under the same parent deadline, with aggregate thirteen and
a complete positive acceptance control. This is planning review, not implementation
qualification or a hosted Codex review. No new runtime tests or hosted CI run is
claimed for documentation preparation.

The private security research artifact write was rejected with only “blocked by
policy”; it was not retried or recreated. Research findings returned in chat
informed the authorized proposal/plan. Setup, dispatch, actual credential/token
issuance and live qualification remain unauthorized. Feedback stays deferred;
neither historical blocked write nor the earlier optional PR-description update
was replayed.
