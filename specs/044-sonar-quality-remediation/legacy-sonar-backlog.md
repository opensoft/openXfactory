# Older Sonar reliability and security backlog

This is a preserved snapshot of 110 open findings outside the retained
September new-code period: six bugs and 104 vulnerabilities. Brett selected
a separate backlog while the two new-period gate blockers are repaired.
No finding in this record is accepted, suppressed, resolved or waived by it.
The existing project, profiles, gate conditions and historical period remain.

Snapshot observed: 2026-11-14T21:48:12.321259-04:00

Source analysis: 9a06995a-534a-4aa5-a3e7-3aaeeef2bbeb

Source revision: d4fdef49e96d6178c9da58327d5b956833c7b5df

Project: opensoft_openxFactory

The original period remains the manual reference analysis
d20bb52c-64fd-4090-986a-fd993f44ff86, dated 2026-09-09T19:37:08-04:00.
The complete API inventory has 112 open bugs/vulnerabilities. Its two
new-period findings are tracked in the [feature evidence](evidence.md);
the 110 below are the separate older backlog. Counts and locations are
snapshot evidence, not a claim about a later revision.

Only issue identities, rule/type/severity and source locations are copied.
Source snippets, flow payloads and any possible secret values are omitted.

| Type | Severity | Rule | Source at the recorded revision | Issue |
| --- | --- | --- | --- | --- |
| VULNERABILITY | BLOCKER | `secrets:S7525` | `contracts/identity-brokering/examples/negative/idp-credential-committed-in-manifest.yaml:29` | [AaCIinIs1WTeVOIYRWTa](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinIs1WTeVOIYRWTa) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/doc_health/derive_possibles_dispatch.py:460` | [AaCIimEw1WTeVOIYRVyH](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyH) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/doc_health/readiness_dispatch.py:424` | [AaCIimBs1WTeVOIYRVxq](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxq) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4565` | [AaCIil7G1WTeVOIYRVvU](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvU) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/nlm_auth.py:373` | [AaHGGxfmXfVYYfeyHqh7](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxfmXfVYYfeyHqh7) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/set-domain-openxfactory-pin.py:139` | [AaCIimU71WTeVOIYRV5F](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimU71WTeVOIYRV5F) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/test-domain-starter-ontology.py:235` | [AaHGGxdIXfVYYfeyHqh6](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxdIXfVYYfeyHqh6) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/test-semantic-context.py:142` | [AaHFP2__EALMvGZEYwo0](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHFP2__EALMvGZEYwo0) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/test-semantic-context.py:149` | [AaHFP2__EALMvGZEYwoz](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHFP2__EALMvGZEYwoz) |
| VULNERABILITY | BLOCKER | `pythonsecurity:S2083` | `scripts/validate-openspec-cli-pin.py:1367` | [AaHGGxXtXfVYYfeyHqh5](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxXtXfVYYfeyHqh5) |
| VULNERABILITY | CRITICAL | `python:S4790` | `scripts/validate-openspec-cli-pin.py:916` | [AaCIimK91WTeVOIYRV0X](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0X) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/clearing-dispatch-gate.yml:110` | [AaCIinF61WTeVOIYRWQn](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinF61WTeVOIYRWQn) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/clearing-dispatch-gate.yml:110` | [AaCIinF61WTeVOIYRWQo](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinF61WTeVOIYRWQo) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/doc-health-reusable.yml:589` | [AaCIinGi1WTeVOIYRWQq](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQq) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/doc-health-reusable.yml:589` | [AaCIinGi1WTeVOIYRWQr](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQr) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/doc-health-reusable.yml:1688` | [AaCIinGi1WTeVOIYRWQs](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQs) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/doc-health-reusable.yml:1688` | [AaCIinGi1WTeVOIYRWQt](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQt) |
| VULNERABILITY | MAJOR | `githubactions:S6505` | `.github/workflows/doc-health-reusable.yml:1700` | [AaCIinGi1WTeVOIYRWQu](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQu) |
| VULNERABILITY | MAJOR | `githubactions:S8543` | `.github/workflows/doc-health-reusable.yml:1700` | [AaCIinGi1WTeVOIYRWQv](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinGi1WTeVOIYRWQv) |
| VULNERABILITY | MAJOR | `githubactions:S7631` | `.github/workflows/merge-master-approval.yml:619` | [AaCIinG11WTeVOIYRWQw](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinG11WTeVOIYRWQw) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/merge-master-approval.yml:696` | [AaCIinG11WTeVOIYRWQx](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinG11WTeVOIYRWQx) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/merge-master-approval.yml:696` | [AaCrEXwZNd9EY7sT_hsJ](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCrEXwZNd9EY7sT_hsJ) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/openxwallet-consumer-gate.yml:126` | [AaCIinFq1WTeVOIYRWQj](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinFq1WTeVOIYRWQj) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/openxwallet-consumer-gate.yml:126` | [AaCIinFq1WTeVOIYRWQk](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinFq1WTeVOIYRWQk) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/review-lane-repin.yml:338` | [AaCIinHC1WTeVOIYRWQy](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinHC1WTeVOIYRWQy) |
| VULNERABILITY | MAJOR | `githubactions:S8541` | `.github/workflows/signed-execution-chain-gate.yml:121` | [AaCIinFy1WTeVOIYRWQl](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinFy1WTeVOIYRWQl) |
| VULNERABILITY | MAJOR | `githubactions:S8544` | `.github/workflows/signed-execution-chain-gate.yml:121` | [AaCIinFy1WTeVOIYRWQm](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinFy1WTeVOIYRWQm) |
| VULNERABILITY | MAJOR | `text:S8565` | `experiments/avatar-brokered-call/pyproject.toml` | [AaCIinKi1WTeVOIYRWTx](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinKi1WTeVOIYRWTx) |
| BUG | MAJOR | `python:S7502` | `experiments/avatar-brokered-call/src/avatar_f0/media.py:88` | [AaCIinJR1WTeVOIYRWTf](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinJR1WTeVOIYRWTf) |
| BUG | MAJOR | `Web:PageWithoutTitleCheck` | `openspec/changes/archive/2026-07-29-add-ideation-dashboard/supporting-docs/wheel-mockup.html:3` | [AaCIinK61WTeVOIYRWUu](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinK61WTeVOIYRWUu) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/apply-domain-starter.py:3750` | [AaCIimOf1WTeVOIYRV12](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimOf1WTeVOIYRV12) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/apply-domain-starter.py:4030` | [AaCIimOf1WTeVOIYRV11](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimOf1WTeVOIYRV11) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/avatar-metering-alert.py:86` | [AaCIimQY1WTeVOIYRV3E](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQY1WTeVOIYRV3E) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/avatar-metering-alert.py:164` | [AaCIimQY1WTeVOIYRV3B](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQY1WTeVOIYRV3B) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/avatar-metering-alert.py:232` | [AaCIimQY1WTeVOIYRV3C](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQY1WTeVOIYRV3C) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/avatar-metering-alert.py:235` | [AaCIimQY1WTeVOIYRV3D](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQY1WTeVOIYRV3D) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/corpus.py:294` | [AaCIimAt1WTeVOIYRVxC](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimAt1WTeVOIYRVxC) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:123` | [AaHGGxTaXfVYYfeyHqh4](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxTaXfVYYfeyHqh4) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:203` | [AaCIimEw1WTeVOIYRVyN](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyN) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:212` | [AaCIimEw1WTeVOIYRVyP](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyP) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:220` | [AaCIimEw1WTeVOIYRVyL](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyL) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:223` | [AaCIimEw1WTeVOIYRVyO](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyO) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:331` | [AaCIimEw1WTeVOIYRVyJ](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyJ) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:459` | [AaCIimEw1WTeVOIYRVyI](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyI) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:460` | [AaCIimEw1WTeVOIYRVyK](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyK) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/derive_possibles_dispatch.py:464` | [AaCIimEw1WTeVOIYRVyM](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEw1WTeVOIYRVyM) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/doc_health/ideation_readiness.py:1038` | [AaCIimA81WTeVOIYRVxH](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimA81WTeVOIYRVxH) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/doc_health/pin_class.py:1804` | [AaCIimEm1WTeVOIYRVyF](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimEm1WTeVOIYRVyF) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:141` | [AaHGGxRbXfVYYfeyHqh3](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxRbXfVYYfeyHqh3) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:184` | [AaCIimBs1WTeVOIYRVxs](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxs) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:202` | [AaCIimBs1WTeVOIYRVxt](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxt) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:205` | [AaCIimBs1WTeVOIYRVxr](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxr) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:265` | [AaCIimBs1WTeVOIYRVxw](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxw) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:423` | [AaCIimBs1WTeVOIYRVxv](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxv) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/readiness_dispatch.py:424` | [AaCIimBs1WTeVOIYRVxu](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBs1WTeVOIYRVxu) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/runner.py:120` | [AaCIimBX1WTeVOIYRVxm](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBX1WTeVOIYRVxm) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/runner.py:582` | [AaCIimBX1WTeVOIYRVxl](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBX1WTeVOIYRVxl) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/runner.py:720` | [AaCIimBX1WTeVOIYRVxk](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBX1WTeVOIYRVxk) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/runner.py:910` | [AaCIimBX1WTeVOIYRVxj](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBX1WTeVOIYRVxj) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/doc_health/runner.py:916` | [AaCIimBX1WTeVOIYRVxi](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimBX1WTeVOIYRVxi) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/hermes_runtime_validation/loader.py:175` | [AaCIilrU1WTeVOIYRVlX](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIilrU1WTeVOIYRVlX) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/hermes_runtime_validation/pytest_execution_validation.py:40` | [AaCIilrI1WTeVOIYRVlT](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIilrI1WTeVOIYRVlT) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4562` | [AaCIil7G1WTeVOIYRVvc](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvc) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4565` | [AaCIil7G1WTeVOIYRVvg](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvg) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4775` | [AaCIil7G1WTeVOIYRVvY](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvY) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4778` | [AaCIil7G1WTeVOIYRVva](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVva) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4780` | [AaCIil7G1WTeVOIYRVvV](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvV) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:4949` | [AaCIil7G1WTeVOIYRVvZ](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvZ) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:5103` | [AaCIil7G1WTeVOIYRVvf](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvf) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/dashboard_refresh_lane.py:5140` | [AaCIil7G1WTeVOIYRVvb](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil7G1WTeVOIYRVvb) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/ideation_dashboard/intent_apply_lane.py:148` | [AaCIil2o1WTeVOIYRVtT](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil2o1WTeVOIYRVtT) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/intent_apply_lane.py:156` | [AaCIil2o1WTeVOIYRVtW](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil2o1WTeVOIYRVtW) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/intent_apply_lane.py:514` | [AaCIil2o1WTeVOIYRVtV](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil2o1WTeVOIYRVtV) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ideation_dashboard/intent_apply_lane.py:766` | [AaCIil2o1WTeVOIYRVtU](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIil2o1WTeVOIYRVtU) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/nlm_auth.py:365` | [AaHGGxfmXfVYYfeyHqh8](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaHGGxfmXfVYYfeyHqh8) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/nlm_auth.py:444` | [AaCIimVP1WTeVOIYRV5M](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimVP1WTeVOIYRV5M) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/nlm_auth.py:505` | [AaCIimVP1WTeVOIYRV5N](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimVP1WTeVOIYRV5N) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-compile-context.py:53` | [AaCIimVF1WTeVOIYRV5J](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimVF1WTeVOIYRV5J) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-compile-context.py:266` | [AaCIimVF1WTeVOIYRV5K](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimVF1WTeVOIYRV5K) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-maintenance.py:62` | [AaCIimWd1WTeVOIYRV5i](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimWd1WTeVOIYRV5i) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-maintenance.py:352` | [AaCIimWd1WTeVOIYRV5j](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimWd1WTeVOIYRV5j) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-release.py:377` | [AaCIimQL1WTeVOIYRV3A](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQL1WTeVOIYRV3A) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/ontology-release.py:378` | [AaCIimQL1WTeVOIYRV2_](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQL1WTeVOIYRV2_) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/proposal-support.py:4728` | [AaCIimQA1WTeVOIYRV24](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQA1WTeVOIYRV24) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/review_lane_repin.py:668` | [AaCIimUp1WTeVOIYRV46](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimUp1WTeVOIYRV46) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/review_lane_repin.py:742` | [AaCIimUp1WTeVOIYRV44](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimUp1WTeVOIYRV44) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/review_lane_repin.py:746` | [AaCIimUp1WTeVOIYRV45](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimUp1WTeVOIYRV45) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/set-domain-openxfactory-pin.py:122` | [AaCIimU71WTeVOIYRV5G](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimU71WTeVOIYRV5G) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/set-domain-openxfactory-pin.py:139` | [AaCIimU71WTeVOIYRV5H](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimU71WTeVOIYRV5H) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/sync-notebooklm-books.py:528` | [AaCIimXf1WTeVOIYRV6M](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimXf1WTeVOIYRV6M) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-client-content.py:444` | [AaCIimKY1WTeVOIYRV0H](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimKY1WTeVOIYRV0H) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-client-content.py:447` | [AaCIimKY1WTeVOIYRV0G](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimKY1WTeVOIYRV0G) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-contract-release.py:67` | [AaCIimPq1WTeVOIYRV2c](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimPq1WTeVOIYRV2c) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-contract-release.py:147` | [AaDtwvvw8psOVKXC8zt-](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaDtwvvw8psOVKXC8zt-) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-document-catalog.py:130` | [AaCIimXs1WTeVOIYRV6c](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimXs1WTeVOIYRV6c) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-domain-openxfactory-pins.py:75` | [AaCIimLI1WTeVOIYRV0m](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimLI1WTeVOIYRV0m) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-hermes-runtime-contracts.py:161` | [AaCIimIx1WTeVOIYRVzb](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimIx1WTeVOIYRVzb) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-hermes-runtime-postgres.py:1060` | [AaCIimWJ1WTeVOIYRV5e](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimWJ1WTeVOIYRV5e) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-openreposhape-pin.py:177` | [AaCIimQ61WTeVOIYRV3S](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimQ61WTeVOIYRV3S) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-openspec-cli-pin.py:495` | [AaCIimK91WTeVOIYRV0i](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0i) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8707` | `scripts/validate-openspec-cli-pin.py:927` | [AaCIimK91WTeVOIYRV0h](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0h) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8701` | `scripts/validate-openspec-cli-pin.py:1277` | [AaCIimK91WTeVOIYRV0e](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0e) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-openspec-cli-pin.py:1540` | [AaCIimK91WTeVOIYRV0g](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0g) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-openspec-cli-pin.py:1674` | [AaCIimK91WTeVOIYRV0f](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimK91WTeVOIYRV0f) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/validate-release-tag-gate.py:192` | [AaCIimWT1WTeVOIYRV5g](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimWT1WTeVOIYRV5g) |
| VULNERABILITY | MAJOR | `pythonsecurity:S8705` | `scripts/verify-openxwallet-pin.py:273` | [AaCIimV51WTeVOIYRV5a](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimV51WTeVOIYRV5a) |
| BUG | MAJOR | `python:S5863` | `tests/avatar_runtime/test_determinism.py:27` | [AaCIim7q1WTeVOIYRWNg](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIim7q1WTeVOIYRWNg) |
| BUG | MAJOR | `python:S5863` | `tests/avatar_runtime/test_determinism.py:38` | [AaCIim7q1WTeVOIYRWNh](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIim7q1WTeVOIYRWNh) |
| BUG | MAJOR | `python:S5863` | `tests/doc-health/test_organizer_dispatch.py:123` | [AaCIimuH1WTeVOIYRWGG](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIimuH1WTeVOIYRWGG) |
| BUG | MAJOR | `python:S9000` | `tests/test_standards_body_registry.py:288` | [AaCIinEO1WTeVOIYRWPT](https://sonarcloud.io/project/issues?id=opensoft_openxFactory&open=AaCIinEO1WTeVOIYRWPT) |
