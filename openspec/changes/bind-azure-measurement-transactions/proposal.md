---
Status: draft
Authored: 2026-11-21
Kind: governance
sequenced_after:
  - add-protected-runtime-azure-composition
code_surface: openXwallet (existing feature017 T013P05 local/remote measurement and tests only after paired source acceptance); openXfactory (this governance packet and generated corpus ledger only)
target_release: implemented (future isolated source candidate only after paired acceptance; no activation, release cut, setup or dispatch)
---

## Why

Commissioned P05 eligibility probes show that the accepted direct measurement
response and existing shared clients do not together provide an explicit fresh
request binding: the response has no nonce, the transport drops response headers,
and the old observation client requires another closed wrapper. Resolve that
source seam before dependent code, as the accepted P05 plan requires.

## What Changes

- Propose one separate direct internal response profile,
  `openxfactory-azure-local-measurement-internal-v2`, retaining every v1 field
  and adding exactly `request_nonce` to bind the complete bytes to one selected
  authenticated request. Preserve v1 and all predecessor packets unchanged.
- Specify the closed selected request, authenticated peer/role/source/scope,
  consume-before-measure nonce handling and original deadline/read accounting.
  Nonce echo alone never replaces actual local measurement or current authority.
- Permit a dedicated P05 client over unchanged bounded PrivateHttps; do not add
  an operation to ObservationClient, introduce a response wrapper, expand the
  16 KiB body cap or allocate another budget.
- Keep independent local kernel/manager/observer evidence and independent
  complete-byte control derivation mandatory. Prove the complete positive and
  rejection controls before claiming source eligibility.
- Hand off to the existing openXwallet feature017 T013P05 row, without another
  feature or executable task list. New wire semantics require exact paired
  source acceptance before dependent implementation.

## Capabilities

### New Capabilities

- `azure-measurement-transactions`: direct, fresh-request-bound local measurement
  and selected remote acceptance over the existing P3 machine-only composition.

### Modified Capabilities

None under canonical openspec/specs. This additive internal v2 profile composes
accepted P3 R03/R06/R11 semantics without rewriting v1, frozen predecessor packets,
neutral APIs, static/full/report profiles or the default operational refusal.

## Impact

Factory owns the proposed internal transaction grammar. openXwallet owns local
adapters, dedicated client and tests through feature017's existing T013P05;
consumer058 T002, operational execution pins and independent human acceptance
remain gated. Four actual process/TLS eligibility probes pass, including a
complete 8,860-byte v1 fixture, but manager/remote finalization/budget eligibility
and P05 implementation are not completed by those probes.

This is proposal preparation under the commissioned P05 compatibility guard.
The proposed source decision is unratified. Publication, source acceptance and
implementation of v2 remain separate gates. P06-P09, actual services/roles,
setup/dispatch and live/human/consumer acceptance are ungranted. Feedback deferred;
historical blocked writes unreplayed.
