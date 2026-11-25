---
Status: draft
Authored: 2026-11-24
Kind: governance
sequenced_after:
  - add-protected-runtime-azure-composition
code_surface: openXwallet (existing feature017 T013P08 after exact paired source acceptance); openXfactory (this source-policy packet, non-product inventory reproduction tests, measured baseline pin-class registration and generated corpus ledger)
target_release: implemented (source acceptance only; dependent isolated runtime implementation later; no activation or release cut)
---

## Why

P08 Gate A is eligible in an isolated source prototype. Gate B correctly refuses
before the complete lifecycle handoff under original private12 when nested
credential observations are prepaid. Counting only controller RPCs incorrectly
hides those physical requests. The accepted P08 subplan explicitly requires a
factory/adapter amendment when a complete handoff needs a changed budget.

## What Changes

- Propose `openxfactory-remote-lifecycle-accounting-internal-v1`, selected only by
  trusted source before I/O from the original registration credential-resource manifest.
- For its unchanged one-to-three credentials, bound complete handoff to12+2N
  private calls (maximum18) and one original runtime cleanup with independent
  audit to2+5N (maximum17). Separate audit-only observation is1+N (maximum4),
  without a cleanup resend or renewal. These allowances cannot be borrowed.
- Prepay each RPC plus the maximum physical nested work before sending. Preserve
  original consumed state, independent lifecycle checks and original deadlines.
- Leave ordinary private12, staging16, qualification39, GitHub/protection limits,
  phase clocks, byte caps, neutral profiles, roles, inputs, pins and default
  operational refusal unchanged. No new journal grammar or authority is proposed.

## Capabilities

### New Capabilities

- `remote-lifecycle-accounting`: a source-selected finite physical I/O policy
  for the first-pilot remote handoff and its separate original runtime cleanup.

### Modified Capabilities

None under canonical openspec/specs. This prospective internal policy refines P3
R02/R03/R07/R11/R12 without rewriting frozen parent packets or earlier policies.

## Impact

Factory owns this [policy and inventory](supporting-docs/call-inventory.md),
[design](design.md), [requirements](specs/remote-lifecycle-accounting/spec.md),
[recorded measurements](supporting-docs/measurements.json), and non-product
[reproducer](supporting-docs/derive-inventory.py). The reproducer checks frozen
record integrity and arithmetic; it authenticates no service and proves no runtime
positive. N1 and N3 were measured; N2 is a derived bound only.

openXwallet owns the paired `p3-entrypoint-accounting-plan.md` and the sole existing
feature017 T013P08 row. Experimental source was archived outside governed source;
runtime/tests/workflows were restored to prepared-plan commit75fc1feb3474.
Nineteen focused controls passed; full/native/hosted P08 qualification did not run.
The original budget failure remains authoritative until exact paired source
acceptance and fresh connected qualification prove the proposed bounds.

Current authority covers isolated P08 and this explicit fallback preparation.
Paired candidates are factory #1368 and adapter #106. The generated ledger now
names the actual PR. Hosted CI and local expert review are in progress; owner
source ratification remains pending. No source acceptance is inferred. P09,
T001/T013/T014/T015, live/human/consumer gates, setup and dispatch remain separate.
Feedback is deferred; historical blocked writes remain unreplayed.

## Publication evidence membership

The measured factory_base and adapter_base fields remain in measurements.json;
they are not removed to evade the derivation-pin sweep. Register this exact active
packet and its future archive paths in scripts/doc_health/pin_class.py: factory_base
is a repo-local measured derivation member with normal main/retention resolution;
adapter_base is a measured cross-repository member owned by openXwallet. Both are
current artifacts. No blanket non-member exclusion, historical exemption, resolver,
retention namespace or existing member changes. Existing pin-reachability tests
and hosted doc-health checks must cover the registration.
