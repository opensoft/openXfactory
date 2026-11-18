# Neutral private-connectivity binding

Status: draft

This is the proposed supported schema-v1 publication for the next authorized
contract cut. Its first bundle version/floor is a review candidate until the
release owner authorizes the actual cut and the next available version is
rechecked. An inventory preview is not a supported release.

The package has four canonical members: binding.schema.json, this README,
conformance.json and scripts/validate-private-connectivity.py. The schema ID is
https://xforge.us/schemas/openxfactory/private-connectivity/binding.schema.json.
Its schema_version remains 1. Publication adds schema identity metadata and
moves the reader to this supported path; binding validation semantics are
unchanged from the ratified optional neutral binding.

An absent or null private_connectivity binding preserves existing factory
behavior. An included binding must match installation, customer and environment.
The closed states are requested, approved, enrolled, ready, unready and revoked.
Customer-operated and managed modes remain independent choices; the neutral
record imposes no hosted subscription.

Approved/enrolled/ready declarations require current endpoint/network-bound
approval and the exact minimum access scope. Enrollment, effective policy,
separately approved routes and declaration verification remain separate.
Ready-shaped JSON is declaration conformance only. It proves no actual TLS
identity, reachability, enrollment, provider behavior or rollout acceptance.

The offline validator returns redacted finding codes. Use CPython with the
[hash-locked contract dependencies](../../requirements/hermes-runtime-contracts.lock),
including `jsonschema` and `rfc3339-validator` for binding timestamps.
Run it from a working directory containing the manifest:

    python3 scripts/validate-private-connectivity.py manifest.json

The `--now` UTC option supports deterministic conformance checks. Exit 0 means
declaration conformance. Exit 1 reports declaration findings. Exit 2 reports
invalid or unreadable input or unavailable RFC 3339 checking for a binding.
The CLI refuses duplicate fields, a symlink at the manifest path, and any path
that resolves outside the working directory.

Consumers select the actual published annotated bundle tag only after independent
tag/commit/inventory/schema/validator/corpus content verification. Copying these
four pinned members into a neutral consumer requires no feature-040 directory,
hosted product, provider SDK or domain runtime. Keep every member's raw-byte
digest and compatible schema version together. Existing pilot pins remain
historical evidence; supported consumer pin adoption is separately authorized.

The deterministic corpus contains synthetic examples only. Its expected findings
were frozen from the prior neutral reader, then checked against the proposed
supported reader. It includes positive optional/local/managed declarations and
refusals for identity, scope, expiry, routes, enrollment, policy and unsafe input.
Production source, staging qualification, canary results and commercial/expansion
decisions retain their own Q0-Q5 gates.
