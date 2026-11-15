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
- FR-002: No-follow descriptor I/O, regular owned single-link credential files,
  private creation mode, atomic per-file replacement, staged pair and writer lock.
- FR-003: Retain merge and wrong-account-before-write semantics.
- FR-004: Validate authorized browser path before startup; preserve occupied state.
- FR-005: Fixed hash-verified wheel-only privileged Python dependencies and locked
  script-free functional worker CLI; no fallback/check removal.
- FR-006: Repair remaining P1 roots, policy inputs, outputs and executable operands.
- FR-007: Coordinate legitimate release cuts and vendored/provider consumers.
- FR-008: Establish fixture provenance privately; retain unresolved uncertainty.
- FR-009: No waivers, coverage/source reclassification, skip additions, reduced
  thresholds or entitlement/billing changes.
- FR-010: Exact original 40-key tracking and actual-main acceptance per phase.

## Success Criteria
All scoped P1 keys have verified source fixes or explicitly evidenced contextual/
external dependencies; no false completion or automatic closure on unchanged
source. Every landed phase passes unchanged checks and existing quality gate.
Unsafe counterexamples refuse, legitimate behavior remains and preservation
fingerprints/session records survive.

## Key Entities
Trusted invocation/state root; validated profile; held directory descriptor;
staged native profile pair; fixed dependency closure; P1 key/repair evidence;
exact source/analysis identity; retained history and active session identities.

## Assumptions and Scope
One new OpenSpec/Speckit feature, phased PRs. The single-repository constitution
retains its existing draft status. No automatic activation against live state.
The PR #1320 triage remains separate and unchanged.
