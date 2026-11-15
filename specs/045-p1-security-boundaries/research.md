# P1 repair research
Status: draft

## Privileged Python dependency decision
The existing reusable CI cryptography>=41,<46 range resolves to 45.0.7.
Upstream advisories GHSA-p423-j2cm-9vmq and GHSA-r6ph-v2qm-q3c2
identify affected versions including that release, with fixes in 46.0.7 and
46.0.5 respectively. The new CI-only lock instead uses the existing provider
runtime pin cryptography==50.0.0. The runtime lock and Opsx developer
requirements remain unchanged. Pinned Opsx preflight behavior must be checked
under the isolated fixed CI environment before landing.

Sources:
- https://github.com/pyca/cryptography/security/advisories/GHSA-p423-j2cm-9vmq
- https://github.com/pyca/cryptography/security/advisories/GHSA-r6ph-v2qm-q3c2

## Lifecycle-free worker CLI
The current official npm wrapper 2.1.325 has postinstall linking/copying its
platform binary into a stub. Simply suppressing that hook breaks the command.
The official Linux x64 platform package is standalone, has no install script
or dependency subtree, and can be integrity-locked and directly exposed as
claude on the existing Ubuntu x64 fallback runner. Npm ci stays script-free.
A fresh isolated home/no inherited credentials and version assertion are part
of installation acceptance; local network-disabled acceptance follows.

Sources:
- https://code.claude.com/docs/en/setup
- https://docs.npmjs.com/cli/v12/commands/npm-ci/
- Official npm registry manifests and package bytes at 2.1.325, inspected
  without lifecycle execution.
