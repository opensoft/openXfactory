# Authentication review: T020 package source after coordinator landing

Status: record

## Exact T020 source-only review target

Brett is the accepted Headscale package source/release owner and source-evidence custodian. He authenticated the actual new private output and its human/source provenance in this exact control at 2026-11-15T21:23:43.887Z, after the actual coordinator qualification results below were available. This decision is separate from the existing owner, support-candidate and custody approvals.

| Item | Immutable review identity |
| --- | --- |
| Authenticated reviewed manifest | [991ebfc0e5](https://github.com/opensoft/openxfactory/blob/991ebfc0e53962990ee587f41307aec809f887a7/specs/043-private-connectivity-production/evidence/commissioning.json) |
| Manifest file SHA-256 | 3bc1ea32f9004c381e1b0eaca08cda57f2ccd703be5266bfa65397a3da89aeb4 |
| Canonical content SHA-256 for authentication | f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332 |
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

This is the first actual foreign binding in the coordinator control. Both existing coordinator CI lanes proved the required private commit presence through that trusted-base producer and the existing repository-scoped read-only App, revoked tokens before tests, and removed ephemeral proof. The actual run/job exports below retain those observed successes. Local metadata preparation did not substitute for live transport qualification. Local full-owner checks and locally derived commit-only metadata cannot substitute for that live transport qualification.

No private source, commit objects/headers or raw output is copied into coordinator Git. The E-only source_container is unchanged. The coordinator retains the typed private references, closed binding expectations and exact owner-resolved inventory; full source/output verification uses the actual private owner Git store separately.

## Human authority, preservation and custody

The [accepted source authority](https://github.com/opensoft/openXfactory/blob/cd13fe4bc03a050d3ad2169b3795e05a3a8bf24d/openspec/changes/commission-headscale-production/review/source-owner-permission.json) and [ratified package design](https://github.com/opensoft/openXfactory/blob/6e2f829b16275827a0b73308623164fa099a7ae9/openspec/changes/commission-headscale-production/design.md) name Brett, the exact four T020 files, required source role, approved source scope and until-superseded source-only lifetime. Existing actual role/matrix/private-source-Git custody decisions remain authoritative. No new source or live authority is inferred from the new output.

The original 43-test candidate, the three reproduced source-review failures, repaired 45-test output 14d1a06f6555e0da2f20353fa385943cf91b2784 and old receipt 9109eeae4313473e3b46dbf5f17628755e6b4729 remain immutable in private history and preparation provenance. The older repaired receipt consumed T010 73ea5d8e646f754088733099ef1680ac6d8605d9; it is not relabeled as having consumed the later corrected T010. This distinct rerun consumed d577589ff0e4796c269b977c2195a1be17a7e2d3.

Reviewed/redacted private source outputs remain in the private owner's Git for the project lifetime under existing permissions. The accepted c8 control at 698bf83671be642421fb28987c820fe36b49b0a6 and its actual [accepted review](https://github.com/opensoft/openXfactory/blob/24c3292df534310c7582fef86bb4baa8653b5c3f/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) remain independently usable; its human decision does not authenticate this new core. All earlier source objects, bindings, historical controls and frozen task bodies remain unchanged.

## Actual custodian authentication

Brett answered `Authenticate this T020 source-only packet (Recommended)` to question `call_b4ada15cf92d4c24989ce1eb79f528bb`, item 0. Original desktop session 01a1c061-ee6e-7e61-9db4-280a724e05c2, user message msg_01a1e118-3a8e-74f1-b440-c7dac73171cd, JSONL record line 36379 records the actual answer at 2026-11-15T21:23:43.887Z. Its raw record SHA-256 is b64f977f4df6f3d03c067f48734121589a61883fbfcce82334a6df10f8be1035 (UTF-8 JSONL record bytes excluding terminal newline). This records a human decision; it is not an agent-generated approval.

```json
{
  "schema": "043-source-authentication-v1",
  "decision": "accepted",
  "custodian": "Brett Heap",
  "reviewed_manifest": {
    "repository": "opensoft/openxfactory",
    "commit": "991ebfc0e53962990ee587f41307aec809f887a7",
    "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
    "sha256": "3bc1ea32f9004c381e1b0eaca08cda57f2ccd703be5266bfa65397a3da89aeb4"
  },
  "content_sha256": "f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332",
  "reviewed_at": "2026-11-15T21:23:43.887Z"
}
```

This accepts exactly the reviewed manifest/core above. Full default verification against a separately committed accepted review/control must still pass before T020 is marked complete. Future changed outputs need their own actual authentication.

## Actual pre-authentication qualification observations

The qualification of coordinator head 98a20eeeb6435f4bcd195fe86d2221e27fb3de5b completed before this decision: 1,197 affected local regressions passed; both actual private-proof CI lanes and SonarCloud passed. Codex cleared that exact head in [its review receipt](https://github.com/opensoft/openXfactory/pull/1325#issuecomment-6898841659). The [actual qualification report](https://github.com/opensoft/openXfactory/pull/1325#issuecomment-6901564896) was the report cited in the authentication question. The root workflow's first attempt was cancelled during the explicit account-switch stop, with cleanup successful; attempt 2 is the separate successful result. Cancellation is retained as cancellation.

The following is a projection of the actual GitHub job API exports, preserving run, attempt, job, times and conclusions for the commissioned proof steps, with each original complete public job-log SHA-256. Projection selects named steps and omits unrelated steps. It contains no environment values, token payloads, private commit headers, private source or private raw output. It is retained here for the project lifetime under existing source-repository permissions. The underlying E-only source_container is unchanged.

````text
[
  {
    "workflow": "pytest-suite",
    "run": 43744065634,
    "attempt": 2,
    "job": 132944956753,
    "url": "https://github.com/opensoft/openXfactory/actions/runs/43744065634/job/132944956753",
    "conclusion": "success",
    "full_log_sha256": "7eed427a1382ee3933abd37a462f2815870c9215baabe607f7c5111f231962bd",
    "head": "98a20eeeb6435f4bcd195fe86d2221e27fb3de5b",
    "steps": [
      {
        "completedAt": "2026-11-15T20:21:33Z",
        "conclusion": "success",
        "name": "Plan private-connectivity commit proof (043)",
        "number": 8,
        "startedAt": "2026-11-15T20:21:33Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T20:21:33Z",
        "conclusion": "success",
        "name": "Require the commissioned App identity (043)",
        "number": 9,
        "startedAt": "2026-11-15T20:21:33Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T20:21:35Z",
        "conclusion": "success",
        "name": "Mint scoped Opensoft source read token (043)",
        "number": 10,
        "startedAt": "2026-11-15T20:21:33Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T20:21:35Z",
        "conclusion": "skipped",
        "name": "Mint scoped domain source read token (043)",
        "number": 11,
        "startedAt": "2026-11-15T20:21:35Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T20:21:36Z",
        "conclusion": "success",
        "name": "Prepare commit-only owner roots with the reviewed producer (043)",
        "number": 12,
        "startedAt": "2026-11-15T20:21:35Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T20:21:36Z",
        "conclusion": "success",
        "name": "Revoke source tokens before any tests (043)",
        "number": 13,
        "startedAt": "2026-11-15T20:21:36Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T21:11:11Z",
        "conclusion": "success",
        "name": "Run private-connectivity production source suites (043)",
        "number": 25,
        "startedAt": "2026-11-15T21:08:37Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T21:11:11Z",
        "conclusion": "success",
        "name": "Remove ephemeral source proof (043)",
        "number": 26,
        "startedAt": "2026-11-15T21:11:11Z",
        "status": "completed"
      }
    ]
  },
  {
    "workflow": "doc-health-py314",
    "run": 43744065782,
    "attempt": 1,
    "job": 132903378627,
    "url": "https://github.com/opensoft/openXfactory/actions/runs/43744065782/job/132903378627",
    "conclusion": "success",
    "full_log_sha256": "2dc04c8adfbac9a3bce66ceb5f451691461bb6ad7f83e13215bf601a04451e30",
    "head": "98a20eeeb6435f4bcd195fe86d2221e27fb3de5b",
    "steps": [
      {
        "completedAt": "2026-11-15T17:58:34Z",
        "conclusion": "success",
        "name": "Plan private-connectivity commit proof (043)",
        "number": 5,
        "startedAt": "2026-11-15T17:58:34Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T17:58:34Z",
        "conclusion": "success",
        "name": "Require the commissioned App identity (043)",
        "number": 6,
        "startedAt": "2026-11-15T17:58:34Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T17:58:35Z",
        "conclusion": "success",
        "name": "Mint scoped Opensoft source read token (043)",
        "number": 7,
        "startedAt": "2026-11-15T17:58:34Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T17:58:35Z",
        "conclusion": "skipped",
        "name": "Mint scoped domain source read token (043)",
        "number": 8,
        "startedAt": "2026-11-15T17:58:35Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T17:58:36Z",
        "conclusion": "success",
        "name": "Prepare commit-only owner roots with the reviewed producer (043)",
        "number": 9,
        "startedAt": "2026-11-15T17:58:35Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T17:58:36Z",
        "conclusion": "success",
        "name": "Revoke source tokens before any tests (043)",
        "number": 10,
        "startedAt": "2026-11-15T17:58:36Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T18:03:52Z",
        "conclusion": "success",
        "name": "Exercise source proof under Python 3.14 (043)",
        "number": 16,
        "startedAt": "2026-11-15T18:03:42Z",
        "status": "completed"
      },
      {
        "completedAt": "2026-11-15T18:03:52Z",
        "conclusion": "success",
        "name": "Remove ephemeral source proof (043)",
        "number": 17,
        "startedAt": "2026-11-15T18:03:52Z",
        "status": "completed"
      }
    ]
  }
]
````

Ops #628, codeXfactory #583, Headscale-Install #2 and coordinator #1325 stay draft. Full program Q0, Q1-Q5, supported release/version/tag publication, actual platform/client compatibility, deployment, enrollment, paid resource execution and commercial admission retain their separate gates. No target, image or client was executed by these source checks.
