# P07 eligibility observations

Date: 2026-11-23, America/La_Paz
Adapter source: `33b2502818fbf86d4b33e700fd61cb1c717b6886`
Status: diagnostic; full first-pilot positive absent; no product source change.

[Machine record](eligibility.json) preserves both gates and the measured refusal.
Six external diagnostic tests pass in 5.06 seconds against unchanged accepted
provider/namespace fixtures. Original old per-kind retirement and historical
creation controls still pass.

| Gate | Actual observation | Consequence |
| --- | --- | --- |
| Setup expiry / cleanup scope | Existing provider and namespace paths refuse after setup expiry, with zero new delete, provider GET or namespace mutation | Additive selected cleanup/read-only observation paths are still needed; old refusal is correct |
| Whole-registration budget | Same original Decision and Provider/cache complete VM at private9/ARM3; OS-disk observation refuses at private12/ARM5; five generations remain admitted | No complete-graph fit; stop dependent code and prepare governed policy |
| Nested state I/O | 32 actual namespace port calls observed independently in that partial trace; absent from ReadBudget | A cap-only increase is insufficient; actual state calls need explicit accounting |
| Late result grammar | Existing pure closed-grammar late failure control passes | Does not qualify authenticated service origin or a live read-only observer |

Separate old per-resource controls total 60 private, 24 ARM and 96 namespace
calls. They use distinct Decisions; that sum is not the same-decision whole graph,
not full S1, and not a proposed cap. Registration, independent observers and
recovery remain to be measured.

The initial real-clock diagnostic attempt hit the unchanged fixture's eager
timeout assertion before the intended boundary. That attempt is retained as a
fixture diagnostic, not a product failure/success. The final probes use the
original frozen wall/monotonic model only for scope/counter checks. They make no
elapsed-deadline claim.

Independent read-only SQLite audit checks all 24 synthetic stores. The partial
whole-graph store confirms one actual fake-provider DELETE, VM tombstoned,
five admitted generations and the excluded image preserved. No extra provider
send completed the graph after exhaustion. Original stores were archived and
verified by hash before their four owned working roots were removed. Archive
SHA256: `6a750b38f6f8a08be433ac5363b97cf441e4bef1bd0715d61af80ecc0dc20419`.
This is fixture filesystem teardown, not infrastructure/runtime cleanup success.
No P07 containers or volumes were created.

P07 product/test/matrix source and pinned dependencies remain unchanged.
No full/native runtime rerun, hosted P07 CI, local panel, source acceptance or
operational qualification is claimed. Setup/dispatch unauthorized; feedback
deferred; blocked writes unreplayed.

## Preparation validation

All six offline adapter preparation gates pass: contract pin, neutral-root/code
pin, syntax, plain, strict and pinned OpenSpec whole-corpus validation. Factory
code-surface, sequenced-after sweep and pinned OpenSpec candidate validation also
pass. Feature prerequisites resolve this same feature. These checks validate this
documentation handoff; they do not supply the failed full-graph runtime positive.
