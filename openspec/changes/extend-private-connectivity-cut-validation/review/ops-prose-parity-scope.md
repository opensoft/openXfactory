# Additional exact Ops prose-parity handoff

Status: ratified
Ratified: 2026-11-16 by Brett Heap; actual four-path decision at 2026-11-17T03:40:50.580Z.
Kind: feature-amendment
Prepared: 2026-11-16
Disposition: accepted; exact T043 companion paths and complete source freeze refreshed

## Approved baseline and measured failure

The N/E design at 55e3cafd3 and matching Ops/Tenant designs were genuinely
accepted at 2026-11-17T02:55:36.438Z and 2026-11-17T03:01:06.114Z.
The resulting complete 4f963e0f23914b745d895fab7859b6dc18d613814a32cbc82f77535188c081b8
source definition is valid and retains all 68 registry rows. Its verifier
source passed 620 tests; the other source suites passed 137; 99 CI/census/pin
checks also passed. These are actual source observations, not authenticated
new output or rollout acceptance.

Ops's previously unnamed CI failure is now reproduced at a fixed head:
the four existing active restatements of its bounded-action requirement must
match the new fifth delta exactly, or archive order can delete approved scope.
The owner-local review/prose-parity-scope.md records the exact intended block.

## Four additional T043 files only

Subject to actual matching Ops and N/E owner acceptance, add these four exact
Ops-relative paths to T043 in the sole feature 043 task list:

- openspec/changes/admit-poddisruptionbudget-to-aks-scope/specs/aks-administration-workflow/spec.md
- openspec/changes/admit-secretproviderclass-to-aks-scope/specs/aks-administration-workflow/spec.md
- openspec/changes/adopt-keycloak-broker-qa/specs/aks-administration-workflow/spec.md
- openspec/changes/reanchor-codexfactory-mcp-workload-set/specs/aks-administration-workflow/spec.md

No N path, T047 path, task ID, owner, class, case, dependency or verification
command changes. Only owner-scopes.md's matching handoff clarification and the
complete 16-input/68-task definition refresh accompany this file refinement.
The canonical Ops spec is already in T043's accepted seventeen additions.

Splice only the complete existing bounded-action requirement block, preserving
the existing MCP spotwork anchor, RULED workcore1 fallback and placement history.
The baseline block SHA-256 is 8d6be8983c8a8a9d24d39bc9b831dc2e46d1d08148c4b4b862f557229e5bf822;
the intended block SHA-256 is 84576b9ad5a71529b60de7a0dc51a1448ff09eecbbe4de59c4965d239223d008.
Only the already approved three QA sets and their boundary scenario are added.
Keep unrelated requirement/scenario bytes and the existing parity assertion.

## Evidence and authority boundary

The current 4f963e0f source candidate is not an authenticated control and SHALL
NOT be added as accepted history. Preserve its actual outputs under their
original source identity. After acceptance, qualify the complete revised E
source/CI on published contract-v4.2, present its new actual packet for separate
custodian authentication, and pass default admission before N consumption.
The existing fixed original 2a46 controls/readers and all current revocations
remain unchanged.

Ops may make the four governance companion splices after this exact acceptance;
actual canonical/workflow/runtime realization remains T043 and keeps its
release dependencies. All PRs stay draft. No merge, publication, target effect,
spend, enrollment, protected lock or Q0-Q5 acceptance is granted.

Before any future authorized landing, #1335 still lands independently before
#1336. The N cut stays separate and must be re-integrated/re-generated only
after its source prerequisites, actual output authentication and late
version/floor checks. No indirect landing is authorized.

Exact owner-local review: [Ops companion scope](https://github.com/opensoft/opsXfactory/blob/657b02d0e6a4f01d6fcbef8453a1937131331550/openspec/changes/admit-private-connectivity-qa-operations/review/prose-parity-scope.md). The four companion files remain unchanged pending actual acceptance.
