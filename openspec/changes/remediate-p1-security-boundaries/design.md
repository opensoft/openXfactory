# P1 tooling boundary design
Status: draft

## Context
The 40 P1 keys are derived from the separate PR #1320 index. User authority is
the direct 2026-11-15 implementation request, with active sessions, history,
checks and billing protected. Source changes happen in feature 045, not 044.

## Goals / Non-Goals
Repair actual boundary weaknesses and prove valid behavior. No live credential
refresh, browser activation, rotation/revocation, database business request,
paid model run, gate/profile/baseline mutation or historical record rewrite.

## Decisions
1. Credential names are bounded single components. The store is explicit
   operator/test configuration, independent of profile data. Hold no-follow
   directory descriptors, check ownership/types/links, lock cooperating writers,
   merge account metadata before changes, and stage both private 0600 files
   before atomic replacement. Retain wrong-account refusal and all unknown keys.
   Raw Path.resolve plus write_text was rejected because it follows links and
   does not close parent replacement races.
2. Dedicated browser state is either the default dedicated private directory or
   inside the trusted invocation root. Validate before extractors/browser startup.
   Refuse occupied Chromium profile markers; reuse over CDP remains explicit.
   Do not inspect or migrate real profiles for acceptance.
3. Privileged CI dependencies have separate tooling-only hash locks. Runtime
   release locks stay intact. The obsolete consumer CI upper bound resolves to
   cryptography 45.0.7, affected by GHSA-p423-j2cm-9vmq and
   GHSA-r6ph-v2qm-q3c2. Use the existing provider runtime pin 50.0.0 for CI
   and prove the pinned Opsx preflight/API compatibility independently; do not
   carry a known-vulnerable range into a new lock. Pip is hash-required
   and wheel-only. The CLI gets an npm integrity lock and lifecycle scripts stay
   disabled. Its actual binary/launcher must work offline; merely appending
   --ignore-scripts to the current wrapper install can leave a broken stub.
   No global developer installation or profile is changed.
4. Remaining P1 I/O roots are authorized by the invocation, independently from
   model-supplied operands; use descriptor-relative regular-file operations.
   Preserve internal APIs and valid multi-repository use through explicit trusted
   caller roots. Command operands and trusted executable selection are separate
   contracts; argv lists alone are insufficient.
5. Release-member and vendored repairs are phased through their owning release/
   consumer process. Existing archive bytes remain immutable. A contextual
   finding is not closed through a status waiver or manufactured provenance.

## Risks / Trade-offs
- Existing unsafe profile layouts refuse instead of silently relocating data.
  Operator repair is separate; no active state is altered by source rollout.
- Atomic replacement is per native file; cooperating harness writers hold one
  directory lock and stage both files first. Upstream readers do not transact
  both files; retain their native format and exercise interrupted-write cases.
- Symlink/race safety requires POSIX descriptor operations in the declared Linux
  bench; unavailable primitives refuse, rather than a weaker path fallback.
- Reusable workflow consumers and contract cuts may constrain landing order.
  Record actual dependencies before attempting pin advancement or a release.

## Migration Plan
Counterexamples first, then source and offline install acceptance, exact-head
review/CI and published-main Sonar readback for each landed phase. Keep source
history and original issue identities. Rollback is a reviewed source revert;
no profile migration, session restart or billing migration is involved.

## Open Questions
Credential-like negative-fixture provenance is not established. Inspect its
repository creation evidence privately; escalate only on credible live exposure.
No value is copied into feature artifacts or tested against a provider.
