---
Status: draft
Authored: 2026-11-15
Kind: governance
sequenced_after:
  - add-protected-runtime-hosting-issuance
  - fix-hosted-protection-read-budget
code_surface: openXwallet (protected staging accounting, current correlation, isolated tests and feature017); openXfactory (this governance packet and generated corpus-ledger row only)
target_release: implemented (source candidate pending review and owner ratification; no activation or bundle cut)
---

## Why

Local review of adapter #71 reproduced actual inert launches after a source hold,
main source or consumed operator context was revoked during durable cleanup
registration. A complete fresh protected observation after that blocking work
cannot fit the accepted ordinary three-protection/thirteen-total allocation.

## What Changes

- Propose a trusted protected-staging-only allocation for at most two complete
  observations under one original Decision: eight correlation, six protection,
  eight source and four control reads, twenty-six aggregate GitHub reads, and
  sixteen private operations. Each correlation reader retains its four-read cap.
- Observe once before any reservation, then again after acknowledged cleanup and
  before opening the one private start request. Propagate the earliest observed
  expiry into that request. Keep all source/control/hold/context/protection/run/
  eligible-human review checks; never renew clocks, reset counters or reuse facts.
- Keep ordinary admission at 3/13, finalization at six observations/18/28, and all
  ARM/key/default private limits, v1/default activation and neutral pins unchanged.

## Capabilities

### New Capabilities

- `hosted-staging-refresh-budget`: bounded complete protected observations before
  reservation and after durable cleanup, including shared enclosing accounting.

### Modified Capabilities

None under canonical openspec/specs. This amends the protected-staging operation
in frozen hosting D2/D6/D7/D8 without editing either accepted decision packet.

## Impact

The factory owns this internal allocation; openXwallet feature017 remains the
sole executable task list. Its paired T012R review correction also closes worker
process-control and partial-read issues, binds reply run/source fields, and
normalizes isolated source-test identities/runtime selection. These enforce the
accepted boundary without changing neutral APIs or protected workflow YAML.

The amendment and adapter remain unratified source candidates. Present exact
paired heads for owner ratification, then land governance before adapter only
after later authorization and green checks. Setup/dispatch and T012S-V remain
unauthorized, feedback deferred, and neither blocked/denied write is replayed.
