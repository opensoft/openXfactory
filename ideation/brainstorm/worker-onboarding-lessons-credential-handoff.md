# Scoped Enrollment and Credential Handoff — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Keep administration authority away from worker jobs and use transient, scoped enrollment material with protected local handoff and independently checked receipts.
Topics: worker-onboarding-lessons, worker-enrollment, credential-reach, installation-identity, donated-compute
Repository context: openXfactory owns enrollment and trust contracts; the broker owns grant issuance; OmniWorker-Install owns local handoff and cleanup.
Captured: 2026-11-21

## Possible feats

- Broker-issued enrollment grants consumed without displaying or persisting administration credentials on the host.
- A local handoff that is bound to an authorized operation, redacts output and expires safely after interruption.

## Focus

Four credential classes appeared in the setup and must remain distinct: a local
OS service-account password, authority to authenticate to the enrollment
broker, a short-lived GitHub registration token, and the credentials a running
job can reach. Success in one exchange grants no authority in the others.

The [worker-enrollment contract](../../contracts/worker-enrollment/README.md)
already separates estate policy, leases, transient registration grants and
renewal. Its volunteer estate has no standing broker-authentication secret on
the host. A local OS credential used to start a service must not become a
backdoor broker credential or replace renewable authority. Managed credential
custody and the volunteer no-standing-secret rule are different policy cases.

## Observed manual enrollment lessons

The pilot's GitHub CLI sign-in could read setup source but could not mint the
organization registration token. Authentication success did not establish the
required authorization. The managed fallback used the organization's runner
setup page and a fresh short-lived token, not a password, PAT or App key.

Remote clipboard transfer and secure console input were unreliable: a hidden
prompt accepted a control character rather than the intended pasted token,
and the runner returned HTTP 400. The working manual path copied the Configure
command inside the CPC browser, waited for Enter only, read the local clipboard,
extracted the token without executing the command, and validated it before
changing Linux state. Accepting the complete Configure command reduced
copy-selection errors. Do not log clipboard contents or diagnose rejection by
asking the owner to paste credentials into chat.

This is a break-glass lesson for an approved managed host. A public donation
app should obtain the scoped grant through the enrollment broker rather than
teach volunteers to acquire organization administration material.

## Cross-account handoff

The additional-runner installer prepared a Windows DPAPI LocalMachine-encrypted
temporary handoff file under the existing administrator/SYSTEM/service-account
ACL. The service could decrypt it and forward the token in the child process
environment, with redaction before logging and cleanup afterward. At the
documented checkpoint this installer was prepared, not proven by completed
three-runner enrollment.

LocalMachine encryption is not a per-service authorization boundary:
[Microsoft's scope reference](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.dataprotectionscope)
states that other processes on the computer can decrypt machine-scoped data if
they obtain it. The file ACL, restricted operation, short lifetime and cleanup
are therefore essential; ciphertext alone is not the security claim. Product
implementation may choose a narrower authenticated local channel.

Do not put the token in source, command-line arguments, task XML, a durable
lease/audit record, exported reports or a shared workspace. An interrupted
handoff must remain bounded by token expiry and protected custody. Removal of
the transient token does not remove the provider credentials created by a
successful runner registration; their lifecycle needs its own revocation path.

## Authority after enrollment

The managed pilot's Default group allowed private organization repositories
and excluded public repositories. Do not reuse that broad private access for
donation. Preserve the existing
[volunteer contribution-repository boundary](omni-unattended-worker-credential-reach-and-contribution-repository.md),
[ephemeral attempt grant](omni-unattended-worker-ephemeral-runner-attempt-grant.md)
and independent output acceptance. Labels route work; they are not proof that
a donor or a result is trustworthy.

## Relationships and open questions

The broker's realized transport, grant-to-local-operation binding, cross-platform
secret handoff and interrupted-cleanup policy remain product decisions. See
[recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md) and
[the onboarding synthesis](worker-onboarding-lessons-synthesis-donor-enrollment.md).
