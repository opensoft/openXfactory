## Context

The selected profile is the codeXfactory MCP workload. The current
[Feature 043 grant](../authorize-private-connectivity-internal-production/design.md#4-intended-targets-and-integrations)
names an EdDSA configuration path. The Domain owner has ratified the
additive verifier design. Ops has ratified the concrete issuer and
resource-audience route. The protected workload source still needs the
owner's verifier realization.

## Goals

Bind the exact approved operating-envelope wording to its human decision and
the existing owner chain. Preserve the immutable grant and its current
duration, repositories, budgets, custody, target and rollout constraints.

## Decisions

### Approved MCP identity row

This text supersedes only the original MCP identity row after protected
admission of the amendment. The [approval record](review/2026-11-18-approval.md)
pins its reviewed packet and original message.

> CodeXfactory MCP uses the ratified Opensoft Entra v2.0 issuer, the tenant-specific published JWKS, and the client ID of its dedicated single-tenant resource application as the exact audience. Apply the Domain owner's additive RS256/EdDSA profile with algorithm-to-key binding and preserve the existing EdDSA path. Require an admitted caller and the existing tenant, subject, time and authorization checks. An existing matching app may be used only with its authoritative registration and claim readback. Creating a dedicated resource registration, admitting a caller or changing tenant configuration requires its own exact operating authority. Keep Hosted Headscale on the separately approved Keycloak RS256 product API identity and entitlement/revocation path.

### C-01 and frozen definition

The follow-up scope lists the exact owner paths, command envelopes and
definition inputs. Review the owner-local scopes independently before use,
recompute the registered sixteen-input/68-task definition and demonstrate
that all unaffected task owners, fields, dependencies and historical proofs
are preserved. An amendment to the root policy takes effect through its own
protected admission and proof, preserving the original authority record.
The independent approval of the wording is recorded by this packet.

### Existing owner dependencies

The Domain owner can prepare the additive verifier and fixtures under the
ratified Slice A source plan once the exact affected-owner file scope is
reviewed. Deployment-specific declarations require the exact Entra resource
identifier and approved Ops plan. The protected Ops hosting plan currently
names `hermes`. Its owner issuer correction selects the Opensoft Entra v2.0
issuer, tenant JWKS and a dedicated resource-only app as audience. Its task
2.1 requires the registration and claim readback. Caller admission is separate.
The material placement and identity plan changes retain the owner's task 4.2
reapproval.

The artifact rebuilt from the unchanged Domain verifier remains historical
reproduction evidence. The eventual Ops task 4.4 must verify the rebuilt
wheel, manifest and image with the actual approved identity configuration
and its refusal cases. Task 4.5 is Brett Heap's separate decision over the
resulting digest set. Owner publication and Ops 5.1 readback follow that act.

- [Ops issuer correction](https://github.com/opensoft/opsXfactory/pull/579)
- [Domain verifier owner proposal](https://github.com/codeXfactory/codeXfactory/pull/561)
- [Domain source and deployment scope](https://github.com/codeXfactory/codeXfactory/blob/0e8bf9fcefa88dd0cca0b1d7577300cfa6eb4978/openspec/changes/adopt-factory-mcp-auth-profile/tasks.md)

## Risks and controls

- The eventual resource registration readback binds tenant, issuer, resource
  audience and admitted caller. Record claim values and protected receipt
  identities. Credential material belongs in the admitted custody system.
- Keep exact reviewed source, positive and refusal results and later
  protected artifact/provider evidence as separate predicates for acceptance.
- Hosted Headscale retains its own Keycloak RS256 integration and its existing
  entitlement and revocation path.
