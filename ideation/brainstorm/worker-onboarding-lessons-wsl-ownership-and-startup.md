# WSL Ownership and Unattended Startup — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Establish the Windows worker identity and loaded profile before WSL ownership, then prove boot startup independently of desktop sign-in or RDP reconnection.
Topics: worker-onboarding-lessons, wsl2-worker-owned-distro, worker-host, worker-readiness, executor-ladder
Repository context: openXfactory owns neutral environment evidence; OmniWorker-Install owns Windows identity, distribution lifecycle and startup reconciliation.
Captured: 2026-11-21

## Possible feats

- Service-owned WSL installation and detection that never depend on an owner's desktop session.
- A migration operation that transfers a qualified managed executor while preventing duplicate provider registrations from running.

## Focus

The initial Linux service was healthy, but its distribution belonged to the
interactive Windows user and its keepalive ran at that user's logon. RDP
disconnect survival did not prove startup after a Windows reboot. Changing
only the task account would not transfer distribution ownership:
[Microsoft documents WSL distributions as per-user installations](https://learn.microsoft.com/en-us/windows/wsl/setup/environment).

## Proposed installation order

1. Reconcile machine prerequisites under the authorized supervisor.
2. Establish the dedicated Windows owner, its allowed non-interactive logon
   path and credential binding; deny interactive/RDP logon as policy requires.
3. Start a probe as that identity. Verify SID, non-administrator status, session
   context, profile path, profile registry hive and WSL access.
4. Register/import and inspect the worker distribution in that same Windows
   context. `wsl --user` selects a Linux user; it does not select the Windows
   distribution owner.
5. Create Linux service identities, services, startup and worker-context
   detection. Advertise capability only after execution acceptance.

In the pilot, one Windows service owner held the CI distribution, while a
different non-root Linux account ran the CI service. Its password-backed boot
task ran in session 0 with a 45-second boot delay, unlimited execution time,
single-instance behavior and failure retries. A Windows-held WSL command kept
the distribution alive; enabling a systemd service alone was not the complete
Windows startup chain.

## Managed migration and rollback lesson

The successful managed-host migration first disabled the old logon task,
stopped the original runner, and added an unsatisfied startup guard before
exporting. The imported copy retained that guard until the new Windows owner
activated it. This prevented the same copied GitHub registration and its
credentials from connecting in both distributions.

The export included the existing Linux filesystem and credentials. It stayed
local under restricted access, with a verified checksum. This was an authorized
managed migration, not a clean donor installation. A new personal donation
journey should create its own distribution rather than copy or adopt the
owner's personal environment by default.

Rollback should first prove the target executor stopped and guarded, then
restore the source. Preserve the original distribution and export until the
chosen acceptance gate; retaining them creates disk and credential custody
obligations. Do not upload them as ordinary logs or delete them implicitly.
Migration, profile initialization and package changes need resumable state and
an explicit drain/cancellation policy for active jobs.

## Qualification and containment boundaries

The pilot first proved non-interactive service-account launch and real CI.
The later [six-job reboot qualification](https://github.com/opensoft/Opensoft-Tenant/actions/runs/44968376008)
also passed for all four Linux registrations. It compared fresh pre/post Windows
and WSL boot identities, checked renewed service-owner evidence, and found no
signed-in desktop users before or after the four Linux jobs. The owner kept the
remote client closed throughout this proof. Session 0 or an old success receipt
alone would have been insufficient.

The later four-runner test used a more explicit proof sequence:

1. Hold every known endpoint on the machine, including native/factory workers,
   and retain each registration's original group. Collect a fresh Windows boot
   timestamp, WSL kernel boot ID and service-owner receipt. Prove that the
   session probe can see the existing desktop before the restart.
2. Restart the machine and close its remote client. Observe provider disconnect
   and reconnect without entering the desktop or invoking WSL from an inspection
   session. Opening the distribution to inspect it could start the capability
   the test is meant to qualify.
3. Use a native Windows service job to compare the new boot identity and check
   for no signed-in users or desktop shell. This job reads CIM/session state;
   it never launches WSL or starts a runner service.
4. Execute a separate job on each expected Linux registration. Check the new
   shared WSL kernel identity, a refreshed owner receipt for that Windows boot,
   service-account session 0, enabled/active systemd units, enforced limits and
   private checkout/workspace execution.
5. Repeat the Windows no-desktop check after the Linux jobs. Restore only the
   operation's owned routing changes after all proof jobs pass, preserving the
   unrelated fleet's maintenance and each factory worker's original access.

The baseline probe could read the interactive user and Explorer session under
the existing non-administrator Windows CI account. The postboot counterpart
requires those observations to be absent. This supplies explicit local session
evidence in addition to the owner's report that the remote client stayed closed.
It remains managed-host operational evidence, not attestation against a hostile
donor. An online flag alone cannot establish this result. Every later reboot
qualification needs its own fresh baseline and operation/source binding;
rerunning a workflow against this operation's old baseline would not prove that
another restart occurred.

The [worker-owned WSL design](omni-unattended-worker-wsl2-worker-owned-distro.md)
already addresses ownership and executor boundaries. Multiple services in one
distribution share its kernel and environment. The trusted managed pilot's
sharing model does not establish concurrent isolation for unrelated volunteer
attempts or replace that design's stronger boundary choices. Preserve unrelated
WSL sessions; a host-wide shutdown is not a routine repair for one executor.

## Relationships and open questions

Supported Windows/WSL builds, first-boot behavior, update qualification and
retirement still need a tested product matrix. See
[service identities](worker-onboarding-lessons-service-identities-and-tools.md),
[recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md) and
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
