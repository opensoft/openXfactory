# Plan

Build tier: [O]. The shared scripts/validate-*-pin.py surface is governed.

Extract cohesive helpers for operand components, pin block parsing and folding,
disposition entries, report decoding, finding flattening and verified cache reuse.
Keep root/file-descriptor lifetime, mutation/validation order and diagnostics.
Use ASCII-scoped word tails and counted literal indentation in the same grammar.
Remove exception subclasses already caught by their retained base, and share the
package manifest filename. Drop only the unused internal report_dispositions
parameter; stale-disposition refusal remains at its unchanged caller boundary.

No lockfile, contract artifact, release digest, workflow, rule, coverage setting,
baseline, runtime budget or billing change is part of this maintenance. Historical
explicit-catch commentary remains identified as historical, with the current
ValueError catch still covering binascii.Error and UnicodeDecodeError.

Qualification:
- All214 existing OpenSpec CLI tests pass, before and after.
- A calibrated complete-file scan reproduces21 original findings, then reports
  zero at the corrected candidate.
- 91,035 finite differential probes agree:10,821 grammar reads,60,150 regex
  vectors (including Unicode rejection),6,000 disposition shapes,7,000 finding
  rows,6,000 report shapes,64 operand-root cases and1,000 integrity inputs.
  Comparison includes returns or exception class/text. These finite probes do
  not prove equivalence for every possible input.
- Full unchanged provider CI, independent review, publication and downstream
  authentication/coverage verification remain pending.

The extracted guard sites move their live doc-health Citation metadata and exact
line assertions together. Historical commentary stays identified as historical;
all guard text, optional-member partition and callable pure guard stay unchanged.
The pre-correction citation failures are retained as diagnostic evidence.
