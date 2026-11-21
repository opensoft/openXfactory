# Synthesis: Donor Enrollment Through a Local Host Manager — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compose a scoped donation invitation, separate identities, worker-owned WSL and transient grants into one recoverable onboarding journey.
Topics: worker-onboarding-lessons, worker-participation, donated-compute, worker-enrollment, synthesis
Repository context: openXfactory owns neutral relationships; OmniWorker-Install owns the local journey; the enrollment broker and workload adapters retain their authority.
Captured: 2026-11-21

## Possible feats

- One owner journey from a website invitation to a qualified contribution, with explicit evidence for every authority handoff.
- A managed-support path that can repair partial onboarding without making manual token exchange the public donation product.

## Members and their joints

Atomic members are [donor entry](worker-onboarding-lessons-donor-entry-and-registration.md),
[service identities](worker-onboarding-lessons-service-identities-and-tools.md),
[WSL ownership](worker-onboarding-lessons-wsl-ownership-and-startup.md),
[credential handoff](worker-onboarding-lessons-credential-handoff.md), and
[recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md).

### Intent becomes authority before it becomes execution

A website invitation expresses which contribution the owner intends. Platform
enrollment supplies renewable authority; optional GitHub registration supplies
a separate provider endpoint. Local privilege to create an account or enable
WSL is another explicit decision. None of those permissions should silently
stand in for the others.

The app should show this chain once, retain accepted choices, and continue
ordinary eligible work under standing consent. Adding a new eligible factory
does not require the owner to join that factory. Expanding data exposure,
workload class or resource allocation does require a new consent decision.

### Identity order determines whether the platform can honor that intent

The reconciler first establishes its execution owner and profile, then owns
the distribution and probes it in that context. This avoids an environment
that only the human desktop can start. Native Windows and optional Linux can
be independently ready; a failed Linux addition need not erase a valid native
contribution or mutate the owner's unrelated WSL/runtime settings.

### Transient grants meet a durable local state machine

The broker can issue a transient grant while the host retains durable,
non-secret progress evidence. A failed attempt must not require storing a PAT,
App administration key or reusable remote authority just to resume. Local OS
credential custody follows its own estate policy and is never inferred from
the registration-token lifetime.

The manual CPC setup's fixed helper and request-specific receipts demonstrate
a useful local seam. The product should own that seam rather than ask donors
to copy successive elevated shell programs. Support can request sanitized
phase/identity/error evidence without requesting credentials or whole exports.

### Dispatch connectivity and administration can mature independently

An outbound work channel can be qualified before private SSH management exists.
The UI should expose those as separate readiness facts, with a bounded owner
handoff if privileged repair is unavailable. It should not invent a VPN endpoint
or open inbound ports merely to make its installation story look complete.

## Emergent behavior and tensions

Together these pieces make onboarding resumable without broadening authority:
the owner can understand what was installed, which identity owns it, what data
and work it may accept, and which gate remains unqualified. Tensions remain
between managed delivery and unmanaged donation, passwordless identity support
and WSL profile needs, and convenient direct GitHub registration and the
volunteer credential boundary.

## Recombination and open questions

The existing [onboarding and dispatch synthesis](worker-participation-synthesis-onboarding-and-dispatch.md)
remains the participation model. The
[operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md)
adds the budget, recovery and acceptance loop. The invitation protocol, first
public-donation adapter, supported OS matrix and exact receipt contract still
need deliberate realization; this packet does not promote them into policy.
