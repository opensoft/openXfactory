---
code_surface: none — source-governance record only; no implementation, tenant or rollout operation
target_release: implemented — protected identity-policy record; separate owner implementation and operation gates remain due
sequenced_after:
  - authorize-private-connectivity-internal-production
  - commission-hosted-domain-production
---

# Align the private-connectivity MCP identity handoff

Status: draft
Kind: governance
Authored: 2026-11-18

## Why

The Feature 043 delegation still describes an EdDSA issuer-key route. The
selected codeXfactory MCP workload already has a ratified owner decision
for Opensoft Entra v2.0, a dedicated resource audience, and an additive RS256
verification path. Brett approved the exact alignment wording on November 18.

## What Changes

- Record the approved replacement for the MCP identity row as a separate
  amendment anchored to the reviewed delegation and human decision.
- Identify the Domain and Ops owner prerequisites for the follow-up C-01
  scope and complete frozen-definition refresh.
- Preserve the Hosted Headscale Keycloak identity path and existing Q0–Q5,
  spend, caller-admission and operating gates.

## Capabilities

### New Capabilities

None. This packet records a product-specific policy decision and its source
handoff.

### Modified Capabilities

None. The approved work continues to use the existing private-connectivity
and hosted MCP requirements and the separately governed owner changes.

## Impact

This packet records approval of the wording in design.md. The affected-owner
reviews, exact file and command scopes, refreshed feature definition and
actual source evidence still govern implementation. The existing resource
registration and caller decisions retain their separate authority.
