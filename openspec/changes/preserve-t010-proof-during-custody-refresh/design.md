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
producer. Preserve the accepted source_ci_producer and
source_ci_original_reference exactly as recorded in the immutable legacy
control. Verify both against that control before the successor is selected.
Keep the original checked source observation and required lanes.
The normal subject for every fresh decision uses its own qualified definition.

### Closed file scope

Under T007 E maintenance, review and update
`specs/043-private-connectivity-production/verify-evidence.py` with the exact
compatibility binding and matching reviewed definition identity. Use the existing
decision and proof readers. Under T010 E maintenance, extend the existing
`specs/043-private-connectivity-production/tests/test_delegated_evidence.py`
regressions and requalify T010 through its original source lanes.
Extend assertions inside existing collected cases to retain the 100
unique test identities, all existing coverage, and the measured count in
both required workflows. Any necessary collection change requires separate
exact scope for both workflow validators before use.
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
Exercise task and phase substitutions separately at compatibility selection
with the original decision, proof and approved successor intact. Require the
normal subject path before the caller's scope validation can mask the result.
Exercise the exact original decision and proof under a different,
unapproved successor definition. Separately change a decision-body field
outside its scope while preserving the source scope, proof and approved
successor. Require refusal in both cases.
Prove the exact original scope retains its original review time and normal
checks. Exercise a valid, independently registered fresh source-phase T010
C-01 in the same approved successor through the current-definition path.
Demonstrate effect and runtime refusal with the historical proof.

## Qualification and recovery

Record independent T007 and T010 maintenance scope acceptance before
implementing the binding. Build the complete successor definition from the
exact approved Ops scope records and the full input freeze. The accepted
scope bodies enter the freeze. Fresh attestations that bind that definition
remain in the existing evidence registration outside the inputs they sign.

Stage the transition on protected main. Keep the current accepted
commissioning manifest selected as the workflows' predecessor during the
reader and definition update. Register that manifest and its reader as one
fixed historical control for the existing nested historical reader. Keep
the registered commit, path and digest. At the reviewed base, both files come from 9da72c839c5904876d0ccdf0af4997ec5fb42eed.
The accepted evidence/commissioning.json has SHA-256
9493a7f106a0306bbb1e057a84b0673d9468f4b320f32cb507f5b062f5195248.
Its verify-evidence.py has SHA-256
87f2c99e7e6f481af1b2cc0d79e78d62e9cc105ca18c46a273cff5c2fe29ee9c.
During the transition, both workflows continue selecting the protected
predecessor for commit-proof preparation. Keep source-only default
verification on the independently pinned predecessor reader until the
successor has an authenticated active manifest. Before an operator verifies
the predecessor, independently select current protected main using the
existing attestor GitHub.qualified_base readback and fetch that commit's
active evidence/commissioning.json with its GitHub.content readback.
Require those active bytes to match the fixed predecessor manifest, then
verify the predecessor with its pinned reader and the exact registered
reference. After that verification and immediately before accepting its
result, repeat the existing GitHub branch readback. Require main to
remain protected at the identical qualified commit. An intervening
advance can change the active control even when the exact older content
fetch still succeeds. Its authenticated revocations and completion
closures are current only while that readback identifies it as the
active protected control. Refuse stale, unavailable or changed authority
and hold the transition. This adds no top-level historical fallback to the
successor reader and does not accept a caller-supplied old trust reference
as evidence of current authority.

After the successor is selected, its authenticated manifest supplies current
revocations and completion closures to the existing nested historical
path. Exercise refusal when current authority is missing or when the active
control changed after pinning. Simulate main moving between the initial
qualification and the final readback while the pinned content and proof
remain valid. Separately exercise nested verification when a predecessor
source grant was revoked without a valid completion closure.

Wait for required CI and evaluated Sonar on the protected reader and freeze.
Prepare the successor's commissioning manifest at a separate immutable
candidate commit using the exact protected reader and current T010 source
evidence. Have the independent reviewers verify that candidate and its actual
source outputs. Pass their immutable review reference and the candidate
manifest to the existing qualified attestor. Register the resulting approval
and verify the successor with default verification before
making it the selected CI control. Verify the historical controls and obtain
successful evidence from both required source lanes using a trusted base
whose selected active manifest is the exact successor. Record each actual
run and its selected base. A promotion run can still select its predecessor
through the PR base or push event.before and cannot establish this result.
If a successor-backed lane fails or remains unverified, hold the private
archive write and use the reviewed rollback under current authority.
Preserve the original T010 proof throughout.

Under the qualified successor, recheck and bind the exact one-path Ops C-01
and C-08 decisions to its definition before the archive write. The qualified
successor stage supplies T010 and the separate custody authorization. After
the Ops archive lands, use its exact private readback to qualify the later
T015 evidence and run default T015 admission.
