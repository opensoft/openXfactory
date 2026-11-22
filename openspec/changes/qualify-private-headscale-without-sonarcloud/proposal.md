---
sequenced_after:
  - authorize-private-connectivity-internal-production
  - commission-headscale-production
---

# Qualify the private Headscale package without SonarCloud

Status: ratified
Ratified: 2026-11-22 by Brett Heap. [Ratification record](review/ratification.md)

## Why

T023 releases a private package from opensoft/Headscale-Install. The rollout owner directed the team to skip SonarCloud for that repository and keep the existing zero-new-spend constraint.

## What Changes

- Move private Headscale release qualification to exact, independently reviewed source and CI evidence with a locally evaluated quality gate.
- Preserve the existing guarded runner tests, measured code coverage, security and quality checks, and immutable release readback. Require a reviewed criterion-by-criterion mapping from the current gate before enabling the replacement.
- Restrict the amendment to T023 and its evidence validation. Keep the public openXfactory post-merge Sonar requirements and the rest of the rollout dependency graph in force.
- Preserve the cancelled historical Sonar analysis and the draft proposal in PR #1346 as source records.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `private-connectivity-internal-autonomy` gains the exact private T023 exception and replacement source-quality criteria.
- `headscale-production-package` requires actual, independently verifiable owner CI and release evidence for the private package.

## Impact

Affected owners are Headscale-Install for T023 and openXfactory for its source evidence and frozen definition. Approval must name the exact tool, source, test and verifier paths before implementation. Q0–Q5 still govern staging and rollout. macOS and external Q5 are deferred.
