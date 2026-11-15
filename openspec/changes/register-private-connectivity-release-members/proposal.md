# Proposal: Register private-connectivity release members

Status: draft
Created: 2026-11-15

## Why

T018 cannot publish a supported neutral package through the current closed release inventory: a reproduced synthetic fixture registers and supplies the schema, README, corpus and validator, yet the builder includes none of those four paths. The ratified publication design explicitly requires affected-owner scope review before a release-builder edit; refining T018 also requires preserving accepted evidence under its prior frozen definition.

## What Changes

- Add the exact release-builder and release-regression paths to the existing T018 file scope after neutral/E owner acceptance. Keep the single feature 043 plan and executable task registry.
- Include the four canonical supported connectivity publication members in the normal generated inventory, with exact registration, raw Git-blob digests, supported schema identity and the existing path/type/symlink/collision rules.
- Introduce a release-semantic floor at the first authorized publication cut, preserving every earlier tag's membership and verification. Allocate no version or inventory filename during drafting.
- Accept only the bounded historical-evidence compatibility needed for this owner-approved definition refinement. Complete and authenticate the actual pending T020 packet under its unchanged current definition first; freeze exact accepted control/reader identities before later source changes.
- Retain independent actual CI, output authentication, late cut authorization, reviewed promotion and annotated-tag readback. This scope grant does not pre-approve unseen outputs or Q0–Q5 decisions.

## Capabilities

### New Capabilities

- private-connectivity-production-release-support: Closed neutral release membership, historical verification and evidence-safe definition refinement for feature 043.

### Modified Capabilities

None. The optional binding shape, conformance behavior, rollout decisions and previously published release semantics remain unchanged.

## Impact

The exact additional implementation files are scripts/hermes_runtime_validation/release.py and tests/hermes_runtime_contracts/test_release_inventory.py. The already accepted T007 reader/test, T010 workflow/control/authentication and narrow inventory-census paths may change only for the directly required fixed historical-control bridge, complete freeze refresh and actual collected CI. The design enumerates them and adds no source prefix.

The sole execution registry remains [043 tasks](../../../specs/043-private-connectivity-production/tasks.md). The [publication design](../publish-private-connectivity-production-contract/design.md) and [source-CI design](../extend-private-connectivity-source-ci/design.md) remain governing constraints. [Draft T020 packet #1325](https://github.com/opensoft/openXfactory/pull/1325) is not superseded or authenticated by this proposal. Current source PRs stay draft.
