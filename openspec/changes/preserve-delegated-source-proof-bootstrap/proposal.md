---
code_surface: openxFactory
target_release: deferred-allocation
sequenced_after: [extend-private-connectivity-source-ci, authorize-private-connectivity-internal-production]
---

# Proposal: Preserve private source proof after delegated authentication

Status: draft
Kind: proposal
Proposed: 2026-11-17

## Why

The two required coordinator CI workflows read the preceding protected commissioning manifest before requesting the existing private commit-proof tokens. Their bootstrap accepts only the human authentication schema. Both exact predicates accepted the current reviewed human control and refused a synthetic delegated control with the new envelope shape. The already pinned proof producer independently requires the same human authentication schema. Once delegated T010 evidence becomes the protected base, a subsequent affected PR or push would fail during proof preparation.

## What Changes

- Keep the existing producer and its human commissioning checkpoint available for metadata-only proof preparation following a delegated source authentication.
- Limit the compatibility repair to the two workflow bootstrap blocks and their existing source-roots regression file. Keep all required checks, owner boundaries, token limits and source evidence admission.
- Qualify the transition and its next protected-base run before treating the delegated evidence path as ready to land.

## Capabilities

### New Capabilities

None. This compatibility repair operates within the existing coordinator CI proof capability.

### Modified Capabilities

None. The existing credential scope, source evidence verifier and production gates retain their current requirements.

## Impact

The two existing CI workflow files in T010 and the existing source-root tests in T009 are the sole executable paths. The producer, task fields, source authority, supported product and rollout gates keep their existing definitions.
