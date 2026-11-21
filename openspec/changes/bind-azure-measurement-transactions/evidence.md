# P05 compatibility evidence

Status: draft; local eligibility diagnostics, not P05 completion.

The owner commissioned existing T013P05 isolated implementation/testing after
six preparation gates passed at adapter 9be62f196694103b6735df9237f511a87b20b10f.
Four actual process/TLS probes then passed in a disposable network-none container
with read-only source, nonroot UID, no supplementary groups/capabilities and no
privilege regain. The corrected run has no failures/errors/skips. Initial import
setup error and denied in-bench unshare are diagnostics, not passed cases.

- One complete canonical v1 measurement is 8,860 bytes: configuration 5,247 and
  policy 2,870. Independent approved-root/artifact/process derivation agrees.
- Actual pinned mTLS succeeds and explicitly denies the worker's distinct valid
  certificate with its corresponding valid request; an outage is not counted.
- The shared transport returns identical status/body for distinct nonce requests
  and an intentionally mismatched nonce response header. Its response API has
  only status/body, while the old observation client requires another wrapper
  and rejects the new operation. This proves an interface gap, not broken TLS.
- Actual disposable namespace absence and independent audit of 11 recorded
  process generations establish zero live processes; both exact owned scratch
  roots are removed. Logs/size/gap/JUnit/audit digests remain in local QA records.

Adapter compatibility evidence is committed at
de26e2b1d59d462e67f6d273ed432e5f627e4453; its
`specs/017-protected-runtime-qualification/p3-measurement-compatibility.md`
records the source seam and recommendation. The probes do not establish actual
local-manager/independent-observer administration, complete remote finalization
budget fit or any deployed/human/consumer acceptance. No v2 runtime exists.

The accepted P05 eligibility guard requires a governed factory/adapter amendment
before dependent implementation when the accepted interfaces cannot supply the
required correlation. This draft follows that guard and preserves the accepted
predecessor packet. Exact paired source acceptance remains ungranted. Ledger
publication provenance needs an actual PR number; no invented moved_by is used.
Setup/dispatch unauthorized; feedback deferred; blocked writes unreplayed.


## Local proposal validation checkpoint

All four planning artifacts are present. Strict validation accepts this candidate;
full current-main corpus is 151 items with one existing failure, while this
candidate is 152 items with the identical one failure. The unchanged baseline
failure is add-chain-attestation: its MODIFIED short-chain requirement omits the
current scenario "a tranche-two link does not exist yet". The baseline was rebuilt
from actual main f2ff6552e61323e872f1e0535e1a6cd7c4d6162b OpenSpec bytes and tested
with the same pinned CLI. That unrelated packet is not edited or waived here.
Dependency/sequence validation passes. Staged ledger-diff identifies the new
change's missing row; its generated provenance must use an actual published PR
number. No placeholder PR, manual ledger edit or publication success is claimed.
Required CI/local review and exact paired source acceptance remain pending.
