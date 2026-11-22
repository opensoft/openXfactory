# Ratification of private Headscale T023 qualification without SonarCloud

Status: ratified
Ratified: 2026-11-22 by Brett Heap
Kind: ratification-record
Decision date: 2026-11-22
Decision timezone: America/La_Paz

## Decision

Brett Heap directed ratification of `qualify-private-headscale-without-sonarcloud` in PR #1361. He authorized marking the PR ready, requesting approval, and merging after checks and approvals pass. He requested post-merge CI verification and retained Q0–Q5, with macOS and external Q5 deferred.

The decision covers private Headscale-Install T023 and the corresponding coordinator evidence requirements in the [reviewed packet at e78ecd70](https://github.com/opensoft/openXfactory/tree/e78ecd70d620565de7e3fb4d703e5febc66c403d/openspec/changes/qualify-private-headscale-without-sonarcloud). The [proposal](../proposal.md) and [design](../design.md) define the zero-new-CI-spend replacement process. Public openXfactory retains its required Sonar checks.

## Admission and release sequence

The criterion mapping, exact L/E implementation paths, C-01 decision, and complete Feature 043 definition refresh remain required before implementation. Evaluated source and owner CI evidence need independent acceptance and current release authority before publication. Immutable publication and readback precede authentication and default T023 release verification. Consumer pins require the verified release under their own gates.

This records the OpenSpec decision and its normal source landing authority. Actual source and release outputs, QA migration, staging, canary, and rollout each require their recorded evidence and authority. The two ratified predecessor changes govern archive order.
