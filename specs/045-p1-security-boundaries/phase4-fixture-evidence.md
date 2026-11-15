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
No manifest, changelog, inventory, historical tag or validator/schema is changed.
The original commit and all old evidence remain available. Main/Sonar acceptance
is pending and historical credential issuance remains a separate uncertainty.
