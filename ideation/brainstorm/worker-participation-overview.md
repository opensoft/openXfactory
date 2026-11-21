# Worker Participation, CI and Shared Capacity — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Capture the missing participation model around existing omniWorker designs: independent GitHub registration, factory CI, optional Linux onboarding and platform-wide donated capacity.
Topics: worker-participation, worker-enrollment, ci-execution, donated-compute, workstation-intake
Repository context: openXfactory is the neutral contract and reference-stack owner; OmniWorker-Install owns the worker-host product; runtime integration belongs to its assigned implementers.
Captured: 2026-11-20

## Possible feats

- An omniWorker journey that inventories a machine and offers qualified Windows
  and optional Linux capabilities.
- Independent enrollment for factory work and registration for direct GitHub
  Actions work, with CI supported as a factory workload.
- One donation enrollment usable by all eligible xFactories under standing
  owner consent and a shared host resource budget.

## Why this supplement exists

Manual Windows Cloud PC CI setup prompted a broader onboarding discussion:
discover installed tools under the actual execution account, distinguish
logical runners from physical capacity, and offer Linux capability when WSL is
absent. The follow-on requirement was a participation model spanning individual
factories and owners who simply want to donate computing time.

The repository already contains substantial coverage. This packet supplements
that work; it is design capture, not deployment evidence, policy ratification,
or authorization to install software on a host.

## Coverage checked in this repository

| Subject | Existing source | Remaining contribution here |
|---|---|---|
| Owner app and unattended host | [Omni overview](omni-unattended-worker-overview.md), [host topology](omni-unattended-worker-host-manager-topology.md), [staged host app](../staging/worker-host-app/worker-host-app.md) | Capability-led onboarding and separate participation choices |
| Current product ownership | [omniWorker naming record](../../docs/omniworker-naming.md) | Reuse omniWorker in OmniWorker-Install rather than invent another host app |
| Linux on Windows | [Worker-owned WSL design](omni-unattended-worker-wsl2-worker-owned-distro.md) | Optional consent, missing-WSL journey and readiness under the executor account |
| Host resource limits | [Aggregate budget and owner controls](omni-unattended-worker-aggregate-budget-and-owner-controls.md) | Account for independent direct GitHub and factory work sources |
| Enrollment and authority | [Worker-enrollment contract](../../contracts/worker-enrollment/README.md), [enrollment authorization brainstorm](omni-unattended-worker-enrollment-authorization.md) | Distinguish platform enrollment, GitHub registration and factory membership; identify contract changes still needed |
| CI execution and donated-host trust | [Governed dispatch](omni-unattended-worker-synthesis-governed-dispatch.md), [sandboxed execution](omni-unattended-worker-synthesis-sandboxed-execution.md) | Explicit factory CI participation without donor-managed GitHub registration |
| Shared donation scope | Existing Omni packet covers volunteered compute and governed dispatch | One platform enrollment usable by eligible factories without individual membership |
| Unmanaged intake | [Promoted workstation-intake specification](../../openspec/specs/workstation-intake/spec.md) | Preserve the existing Microsoft-enrollment requirement and identify personal donation as a future delta |

The existing enrollment contract is ratified but describes GitHub-oriented
grants. The Omni packet is brainstorm material. The staged host-app documents
are also design sources, not evidence that the requested onboarding or shared
pool runs today. This review establishes documentation coverage, not a runtime
implementation audit.

## Captured user requirements and design options

Brett requested CI work through xFactory workers as well as direct GitHub
runners, recognized the two registration relationships, and requested donation
by registering with openXfactory so all xFactories can use the contribution.
He also proposed an app that inventories OS and hardware and asks whether to
add WSL for Linux work on a Windows machine.

This packet interprets “all xFactories” as all **eligible** factories within the
owner's accepted donation scope and the platform's trust and admission policy.
It does not grant unrestricted host access or release private inputs. Selected
factories, mixed reservations, fixed resource partitions and specific adapter
choices are proposed design options; they were not settled by that discussion.

## Terms and intended ownership

| Term | Meaning |
|---|---|
| Platform enrollment | An authorized, renewable relationship between a host/worker and the openXfactory runtime |
| Factory membership | A human or organizational relationship with a particular factory; not required merely to donate capacity |
| GitHub runner registration | A logical Actions execution endpoint registered in an authorized GitHub scope |
| Host | The machine whose resources are shared by its execution environments |
| Execution environment | A qualified native, WSL or other supported execution context |
| Work slot | An admitted unit of execution capacity; not additional hardware |
| CI workload | Build/test/package work, whether requested through GitHub or a factory integration |

omniWorker owns the host experience and reconciliation. openXfactory owns
neutral contract design. Existing enrollment and clearing/dispatch seams should
be extended where appropriate; the shared pool's service placement and factory
adapters still need assigned implementation ownership. The repository name does
not imply an already deployed global scheduler.

## Packet map

Start with the [onboarding and dispatch synthesis](worker-participation-synthesis-onboarding-and-dispatch.md),
which connects all four atomic documents:

- [Registration boundaries and CI routes](worker-participation-registration-boundaries.md).
- [Capability-aware onboarding and optional WSL](worker-participation-capability-onboarding.md).
- [Shared network participation and eligibility](worker-participation-shared-network-pool.md).
- [Aggregate host admission across work sources](worker-participation-shared-host-admission.md).

## Follow-on decisions

The next design step should resolve the transport-neutral enrollment boundary
against existing contracts, select an initial factory CI adapter and result
publication path, locate shared allocation in existing dispatch ownership, and
qualify Windows/Linux admission under real service identities. Personal
donation also needs the already identified workstation-intake delta. No
OpenSpec proposal, contract promotion, scheduler implementation or host change
is performed by this documentation packet.
