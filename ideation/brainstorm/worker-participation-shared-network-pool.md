# Shared Network Worker Participation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Let owners donate capacity once to the openXfactory network so eligible factories can request governed work without individual factory membership.
Topics: worker-participation, donated-compute, clearing-dispatch, consent, worker-enrollment
Repository context: openXfactory owns neutral participation and allocation contracts; runtime placement and domain integrations must be assigned during realization.
Captured: 2026-11-20

## Possible feats

- One platform enrollment for donation across eligible xFactories.
- Standing, revocable owner consent with explicit workload and resource limits.
- Capability and trust matching before an authorized factory receives a lease.

## Focus

Brett's requirement is that an owner can register with **openXfactory** to donate
CPU time, allowing all eligible xFactories to use that offered capacity. The
owner need not become a member or administrator of each factory. Platform
enrollment records the worker relationship; factory membership records a human
or organizational relationship and is a different concept.

Here, the shared pool is a logical allocation scope. The openXfactory repository
defines contracts and reference architecture; its existence does not establish
an operating global service. Realization must locate this scope within the
existing enrollment, clearing and dispatch responsibilities, rather than
creating an uncoordinated competing scheduler.

## Proposed participation controls

| Mode | Intended allocation | Decision status |
|---|---|---|
| Shared network | Any eligible factory may request the donated allocation | User-requested participation model |
| Selected factories | Allocation restricted to an owner-selected set | Design option, not a settled requirement |
| Mixed | A reserved allocation plus a shared donation allocation | Design option, not a settled requirement |

Standing consent covers eligible jobs within the accepted policy, without asking
the owner to approve each new factory or each ordinary job. Material expansion
of that consent requires a new approval. The scope includes accepted workload
classes, availability windows, CPU/memory/disk limits and any metered-resource
policy. Owner pause, withdrawal and policy expiry must affect dispatch and lease
renewal. A pause stops new admission; draining or immediate cancellation of
active work must have clearly stated semantics.

## Eligibility is an intersection

A factory request can use a worker only when factory authority, owner consent,
workload trust class, execution capability, current readiness and available
resources all permit it. A scoped, expiring lease binds the accepted attempt.
Factories submit requests and receive permitted results through governed
interfaces; they do not receive unrestricted host access.

Shared availability does not grant every factory private source, production
credentials or standing GitHub runner access. The existing
[Omni execution design](omni-unattended-worker-synthesis-sandboxed-execution.md)
separates release of inputs, containment of executing code and independent
acceptance of outputs. A donated host's administrator can inspect its inputs
and influence its results. Preserve those gates and the existing public-input,
no-secret volunteer baseline unless a separately authorized policy changes it.

## Open questions

Factory eligibility governance, fair allocation, abuse handling, accounting and
the runtime service owner still need decisions. New factories should qualify
through policy, not require ad hoc owner membership; removal of eligibility must
also propagate to outstanding leases. Neither a deployed shared pool nor a
cross-factory scheduling implementation is asserted here.

See [shared host admission](worker-participation-shared-host-admission.md) for
the physical limit that applies across all allocation modes and work sources.
