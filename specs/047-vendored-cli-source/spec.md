# Verified supplied CLI installation

Implementation repair of the existing --tarball contract and the neutral spec
leg's vendored-artifact ruling, surfaced by hosted review of openWallet-spec #12.
The exact supplied authenticated CLI bytes must be the install source even when
npm's cache is cold. SHA-512, corroborating checksum, unchanged lockfile closure,
operator/profile boundaries, no lifecycle scripts and all cache checks remain.
Authorized by Brett Heap's openXwallet #73 repair instruction on 2026-11-16.

## Bounded shared-consumer amendment (2026-11-16 America/La_Paz)

The openXwallet full-main scan exposes duplicate canonical consumer copies.
Preserve existing neutral-product-pin semantics while permitting one visible
implementation to serve an explicitly bound consumer. The verifier and installer
entrypoints accept an internal keyword-only consumer_root context. This is not a
model-selected CLI flag. It selects the default local pin and default validation
repository together; explicit operator pin configuration retains its precedence.
Standalone defaults, all refusal ordering and cache/artifact/lock checks remain.
Do not mutate ROOT/PIN_PATH globals or hide code in opaque artifacts. Consumers
must verify their declared shared implementation and test actual transports in
addition to every existing provider assertion. This is implementation maintenance
under Brett Heap's authorized openXwallet #73 full-main gate repair, whose bounded
OpenSpec amendment is in the consumer's restore-wallet-sonar-main change.
