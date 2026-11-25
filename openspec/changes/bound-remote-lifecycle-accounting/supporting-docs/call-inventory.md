# First-pilot remote lifecycle call inventory

Status: draft
Policy: `openxfactory-remote-lifecycle-accounting-internal-v1`
Policy file SHA-256: `fd198b7d7e8e786b5d5f64257ec0e276e881ea5364b265cb9ccb519208f77fa7`.

This is prospective source policy. [Measurements](measurements.json) are isolated
diagnostics at adapter75fc1feb3474, not P08 qualification. [Inputs](inventory-inputs.json)
freeze actual bytes; [the reproducer](derive-inventory.py) checks both hashes,
physical totals and the following formulas without network or project imports.

| Original operation | Parent requests | Nested credential requests | Complete private calls |
| --- | ---: | ---: | ---: |
| P05 observers and six fresh stage leases | 9 | 0 | 9 |
| Lifecycle prepare | 1 | N status observations | 1+N |
| Lifecycle independent ack-final | 1 | N status observations | 1+N |
| Lifecycle release-stage | 1 | 0 | 1 |
| Complete handoff | 12 | 2N | 12+2N |
| One original final cleanup | 1 | 4N: before-status, retirement request/confirmation, after-status | 1+4N |
| Independent cleanup audit | 1 | N status observations | 1+N |
| Cleanup plus audit | 2 | 5N | 2+5N |

File, retained/shared-file and process checks remain mandatory; their local
observations do not invent private RPCs. Credential checks cannot be omitted.
The existing PosixResources maximum is three credentials. The unrelated P07
infrastructure maximum of sixteen handles does not change that manifest.

| N | Handoff observed | Handoff proposed cap | Final cleanup observed | Cleanup proposed cap | Audit-only bound |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 14 | 14 | 7 | 7 | 2 |
| 2 | unmeasured | 16 | unmeasured | 12 | 3 |
| 3 | 18 | 18 | 17 | 17 | 4 |

Measured handoff times were approximately1.98s (N1) and2.19s (N3), using
GitHub12/protection12 and original two-member finalization. They do not
establish a worst-case timing guarantee. Final cleanup times were0.66s and1.20s.
Under unchanged private12, proper prepayment refuses before ack-final for N1,
before prepare for N3, at consumed12/attempted13. No takeover/release/proof occurs;
original nonce and Decision remain. Those refusal results, rather than a positive,
are the eligibility result. A caller-only12 diagnostic omits nested I/O and cannot
be treated as a valid complete positive.

Stage/unreleased fixture cleanup costs2+4N (observed6/14); the final cleanup
bound2+5N conservatively covers it. Known closed state uses one audit RPC
plus N observations (observed2/4), with no mutating resend. These fixture operations
are not an approved product policy or live cleanup qualification.

The fresh19-control run independently checked16 nonce databases,111 witness hashes,
retired issuance records and no unexpected processes after teardown. The prior
producer's issued-record audit failure remains unqualified. All nine owned test
containers are absent; no volumes were deleted and original benches are preserved.

Before dependent implementation: paired source acceptance, then repeat both gates
and prove the whole owning-proof path still fits unchanged qualification39 and
all original full/native tests, clocks, bytes and cleanup. This inventory supplies
no source ratification, operational permission or completion credit.
