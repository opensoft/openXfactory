## Context

The current main analysis is successful but the quality gate status is NONE.
The default gate is already Sonar way (ID 9). Public API
api/project_analyses/set_baseline explicitly supports selecting a retained
analysis as the New Code Period baseline. It preserves analysis identities and
overrides the otherwise absent definition.

## Decision

Select the earliest retained main analysis, never the latest successful
snapshot. Save all gate conditions and project settings before mutation.
Require a fresh main revision analysis and report every computed result,
including errors and missing coverage; do not mistake an upload or neutral
check for a computed passing gate.

## Verification and recovery

Read the manual reference marker and resulting period back. Compare gate
conditions/settings/profiles and retained analysis IDs with baseline.
The recovery operation is api/project_analyses/unset_baseline for this project;
it restores the missing-definition state and is not an acceptance mechanism.
No recovery or issue disposition is performed merely to make a gate green.
Preserve active operating worktrees, session identities and unpublished work.
