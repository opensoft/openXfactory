# Shared Host Admission for CI and Factory Work — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Admit Windows, Linux, direct GitHub and factory jobs against one host budget, with explicit coordination limits for independently scheduled runners.
Topics: worker-participation, aggregate-budget, ci-execution, worker-readiness, owner-controls
Repository context: openXfactory owns admission semantics; omniWorker enforces qualified host controls; workload adapters must participate in admission.
Captured: 2026-11-20

## Possible feats

- One accounted host budget across native Windows and Linux execution.
- Resource reservations that prevent separate work sources from spending the same capacity.
- Readiness and draining states that survive service restarts and owner pause.

## Focus

A physical or virtual host has execution environments and logical work slots.
Two GitHub runners plus two factory workers do not mean four independent
machines. A Windows host and its WSL workloads consume the same underlying
resources. CI concurrency must follow the combined workload demand and measured
host limits, not the count of registrations.

The existing [aggregate budget and owner controls](omni-unattended-worker-aggregate-budget-and-owner-controls.md)
already define the host-wide budget and distinguish enforceable limits from
measurements. This note applies that model to the newly explicit independent
GitHub and factory participation routes.

## Proposed admission behavior

Before a factory attempt starts, admission reserves capacity from the owner
allocation and obtains a scoped work lease. Execution binds that reservation to
an attempt and environment. Completion or confirmed termination releases it;
loss of a heartbeat alone does not prove that a process stopped consuming
resources. Recovery reconciles durable leases with live executors before
declaring capacity free.

Direct GitHub runners receive jobs from GitHub. A separate local agent cannot
claim to gate those jobs merely because it knows the host budget. Dynamic
sharing requires a qualified integration that controls when those runners can
accept work, or an execution boundary that reliably enforces their allocation.
Until then, conservative fixed partitions between direct GitHub and factory
work are a candidate first implementation. Uncontrolled runners count against
the host budget and prevent advertising that same capacity elsewhere.

For example, if a host is qualified for two comparable heavy jobs, allowing two
direct GitHub slots and two factory slots to start simultaneously overcommits
it. A partition of one admitted slot per route, or coordinated admission of two
total, respects that qualification. This is an illustrative policy, not a
benchmark or a concurrency promise for the CPC discussed in session.

## Lifecycle and failure behavior

Installed, enrolled, connected, capable, ready, busy, draining and paused are
different observations. A connected host with missing tools is not ready for
that workload. A revoked lease or owner pause prevents new work. Maintenance
must drain active jobs before a planned restart; the UI must explain any
owner-requested force cancellation separately.

Open decisions include first-release resource classes, enforcement mechanisms
per executor, direct GitHub coordination, cancellation deadlines and recovery
of uncertain attempts. See the [synthesis](worker-participation-synthesis-onboarding-and-dispatch.md)
for the relationship to enrollment and cross-factory allocation.
