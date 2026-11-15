# Evidence model
Status: draft

The source inventory maps tracked paths to production/test roles and source
digests. Foreign gitlinks are provider dependencies, not root-owned analysis
files. Coverage reports retain real executable lines, branches and hit counts,
including zero-hit files. A report receipt binds source revision, inventory,
test report and coverage digest. A stale revision, missing source, unresolvable
path or absent measurement is refusal, never an empty successful report.

Sonar readback binds analysis ID and source revision to the unchanged manual
reference, gate/profile identities and every computed condition. Historical
issues and original driver/verdict digests remain separate dated evidence.
Operating fingerprints and session identities prove preservation; unrelated
same-branch descendant progress is retained rather than reset.
