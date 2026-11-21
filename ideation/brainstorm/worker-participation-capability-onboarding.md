# Capability-Aware Worker Onboarding — Brainstorm

Status: brainstorm
Kind: process
Summary: Reuse omniWorker to inventory a host, offer optional Linux capability on Windows, and qualify execution under the actual worker identity.
Topics: worker-participation, worker-host, workstation-intake, wsl2-worker-owned-distro, worker-readiness
Repository context: openXfactory owns neutral intake and readiness semantics; OmniWorker-Install owns host installation and the native owner experience.
Captured: 2026-11-20

## Possible feats

- An inventory-led onboarding flow for managed and owner-donated machines.
- Explicit, resumable approval for adding WSL capability to a Windows host.
- Capability claims backed by probes under the service or executor identity.

## Focus

Extend the existing **omniWorker** host product rather than introducing another
host manager. The [naming record](../../docs/omniworker-naming.md) assigns that
product to `opensoft/OmniWorker-Install`; older notes naming Omnigent-Install as
host owner predate the split.

The app first inventories OS and architecture, CPU, memory, free disk, relevant
build tools, virtualization availability, existing Linux environments, and known
worker or GitHub runner registrations. It distinguishes observed facts from
requested changes and never infers permission to take over existing resources.

The owner chooses participation and work capabilities. On Windows, native
Windows work can be selected independently of Linux work. If Linux execution
requires WSL that is absent, the app explains the proposed installation, disk
allocation, privilege requirements and possible restart, and asks for explicit
consent. Declining leaves the host eligible only for capabilities it can actually
provide. Existing WSL installation is an inventory fact, not proof of an
approved executor for donated code.

## Proposed onboarding sequence

1. Inventory without mutation and show the relevant findings.
2. Choose [registration relationships](worker-participation-registration-boundaries.md),
   allowed workloads, participation scope and resource limits.
3. Present required host changes, including optional WSL, and obtain consent.
4. Apply changes through the existing host reconciler; checkpoint progress for
   elevation, restart, retries and cancellation.
5. Qualify each execution environment using its actual account and service
   context; then advertise only the capabilities that passed.

On Windows, tools installed in an interactive user's profile may be unavailable
to a service. Readiness therefore probes the effective PATH and executable
versions under the executor identity, not just the desktop user. A successful
installer exit does not prove readiness. The acceptance path should also prove
startup after reboot, operation without an interactive desktop, and recovery
after a disconnected session.

## Reuse and qualification boundaries

The [host-manager topology](omni-unattended-worker-host-manager-topology.md)
already separates privileged reconciliation from UI and execution. The
[worker-owned WSL design](omni-unattended-worker-wsl2-worker-owned-distro.md)
already covers dedicated ownership and isolation concerns. Reuse those designs:
do not adopt the owner's personal distribution, change their editor or Codex
runtime settings, or treat two distributions as independent security boundaries.
WSL support and containment on the exact host still need qualification before
advertising untrusted Linux execution.

The staged [Worker Host App](../staging/worker-host-app/worker-host-app.md)
and [WSL setup](../staging/worker-host-app/wsl-install-and-setup.md) describe
earlier installation work. Their existence is not evidence of today's deployed
capability. The promoted [workstation-intake specification](../../openspec/specs/workstation-intake/spec.md)
ties unmanaged intake to an approved Microsoft enrollment route; personal
donation without device management needs an explicit future requirement delta,
as the existing Omni enrollment brainstorm already identifies.

## Open questions

Which OS versions and WSL configurations will the first release qualify? What
changes require administrator approval? Which probes establish capability
expiry after tool or policy changes? These remain realization decisions; this
packet authorizes no host installation or restart.
