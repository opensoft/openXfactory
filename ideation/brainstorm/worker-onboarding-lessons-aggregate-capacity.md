# Measured Capacity and Logical Work Slots — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Count physical resources, execution envelopes and logical registrations separately, then enforce an owner-approved aggregate budget across independently scheduled work.
Topics: worker-onboarding-lessons, aggregate-budget, owner-controls, ci-execution, worker-readiness
Repository context: openXfactory owns admission semantics; omniWorker owns host accounting; each executor declares its actual enforcement boundary.
Captured: 2026-11-21

## Possible feats

- A host view that distinguishes hardware, environment ceilings, work slots and duplicated provider-registration views.
- Admission based on enforceable parent budgets and workload demand rather than the number of installed services.

## Focus

The pilot had two factory-oriented Windows workers that were themselves GitHub
registrations, one general Windows CI runner, and one Linux CI runner. That was
four logical endpoints, not six and not four independent machines. GitHub's OS
view counted three Windows registrations and one Linux registration. The same
service must not be counted again merely because it appears in two products.

## Distinguish the resource views

The managed host was an 8-vCPU, 32-GiB Cloud PC. Its service-owned WSL environment
reported about 16 GiB RAM. Inside the existing two-CPU cgroup, `nproc` reported
two, while the host inventory described eight logical processors. Linux's
virtual disk reported much more potential capacity than the underlying Windows
disk. These observations motivated separate checks of host CPU/RAM, guest
memory, effective cgroup constraints, guest free space and backing-volume free
space before promising new capacity.

| Quantity | Meaning |
|---|---|
| Host resources | Shared physical/virtual machine capacity consumed by Windows, WSL and host overhead |
| Environment ceiling | A VM or per-user WSL limit; excludes some host overhead |
| Per-runner maximum | A bound on one service, not a reservation or guaranteed throughput |
| Parent allocation | A shared ceiling that can be tighter than the sum of child maxima |
| Slot count | Number of logical jobs that could execute; not a performance claim |
| Ready capacity | Qualified, consented and currently admitted work after competing consumers are accounted |

## Pilot budget and later expansion qualification

The existing Linux service's enforced limits were two CPU equivalents and
8 GiB RAM. A real CI job checked its cgroup CPU ratio and memory maximum.

Three additional Linux registrations were requested and an installer prepared.
Its proposed partition kept the original limit and placed the additions in a
shared slice capped at four CPU equivalents and 6 GiB RAM. Each child had a
two-CPU and 4-GiB maximum subject to that parent. Combined Linux service maxima
were therefore six CPU equivalents and 14 GiB RAM. The three child memory
maxima did not each reserve 4 GiB. Concurrent heavy jobs could experience
contention or memory pressure within the shared pool.

At the initial checkpoint that expansion was only prepared. The owner later
executed the installer under the admission hold, and four distinct Linux
registrations passed the parallel qualification with 88 seconds of overlapping
workspace execution. The test checked the actual child and shared-parent
constraints before normal dispatch was restored. This establishes concurrent
logical execution under that envelope; it does not prove that four large builds
fit comfortably or receive their individual maxima simultaneously. The numbers
remain a dated managed-host example, not public-donation defaults or a benchmark.

CPUQuota percentages refer to CPU equivalents, not a percentage of all host
processors. Memory ceilings and reclaim thresholds are not admission control.
See the [systemd resource-control reference](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
for the hierarchy used by that example.

## Aggregate admission still belongs to the owner budget

Linux cgroups do not cap independent native Windows factory/CI jobs or every
host-manager operation. Reserve virtualization and service overhead and account
for packages, caches, logs, retained exports, network and temporary tools.
Direct GitHub dispatch requires a qualified gating integration or a conservative
reserved partition; a local UI cannot claim to gate jobs simply by observing
them. Do not spend the same donated allocation through factory dispatch and an
independent GitHub scheduler.

Pause, schedules, battery and metered-resource controls remain durable owner
intent. New registrations, reconciliation, updates and job completion must not
silently increase the accepted allocation or undo pause. GPU eligibility needs
its own qualification; available CPU does not establish it.

## Relationships and open questions

Reuse [aggregate budget and owner controls](omni-unattended-worker-aggregate-budget-and-owner-controls.md)
and [shared host admission](worker-participation-shared-host-admission.md).
Resource classes, Windows enforcement, scheduler integration and capacity
requalification remain product decisions. See
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
