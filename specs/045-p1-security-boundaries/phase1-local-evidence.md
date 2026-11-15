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
