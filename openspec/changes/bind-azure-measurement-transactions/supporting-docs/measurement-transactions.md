# Proposed direct measurement transaction grammar

Status: draft; factory-owned candidate, not accepted wire behavior.

## Compatibility basis

The exact accepted predecessor is add-protected-runtime-azure-composition at
c2dfbbcc6fa6965fcde18661bddca1dac7128d47, supporting-docs/composition-boundary.md.
Its local-measurement v1 field meanings, canonical complete-byte rules, selected
peer provenance, actual local manager/process/namespace semantics, independent
observers and original phase bounds remain mandatory. This document creates a
separate direct v2 transaction profile; it does not edit that predecessor.

## Direct response

profile is literal openxfactory-azure-local-measurement-internal-v2. The exact root
keys are profile, principal_ref, independent_observer_refs, deployment_ref,
plan_digest, case_ref, source_commit, run_id, run_attempt, launch_ref, host_ref,
incarnation_ref, boot_id, invocation_ref, pid, start_time, configuration, policy,
observed_at, expires_at, request_nonce. No other field or wrapper is accepted.
All fields except profile/request_nonce retain exactly the predecessor meanings
and constraints. request_nonce is exactly 64 lowercase ASCII hexadecimal characters
and must equal the nonce the selected caller generated for this authenticated read.

The complete canonical UTF8 JSON response, including both complete configuration
and policy documents and all metadata, is at most 16,384 bytes. Individual old
configuration/policy caps also remain. Duplicate/extra/missing fields, wrong types,
noncanonical raw bytes, malformed nonce, digest-only substitutes, split bodies,
paging, truncation and mismatched selected scope refuse. A partial response cannot
be upgraded to a verified capability by obtaining another unmetered body.

## Selected request

Use a dedicated source-selected mTLS POST /readback operation, not an added
ObservationClient operation. The canonical request is at most 4,096 bytes, with
exact root keys profile, operation, request_nonce, deployment_ref, plan_digest,
case_ref, source_commit, run_id, run_attempt, launch_ref, deadline,
remaining_milliseconds. profile is the v2 literal above and operation is measure.
Refs/digests/run/source use their existing selected-context grammars and must
match independently approved service scope; no request field selects a trust root,
peer, role, filesystem path, PID or observer policy. deadline is the original
caller's current integer epoch deadline. remaining_milliseconds is an integer
1..10,000 no greater than the original caller's measured remaining interval at
construction and actual send. Neither request field supplies a new grant.
The caller chooses a conservative fixed interval and checks that it still fits
its original remaining time after TLS readiness, immediately before GO/send.
It MUST refuse before sending when that fixed interval no longer fits; it MUST
NOT rewrite the request, increase the interval or retry with fresh authority.
Response expires_at is no later than the original request deadline and all
selected service/scope expiries. The original caller's monotonic end still
controls acceptance after receipt; the server's independent local timer cannot
extend it or authorize an effect after the caller has expired.

The trusted service authenticates actual selected peer credentials, effective
role/incarnation/source/fingerprint and separately approved scope/expiry before
consuming nonce state or observing the target. A valid worker request receives
explicit denial; malformed input or outage cannot stand in for that denial.
Nonce consumption precedes local measurement and cannot be reset after failure,
response loss or cancellation. The server uses an independently clipped local
timer for kernel/file/nonce-state work; it performs no hidden provider/admission
operation or new proof Decision. Missing initialized protected nonce state refuses.

The selected client consumes its original private read slot before the exchange,
freezes expected peer/material/scope, and rechecks original authority/clock bounds
at the existing TLS send checkpoint and after I/O. It verifies response nonce,
all selected identities/current scope, exact canonical complete body and expiry
before constructing a private verified byte/provenance capability. Each observer
has a distinct request nonce and independently selected credential/approval origin.

## Scope and qualification

These are internal factory composition semantics, not neutral wallet/MFA signing
or a public authenticator standard. Existing APIs, source/runtime role counts,
three inputs, old static/full/report profiles, ten-second original decision,
five-second TLS readiness bound, body/read limits and default refusal remain.
Complete remote finalization must demonstrate actual charges and independent
complete-byte derivation; failure to fit is ineligible, not an allowance to renew.
Exact paired source acceptance precedes dependent implementation. Isolated source
results do not establish deployed administration, enrollment, setup/dispatch,
attended human assurance or consumer058 T002 acceptance.
