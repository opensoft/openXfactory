# Proposed Azure composition for protected runtime qualification

Status: draft; P3 source decision unratified; no implementation or operational authority

## Context

See [proposal](proposal.md). Accepted planning inputs are adapter
`081dad41cfb42a3bc58aefe356bb6d424fab871d` and consumer
`049ede52b6ee03f15a57ecf7cdb9517002d8714f`, T013-S1 design basis only. Accepted
runtime code remains the #94/#95 lineage, not a deployed integration. This
amendment leaves all predecessor packets and neutral standards frozen.

## Goals / Non-Goals

Goals: define the smallest concrete source composition that can later be qualified
in isolation, then independently assessed for actual deployment. Resolve locality,
runner trust, managed images, state continuity and infrastructure generation safety
without replacing accepted proof semantics.

Non-goals: implementation now; actual appointments, resource creation, credential
issuance, OIDC discovery, setup/dispatch, provider write probes, consumer locks,
attended human assurance or resistance to malicious privileged administrators.

## Decisions

### D1: Explicit source selection preserves the existing refusal

Keep existing workflow.operational_bindings and its entrypoint unchanged. Propose
an additional deployment-specific builder and companion entrypoint called only by
a later explicitly reviewed source-selected workflow route. No environment flag,
file path, three-input value, JSON profile or plugin can choose/activate that code.
The future route retains the caller/local-reusable same-commit graph, three input
names, source/protection checks and phase-scoped job permissions. Its exact source
requires acceptance and operational grant before use. No workflow changes now.
A new manual dispatch input or broad default builder would widen the authority
surface and is rejected.

### D2: Trusted local helpers stay beside the kernel they measure

The control host owns the broker, authority/controller and control-host janitor.
The gate host owns records/challenge/registry/custody and trusted proof processing.
The worker host has two distinct layers: an untrusted workload UID, and protected
local measurement/launch/lifecycle helpers. Helpers are trusted services, not
workload capabilities; the workload cannot read their keys/policy, administer their
sockets, call privileged operations or reach IMDS/credential brokers. Host-root,
setup operators and subscription Owners remain explicitly trusted.

Existing measurement reads this host's /proc, boot ID and protected files and
requires an actual local ProcessLaunch. HostedLifecycle likewise binds the local
PID namespace, boot/scheduler and PosixResources. Execute these primitives locally;
do not build a fake ProcessLaunch from remote JSON or move the control janitor's
PosixResources onto another VM. Retain reference-posix-session-v1 semantics; a
systemd/cgroup replacement is a separate source decision.

Propose a closed authenticated internal remote-measurement envelope linking case,
accepted source/static plan, actual run/attempt, host/incarnation/boot, local launch
invocation/PID/start, independent observer identities and complete canonical final
configuration/policy bytes. The local finalization service uses unchanged local
measurement primitives with independently selected observation capabilities. The
control authority separately checks complete canonical bytes, allowed late-field
derivation, current source/protection/lease and independent authenticated observer
agreement before approving the existing full configuration/grant. It does not
pretend to read the remote kernel itself or accept a digest as byte derivation.
No authority/custody/GitHub App signing secret is placed in the workload.

This is a proposed new remote composition contract, not an existing remote API.
See [internal boundary](supporting-docs/composition-boundary.md). The existing
signed supervisor observation and owning proof retain their neutral shapes.
An unavailable/disagreeing local observer or foreign PID namespace refuses.

### D3: Realize compatible image and disk selections

Build/import an exact measured managed-image artifact from the S1 stable Canonical
base. The provider readback must select its actual image ID and build/source/digest
receipt; the marketplace URN is not passed as that ID. Image construction and its
storage are later bounded setup resources, not implied by this preparation.

Use one retained data disk on control and one on gate, no worker data disk. This
is within S1's at-most-five ceiling and existing reader's OS-plus-one-data-disk
limit. Separate private initialized store directories and permissions bind every
role's state. Preserve data disks on VM retirement; enforce explicit detach and
absence/preservation readback. A full layout requiring more disks needs separate
governance, not a widened reader hidden in setup configuration.

### D4: Runner endpoint capture has an explicit platform trust boundary

The selected companion entrypoint captures original GitHub-runner injected OIDC
URL/request bearer exactly once before worker/untrusted steps, after accepted
source/workflow checks. A bounded helper accepts canonical HTTPS443, an exact
preapproved GitHub-owned origin from trusted phase policy, bounded ASCII path/query,
and rejects userinfo, fragments, duplicate query keys, preset audience, redirects,
proxies and post-capture changes. It feeds the frozen URL to existing TokenClient.
Bearer material stays private memory and is omitted from worker environments,
files, logs and receipts; URL query material is not retained in evidence.

This trusts original GitHub-hosted runner injection plus accepted source; no
independent public REST readback of the exact endpoint is invented. Actual origin/
path policy is an operator-selected trust reference; unsupported shapes refuse,
never discover by minting a token. Fixed GitHub issuer/JWKS verification and
independent provider correlation must validate exact run/source/phase/audience
claims before any readiness. Captured URL metadata alone grants no identity.

### D5: Phase-limited issuance and retained state reuse accepted primitives

Use separate authenticated broker, reader, authority, supervisor, custody, local
helper and watchdog identities. Workload VM has no Azure assigned identity; any
trusted local helper has a separately provisioned private peer credential with
worker UID exclusion, not a VM-wide MI or delegated control credential. VM-root
is in the TCB. No broad existing App or shared bench credential is selected.
Bootstrap-purpose OIDC authenticates admission, not setup/dispatch/signing use;
protected proof has its own audience and full existing gate checks.

Initial host/issuer/CA enrollment needs selected out-of-band setup authority and
provider-correlated incarnation, source, role, nonce and public fingerprint. Neither
CSR fields, possession of a bootstrap key nor the same candidate's claimed role
can approve issuance. Only after independent effective-scope/expiry readback may
authenticated bounded role capabilities be used. Private retained POSIX journals
are explicitly initialized; no missing-store creation, reset or active-scope backup
restore. Credential retirement remains independently observed.

### D6: Separate infrastructure ownership from existing RunPlan

Existing RunPlan kinds remain process, credential and file. Azure VMs, NICs and
disks are not mislabeled as those kinds. Propose separate factory-owned closed reservation/provisioned deployment forms,
a later actual-run final-scope link and an infrastructure-retirement receipt.
Reservation forbids unavailable provider/static/run facts; provisioned records
actual setup facts; only the later link binds independently approved static/full
config, case and authenticated run/attempt/lease without a commitment cycle. Existing runtime
cleanup and protected report remain byte-compatible; the independent infrastructure
receipt is an additional owner acceptance artifact, not a new hidden report field.
Overall deployment qualification is incomplete unless both scopes pass. Process
cleanup cannot stand in for VM retirement, nor the converse.

### D7: Permanent no-name-reuse supplies the controller safety invariant

Azure VM Delete documents no generation precondition. Never claim ETag compare-
and-delete. Within the explicitly trusted privileged-administrator boundary,
require one admitted generation per ARM resource path for the lifetime of a retained
namespace. Persist a name reservation/tombstone and single creation attempt before
provider send; tombstones survive cancellation, retirement, restarts, closed cases
and evidence-retention expiry. A future case needs newly accepted unused names.

The selected sole provisioner is the only ordinary create/update writer. Independent
readback must examine additive/inherited privileges and exclude every workload,
control runtime, gate and watchdog principal from recreation or journal rewrites.
NotActions is not a deny. Trusted subscription Owners can defeat this premise;
this is explicitly outside the protection claim, never silently called isolation.
Use documented create-only preconditions where available, never assume them for
other resource kinds. No automatic send retry follows timeout/lost response.

Require authenticated terminal creation plus actual per-kind incarnation before
admission. Pending/ambiguous create or outstanding update quarantines the scope.
Before retirement, close write/run authority, persist retiring state and permanently
forbid replacement, then compare fresh identity to the retained manifest. Changed
identity, unproved writer exclusion or missing namespace state refuses mutation.
This is controller-composition fencing, not provider CAS; a GET followed by DELETE
is safe only under these independently established no-replacement premises.

### D8: Per-kind retirement is explicit, bounded and independently observed

Enumerate exact ephemeral resources and their provider incarnation/dependency
rules. VM uses authenticated vmId; each supporting type requires its own accepted
identity and lifecycle semantics, never inherited VM guarantees. Subnets retire
only with their selected parent VNet. Retained disks/stores, vault, watchdog,
evidence and unrelated/shared resources are excluded. No RG/wildcard delete,
automatic force-delete, silent adoption, resource-name reuse or broad Contributor
watchdog credential. Unsupported type/identity stays ineligible before setup.

The external Functions timer is outside all three hosts, administered separately
from control-host runtime, with durable private reconciliation state and a narrow
read/retire capability. A one-minute schedule is a proposal, not a deadline SLA or
provider fencing. Duplicate triggers consume one durable operation. HTTP202 only
acknowledges the original operation; independently observe terminal outcome and
absence/revocation/preservation. Lost responses stay pending/indeterminate and
reconcile that original identity/operation; no replacement grant or retry/reset.
If the control host is lost, retained namespace/receipts must be independently
available without mounting/resetting active POSIX databases as network SQLite.
The watchdog uses the independently hosted authoritative Blob-backed namespace
service in the [internal boundary](supporting-docs/composition-boundary.md), not
a copy/restore of a lost control-host POSIX ledger or an uncorroborated backup.
Create-only and ETag transitions serialize namespace state; these storage
preconditions do not supply Azure resource compare-and-delete.

### D9: Existing budgets, proofs and privacy remain bounds

Retain static-v2/hosted canonical-finalization-v2/full-runtime-v1, seven runtime
roles, eight source roles and three inputs. Ordinary GitHub aggregate13,
staging26/private16, finalization28/protection18/six observations, and qualification
private39 retain one original Decision and earliest wall/monotonic deadlines.
All existing per-reader/ARM/key/body/response caps remain. New composition calls
must occupy budgeted existing capability slots with every nested I/O charged;
no fresh child budget, hidden page or late upgrade. If a complete positive cannot
fit, refuse this implementation candidate and seek a separate factory amendment.
New remote envelopes and their contained canonical bytes have a proposed16KiB
cap. Existing per-reader caps remain unchanged (including larger bounded
observation/provider readers); this opt-in wrapper cannot increase those limits. Empty/digest-only substitutes are rejected.

Owning crypto, valid-preimage worker denial, one-use/replay reservations and fresh
protected full admission remain mandatory. No source/fixture report becomes a
protected origin by label, and no raw workload token, private key, credential,
provider payload or browser/factor material enters retained evidence.

## Risks / Trade-offs

- Common privileged administrators can bypass ordinary controls -> explicit TCB;
  missing owner acceptance/effective-access evidence blocks deployment.
- Permanent tombstones cost retained storage and cannot be reinitialized after
  30days -> independently priced/owned retention, no reset or automatic GC.
- Cross-host evidence adds authenticated interfaces and latency -> closed narrow
  source contract, local real measurements, independent complete-byte acceptance
  and unchanged budgets; no readiness if a positive cannot fit.
- Per-kind Azure behavior differs -> unsupported kinds refuse, separate identity/
  operation qualification, and no unsafe generic reaper.
- Source and setup change over time -> immutable candidate/source/build identities,
  coordinated source policy and fresh independent readback before later grants.

## Migration Plan

Preparation changes only governance/feature documents and owner acceptance records.
After exact P3 source acceptance and explicit isolated commission, realize proposed
feature017 tasks, qualify locally, review/publish source and obtain final source
acceptance. Deployment/activation stays separately gated. Then complete T013's
actual selections/pricing/window and seek P4 setup-only authority; read back P5
before any separately authorized P6/P7/P8 operation. No rollback command exists
now. Future rollback retires only exact approved generations and preserves retained
namespace/state; reverting source never restores consumed attempts.

## Deferred operational facts

Actual human confirmations/account ownership, effective writers/admin exclusions,
managed-image/builds, service/App/CA/credential IDs, OIDC origin policy, initialized
state and watchdog receipts, complete supporting-resource pricing, capacity,
network/CA/routing, exact final source and absolute UTC windows remain owner/operator
inputs. They are not unresolved algorithm defaults and cannot be fabricated to
make a document look executable. The P3 source model/negative controls are proposed;
no deployed capability is claimed.
