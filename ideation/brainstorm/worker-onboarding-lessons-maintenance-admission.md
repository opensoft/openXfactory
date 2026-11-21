# Maintenance Admission and Safe Fleet Expansion — Brainstorm

Status: brainstorm
Kind: process
Summary: Deny new dispatch before draining a worker, enroll added slots under that same hold, and restore normal routing only after scoped parallel qualification succeeds.
Topics: worker-onboarding-lessons, owner-controls, worker-readiness, ci-execution, worker-enrollment
Repository context: openXfactory owns neutral admission intent; omniWorker and each provider adapter must realize and verify the corresponding dispatch gate.
Captured: 2026-11-21

## Possible feats

- A durable maintenance state that blocks every configured work source while preserving an active job until it drains.
- Expansion that enrolls into quarantine, admits only a pinned qualification workflow, and restores the recorded route after independent checks.

## Focus

Adding registrations safely requires control of admission before changing the
host. An online listener may remain healthy while the owner deliberately denies
new work. Draining, stopping a service, cancelling a job and removing a provider
registration are separate operations with different effects and authority.

## Observed managed-host drain

During the CPC expansion, the owner requested a hold followed by three added
Linux slots. The existing Linux registration was moved from its normal private
organization group into a dedicated maintenance group. That group had selected
repository visibility and an empty repository-access list. Readback confirmed
the membership and denied access while the assigned job remained in progress.
The job subsequently passed and the runner became idle under the hold.

This is a verified admission/drain precedent for that managed GitHub estate.
It does not prove a general donor pause adapter or authorize applying the same
group policy to other workers. The native Windows/factory registrations were
outside this Linux-only maintenance operation.

Removing one custom label would leave broader selectors such as `self-hosted`
eligible. The useful invariant is a provider-enforced denial covering every
ordinary selector that could reach the held registration. GitHub's
[runner-group access controls](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access)
provide repository and workflow policy; an adapter must verify the effective
policy and membership rather than infer a hold from a group's name.

## Proposed expansion sequence

1. Record the precise owner scope, affected registration IDs, current group and
   route, active job and intended completion conditions. Keep unrelated factory,
   host and provider maintenance state outside this operation.
2. Deny new ordinary dispatch, verify that denial, and allow the current job to
   finish. Check both the provider job and local worker process before host
   mutation; an idle flag alone is a limited observation.
3. Enroll new registrations directly into the held group. Registration into a
   broadly eligible default group followed by a later move leaves a race in
   which queued business work can claim an unqualified slot.
4. After the complete expected inventory is online and idle, admit only the
   qualification repository and exact immutable workflow revision. Keep normal
   business dispatch denied while the parallel matrix executes.
5. Require success on the expected distinct runner IDs, expected identities and
   actual limits, with overlapping workspace execution. Four sequential green
   jobs are insufficient evidence of four-slot concurrency.
6. Recheck that the normal group policy still matches the recorded intent, then
   move only the owned registrations back to that route. Verify membership and
   close the hold receipt. Preserve the hold on an unmet gate.

Steps after the observed drain were prepared for the pilot; the added slots and
four-way qualification had not been executed at this documentation checkpoint.
The release plan retained the existing group and common Linux selectors, adding
unique slot labels only for diagnostics. It did not require business workflows
to adopt a new route or bypass their required checks.

## Recovery and authority boundaries

Persist phases such as held/draining, held/idle, enrolling, qualification-only,
qualified and released. Bind each transition to its operation, registration IDs
and source revision. An interrupted group update or partial release needs
readback and reconciliation; a controller exit is insufficient proof of the
provider's effective state.

Restore the operation's owned membership changes, not an old fleet-wide
snapshot over another operator's newer profile, policy or drain. Releasing the
expansion hold also must not revoke a distinct owner pause. Automatic release
is appropriate only within the owner's stated completion conditions; elapsed
time, successful registration or another project's queue pressure cannot
substitute for qualification.

For openXfactory, one host can have both direct GitHub and factory admission.
A GitHub group change gates only that route. A host-wide owner pause needs every
executor adapter and scheduler to acknowledge the appropriate scope before the
product reports a complete pause.

## Relationships and open questions

Connect [aggregate capacity](worker-onboarding-lessons-aggregate-capacity.md),
[job-state observation](worker-onboarding-lessons-job-observability.md),
[qualification](worker-onboarding-lessons-qualification-and-portability.md) and
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
Provider-specific drain acknowledgement, dispatch reservations, bounded drain
deadlines and partial-release recovery remain realization decisions.
