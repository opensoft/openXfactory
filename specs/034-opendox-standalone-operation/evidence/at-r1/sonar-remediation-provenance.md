# AT-R1 replay-driver maintenance provenance
Status: draft

This is a new maintenance record under
[remediate-sonar-findings-and-coverage](../../../../openspec/changes/remediate-sonar-findings-and-coverage/proposal.md),
authorized by Brett Heap on 2026-11-14. It changes the maintained replay
implementation, not the meaning of an earlier run.

The original driver and runner remain recoverable from immutable Git source.
The dated oracle verdicts, raw results, logs and screenshots retain their
original bytes. Their PASS claims concern their recorded source and execution,
not the maintained replacement below. No live AT-R1 replay is claimed by this
maintenance note; synthetic boundary tests are distinct from browser acceptance.

Original source commit: c283547b3490c5f3a29b0c800c5c63da361c7da7

Original driver SHA-256: e5ce78d648f17c9e3357514625784eb0906cbc990ff1208528a402e13bd5fd36

Original runner SHA-256: 8ba962fd7586ad476a6a464b0be4c102b415d078469ce4ed53ded2c03426bbb9

Maintained driver SHA-256: 0d6b4744154c327696d16bec7dd8ab33e8106b32229d746c9fc2b1469849b608

Maintained runner SHA-256: 8420fd30feee73c86bf27594180d41d35e4dcddb1ca8a010e98d90f1d0fc6383

Preflight helper SHA-256: f2deae220e66a171df7ac8494e3a77e3dafb2b3c3a7a2e17be39ca3182052b69

The maintained implementation confines output to the invocation root,
uses documented labels, validates the fixed private-copy identity with
descriptor-based owner/mode/type checks, and keeps all security checks under
optimized Python. Evidence writes are exclusive. The runner selects the
private output invocation and refuses an existing evidence directory before
writing logs. The redundant step assignment is removed; event/check meanings
and the independent product oracle are retained.

The original implementation's invalid-mode rejection was checked directly:
its security assertions reject normally but disappear under optimization.
The maintained helper rejects in both modes. This establishes a real
behavioral repair; it does not manufacture a fresh browser PASS or revise a
previous oracle verdict. Verification and actual-main Sonar/coverage results
belong in [feature 044 evidence](../../../044-sonar-quality-remediation/evidence.md).
