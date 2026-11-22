# Installer Regression Gates from the CPC Failures — Brainstorm

Status: brainstorm
Kind: process
Summary: Turn each observed runner-bootstrap failure into a reproducible regression or native preflight gate before another privileged installer is handed to an owner.
Topics: worker-onboarding-lessons, worker-host-app, worker-readiness, worker-enrollment, installer-regression-gates
Repository context: OmniWorker-Install owns installer realization and its test estate; openXfactory captures the neutral evidence and release-gate lessons without ratifying a new test contract.
Captured: 2026-11-21

## Possible feats

- A regression corpus built from the actual account, profile, token, task and serialization failures encountered during CPC enrollment.
- An installer release receipt binding immutable source, supported execution contexts, failure-injection results and native disposable-host qualification before owner execution.

## Focus

The pilot needed successive corrected scripts to register a Linux runner and
migrate it to service ownership. Preserving a narrative is useful, but preventing
the same rounds requires executable regression cases and native qualification.
This document is the proposed acceptance checklist for that realization. It
does not claim that a complete automated installer harness has been implemented.

## Failure-to-check matrix

The [bootstrap failure catalogue](worker-onboarding-lessons-recoverable-bootstrap.md)
records the incidents. The following matrix connects those failures to a gate
and the partial state that recovery must respect.

| Failure seen during setup | Regression or native preflight to require | State/effect to protect |
|---|---|---|
| Task principal text and the caller's account name represented the same user differently | Exercise name/alias/SID forms against actual task XML; compare resolved SIDs; reject a genuinely different SID | Reject mismatched ownership before stopping the original runner or changing files |
| A 72-character local-user description exceeded the 48-character API limit | Validate native cmdlet binding on the supported Windows build; include boundary-length and over-limit descriptions | Recover the recorded pre-account staging state without deleting it |
| Native profile initialization failed with `0x800706F7` after account creation | Qualify the real noninteractive task logon, expected profile directory, loaded user hive and session under a disposable supported Windows host | Resume only the recorded service account; preserve the account-created receipt and existing credentials |
| A previously loaded PowerShell helper type could survive into a corrected script run | Test a fresh process and repeated invocation; version helper types or avoid redefining native interop in an uncertain persistent session | Establish which implementation actually executed before attributing a new result to new source |
| Linux JSON parsing rejected a UTF-8 BOM in Windows-produced data or runner metadata | Test BOM and plain UTF-8 fixtures through the actual PowerShell/WSL/Python handoff and compatible decoder | Preserve existing registration files while inspection fails |
| PowerShell 7 produced a typed JSON `DateTime`, then string reparsing changed its UTC interpretation | Exercise strings with explicit offsets, UTC/local `DateTime` and `DateTimeOffset` across time zones; reject ambiguous input and truly expired receipts | Keep the ownership time tolerance narrow; preserve the instant instead of widening the guard |
| Updating a password-backed task action reported an incorrect username/password | Use an actual password-logon task to prove fixed action/credential reuse; inject update failure and exercise the administrator-owned allowlisted request channel | Keep the existing task binding and saved credential; do not rotate an unknown account as a repair |
| A non-terminating task error printed while the controller continued to stop/export the source | Inject boundary-call errors and verify terminating handling plus explicit native exit-code checks | Assert that no dependent source stop, export, import or registration occurs after a failed prerequisite |
| A Probe task ran while the controller waited for Import; stale success could be confused with the requested operation | Supply wrong mode, stale request ID, wrong SID/session and missing receipt; require the unique matching response and helper exit | Preserve the guarded source/export and inspect the actual helper before another operation |
| Hidden token input and remote clipboard transfer produced invalid/truncated input or the whole Configure command | Exercise local clipboard extraction of one token or a complete Configure command without executing it; reject control characters, oversized/malformed values and expired grants; prove log redaction and protected handoff | Keep credentials out of command lines, chat, source and ordinary logs; retain resumable non-secret state |
| An opaque wait left the owner uncertain whether the controller or helper was working | Exercise bounded progress/deadline output, cancellation, helper-still-running and helper-exited-without-receipt cases | Controller cancellation must not implicitly restart the source or launch a duplicate helper |
| An earlier operation's "Ready" was taken as completion of a later slot expansion | Bind readiness to operation/generation, expected endpoint names/count and actual provider IDs; test old receipts and missing registrations | Keep admission held until the requested inventory and qualification evidence exist |
| GitHub accepted a full-SHA runner-group selector for a non-reusable workflow, but its jobs remained queued | Test actual workflow admission; use the documented branch selector for a non-reusable workflow, separately check branch/run source, or use a SHA-pinned reusable workflow | Keep ordinary jobs held; policy-write success alone cannot qualify the route |

Parameter validation alone cannot qualify profile creation or credential-backed
Task Scheduler behavior. A successful parse cannot establish correct dispatch,
cross-account custody or rollback. These cases need the real APIs in a disposable
test estate matching the supported host/runtime combination.

## Candidate gate before owner execution

1. **Reproduce the failure.** Add a sanitized fixture or native scenario for the
   observed defect, show that the previous behavior fails, and prove the new
   behavior preserves the intended identity and authority boundaries.
2. **Exercise the complete runtime chain.** Parse and run relevant boundaries
   under both the interactive PowerShell version and the scheduled helper's
   actual Windows PowerShell version. Validate Bash and embedded Python as well
   as Windows-to-WSL encoding, environment and exit-code transfer.
3. **Inject failure before each mutation.** Prove dependency ordering and
   fail-closed behavior before source stop, export, target import, registration
   and release. Exercise resume from each owned partial state, including an
   already-created account and an already-exported distribution.
4. **Qualify native behavior on a disposable supported host.** Check the
   service logon/profile, fixed helper action, loaded WSL registration and
   noninteractive executor before repeating privileged owner-facing scripts.
   Do not turn the active donated worker into the default regression sandbox.
5. **Prepare one immutable candidate.** Bind source revision and checksum to the
   tested helper and Linux payload. Verify the published bytes match, and report
   the supported host, account and runtime assumptions plus remaining limits.
6. **Perform target preflight under the hold.** Check the exact host, current
   owner SID, protected receipts, idle task/process state, existing launcher
   digest, effective resources and backing-disk capacity. Refuse unknown state
   before mutation. Keep task credentials and unrelated installations intact.
7. **Record scoped completion and qualification.** Emit the operation, endpoint
   inventory and phase reached. Independently read provider registrations and
   run the requested workload/concurrency test before releasing admission.
   A no-sign-in reboot remains a separate acceptance gate.

The goal is one recoverable, qualified installer rather than repeated edited
commands handed to the owner. A newly discovered native failure should expand
this corpus and the implementation's test suite. The owner should receive the
concrete failed phase and safe next action, with credentials and raw exports
kept local.

## Retain the known-good pilot artifacts

The managed pilot's operator scripts remain in the private Tenant repository;
they are evidence and implementation references, not the public donor package:

| Completed pilot operation | Source reference | What that source qualified |
|---|---|---|
| Resume the already-exported service-account migration | [Complete-ExportedMigration.ps1 at the accepted recovery revision](https://github.com/opensoft/Opensoft-Tenant/blob/103004584eb23c268fdcf8c80f39ff6921457ce4/ops/cpc-linux-service-migration/Complete-ExportedMigration.ps1) | Retained export reuse, fixed helper task/credentials, request-specific receipts, service-account profile/session and target startup |
| Add three Linux registrations under the expansion hold | [Add-CpcLinuxRunners.ps1 at the accepted expansion revision](https://github.com/opensoft/Opensoft-Tenant/blob/200142992dfe21a810c8da8932208f9f002ddb5b/ops/cpc-linux-fleet/Add-CpcLinuxRunners.ps1) | Existing owner/task checks, separate slot accounts and registrations, protected transient token handoff and shared child-service limits |
| Qualify startup after an actual reboot with no desktop sign-in | [Six-job reboot workflow at its accepted revision](https://github.com/opensoft/Opensoft-Tenant/blob/1962c594ef69152df8ecec9d5cb4b51b4d9ef42d/.github/workflows/cpc-reboot-qualification.yml) | New Windows/WSL boot identities, fresh service-owner evidence, all four Linux jobs and no-desktop checks before/after them |

Use the protected operator receipts for the matching checksums and actual
execution results. Start a repair by inspecting the applicable accepted source
and current phase instead of reconstructing an older command from chat. These
references do not authorize rerunning a migration against a later state. The
reboot proof binds one fresh captured baseline; every future reboot test needs
a new baseline and operation/source binding. Recovery or expansion success alone
does not establish cold startup. These precedents still need extraction into
the owning host product with the regression corpus above and supported-host
qualification.

## Relationships and open questions

Combine this checklist with [recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md),
[service identity/tool environments](worker-onboarding-lessons-service-identities-and-tools.md),
[credential handoff](worker-onboarding-lessons-credential-handoff.md),
[maintenance admission](worker-onboarding-lessons-maintenance-admission.md) and
[qualification](worker-onboarding-lessons-qualification-and-portability.md).
The [enrollment synthesis](worker-onboarding-lessons-synthesis-donor-enrollment.md)
connects installer evidence to the owner journey; the
[operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md)
connects it to holds and runtime acceptance. Supported Windows/WSL build coverage,
disposable-test provisioning, fixture ownership and release custody still need
realization in the host product.
