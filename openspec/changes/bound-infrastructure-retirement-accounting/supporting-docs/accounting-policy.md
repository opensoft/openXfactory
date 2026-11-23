# Proposed first-pilot infrastructure accounting policy

Status: source candidate; unratified; no product implementation or operational grant.
Policy identity: `openxfactory-infrastructure-retirement-accounting-internal-v1`.
This is a new factory-internal source selection, not an extension of ReadBudget,
a neutral contract, runtime/source role, workflow input or old receipt field.

## Selected graph and finite allocations

The [complete inventory](call-inventory.md) and [machine record](call-inventory.json)
select 14 ephemeral resources / 16 dependency edges for this pilot. Three separate
role NSGs explicitly refine the previously open S1 NSG count. No fourth VM, second
public IP, standalone subnet or extra disposable resource is selected. Any graph
change needs owner source review; the unchanged parser maximum24 is not permission
to add ten resources. Retain the two P3 data disks, measured image, vault, evidence/
watchdog infrastructure, all three RG parents and protected state.

All amounts below are maximum actual call attempts, charged before use:

| Pool | Private exchanges | ARM exchanges | Namespace backend calls | Registration/action journal calls | Complete application bytes |
| --- | ---: | ---: | ---: | ---: | ---: |
| Registration, including genuine later final-link registration | 128 | 0 | 128 | 32 | 1 MiB |
| One original cleanup execution | 768 | 160 | 512 | 128 | 12 MiB |
| One independently authorized observation/result execution | 192 | 48 | 128 | 32 | 3 MiB |
| Fixed whole-registration allocation | 1088 | 208 | 768 | 192 | 16 MiB |

No class or pool borrows unused allowance from another. Charges are for attempted
I/O, including failure, losing CAS, polling, uncertainty reloads, callbacks and
reconstruction. Registration/run-link transactions share the same original
registration pool; none of these limits is per resource, trigger or poll.
Private exchanges include real namespace/journal façade RPCs when present.
Their actual physical backend reads/writes are additionally charged in their
respective columns. A local pure method/cache hit is not an invented RPC;
hidden backend calls are never free. A backend roundtrip is charged once in its
own class, not relabeled ARM/private as a substitute for another exhausted class.

Existing per-message limits remain: complete closed envelopes/results <=16,384
bytes, provider reply body <=1 MiB and existing private transport/message caps.
The new byte pools count complete application request/response metadata and
payload, including backend state; they do not truncate bytes or claim a bound
on TLS/TCP overhead. Raw material is measured, not retained as a public trace:
journals/reports/errors retain only the existing permitted safe refs/counts/
digests and never tokens, keys, URLs, raw private state or exception canaries.

## Original authority and clocks

Registration transactions have one original <=30-second wall/monotonic interval
per genuine registration or later immutable final-link transaction, each clipped
to its actual approval. They use one fixed shared allocation; an error/retry does
not open another transaction or refund charges. A later run-link transaction is
permitted only when actual genuine P7 facts exist; never invent them at setup.
The original reservation/setup authority retains its accepted <=86,400-second
window and genuine separately approved UTC boundaries. No UTC window is selected.

At the first accepted cleanup trigger, consume the cleanup allocation once and
fix one original <=300-second wall/monotonic execution end, clipped to the
independently approved original absolute cleanup deadline. Every nested call,
resource and poll uses that same original cleanup clock/account. A per-call
timeout is <=10 seconds and <=remaining original interval/current source fence.
A new current fence can shorten a call, never extend the original cleanup end.
Existing setup-bound routes keep their current refusal and global clipping.
The additive cleanup route enforces current fencing at each send without using
successive fences to renew the original execution or original mutation authority.

The observation pool is separately selected by a current independently approved
read-only capability. Its one original execution is <=60 seconds and clipped to
that capability's exclusive expiry (still <=observed_at+60 in the old receipt).
Each call is <=10 seconds and original remaining time. Observation after original
cleanup expiry derives failed; it does not allocate a cleanup/proof Decision.
No automatic observation retry, extra permit or replenishment occurs. If the
one pool/capability is absent, spent or expired, emission refuses. A new separately
approved observation outside this policy would require its own explicit authority,
never an inferred rerun or renewal of the old proof/cleanup scope.

The existing proof/readback Decision default of10seconds, ordinary private12/
ARM24 and all other old phases/limits remain byte-identical. Only accepted new
source constructors may select this new infrastructure policy.

## Durable ownership without a recursive metering journal

Before ownership handoff or a first destructive send, the trusted external
registration service durably assigns the entire fixed maximum allocation to
one authenticated execution-owner incarnation. It uses a single original
conditional claim with non-reused ETag. Allocation is prepaid and never refunded.
Registration acknowledgement is forbidden before its durable claim; an ambiguous
claim/ack is not permission to resend. The provisioner retains its original
rollback obligation until actual acknowledged external ownership is established.

A live owner keeps exact before-call counters and byte counts for its prepaid
pool. Journal read/CAS/checkpoint calls themselves consume the journal pool;
they are not followed by recursively funded journal writes. Per-call accounting
is local under the original serialized owner; immutable operation/action evidence
is durable at the existing required boundaries. An unavailable journal stops the
next effect. No unbounded storage SDK retry/pagination/redirect occurs underneath
a single advertised call. Required nested work must be exposed to that same
meter or use a preassigned, disjoint, independently enforced slice of its pool.

A duplicate trigger can inspect only the original claim and cannot claim another
cleanup pool. Admit at most four trigger deliveries (one owner plus three duplicate
checks) under this policy; further delivery is refused before work. There are
at most three observations of each original creation operation and three of each
original deletion operation, charged to the same cleanup pool. A failed/uncertain
DELETE attempt is never resent; pending or ambiguous effects stay truthful.

This pilot deliberately does not implement transferable/restartable mutation
budgets. On loss of a pool's owning process/incarnation, its unused allocation is
burned; retained records never appoint a new mutator, recover a fresh timer or
refund unknown charges. Mutation continuation after that loss refuses. The
separately current independent observer can reconstruct original immutable
operations/namespace state and report an incomplete/indeterminate/late-failed
outcome using only its original observation pool. Loss of the control/gate/worker
does not lose the independently administered external owner. Loss of that owner
is an explicit fail-closed boundary, not a cleanup SLA or a success claim.
Supporting mutation transfer/restart would require another governed source change.

## Closed internal allocation evidence

These new internal records reside in the already selected protected external
registration/action store, not in old namespace records or runtime POSIX ledgers.
All are complete canonical UTF8 <=16KiB, reject duplicate/extra/missing fields and
use the existing Ref/Digest/Epoch bounds. Unknown future facts stay absent.

The immutable registration allocation anchor has exactly: `profile` (the literal
policy identity), `registration_ref`, `reservation_digest`,
`namespace_generation_ref`, `source_roles_digest`, `owner_scope_ref`,
`setup_cleanup_authority_ref`, `retained_scope_ref`, `policy_digest`,
`registration_owner_incarnation_ref`, `registration_allocation_ref`,
`cleanup_allocation_ref`, `observation_allocation_ref`, `not_after`.
The refs identify only the source-selected fixed pools above. They are not bearer
grants. policy_digest addresses the exact accepted policy; every identity matches
independently approved source/authority/current storage provenance. not_after is
clipped to the approved registration/setup scope. This registration-only not_after is not a cleanup expiry; historical anchor
matching after setup expiry still requires separately current original cleanup
authority. No run/link/incarnation of an
uncreated resource or chosen operational accepted_commit appears in this anchor.

The immutable cleanup claim has exactly `profile`, `anchor_digest`,
`allocation_ref`, `owner_incarnation_ref`, `trigger_ref`,
`cleanup_authority_ref`, `started_at`, `wall_end`, `clock_domain_ref`,
`monotonic_end_milliseconds`. profile is the policy identity with
`:cleanup-claim` suffix; end milliseconds is an integer1..9007199254740991 in
the selected local monotonic clock domain. Original cleanup authority remains
separately authenticated; labels cannot appoint it. The claim fixes the entire
cleanup allocation and its original clock once. Missing, ambiguous, rebound,
expired or differently owned claims refuse mutation.

The genuine run-binding addition is a separate immutable record with exactly
`profile`, `anchor_digest`, `provisioned_envelope_digest`,
`final_scope_ref`, `run_cleanup_authority_ref`; profile has `:run-binding`
suffix. It exists only after actual final-scope authority. The selected final
link supplies the original run/attempt/lease binding; this record cannot invent
or extend it. Setup receipts never require this addition.

A single conditional registration slot permanently names its anchor/owner; a
single conditional cleanup slot names its claim; immutable run/operation records
are append-only under their original refs. No record, allocation or resource
attempt is deleted, reset, replaced with a new owner, repaired from missing state
or restored from backup. Conditional status records may add genuine original
operation observations but cannot mutate these immutable bindings. Record parsing
and a digest alone do not establish service identity, current authority or storage
provenance. Observation ownership/consumption is likewise durably single-use in
its selected current authority record before its first read, not by adding fields
to an old retirement receipt. No private endpoint or runtime initializer is added.

## Gate that remains after source acceptance

The [call inventory](call-inventory.md) is a conservative source schedule, not a
measured new runtime positive. Its existing per-kind basis and complete synthetic
parser sizes are measured; new registration/facade/observer actions are proposed.
Exact paired source ratification makes this new policy eligible for isolated
implementation only. T013P07 remains unchecked until an actual complete selected
graph fits these unchanged proposed limits under authenticated ports, real clocks,
nested physical accounting and all original refusal/privacy/crash controls, prior
full/native qualification and independent cleanup. No cap can be raised or
observation omitted during that implementation to force a pass. If it fails,
retain the result and return through governance.
