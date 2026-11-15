# Phase 1 local verification
Status: draft
Date: 2026-11-15

## Counterexamples and native state
The original source at d6cd4083 failed 14 new profile/path/link counterexamples
before implementation. Initial repaired profile suites passed 56 tests and
11 subtests. Extended coverage adds writer serialization, concurrent metadata
change, private creation under permissive umask, staged-write failure cleanup,
unsupported-platform refusal, descriptor retention and dedicated-browser cases.
Every test uses synthetic state and explicit temporary store roots. No real
cookie, browser, active profile, token exchange or notebook is used.

The broader notebook/profile, Sonar, review-lane and code-surface suites passed
618 tests with 105 subtests before provider materialization, with three named
local skips: two pre-existing tranche-B tooling-home cases and the unmaterialized
openDox hermeticity check. After the declared provider graph was initialized, that hermeticity check ran:
619 tests passed with 105 subtests and only the same two pre-existing
tranche-B skips. No new skip was added or hidden.

## Dependency installation and functional acceptance
The CI-only Python closure installs from downloaded, hash-verified wheels with
no index access, hashes required and binary-only enforced. Imports succeed with
cryptography 50.0.0, the existing provider runtime pin. The old <46 constraint
was not copied into the new lock because its 45.0.7 resolution has upstream
security advisories; original runtime and developer lockfiles are unchanged.

The exact pinned Opsx consumer d5036247 with its declared provider 539cb563 was
prepared in isolated diagnostic clones. Under the fixed CI environment,
97 crypto-related consumer tests and 899 subtests passed, and its complete
standalone make validate finished OK. This is compatibility evidence, not a
claim of deployed nightly or live fleet acceptance.

The official Linux x64 CLI 2.1.325 installs through a fixed npm integrity lock
with lifecycle scripts disabled. The actual native binary reports the pinned
version in a scratch container with networking disabled, zero host/profile
mounts, unprivileged user and exit zero. Only that task-owned stopped scratch
container was removed after its acceptance receipt was saved. Existing benches,
global CLI binaries and sessions were not restarted or modified.
The reusable finalize job disables background updater drift during use.

## Workflow validation and existing controls
The new read-only privileged-dependencies workflow passes actionlint; the
worker installer passes shellcheck and bash syntax validation. The two changed
existing workflows have the same nine default shellcheck diagnostics as their
unchanged source baseline; no ignore/configuration change was introduced.
All existing test census, skip/freshness assertions, gate conditions, source/
coverage inventory, baseline, quality profiles and billing remain unchanged.

## Scope and unresolved provenance
User confirmed that fixture provenance is unknown and requested continued
investigation. No matching GitHub secret-scanning alert established provenance
for that literal. No credential liveness check or rotation was attempted.
That P1 key remains unresolved; the value is absent from these records.
The first phase does not claim completion of all 40 P1 records.

A subsequent preservation review added four counterexamples for read-only and
shared-write native targets. They failed against the initial phase-1 candidate;
the repair now respects those existing file intents before any replacement.
This correction does not change real profile modes or state during deployment.

Final read-only-intent follow-up verification: 623 tests passed with 105
subtests, with the same two pre-existing tranche-B skips.

## Exact-head review corrections
The review correction adds read-only store preflight before browser/extractor
work, rejects group/world access to existing private directories and files
without changing their modes, and compares capture-start generations under the
writer lock. A validated persistent browser descriptor remains open through the
owned browser lifetime; the launch path uses the parent process's procfs anchor.
Synthetic subprocess substitution and owned/CDP lifecycle tests cover this
without accessing a real session.

The CI launcher sets DISABLE_UPDATES and DISABLE_AUTOUPDATER at exec time, after
worker environment scrubbing. The actual pinned native binary through that
launcher again returned 2.1.325 with network mode none, zero mounts and exit 0.
A mutation test proves a comment cannot mask removal of --ignore-scripts.
The new dependency job uses the real openxFactory submodule layout and requires
all eight named dependency tests, with no skips/failures/errors.
The generated corpus ledger is regenerated using the canonical tool for #1321;
the initial full run's four failures all concerned this missing new packet row
(10,619 tests and 809 subtests otherwise passed; Sonar correctly did not run).

The native profile contract exposes two independent files and upstream readers
and writers do not implement a multi-file transaction or this harness's lock.
This repair promises private per-file replacement and cooperating writer
serialization, not atomic upstream pair reads or exclusion of an arbitrary
same-UID process. Those two review suggestions require upstream protocol changes
to provide stronger guarantees and cannot be represented as implemented here.
No upstream credential schema, active profile or running consumer is migrated.

The native CLI package retains its official LICENSE.md. Its notice identifies
Anthropic and refers to the vendor legal agreements; the scanner cannot classify
that notice as an open-source license. No lock/license field was falsified,
scanner suppressed, billing changed, or account/license terms accepted by this
repair. This remains the same official CLI used by the existing API-key fallback.

Review-correction verification: 921 tests, 105 subtests passed, with the same two
existing skips, across NotebookLM, Sonar quality, review-lane pin, code-surface
and sequencing suites. Four subsequently added browser lifecycle cases also
pass in the focused run: 94 tests and 11 subtests. Independent measured focused
line coverage is 84 percent for nlm_auth and 97 percent for safe_tooling_io
(88 percent combined); this is local evidence, not a substitute for CI's
exhaustive source/child coverage or the eventual main Sonar gate.
The corrected workflow passes actionlint and both installer/launcher pass
shellcheck. No checks or exclusions were removed.

## Caller compatibility during rollout
Inspection of the actual aggregation main found its reusable workflow tracks
main while its provider gitlink still selects 894885fe6afbe92c77c0c15ab7dbde899e8690f1.
That provider predates these lock/CLI files. The reusable jobs now read all
installer support at immutable published commit
2cd4050a220a9c46e1d6cdd8eff59fe41817d174, leaving caller-selected provider source
and pins unchanged. The regular merge preserves this commit in main history.

A disposable real old-provider worktree proved the exact materialization while
the files remained absent from that checkout: all eight support artifacts
matched this candidate, hash-locked Python dependencies installed from offline
wheels, and the actual CLI reported 2.1.325. Its provider HEAD and working files
stayed unchanged. The smoke workflow performs the same materialization and
byte comparison. Nine named dependency tests pass; actionlint passes on that
new workflow. This corrects a real rollout dependency before main cutover.

Brett Heap confirmed on 2026-11-15 that the existing Claude CLI API-key CI use is
already approved under Opensoft's Anthropic commercial agreement. The official
package and notice stay unchanged. The GitHub license discussion was resolved
with that authority recorded in the PR, without a scanner ignore or severity
override. A requested fresh Sourcery review then reported SKIPPED because its
250,000-diff-character seven-day budget was exhausted (available again in
6 days 22 hours at readback). That skip is not a passed fresh review; no billing
change or check dismissal was performed. Codex's exact 2cd4050a22 review found
no major issues. The rollout correction requires its own fresh review and CI.
