# Protected runtime hosting and issuance design

Status: draft
Kind: governance
Basis: accepted GitHub bootstrap source and adapter #66 handoff; T013 design recommendations only

## Context

See [proposal](proposal.md). Accepted source provides bounded crypto/transport,
correlation, full runtime admission, owning proof and fixture cleanup. It supplies
no operational resolver, issuer, guest agent or live qualifier. The portable
fixture launches and measures before recomputing its policy/configuration; that
order cannot be treated as an actual predispatch commitment.

`bootstrap.selection_document` removes only run ID/attempt. `launch.worker_configuration`
contains the final launch claims; `ProcessLaunch` composition also contains actual
PID/start time/argv/cwd. Policy digest depends on that composition. State/custody,
operation grant, scheduler and final cleanup scope then depend on full config digest.
The launch projection intentionally excludes its own hashes, so this is a temporal
binding problem, not an inherent hash fixed-point problem.

## Goals / Non-Goals

Make the remaining source integration implementable with truthful plan-only
preflight, protected staging, measured finalization, actual authenticated readback
and independent cleanup. Keep every existing proof/source/phase/one-use check.

Preparation implements no code or provider operation. Neutral proof/custody APIs,
frozen static-v1, existing source/fixture scopes, three inputs and seven runtime
roles do not change. No actor is appointed, SKU reserved, subject observed by token
mint, credential issued, source hold enabled, environment created or dispatch authorized.

## Decisions

### D1 — Versioned static plan, not unknown hashes in v1

Propose `openxfactory-dispatch-selection-internal-v2` and a separately typed hosted
bootstrap protocol. No v2 payload enters current v1 Approval/selection validators.
The closed plan contains configuration_template, policy_template, measurement_plan,
derivation_rules, staging_policy, hosting_selection_digest and source_hold_ref.
Its digest commits exact canonical bytes, immutable source/dependency/image/
executable/artifact and policy templates, scope/window, protected identity/protection,
all seven service identities/trust refs, initialized state and lifecycle handles.

Exactly four final configuration paths are late-bound: launch.run_id,
launch.run_attempt, composition_digest and authority.policy_digest. These paths
are absent, not null/sentinel/dummy values. All other fields are present, closed
and preapproved; handles are allocated before dispatch and bound/issued only under
later authority. A new need for dynamic handles/fields requires a versioned source
decision; there is no wildcard omission or general merge-patch escape.

Policy template excludes only its composition digest; policy claims retain the
existing static claim set and explicitly do not acquire run claims by inference.
Measurement plan fixes artifact digests, interpreter digest, immutable source,
approved image/install-root references, relative script/config/cwd locations,
privilege policy and deterministic worker-configuration projection. Runtime absolute
locations are resolved from independently selected roots, never committed host paths
or worker-selected interpolation. Derivation rules are a fixed versioned algorithm,
not an expression, plugin or worker-provided callback.

Finalization inserts independently corroborated run/attempt (attempt 1), builds the
existing non-self-referential launch projection, observes the actual controlled
process generation and composition, derives exact full policy bytes/digest, then
full runtime configuration bytes/digest. A separate current authority recomputes and
compares complete canonical plan-derived configuration/policy bytes before accepting
the final binding. It must not approve arbitrary digests supplied by the launcher.
The full runtime-v1 validator and unchanged owning proof verifier run afterward.

### D2 — Phase-limited preflight and protected launch

The hosted v2 phases are:

1. Independently approve the static v2 plan and hold/window, then durably reserve
   one dispatch attempt before the broker's one separately authorized request.
2. Authenticate/corroborate the assigned GitHub run using the accepted issuer,
   purpose/phase and fixed API facts. Read current plan/hold/protection and cleanup
   service capability. Return only plan readiness and the approved existing
   environment name. No worker starts and no full config/grant/proof-ready output
   exists in this read-only preflight.
3. After actual environment approval, repeat protected bootstrap identity, eligible
   original-human review, current source/hold/protection/authority checks. Independently
   authorize one staging launch. Register and durably acknowledge its cleanup lease
   before any start call; a JWT or environment approval alone cannot issue that grant.
4. Launch an inert measured process in the approved isolated slot, derive actual
   composition/policy/configuration and independently finalize them. The worker has
   no proof/signing or control-plane capability during staging.
5. Register a distinct immutable final full-config-bound RunPlan/lease/state scope;
   independently acknowledge takeover of the same measured generation. Only then
   release staging cleanup ownership and perform existing full admission/proof use.

PlanAdmission, StageLaunchGrant, StagingLease and FinalizationBinding are proposed
internal records with distinct closed purpose/version/phase. They cannot masquerade
as current BootstrapReadback, OperationReadback or an accepted machine receipt.
The new graph validator must admit only the explicitly versioned phase commands,
pins/order/permissions/guards; no permissive parser or extra OIDC worker job is added.
Exactly accepted_commit, selection_digest and preauthorization_ref remain dispatch
inputs. A trusted source-selected composition chooses v2; no environment boolean,
worker plugin or unchecked JSON flag activates production. Default CLI refusal stays.

### D3 — Staging ownership and crash safety

Bind staging registration to static plan digest, actual case/run/attempt/source,
current host resource/incarnation, service principal, immutable launch template,
preallocated nonreusable launch ref and earliest window. The selected host manager
owns a durable unit/cgroup slot and generation mapping before starting the child.
A worker-reported PID, bare unit name, tag or mutable directory is insufficient.

Use the host manager's authenticated generation/invocation plus actual PID/start/
boot/source facts. A crash after start but before PID persistence can still be
reconciled through that registered slot. Ambiguous registration/start responses
stay consumed/indeterminate: never create a replacement launch or reuse a ref.
Missing identity, changed generation or unsupported atomic ownership semantics
refuses and preserves the object for the independently authorized recovery owner.

Staging is a durably initiated background operation, not an unbounded readiness
callback. At most one start request is attempted. Lost acknowledgement permits
only authenticated status/reconciliation reads of the preallocated ref, never
resubmission. The proposed phase allows at most six read-only status decisions
within an absolute 60-second staging wait and the earlier case/grant/lease expiry;
each RPC retains its own at-most-ten-second bound and current authority checks.
No polling success renews or extends the stage. Timeout keeps cleanup ownership
and reports not-ready. Full admission is a new fresh bounded decision after final
binding; it does not reuse expired plan readiness.

Final promotion creates linked immutable records. Staging owns cleanup until both
final registration and independent readback acknowledge identical target/generation
and no later deadline; no gap, destructive overwrite or implicit lease extension.
Failures at any intermediate step leave staging janitor ownership live. Full plan,
state/custody grants, scheduler and receipt hashes all bind the actual config digest.

### D4 — Three hosts with an explicit administrator TCB

The design basis is three disposable Linux hosts: control (broker/controller and
control services), gate (proof gate and owning services), worker (unprivileged worker
and separately privileged supervisor). Selected kernel/service UIDs, private keys,
read-only image/artifact roots, cgroups and network policy require actual denial
readback. Host root, Azure administrators and trusted service code remain in the TCB.
No hostile-root, hypervisor attestation or in-memory model-behavior claim is made.

A VM managed identity is host-wide. Multiple assigned identities/client IDs do not
isolate cohosted processes. The worker host has no assigned identity. On trusted
hosts, only a privileged kernel-authenticated local credential broker may reach
IMDS/provider issuance; effective OS denial prevents other service/worker principals
from bypassing it. Where that cannot be proved, the deployment is ineligible or needs
another host/isolation design; merely naming different principals is insufficient.

Propose public-CA HTTPS 443 admission-only ingress on the control boundary so the
existing GitHub-hosted orchestration can reach it. Publish only intrinsic plan/
protected routes; broker dispatch, issuer/admin and guest-control routes stay private.
Require bounded token/API correlation before returning plan/config data. Internal
service/guest traffic uses selected mTLS identities and fixed endpoints. No shared
AKS, existing bench, peering, public SSH or new self-hosted runner is implied.
Actual DNS/certificate/network allocation remains a separate non-secret setup input.

### D5 — Credential issuance and software custody

Use separately selected repository-only GitHub App installations for broker Actions
write and reader Actions read; add Contents read only to the source reader where
required. Neither runtime App gets Contents write or administration. The original
human and eligible reviewers remain independent of the App actor.

Future controlled setup may import the GitHub-created App RSA key into a versioned
Key Vault RSA key. A trusted issuer constructs and verifies the RS256 App JWT with
that exact public key and exchanges it at the fixed installation endpoint for the
selected repo/permission subset. This is proposed API composition, not a tested
integration. Issuer platform identity gets selected-key sign only; import/admin
capabilities stay with setup. Tokens travel only over private channels, never worker
config/logs/evidence. Validate returned installation/repository/permissions/expiry.

GitHub installation tokens can outlive a 30-minute case. Separate current authority
bounds broker use but does not narrow a stolen bearer's provider scope. Plan actual
retirement/provider revocation and prevent further issuance; uncertain revocation
fails cleanup. MI group/RBAC changes are not claimed as instant token revocation.

Key Vault Keys has no native Ed25519 signing for the accepted owning service. The
pilot retains software Ed25519 custody on the trusted owning-service host; Key Vault
may store/deliver encrypted opaque secrets/certificates. No HSM/non-exportability
claim or proof-algorithm fork follows. A hardware-only requirement is an upstream
custody/backend decision, not a configuration switch.

Enrollment must bind actual host/incarnation, service UID, immutable source, nonce,
public fingerprint and requested role. An independently authenticated provider/
bootstrap channel corroborates them before issuance. CSR claims or an echoed
inventory document do not establish identity. Provider RunCommand/installation,
App/key creation and enrollment are future separately authorized setup writes.

### D6 — Current provenance for every callback

| Fact | Selected source behavior | Refusal boundary |
| --- | --- | --- |
| Plan/approval/hold | Authenticated operator/authority store plus fresh actual source/control reads | No request-body self-approval, signed echo or stale hold |
| Source/run/phase/review | Fixed GitHub repo/ref/blob/run/job/review APIs and verified signed claims | No response-URL fetch, newest run, rerun or originator self-review |
| Protection | Current environment and complete bounded branch-policy pages; exact reviewer/type/self-review/admin-bypass fields | No default false, omitted setting, wildcard or branch/tag confusion |
| Deployment | Selected Azure ARM VM/image/disk/NIC/identity/network resource/incarnation readback | Metadata alone does not establish guest policy |
| Guest measurement | Authenticated non-worker host agent reads actual process/artifact/UID/capability/key-file/IMDS/network facts | No worker self-report or generic RunCommand-as-read shortcut |
| Issuance | Selected issuer/Key Vault/App current key version, enrollment, effective scope and revocation | No own request echoed as observed issuance |
| State | Independent initialization receipt plus actual private filesystem/store identity and recovery scope | No missing-store creation/reset or active-scope rollback claim |
| Scheduler/cleanup | Durable registration, actual lease/generation and separate absence/revocation readback | No finally-only success, stale PID or cleanup writer self-attestation |

Current actual environment JSON exposed can_admins_bypass while the official schema
omits that property. Select a strict provider-specific projection requiring an
explicit boolean from authenticated current readback; missing/wrong type refuses.
Keep the observed-extension provenance and qualify actual false behavior only in
later authorized protected setup. Do not invent a GraphQL fallback or vendor guarantee.
Project branch-policy name main to refs/heads/main only with branch type proved;
reject tags, patterns, unsupported rules or additional permissive policies.

### D7 — Freshness, limits and independent cleanup

Preserve accepted fixed issuer/endpoints, TLS/no-redirect rules, canonical bounded
records, up-to-1-MiB API responses, 64-KiB internal envelopes/16-KiB full config,
first-attempt-only identity and 5/10-second transport bounds. The existing
ProviderReader run/job/review correlation retains its four-request/two-job-page
budget; that is not a global budget for newly added callbacks. New v2 separately
bounds protection to three reads (environment plus at most two policy pages and
32 entries), source/graph to four reads (main, two workflow blobs, final main)
and hold/control corroboration to two reads (at most 32 rules, one selected
control set). The aggregate maximum is 13 GitHub reads per decision. Every group
shares the SAME enclosing wall/monotonic deadline; no nested client resets it,
resets the correlation counter or omits current protection to fit a budget.
Unsupported pagination/control complexity refuses. Issuer/guest/ARM operations
also have fixed per-operation bounds under that same parent, not hidden retries. New clients share enclosing deadlines, recheck after
blocking work and propagate their earliest expiry back. No cache/retry or callback
label extends authority. Allocation/host scheduling remains a trusted-host limit.

The control-host janitor survives worker/gate/GitHub-runner loss, not total control
host loss. An independently administered external watchdog/scheduler and audit
capability outside all three hosts is REQUIRED before claiming automatic 24-hour
infrastructure expiry or control-host-loss cleanup. Source defines bounded authenticated
registration/reconciliation ports; actual service/identity/transport references remain
T013 inputs. If unavailable, setup/expiry acceptance stays blocked; there is no
hidden existing bench deployment or fourth VM/budget increase.

Keep existing process/file/credential RunPlan cleanup separate from infrastructure
retirement. The latter needs a separately scoped resource/generation allowlist and
supported conditional/provider semantics; a read-then-delete race or whole-resource-
group deletion cannot prove exact-generation safety. Unsupported retirement remains
operator-reconciled/incomplete, never a successful qualification or hard spend cap.
Preserve retained stores and redacted evidence; no reset or broad deletion occurs.

### D8 — Coordinated hold and staged authority

Use the recommended coordinated policy under trusted administrators: named owner,
case/source/window, exact current main SHA, scope of prohibited updates, independent
current control readback and revocation path. Provider ref/ruleset reads corroborate
facts; they cannot prove future administrator behavior or atomic pinning. A hold record
alone supplies no enforcement. If required control is absent/expired, refuse before
reservation/start/finalization/proof. No freeze/rule/tag/permission is changed now.

T013 must accept concrete non-secret target/actor/subject/issuer/store/scheduler and
budget/window inputs. Proposed bounds are one first-attempt machine proof, 30-minute
case, at most three small hosts and a 24-hour resource limit with a proposed spend
ceiling; capacity/pricing and actual UTC window remain unconfirmed. Budget alerts
are not resource stops. Source planning does not approve those operations.

## Risks / Trade-offs

- New v2 phase/finalization semantics are material source policy -> separate owner acceptance and explicit source commissioning before code; v1 untouched.
- Guest/process controls share host-root administrators -> disclose TCB, test actual worker denial, never claim malicious-root isolation.
- Complete protection uses an observed provider extension -> explicit typed field, fail closed on disappearance, require later live corroboration.
- External watchdog or generation-safe infrastructure retirement unavailable -> fail setup/expiry acceptance rather than assume automatic cleanup/cost enforcement.
- Cooperative main coordination can still race administrators/provider execution -> no atomic prevention claim; stricter guarantee needs upstream design.
- Proposed token signing/issuer integration and SKU/cost unknown -> isolated protocol/crypto tests and actual later readback before use, no capacity or HSM claim.

## Migration Plan

Source-only order: owner accepts this profile and commissions implementation;
feature 017 realizes/tests v2 and concrete hosting adapters behind an opt-in trusted
composition; publish and review exact source; obtain source acceptance; refresh
actual T013 selections and staged authority. Existing v1/default behavior stays
unchanged throughout. No live migration, activation, setup or dispatch happens now.
Rollback after a separately authorized future run disables the new composition,
retires only owned ephemeral credentials/resources and preserves consumed state;
no rewind/reset/consumer pin promotion is a rollback mechanism.

## Deferred operational inputs

Actual SKU/image/version/capacity/price, network/DNS/CA allocation, external watchdog
service, appointed principals, App installation/key IDs, host/store identities,
UTC window and conditional retirement support are known future T013/readback gates.
They are not missing technical defaults to guess. No executable config/grant is emitted.
