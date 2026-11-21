# Design: Preserve package analysis with an exact source/test partition

Status: draft
Kind: design

## Context

The package owner is opensoft/Headscale-Install. Current source main is 705d4f08f143f4922be98bf5e634c5494cac47cf. Actual owner validation passed; the Sonar analysis failed at the organization line ceiling, so release acceptance remains pending. There is no authorization for new CI spend.

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

Regression must prove that the MAIN/TEST partition covers the complete previously analyzed source universe without overlap, every selected file exists and is a genuine test module, the live qualification helpers remain MAIN, and the configuration contains no additional analysis/rule/coverage exclusion. Preserve existing quality profiles, condition thresholds and baseline; TEST files use Sonar's test-code rules.

### Real coverage and Sonar analysis

SonarCloud readback shows opensoft_Headscale-Install has automatic analysis enabled and no successful analysis. Automatic analysis cannot import actual coverage. Keep the existing project identity, visibility, quality profiles, six gate conditions, and new-code definition. The draft CI route would require an authorized switch of this project alone from automatic to CI analysis after the candidate workflows and rollback are reviewable. No settings have changed.

Run the entire existing qualification unittest suite with a hash-pinned, wheel-only coverage tool in the existing credential-free owner job. Preserve its explicit 49-runner collection, all cases, and zero skips. The report must include zero-hit runtime modules and both qualification helpers. Validate a complete MAIN/TEST partition and a report receipt with the exact tested commit and report digests. Run the scanner in a separate, credential-free checkout until the verified report is in place. Supply the existing project scanner credential only to the scanner steps. No App, secret access scope, paid runner, or billing changes are included.

Use coverage source discovery for Python, including namespace packages. Restrict reporting to the exact tracked Python MAIN file list, then require the XML file paths to match that list exactly. A run that instruments only imported files can silently omit zero-hit modules. Reject missing, duplicate, absolute, out-of-tree or test-only paths, and reject a report whose source revision, branch coverage or digests fail validation. Keep this validation in the existing qualification workflow.

The existing package workflow replay on protected main 705d4f08f143f4922be98bf5e634c5494cac47cf passed 160 unit tests and separately collected and passed all 49 guarded runner cases. All 11 current release inventory members verified. The first coverage report omitted two unexecuted modules. A corrected run included all ten MAIN candidates. It measured 1,078 of 1,485 statements and 153 of 314 branches overall (68.43% combined) and 909 of 1,011 statements and 112 of 136 branches for the four Python files added by the package merge (89.01% combined). These are local Coverage.py measurements. Actual Sonar analysis determines the applicable new-code set and evaluates the existing gate.

Use the existing CI allowance for PRs to main and protected-main scans. Verify actual provider source provenance, line usage, analysis and six evaluated conditions. If measured coverage fails, retain the result and scope any required additional regression files through owner review. If a project setting switch is authorized and the CI path cannot be made operational, offer restoration of the previous automatic mode under that same bounded change decision.

### Exact source envelopes

| Owner / task | Proposed scope |
| --- | --- |
| L / T023 | Add exactly sonar-project.properties and requirements/sonar-analysis.lock. The existing .github/workflows/qualification.yml checks the exact partition, retains measured test collection and generates real coverage. A separate job in that workflow checks the artifacts and runs analysis. The existing release/private-connectivity-production.json records generated member hashes including the scanner configuration and analysis lock. The existing docs/runbooks/production-package.md explains the procedure. The prior task files and cases remain within their accepted scope. |
| E / definition | Use only the already accepted feature tasks.md, contracts/task-evidence.md, verify-evidence.py and tests/test_evidence.py surfaces for the one T023 file-list refinement and complete definition refresh. Existing commissioning/authentication records preserve prior accepted manifests and readers. Any required additional compatibility surface returns to scope review first. |

The amendment adds no implementation task or parallel checklist. T023 keeps owner L, all dependencies, class, required cases, gate and verify command. Only the two exact new source paths are proposed. Every other task line/registry row and frozen input body must remain identical except the explicitly reviewed matching definition representation.

### Decision and execution order

Draft this packet; independently review the exact scope; use the qualified protected-base delegation mechanism for a fresh C-01 owner decision; refresh all sixteen frozen inputs and all 68 task/registry rows; only then implement the new file in a task-scoped package commit. This draft records no acceptance.

The source amendment does not authenticate future outputs. After actual changed-source validation, CI and independent review, obtain a distinct actual-output admission/default verification before using the result for a release. Prior human and delegated decisions remain immutable.

### Capacity and actual acceptance

Classification is semantic correctness, not a capacity guarantee. The actual organization usage and scanner results must be read again at execution. No test-name estimate or local physical-line count supplies admission. If the existing cap is still insufficient, stop the affected analysis for a separately authorized existing-capacity option; do not buy capacity or waive a gate.

Require all original owner checks and an actual successful protected-main analysis for the exact source. Read and preserve actual analyzed paths/categories, line accounting and evaluated quality conditions. Fix actual findings. A cancelled, failed, skipped or uncomputed analysis cannot be reported as a passing gate.

## Risks / Trade-offs

A qualification controller can be mistaken for a test because of its directory; retain both exact helpers as MAIN and test that boundary. A new test module can escape the configured test list; fail the inventory regression and obtain the necessary exact source update. Concurrent analyses can consume apparent spare lines; recheck actual usage. A classification change can affect test-code rule selection; disclose that normal semantics and preserve all profiles, thresholds and original history.

## Migration Plan

Preserve existing package/source history and failed analysis. Complete the distinct scope acceptance/freeze, implement in the isolated owner worktree, verify actual source and release member hashes, independent review, CI and protected-main analysis. Publish/read back no candidate until all required source/release predicates pass. Q0–Q5, actual target preparation, enrollment and observations remain separate.
