# Implementation Plan: Measured Sonar quality acceptance

**Branch**: 044-sonar-quality-remediation | **Date**: 2026-11-14 | **Spec**: [spec.md](spec.md)
Status: draft

## Summary

Fix the remaining source findings, keep historical evidence intact, collect
genuine whole-suite branch/subprocess coverage and migrate the same Sonar
project to CI analysis. Actual merged main must pass the original six
conditions with the same September reference.

## Technical Context

Python 3.12 and the existing pinned test dependencies; coverage.py 7.16.2 in a
separate analysis-only hash lock; GitHub Actions and the official immutable
Sonar scanner action. Existing tests use subprocesses extensively. Measurement
covers every owned Python file across scripts, xfactory, experiments, specs
and openspec, with namespace discovery and zero-hit inventory validation.
A clean scanner checkout does not materialize foreign gitlinks. Root tests
and the explicit genuine experiment/spec test paths are typed as tests.

## Constitution Check

Neutral ownership remains unchanged. This OpenSpec packet precedes code;
Speckit 044 owns the single task list. Historical verdicts/logs and source
preimages remain dated evidence. Existing manifests, contract/schema versions,
provider pins, runtime dependency lock and approval/protection rules remain
unchanged. Security refusals stay fail-closed. No credential is committed,
copied or newly published; the existing organization SONAR_TOKEN is used only
in a separate scanner job. No billing or active-session change is authorized.
The repository constitution remains at its existing draft adoption status.

## Research and Design

See [research.md](research.md) and [data-model.md](data-model.md). Source
security tests precede fixes. The existing literal full pytest command and
all census/skip/named-verifier guards stay. The coverage startup environment
and analysis tool lock add measurement, not a different test selection.
Coverage/report generation fails on missing production files or stale source.
The scanner waits for server gate computation, then checks measured conditions
and the fixed period instead of trusting upload success.

## Project Structure

Feature records are under this folder. Source changes are limited to the
identified validators/adapters and maintained historical replay driver.
The replay driver's pure preflight helper and tests make boundary rejection
testable without a browser or live server. CI/report tooling and workflow
contracts are tested independently with synthetic reports and real subprocess
traces; tests are then driven together through the unchanged complete suite.

## Governed Invariants

- .github/workflows/ — existing test census and named checks; new artifact-bound analysis.
- requirements/sonar-analysis.in and .lock — analysis-only dependency integrity.
- .coveragerc and sonar-project.properties — complete measured/typed source scope.
- scripts/doc_health/pin_class.py — ordinary foreign action-pin declaration, no exemption.
- tests/sequenced_after/corpus-ledger.yaml — seed only with the canonical seeder and real PR number.
- Historical AT-R1 verdicts/logs — original claims and hashes are not rewritten.

## Verification and Landing

Follow [quickstart.md](quickstart.md). Qualify focused refusal regressions,
complete coverage, source/report inventory, workflow contracts, OpenSpec and
ledger before final publication. Request an exact-head Codex review. Recheck
ownership/landing holds and rules before merge; only the existing author-side
human-review exception is available when every actual check passes.
Verify published-tree equality, all main workflows and actual main Sonar OK
with all six conditions. Retain failed measurements and preservation readback.
