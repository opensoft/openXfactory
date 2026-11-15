# Installer runtime and distribution choice

Status: draft
Created: 2026-11-14

## Proposed first qualification channel

This is the remaining installer-product choice for T012 source preparation. Brett already accepted the exact installer source owner/scope, private source-only Git custody, local server/client candidates and optional hosted-selection behavior. The previously approved MSI/PKG/Debian channels are Tailscale client channels.

| Subject | Proposed source qualification choice |
| --- | --- |
| Installer command host | Ubuntu 24.04 LTS amd64, CPython 3.12 in an isolated virtual environment |
| Exact runtime closure | Pin and record the actual security-patched Ubuntu/Python package and build-tool identities before T026 build/release/qualification; a mutable latest runtime cannot qualify |
| Product | Isolated private-connectivity Python CLI/package; console command xfactory-connectivity, distribution name xfactory-private-connectivity; preserve workstation application and exclude Store/intake work |
| Build inputs | The ratified isolated PEP 517 context and hash-pinned build-dependency lock; no unrelated workstation build or dependency reuse |
| Internal distribution | Owner-reviewed wheel, sdist and complete hash-pinned offline dependency bundle as private xFactory-Installer GitHub release assets under existing access; actual publication still needs current release authority |
| Install input | Verified approved local artifact bundle, installed into the isolated environment without package-index access; no Hosted Headscale entitlement is required for local use |
| Trust and readback | Exact owner release tag/commit, asset identities, SHA-256, approved compatibility manifest and normal owner release provenance/readback; package bytes must match before installation |
| Public/customer delivery | Not selected by this internal qualification choice; each actual customer distribution/commercial offer still needs its own approved channel and access decision |

Ubuntu's [Python availability reference](https://ubuntu.com/developers/docs/reference/availability/python/) identifies CPython 3.12 for Ubuntu 24.04. This minor-runtime choice does not pin or accept an unpatched interpreter image.

pip documents [local-only installation](https://pip.pypa.io/en/stable/user_guide/) using no-index/find-links. The actual bundle must close and hash all required dependencies; an incomplete bundle or an online fallback is refused.

GitHub's [release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) describes tag-based assets and existing repository read access. Its [asset API](https://docs.github.com/en/rest/releases/assets) exposes individual content digests and read permissions. These capabilities support the proposed private channel; they do not establish a current release, permission to publish, or the integrity of unseen bytes.

Windows/macOS/Linux Tailscale client qualification remains the separately accepted matrix. This first installer command-host choice qualifies no native Windows/macOS Python CLI, Store installer, customer delivery path, hosted integration or real target.

## Decision requested

Accept the proposed internal runtime/channel/names for source preparation, or specify revisions. This selects source architecture and future qualification inputs only. T012 still needs actual source acceptance evidence and independent authentication/default verification. T026 still needs real deterministic build, artifact identities, current release authority and actual source/CI/readback.

No artifact is published or installed by this choice. No credential, repository visibility, billing setting, runner dispatch, paid resource, enrollment or Q1–Q5 gate changes. All three PRs remain draft.
