---
Status: draft
Proposed: 2026-11-14
code_surface: openxFactory — source hardening, behavioral regressions and measured CI analysis
target_release: implemented — maintained tooling and analysis CI only; no contract bundle or runtime activation
---

## Why

The restored main Sonar gate computes ERROR for existing reliability/security
findings and cannot assess coverage through automatic analysis. Brett directly
authorized fixing the remaining findings and adding genuine coverage until
merged main satisfies the existing gate, while preserving sessions, history
and billing.

## What Changes

- Fix the identified nullable-flow, redundant assignment, preflight, path and
  command operand boundaries with counterexample tests.
- Keep dated acceptance verdicts/logs and the original Git preimage; identify
  the repaired replay driver's provenance without rewriting past results.
- Run the existing complete required suite under branch- and subprocess-aware
  coverage; retain its census, exact skip budget and named freshness guard.
- Import real reports using CI analysis in the same Sonar project with its
  existing organization secret. Switch off duplicate automatic analysis only
  for this controlled migration.
- Classify genuine test modules as tests using an explicit audited inventory;
  retain every existing production source and report zero-hit source files.
- Keep the September historical reference, six existing gate conditions,
  profiles, issue history and billing. No suppression, threshold reduction,
  blanket evidence exclusion or fabricated coverage is authorized.
- Hand off to exactly one feature:
  [Speckit 044](../../../specs/044-sonar-quality-remediation/tasks.md).

## Capabilities

### New Capabilities

- sonar-measured-quality-acceptance: code fixes and complete measured CI
  evidence for the existing project quality gate.

### Modified Capabilities

None.

## Impact

Owning source validators and replay tools, behavioral tests, a separate
analysis-only dependency lock, coverage/scanner configuration and CI workflow.
No contract/schema, provider pin, application permission, billing or active
session mutation is planned. Any discovered contractual impact must be
recorded before its dependent implementation. Historical run records remain
their original dated claims, not acceptance of the repaired driver.
