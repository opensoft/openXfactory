# Donor Entry and Registration Choices — Brainstorm

Status: brainstorm
Kind: process
Summary: A donation entry point should establish owner intent, then enroll a qualified local worker through separately authorized platform and GitHub relationships.
Topics: worker-onboarding-lessons, donated-compute, worker-participation, workstation-intake, worker-enrollment
Repository context: openXfactory owns neutral participation seams; omniWorker in OmniWorker-Install owns the host experience; a sponsoring website owns its invitation.
Captured: 2026-11-21

## Possible feats

- A contribution button that hands a scoped invitation to omniWorker and reports enrollment progress.
- Separate platform-donation and direct-GitHub choices with an explicit credential and workload scope.

## Focus

Turn “donate my CPU” into an understandable owner journey without conflating a
website visit, installing an executor, joining a factory, and granting GitHub
runner access. This supplements the existing
[registration boundaries](worker-participation-registration-boundaries.md) and
[shared network pool](worker-participation-shared-network-pool.md).

## Proposed owner journey

1. A button on a sponsoring site, such as the proposed opensoft.dev entry,
   explains the recipient scope, workload classes, availability and resource
   costs. The website records intent and supplies an expiring invitation.
2. The owner opens or installs omniWorker. Native unattended build/test work
   needs a local executor; a website button alone does not create a Windows
   service, WSL distribution or GitHub runner. A browser-only compute adapter
   would be a different capability requiring its own qualification.
3. The app inventories before mutation and presents changes requiring local
   privilege, including optional WSL and any restart. The owner can decline
   Linux while retaining eligible native capabilities.
4. The owner chooses platform donation, authorized direct GitHub work, or both.
   Platform donation can cover all eligible xFactories under standing consent;
   it need not create a human membership in every factory.
5. The existing enrollment authority issues the applicable lease and transient
   grants. The host advertises only capabilities that passed execution and
   startup checks under their actual identities.
6. The owner can see ready, busy, draining, paused, repairing and withdrawn
   states and can change the contribution without opening an administrator
   terminal for routine operation.

This is proposed product behavior. No donation button, deployed global pool or
new enrollment endpoint was delivered by the CPC setup.

## Connectivity learned from the pilot

GitHub runners establish outbound HTTPS connections; inbound public addressing
is not a prerequisite for ordinary Actions dispatch. The
[GitHub runner reference](https://docs.github.com/en/actions/reference/runners/self-hosted-runners#communication)
describes that communication. The factory adapter likewise needs an explicitly
chosen outbound transport, authenticated polling or equivalent connection;
that transport remains a realization decision rather than an implemented API.

Private SSH administration is a separate capability. In the pilot, a planned
Headscale network did not provide a verified working endpoint, while GitHub CI
still worked. The app should report management connectivity independently of
work dispatch. Do not infer an operational VPN from a plan or expose a public
SSH listener merely to make job delivery work.

## Managed pilot versus public donation

The company-owned pilot used an approved organization runner group for private
CI. That is not a public-donor enrollment recipe. A volunteer-controlled host
can inspect its inputs and influence outputs. Reuse the existing
[credential-reach and contribution-repository design](omni-unattended-worker-credential-reach-and-contribution-repository.md),
[attempt grant](omni-unattended-worker-ephemeral-runner-attempt-grant.md) and
[three policy gates](omni-unattended-worker-three-policy-gates.md). Public
donation does not imply access to organization private repositories or secrets.

## Open questions and relationships

Invitation ownership, account linking, the first contribution adapter and a
browser-only capability are still design choices. The existing
[workstation-intake specification](../../openspec/specs/workstation-intake/spec.md)
retains its managed-intake requirements until a deliberate delta changes them.
See [the onboarding synthesis](worker-onboarding-lessons-synthesis-donor-enrollment.md)
for how consent, identities and qualification compose.
