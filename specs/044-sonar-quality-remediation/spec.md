# Feature Specification: Measured Sonar quality acceptance

**Feature Branch**: 044-sonar-quality-remediation
**Created**: 2026-11-14
**Status**: draft
**Input**: Fix the remaining openXfactory Sonar findings and add real coverage
until main is fully green; preserve active sessions and historical evidence,
without weakening checks or changing billing.

## User Scenarios & Testing

### User Story 1 - Safe maintained tools (Priority: P1)

An operator can validate legitimate declarations and replay acceptance while
unsafe file, revision and browser-preflight inputs fail before side effects.

**Independent Test**: Positive fixture round trips plus outside-root, symlink,
option-operand, missing-row and optimized-Python refusal regressions.

**Acceptance Scenarios**:
1. Given a valid fixture under the invocation root, validation and output work.
2. Given an escaping path or invalid private copy, execution refuses safely.
3. Given optimized Python, all preflight security checks still run.

### User Story 2 - Measured quality acceptance (Priority: P1)

A maintainer receives genuine coverage and an evaluated existing gate for the
same commit that passed the complete required test suite.

**Independent Test**: Real subprocess coverage, XML inventory/path checks,
unchanged collection/skip/freshness guards, and actual server gate readback.

**Acceptance Scenarios**:
1. Given a zero-hit production file, the report includes its uncovered lines.
2. Given missing, stale or unresolved coverage, qualification fails.
3. Given the published candidate, all six existing conditions pass with the
   original historical reference and evaluated coverage at least 80 percent.

### User Story 3 - Preserved evidence and sessions (Priority: P1)

An operator keeps active work, original run receipts and analysis history
while the maintained implementation improves.

**Independent Test**: Before/after fingerprints, session identities, provider
pins, source provenance and dated receipt hashes.

**Acceptance Scenarios**:
1. Given an old driver PASS receipt, its original bytes and source preimage remain.
2. Given unrelated active worktree progress, maintenance preserves it.
3. Given the existing Sonar project, its identity, history and billing remain.

### Edge Cases

Escaping symlinks, sibling-prefix paths, non-regular or oversized files,
optimized execution, malformed Git output, cleared subprocess environments,
zero-hit namespace modules, foreign gitlinks, mislabeled tests, stale XML,
a missing coverage condition and flapping automatic issue closures.

## Requirements

- FR-001: Fix reported new-period reliability/security findings through source
  behavior and regressions, including a reopened attestation output finding.
- FR-002: Keep the original eleven-finding snapshot and driver preimage;
  do not claim an automatic closure on unchanged source as remediation.
- FR-003: Confine ordinary file operands to the trusted invocation directory;
  retain explicit private-state ownership, mode, descriptor and URL identity.
  Repository-governed attestation records retain their repository-root boundary
  and refuse existing evidence or substituted output directories.
- FR-004: Measure every tracked owned production Python file across scripts,
  xfactory, experiments, specs and openspec, including zero-hit modules.
- FR-005: Classify genuine test modules explicitly; retain all production
  languages and avoid blanket evidence, source or coverage exclusions.
- FR-006: Keep the exact existing test invocation, census, skip and named
  freshness guards. New tests increase passes; no new skip is authorized.
- FR-007: Bind coverage to the exact source and test result consumed by analysis.
- FR-008: Verify actual published-main CI and all six unchanged gate conditions;
  new-code coverage is present, evaluated and at least 80 percent.
- FR-009: Preserve baseline, profiles, issue/history identities, permissions,
  billing, active worktrees and sessions.

## Success Criteria

- SC-001: Fresh published-main quality result is OK with all six conditions.
- SC-002: Unsafe operand/preflight counterexamples refuse, including under optimization.
- SC-003: Complete required suites pass without increasing their skip budgets.
- SC-004: Owned source inventory has no omitted production coverage file.
- SC-005: Preservation evidence retains historical claims and active work.

## Key Entities

Analysis identity and source revision; owned source/test inventory; measured
coverage report; test census and named verdicts; unchanged gate/reference;
historical driver source and dated receipts; operating-state fingerprints.

## Assumptions and Scope

The existing organization analysis credential can be used without a new
secret or permission grant. There is no contract/schema or provider-pin change
planned. Historical driver code remains maintained and replayable; old run
records retain their original meaning. Hermes remains under its separate
explicit Sonar exception and is not changed by this feature.
