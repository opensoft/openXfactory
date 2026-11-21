# Job-Level Observation and Conflicting Provider State — Brainstorm

Status: brainstorm
Kind: process
Summary: Correlate runner, workflow, job and local runtime evidence before diagnosing a worker, because workflow-list filters can omit a job that is actually executing.
Topics: worker-onboarding-lessons, observability, worker-readiness, ci-execution, owner-controls
Repository context: openXfactory owns neutral readiness evidence; provider adapters correlate provider records while the host manager supplies separately scoped local observations.
Captured: 2026-11-21

## Possible feats

- A job-aware readiness view that explains running, held, queued, draining and uncertain state with timestamps and evidence sources.
- Provider diagnostics that detect conflicting aggregate/job state without automatically restarting a worker or changing admission.

## Focus

A provider's online/busy flag does not name the executing job, show useful
progress, or explain why another job is waiting. Diagnosis needs the identity
and scope of each observation before an operator changes a service or releases
a hold.

## Observed false negative

In the managed CPC pilot, an organization-wide diagnostic queried workflows
with `status=in_progress` and inspected their jobs. It found no job assigned
to the runner even though the runner was online/busy. A direct read of a known
job then showed that job in progress on the expected runner, with its test-suite
step active. Fresh reads also showed the parent workflow as queued.

The narrower workflow-list filter had excluded the active job's parent. The
diagnostic was corrected to inspect queued parents as well. The job later
completed successfully. This records an observed provider-state combination;
it does not establish that every queued workflow contains active jobs or
identify the underlying cause of GitHub's aggregate state.

## Candidate observation procedure

| Evidence | What it supports | What remains uncertain |
|---|---|---|
| Organization runner record | Registration identity, online/busy report and labels | Assigned job identity, useful progress and local process health |
| Workflow record | Source revision, workflow identity and reported aggregate state | Every child job's actual state |
| Direct job record | Assigned runner ID/group, job state, active step and timing | Local subprocess progress between provider updates |
| Local service and process evidence | Effective account, task/service state and surviving worker processes | Independent provider acceptance or trustworthy results on a hostile donor |
| Admission/hold receipt | Owner scope, policy change and verified dispatch denial | Whether an already accepted job has finished |

For a known workload, query its exact job ID first and bind the response to the
repository, run/attempt, source revision and runner ID. Use fresh reads when
responses conflict and retain the observation times. Cache-control requests or
unique read parameters can help investigate freshness; they do not make a
multi-request scan atomic or make an API response independent attestation.

For discovery across repositories, inspect the relevant nonterminal parent
states, including queued parents, and paginate both runs and jobs. Reconcile
directly known jobs even when they do not appear in the filtered list. Report
an unmatched busy runner as uncertainty until that correlation has been done.
Changing filters improves coverage; it does not prove there are no other active
jobs outside the token's visible repositories or the scan window.

## Interpreting a queue during maintenance

The same pilot later placed the runner into an explicit expansion hold. Its
active job passed, the runner became idle, and normal jobs stayed queued with
no runner assigned. Those observations were consistent with the intended
admission policy. A queue that remains waiting under a recorded owner hold is
different evidence from a supposedly available worker failing to accept work.

Keep reported provider state, observed local state, owner intent and diagnostic
inference distinguishable. An active step can itself be slow or stuck; a direct
job assignment establishes assignment, not productive progress. Inspect local
diagnostics when that distinction is needed. Do not restart a runner, enroll
extra slots, remove a hold or change priority solely to reconcile a dashboard.

## Relationships and open questions

Use these observations with [maintenance admission](worker-onboarding-lessons-maintenance-admission.md),
[recoverable bootstrap](worker-onboarding-lessons-recoverable-bootstrap.md),
[qualification](worker-onboarding-lessons-qualification-and-portability.md) and
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
The provider adapter still needs an explicit freshness policy, visibility scope,
progress/stall criteria and escalation contract. Host-controlled evidence
cannot replace the independent result-acceptance gate for donated hardware.
