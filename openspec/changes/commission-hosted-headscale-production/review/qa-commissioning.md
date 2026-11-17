# Hosted Headscale Q0-H decision prepared for review

Status: draft
Kind: review-packet
Prepared: 2026-11-16

## Exact decision boundary

Brett Heap is already accepted as hosted-product source/release owner and
source-evidence custodian. The existing ratified [design](../design.md) remains
unchanged. This packet prepares consumed C-02/C-04 choices for T013. The actual source-choice decision is now recorded below; actual output authentication and task admission remain pending.

The private openXsoft-Hosted-Services Azure plan proposes the existing Opensoft
QA AKS platform in West US, the existing QA Keycloak issuer, scoped vault and
registry reuse, a missing product-owned entitlement/current-revocation journal,
dedicated fenced single-writer storage and explicit per-boundary relay/TLS
decisions. Exact subscription/resource selectors stay in that private plan.
Identity remains independent of product, application and execution authority.

The private plan's two preparation-only files are .azure/plan.md and
docs/production-commissioning.md. They introduce no new executable surface.
The ratified T028-T041 path intersection stays unchanged. Future target/edge,
identity or Ops workload-admission changes require their own exact owning
proposals; source scope cannot substitute for those decisions.

## Actual source-choice acceptance

Brett Heap accepted the exact private plan for source preparation at 2026-11-16T22:16:06.872Z, answering: Approve the plan and source choices (Recommended).
The immutable reviewed [private plan](https://github.com/opensoft/openXsoft-Hosted-Services/blob/6b8b7c4542eb48f9c602afe64ecca460978a674b/.azure/plan.md) and [source permission](source-owner-permission.json) bind the actual choices and original user-record hash. This is source consent only, not actual task-output authentication. Bind the
actual decision to its source and later default-verified T013 output. Do not
interpret source acceptance as target provisioning, C-03/C-07 execution,
protected-output custody, a retention lock, release publication or Q1.

The source-only Git custody policy remains available. Protected live evidence,
actual entitlement/current-revocation readback, DNS/TLS/relay operation and
numerical qualification limits remain distinct consumed decisions.

## Release and gate blockers

The neutral T018 preview is not a published contract and T019 cannot pass yet.
Headscale-Install #2 contains the package source and remains draft; T023 has not
published the supported package/guarded real-client candidate. Source service
implementation must wait for its declared release dependencies. A no-op adapter,
fixture issuer, caller entitlement or copied lab result cannot close them.

The [QA Q1 packet](../../../../specs/043-private-connectivity-production/review/qa-q1-approval-packet.md)
tracks full-program dependencies and exact later decisions. It prepares the
review without executing T050 or passing T051. No frozen input, task metadata,
commissioning control, accepted observation or prior authentication is changed.

## Genuine decision provenance

The original response_item/message/user record is timestamped 2026-11-16T22:16:06.872Z. SHA-256 b95ac26003376eb2e536b74bf16c0a426644168d239cd42144b0b2841d834e82 covers its original UTF-8 JSON line excluding the terminator. The actual question named only source choices and explicitly retained the later gates. No missing role, execution grant, publication or actual output authentication is inferred.

Artifact pin custody: T013 is the canonical machine-readable artifact identity, repository ownership and reachability graph. The source permission retains the genuine human consent, exact choices and unchanged bounded authority without duplicating its private-plan pin. The earlier preparation is preserved by immutable references; a fresh source audit is required for the normalized packet.
