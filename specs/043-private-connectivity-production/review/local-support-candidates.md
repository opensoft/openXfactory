# C-05 local support qualification candidates

Status: draft
Created: 2026-11-14

This is a concrete source-preparation choice for T011-T012. The source owners
and exact implementation scopes are already accepted. This choice supplies
proposed versions, platforms and distribution channels; actual compatibility
qualification, current execution authority and Q1-Q5 remain separate.

## Proposed first matrix

| Subject | Qualification candidate |
| --- | --- |
| Headscale | Upstream stable v0.29.7; official Linux amd64 release inputs and resulting immutable Docker image pinned during T020 |
| Tailscale clients | Stable v1.104.7 for each approved client combination |
| Local server | Ubuntu 24.04 LTS amd64, Docker Engine 29.9.3; dedicated isolated writable state |
| Windows client | Windows 11 amd64, official architecture-specific MSI |
| macOS clients | macOS 15, Apple Silicon and Intel, official Standalone GUI PKG |
| Linux client | Ubuntu 24.04 LTS amd64, official stable Debian package/repository |
| Installer behavior | Local install-new/connect-existing and optional Hosted Headscale selection within the accepted adapter/setup scope; workstation-intake and Store work remain excluded |

The [Headscale v0.29.7 release](https://github.com/juanfont/headscale/releases/tag/v0.29.7)
and [Tailscale v1.104.7 release](https://github.com/tailscale/tailscale/releases/tag/v1.104.7)
were checked against their official latest-release APIs on 2026-11-14:
both are published stable releases. Availability does not establish their
compatibility or acceptance in this factory.

The [official stable package index](https://pkgs.tailscale.com/stable/) currently
lists the v1.104.7 Windows amd64 MSI and macOS Standalone PKG, provides
distribution-specific Linux packages, and describes checksum retrieval.
The package trust/signature checks, exact content digests and complete
server/client combination identities must be retained before qualification.

Eagle currently reports Docker Desktop 4.99.0 with Linux amd64 Engine 29.9.3.
That is an observed development runtime. It does not establish qualification
of the proposed native Ubuntu server profile; the actual target and runtime
identities are closed before execution.

## Mac evidence boundary

Tailscale documents [Standalone, App Store and CLI variants](https://tailscale.com/docs/concepts/macos-variants)
with different OS integration. The proposed customer profile is the Standalone
GUI package. The GitHub macOS runner investigation remains a separate CLI/utun
source-test profile and cannot qualify that GUI profile.

An actual authorized GUI-capable Mac target for each approved architecture is
still required before its qualification consumer and Q1. Missing hardware
keeps that combination unqualified. The existing repository USD 0 paid-Mac
guard remains effective; this choice starts no runner job or enrollment.

## Decision requested

Accept this first qualification matrix for source preparation, or specify the
versions/platforms/channels to revise. Acceptance supplies the consumed
support-scope choice for the package/installer readiness records. Actual
source evidence and their verification remain required before either task
is completed.

This decision allocates no contract version, advances no consumer pin and
does not claim a supported commercial release. It authorizes no installation,
deployment, paid resource, client enrollment or fault injection. Exact target,
authority, integration, custody, numeric objectives and staging-envelope
decisions remain due at their consuming gates. All three PRs remain draft.
