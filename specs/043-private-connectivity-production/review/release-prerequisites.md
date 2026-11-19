# Neutral/package release prerequisites for QA

Status: draft
Kind: review-packet
Prepared: 2026-11-16

## Current neutral preflight

The existing [T018 review candidate](../evidence/T018.json) was applied only to
an isolated review checkout of current main. Canonical source, versions, tags
and inventories were not changed. The same reviewed patch remains identified
by SHA-256 6ef8608caa8e19c01b22f3abb06d69b9868c903c5057375345ba7f12b4510172; no version is reserved.

Actual refreshed checks passed: 93 release regressions, 37 neutral regressions
plus 52 subtests, and 189 manifest digests. The builder generated a 346-member
preview, SHA-256 632c29f80e4f999fa2100089c276ff4a986a92abac4ce6aa086448ff359c4458. Initial generation
correctly refused unmaterialized pinned carved legs; after initializing those
exact gitlinks, unchanged-source generation passed. The failed preparation is
retained and is not recorded as a release failure or pass.

Fresh independent remote readback of actual contract-v4.0, contract-v4.1 and
contract-v4.2 passed. The observed next minor candidate is contract-v4.3,
conditional on late version/floor and exact inventory-file closure at an actual
authorized cut. The generic preview is outside contracts/releases and is not
a canonical inventory or allocated release.

## Actual remaining release actions

T018 still needs the concrete cut authority, late version/floor/path closure,
normal atomic source/manifest/changelog/generated inventory, reviewed landing
and annotated publication. T019 independently verifies the actual released
tag, commit, content and compatibility before consumer pins. Source tests or
this preview cannot supply either completion.

Headscale-Install #2 retains its authenticated T020-T022 foundation/endpoint/
recovery source. T023 still needs its guarded real-client runner, supported
candidate, required source CI and actual artifact/tag/provenance readback.
The actual standalone Ubuntu qualification target and native client
qualification remain consuming-gate prerequisites.

T028 consumes T013/T019/T023; T029 and T032 consume T013/T019. Do not write
production adapters against draft neutral/package pins or the synthetic pilot.
The remaining hosted, installer, actual-domain and Ops releases then close the
full T049 integration/harness matrix before T050/Q1.

## Draft constraint and decisions still due

Headscale-Install #2, Ops #628 and codeXfactory #583 remain draft. A requirement
to keep them draft leaves reviewed landing/publication pending; there is no
approved indirect-merge or mutable-tag workaround. Prepare their exact source
candidates and request a concrete exception only when reviewable and qualified.

The source-choice approval for the Hosted plan supplies no cut, tag, merge,
deployment or Q1 grant. Actual output authentication remains independent.
The [Q1 dossier](qa-q1-approval-packet.md) records all later entry blockers.
No task checkbox, accepted control, historical observation or frozen task
definition is changed by this preflight packet.
