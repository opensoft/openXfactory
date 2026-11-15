# Authentication review: T020 package source after coordinator landing

Status: draft

## Exact T020 source-only review target

Brett is the accepted Headscale package source/release owner and source-evidence custodian. Review the actual new private output and its human/source provenance in this exact control. Existing owner, support-candidate and custody approvals establish scope; they do not authenticate this new observation.

| Item | Immutable review identity |
| --- | --- |
| Proposed reviewed manifest | Pending the following immutable control commit; this preparation is not an authentication target. |
| Manifest file SHA-256 | Not yet bound |
| Canonical content SHA-256 for authentication | Not yet bound |
| Complete frozen definition | c37f19af3ebe6340ce417286d54875f40a201f86e41d22077b676044f7f44431 |
| Actual tested package source | [9e94411f89](https://github.com/opensoft/Headscale-Install/commit/9e94411f893836550b481085f0ef628f4b14b99b) |
| Actual source baseline | 11bd61fe665cf40f2bbf02980c512475329b3151 |
| Actual private original output | [001ca79a7f](https://github.com/opensoft/headscale-install/blob/001ca79a7f523fb8d063e73f83e22c5b4b609fac/evidence/private-connectivity-production/T020.json) |
| Original output file SHA-256 | f0c2f641111e52ed7a8f385935bfc785c8c2b9060082999bc7999ca062fe7cf6 |
| Distinct private T020 receipt | [9b4c610663](https://github.com/opensoft/headscale-install/blob/9b4c6106633d5d28b777ef00f1d9bd695588efcf/evidence/private-connectivity-production/T020.json) |
| Receipt file SHA-256 | ee242a31569d4c10726a0007c99ed19526824988325b45ee8e08d1aa8cef31c7 |
| Corrected consumed T010 | [d577589ff0](https://github.com/opensoft/openxfactory/blob/d577589ff0e4796c269b977c2195a1be17a7e2d3/specs/043-private-connectivity-production/evidence/T010.json) |
| Unchanged consumed T011 | [2438f54b65](https://github.com/opensoft/openxfactory/blob/2438f54b65e43837a33e3c0f3aff7dbbd4ba0cb4/specs/043-private-connectivity-production/evidence/T011.json) |
| Actual owner source CI | [qualification run/job](https://github.com/opensoft/Headscale-Install/actions/runs/43743171210/job/132900583919) |

## Actual new output and source checks

The fresh approved source collector ran from 2026-11-15T17:47:47.816127+00:00 through 2026-11-15T17:47:48.857637+00:00 at the exact unchanged repaired code above, after #1310 merged and all actual post-merge checks passed. Its exit code was 0. It passed make validate, all 45 source tests including 19 package regressions with zero skips, helper CLI help, locked upstream/input/helper metadata and exact-scope checks. All 26 original lab paths and both pilot hashes were unchanged. The closed three-case expectations and exact collector command are in the T020 binding; actual stdout, observed facts, timings and raw/export SHA-256 are preserved in the private original output.

The output was freshly generated, not copied from an old pass. The raw command-output SHA-256 is e10e20fbf9d7ecde635aeaf15f4309b070b2d57c34e62f8a4a10884ba4289197. The private receipt references that distinct output; it does not contain its own commit hash. Full default T010 and T011 verification passed against the accepted main control before this separate source collection. Their exact immutable dependencies are recorded in the private receipt and original dependency-preflight record.

Owner qualification passed at receipt head 9b4c6106633d5d28b777ef00f1d9bd695588efcf. Only the listed T020 evidence file differs from tested source 9e94411f89 at that head; all nine source/governance artifact hashes were compared and are unchanged. This is source/fixture CI, not intended-platform qualification.

## Landing and private-proof prerequisites

[Coordinator PR #1310](https://github.com/opensoft/openXfactory/pull/1310) landed source-only as 6e2f829b16275827a0b73308623164fa099a7ae9 after all reviewed-head checks and Codex review cleared. The standing author-owned approval override was used because the requested independent approval had not arrived; no independent approval is invented. The actual merge has the reviewed tree and expected two parents.

Its [actual root/Sonar run](https://github.com/opensoft/openXfactory/actions/runs/43738051687) and [Python 3.14 run](https://github.com/opensoft/openXfactory/actions/runs/43738051656) both passed. All eight actual merge-commit checks, including SonarCloud, succeeded. Trusted-base readback preserved accepted core c8be9c1d56f7fd7dbbaca5ca4c3f416ae03f7e1855722fb4aa0e54e5a6f3ef54 and default T010/T011/T012/T016. The authenticated source-CI producer remains the independently accepted 94caf6717ece69af66dfde121bf4b868a6c3abdf.

This is the first actual foreign binding in the coordinator control. Before presenting this packet for authentication, both existing coordinator CI lanes must prove the required private commit presence through that trusted-base producer and the existing repository-scoped read-only App, then revoke tokens before tests and remove ephemeral proof. The exact packet PR's checks and review comment record those actual run/job results. Local full-owner checks and locally derived commit-only metadata cannot substitute for that live transport qualification.

No private source, commit objects/headers or raw output is copied into coordinator Git. The E-only source_container is unchanged. The coordinator retains the typed private references, closed binding expectations and exact owner-resolved inventory; full source/output verification uses the actual private owner Git store separately.

## Human authority, preservation and custody

The [accepted source authority](https://github.com/opensoft/openXfactory/blob/cd13fe4bc03a050d3ad2169b3795e05a3a8bf24d/openspec/changes/commission-headscale-production/review/source-owner-permission.json) and [ratified package design](https://github.com/opensoft/openXfactory/blob/6e2f829b16275827a0b73308623164fa099a7ae9/openspec/changes/commission-headscale-production/design.md) name Brett, the exact four T020 files, required source role, approved source scope and until-superseded source-only lifetime. Existing actual role/matrix/private-source-Git custody decisions remain authoritative. No new source or live authority is inferred from the new output.

The original 43-test candidate, the three reproduced source-review failures, repaired 45-test output 14d1a06f6555e0da2f20353fa385943cf91b2784 and old receipt 9109eeae4313473e3b46dbf5f17628755e6b4729 remain immutable in private history and preparation provenance. The older repaired receipt consumed T010 73ea5d8e646f754088733099ef1680ac6d8605d9; it is not relabeled as having consumed the later corrected T010. This distinct rerun consumed d577589ff0e4796c269b977c2195a1be17a7e2d3.

Reviewed/redacted private source outputs remain in the private owner's Git for the project lifetime under existing permissions. The accepted c8 control at 698bf83671be642421fb28987c820fe36b49b0a6 and its actual [accepted review](https://github.com/opensoft/openXfactory/blob/24c3292df534310c7582fef86bb4baa8653b5c3f/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) remain independently usable; its human decision does not authenticate this new core. All earlier source objects, bindings, historical controls and frozen task bodies remain unchanged.

## Actual authentication boundary

The decision below is pending. Default T020 verification must refuse until Brett authenticates this exact actual packet and the accepted immutable review/control is recorded and default-verified. Read-only preparation checks may validate source, scope, cases, artifacts, authority, original provenance, dependencies, ordering and inventories; they are not full task admission.

```json
{
  "schema": "043-source-authentication-v1",
  "decision": "pending",
  "custodian": "Brett Heap",
  "reviewed_manifest": null,
  "content_sha256": null,
  "reviewed_at": null
}
```

T020 remains unchecked and T021 onward has not started. Ops #628, codeXfactory #583 and Headscale-Install #2 stay draft; the new coordinator packet PR stays draft. Full program Q0, Q1-Q5, supported release/version/tag publication, actual platform/client compatibility, deployment, enrollment, paid resource execution and commercial admission retain their separate gates. No target, image or client was executed by these source checks.
