# P1 security boundary repairs
Status: draft

This feature implements the directly authorized P1 repairs from the separate
[triage PR #1320](https://github.com/opensoft/openXfactory/pull/1320).
It preserves completed feature 044 and original issue/history identities.

- [Governance proposal](../../openspec/changes/remediate-p1-security-boundaries/proposal.md)
- [Boundary design](../../openspec/changes/remediate-p1-security-boundaries/design.md)
- [Capability delta](../../openspec/changes/remediate-p1-security-boundaries/specs/p1-tooling-security-boundaries/spec.md)
- [Feature requirements](spec.md)
- [Implementation plan](plan.md)
- [Sole implementation task list](tasks.md)
- [Research and dependency decisions](research.md)
- [Clarifications and applied answers](clarify-questions.md)
- [Consistency analysis](analysis.md)
- [Current specification quality checklist](checklists/requirements.md)
- [Original 40 P1 keys](p1-keys.json)
- [Phase 1 local evidence](phase1-local-evidence.md)

Phase 2 authority/I/O refinements are recorded in the implementation plan.

Phase 1 repairs profile/state boundaries and privileged CI installers. Required
exact-head review/CI and actual merged-main acceptance are separate pending
steps. Remaining P1 worker/report/control, executable, vendor and fixture
provenance work stays explicit in the task list.

[Phase 2 local evidence](phase2-local-evidence.md) records artifact/policy verification.

[Phase 3 local evidence](phase3-local-evidence.md) records execution-boundary verification.
