# Design: Preserve private source proof after delegated authentication

Status: draft
Kind: design

## Context

Protected coordinator revision 44e7b4bf8443f8d97790899c74228d5b56eab54a contains the current human-authentication-only bootstrap. Both workflows select the event's real previous or PR base revision. Both use the same predicate before the existing App-token step. A direct replay of that predicate accepted the actual human-authenticated control and refused the delegated envelope shape. The immutable producer also insists on a human-authenticated base.

On the first landing of delegated evidence, the event still points at the human-authenticated predecessor. A successful first PR and its post-merge run cannot establish compatibility for the next event. CI needs an explicit transition check that starts with an already delegated protected base.

## Decisions

- Preserve the normal selection and verification for a human-authenticated event base. Preserve the existing pre-feature fallback, the local-only path, and refusal on unrecognized, missing or malformed control.
- For a closed delegated source-authentication envelope in the real protected event base, use the exact preceding human proof checkpoint 59c4931fd89811f07f1a02046424a0fa78a2c92a for the existing metadata-only executable. Require that checkpoint to be an ancestor of the actual event base. Its commissioning bytes have SHA-256 02158d50df76a25eed4b1cd046bef3bf724aa21c0e9763b3352a02a60ac9a326 and match the current live human-authenticated commissioning bytes. The checkpoint passed all nine of its main checks, including an evaluated Sonar result. Preserve its independently verified human review and exact content digest. [Checkpoint CI](https://github.com/opensoft/openXfactory/actions/runs/44168838864)
- Require the delegated event base's original proof producer and source-control pins to match the checkpoint. The selector can use only the producer already recorded there at 94caf6717ece69af66dfde121bf4b868a6c3abdf with SHA-256 64df95a3906112e088c026cc2e99d9ad97d93b8dc5e48987f38248784869181e. Preserve the producer's existing authentication check by passing the selected legacy base to its plan command.
- Treat selection as authorization for the existing read-only Git metadata proof only. The rule permits no candidate code, evaluator or executable path to come from a delegated record. The full verifier still requires the real delegated attestation, exact source and output bindings, actual review and admission. A successful metadata bootstrap supplies neither task acceptance nor authority.
- The pinned producer continues to discover strictly scoped owner commit pins from the checked-out source. Preserve the fixed App and installation identities, exact repository allowlist, commit-only fetch, token revocation, credential isolation, private proof-root handling, temporary cleanup, job triggers and check names. Missing credentials or incomplete proof remains a failure.

## Exact surfaces

- T010 uses the existing .github/workflows/pytest-suite.yml and .github/workflows/doc-health-py314.yml bootstrap blocks. Both require identical selection and verification behavior.
- T009 uses the existing specs/043-private-connectivity-production/tests/test_source_roots.py regression file. Preserve the original pre-feature, current-human, no-private, bad-producer, actual-Git and credential-boundary controls.
- Freeze inputs, task fields and the producer file remain byte-identical. Changes in measured test collection use the existing counting obligations and actual collected results.

## Verification

Exercise both workflows with actual Git objects for the human predecessor, the first delegated transition and a subsequent event based on the delegated control. Test unknown or pending authentication, malformed reference, wrong or missing ancestor, changed legacy or delegated producer pins, and incomplete proof. Verify unchanged metadata discovery in both supported branches and byte-identical producer execution. Trace that no candidate code is executed or token issued before the existing isolated preparation step. Preserve the original exact-head checkout, historical controls and measured source-suite obligations.

Collect the new compatibility regression results and the actual exact-head and protected-main results. The T010 evidence itself still requires the qualified actual-output review, registered immutable proofs and verification using the default reader.
