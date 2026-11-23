# Historical drafting context and actual reproducibility inputs

Status: historical context, not a source derivation/reader pin.
Date: 2026-11-23, America/La_Paz

The earlier local draft checkpoints viewed during preparation were factory
`afb20ce1df21199e75550e48732b56ee67069c51` and adapter
`b39feb3a5e9c30f25b28eb55751beb2ad4ff3e87`. These complete identities are
retained as historical context. Neither commit label is consulted by the
inventory deriver or claimed to regenerate its current proposed model.
The new graph/schedule is literal source in the current candidate deriver.

The machine inventory records the actual baseline input files by SHA256. Default
offline derivation checks the retained canonical fixtures against their recorded
hashes/sizes and recomputes the model; it does not claim to run the baseline
parsers. The explicit `--adapter-root` option verifies all five parser/fixture/
evidence/provider/namespace inputs before importing the actual unchanged
parsers. Both modes emit the full result for byte-for-byte comparison.
There is no factory-source checkout/read under the historical draft label.
Repository/source acceptance and authentication remain separate from these hashes.

Initial PR CI correctly rejected the old unused `basis.factory` field as an
undeclared local commit derivation site. The correction removes unused draft
commit labels from the machine basis/deriver together and retains both complete
identities here under the existing Markdown governance-context convention.
It does not shorten/split hashes, exempt a genuine derivation input, modify the
shared reachability reader, add an exception or weaken any test/gate.
The source hashes, modeled values and synthetic fixture measurements are retained.
