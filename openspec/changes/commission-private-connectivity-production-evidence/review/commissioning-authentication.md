# Authentication review: Hosted Headscale source commissioning

Status: record

## Exact Hosted source review target

This is a new actual T013 source-output authentication request for Brett Heap as the accepted Hosted Headscale source/release owner and source-evidence custodian. His source-choice approval at 2026-11-16T22:16:06.872Z is recorded separately. It does not authenticate these later actual outputs.

| Item | Exact immutable identity |
| --- | --- |
| Proposed reviewed manifest | Pending immutable control construction |
| Canonical content SHA-256 | 882449dd9b8dbff18c8adfb7d22306f1f1f558642a868243fee511ef33a9bb4b |
| Complete unchanged definition SHA-256 | 2a46a5420c9f90f5ace72e8482b0fa0541b55f733bd6ad7a8e53ebb99215d796 |
| Actual source | a8bff63ded4372294196b3cf36625990f07bd97d; base f3d47312da796ba893022dc22b93f352b7bd3e0b |
| Original actual output | [29c5ca6cb2b5b1fb56393fefa7b7aa7b157c63b6](https://github.com/opensoft/openXfactory/blob/29c5ca6cb2b5b1fb56393fefa7b7aa7b157c63b6/specs/043-private-connectivity-production/evidence/T013.json), SHA-256 8e659674756f93178a2654a5bb60cd17109734ff08ed4bf2c1aa387dec0af4ff |
| Distinct receipt | [17a1b1e280b64ed366f7bca5da7de7b01a51644c](https://github.com/opensoft/openXfactory/blob/17a1b1e280b64ed366f7bca5da7de7b01a51644c/specs/043-private-connectivity-production/evidence/T013.json), SHA-256 4f2364845af9d9279c31d261b406507750f2502052bf6fcfc39ad487a47f97f3 |
| Source permission | [Actual consent and exact scope](https://github.com/opensoft/openXfactory/blob/a8bff63ded4372294196b3cf36625990f07bd97d/openspec/changes/commission-hosted-headscale-production/review/source-owner-permission.json) |

## Actual observations

The read-only owner audit ran from 2026-11-16T22:58:37.001237+00:00 to 2026-11-16T22:58:41.693698+00:00 and exited zero. It verified actual accepted source consent, the ratified proposal, the unchanged complete 043 definition, all nine exact Hosted task/file scopes, the accepted private plan bytes at 6b8b7c4542eb48f9c602afe64ecca460978a674b by SHA-256, and pinned OpenSpec 1.12.0 strict validation. It produced all three frozen T013 cases: actual-provider-platform, identity-entitlement-custody, and product-owner-scope.

The accepted choices are existing Opensoft QA AKS in West US, the QA Keycloak issuer and RS256 API verification path, independent product-owned SQLite current entitlement/revocation state, scoped QA vault/registry reuse and dedicated fenced single-writer durable state. The private plan remains in the private owner repository; this public packet exports only reviewed/redacted source facts and typed immutable references. API authority remains separate from the MCP Ed25519 requirement. No live compatibility or capacity is inferred.

The collector first passed full default verification of the actually authenticated T010 predecessor against control 8ac068510936c97d21ace2b923ad00c0a6238b68, whole-file SHA-256 e42735845944bb5c36d46a4648c56ab9bd4b0dfd82d4bc3a5b7128b08c6b89bf. It then repeated the audit against unchanged source. The successful initial audit remains in preparation_history. Initial export preparation refused machine-local paths emitted by the verified CLI; the actual raw output hashes are retained and only the exact checkout/cache prefixes are redacted. No original observation, Git identity, command, result or timestamp was changed.

## Preserved prior acceptance

The prior actual T010/T021/T022 authentication and source packet remain immutable at [the original review](https://github.com/opensoft/openXfactory/blob/b2670b0d8ecc2b225d4e114ecacb00276c536398/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md) and control 8ac068510936c97d21ace2b923ad00c0a6238b68. All prior bindings, outputs, historical readers and contained E objects are preserved unchanged. T013 uses distinct public Git original/receipt references; it is not added to the contained E bootstrap object table. No definition or 68-task registry field changes.

## Authentication decision

The following decision remains pending until Brett reviews these actual observations. Source-scope approval, preparation checks, unit tests, CI and automated review do not replace actual custodian authentication. Default verification must refuse this new control while pending. T013 stays unchecked until the real decision is recorded and full default verification passes.

```json
{
  "schema": "043-source-authentication-v1",
  "decision": "pending",
  "custodian": "Brett Heap",
  "reviewed_manifest": null,
  "content_sha256": "882449dd9b8dbff18c8adfb7d22306f1f1f558642a868243fee511ef33a9bb4b",
  "reviewed_at": null
}
```

## Release and rollout boundary

The source-only release-builder PR #1327 is merged. PR #1325 was indirectly marked merged because its head was already an ancestor; neither is presented as an open draft. The package #2, Ops #628, codeXfactory #583 and Hosted Services #2 remain draft. All new preparation PRs remain draft.

T018/T019 release cut, version/tag/publication and compatibility readback remain incomplete; no version is allocated here. T023 package publication and real-client runner prerequisites remain due before H runtime consumers. Full program Q0 remains incomplete. Target admission, edge/TLS/relay compatibility, protected custody and irreversible retention decisions, provisioning, C-03, Q1-Q5, enrollment and commercial rollout remain separately gated. This packet authenticates no deployment or live qualification.
