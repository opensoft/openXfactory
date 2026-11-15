# Design: Exact 043 source-test classification

Status: ratified
Ratified: 2026-11-14 by Brett Heap, through [classify-private-connectivity-source-tests](proposal.md).

## Context

See [proposal](proposal.md). Main's PR #1316 added scripts/validate-sonar-coverage.py and sonar-project.properties. Their test classifications enumerate the existing tests/, avatar experiment tests/support and 040 test tree. Neither enumerates the three 043 test modules. The integrated feature suite is explicitly collected separately by the existing pytest-suite workflow; collection alone does not repair the scanner's classification.

The ratified E design states: "If implementation needs another source/test/CI path, return to owner review before editing." The accepted source-CI refinement grants the two workflow paths and existing E helpers, but does not grant the newly introduced shared coverage reader, scanner configuration or its root regression module. This packet requests Brett Heap's acceptance of that exact addition to the existing E owner role.

## Goals / Non-Goals

**Goals:** Classify the actual 043 tests consistently in both tools; retain exhaustive real measured production coverage and zero-hit files; preserve the complete source-evidence and rollout gates.

**Non-Goals:** Coverage exclusions for production code; a generic specs/** test exemption; changed Sonar project, baseline, thresholds, credentials or settings; altered Python locks; new check identities; new skips or waived verdicts; source or rollout acceptance through ratification alone.

## Decisions

### Exact additional owner scope

All paths below are in opensoft/openXfactory. No directory-wide source grant is requested.

| Path | Proposed bounded edit | Existing task |
| --- | --- | --- |
| scripts/validate-sonar-coverage.py | Add exactly specs/043-private-connectivity-production/tests/ to test_source; preserve every production root, source/config/revision binding and report/gate check | T010 |
| sonar-project.properties | Append exactly specs/043-private-connectivity-production/tests/** to the existing sonar.test.inclusions list; preserve every existing inclusion and all other settings | T010 |
| tests/sonar_quality/test_coverage_evidence.py | Regress the classification agreement and ensure all three production helpers remain owned/measured; retain existing actual-child, zero-hit, source identity and refusal controls | T010 |

The actual test modules are test_evidence.py, test_evidence_pins.py and test_source_roots.py under that exact feature test directory. verify-evidence.py, register-evidence-pins.py and prepare-source-roots.py remain production source, together with every other production Python path. The coverage configuration, production ROOTS and omission policy do not change. An exact tree classification supports subsequent owner-approved tests in that existing feature test directory; it exempts no other specs tree.

Add only these three new paths to T010's files field after acceptance. Preserve all existing paths and all 68 task identities, owners, classes, cases, dependencies and verification commands. Recompute the entire 16-input/task/registry definition and update its existing freeze/reader identity surfaces; no additional frozen-input body change is requested. Existing accepted historical controls retain their immutable original definition, reader, provenance and anchors. The pending/withdrawn extended controls acquire no authentication through this refinement.

The already accepted .github/workflows/pytest-suite.yml surface may integrate the classification with its real feature-suite coverage measurement and update only the actually measured root collection count resulting from the added regression. Preserve its skipped-count pins, floors, named freshness/vector verdicts, bounded CLI pass, actual parent/child tracing, exact-source receipt and separate analysis job. No floor is relaxed to make a run pass. The separate Python 3.14 workflow keeps its existing obligations and explicit source-proof collection.

Existing exact 043 commissioning.json, T010.json and commissioning-authentication.md remain the only E control/receipt/authentication output paths. README's existing OpenSpec record block and the machine-generated corpus ledger record this proposal. No published contracts, contract bundle versions or new evidence prefixes are in scope.

### Validation and actual authentication

Before implementation, add a synthetic classification regression in an isolated scratch copy to demonstrate the current disagreement. After acceptance and repair, exercise the real inventory with the three test modules and three production helpers, and compare scanner classification with the same exact paths. Include a neighboring production path and retain all existing tree classifications; a broad exemption must fail.

Run the affected coverage-reader and feature regressions, the complete definition check, pinned strict OpenSpec validation and corpus ledger checks. Require actual exact-head CI for the root measured gate and Python 3.14 source-proof lane, plus fresh Codex review. Actual original source/CI exports, including refused preparations and superseded review findings, remain preserved. The new extended E packet needs separate actual custodian authentication and default T010 verification; no consent to future output is inferred from this scope decision.

## Risks / Trade-offs

- Inconsistent inventory and scanner classifications could hide a production file or misstate coverage. Mitigate with paired path controls and exhaustive production enumeration; introduce no source omission.
- The new regression legitimately changes the root collection count. Record only its observed increase while retaining exact skips and required named outcomes.
- A new task definition could appear to authenticate older exports. Preserve immutable historical anchors and require a new actual control/output review for the extended definition.

## Migration Plan

Obtain the affected owner's exact scope/refreeze acceptance and ratify this packet. Apply the three bounded edits and matching T010 refinement, recompute the complete definition, then qualify the unchanged gate semantics on actual source. Present the resulting actual packet separately for authentication. Keep coordinator #1310, Ops #628, domain #583 and Headscale #2 draft. Full Q0, Q1–Q5, publication, merge, target execution, deployment, enrollment, paid resources and commercial gates remain pending.
