---
Status: draft
Authored: 2026-11-15
Kind: governance
sequenced_after:
  - add-protected-runtime-hosting-issuance
code_surface: openXwallet (hosted read budgets, finalization composition, isolated tests and feature 017); openXfactory (this governance packet and generated corpus-ledger row only)
target_release: implemented (source candidate after review and owner ratification; no activation or bundle cut)
---

## Why

The accepted T012O finalizer makes six fresh protection observations across caller
and independent authority. T012Q correctly refuses the second observation under
the accepted three-read budget; omitting a recheck or resetting its counter would
weaken the accepted safety boundary.

## What Changes

- Propose a trusted finalization-only allocation: six complete observations,
  three reads each (environment plus at most two bounded policy pages), eighteen
  protection reads and twenty-eight aggregate GitHub reads across caller and
  independent authority. Ordinary admission/correlation retains three/thirteen.
- Share one ledger across independent decisions, including correlation high-water,
  group counters, snapshot count and earliest authority. Preserve independent
  recomputation, all current reads, original ten-second wall/monotonic bounds,
  per-request TLS limits and no retry/cache/freshness relaxation.
- Implement and qualify only the isolated adapter candidate in existing feature
  017. Owner source ratification of the reviewed pair remains separate.

## Capabilities

### New Capabilities

- `hosted-protection-read-budget`: explicit bounded finalization allocation and
  caller/authority shared accounting under the enclosing deadline.

### Modified Capabilities

None under canonical `openspec/specs/`. This narrowly amends D7 of the frozen
`add-protected-runtime-hosting-issuance` decision for the finalization operation
only; the accepted packet remains byte-identical. No neutral/wire profile changes.

## Impact

The factory owns the amended internal limits; openXwallet owns the implementation
and sole executable feature017 task list. Existing v1/defaults, source/control and
correlation limits, ARM/key/private limits, pins, contracts, roles and workflows
remain unchanged. This is a source candidate, not source acceptance, staging,
setup, dispatch, deployment or live qualification. T012R-V and T013 remain gated.
Feedback is deferred and neither blocked/denied write is replayed.
