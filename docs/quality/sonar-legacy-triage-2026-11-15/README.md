# Older Sonar finding triage — 2026-11-15

Status: draft
Kind: analysis and prioritized repair recommendations
Scope: the original 110 active pre-baseline BUG/VULNERABILITY records only

## Result and separation from gate acceptance

All 110 original issue keys were reconciled against a fresh read-only Sonar
main export at 2026-11-15T11:51:50Z and reviewed against source revision
`d6cd4083db0acb446f1089182b0be54044cfcbdc`. They occupy 45 files: 104 vulnerabilities and
6 bugs; the scanner severities are 10 BLOCKER, 1 CRITICAL and 99 MAJOR.
Their creation timestamps range from 2026-07-02 through 2026-09-08, before
the retained September 9 baseline. There were no missing, replaced or
additional issue keys in this scoped export.

Recommended priority is **40 P1, 59 P2 and 11 P3**. No P0 live incident is
established by this review. P1 means the next security repair queue, not a
claim that every row is remotely exploitable. Several rows share one input
or filesystem boundary and should be fixed together. A possible secret in
an intentional negative fixture needs immediate private provenance checking;
its liveness was not tested.

The [110-row index](findings.csv) is the authoritative membership list for
this triage. Each row retains the issue key, scanner rule/type/severity and
OPEN status, exact source location, enclosing function, supplied taint-source
locations, inspected controls, assessment/confidence, proposed fix,
acceptance criteria and governance constraints. Batch counts below partition
these same keys exactly once. Line numbers refer to the source revision above.

This report is separate from [feature 044's completed gate work](../../../specs/044-sonar-quality-remediation/tasks.md)
and its [original historical backlog snapshot](../../../specs/044-sonar-quality-remediation/legacy-sonar-backlog.md).
Neither record is rewritten. This report is not a ratified behavior change,
implementation plan, permission to mutate credentials, or a Sonar disposition.

At triage intake, actual main was `d6cd4083db0acb446f1089182b0be54044cfcbdc` and its
Sonar analysis was 5c8ac28f-06d6-4283-9049-24849adfaa79. The unchanged
Sonar way gate evaluated all six conditions OK: new-code reliability,
security and maintainability A; new coverage 88.6% (minimum 80%);
duplication 0.2% (maximum 3%); hotspots reviewed 100% (minimum 100%).
ignoredConditions was false. The manual baseline remained
d20bb52c-64fd-4090-986a-fd993f44ff86 at
2026-09-09T19:37:08-04:00, source
8480378acd806b112ebd0462e18a86a9026ab155. These are intake observations,
not acceptance of the older debt or a prediction about later main revisions.

## Priority and repair order

P0: credible live credential exposure, active exploitation or an immediately
demonstrated production incident; none established here. Escalate without
waiting for this queue if evidence changes.

P1: credential writes, privileged dependency execution, review/report/control
outputs or high-authority executable selection. Address the trust boundary
before polishing scanner presentation.

P2: local CLI input/output authority, residual installer hardening, command
operand contracts and bounded experiment defects. Require an explicit approved
root/executable policy for agent use; do not declare raw CLI access safe merely
because a human can already run commands.

P3: contextual analyzer warnings, existing guards needing proof, test clarity
and frozen artifact markup. Preserve behavior and evidence; these are not
automatic false-positive/accepted resolutions.

| Batch | Findings | Priorities | Repair family |
| --- | ---: | --- | --- |
| B01 | 3 | P1: 3 | Credential and browser profile boundaries |
| B02 | 8 | P1: 8 | Privileged workflow dependency installation |
| B03 | 36 | P1: 24, P2: 12 | Worker/report and review-control file boundaries |
| B04 | 6 | P1: 3, P2: 3 | Pinned OpenSpec CLI authority and operands |
| B05 | 26 | P2: 26 | Other local file-input/output boundaries |
| B06 | 10 | P1: 1, P2: 9 | Command operand and trusted executable contracts |
| B07 | 7 | P2: 7 | Other workflow dependency installation |
| B08 | 1 | P1: 1 | Credential-shaped negative fixture provenance |
| B09 | 1 | P2: 1 | Experiment media task lifetime |
| B10 | 1 | P2: 1 | Experiment dependency/build reproducibility |
| B11 | 3 | P3: 3 | Negative harness taint-context validation |
| B12 | 4 | P3: 4 | Test-oracle clarity and strength |
| B13 | 1 | P3: 1 | Existing import containment proof |
| B14 | 1 | P3: 1 | Trusted base/pinned-core checkout proof |
| B15 | 1 | P3: 1 | Required secondary SHA-1 compatibility |
| B16 | 1 | P3: 1 | Historical mockup markup |

Recommended sequence, with accountable owner roles rather than invented
assignments:

1. **B08 provenance check in parallel with B01 credential boundaries.**
   The credential owner privately establishes whether the negative-fixture
   literal was ever issued. Never copy it into an issue, test it against a
   provider or rotate/revoke active credentials during triage. If credible live
   exposure is found, escalate P0 through the credential owner's incident
   process. B01 belongs to the NLM/profile maintainer: names, store boundaries,
   link refusal, private atomic writes and lost-update protection must preserve
   account identity, cookies, metadata, unrelated profiles and active sessions.
2. **B02 privileged installers.** Workflow/review-authority maintainers first
   lock the prepare/finalize/review dependency sets and CLI closure. Finalize
   carries write privileges and installs a global unpinned fallback CLI with
   lifecycle execution enabled. Hash-pinned Python wheels and reviewed locked
   CLI installs must preserve worker/fallback behavior; deleting the fallback
   or turning off checks is not a repair. Then reuse the validated dependency
   policy in B07, retaining the existing --require-hashes control.
3. **B03 shared filesystem boundaries, then B04/B06 executable/operand
   authority.** Tooling and review/worker maintainers define separate approved
   input, output, policy and executable roots. Reuse a small tested safe-I/O
   primitive only where contracts match; the authorized root cannot simply be
   another unchecked model-supplied argument. Preserve valid multi-repository
   and operator-selected workflows. Reject links, resolved escapes and unsafe
   file types before I/O; handle parent replacement races where the threat
   model permits a concurrent adversary. Keep actual decision/refusal checks
   and strict validation. For B04 coordinate every byte-identical vendored
   verifier. For B06 prioritize the superuser-capable PostgreSQL template before
   ordinary fixed git operand proofs.
4. **B05 remaining CLI paths and B07 ordinary gate installers.** Apply the
   proven boundaries to corpus reads and report outputs, preserving missing/
   unreadable-baseline refusals and complete corpus participation. Split
   release-member work from ordinary helpers so a convenience fix cannot leave
   published inventories stale.
5. **B09/B10 offline experiment fixes.** The experiment maintainer retains and
   cleans up media drain tasks, then makes runtime/build artifact installation
   reproducible through the declared candidate/profile evidence process.
   Fake tracks and offline dependency checks suffice for development; no live
   provider calls or paid run is needed for triage.
6. **B11–B16 contextual proof and test clarity.** Reproduce intended guards,
   improve independent test observations and document protocol constraints.
   Correct maintained descendants of the archived mockup in their owning
   repository; leave the frozen original intact.

Small (one helper/test module), medium (several coupled scripts/workflow
tests), and large (vendor/release/consumer coordination) are planning bands,
not time estimates: B01 medium; B02 large; B03 large and split by CLI family;
B04 large; B05 medium per family, large for release members; B06 medium,
with PostgreSQL acceptance separate; B07 medium; B08 investigation first,
release/incident scope conditional; B09 small/medium; B10 medium;
B11–B15 small proof batches; B16 descendant-only small follow-up.

## Concrete evidence behind the order

Five disposable probes used extracted functions from the recorded source,
synthetic strings and files under a new temporary directory only:

| Probe | Observed result | Meaning and limit |
| --- | --- | --- |
| NLM profile parent segments | Computed profile directory escaped injected store/profiles | Missing profile-name/root boundary; no real store read |
| NLM absolute profile name | Computed profile directory escaped injected store/profiles | Absolute component overrides store construction; path computation only |
| NLM linked cookie file | Synthetic sentinel outside selected profile was overwritten | Write follows a link; all data stayed within temporary test directory |
| Dashboard linked report | Synthetic sentinel was appended through a link | Report sink is not covered by separate seal/archive containment helpers |
| OpenSpec option-shaped change ID | Constructed child argv contained validate, --help, --strict | Identifier validation missing; child CLI was not executed, so a gate bypass is not claimed |

These support targeted repairs, not exploitation of a live account, database,
workflow or deployment. No actual cookie, provider session, browser, token
exchange, notebook, build or business request was used.

Important contextual cases, already attached to every applicable index row:

- 76 findings are agentic CLI rules: 63 path, 12 argument and 1 executable/
  command finding. Sonar taint messages mention HTTP requests generically,
  but these sources are local CLI/evidence inputs; an internet endpoint was
  not established. An argv list prevents shell expansion, not executable
  selection or the child program interpreting option-shaped operands.
- Nine S2083 records track file content to file writes. Content being tainted
  does not prove it controls the destination. Three are controlled negative
  fixture rewrites in temporary harnesses (B11). Others need the independently
  observed selected-path/link boundary repair; the OpenSpec installer also has
  private scratch and verified lock bytes, while its explicit cache root needs
  separate ownership/link review. Do not dismiss all nine or remove fixtures.
- The lone secrets rule is in a declared IDB-R7 negative corpus fixture
  introduced with the identity-brokering release. Intent does not establish
  credential provenance. The value is deliberately absent from this report.
- The SHA-1 finding is secondary npm compatibility corroboration: SHA-512 is
  checked first and both mismatches refuse. Removing SHA-1 or SHA-512 checks
  would weaken integrity. Any later disposition needs narrow proof, not a
  global suppression or changed quality profile.
- The pull_request_target checkout warning points to a literal trusted-core
  commit with persist-credentials:false; it is not a checkout of a fork head.
  Retain base/pin trust and negative fork-execution tests. The separate unpinned
  installer in that job is real supply-chain work and remains P1.
- Review-lane repin already installs with --require-hashes. Its remaining
  warning concerns source-build execution, not absent hash locking. Enforce
  binary-only after verifying approved wheel availability; do not drop hashes.
- The experiment already has a fully version-pinned requirements.lock and
  documented --no-deps editable install. The scanner does not recognize that
  filename as its expected lock; remaining concerns are missing artifact hashes
  and an open-ended isolated build dependency. Renew candidate evidence if
  dependency/profile bytes change rather than rewriting a historical receipt.
- Repeated-call equality tests intentionally compare independent runs; they
  are not comparisons of one stored variable with itself. Strengthen expected
  semantic outcomes and clock-independence tests while preserving both calls.
- append_import already resolves and checks relative containment. Preserve
  the guard and verify race behavior rather than applying a blanket exemption.
  The archived mockup has a title in body instead of head and is frozen evidence.

## Future fix acceptance and release boundaries

Behavior, policy and workflow fixes require their own OpenSpec/Speckit work
before implementation. This report does not reopen or extend feature 044.

Each repair batch must keep a pre-change failing regression, valid-path control
and post-change result. Boundary tests must verify no modification or disclosure
outside authorized fixtures; an error after a write is insufficient. Model
inputs, reviewed operator configuration and authenticated workflow data have
different authority and cannot all be treated as one trusted string.

Run each changed child's complete declared validation in its owning bench.
Installer/workflow edits require actionlint, install-contract and actual
affected workflow checks. Release members in scripts/hermes_runtime_validation,
release CLIs and contract fixtures need a legitimate new release inventory and
coordinated consumer pins; never update old inventories by hand. Vendor changes
must remain byte-identical across consumers and coherent with their pins.

Before claiming a batch fixed: reconcile all its original keys, show source
and regression evidence, exact-head review/checks and actual-main Sonar
readback at the merged revision. Preserve the original IDs and dates even when
one root-cause fix closes many rows. A proposed contextual resolution requires
separate evidence and authorized review; this report changes no server status.

No new exclusions, source/test reclassification, check skipping, severity/rule
relaxation, baseline reset, profile changes, gate-threshold changes, entitlement/
billing changes or replacement of full scanning with partial scanning is part
of this plan. Existing skip distinctions and coverage instrumentation stay
intact.

## Method and auditability

Read-only issue export used legacy project key opensoft_openxFactory, main,
resolved=false and types=BUG,VULNERABILITY, including both API pages and taint
flows. This is deliberately not an all-code-smell or hotspot backlog. The
membership was checked against the retained original-110 issue-key snapshot,
then every row was inspected by sink/function and source/control family.
Proposed priorities are local planning metadata; every Sonar record remains OPEN.

Reconcile locally by reading findings.csv with Python csv.DictReader and
checking: exactly 110 unique issue_key values; types BUG=6 and
VULNERABILITY=104; priorities P1=40, P2=59, P3=11; 45 distinct paths;
16 batches; all statuses OPEN; and exact issue-key set equality with the
original historical backlog snapshot. Source locations and enclosing functions
were checked at `d6cd4083db0acb446f1089182b0be54044cfcbdc`. The raw export and preservation
receipts stay in operator-private evidence storage; only redacted, bounded
metadata and recommendations are published here.

The analysis used a separate maintenance worktree. Shared primary checkouts,
existing feature worktrees, staged/unstaged work, TMUX session/pane identities,
historical records and provider pins are preservation targets. No session
handoff, lane binding or active authentication state is modified by this report.

## Triage verification

The 110 unique IDs match both the original historical backlog and refreshed
live main export exactly. All per-row source lines/enclosing functions and new
local document links were checked; the credential-like fixture value is absent
from both published files. The staged diff passes whitespace validation.

In the declared Python bench, the existing code-surface and document-catalog
test suites passed: **196 passed**, no skips. The five isolated synthetic
probes above all produced their stated observations. These validate triage
evidence and document/governance compatibility; they do not certify a repair
of the older source findings.

Read-only Sonar recheck at 2026-11-15T12:14:12.1514757Z confirmed the same main
analysis/revision and all six green gate conditions, zero new bugs/vulnerabilities,
and the same 110 older OPEN records. Gate conditions, manual baseline and quality
profile configuration matched intake. Only shared profile last-used timestamps
advanced through concurrent analysis activity; no configuration was changed.

All seven primary checkout heads, statuses and staged/unstaged diff fingerprints
match intake. Existing worktree registrations remain present; this task added
only its isolated maintenance worktree. The separate active 043 branch advanced
independently from 2d1d8164 to bac4aede (also observed on PR #1310); it was not
reset, refreshed or modified by this work. All nine cloud-bench sessions/pane
identities and six py-bench sessions remain present. Completed feature 044 is
still clean at its published head; its evidence, provider pins and backlog
snapshot are unchanged. No code, workflow, contract, credential, Sonar status,
baseline, quality check or billing configuration was modified.
