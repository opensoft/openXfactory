---
Status: draft
Authored: 2026-11-19
Kind: governance
sequenced_after:
  - prepare-protected-runtime-qualification
  - add-protected-runtime-hosting-issuance
  - add-protected-runtime-report
code_surface: openXwallet (proposed Azure deployment composition, local/remote measurement and lifecycle adapters, explicit source-selected activation route and isolated tests in feature017); openXfactory (this governance packet and generated corpus-ledger row only)
target_release: implemented (future isolated source only after explicit source acceptance and implementation commissioning; no activation, setup, dispatch or bundle cut)
---

## Why

The accepted isolated runtime cannot become a deployed three-host pilot merely by
filling service URLs: its measurement/lifecycle interfaces are local, Azure deletion
has no documented generation precondition, and GitHub supplies a per-job OIDC
request endpoint. Brett accepted T013-S1 as a design basis only and commissioned
this P3 proposal/plan; actual composition and operational authority remain absent.

## What Changes

- Propose a narrow Azure composition over accepted T013-S1: three QA Linux hosts,
  local trusted worker-host measurement/lifecycle helpers, separate control/gate
  authorities, retained private state and an external watchdog. Keep roles subject
  to confirmation and common privileged administrators explicitly trusted.
- Govern closed internal deployment/retirement and remote measurement evidence,
  preserving existing process/credential/file RunPlan semantics, full runtime and
  static-v2 profiles, seven runtime roles, eight source roles and three inputs.
- Require permanent resource-name tombstones, sole-writer/one-shot creation and
  provider-authenticated generation/operation readback for infrastructure retirement;
  unsupported writer exclusion or per-kind semantics refuse. No Azure CAS-delete,
  wildcard RG deletion or timer-as-deadline claim.
- Define selected managed-image construction, at most one data disk per trusted
  host, and trusted per-job runner endpoint capture. No marketplace URN is passed
  as a managed-image ID and no worker environment supplies trust.
- Propose a separately reviewed source-selected companion entrypoint/workflow
  route. Preserve the existing default operational_bindings refusal verbatim;
  documents, environment flags and fixture credentials cannot activate it.
- Hand off only to openXwallet feature017's proposed T013P tasks and scoped P3
  subplan. Prepare substantive future isolated acceptance controls without
  implementation, executable deployment configuration, credentials or live use.

## Capabilities

### New Capabilities

- `protected-runtime-azure-composition`: explicit source-selected Azure hosting,
  authenticated local/remote provenance, retained generation ownership and honest
  source/deployment/retirement acceptance over the existing machine-only runtime.

### Modified Capabilities

None under canonical openspec/specs. Frozen predecessor packets, neutral wallet/
MFA contracts, existing static-v1/static-v2/full-runtime-v1 and protected-report
profiles remain unchanged. New internal composition evidence is separately owned
here; it must not be smuggled into old RunPlan kinds or old report fields.

## Impact

Factory owns this proposed composition and internal evidence semantics.
openXwallet owns the later adapters, service packaging, selected activation source
and tests, governed by feature017's sole executable task list. codeXfactory keeps
its consumer handoff and blocked058 T002; no executable consumer lock or pin moves.
No keyholding/provider runtime belongs in this factory repository.

Design basis accepted: adapter081dad41cfb42a3bc58aefe356bb6d424fab871d with
consumer049ede52b6ee03f15a57ecf7cdb9517002d8714f, for design only, roles subject to
confirmation. This P3 technical decision is a new unratified candidate. Source
acceptance and explicit isolated implementation commissioning precede any code;
P2 selections, P4 setup, P5 readback, P6 dispatch, P7 actual-run authority, P8/T014
qualification and T015 consumer/human acceptance remain separate. Feedback deferred;
all blocked writes and optional rejected public metadata publications remain unreplayed.
