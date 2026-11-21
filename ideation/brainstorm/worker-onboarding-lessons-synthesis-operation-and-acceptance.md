# Synthesis: Worker Operation and Evidence-Based Acceptance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Connect startup ownership, fenced recovery, shared capacity, maintenance admission and job-specific evidence so donated capacity is advertised and restored honestly.
Topics: worker-onboarding-lessons, worker-readiness, aggregate-budget, owner-controls, observability, synthesis
Repository context: openXfactory owns neutral admission and acceptance seams; host managers, executor adapters and independent verifiers supply their own evidence.
Captured: 2026-11-21

## Possible feats

- A readiness ledger that distinguishes registration, workload success, actual concurrency and unattended reboot acceptance.
- Recovery that preserves owner controls and active work while reconciling local processes with provider and platform state.

## Members and their joints

Atomic members are [WSL startup](worker-onboarding-lessons-wsl-ownership-and-startup.md),
[recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md),
[aggregate capacity](worker-onboarding-lessons-aggregate-capacity.md),
[qualification and portability](worker-onboarding-lessons-qualification-and-portability.md),
[maintenance admission](worker-onboarding-lessons-maintenance-admission.md), and
[job-level observation](worker-onboarding-lessons-job-observability.md).

### Capacity advertisement depends on both runtime state and current authority

The host manager reserves overhead, intersects the accepted owner budget with
qualified executor controls, and accounts for every route sharing that host.
Logical registration count is inventory. Available admission is a separate
decision about current authority, workload demand, live execution and owner
intent. A heartbeat gap cannot release resources if an executor may still run.

Fixed partitions can bound independently scheduled GitHub and factory work
until an actual coordination mechanism exists. A Linux parent cgroup can bound
its children, but cannot by itself enforce a Windows-wide donation percentage.
Proposed UI values should state whether they are enforced, measured or planned.

### Recovery changes what evidence remains usable

An identity, profile, package or budget change can invalidate a prior readiness
receipt. Restarting a service to refresh PATH is a runtime intervention, not
just a metadata update. The same reconciler that applies changes should drain
work, keep durable phase/operation identities, reject stale success, and leave
unknown state unavailable rather than assume it is free.

A guarded migration has a critical ordering edge: the old registration must
stop before a copied identity can start, and rollback must reverse that safely.
Controller cancellation, helper termination and provider disconnection are
different facts. The owner should see which one has actually occurred.

### Startup evidence and workload evidence close different loops

A successful non-interactive job proves an executor can work under the service
identity. A no-sign-in reboot test proves the whole Windows-profile/WSL/systemd
chain can recreate that capability. A four-slot overlap test proves concurrent
logical execution; it does not guarantee that four large builds fit within the
shared memory envelope. All three claims require their own evidence.

Likewise, a full CI pass for one head/profile does not accept another source
revision. Workflow routing and compatibility conditions must move together,
without dropping tests or weakening environment-isolation assertions. The
owner-facing health view should identify a workload failure separately from a
host-enrollment failure.

### Maintenance intent changes the meaning of observed queue state

Admission must be denied before draining, and new slots must enter under that
same hold. Otherwise an independent provider scheduler can consume a slot
between registration and qualification. Qualification-only repository/workflow
access allows evidence collection while ordinary business dispatch remains
blocked. Release then reconciles only the operation's owned membership against
the current normal policy, preserving other maintenance decisions.

Job-level observation explains this sequence. A queued parent can have an
executing child; an idle runner under a verified hold can correctly leave jobs
unassigned. Neither a filtered workflow list nor the word "Ready" can decide
that the desired inventory is installed and qualified. Bind admission transitions
to the expected registration IDs and completed operation, then require actual
overlap for a concurrency claim.

## Emergent behavior

These relationships produce a contribution that can degrade honestly: native
work may remain available while Linux repairs; a paused host stays paused after
reconciliation; a new registration stays unqualified until tested; a broker
lease expiry denies new work even if a provider listener is still connected.
The system can explain missing capability rather than repeatedly reinstalling.

## Tensions and open questions

Sharing one managed WSL environment improves utilization but does not establish
isolation for unrelated untrusted attempts. Retained exports improve rollback
and enlarge disk/credential custody. Conservative partitions reduce contention
and can leave capacity unused. Policy needs explicit choices for these tensions,
including drain deadlines, force-stop semantics, evidence expiry and cleanup.

See [the enrollment synthesis](worker-onboarding-lessons-synthesis-donor-enrollment.md)
and [the overview](worker-onboarding-lessons-overview.md). Input release,
containment and independent result acceptance remain the existing trust gates;
operational green checks do not replace them.
