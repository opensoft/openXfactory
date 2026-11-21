# Service Identities and Execution Tools — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Inventory and qualify tools under the actual service identities while keeping platform identity, Windows ownership, Linux users and GitHub registrations distinct.
Topics: worker-onboarding-lessons, installation-identity, worker-host, worker-readiness, ci-execution
Repository context: openXfactory owns identity and readiness semantics; OmniWorker-Install owns host reconciliation and credential binding.
Captured: 2026-11-21

## Possible feats

- An identity map linking installation, environment owner, executor and provider registration without treating their identifiers as interchangeable.
- Tool probes that run as the service account and detect stale service PATH or incompatible clean-environment execution.

## Focus

“Installed on the machine” did not establish that a CI service could execute a
tool. The pilot also exposed the difference between a Windows account owning
WSL and a Linux account running a job. These are separate identity layers.

| Layer | Responsibility | Qualification fact |
|---|---|---|
| Installation and lease | Platform relationship and current authority | Stable installation identity, enrollment generation and active scope |
| Windows execution owner | Profile, WSL registration and startup | Canonical SID, loaded profile, allowed logon type and task/service binding |
| Linux execution account | Job files, processes and tool cache | Actual UID/GID, account restrictions and workspace ownership |
| GitHub registration | Logical Actions endpoint | Runner ID, configured group, labels and independently observed connection |

Local account names are not installation identity, and service-account
credentials are not broker renewal authority. The
[installation-identity design](omni-unattended-worker-installation-identity.md)
retains ownership of platform identity and credential generations.

## Observed failures and proposed handling

- Windows rendered the same task principal through different account-name
  forms. Compare resolved SIDs and the exported task definition, and reject
  conflicting identities. Do not relax an ownership check to a name substring.
- `New-LocalUser` rejected a 72-character description because its installed
  cmdlet limit was 48. Probe real parameter constraints before creating state;
  syntax parsing alone cannot establish that an installation call will bind.
- Explicit native `CreateProfile` returned `0x800706F7`. The successful path
  used a password-backed scheduled-task logon and then verified its profile
  path, user hive and session. This is an observed workaround on the tested
  build, not a diagnosis of all Windows profile failures or a guarantee for
  every supported build.
- A generated local account password outlived the failed process only in its
  bound operating-system tasks. Recovery must follow the applicable credential
  custody policy. A narrow pre-task recovery rotated the newly created account
  only after checking protected state, identity and absence of dependent tasks
  or services. That is not permission to reset an unrelated account.

The pilot did not establish managed vault escrow at birth. Do not present its
manual credential lifecycle as fulfillment of the staged host app's custody
design. Prefer supported managed identities where feasible, or an explicitly
governed credential generation and task/service rotation mechanism.

## Tools are properties of an executor

Windows .NET and PowerShell installed under the desktop user's profile were
not sufficient evidence for a service. Use an appropriate machine installation
or a service-owned/job-local tool path. Probe effective PATH, executable path
and version under the service identity. A running service can retain an older
environment; any restart used to refresh it should drain work first.

On Linux, private workspaces and tool caches support installation without sudo.
The platform validation pilot installed pinned utilities in a job temporary
directory. Its Python 3.12 build worked in the normal job environment but
clean-environment subprocesses exposed a shared-library lookup dependency. A
job-private Python copy with a relative ELF lookup path passed those tests
without changing the shared cache or host linker configuration. A `--version`
probe alone would have missed that capability failure.

## Boundaries and relationships

Separate accounts and restrictive workspace permissions reduce accidental
cross-job access; they do not make hostile volunteer code safe or prevent a
host administrator reading inputs. Use the existing executor and trust gates.
Do not change the owner's editor, desktop agent runtime or personal tool
configuration as a side effect of worker setup.

See [WSL startup](worker-onboarding-lessons-wsl-ownership-and-startup.md),
[qualification](worker-onboarding-lessons-qualification-and-portability.md) and
[the onboarding synthesis](worker-onboarding-lessons-synthesis-donor-enrollment.md).
