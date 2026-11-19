# Exact attestor regression scope refinement

Status: accepted (source scope only)
Kind: source-scope-amendment
Accountable-owner: Brett Heap
Proposed-delegate: Codex
Human-root: pc043-internal-20261117-e995d2290328
Authority: the actual thirty-day source-amendment delegation; independent review before use

## Concrete coupling

The original root places the new attestor in T010. Existing test_evidence.py
belongs to T007 and test_source_roots.py belongs to T009, both predecessors of
T010. Putting executable attestor regressions into either predecessor would
couple its source qualification to the later T010 implementation. Embedding
test fakes in the runtime attestor or workflow would mix responsibilities.

## Exact bounded refinement

| Task or surface | Exact permitted addition or refinement |
| --- | --- |
| T010 files | Add only specs/043-private-connectivity-production/tests/test_delegated_evidence.py alongside the already approved attestor |
| Existing T007 reader/tests | Retain their accepted files; test closed human-root/delegated-form and read-only/instance semantics there |
| Existing T009 source-root tests | Only directly affected assertions of CI/proof/privacy wiring in their existing accepted file |
| Existing T010 workflow entry points | Collect the one new attestor module as a fourth measured source suite; preserve all original three suites and every original gate/count/skip obligation |
| Existing T007 T010 CI guard | Require the four exact current suites; retain original three-suite human historical readers unchanged |
| Frozen feature inputs | Reconcile this one additional T010 file and the four-suite validation contract, then refresh all sixteen inputs and all 68 task lines before use |

No task identity, owner, class, dependency or verify command changes. The
T061 conditional aggregate-only handoff and independent child cases remain.
The attestor tests cover actual provider readback identity, qualified producer
activation, root/actor/time/scope, missing review, false verdicts and CLI privacy.
No test fabricates an actual project acceptance.

## Authority and unchanged limits

This is a source-scope decision inside the human-authorized implementation
purpose. After actual independent review, Codex may record a distinct delegated
C-01 source-scope acceptance before writing the new file. That source authority
does not authenticate implementation outputs or pass Q0-Q5. Qualified
protected-base activation is still required before the mechanism accepts
new evidence.

The human root, its eight immutable policy members, functional/target/financial
bounds, original private-proof producer, App scope, global human-only authority,
Sonar gates, supported artifact obligations and macOS/external-Q5 holds remain
unchanged. There is no new workflow, token permission or source publication.

## Actual delegated C-01 source-scope decision

Decision-by: Codex, distinct delegate under the actual human root
Accountable-owner: Brett Heap
Decision-at: 2026-11-17T10:18:51.198109+00:00
Reviewed-proposal: 7ed90134af760b0a68ca12601fc2f0fe098ee8ed
Decision: accepted for the exact one-file/four-suite refinement above

All nine independent Codex expert roles reviewed the exact proposal:
architecture, performance, security, QA, static/CI quality, contracts, integrity,
reliability and maintainability. Each returned no actionable finding. The
actual source record is made before the new test file is written. This is no
new human sign-off and no source-output authentication. The genuine human root
already delegates this bounded source-amendment procedure; the qualified
evidence producer must still be implemented/activated before evidence admission.
