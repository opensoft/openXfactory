# Report source preparation evidence

Status: draft
Kind: record

## Commission and predecessor

Brett Heap ratified openXwallet #75 at
`dbe855cf3a41475426cd1329ca46d7b95dee2905` for source acceptance only, then
instructed normal governed landing when green, post-merge CI verification and
T012T preparation. This new report decision remains unratified/unimplemented.

PR #75 merged normally as `d832709a1119c17014287cd15ff8661bfd758cc4`.
Main already contained `fce58c192e93be9678cfd94fee81f9dacd41e5aa` P1 consumer
fixes; the actual tree `2e058d12f1f32c2795629ea21e305cc1f6131dfe` equals a clean
merge of that first parent and the ratified head. Runtime, native tests and feature
017 content are unchanged by that inherited difference. No admin override was used.

[Post-merge source validation](https://github.com/opensoft/openXwallet/actions/runs/43887121548)
ran the existing main-only ordinary workflow, not the protected runtime workflow.
Its full stage passed 2,322 tests plus nine subtests with three shallow-history
skips, and its required native stage passed all 2,017 cases with no skips. H05=29,
H10=34 and H11=119. Full/native steps and the complete run concluded success.
PR #75's seven runnable checks and exact-head local/connector review had passed.
No post-merge success is asserted for PR-only workflows; main Sonar posted NEUTRAL.

## Source findings driving preparation

The accepted `hosting-issuance-plan.md` section 5 reserves new closed report/case
vocabulary to explicit factory source review and owner acceptance. Existing
`evidence.py` supports source/fixture only; CLI operational selection refuses;
H10 anchors hosted budget controls and H12 is absent. No new report or connected
live qualifier exists. Proposal/design/requirements therefore make future source
and operational gates explicit instead of promoting those predecessor test counts.

## Preparation checks and limits

The repository-pinned OpenSpec 1.12.0 executable and complete dependency closure
were verified before scaffolding. Baseline default `--all` verification succeeded
with the existing accepted `add-chain-attestation` scenario disposition: it was
not a clean-tree verdict. Final default validation returns success with 143 passing items and the same
one accepted finding (144 total); the new report change alone passes strict
validation with no issues. No new disposition is added.
No claim of fresh hosted CI or expert review of this unpublished draft is made.

This packet changes governance documents only. It does not move pins, canonical
neutral contracts, released inventory or runtime defaults. T012T source acceptance
and implementation remain separate; T012U-V/T001/T013-T015 remain open. Setup and
protected dispatch remain unauthorized; feedback deferred; blocked writes unreplayed.

## Historical preparation gates and publication dependency

Code-surface grammar/membership, target-release and sequenced-after/archive-date
checks pass. The existing corpus ledger is deliberately unchanged: ledger-diff
identifies the new draft row as missing. Its seeder explicitly requires the real
moving pull request through `--moved-by`; no new factory PR exists in this
preparation and no guessed reference or wallet #75 is substituted.

When publication is separately requested, first open the actual factory candidate
PR, then run `python3 scripts/validate-sequenced-after.py . --seed-ledger --moved-by '#<actual-factory-PR>'`
with that real reference. Verify only the new row moves and every old row's
provenance stays intact, rerun ledger-diff/all affected gates, and push the update.
This is a known publication prerequisite, not a clean ledger or hosted-CI claim.
Do not weaken the seeder, hand-edit generated rows or change shared tooling to
manufacture provenance. The current candidate is preparation complete, not
publication/merge ready or accepted for implementation.

## Publication ledger completion

The owner subsequently commissioned both candidate PRs, CI and local Codex review.
Factory candidate [#1332](https://github.com/opensoft/openXfactory/pull/1332) was
opened in draft first, supplying actual provenance for the unmodified seeder:
`python3 scripts/validate-sequenced-after.py . --seed-ledger --moved-by '#1332'`.
Only the new `add-protected-runtime-report` ledger row was added; existing rows
and their provenance remain byte-identical. Ledger-diff and the affected house
gates are rerun for publication. Exact-head hosted CI and local review receipts
will be recorded on the PR after completion. No source acceptance, implementation
commission or operational authorization is inferred from publication.
