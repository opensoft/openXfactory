---
Status: draft
Authored: 2026-11-14
Kind: governance
code_surface: openXwallet (proposed versioned plan finalization, hosting/issuance/readback adapters and isolated tests); openXfactory (governance and generated corpus-ledger row only)
target_release: implemented (future source realization after explicit profile acceptance/commissioning; no activation, deployment or bundle cut)
---

## Why

The accepted GitHub bootstrap adapter authenticates and correlates isolated jobs,
but actual hosting/issuance/readback clients and live qualification remain absent.
Research also found that static-v1 commits process/run-dependent composition and
policy digests before those values exist; callbacks alone cannot make a real
predispatch commitment. The accepted preparation handoff is adapter #66.

## What Changes

- Propose a separate `openxfactory-dispatch-selection-internal-v2` plan and explicit hosted phase protocol: read-only plan readiness before environment approval, then protected staging, measured finalization and unchanged full runtime/proof admission. Preserve v1, existing neutral contracts, three dispatch inputs and seven runtime service roles.
- Preapprove exact source/image/executable/policy/launch templates and all other configuration fields. Permit only enumerated host/provider-derived late fields; independently approve the actual final configuration. Never predict run/PID values or put dummy hashes in v1.
- Propose authenticated bounded GitHub/Azure/guest/issuer/state/scheduler clients and role-specific credential issuance over the T013 three-host QA design basis. Managed identity is a host boundary, and current wallet Ed25519 custody is software custody; neither principal labels nor Key Vault imply process/HSM isolation.
- Require durable acknowledged staging cleanup before launch, immutable full-plan takeover without a cleanup gap, and an independent external watchdog or explicitly ineligible control-host-loss case. Keep infrastructure retirement separate from process/file/credential RunPlan cleanup.
- Define source and isolated acceptance controls in the existing adapter feature 017 plan. The sole executable list remains its tasks.md; preparation commissions no implementation, token acquisition, App/permission/environment change, setup, dispatch or live receipt.

## Capabilities

### New Capabilities

- `hosted-runtime-finalization`: versioned static plan, phase-limited readiness, protected staging and independently approved actual-run/measurement finalization.
- `protected-runtime-hosting-issuance`: actual hosting/identity/readback/cleanup integration boundaries and source-only qualification for a protected machine pilot.

### Modified Capabilities

None under canonical `openspec/specs/`. This is an opt-in extension to accepted
`add-github-bootstrap-authentication`, `fix-protected-runtime-dispatch-bootstrap`
and `prepare-protected-runtime-qualification` decisions. Their frozen v1 packets
and neutral proof/registry/custody APIs are unchanged. New internal v2 semantics
require explicit owner source acceptance before implementation.

## Impact

Factory owns the composition and proposed internal grammar. openXwallet owns
future source and feature 017 planning/tasks; no live implementation belongs in
this repository. Concrete non-secret deployment candidates belong in the adapter
selection packet, not a canonical neutral contract. Three proposed Linux hosts,
coordinated main-update policy, distinct initiating human/reviewer, scoped Apps,
retained POSIX state and bounded spend/window are design inputs, not appointed
actors, reserved capacity, provisioned resources or issued grants.

See [design](design.md), [finalization requirements](specs/hosted-runtime-finalization/spec.md),
[hosting requirements](specs/protected-runtime-hosting-issuance/spec.md) and
[handoff](tasks.md). See [preparation evidence and publication gates](evidence.md). Source ratification/commissioning, T013 operational decisions,
setup, one dispatch, actual-run authority, cleanup, T014 qualification and T015
consumer acceptance remain separate. Feedback stays deferred and neither
historical blocked write is replayed.
