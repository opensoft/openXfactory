---
Status: draft
Authored: 2026-11-25
Kind: governance
sequenced_after:
  - bound-remote-lifecycle-accounting
code_surface: openXwallet (existing feature017 T013P08; source-selected lifecycle descriptor wire, original controller-store retention/claim grammar, source construction and tests); openXfactory (this source-only contract/handoff packet, README records and generated corpus ledger at publication)
target_release: implemented (source acceptance only; dependent runtime implementation and operational grants remain separate)
---

## Why

The accepted P08 accounting policy cannot be selected safely because the caller
has no authenticated original-registration manifest or retained-store capability.
Fresh Gate A passes15 controls; Gate B's input/contract audit confirms that
registration/status/acknowledgement replies carry digests, not that capability.
This proposal makes the original owner-to-caller handoff explicit before code.

## What Changes

- Propose a fixed companion lifecycle wire that carries an owner-derived descriptor
  on the existing primary registration and independent stage acknowledgement;
  preserve the old v1 wire exactly and add no manifest-lookup RPC.
- Bind the complete original credential-resource projection to registration,
  scope, unit, resource epoch and original lifecycle-store identity. Capture only
  actual authenticated transport evidence, never caller-built JSON or counts.
- Retain it in a source-selected v2 of the existing original controller StageStore,
  with original identity/UID/scope fencing and no new backend, file or resource.
  Atomically consume a handoff slot keyed by the original launch_ref before
  authority I/O. No separate finalization NonceStore or recreated approval.
- Materialize a sealed caller view locally from that original controller store
  before per-N policy selection. This route requires the companion's trusted
  caller/controller to retain access to that existing store; a remote-controller
  deployment without that access is ineligible, not a hidden lookup fallback.
- Preserve the accepted accounting commitment and caps, existing RPC schedule,
  three inputs, seven runtime/eight source roles, fourteen managed resources,
  neutral/static/full/report grammars, deadlines and default refusal. Measure
  actual complete transport and local retention work; any mismatch returns to
  governance instead of raising a cap or omitting a check.

The proposed design selects staging/retention. It remains unratified; no new wire
or record implementation is inferred. An explicit extra-read design would instead
need a different sequence and measured accounting amendment.

## Capabilities

### New Capabilities

- `original-registration-handoff`: source-selected authenticated descriptor capture,
  original controller retention, one-original-attempt conservation and caller materialization.

### Modified Capabilities

None under canonical openspec/specs. Frozen parent packets and accounting policy
bytes stay unchanged; this proposed internal contract supplies their missing port.

## Impact

openXwallet owns the paired feature017 registration subplan and existing unchecked
T013P08 row. Planned owner modules include companion lifecycle transport, controller
store/route construction and remote_evidence; ordinary lifecycle/StageStore APIs
remain v1. The new descriptor is internal, not a neutral wallet/MFA profile or an
approval capability. No new source task list, external dependency or credentials
are introduced by this source packet.

Factory1368 and wallet106 are source accepted and landed normally as8833c7d001b3a
and12cdf3161c5d with identical ratified trees. Their independent main CI is tracked
separately. The15-case prototype was archived and product runtime/tests restored;
independent read-only audit checked36 databases and155 file/link hashes before
151 temporary entries and three owned containers were removed.

Publication requires the actual paired PR identities and generated ledger, fresh
CI/local Codex review and exact owner source acceptance before dependent code.
P09, T001/T013/T014/T015, live/human/consumer acceptance, setup and dispatch remain
separate. Feedback deferred; historical blocked writes unreplayed.
