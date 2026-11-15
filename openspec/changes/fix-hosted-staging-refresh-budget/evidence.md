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
finalization. Seven further actual kernel/control/expiry checks pass. Full final
qualification, exact-head hosted CI and local expert rechecks remain pending.

The pinned CLI validates this new change strictly. Default all-corpus validation
returns its existing dispositioned add-chain-attestation finding; no new exception
or baseline edit is introduced. The generated sequence ledger requires the actual
publication PR number; it will be seeded through the owning script after draft
publication, followed by focused corpus tests and hosted CI.

This is review evidence, not owner source ratification, landing, setup/dispatch,
production hosting or T012S-V commission. Feedback remains deferred and neither
blocked/denied write is replayed.
