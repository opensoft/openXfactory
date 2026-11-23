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

Use the tracked analyzable input census at the pinned owner revision under the retained effective settings as the preservation baseline when a failed scan did not produce a complete indexed file list. Independently enumerate the exact scanner candidate's eligible tracked inputs under the same effective settings. Include either of the two approved new files if the provider indexes it and classify it as MAIN. Regression must prove that the candidate MAIN/TEST partition covers that candidate census without overlap, preserves every eligible baseline file, keeps the exact seven genuine test modules in TEST and both qualification helpers in MAIN, and adds no analysis, rule or coverage exclusions. Verify the actual provider-indexed categories against the candidate census. Preserve existing quality profiles, conditions and new-code settings. Sonar applies its existing test-code rules to TEST files.

### Real coverage and Sonar analysis

SonarCloud readback shows opensoft_Headscale-Install has automatic analysis enabled and no successful analysis. Automatic analysis cannot import actual coverage. Keep the existing project identity, visibility, quality profiles, six gate conditions, and new-code definition. Before any switch, read back the current project mode, effective project and inherited new-code definition, and assigned gate. Verify the trusted scanner candidate, scoped credential and the available Sonar and GitHub Actions capacity. A project administrator must separately authorize the bounded switch of this project from automatic to CI analysis after reviewing the candidate workflows and rollback controls.

Before changing this project's mode, successfully rehearse the rollback in an already authorized rehearsal scope within the existing allowance. Use the reviewed scanner workflow and restoration procedure. Record the baseline mode, the submission fence, the provider-side task drain, the restoration result, and the readback of provider settings and expected owner-job behavior. Verify that the project identity, visibility, quality profiles, six gate conditions and new-code definition remain intact. Keep the rehearsal record with the reviewed workflow revision and the switch decision. A failed, unavailable or unverified rehearsal leaves the project in automatic analysis. This proposal grants no additional rehearsal access or capacity. No settings have changed.

Run the entire existing qualification unittest suite with a hash-pinned, wheel-only coverage tool in the existing credential-free owner job. Preserve its separate explicit 49-case guarded-runner check. The coverage-producing run must match the unique collected and executed test identities against the pinned full-suite baseline from the reviewed owner revision and finish successfully with zero skips. Include the tested commit, collected and executed counts, expected baseline identity digest, separately measured collected and executed identity digests, execution verdict and report digests in the same-run receipt. Use the same identity canonicalization for all three digests. The scanner checks both measured digests against the expected baseline. Reject a reduced, duplicated, substituted, failed or skipped instrumented suite even if its report lists all expected source paths. The report must include zero-hit runtime modules and both qualification helpers. Validate the complete MAIN/TEST partition and receipt before transferring the report.

Run the scanner in a separate job with an exact, full-history checkout,
minimal GitHub token permissions and checkout credential persistence
disabled. Bind the coverage report and receipt to the immutable artifact
from the same run attempt and scanner revision. Stage the downloaded report
and receipt outside the checkout. Confirm that the scanner indexes none of
the transient reports, receipts or work files. Pin the actions and scanner,
and fix the provider destination and project.

Before scanner activation, verify a credential-delivery control enforced
outside the candidate workflow. Admit only the reviewed protected-main
revision through protected history or an independently admitted immutable
owner-PR revision, and verify refusal from other refs. Keep workflow
credentials available only to the pinned scanner step. A condition written
in the candidate workflow cannot establish this fence. Run unadmitted PRs
credential-free and exclude their code, artifacts and cache from privileged
execution. Verify that the effective credential can execute analysis only
on the intended project using scope metadata. Hold the scanner if the
ref or credential scope is unproven. Any necessary authorization or
credential-delivery change requires a separate decision before activation.

Use coverage source discovery for Python, including namespace packages. Restrict reporting to the exact tracked Python MAIN file list, then require the XML file paths to match that list exactly. A run that instruments only imported files can silently omit zero-hit modules. Reject missing, duplicate, absolute, out-of-tree or test-only paths, and reject a report whose source revision, branch coverage or digests fail validation. Keep this validation in the existing qualification workflow.

Review the exact protected-main qualification, release inventory, and local report in the owner's source evidence. The source report is a coverage diagnostic. Sonar determines the applicable new-code set and evaluates the configured gate.

Use the existing CI allowance for eligible PRs to main and protected-main scans. Bind the provider readback to the analysis task submitted by that exact scanner attempt and its resulting analysis ID, then verify the analyzed source revision. Record actual line usage, the analysis period and basis for new code, the measured new-code metrics, and the provider quality-gate response for that exact analysis ID. Require an overall OK verdict with no ignored conditions. Read back the same six metric, comparator, and threshold tuples as the verified baseline and require an evaluated OK result for each. Regress the case where a successful background task returns all six conditions but the aggregate quality gate fails. The first successful scan may only establish the baseline. An uncomputed gate, an omitted condition including one omitted by small-change handling, or a period that excludes the intended production changes leaves qualification pending. If the unchanged definition cannot evaluate all six conditions on the intended source, retain the observations and return for a bounded decision. If measured coverage fails, retain the result and scope any required additional regression files through owner review. In both the rehearsal and the real rollback, stop new CI submissions and confirm from the provider that all affected background analysis tasks are terminal or confirmed cancelled. Reconcile known task IDs with the project's background task queue and history so a submission accepted before a runner lost its receipt is accounted for. A terminal GitHub job alone cannot establish this drain. Hold restoration if the provider readback is incomplete or any task remains pending or running. Restore only this project's observed prior analysis mode and verify both the provider setting and expected owner-job behavior after restoration. Stop on concurrent mode drift or an unverifiable rollback and return for operator review. Failed or timed-out analysis remains unqualified.

### Exact source envelopes

| Owner / task | Proposed scope |
| --- | --- |
| L / T023 | Add exactly sonar-project.properties and requirements/sonar-analysis.lock. The existing .github/workflows/qualification.yml checks the exact partition, retains measured test collection and generates real coverage. A separate job in that workflow checks the artifacts and runs analysis. The existing release/private-connectivity-production.json records generated member hashes including the scanner configuration and analysis lock. The existing docs/runbooks/production-package.md explains the procedure. The prior task files and cases remain within their accepted scope. |
| E / definition | Use only the already accepted feature tasks.md, contracts/task-evidence.md, verify-evidence.py and tests/test_evidence.py surfaces for the one T023 file-list refinement and complete definition refresh. Existing commissioning/authentication records preserve prior accepted manifests and readers. Any required additional compatibility surface returns to scope review first. |

The amendment adds no implementation task or parallel checklist. T023 keeps owner L, all dependencies, class, required cases, gate and verify command. Only the two exact new source paths are proposed. Every other task line/registry row and frozen input body must remain identical except the explicitly reviewed matching definition representation.

### Decision and execution order

After independent exact-scope review, record the fresh C-01 L/E decision against the current qualified protected-base definition. That immutable record authorizes only the reviewed scope and complete definition refresh. Use the reviewed scope bodies for all sixteen frozen inputs and 68 task/registry rows. Keep fresh attestations in existing evidence registration outside the inputs they sign.

Keep the accepted T010 predecessor selected in both workflows during the protected reader and freeze update. Independently select current protected main through the existing attestor's GitHub.qualified_base readback and confirm its active evidence/commissioning.json through GitHub.content before source-only verification with the exact pinned predecessor reader. Hold if the active control or current authority is stale, changed or unverified. Any compatibility binding for the exact T023 successor must receive its own scope and tests. The separately proposed T015 successor binding cannot authorize a T023 definition. Keep original subject, authority, revocation and historical checks and preserve measured test identities and counts. Obtain separate exact review for any additional E paths or changed workflow validators.

Qualify the successor reader and freeze on protected main with both source lanes and evaluated Sonar. Prepare the fresh T010 commissioning manifest at a separate immutable candidate commit. Independently review its actual source outputs, run the qualified attestor with that manifest and exact review, register the resulting proof and pass default verification before selecting the successor control.

Once the successor is qualified, register a fresh C-01 binding to the same approved scope and exact refreshed definition using the accepted E verifier registration surface. Verify that the refreshed default reader admits only the exact bound scope for T023 and that the original decision and historical outputs still verify under their recorded definitions. The original subject must not substitute for the refreshed subject. If the refreshed binding or regression cannot be completed within the listed E scope, stop before consuming the scope and return for review. Implement the two new paths only after that admission. This draft records no acceptance.

The source amendment does not authenticate future outputs. After actual changed-source validation, CI and independent review, obtain a distinct actual-output admission/default verification before using the result for a release. Prior human and delegated decisions remain immutable.

### Capacity and actual acceptance

Classification is semantic correctness, not a capacity guarantee. Verify the actual Sonar organization usage again at execution. Independently verify that an existing no-overage control or a bounded included GitHub Actions compute and artifact-storage allowance covers the additional coverage work, scanner job and artifact transfer in the private owner repository. Bound job duration, artifact size and retention using the verified allowance. Check capacity before enabling or retrying the additional work and hold it if either allowance is unproven. No test-name estimate or local physical-line count supplies admission. If capacity is insufficient, stop the affected analysis for a separately authorized existing-capacity option. This proposal authorizes no spending, billing change or gate waiver.

Require all original owner checks and a successful protected-main analysis with the exact-analysis quality-gate verdict and six evaluated condition passes specified above. Read and preserve actual analyzed paths/categories, line accounting and evaluated quality conditions. Fix actual findings. A cancelled, failed, skipped or uncomputed analysis cannot be reported as a passing gate.

## Risks / Trade-offs

A qualification controller can be mistaken for a test because of its directory; retain both exact helpers as MAIN and test that boundary. A new test module can escape the configured test list; fail the inventory regression and obtain the necessary exact source update. Concurrent analyses can consume apparent spare lines; recheck actual usage. A classification change can affect test-code rule selection; disclose that normal semantics and preserve all profiles, thresholds and original history.

## Migration Plan

Preserve existing package/source history and failed analysis. Complete the distinct scope acceptance/freeze, implement in the isolated owner worktree, verify actual source and release member hashes, independent review, CI and protected-main analysis. Publish/read back no candidate until all required source/release predicates pass. Q0–Q5, actual target preparation, enrollment and observations remain separate.
