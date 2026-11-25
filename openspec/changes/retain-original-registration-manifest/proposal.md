---
Status: draft
Authored: 2026-11-25
Kind: governance
sequenced_after:
  - bound-remote-lifecycle-accounting
code_surface: openXwallet (existing feature017 T013P08; source-selected lifecycle descriptor wire, original controller-store retention/claim grammar, bounded original-manifest acquisition, source construction and tests); openXfactory (this source-only contract/handoff packet, README records and generated corpus ledger at publication)
target_release: implemented (source acceptance only; dependent runtime implementation and operational grants remain separate)
---

## Why

Fresh P08 Gate A passes15 controls. Gate B cannot select the accepted per-credential
handoff policy because the runner caller lacks authenticated original registration
resources and store binding. The initial controller-local route failed architecture
review: the workflow executes qualify on the runner, and its exact local Qualifier
has no existing controller invocation/result bridge. This v2 source proposal instead
makes one bounded acquisition from the original controller explicit.

## What Changes

- Preserve the runner-local Qualifier, unchanged full admission, report and phase APIs.
- Carry an owner-derived complete descriptor on the existing primary register and
  independent ack-stage replies under a separate fixed companion lifecycle profile.
- Retain authenticated capture and a one-handoff slot in source-selected schema v2
  of the same original controller StageStore; no side backend, file or managed resource.
- Add one explicit fixed companion claim endpoint on the existing trusted controller
  service. The authenticated original-scope request consumes that original slot and
  returns descriptor/binding facts to the runner. It confers no proof approval.
- Propose a distinct compound source accounting policy: one acquisition RPC with no
  nested network/credential lookup, then the unchanged12+2N handoff. Cumulative
  bound13+2N gives15/17/19 for N1/N2/N3. Existing private12 and prior accepted policy
  bytes stay unchanged. Cleanup/audit caps, qualification39 and other bounds stay
  hard gates; any actual extra work returns to governance.
- Preserve original counters, clocks, deadline and attempt across the acquisition
  and handoff. No late upgrade of an ordinary ledger, retry, refund or new approval.

This deliberately adds a closed internal operation and its narrow metadata/slot
permission to an existing trusted principal. It does not assert that current live
credentials already hold that permission. Exact source acceptance precedes code;
concrete principal/credential/hosting grants remain later T013 decisions.

## Capabilities

### New Capabilities

- original-registration-handoff: authenticated original capture, retained claim and
  bounded acquisition at the existing runner proof consumer.

### Modified Capabilities

No canonical neutral capability. Frozen parent packets/policy bytes remain unchanged;
the new source policy is separately identified in supporting-docs/acquisition-policy.json.

## Impact

The paired openXwallet feature017 plan and existing unchecked T013P08 own future
companion lifecycle/controller transport, original retention, acquisition accounting,
source construction and tests. Ordinary v1 wire/store/APIs remain closed and unchanged.
Source validation is not a connected runtime positive. P08/P09 remain incomplete.

Factory1368 and wallet106 landed normally as8833c7d001b3a and12cdf3161c5d with equal
ratified trees. Main CI verification is separate. Fresh Gate A source is archived;
36 databases/155 file-link hashes were independently audited before151 fixture
entries and three owned test/audit containers were removed.

Actual candidates are factory1369 and wallet107. Generate the corpus ledger with
that real factory identity, run source CI/local Codex review and obtain exact paired
source ratification before dependent code. Setup/dispatch remain unauthorized;
live/human/consumer gates separate, feedback deferred, blocked writes unreplayed.
