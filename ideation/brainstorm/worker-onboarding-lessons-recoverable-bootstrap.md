# Recoverable Worker Bootstrap — Brainstorm

Status: brainstorm
Kind: process
Summary: Replace repeated setup commands with a durable, identity-checked reconciler that halts on prerequisite failure and accepts only fresh evidence for the requested operation.
Topics: worker-onboarding-lessons, worker-host-app, worker-readiness, owner-controls, worker-enrollment
Repository context: OmniWorker-Install owns host reconciliation; openXfactory owns the neutral state and evidence seams proposed here.
Captured: 2026-11-21

## Possible feats

- A checkpointed installer that resumes known partial states without deleting unknown resources or rerunning completed enrollment.
- Credential-independent helper dispatch with operation IDs, terminating errors and negative recovery tests.

## Focus

The manual pilot required repeated repair commands. The product lesson is to
build the existing host-manager reconciler, not expose that command sequence
as the normal donation journey. Recovery has to preserve both running jobs and
the owner's unrelated machine state.

## State before retries

Candidate phases are inventoried, identity-created, profile-qualified,
environment-prepared, source-guarded, exported/imported when migration applies,
registered, executing, and acceptance-pending. A receipt should bind the
operation ID, installation generation, canonical owner SID, environment,
provider runner ID, artifact revisions and relevant policy. These are proposed
fields, not a new ratified schema.

An existing folder, account or online registration is not sufficient proof to
reuse it. The pilot recovered an otherwise empty staging folder only after
checking its protected state file and exact ownership. Later account recovery
required the matching SID or a narrowly checked legacy creation receipt, the
expected account shape, and no dependent tasks/services before rotating its
generated password. Unknown files and later phases were preserved and refused.

## Failure catalogue and the resulting checks

| Observed failure | Reconciler lesson |
|---|---|
| Account-name strings differed for the same Windows principal | Resolve canonical SIDs and inspect the registered task definition; report a real mismatch without weakening identity checks |
| Local-account description exceeded the cmdlet's 48-character maximum | Validate actual API constraints and use non-mutating parameter checks before creating persistent state |
| Native profile creation failed after the account existed | Checkpoint account identity early; verify the actual profile from the service logon before substrate changes |
| GitHub runner `.runner` JSON carried a UTF-8 BOM | Use an explicit compatible decoder such as `utf-8-sig` and test both encodings against the real file format |
| PowerShell 7 parsed a JSON UTC timestamp into `DateTime`, then string reparsing treated it as local time | Preserve the instant and type across strings, `DateTime` and `DateTimeOffset`; reject ambiguous dates rather than widening ownership time tolerances |
| Updating a password-backed scheduled-task action failed with a credential error | Keep the action and credential binding stable; select a bounded operation through administrator-owned input or another authenticated local control channel |
| A non-terminating task error was printed but the controller continued | Use explicit terminating error handling at boundary calls and verify task/state/receipt success before dependent mutations |
| An unchanged Probe task ran while the controller waited for Import | Bind each operation to a unique request ID and receipt path; mode and identity must match, and stale success is not evidence |
| The UI appeared to wait indefinitely | Show the active phase, progress, bounded deadline and whether a helper is still running; distinguish parsing/input, download, import and provider waits |

In the serious task-update failure, the controller continued far enough to
stop/guard the source and export it. Correct recovery reused the saved task
credentials and retained export, inspected target absence, and imported only
after the requested helper operation was proven to run. Repeating the original
installer or blindly restarting the source could have created duplicate
listeners or overwritten partial state.

## Stable privileged helper

The working recovery kept one fixed helper task action. Administrator-owned
requests selected allowlisted operations, and the service account could read
but not rewrite those requests or launcher code. Responses included a unique
request ID, operation, SID, session and explicit outcome. The controller checked
those values and task completion before advancing.

This is an implementation precedent, not a claim that a writable status file
is independent attestation against a malicious host. Provider status and
independent acceptance remain separate. A public donor may control the host.

## Cancellation and rollback

Stopping the controller does not prove its helper or Linux processes stopped.
Inspect actual task/process and provider state before retrying. Do not kill an
unknown import, unregister a distribution, reset an unrelated password, or
delete the whole staging tree as a generic repair. For migration rollback,
prove the target stopped before re-enabling the source. Preserve owner pause,
maintenance holds and live job ownership.

Negative checks should inject task errors and prove no dependent source stop,
export or registration occurs; reject stale receipts, mismatched SIDs,
unexpected files, later phases, ambiguous dates and wrong-host invocation.
Static parsing alone did not catch the pilot's binding or runtime failures.

## Preventing the next script-repair loop

Use the [installer regression gates](worker-onboarding-lessons-installer-regression-gates.md)
as the concrete failure-to-check map. Each fix needs a reproducing fixture or
native scenario, a proof that later mutations are fenced on failure, and a
known-state resume check. Qualify the complete interactive/helper/WSL chain on
a disposable supported host before presenting another immutable candidate to
the owner. Documenting the symptom alone does not establish that this regression
gate exists in the product.

## Relationships and open questions

Receipt schema ownership, generation/rollback fencing and crash recovery need
realization against the existing host-manager design. See
[credential handoff](worker-onboarding-lessons-credential-handoff.md),
[WSL ownership](worker-onboarding-lessons-wsl-ownership-and-startup.md), and
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
