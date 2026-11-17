# Authentication review: Expanded T010 source CI

Status: record

Codex authenticated the exact expanded T010 source-only output under Brett Heap's recorded delegation. The original scope attestation preserves the earlier C-01 decision and its nine independent reviews. The separate output attestation binds the actual primary and Python 3.14 run, job, attempt, measured collection and source-step output.

The independently reviewed manifest is eaedb5ce459260b0033fabc5aaeed2abe41eb6a8. Its canonical content SHA-256 is c32b7c97e96a3cdde3bf1ac2c202eac854bede4b7119267062aff795c6197516. The original source-only custody decision and previous accepted bindings retain their exact references. The earlier Hosted Headscale authentication is preserved in [the T013 record](https://github.com/opensoft/openXfactory/blob/4d61a150fc44e472a4259792dd56b08a23da2cad/openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md).

This record covers source-output custody and admission. Program commissioning, publication, deployment, spend and Q0 through Q5 remain separately gated.

```json
{
  "schema": "043-delegated-source-authentication-v1",
  "decision": "accepted",
  "actor": "Codex",
  "accountable_owner": "Brett Heap",
  "reviewed_manifest": {
    "repository": "opensoft/openxfactory",
    "commit": "eaedb5ce459260b0033fabc5aaeed2abe41eb6a8",
    "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
    "sha256": "49518e60c523b500f5b01bdadf10368979063eae4b437e382c798382f346fffc"
  },
  "content_sha256": "c32b7c97e96a3cdde3bf1ac2c202eac854bede4b7119267062aff795c6197516",
  "attestation": {
    "repository": "opensoft/openxfactory",
    "commit": "169d16217150264ce7a5cc9a21ff055172376499",
    "path": "specs/043-private-connectivity-production/evidence/T010.json",
    "sha256": "97a01cdd2bc56897aee1e9e9898218aa5d260bc0562af3444de47dab7ac9b348"
  }
}
```
