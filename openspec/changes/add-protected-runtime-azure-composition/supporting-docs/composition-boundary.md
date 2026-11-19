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

The following deployment variants, final-scope link, remote-measurement and
retirement records are proposed factory-internal composition records outside those
profiles. Their source acceptance is separate from T013-S1 design acceptance.
No deployed value, resource ID, credential, approval or signing operation exists
by describing a field. Future source must provide a closed canonical parser and
reject extra/missing/duplicate/noncanonical fields, not merely prose labels.

## Deployment envelope

Proposed profile: `openxfactory-azure-deployment-envelope-internal-v1`.
Each immutable canonical UTF8 JSON document is <=16KiB with 1..24 ephemeral
resource entries. Unknown/missing/duplicate keys, noncanonical bytes and oversized
complete records refuse. The two forms below have exact field sets; an unavailable
fact is forbidden, never supplied as null, an empty string or a placeholder hash.
They are distinct immutable documents, not edits that release an existing reservation.

### Common types and exact field sets

`Ref` is an opaque independently resolved ASCII handle, 1..160 characters,
matching `[A-Za-z][A-Za-z0-9:._/-]{0,159}`; it is never an endpoint or approval by
itself. `Digest` is `sha256:` plus exactly64 lowercase hexadecimal characters.
`Epoch` is an integer UTC second in1..9007199254740991; booleans/floats refuse.
UUIDs are lowercase canonical8-4-4-4-12. Resource paths are bounded ASCII ARM paths
<=1024characters validated by the namespace-key rule below; wire spelling is frozen,
while uniqueness/order use the case-folded Azure key. No GitHub claim is normalized.

Both forms have these exact root keys:
`profile`, `phase`, `deployment_ref`, `owner_scope_ref`, `namespace_ref`,
`namespace_generation_ref`, `case_ref`, `source_roles_digest`, `build_recipe_ref`,
`target`, `resources`, `retained_scope_ref`, `window`, `setup_authority_ref`.
Every root key ending `_ref` uses Ref;
source_roles_digest is Digest over the independently selected existing eight-role
source record. No new role or adapter-defined source grammar is introduced.

`target` has exactly `tenant_id`, `subscription_id`, `region`, `parent_paths`:
the first two are UUIDs matching the accepted S1 QA scope, region is literal
`westus`, parent_paths is a case-fold-key-sorted unique array of1..8 approved ARM
parent paths. Prospective resource paths are planned names, not provider-assigned
incarnation identities or observations of existing resources.

`window` has exactly `not_before`, `not_after` (Epoch), with not_before<not_after
and span<=86400seconds, both inside actual separately approved setup authority.
This document creates no UTC window or authority. retained_scope_ref resolves the
independently approved preservation set; retained resources never appear in resources.
All source/build/owner/namespace/target/window/preservation/authority fields freeze
at reservation. Later source, target or scope changes require a new unused path
and separately accepted authority; no old name/attempt can be freed or reused.

### Reservation form before resource creation

phase is exactly `reservation`, with exactly the common root keys above.
Each resources entry has exactly `resource_path`, `kind`, `dependency_paths`,
`resource_policy_ref`, `create_attempt_ref`, `disposition`.
kind is one of vm/nic/os_disk/public_ip/vnet/nsg; disposition is literal ephemeral;
the two refs are Ref. dependency_paths is a unique sorted array of0..23 paths
from this same selected set, excluding self, forming an acyclic graph consistent
with the per-kind dependency table. Each path must match its kind's provider/type,
the exact target subscription and an approved parent by parsed full segments,
not a string prefix or URL alias. resources itself is strictly sorted and unique
by normalized Azure path; case variants and duplicate/extra/omitted approved paths
refuse. Its set must equal the independently approved temporary allowlist.
resource_policy_ref binds immutable independently selected image/network/disk
policy; it is not a worker-provided policy or a new permission grant.

Reservation deliberately has no static-plan digest, full configuration/policy,
run ID/attempt, provider incarnation, provider operation or creation readback.
Those facts do not yet exist. Each create_attempt_ref is durably consumed before
one provider send under setup-only authority, never reset after uncertainty.

### Provisioned form after actual setup readback

phase is exactly `provisioned`. Its root set is the common set plus exactly
`reservation_digest` (Digest) and `provisioning_readback_ref` (Ref).
Every common root field except phase/resources is identical to reservation.
Projecting each provisioned entry to its six reservation fields must exactly
reproduce reservation.resources, including order. Each resource adds exactly `incarnation_ref`,
`create_operation_ref`, `creation_readback_ref` (Ref). Provider IDs are resolved
from independently authenticated actual terminal creation/readback; a Ref does
not invent a VMvmId/diskuniqueId/networkresourceGuid or assert an operation completed.
For a synchronous create, create_operation_ref identifies the authenticated
original request/terminal-response receipt; it must not invent a provider LRO ID.
No selected resource may be missing, added, renamed, rebound to a different kind,
owner, dependency, policy or creation attempt. The reservation's digest and legal
namespace state must independently match before this form is admitted.

This form still forbids static-plan/full-config/run fields. It records actual P5
setup facts before the separately approved P6 static-v2 selection. Current provider/
protection/state checks remain required; historical creation receipts are not a
fresh runtime grant. Missing/pending/ambiguous creation leaves no provisioned form.

### Final-scope link after selection and actual-run assignment

Proposed profile: `openxfactory-azure-final-scope-link-internal-v1`.
Its exact root keys are `profile`, `final_scope_ref`, `deployment_ref`,
`provisioned_envelope_digest`, `selection_digest`, `configuration_digest`,
`policy_digest`, `case_ref`, `source_commit`, `run_id`, `run_attempt`, `lease_ref`,
`authority_ref`, `observed_at`, `expires_at`. It is canonical UTF8 JSON<=16KiB.
Refs use Ref; four digest fields use Digest; source_commit is40lowercase hex;
run_id matches `[1-9][0-9]{0,19}`, run_attempt is literal string`1`; times are Epoch
with observed_at<=now<expires_at<=observed_at+60 and no later than the original
Decision/authority/lease deadline. No renewal, new budget or inherited rerun grant.

Only after independent P6 static selection and authenticated P7 actual run/attempt/
complete-byte finalization may the authority issue this link. Its case/deployment/
sources/generation set must match the provisioned envelope and approved runtime
selection; all full digests and lease refer to those actual approved bytes/scope.
Neither envelope contains a backward link to this record. Static/full profiles
are unchanged and cannot be made to hash this later link, avoiding a commitment
cycle. The link adds no dispatch input, source role, RunPlan kind or old report field.
It confers no authority without the separately authenticated existing grant/lease.

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
Each closed canonical UTF8 document is <=16KiB with exactly one result per
reserved ephemeral resource, in reservation order (1..24). It is separate from
the old protected report. Missing/extra/duplicate targets refuse; raw provider
payloads, private URL queries, tokens, keys and logs are forbidden.

Both variants have exact root keys: `profile`, `phase`, `deployment_ref`,
`namespace_ref`, `owner_scope_ref`, `reservation_digest`, `authority_ref`,
`observer_ref`, `observation_authority_ref`, `observed_at`, `expires_at`, `outcome`, `resource_results`,
`preservation_digest`. Identity/authority/observer fields use Ref, digest fields
use Digest and times use Epoch with observed_at<=now<expires_at<=observed_at+60,
clipped to the independently selected current read-only observation authority,
not to an expired mutation grant. observation_authority_ref is that Ref;
authority_ref still identifies the original setup/run mutation authority.
Origin is independently authenticated; reference strings/digests are not
provenance or a new grant. A factual observation cannot renew mutation authority.

- **Setup variant:** phase is literal `setup`, with exactly the common keys.
  It covers partial setup, setup expiry/failure, predispatch abort and any cleanup
  before P7 final-scope issuance. It binds the original reservation and separately
  approved setup rollback/expiry authority, even if not all resources were created
  and no provisioned envelope exists. final_scope_ref, provisioned_envelope_digest,
  run IDs/full/static digests and guessed incarnation facts are forbidden.
- **Run variant:** phase is literal `run`; exact common keys plus
  `provisioned_envelope_digest` (Digest) and `final_scope_ref` (Ref). These bind
  the actual provisioned envelope and P7 link, original reservation and exact
  registered run/attempt/lease cleanup authority. Neither a rerun nor a new
  generation inherits it. Selecting a phase never supplies missing authority.

Each result has common exact keys `resource_path`, `kind`, `create_attempt_ref`,
`state`, `readback_ref`, matching the reserved path/kind/attempt. Ref/type rules
above apply. State selects these exact additional-key variants:

- `not-created`: no additional keys. The authenticated readback must establish
  that creation was never permitted/sent or the original request definitively
  terminated without effect. A missing response or bare404 cannot prove that
  an outstanding create will not take effect. No incarnation/LRO ID is invented.
- `absent`: exactly `incarnation_ref`, `retirement_operation_ref` (Ref) in addition.
  Independently observed actual incarnation and original retirement outcome must
  match. If already absent with no provider send required, retirement_operation_ref
  identifies the authenticated controller no-send/absence observation, not a
  fabricated provider LRO. No pending create/update or replacement is permitted.
- `pending`, `indeterminate` or `failed`: exactly `reason`, optionally followed by
  the known `incarnation_ref`, or by both known `incarnation_ref` and
  `retirement_operation_ref`. These are the only three allowed key sets; an
  operation ref without a known incarnation is forbidden. Unknown fields stay
  absent, never null. reason is one of creation-pending/creation-uncertain/
  retirement-pending/retirement-uncertain/readback-unavailable/identity-mismatch/
  authority-missing/dependency-mismatch. The referenced observation records the
  actual incomplete/refused check, not an asserted successful provider fact.

Outcome is derived: observing completion/failure after the original approved
cleanup deadline -> failed (even if resources are now absent); otherwise any
failed result -> failed; otherwise any indeterminate
result -> indeterminate; otherwise any pending result -> pending; otherwise
missing independent preservation/revocation evidence -> incomplete; otherwise
complete only if every exact reserved result is not-created/absent and all
retained/shared preservation and credential revocation checks pass. A missing
preservation observation cannot be replaced by a success digest; the fixed
Digest field identifies the actual incomplete observation projection in that case.
Worker/proof success never overrides an incomplete cleanup scope.

A current separately authorized read-only observer can therefore emit a fresh
failed/incomplete/indeterminate observation after mutation authority expires.
Such reporting uses only its bounded authenticated observation capability; it
cannot call admission, allocate a new cleanup/proof Decision, send retirement
mutations, renew a lease, reset consumed scope or trigger any retry. The old
proof/cleanup budgets and deadlines stay expired. If current observation authority
is absent, receipt emission refuses; the missing authenticated receipt visibly
fails qualification instead of being replaced by an invented failure origin.

Both phase variants preserve permanent namespace tombstones and consumed attempts.
Unknown creation effects remain quarantined, without deletion or resend solely to
obtain a complete receipt. No fresh signing use or workflow dispatch is authorized
by setup cleanup. Pre-run rollback and post-run cleanup have distinct scopes, but
neither requires fictitious facts from the other phase.

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

Docs identify provider behavior, not a live capability test. The table proposes
pinned request versions; Learn view selectors can redirect to a different rendered
version (the NIC link currently renders2026-03-01). Actual supported request
version/schema and each own incarnation field require authenticated readback
before deployment eligibility; no automatic version fallback is permitted.
No provider mutation, workload token or actual deployment is performed here.

Namespace key rule: validate a bounded ASCII ARM path with no query, fragment,
percent encoding, empty/dot segments or trailing slash; derive a
case-folded Azure-resource key so case variants cannot reserve the same path
again. Keep the independently selected original provider ID for wire/readback
binding. This key rule does not normalize GitHub identities, signed claims or
any neutral/runtime source contract. Case-variant reservation attempts refuse.
Empty pilot RGs are retained administrative parents, not automatically deleted
by the bounded per-kind sweep; later parent retirement needs separate scope.
