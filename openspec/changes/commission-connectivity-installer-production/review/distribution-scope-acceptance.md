# Internal installer qualification channel acceptance

Status: record
Recorded: 2026-11-14

Brett answered the exact [reviewed distribution proposal](https://github.com/opensoft/openXfactory/blob/712452cb8c759fa547a9aead7c7d2b284885b13d/openspec/changes/commission-connectivity-installer-production/review/distribution-candidates.md):

> Approve this internal qualification channel (Recommended)

The accepted source/qualification choice is Ubuntu 24.04 LTS amd64 with CPython 3.12 in an isolated environment, with the exact security-patched runtime/build identities frozen before build/qualification. The command is xfactory-connectivity and distribution name xfactory-private-connectivity. The proposed internal channel is private xFactory-Installer GitHub owner-release wheel/sdist assets plus a complete hash-pinned offline dependency bundle. Existing repository access and normal owner release provenance/readback remain required; no repository is made public.

This selection is separate from the already accepted Tailscale client MSI/PKG/Debian channels. The existing private-connectivity adapter/setup scope and exact source files remain unchanged, with workstation-intake and Store work excluded. Actual installer source output must still be authenticated/default-verified for T012; actual release/build/CI/content/trust readback remains due at T026/T035.

The actual user record is timestamped 2026-11-14T17:25:29.544Z in session 01a1c061-ee6e-7e61-9db4-280a724e05c2, line 26306, individual raw-record SHA-256 ea17c6c998809e8fc1b580d6dc0917d7891febfd1ca66a08f83d7a1c9a95de4d (UTF-8 JSON record without line terminator). The question expressly selected source/qualification inputs only and kept actual publication, installation, customer delivery and execution behind their own gates.

The previously ratified owner/source-only custody policy remains unchanged. No artifact publication, target authority, credential, installation, enrollment, runner dispatch, paid resource, billing change, version/tag/pin operation, hosted integration or commercial offer is accepted by this choice. All three current PRs remain draft.
