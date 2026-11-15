# Feature Specification: P1 security boundaries
Feature Branch: 045-p1-security-boundaries
Created: 2026-11-15
Status: draft
Input: Implement the P1 fixes, starting with credential/profile boundaries and
privileged CI dependencies; preserve sessions/history, checks and billing;
verify actual main.

## User Scenarios & Testing
### US1 — Private profile safety (P1)
Valid same-account refresh retains identity and unknown metadata. Escaping
names, unsafe file objects, wrong-account captures and occupied browsers refuse
before any unsafe side effect. Tests use synthetic injected stores only.

### US2 — Reproducible privileged CI (P1)
All current checks/fallbacks execute using fixed verified Python wheels and a
functional lifecycle-free CLI installation. Offline installation/version checks
must work with an empty isolated home and no provider credentials.

### US3 — Remaining P1 trust boundaries (P1)
Worker/report/control destinations and executable operands satisfy explicit
trusted contracts, retaining valid controlled multi-repository operations.

### US4 — Published-main proof and preserved history (P1)
Each merged phase passes required exact-head review/CI and actual-main Sonar.
Existing credentials, worktrees, sessions, historical source/receipts, baseline,
profiles, skips, census, freshness assertions and billing remain intact.

## Requirements
- FR-001: Bound profile names; reject traversal, absolute and option-shaped names.
- FR-002: Credential operations cannot follow substituted filesystem objects
  or affect outside data; files are private from creation, read-only/shared-write
  targets refuse, and concurrent writers cannot silently overwrite each other.
- FR-003: Retain merge and wrong-account-before-write semantics.
- FR-004: Validate authorized browser path before startup; preserve occupied state.
- FR-005: Privileged dependency bytes and versions are fixed and verified;
  installation runs no package lifecycle/build code, and the existing worker
  command remains functional without removing any fallback or check.
- FR-006: Repair remaining P1 roots, policy inputs, outputs and executable operands.
- FR-007: Coordinate legitimate release cuts and vendored/provider consumers.
- FR-008: Establish fixture provenance privately; retain unresolved uncertainty.
- FR-009: No waivers, coverage/source reclassification, skip additions, reduced
  thresholds or entitlement/billing changes.
- FR-010: Exact original 40-key tracking and actual-main acceptance per phase.

## Success Criteria
- SC-001: All 40 original P1 records have source/behavioral evidence and a verified
  outcome. An unresolved dependency remains incomplete and cannot count as fixed.
- SC-002: Every landed phase passes every existing gate condition and required
  check at the actual published main revision.
- SC-003: Every unsafe acceptance case refuses before outside/native-state
  damage; every corresponding legitimate case retains its intended result.
- SC-004: Original historical records and all unrelated active state remain
  intact; no skip addition, check relaxation or billing change is introduced.

## Key Entities
Authorized location; profile identity and native state; verified dependency set;
P1 key/repair evidence;
exact source/analysis identity; retained history and active session identities.

## Assumptions and Scope
One new OpenSpec/Speckit feature, phased PRs. The single-repository constitution
retains its existing draft status. No automatic activation against live state.
The PR #1320 triage remains separate and unchanged.
