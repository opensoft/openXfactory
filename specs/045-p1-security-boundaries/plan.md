# Implementation Plan: P1 security boundaries
Branch: 045-p1-security-boundaries
Date: 2026-11-15
Status: draft

## Summary
Implement the directly authorized P1 backlog through one task list and phased
PRs: private profile safety and privileged CI installers first; remaining P1
writers/executables and release/vendor dependencies follow. Preserve 044 and
PR #1320 as their original evidence.

## Technical Context
Python 3.12/POSIX in py-bench, Git/GH in cloud-bench, pytest, actionlint,
existing coverage pipeline and pinned providers. New CI-only locks live under
.github so the existing runtime release lock remains byte-identical.

## Constitution Check
OpenSpec precedes implementation, draft authority is not ratification, neutral
ownership and current governance remain. User's direct request authorizes this
repair and main verification; no credential rotation, session interruption,
runtime activation or billing mutation. Existing exact skip/census/freshness,
coverage inventory, gate conditions and historical reference are retained.

## Project Structure
openspec/changes/remediate-p1-security-boundaries/ governs the decision.
specs/045-p1-security-boundaries/ owns requirements, tasks, analysis and receipts.
Owning scripts/tests and CI-only locks implement the repair. Contract/release
and vendor-byte updates obey existing owner/consumer ordering.

## Governed invariants
- .github/workflows/ — privileged dependency behavior; check names/participation intact.
- .github/requirements/ — fixed tooling-only dependency artifacts.
- .github/worker-cli/ — fixed lifecycle-free worker installation closure.
- scripts/safe_tooling_io.py — trusted filesystem boundary.
- scripts/nlm_auth.py — private credential identity/ownership/write boundary.
- scripts/validate-openspec-cli-pin.py — pinned verifier byte parity and integrity.
- contracts/ — published versioned corpus; only legitimate release changes.
- specs/045-p1-security-boundaries/ — current feature decisions and measured evidence.

## Verification
Meaningful pre-fix counterexamples and valid controls; focused changed-child
suites; offline hash/wheel and CLI version installation; actionlint; complete
unchanged required CI and measured coverage; exact-head hosted Codex review;
actual merged-main gate/analysis/issue readback; preservation fingerprints.

## Landing Strategy
Phase 1 credentials + privileged installers, then remaining P1 repair families.
Each phase has independent reviewed exact-head CI/main acceptance. Do not
advance foreign pins before children publish or hand-edit historical inventories.
