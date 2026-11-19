# Design for an exact T010 proof compatibility binding

Status: draft
Kind: design

## Context

The signed source grant requires retaining the original accepted proof and
qualifying each new source scope. The current protected reader is
`9da72c839c5904876d0ccdf0af4997ec5fb42eed`. The in-memory T015 preview verified
all sixteen inputs and the same 68 task rows. The original T010 C-01 proof
passed under its accepted definition. The same decision under the preview
definition produced `delegated output is not independently qualified`.

## Goal and boundary

Keep the original T010 source-scope evidence verifiable during the exact,
approved T015 custody refresh. The proof continues to attest to the original
T010 decision. New custody and execution decisions need their own valid
subject and review.

## Decisions

### Preserve one immutable proof

Bind the compatibility check to source-phase T010, kind C-01, the exact
canonical decision content and the exact registered proof. Use these already
accepted values:

| Field | Immutable value |
|---|---|
| Original definition | `281fdf8a64a6d3851a775d558bc95fcf2899d162bc6c2a615bdc88657fcc9421` |
| Canonical decision SHA-256 before the delegation reference | `4f7060b31899c5b1a04452bd8b968edc42e9de04d47d6204287792c9c1e0cbcb` |
| Proof repository | `opensoft/openxfactory` |
| Proof commit | `5d82621d28fe94a9f0bef663015dcc8cd2f6d10f` |
| Proof path | `specs/043-private-connectivity-production/evidence/T010.json` |
| Proof SHA-256 | `8060207aca399a81340fb992271e1358b605f4d38bd6842721c154ef779f8619` |

Restrict the carry to the exact successor definition approved for this
custody refresh. Bind that successor after review of its actual owner records
and full input freeze. Keep the existing registered reference, content hash,
human grant, original reviewers, time and revocation checks. Obtain fresh
authentication for the current commissioning subject through the existing
producer. Keep the original checked source observation and required lanes.
The normal subject for every fresh decision uses its own qualified definition.

### Closed file scope

Under T007 E maintenance, review and update
`specs/043-private-connectivity-production/verify-evidence.py` with the exact
compatibility binding and matching reviewed definition identity. Use the existing
decision and proof readers. Under T010 E maintenance, extend the existing
`specs/043-private-connectivity-production/tests/test_delegated_evidence.py`
regressions and requalify T010 through its original source lanes.
Preserve both task file envelopes and their existing dependencies.

Use the existing `owner-scopes.md` and `contracts/task-evidence.md` inputs for
the reviewed scope and complete regenerated freeze. Keep all 68 executable
rows, commands, evidence classes, scopes and cases. T015 retains T010 and its
coordinator-only write paths. The Ops owner’s one-path C-01 and C-08 decisions
govern the new archive write. The original audit commands retain their
original authority and timestamps.

## Risks and controls

A decision may appear valid under a different task, phase, scope or proof
reference. Require a refusal for each substitution and for revoked authority.
Exercise the exact original decision and proof under a different,
unapproved successor definition. Separately change a decision-body field
outside its scope while preserving the source scope, proof and approved
successor. Require refusal in both cases.
Prove the exact original scope retains its original review time and normal
checks. Exercise fresh source approval through the current-definition path.
Demonstrate effect and runtime refusal with the historical proof.

## Qualification and recovery

Record independent T007 and T010 maintenance scope acceptance before
implementing the binding. Record the proposed Ops custody scope and refresh
the complete definition from its actual accepted source records. Qualify the
successor with current T010 commissioning and the applicable historical
controls. This qualification uses the original T010 proof and fresh measured
source authentication for the successor before the private archive exists.
If a predicate fails, retain the original protected definition and proof.

Under the qualified successor, recheck and bind the exact one-path Ops C-01
and C-08 decisions to its definition before the archive write. The qualified
successor stage supplies T010 and the separate custody authorization. After
the Ops archive lands, use its exact private readback to qualify the later
T015 evidence and run default T015 admission.
