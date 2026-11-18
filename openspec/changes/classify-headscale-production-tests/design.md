# Design: Preserve package analysis with an exact source/test partition

Status: draft
Kind: design

## Context

The package owner is opensoft/Headscale-Install. The existing organization line ceiling prevents the package's required Sonar analysis. Before C-01 review, pin the exact private producer commit and the SHA-256 of the custody-scoped source census and provider readback. The private record must identify all seven test paths, both executable helpers, the reported scan input and line-cap failure, and the effective provider settings. Keep private source and raw provider output in owner custody. Release acceptance requires qualifying analysis within existing capacity.

The existing coordinating owner scope is commission-headscale-production. This amendment remains inside the seven-owner finite policy at a66cfe601407818dbd04f294bbaf92af15246e22 and does not amend that policy.

## Goals / Non-Goals

Goals: correct genuine test classification, retain every analyzed runtime/control surface, require actual provider readback and preserve historical evidence and release content identity.

Non-goals: acquire capacity, promise available lines, change another owner's source or Sonar project, suppress a finding, omit code from analysis, change a quality profile/gate/baseline, grant runtime authority or claim release qualification.

## Decisions

### Exact package partition

Set sonar.sources to the repository root. Set sonar.tests to these exact seven individual paths. Exclude exactly those same paths from MAIN scope; they remain analyzed as TEST:

- tests/qualification/test_fixture.py
- tests/qualification/test_production_endpoint.py
- tests/qualification/test_production_package.py
- tests/qualification/test_production_recovery.py
- tests/qualification/test_production_runner.py
- tests/qualification/test_recovery.py
- tests/qualification/test_workloads.py

No wildcard is permitted in the initial source/test path lists. No blanket tests-directory classification is permitted. The executable tests/qualification/init_hosted_boundary.py and tests/qualification/qualify_production.py remain MAIN, together with deploy/ code and the qualification workflow. Newly encountered executable code defaults to MAIN until reviewed.

Use the tracked analyzable input census at the pinned owner revision under the retained effective settings as the reference when a failed scan did not produce a complete indexed file list. Regression must prove that the MAIN/TEST partition covers this reference without overlap, every selected file exists and is a genuine test module, both qualification helpers remain MAIN, and the configuration adds no analysis, rule or coverage exclusions. Verify the actual provider-indexed categories against the census. Preserve existing quality profiles, conditions and new-code settings. Sonar applies its existing test-code rules to TEST files.

### Real coverage and Sonar analysis

SonarCloud readback shows opensoft_Headscale-Install has automatic analysis enabled and no successful analysis. Automatic analysis cannot import actual coverage. Keep the existing project identity, visibility, quality profiles, six gate conditions, and new-code definition. Before any switch, read back the current project mode, effective project and inherited new-code definition, and assigned gate. Verify the trusted scanner candidate, scoped credential and available capacity. A project administrator must separately authorize a bounded switch of this project from automatic to CI analysis after reviewing the candidate workflows and rollback controls. No settings have changed.

Run the entire existing qualification unittest suite with a hash-pinned, wheel-only coverage tool in the existing credential-free owner job. Preserve its separate explicit 49-case guarded-runner check. The coverage-producing run must match the unique collected and executed test identities against the pinned full-suite baseline from the reviewed owner revision and finish successfully with zero skips. Include the tested commit, collected and executed counts, full baseline identity digest, execution verdict and report digests in the same-run receipt. Reject a reduced, duplicated, substituted, failed or skipped instrumented suite even if its report lists all expected source paths. The report must include zero-hit runtime modules and both qualification helpers. Validate the complete MAIN/TEST partition and receipt before transferring the report.

Run the scanner in a separate job with an exact, full-history checkout, minimal GitHub token permissions, and checkout credential persistence disabled. Bind the coverage report and its receipt to the immutable artifact from the same workflow run attempt and exact scanner revision. Permit access to the scanner credential only from the pinned scanner step, on protected main or an explicitly trusted owner-PR revision admitted by existing controls. Fork and other untrusted PRs run credential-free qualification. Do not pass their code, artifacts or cache through any privileged trigger or job. Pin the actions and scanner, and fix the provider destination and project. Verify the existing credential grants Execute Analysis for only the intended project without retrieving the credential value. If the required credential scope and trust boundary cannot be verified, stop this route. No App, secret access scope, paid runner, or billing changes are included.

Use coverage source discovery for Python, including namespace packages. Restrict reporting to the exact tracked Python MAIN file list, then require the XML file paths to match that list exactly. A run that instruments only imported files can silently omit zero-hit modules. Reject missing, duplicate, absolute, out-of-tree or test-only paths, and reject a report whose source revision, branch coverage or digests fail validation. Keep this validation in the existing qualification workflow.

Review the exact protected-main qualification, release inventory, and local report in the owner's source evidence. The source report is a coverage diagnostic. Sonar determines the applicable new-code set and evaluates the configured gate.

Use the existing CI allowance for eligible PRs to main and protected-main scans. Bind the provider readback to the analysis task submitted by that exact scanner attempt and its resulting analysis ID, then verify the analyzed source revision. Record actual line usage, the analysis period and basis for new code, the measured new-code metrics, and the status of all six unchanged conditions. The first successful scan may only establish the baseline. An uncomputed gate, an omitted condition including one omitted by small-change handling, or a period that excludes the intended production changes leaves qualification pending. If the unchanged definition cannot evaluate all six conditions on the intended source, retain the observations and return for a bounded decision. If measured coverage fails, retain the result and scope any required additional regression files through owner review. If the authorized switch cannot be made operational, use the bounded rollback only after new CI submissions are stopped and in-flight submissions have drained or been cancelled. Restore only this project's observed prior analysis mode and verify both the provider setting and expected owner-job behavior after restoration. Stop on concurrent mode drift or an unverifiable rollback and return for operator review. Failed or timed-out analysis remains unqualified.

### Exact source envelopes

| Owner / task | Proposed scope |
| --- | --- |
| L / T023 | Add exactly sonar-project.properties and requirements/sonar-analysis.lock. The existing .github/workflows/qualification.yml checks the exact partition, retains measured test collection and generates real coverage. A separate job in that workflow checks the artifacts and runs analysis. The existing release/private-connectivity-production.json records generated member hashes including the scanner configuration and analysis lock. The existing docs/runbooks/production-package.md explains the procedure. The prior task files and cases remain within their accepted scope. |
| E / definition | Use only the already accepted feature tasks.md, contracts/task-evidence.md, verify-evidence.py and tests/test_evidence.py surfaces for the one T023 file-list refinement and complete definition refresh. Existing commissioning/authentication records preserve prior accepted manifests and readers. Any required additional compatibility surface returns to scope review first. |

The amendment adds no implementation task or parallel checklist. T023 keeps owner L, all dependencies, class, required cases, gate and verify command. Only the two exact new source paths are proposed. Every other task line/registry row and frozen input body must remain identical except the explicitly reviewed matching definition representation.

### Decision and execution order

After independent exact-scope review, record the fresh C-01 L/E decision against the current qualified protected-base definition. That immutable record authorizes only the reviewed scope and complete definition refresh. Qualify the refreshed definition and all sixteen frozen inputs and 68 task/registry rows through the authorized source-only path. Once the refreshed attestor is qualified, register a fresh C-01 binding to the same approved scope and exact refreshed definition using the accepted E verifier registration surface. Verify that the refreshed default reader admits only the exact bound scope for T023 and that the original decision and historical outputs still verify under their recorded definitions. The original subject must not substitute for the refreshed subject. If the refreshed binding or regression cannot be completed within the listed E scope, stop before consuming the scope and return for review. Implement the two new paths only after that admission. This draft records no acceptance.

The source amendment does not authenticate future outputs. After actual changed-source validation, CI and independent review, obtain a distinct actual-output admission/default verification before using the result for a release. Prior human and delegated decisions remain immutable.

### Capacity and actual acceptance

Classification is semantic correctness, not a capacity guarantee. The actual organization usage and scanner results must be read again at execution. No test-name estimate or local physical-line count supplies admission. If the existing cap is still insufficient, stop the affected analysis for a separately authorized existing-capacity option; do not buy capacity or waive a gate.

Require all original owner checks and an actual successful protected-main analysis for the exact source. Read and preserve actual analyzed paths/categories, line accounting and evaluated quality conditions. Fix actual findings. A cancelled, failed, skipped or uncomputed analysis cannot be reported as a passing gate.

## Risks / Trade-offs

A qualification controller can be mistaken for a test because of its directory; retain both exact helpers as MAIN and test that boundary. A new test module can escape the configured test list; fail the inventory regression and obtain the necessary exact source update. Concurrent analyses can consume apparent spare lines; recheck actual usage. A classification change can affect test-code rule selection; disclose that normal semantics and preserve all profiles, thresholds and original history.

## Migration Plan

Preserve existing package/source history and failed analysis. Complete the distinct scope acceptance/freeze, implement in the isolated owner worktree, verify actual source and release member hashes, independent review, CI and protected-main analysis. Publish/read back no candidate until all required source/release predicates pass. Q0–Q5, actual target preparation, enrollment and observations remain separate.
