# Proposed internal composition and evidence boundary

Status: draft; factory-owned source proposal, not an executable schema/config/grant

## Compatibility

Preserve `openxfactory-dispatch-selection-internal-v2`,
`openxfactory-hosted-canonical-finalization-v2`,
`openxfactory-protected-runtime-internal-v1` and
`openxfactory-protected-runtime-report-internal-v1`. Legacy readers remain separate.
Runtime roles remain records/challenge/registry/custody/supervisor/worker_channel/
janitor. Source roles remain factory_profile/adapter/wallet_contracts/wallet_code/
worker/supervisor/caller_workflow/reusable_workflow. Inputs remain accepted_commit,
selection_digest, preauthorization_ref. No additional role, RunResource kind,
workflow input or field in a closed predecessor grammar is introduced.

The following are proposed factory-internal composition records outside those
profiles. Their source acceptance is separate from T013-S1 design acceptance.
No deployed value, resource ID, credential, approval or signing operation exists
by describing a field. Future source must provide a closed canonical parser and
reject extra/missing/duplicate/noncanonical fields, not merely prose labels.

## Deployment envelope

Proposed profile: `openxfactory-azure-deployment-envelope-internal-v1`.
One canonical UTF8 JSON envelope, <=16KiB, <=24 explicitly selected ephemeral
resource entries. An overly large complete candidate refuses; no hidden paging.

| Closed group | Required semantics |
| --- | --- |
| Identity | Exact profile, immutable deployment_ref, owner_scope_ref and namespace_ref; scope generation digest |
| Sources | Accepted composition/workflow source identity and build/image/source measurement references, existing eight source-role digest binding |
| Case | Exact case_ref and selected static-plan digest; full config/run/attempt are absent until independently assigned/finalized and then bound through a separately authenticated final-scope link |
| Target | Explicit tenant/subscription/region and exact approved parent/name allowlist; per-resource ARM ID, kind, provider incarnation, ownership and dependency refs |
| State | Independently initialized namespace identity/generation, receipt and retained-state references; no credentials or store contents |
| Lifecycle | Absolute approved start/end/expiry and exact temporary/retained dispositions, create-attempt and original provider-operation references |
| Authority | Exact independently authenticated selection/operation authority reference; envelope content alone is not a grant |

Actual source must distinguish pre-create reservation (approved parent/name only)
from admitted resource (actual provider incarnation/terminal create readback).
Do not put guessed IDs or placeholder hashes into an executable envelope. The
same deployment identity cannot acquire a new name generation or wider allowlist.
An opaque immutable final-scope link binds the existing static/full digests and
actual run/attempt/lease without modifying those existing closed profiles.

## Remote local-measurement envelope

Proposed profile: `openxfactory-azure-local-measurement-internal-v1`.
A directly authenticated bounded response, <=16KiB including complete canonical
configuration and policy documents; source may accept a narrower complete subset,
but cannot drop bytes or expand existing caps. Raw documents must be canonical and
unchanged through decoding/re-encoding. A response contains exactly: profile,
principal_ref, independent_observer_refs, deployment_ref, plan_digest, case_ref,
source_commit, run_id, run_attempt, launch_ref, host_ref, incarnation_ref, boot_id,
invocation_ref, pid, start_time, configuration, policy, observed_at, expires_at.
Principal/observer identities and trusted transport come from selected hosting,
not those response strings; current selection/readback must corroborate them.

The producer runs on the worker kernel, with protected local file roots and actual
ProcessLaunch, existing manager semantics and local lifecycle. A separate accepted
observer capability independently measures the same target. The control authority
checks complete bytes, unchanged templates and the only allowed late fields
against both authenticated observations, current phase/source/protection/state.
It grants no authority from a response field, copied digest or worker assertion.
It never constructs a pretend local ProcessLaunch for the remote PID.

Each observation/authority transport consumes its original budgeted capability
slot; nested I/O is accounted. No secondary unmetered body fetch or snapshot
replay is permitted. If full bytes or two independent observations cannot fit
accepted caps, that source candidate fails until a separately accepted amendment.
The wrapper confers no new neutral signing semantics or HSM/hostile-root claim.

## Infrastructure retirement receipt

Proposed profile: `openxfactory-azure-retirement-receipt-internal-v1`.
Closed canonical <=16KiB, <=24 result entries, separate from old protected report.
Fields: profile, deployment_ref, namespace_ref, owner_scope_ref, envelope_digest,
final_scope_ref, authority_ref, observer_ref, observed_at, expires_at, outcome,
resource_results, preservation_digest. Each result has exact arm_id/kind/
incarnation_ref/create_attempt_ref/retirement_operation_ref/state/readback_ref.
No token, request bearer, private URL query, key, provider payload or raw log.
Outcomes: incomplete, pending, indeterminate, failed, complete. Complete requires
all exact selected absences plus independent retained/shared preservation and
credential revocation; worker/proof success cannot override it. An authenticated
current origin and same scope are mandatory; digest possession is not provenance.

## Authoritative namespace outside the three hosts

Choose a dedicated authenticated namespace service with private Azure Blob state
in the watchdog RG, administered independently of control-host runtime. This is
separate infrastructure-generation state, not network SQLite or a replica/restore
of the retained POSIX runtime ledgers. Only this service holds Blob write
credentials. Provisioner and watchdog use bounded authenticated semantic operations;
they have no raw overwrite/delete or namespace-initialization capability.

Use create-only conditional blob writes for first permanent name reservation and
ETag-conditional transitions of the accepted resource record. Missing expected
blob/container/namespace identity refuses; no silent create/reset/backup restore.
Store terminal tombstones permanently with no runtime garbage collector. Loss or
ambiguity quarantines scope. A lease timeout never frees an old name or permits
an outstanding sender to regain authority. Actual Blob API/transport/identity and
initialization receipts need source verification and later setup readback.
This uses storage concurrency, not a conditional Azure VM delete. Compromised
privileged namespace/platform administrators and valid-backup rollback remain
outside the accepted trusted-admin guarantee.

## First-pilot per-kind disposition

All entries require permanent no-name-reuse and proven ordinary-writer exclusion.
A fresh GUID identifies a generation; it does not make deletion atomic. Supported
API-version readback and exact semantics must be qualified before setup acceptance.

| Kind | Explicit provider identity / documented API | Retirement dependencies |
| --- | --- | --- |
| VM | vmId; Compute2025-04-01 | Terminal creation and no pending writes; close admission; explicit Detach policies; exact VM only |
| Ephemeral OS disk | uniqueId; Compute2025-01-02 | Exact VM absent, attachment clear; retained data disks never included |
| NIC | resourceGuid; Network2026-01-01 | VM absent, no virtualMachine association; exact approved IP/subnet/NSG relationships |
| Public IP | resourceGuid; Network2026-01-01 | NIC absent, no foreign association; numeric address is not generation identity |
| VNet | resourceGuid; Network2026-01-01 | Selected NICs absent; only original approved subnets and no foreign attachment/peering/private-endpoint/delegation/service link |
| NSG | resourceGuid; Network2026-01-01 | Last; all NIC/subnet associations empty after selected VNet removal |

No standalone subnet DELETE. No RG deletion. No implicit cascade: verify explicit
Detach behavior for VM OS/data disks/NICs and NIC/public-IP dependencies so each
approved ephemeral resource can be checked separately and retained state survives.
Managed images, vault, retained disks/storage, watchdog/identity/state and evidence
are retained/excluded, and require later separately approved lifecycle disposition.
Unlisted kinds or missing own incarnation identity make the whole selection ineligible.

VM create-only If-None-Match support must not be extrapolated to every provider.
For any type without it, the sole-writer unused-path preflight plus permanent
namespace invariant is mandatory; lost create/update response still quarantines.
HTTP202/deletion submission is not completion. Poll/reconcile only original bounded
operation/readback; never blindly replay a mutation after response loss.

## Source/readback references

- [VM create/update2025-04-01](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/create-or-update?view=rest-compute-2025-04-01), [GET](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/get?view=rest-compute-2025-04-01), [DELETE](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/delete?view=rest-compute-2025-04-01).
- [Disk GET](https://learn.microsoft.com/en-us/rest/api/compute/disks/get?view=rest-compute-2025-01-02), [DELETE](https://learn.microsoft.com/en-us/rest/api/compute/disks/delete?view=rest-compute-2025-01-02).
- [NIC GET](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-interfaces/get?view=rest-virtualnetwork-2026-01-01), [DELETE](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-interfaces/delete?view=rest-virtualnetwork-2026-01-01).
- [Public IP GET](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get?view=rest-virtualnetwork-2026-01-01), [DELETE](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/delete?view=rest-virtualnetwork-2026-01-01).
- [VNet GET](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?view=rest-virtualnetwork-2026-01-01), [DELETE](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/delete?view=rest-virtualnetwork-2026-01-01).
- [NSG GET](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-security-groups/get?view=rest-virtualnetwork-2026-01-01), [DELETE](https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-security-groups/delete?view=rest-virtualnetwork-2026-01-01).
- [Explicit associated-resource deletion policy](https://learn.microsoft.com/en-us/azure/virtual-machines/delete), [RBAC additive permissions](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions).
- [Blob concurrency](https://learn.microsoft.com/en-us/azure/storage/blobs/concurrency-manage), [Put Blob](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob), [Functions timer](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer).
- [GitHub OIDC injection](https://docs.github.com/en/actions/reference/security/oidc), [runner source](https://github.com/actions/runner/blob/main/src/Runner.Worker/Handlers/ScriptHandler.cs).

Docs identify provider behavior, not a live capability test. Rendered API versions,
not a redirecting Learn view label, were used for the table. No provider mutation,
workload token or actual deployment is performed by this research/preparation.

Namespace key rule: validate a bounded ASCII ARM path with no query, fragment,
percent-encoded separators, empty/dot segments or trailing slash; derive a
case-folded Azure-resource key so case variants cannot reserve the same path
again. Keep the independently selected original provider ID for wire/readback
binding. This key rule does not normalize GitHub identities, signed claims or
any neutral/runtime source contract. Case-variant reservation attempts refuse.
Empty pilot RGs are retained administrative parents, not automatically deleted
by the bounded per-kind sweep; later parent retirement needs separate scope.
