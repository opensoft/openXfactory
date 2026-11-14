---
code_surface: openxFactory
target_release: deferred-allocation
sequenced_after: [commission-private-connectivity-production-evidence, amend-private-connectivity-evidence-bootstrap]
---

# Proposal: Verify private component source pins in coordinator CI

Status: ratified
Ratified: 2026-11-14 by Brett Heap. [Ratification record](review/ratification.md)
Kind: proposal
Proposed: 2026-11-14

## Why

Feature 043 has authenticated coordinator, neutral and package commissioning inputs, and an actual private Headscale source candidate. The coordinator's real-data inventory regression deliberately supports only its own Git store: admitting private component references now would fail the required checks. The ratified E scope requires affected-owner review before adding another source/test/CI path; source consent for the component does not grant private CI custody.

## What Changes

- Commission the exact read-only source-proof preparation and two existing CI entry points in [design](design.md), using existing GitHub App access with repository-scoped, contents-read-only tokens. Add no installation, permission, secret or billing setting.
- Prepare only the referenced immutable commit metadata in separate ephemeral owner Git stores outside the public coordinator checkout. Publish no private source, commit objects, headers, credentials or private checkout as coordinator artifacts, logs or caches.
- Give the real-data inventory regression an explicit, closed owner-to-root map. Missing credentials, wrong origin, unavailable objects or incomplete proof fail when private references exist; no local-object fallback, skip, rolling population or waiver is added.
- Refine exactly T009/T010's file envelopes and the source-CI custody clarification, then refresh the complete reviewed definition only after actual affected-owner acceptance. Preserve all 68 task identities, dependencies, owners, classes, cases and verification commands.
- Keep inventory proof separate from full source-evidence admission. A new actual extended source/CI packet still requires custodian authentication and default verification; existing accepted packets retain their historical reader and anchors.

## Capabilities

### New Capabilities

- private-connectivity-source-ci-proof: bounded private owner commit proof, ephemeral metadata custody and fail-closed real-data inventory checks in both existing coordinator CI jobs.

### Modified Capabilities

None. Existing source authentication, release, reachability and Q0–Q5 requirements remain mandatory.

## Impact

The exact surfaces, closed repository allowlist, proposed frozen-input changes and validation obligations are in [design](design.md). Brett Heap is already the accepted E/component source owner and source-evidence custodian; this packet requests acceptance of the additional CI/custody and task-file scope, without reopening those roles. It changes no published contract, bundle version or existing required check identity.

Continue through the sole [043 task list](../../../specs/043-private-connectivity-production/tasks.md). Brett ratified this exact source-CI/custody/file/refreeze scope; actual new producer/output authentication remains separate. [Coordinator #1310](https://github.com/opensoft/openXfactory/pull/1310), [Ops #628](https://github.com/opensoft/opsXfactory/pull/628), [domain #583](https://github.com/codeXfactory/codeXfactory/pull/583) and [Headscale #2](https://github.com/opensoft/Headscale-Install/pull/2) remain draft. Full Q0, Q1–Q5, actual release/tag publication, deployment, target execution, enrollment and commercial gates remain unaccepted.
