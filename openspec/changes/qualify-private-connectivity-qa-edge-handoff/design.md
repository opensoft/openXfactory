# Design

## Context

At coordinator protected main `1caab36751dc1af729afe94ea1509c4fb9a09114`, the qualified producer generated the source-only C-01 receipt. The decision covers the twelve exact Tenant paths in candidate packet SHA-256 `a0568136f55cb062685543a52231d730c11339945e98686e76520713dcd667f7`. Nine distinct reviewers checked the exact packet. The original receipt SHA-256 is `8c5014ca959eefac1a6b79046e7ae09bef68b41c632e313449df89c0c54629b9`, with subject key `7fd81406012634e848a541cf48035344c93d7121c0c5e3b39c72b542580aacec`. The active reader refuses an exact but unregistered receipt.

## Goals / Non-Goals

**Goals:** Register this one exact, independently qualified source receipt and preserve prior evidence admission.

**Non-goals:** Definition activation, changes to delegated authority or review predicates, requalification of retained source bytes, modifying task files, source changes in Tenant, runtime effects and circulation of private-provider evidence.

## Decisions

### Resolve the exact immutable object and publication boundary

The local receipt commit is `5fe61d54f0d12b8e6e6dbe23f6716e96c3e7f105`. It descends from local T023 closure commits. It cannot justify bundling those commits into a QA source-resolution change. Before protected registration, independently review the usable commit path and make the exact approved source artifacts and receipt reachable from protected coordinator history. If the landing path requires reanchoring the evidence, preserve the reviewed decision, subject and review bodies, regenerate the attestor receipt with verified immutable references, and qualify the resulting receipt separately. Retain the original receipt as local history. Review public-coordinator disclosure separately and retain redacted summaries only. Avoid referencing a local-only object in a required CI or protected manifest.

The successful isolated reanchor preview starts directly from protected coordinator main and contains only five source-review files in its two commits. Its local receipt commit is `d227e91d22d52f90b54bc125719389cde5a8b609` and its receipt SHA-256 is `f23d7352b0fb5b5c0ecbc96f7b4b4fa42160e99d16c2ab1dcb0629d954ddff48`. It preserves the original decision and review bytes, their content hashes and the canonical subject. The preview verified that the original local receipt reference is refused when the register contains the reanchored exact reference. The commit and candidate patch remain local.

### Landing order required by observed reachability

Doc-health checks local pins against main ancestry or legitimate retained refs.
It does not count an earlier draft commit as protected reachability. The
isolated preview classified all six exact receipt-site references without
relaxing reachability. Only the existing delegation root and producer were
reachable from the real protected base. The other four references pointed to
the same draft materials commit. A read-only ancestry preview using that
materials commit as the proposed main revision found all six reachable.

1. Land the four separately reviewed source-material files in approved
   protected coordinator history. Declare their two protected-base references
   as current, repo-local pins. The declarations cover only
   `c01-scope-and-freeze.json` at `protected_head` and
   `protected-c01-attestor-preflight.json` at `actual_protected_base`.
   The scope record also uses the same key for the Tenant. Resolve each
   scope-record pin in its declared repository, with local reachability
   still required for the coordinator. Verify protected readback and current
   checks before producing a receipt pinned to the landed materials. Steps 2
   and 3 own the receipt declaration and registration.
2. Independently qualify the exact receipt on that protected base. Review
   and land the receipt and its single path-specific `commit` declaration
   together. The one required classifier path is
   `scripts/doc_health/pin_class.py` and its one focused regression path is
   `tests/doc-health/test_pin_reachability.py`. Preserve all other
   declarations and reject foreign or unreachable substitutions.
3. Register only the exact receipt proven reachable after step 2 and run the
   existing owner and E gates. Verify source receipt acceptance under the
   unchanged current definition before independently qualifying its
   successor freeze.

GitHub currently permits merge, squash and rebase. Use the actual protected
commit readback to select the proof refs. If a merge method changes local
commit identities, regenerate the receipt from the landed identical decision,
review and material bytes and independently qualify that exact result. No
retention-ref creation or policy exception is part of this proposal.

### Exact registry envelope

The only verifier change proposed here is one data entry in `specs/043-private-connectivity-production/verify-evidence.py`, inside `DELEGATED_ATTESTATIONS`. Its key is the actual canonical subject SHA-256. Its value is the exact coordinator repository, commit, path and SHA-256 of the independently qualified and reachable receipt. Keep the existing root, producer, verification predicates, all other entries, the default definition and accepted historical readers unchanged. Do not loosen reference equality or change the accepted repository list. Retain T007 as the verifier source owner and T010 as the existing CI/E proof owner. Update only the existing closed key inventory and exact path assertion in the associated `specs/043-private-connectivity-production/tests/test_evidence.py` test. Preserve every previous key, path, digest and producer assertion. The scratch preview demonstrated this exact regression requirement. A read-only census of the five immutable draft evidence paths found six uncovered commit sites, all in the exact receipt JSON above. The other four files had no uncovered sites. Protected admission therefore also needs a separately reviewed exact receipt-path and commit-field entry in the existing pin classifier and the corresponding focused reachability regression. Keep all six coordinator commit references subject to local reachability. No generic path, vocabulary or history suppression.

### Verification and later definition activation

Reproduce positive acceptance of the exact receipt and refusal of wrong commit, path, digest, subject, or revoked authorizing grant. Keep every existing record byte-identical. Run the affected source and CI-format regressions, validate pinned OpenSpec and doc-health, independently review the exact protected candidate and replay retained default T010, T017 and T023 controls against their admitted inputs. Preserve the original template and verification gates.

The candidate Feature 043 freeze `1e5d1a03b2d7cfab1bea57d838cbc080bc62b0951661b7508c901b432484ec11` is a separate step. A default-reader change must use separately authenticated actual E output and explicitly preserve the accepted pre-change reader and definition anchors. Verify the historical scope receipt under its original definition. Do not relabel its subject or extend a generic historic compatibility branch solely to pass the new definition.

## Risks / Trade-offs

- A local commit is immutable but lacks protected reachability. Prove the exact reviewed ancestry before using it in the register.
- Keeping registration separate from the definition refresh requires a staged landing and protects source/CI and task evidence from incidental definition changes.
- An authority scope can be valid while Q1 remains held. Record the independent release, custody, target and rollout prerequisites in their existing owners and gates.
