# Protected runtime report source design

Status: draft
Kind: design
Owner: add-protected-runtime-report
Scope: proposed source decision; no implementation or operational grant

## Context

See [proposal](proposal.md). T012S source is accepted and landed; its 119 lifecycle
controls and all 2,017 native cases pass. Current runtime evidence has only
`source-conformance` and `isolated-fixture` scopes. The default CLI refuses before
operational binding selection. H10 currently anchors hosted budget controls;
H12 has no connected protected report implementation.

## Goals / Non-Goals

**Goals:** bind a later factual report to one independently authenticated operational
case, actual first run/attempt, immutable finalized configuration and generation,
actual issuance/proof barriers and fresh independent cleanup. Make source/fixture
substitution, copied pass labels and report/authority confusion fail closed.

**Non-Goals:** activation, provisioning, new services/roles, artifact upload or a
filesystem sink, neutral wallet/MFA contracts, operational grant issuance, human
MFA/approval, consumer acceptance, release qualification, HSM/non-exportability,
or recovery after loss of every selected control host.

## Decisions

### D1 — A separate internal profile with an authenticated provenance prerequisite

Propose `openxfactory-protected-runtime-report-internal-v1`, scope
`protected-machine`. Keep `openxfactory-runtime-evidence-internal-v1`, its two
scopes, case vocabulary, serialization and fixed false authority flags compatible.
Do not add protected scope or H-case slots to that existing profile.

Before constructing this new report, trusted hosting must independently establish
actual approved operational source/run/phase provenance, generation and issuance.
Selected authenticated provider/guest/issuer/control observations establish it;
a Python type, principal string, request body, `live=true` flag, copied deployment
manifest or self-issued digest does not. Absent provenance refuses report creation
with a fixed safe error. Golden encoder vectors are test artifacts only and have
no protected artifact publication or acceptance path. An actual fixture execution
continues to produce only honest source/fixture evidence.

Alternative: relabel the old profile or accept a caller-selected scope. Rejected
because it turns a source-test result into an operational assertion.

### D2 — Closed projection and eligibility

Proposed exact top-level keys:

`profile scope status started_at issued_at context phase_provenance_digest
 generation_digest issuance_digest proof cleanup results error_code
 protected_machine_qualified human_approval domain_effect consumer_dependency_lock`

The profile and scope are the literals above. Status is `passed`, `failed`,
`cancelled` or `incomplete`. Times are nonnegative integer epochs, with
`started_at <= issued_at`. All digests use the existing factory digest syntax.
No zero/placeholder digest substitutes for an unavailable required observation.
Unknown/duplicate keys, malformed types or canonical output over 16,384 bytes
refuse; no truncation or raw fallback is permitted.

`context` is the closed redacted historical selection projection with exactly:

`config_digest case_digest run_id run_attempt sources dependency_digest
 composition_digest protection_digest launch_digest services_digest authority_digest
 issuer_digest state_digest lifecycle_digest selection_checked_at selection_valid_until
 readback_digest readback_principal_digest readback_observed_at readback_valid_until`

The eight source roles remain `factory_profile`, `adapter`, `wallet_contracts`,
`wallet_code`, `worker`, `supervisor`, `caller_workflow`, `reusable_workflow`.
Each has exactly `repository_digest commit path_digest digest`. Recompute the
projection from validated selection and authenticated phase facts; a report never
reactivates that historical configuration or extends its use window.

`proof` is either `{status: not-performed}`, `{status: failed}`, or a verified
record containing exactly `status accepted_proof_digest verification_digest
replay_refusal_digest audience_barrier_digest environment_barrier_digest
worker_denial_digest`. Verified requires the actual owning verifier positive,
exact same-proof replay refusal, valid-signed audience-only and environment-only
negatives, plus an available worker-denial positive and its excess-permission
control. Audience/environment checks remain in the existing factory workload/context
verification path to that proof; they do not add GitHub-specific semantics or fields
to neutral wallet proof verification. An outage or invalid signature is not an equivalent negative. Source counterfactuals
validate the checker separately; they do not become live results. Never widen
production permissions to manufacture a counterfactual. Missing approved, safe
negative/disposable capabilities leave the affected live predicate unperformed.

`cleanup` is `{status: missing}`, `{status: unverified}`, or exactly
`status plan_digest scope_digest outcome observed_at checked_at valid_until
readback_digest readback_identity_digest attempt_digest`, with status `verified`.
Verified binds the same actual RunScope/RunPlan/generation and fresh independent
audit attempt, actual run-resource absence/revocation and original retained/shared
generations. For passed reports, cleanup observes after the latest actual operation/proof use
and `observed_at <= checked_at <= issued_at < valid_until`. Cleanup-derived and
report-privacy slots may be finalized after cleanup checking and before issuance;
those report-only observations grant no operation authority. Do not apply the old
v1 all-case timestamp floor to these later observations or change v1 behavior.

`results` has exactly the eleven existing semantic identifiers I01-I05, G01-G03,
S01, L01, R01; H01-H12; and live identifiers P01, deployed-G02, deployed-G03,
deployed-L01. Each slot is `{status: not-performed}` or exactly
`status observed_at artifact_digest`, with status `passed` or `failed`. An executed
slot is derived from independently checked, same-run facts, not a caller-supplied
pass/count value. Observation times fall within the actual operation history and
precede report issuance. These are semantic checks, not offline pytest counts.

`protected_machine_qualified` is true only for status `passed`, all 27 semantic/live
slots passed, verified complete proof barriers, authenticated operational provenance
and fresh verified successful cleanup. A failed case or safe failure error yields
`failed`; an actual cancellation yields `cancelled`; missing case/proof/cleanup
facts yield `incomplete`. Every non-passed status fixes qualification false.
Cancellation has precedence over other failure status. No successful cleanup can
upgrade a failed/cancelled operation. `human_approval`, `domain_effect` and
`consumer_dependency_lock` are always false. The report has no bearer authority
and is not a wallet possession proof, MFA receipt or approval grant.

`error_code` is null or one of `qualification-failed`, `qualification-cancelled`,
`qualification-incomplete`, `protected-report-refused`. Never serialize exception
text/args/notes/causes/tracebacks, request credentials, tokens, private keys,
raw challenges/proofs, service addresses, provider payloads or private paths.

Alternative: copy provider objects or synthesize a single success boolean.
Rejected because it loses independent provenance and leaks sensitive material.

### D3 — Compose the accepted run and cleanup; projection performs no I/O

Future trusted adapter bindings connect current admission/finalization and the
existing per-use RuntimeBinding to the owning verifier and fixed case validators.
Run the qualification operation once inside the accepted RunLifecycle. Capture
bounded observations, preserve cancellation and let that lifecycle perform its
existing success/failure/cancel cleanup. Consume its independently verified
cleanup result; report assembly does not invoke cleanup or repeat an operation.
After runner death, use only selected same-reference status/audit observations;
never a replacement launch or newest-run search.

Retain seven runtime service roles, eight source roles and three dispatch inputs.
The reporter adds no runtime role, network budget, authority deadline, journal kind,
state reset or endpoint discovery. Read budgets remain ordinary 3/13, protected
staging 26 total/private16, finalization six observations/18 protection/28 total
and private12, with the existing per-reader/non-GitHub caps. Same phase Decisions
and earliest expiries remain authoritative. Cleanup uses its original registered
cleanup_until/timeout. Pure report assembly uses historical authenticated facts
without acquiring new operation authority. If a complete positive cannot fit an
accepted allocation, stop for a separate factory amendment; never omit checks,
reset counters or extend a window.

Alternative: run pytest in the protected workflow, infer success from service
availability, or let report generation repair missing evidence. Rejected because
none executes and observes the approved operation.

### D4 — Privacy verification has no self-digest cycle

H12 measures the bounded redacted projection and independent privacy controls
before final report encoding. Its artifact digest covers those inputs/results,
not the final report bytes containing that digest. Final report content addressing
is external to the report; an unauthenticated hash is not provenance. No artifact
uploader, delivery endpoint or protected workflow change is introduced here.

### D5 — Source qualification and operational acceptance remain distinct

Isolated tests exercise real local TLS/process/custody/owning-verifier boundaries,
independent single-field mutations, cancellation/death and existing lifecycle
cleanup. They reject fixture-origin input at the protected emission boundary.
Pure encoder vectors may validate grammar but are explicitly not live receipts.
Keep all 2,017 baseline nodes/fingerprints/anchors; measure later new cases.
T012U broader source conformance, T012V handoff, T013 selection/authority, T014 live
qualification and T015 consumer delivery remain separate. No operator or human
acceptance is manufactured by artifact completion.

## Risks / Trade-offs

- Origin laundering through otherwise valid JSON -> require independently authenticated
  phase facts and exact scope; exercise copied source/fixture candidates as negatives.
- Replay/cancellation treated as arbitrary exceptions -> validate exact expected
  outcomes and preserve actual failure/cancellation through independent cleanup.
- Report issuance after a cleanup observation expires -> qualification remains
  incomplete/refused; no renewed operation or destructive cleanup retry.
- Exhausted/corrupt lifecycle journal -> preserve existing refusal, including the
  reserved clock slot and unchanged 2,048-event cap; no reset/repair/roll-back.
- Missing operational provider/crypto-negative/watchdog capability -> mark the
  corresponding live gate unperformed; isolated tests cannot select a substitute.

## Migration Plan

Review and ratify paired factory/adapter preparation heads before source realization.
Implement only after explicit isolated commissioning through feature017 tasks.
Existing source/fixture callers and default refusing CLI continue unchanged.
Operational binding/retention/transport and one-run cleanup authority require later
T013 decisions; actual protected emission requires T014 observations. Reverting
an unactivated source candidate leaves those defaults refusing. No deployment or
infrastructure rollback is commissioned by this packet.
