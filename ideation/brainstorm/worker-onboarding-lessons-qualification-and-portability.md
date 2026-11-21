# Capability Qualification and CI Portability — Brainstorm

Status: brainstorm
Kind: process
Summary: Advertise workload readiness only after identity-specific execution, resource enforcement, workflow portability and separately recorded reboot acceptance have passed.
Topics: worker-onboarding-lessons, worker-readiness, ci-execution, executor-ladder, donated-compute
Repository context: openXfactory owns neutral capability and evidence semantics; host implementers and workload adapters produce distinct qualification evidence.
Captured: 2026-11-21

## Possible feats

- Capability receipts that bind an executor, workload profile and source revision to specific acceptance gates.
- A concurrency and unattended-reboot test that prevents registration count or session-0 launch being reported as full readiness.

## Focus

Installed, registered, online, capable, idle, qualified and admitted are separate
claims. The pilot repeatedly demonstrated that success at one gate did not
establish the next. Capability discovery should report the missing gate and
evidence freshness rather than one broad green status.

## Candidate acceptance matrix

| Gate | Evidence to check | Insufficient substitute |
|---|---|---|
| Identity and profile | Effective Windows SID, loaded profile and Linux UID/GID | Desktop account name or successful administrator install |
| Provider enrollment | Actual runner ID, group, labels and current provider status | A local registration file alone |
| Runtime | Exact OS/architecture and workload toolchain under the executor | Installed WSL, a virtual adapter or one `--version` command |
| Limits | Actual cgroup/job/VM enforcement and parent budget | Declared configuration text or a UI slider |
| Workload | Private/public-input route as authorized, pinned source checkout, build/test and result checks | An online listener or a trivial shell command |
| Concurrency | Jobs overlapping on distinct expected runner IDs within shared limits | Four registrations or four sequential successes |
| Reboot | New Windows boot identity, fresh owner evidence and a job before desktop reconnect | RDP disconnect survival, session 0 or a pre-reboot receipt |
| Recovery and withdrawal | Negative tests, drain, revoke and owned cleanup behavior | Re-running an installer until it exits zero |

Capability changes can invalidate earlier evidence: service-account changes,
new tool versions, policy, OS/WSL updates, resource limits, shared placement and
workflow assumptions should have explicit requalification rules.

## Toolchain and routing lessons

The Linux smoke passed under the non-root service account with private checkout,
Python execution, separate workspace access and actual resource limits. A later
full platform-validation job exposed a deeper portability seam: clean-environment
subprocesses could not use a Python build whose normal invocation depended on a
loader environment variable. The accepted job-local correction preserved the
environment-isolation tests and shared tool cache. Preserve the tests that
reveal a host difference rather than weakening their assertion to get a pass.

Pinned utilities installed into a private job directory avoided sudo and global
host mutations. Tool installers, caches and executable lookup must support each
service account independently, especially when adding more slots.

Routing also lives in the workflow source. The qualified example selected a
different runner group/label set and enabled a compatibility step only for one
pull request. Rerunning an old queued job or advancing main did not broaden
that branch's selection. If another head is authorized to use the same profile,
update all related conditions together while preserving validation, permissions,
timeouts, exact-source checks and review. Matching labels do not establish a
Docker engine, a different Ubuntu version or workload qualification.

## Dated evidence and limits of inference

The 2026-11-21 checkpoint established one migrated Linux runner under a dedicated
Windows owner in session 0. A private smoke job passed identity, checkout,
workspace and two-CPU/8-GiB cgroup checks. The full platform suite then passed
for its qualified PR head in about 27 minutes. Another compatibility head
failed in its test-suite step; a successful host precedent does not make other
source revisions green or diagnose every failure as infrastructure.

Three additional Linux slots were prepared but not reported enrolled; their
four-slot concurrency test and the no-sign-in reboot test remained pending.
These are checkpoint facts, not a live fleet inventory or a global donor trust
qualification. Sanitized private receipts and organization CI runs remain with
the operator; do not publish credentials, machine SIDs, copied home data or
complete filesystem exports to make a brainstorm look evidenced.

## Relationships and open questions

See [identity-specific tools](worker-onboarding-lessons-service-identities-and-tools.md),
[WSL startup](worker-onboarding-lessons-wsl-ownership-and-startup.md),
[capacity](worker-onboarding-lessons-aggregate-capacity.md) and
[the operations synthesis](worker-onboarding-lessons-synthesis-operation-and-acceptance.md).
Receipt format, expiry, independent acceptance and the first supported OS/build
matrix still need realization. Host success does not replace the existing
volunteer input-release, containment and output-acceptance gates.
