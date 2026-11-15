---
Status: draft
Proposed: 2026-11-15
code_surface: openxFactory — P1 credential, filesystem, executable and CI dependency boundary repairs
target_release: implemented — maintained tooling and workflows; release-member changes require their own legitimate release cut
---

## Why

Brett authorized the P1 repairs from the separate 110-finding triage in
opensoft/openXfactory PR #1320, starting with credential/profile boundaries
and privileged CI dependencies, preserving active sessions, history, checks
and billing, with actual-main verification. Forty original records share
several trust boundaries; fixing them requires behavioral counterexamples
rather than status waivers or suppressions.

## What Changes

- Validate profile identity and authorized browser paths before browser/auth
  side effects; refuse link/non-regular/foreign-owned credential state and use
  private staged atomic writes while retaining account-mismatch and metadata
  merge semantics. Do not touch live state to activate these source repairs.
- Replace privileged unpinned/source-build-capable installs with reviewed
  hash-locked binary Python dependencies and an integrity-locked, lifecycle-free
  worker CLI installation. Preserve fallback participation and permission scope.
- Repair remaining P1 worker/report/policy/output boundaries and executable/
  operand contracts in phased PRs. Maintain valid authorized multi-repository
  use, private-state authority and fail-closed validation.
- Privately establish negative-credential fixture provenance; never test the
  value for liveness or rewrite frozen history. Issuance remains unknown.
  Replace the current literal with an explicit nonissued marker while retaining
  the same forbidden-property refusal and unchanged credential scanner/schema.
  Although excluded from the digest membership, this contracts/ conformance
  example follows the broader AGENTS.md rule and requires a proper new cut.
  Old inventories, tags and the original creation commit remain immutable.
- Preserve baseline, profiles, all gate conditions, production source coverage,
  existing skip/freshness/census controls, original 110 IDs and historical
  receipts. No credential rotation, session interruption or billing change.
- Hand off to exactly one task list:
  [Speckit 045](../../../specs/045-p1-security-boundaries/tasks.md).

## Capabilities

### New Capabilities

- p1-tooling-security-boundaries: explicit authority and safe I/O/installation
  contracts for the retained P1 maintenance backlog.

### Modified Capabilities

None. Existing governed acceptance and release semantics remain; later
contractual refinements must be recorded before dependent implementation.

## Impact

scripts/nlm_auth.py; privileged doc-health/review workflows and isolated
CI-only dependency locks; worker/report/review control helpers; OpenSpec pin
validator consumers; PostgreSQL command-template boundary; behavioral tests
and new feature evidence. Canonical contracts, release inventories and vendor
copies change only with their required coordinated release/provider process.
The scope does not absorb feature 044 or the separate triage publication.
