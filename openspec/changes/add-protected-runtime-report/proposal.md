---
Status: draft
Authored: 2026-11-16
Kind: governance
sequenced_after:
  - add-protected-runtime-hosting-issuance
  - fix-hosted-staging-refresh-budget
code_surface: openXwallet (proposed trusted qualification adapter, separately versioned internal protected report and isolated tests in feature017); openXfactory (this governance packet and generated corpus-ledger row only)
target_release: implemented (future source realization after explicit profile acceptance and implementation commissioning; no activation or bundle cut)
---

## Why

Source-accepted openXwallet #75 completes isolated lifecycle ownership and cleanup,
but no connected protected qualification runner or protected report exists. The
accepted hosting plan reserves any new closed report/case vocabulary to factory
source review and owner acceptance before T012T implementation.

## What Changes

- Propose `openxfactory-protected-runtime-report-internal-v1` as a separate,
  bounded factual projection of one independently authenticated operational run.
  Keep the existing source/fixture profile and its case vocabulary unchanged.
- Define exact report fields, required semantic/live case slots, eligibility,
  safe errors and independent cleanup binding in the [design](design.md).
  Constructor labels, supplied pass booleans, offline pytest and fixture reports
  cannot establish protected-machine provenance.
- Connect later source realization to the existing owning-wallet proof, exact
  replay refusal, valid-signed audience/environment negatives, worker denial and
  RunLifecycle cleanup. Reporting itself has no I/O or mutation authority.
- Preserve seven service roles, eight source roles, three dispatch inputs, all
  accepted budgets, deadlines, neutral APIs/pins and refusing operational defaults.
- Prepare only. The sole implementation list remains openXwallet feature017
  tasks.md, proposed T012T01-T012T06. Profile acceptance, implementation, T013
  operational authority, T014 live qualification and T015 delivery stay separate.

## Capabilities

### New Capabilities

- `protected-runtime-report`: authenticated evidence eligibility, a closed protected
  report projection, privacy/compatibility and honest isolated qualification.

### Modified Capabilities

None under canonical `openspec/specs/`. This is the separate report-source decision
anticipated by `add-protected-runtime-hosting-issuance`; neither frozen predecessor
packet is edited. No canonical neutral wallet or MFA contract is introduced here.

## Impact

The factory owns the proposed grammar and acceptance semantics. openXwallet owns
future internal `hosted/qualification.py`, `hosted/evidence.py`, explicit trusted
CLI integration and tests under feature017. The adapter implements no new neutral
contract. No runtime source, workflow, dependency, release inventory, source pin,
credential, environment or service changes in this preparation.

Baseline: adapter #75 accepted at `dbe855cf3a41475426cd1329ca46d7b95dee2905`,
landed normally as `d832709a1119c17014287cd15ff8661bfd758cc4`. Its
[post-merge source run](https://github.com/opensoft/openXwallet/actions/runs/43887121548)
passes 2,322 full tests and 2,017 required native cases. That result is source
qualification, not a protected pilot or report.

See [requirements](specs/protected-runtime-report/spec.md), [handoff](tasks.md)
and [preparation evidence](evidence.md). This draft is not ratified. Setup and
protected dispatch remain unauthorized; feedback is deferred and neither historical
blocked write is replayed.
