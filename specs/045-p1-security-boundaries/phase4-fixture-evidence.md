# Negative credential fixture qualification
Status: draft
Date: 2026-11-15

The original value first appears in 6cbb4495a2c08ce10c9bd4460f46cc0bda3c3a2d
(PR #235). Its issuance remains unknown. Historical feature prose, absent
matching alert metadata and a nonmatching built-in example do not prove it
never existed. No provider request, liveness check or rotation was attempted.

The current value is an explicit NOT_ISSUED marker. The exact expected failure
metadata is unchanged. Three new tests prove the same one credential-name
refusal, independent closed-world refusal, and that removing the forbidden
property removes this name finding. The unchanged full strict validator passes
14 positive examples and 41 negative confirmations across all nine requirements.

Exact membership and the published contract-v4.1 inventory exclude this example.
That does not exempt it from AGENTS.md's broader contracts/ rule. The original
membership-only no-cut interpretation was rejected in review before landing.
contract-v4.2 now records the nonbreaking marker through the required atomic
manifest/changelog/fixture/new-inventory candidate. Original tags/inventories,
the creation commit and all earlier receipts remain available. Validator/schema
bytes stay unchanged. Main/Sonar/tag acceptance remains pending and historical
credential issuance is still a separate uncertainty.

Final candidate qualification: the official supported-domain resolver read all
five frozen inventory entries from exact Git objects under deterministic
repository mappings, recomputed their stack digests and validated their
contract pins and conformance: five entries, zero findings. The unchanged
identity CLI again reported 14 positive examples, 41 negative confirmations,
nine of nine requirements, zero errors and warnings. The final focused run
covering fixture boundaries, privileged dependencies, OpenSpec and citation
adapters passed 289 tests; actionlint passed the changed approval workflow.
The prior 311-test run additionally included the wider execution module.
