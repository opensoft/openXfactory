# Worker Registration Boundaries — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Separate openXfactory worker enrollment from GitHub runner registration, and treat CI as a workload available through either route.
Topics: worker-participation, worker-enrollment, ci-execution, github-runners
Repository context: openXfactory owns neutral participation contracts; omniWorker owns the host experience; factory integrations own workload dispatch.
Captured: 2026-11-20

## Possible feats

- Independent opt-in for factory work and direct GitHub Actions work.
- CI build and test work through enrolled xFactory workers.
- An onboarding view that distinguishes host enrollment from each runner registration.

## Focus

There are two independent relationships. A machine enrolls with the openXfactory
platform as a worker, while a logical GitHub Actions runner registers with a
GitHub repository, organization or enterprise. One host can support multiple
logical runners and worker execution slots. Their count does not establish the
host's safe concurrency.

| Owner choice | Participation | Dispatch authority |
|---|---|---|
| GitHub only | Authorized runner registrations | GitHub assigns Actions jobs within their configured scope |
| xFactory only | Platform worker enrollment and authorized capacity allocation | Factory work arrives through the governed dispatch path |
| Both | Both relationships, with separate status and credentials | Both paths share the host's admitted resource budget |

CI is a workload: checkout, build, test, package and return results. An xFactory
can request such work from its workers. Supporting CI does not by itself mean
interpreting arbitrary GitHub Actions YAML; workflow compatibility and check
publication need an explicit integration and scoped repository authority.

The owner should be able to enroll for factory work without manually joining a
GitHub organization or registering a runner there. An authorized integration
could still use ephemeral GitHub runners internally. That transport choice must
remain distinct from the owner's participation choice.

## Relationship to existing contracts

The [worker-enrollment contract](../../contracts/worker-enrollment/README.md)
already grants renewable leases, rather than permanent authority, and includes
GitHub runner groups, labels and transient registration grants. The
[Omni governed-dispatch synthesis](omni-unattended-worker-synthesis-governed-dispatch.md)
proposes GitHub-backed ephemeral execution and reuses clearing dispatch.

This supplement records an additional product requirement: platform enrollment
and direct GitHub participation are independently selectable. It does not claim
the current contract already provides a transport-neutral implementation, replace
its schemas, or select a second scheduler. Realization must decide which existing
lease fields generalize, which remain GitHub adapter details, and how factory CI
results bind to the requested revision and publish authorized checks.

## Boundaries and open questions

Runner credentials belong to the relevant registration; platform identity does
not imply repository access. A factory's request does not grant it machine
administration. Enrollment, GitHub registration, connectivity and execution
readiness need separately observable states.

Open decisions include the first factory CI execution adapter, its result
envelope, and whether the UI offers direct GitHub registration in its initial
release. See the [onboarding and dispatch synthesis](worker-participation-synthesis-onboarding-and-dispatch.md).
