---
Status: draft
Proposed: 2026-11-14
code_surface: none — Sonar service configuration and maintenance evidence only
target_release: implemented — verified service configuration; no code, contract bundle or runtime release
---

## Why

Sonar project opensoft_openxFactory has ten retained successful main analyses
and the existing Sonar way gate (ID 9), but no new-code definition. Its main
status is NONE, which does not establish acceptance. Brett directly authorized
repair on 2026-11-14 without weakening checks, changing billing or disturbing
active sessions.

## What Changes

- Preserve Sonar way's six existing conditions and all profiles, source scope,
  exclusions, permissions, issue dispositions and history.
- Use the earliest retained successful main analysis as a fixed reference:
  d20bb52c-64fd-4090-986a-fd993f44ff86, source
  8480378acd806b112ebd0462e18a86a9026ab155, analyzed
  2026-09-09T19:37:08-04:00. Do not choose the current analysis, shorten a
  rolling window or clear debt to obtain green.
- Trigger/observe a fresh actual-main analysis, record its computed conditions
  faithfully, and distinguish restoring computation from repairing surfaced
  findings or providing measured coverage.
- Verify operating checkout/session preservation and record the before/after
  configuration. A failing computed gate remains a failing gate.
- Hand implementation to exactly one feature:
  [Speckit 043](../../../specs/043-sonar-quality-gate-recovery/tasks.md).

## Capabilities

### New Capabilities

- sonar-gate-computation: restore explicit historical assessment for the
  existing project without relaxing any acceptance condition.

### Modified Capabilities

None.

## Impact

Only the existing Sonar project's missing definition and dated maintenance
evidence. No runtime, contract, provider pin, credential, billing, visibility,
profile, rule, threshold, source/test classification or issue-status change.
Hermes' separate capacity investigation remains in its owning repository.
