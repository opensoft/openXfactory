---
code_surface: openxFactory
target_release: deferred-allocation
sequenced_after: [extend-private-connectivity-source-ci, remediate-sonar-findings-and-coverage]
---

# Proposal: Classify private-connectivity source tests in the measured Sonar gate

Status: ratified
Ratified: 2026-11-14 by Brett Heap. [Ratification record](review/ratification.md)
Kind: proposal
Proposed: 2026-11-15

## Why

Main's newly landed measured Sonar gate recognizes the 040 test tree explicitly, but currently treats all three 043 test modules as production source. The same missing classification occurs in its owned-source inventory and scanner configuration. Source work for 043 needs their classifications to agree before its extended CI qualification can complete.

## What Changes

- Recognize only specs/043-private-connectivity-production/tests/ as an additional actual test tree in the existing coverage inventory and scanner test inclusion list. Keep every production Python source in that feature measured, including zero-hit sources.
- Add regression coverage proving agreement between the inventory and scanner classification, while preserving all existing test trees, production paths, coverage thresholds, check identities, skipped-count pins and named verdicts.
- Record Brett Heap's affected E owner acceptance of exactly the three additional source/test/configuration paths in [design](design.md), T010's matching file refinement and the complete definition refresh. Existing owner roles and the sole task registry remain in place.
- Requalify the actual source/CI outputs after implementation and obtain distinct custodian authentication. Preserve accepted historical anchors and the withdrawn source-CI preparation; source scope acceptance cannot authenticate future observations.

## Capabilities

### New Capabilities

None. This is a tooling classification repair, with skip_specs declared in the change metadata.

### Modified Capabilities

None. The existing exhaustive measured-production-coverage and source-evidence requirements remain unchanged.

## Impact

Only the exact shared surfaces and existing 043 governance/output paths listed in [design](design.md) are accepted through the [actual owner decision](review/ratification.md). Implementation and validation may proceed within that scope; actual new output authentication remains separate. All four PRs remain draft; full Q0, Q1–Q5, release/tag publication, target access, deployment, enrollment, paid resources and commercial gates remain pending.
