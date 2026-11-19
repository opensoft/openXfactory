---
code_surface: openxFactory
target_release: deferred-allocation
sequenced_after: [authorize-private-connectivity-internal-production, preserve-delegated-source-proof-bootstrap]
---

# Proposal for an exact T010 proof compatibility binding

Status: draft
Kind: proposal
Proposed: 2026-11-19

## Why

A proposed T015 custody refinement changes one owner-scope input and preserves
all 68 executable task rows. The protected verifier accepts the original T010
C-01 proof under its qualified definition and refuses the same proof when its
subject is recomputed under the proposed successor definition.

## What Changes

- Preserve verification of the one exact accepted T010 C-01 proof at its
  original source definition and original review time during the approved T015
  definition refresh.
- Independently review the exact compatibility binding and test arguments
  before use. Verify fresh choices and source admissions against their own
  current subject and separately qualified outputs.
- Qualify the successor definition and all existing source checks before
  consuming the new Ops custody scope.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. The repair implements the existing requirement to preserve original
qualified evidence while requalifying an amended source scope.

## Impact

The executable change is limited to `specs/043-private-connectivity-production/verify-evidence.py`
and `specs/043-private-connectivity-production/tests/test_delegated_evidence.py`.
Record the matching approved owner scope and complete freeze in their existing
input files. Feature 043 remains the governing task list and acceptance model.
