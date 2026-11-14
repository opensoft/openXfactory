# Design: Private component source proof in coordinator CI

Status: draft

## Context

See [proposal](proposal.md). The real-data inventory test in tests/doc-health/test_pin_reachability.py constructs only a coordinator Git root. The production foreign pin member is correctly FUTURE while no foreign record is committed. Headscale-Install #2 has an actual package source candidate; adding its binding without a private owner proof root would fail that test in both pytest-suite and doc-health-py314.

The accepted E design states: "If implementation needs another source/test/CI path, return to owner review before editing." The bootstrap amendment permits only E contained objects. It does not permit private component source imports into that container or public Git exports of private commit objects. The existing component owner decisions remain valid; this proposal supplies the missing bounded CI/custody scope.

## Goals / Non-Goals

**Goals:** Prove ownership and immutable commit presence for actual registered 043 references, in both existing CI jobs, with explicit inputs and ephemeral private metadata. Keep actual source admission, human authentication and historical controls distinct.

**Non-Goals:** Full private source checkout in public CI; private source publication; App/installation/secret/permission or billing changes; generic repository discovery; target access; release/tag authority; Q0-program or Q1–Q5 acceptance.

## Decisions

### Exact additional E surfaces

All paths are relative to opensoft/openXfactory. No directory-wide grant is proposed.

| Path | Bounded change | Task |
| --- | --- | --- |
| specs/043-private-connectivity-production/prepare-source-roots.py | Separate, explicitly networked CI preparation of fixed-owner commit proof roots; no task verification or target commands | T009 |
| specs/043-private-connectivity-production/tests/test_source_roots.py | Closed inputs, actual Git object/provenance, credential/custody, incomplete-proof refusal and workflow-wiring regressions | T009 |
| tests/doc-health/test_pin_reachability.py | Read explicit private proof roots for actual 043 inventory validation; retain coordinator-only and rejection controls | T009 |
| scripts/doc_health/pin_class.py | Promote the existing foreign production member only when actual foreign data is committed; preserve all ownership/reachability rules | T009/T010 |
| tests/doc-health/test_sentinel_vocabulary.py | Only actual measured census/member-presence deltas | T009/T010 |
| .github/workflows/pytest-suite.yml | Explicit preparation before tests, bounded read-only tokens, new suite collection/results; preserve existing decision-core checkout and all gate obligations | T010 |
| .github/workflows/doc-health-py314.yml | The same source-proof precondition before its existing doc-health run; preserve its trigger/check name and obligations | T010 |

Existing E reader/inventory helpers and their regression modules remain available only for directly affected compatibility/regression repairs within their accepted scope. The existing exact commissioning JSON, T010 receipt and authentication review record remain the sole coordinator commissioning/control output surfaces; this change adds no export prefix.

### Exact proposed frozen-input refinement

After actual affected-owner acceptance, add only the two new helper/test paths above to T009's existing files field, and add only .github/workflows/doc-health-py314.yml to T010's existing files field. Their existing fields remain present. Add to contracts/task-evidence.md the distinction between temporary CI commit-presence proof roots and full read-only source/task admission. The 16-input freeze is then recomputed in full and the accepted verifier definition is refreshed to that reviewed identity. All 68 task IDs, owners, classes, dependencies, cases and verification commands remain unchanged. No other frozen input refinement is proposed.

Historical accepted E/N/L controls retain their exact prior definition, reader and immutable anchors. They are not repinned, rewritten or made to claim tests they did not run. A newly extended control must identify the new definition and actual source/CI evidence, preserve original observation identities, and receive separate actual custodian authentication before default admission. If a prior dependency needs the historical definition, use its matching immutable reader and inputs; never treat a new freeze as retroactive authentication. Existing E helper surfaces may implement that bounded historical-definition validation with rejection tests; they may not accept a caller-selected definition or waive a mismatch.

### Fixed owners and existing App access

The closed private source allowlist is:

| Owner | Repository |
| --- | --- |
| L | opensoft/Headscale-Install |
| I | opensoft/xFactory-Installer |
| H | opensoft/openXsoft-Hosted-Services |
| O | opensoft/opsXfactory |
| D | codeXfactory/codeXfactory |

Canonical case normalization follows the existing fixed repository identities; no arbitrary owner, repository, remote or URL is admitted. Fetch only repositories/full 40-character commit identities actually required by committed, closed 043 records and their exact inventories. The coordinator root remains its own checkout and cannot be overridden by an environment map.

Read-only service inventory on 2026-11-14 observed App openxfactory, ID 4253636, with active Opensoft installation 145372182 and codeXfactory installation 160352673. Both existing installations select all repositories. This proposal does not expand them. The coordinator already has OPENXFACTORY_APP_ID and OPENXFACTORY_APP_PRIVATE_KEY secret names; no secret value was read. Each job must verify the configured App/installation identities at use, request contents:read explicitly and only the required repository names, and fail on an unavailable/mismatched identity. Do not use MERGE_MASTER_APP_KEY, inherit the App's write permissions, modify a secret, or reuse the separate existing decision-core token for this purpose.

Credentialed preparation occurs in its own bounded step before PR tests. It must use the exact reviewed producer revision accepted for this source-CI scope and refuse if that provenance cannot be established; unreviewed PR commands, hooks, credential helpers, remotes or script paths cannot run with either App key or private read token. Establish and qualify that producer before introducing private records. Preserve existing fork/secret availability and bootstrap-authority rules; no pull_request_target trigger, author bypass, generic trust promotion or new approval envelope is introduced. The App key goes only to token creation, never to the producer or test processes. Revoke the new tokens and remove transient credential material before any PR test process, including on failure.

### Ephemeral commit metadata and explicit roots

Create separate task-owned bare Git stores under runner temporary storage, outside the coordinator checkout. Fetch only required full commit objects with bounded shallow, tree-filtered, no-tag reads from their exact canonical GitHub repositories. Verify object type/identity, origin and the filtered object population. Unexpected trees/blobs or an unavailable filtering guarantee fail; no full-fetch fallback or checkout is allowed. Keep credentials out of remotes/config, command-line output and logs. Do not log commit contents/headers/messages or upload/cache these stores. Remove temporary stores after the job; retain only reviewed/redacted public source/CI results under the already accepted source custody policy.

An explicit PC_SOURCE_PROOF_ROOTS map supplies the fixed owner roots to the actual-data inventory regression. It is distinct from the full verifier's PC_EVIDENCE_ROOTS. Reject unknown/duplicate/missing required owners, coordinator overrides, roots aliasing the coordinator or each other, wrong origins, missing commits, forged local ownership, and implicit discovery. With no actual private references no token or fetch is needed, and the foreign population remains FUTURE. With private references, absent credentials or any incomplete proof is a failure, never a skip or local-object fallback.

The inventory reader remains offline/read-only with lazy fetch disabled. These shallow metadata stores prove only immutable commit presence in the correct owner's repository. Full task/source/case/artifact/dependency/default authentication verification still requires the actual private owner Git stores and accepted source custody. CI metadata proof cannot substitute for reading tested source/output bytes or authenticating them.

Copying private commit objects or source into public coordinator Git, using a broad App token, silently skipping foreign proof, and converting standing members to rolling are rejected. Full private checkouts in both public CI jobs are also rejected because commit-presence inventory proof does not need their source trees.

### Validation and evidence

Tests precede implementation. Include positive actual-Git fixture controls and refusals for every input/provenance/custody rule, absent credentials, changed owners/commits, incomplete metadata, hidden lazy fetch and credential leakage. Assert both workflow entry points prepare proof before collection, revoke credentials before tests and preserve existing names, floors, exact skip counts, named verdicts and decision-core behavior. Explicitly collect the new helper suite and measure its real result; no guessed count is introduced in this draft.

Run the affected 287 verifier/40 inventory tests and shared pin/reachability/sentinel/governance checks, then actual exact-head CI in both existing jobs. Measure any changed standing census/member count from the committed tree. Preserve failed preparations and successful reruns. Source qualification and the actual new custodian review precede an extended control's admission; T020 stays unchecked until its full default verifier passes.

## Risks / Trade-offs

- Private metadata or credentials escaping through artifacts/logs → separate stores, minimal object population, closed origins, reviewed producer, token revocation, no upload/cache and cleanup on every exit.
- A shallow proof being mistaken for source verification → separate root maps and retain full owner-store/default-authentication requirements.
- A new definition invalidating historical dependencies → retain matching historical readers/anchors and qualify the bounded definition bridge; no rewriting old observations or inherited authentication.
- Existing App secrets not matching the observed installation → fail and report the exact missing prerequisite; make no settings or secret change.
- One CI lane lacking private proof → both named entry points carry the same precondition and fail on incomplete actual data.

## Migration Plan

Keep this proposal draft until Brett accepts its exact E/file/custody/refreeze scope. Then refine only the listed frozen fields, retain the previous definition, implement and qualify the producer and regressions, and collect actual reviewed source CI before private data admission. Introduce an actual private binding only after the proof precondition is usable; promote/census its real foreign member deliberately. Obtain authentication of the new actual packet and use default verification before checking any dependent task.

On failure retain all original observations and prior accepted anchors, stop affected admission and supersede only through reviewed source corrections. Do not disable checks, broaden token access, replace accepted evidence, enter a live gate, merge or publish a release as a recovery shortcut. All four current PRs remain draft.
