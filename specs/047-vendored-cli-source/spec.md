# Verified supplied CLI installation

Implementation repair of the existing --tarball contract and the neutral spec
leg's vendored-artifact ruling, surfaced by hosted review of openWallet-spec #12.
The exact supplied authenticated CLI bytes must be the install source even when
npm's cache is cold. SHA-512, corroborating checksum, unchanged lockfile closure,
operator/profile boundaries, no lifecycle scripts and all cache checks remain.
Authorized by Brett Heap's openXwallet #73 repair instruction on 2026-11-16.
