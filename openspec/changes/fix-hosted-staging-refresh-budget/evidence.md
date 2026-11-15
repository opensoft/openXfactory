# Protected staging refresh candidate evidence

Status: draft
Date: 2026-11-15

Local expert review of openXwallet #71 at 14adfef712087 independently reproduced
three actual running workers after hold, main source or current operator context
changed during durable cleanup registration. All isolated worker PID/start
generations were reaped. The prior ordinary ledger refuses complete reobservation,
so this packet proposes an explicit source-owned allocation rather than resetting
counters or removing checks.

The proposed adapter correction retains one original Decision and all current
predicates, repeating correlation after acknowledged cleanup but before opening
the start request. Initial focused correction checks pass (31 cases), including
late authority refusal, complete positive, per-reader/aggregate caps and legacy
finalization. Seven further actual kernel/control/expiry checks pass. Final qualification and review receipts are posted on the paired pull requests,
keyed to their exact heads; these initial counts do not replace later checks.

The pinned CLI validates this new change strictly. Default all-corpus validation
returns its existing dispositioned add-chain-attestation finding; no new exception
or baseline edit is introduced. The sequence ledger was generated through the owning script with actual PR #1326;
only this change row moved. Fresh corpus validation follows the merged main baseline.

This is review evidence, not owner source ratification, landing, setup/dispatch,
production hosting or T012S-V commission. Feedback remains deferred and neither
blocked/denied write is replayed.


## Resumed source reconciliation

The candidate incorporates main 2f68b079072e7e1a2be6886eaa61069cd593fab5 without
changing the unrelated P1 tooling boundary work. The generated ledger retains
all current main provenance and adds exactly the staging-refresh row for #1326.
Fresh code-surface, sequencing and target-release tests pass: 538 cases, zero
failures/errors/skips. Sequence, ledger-diff, target-release and pinned default
all-corpus OpenSpec validations pass; only the already accepted dispositioned
add-chain-attestation finding remains in that baseline report.

Local architecture, defensive security, reliability, static and API reviews
find the corrected paired source consistent with this allocation. Remaining
panel/qualification and hosted evidence will be recorded on the reviewed pull
requests; this source evidence is not owner ratification or operational authority.
