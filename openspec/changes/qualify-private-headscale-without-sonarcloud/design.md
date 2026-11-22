# Design for the private Headscale release gate

Status: draft

## Context

The current autonomy requirement retains Sonar conditions for protected source. Apply the owner's direction only after the exact private T023 amendment is accepted. Existing protected main evidence remains valid. T023 already has an exact source census, real owner qualification, and an offline coverage rehearsal that includes zero-hit modules.

## Goals / Non-Goals

**Goals**
Qualify the private package with evaluated checks under existing capacity. Preserve the claims and boundaries that downstream installer and hosted consumers rely on.

**Non-Goals**
The public coordinator, provider administration, hosted services, package activation, QA migration, and rollout authorization sit outside this amendment.

## Decisions

### Source gate

Use the existing credential-free package qualification lane as the producer. Keep the current guard suite and the independent release inventory. Pin the tested toolchain and reconstruct the eligible source, changed-code baseline, exact collected test identities, and actual execution results from Git and CI. Require the coverage file set to include all eligible MAIN Python paths, including zero-hit paths. Fail on missing, duplicate, skipped, stale, or substituted evidence.

Before C-01 approval, review every currently configured source-quality criterion against a proposed local control. Include thresholds, baseline, actual analysis inputs, and refusal examples. A criterion with no proven replacement stays open until the affected owner accepts an explicit disposition. A coverage report alone cannot satisfy security, maintainability or duplication criteria. Select and pin tools only after exact file and tool review. Enforce the no-spend boundary for CI compute and artifact storage.

### Scope and custody

Apply the decision only to the T023 source and release of opensoft/Headscale-Install. Keep private source, detailed findings, and raw coverage in its approved custody. The coordinator consumes exact hashes and verified result summaries. Preserve package and provider history, including the cancelled analysis and #1346's original source proposal. Record any future disposition of that draft through its own review.

### Evidence and release

The two predecessor capabilities still live in active ratified changes. Archive this amendment after those deltas are in the canonical specs. The sequencing declaration preserves their order.

Use the existing L/E C-01 refinement and definition refresh route for any proposed file additions. Freeze the whole Feature 043 definition before implementation, preserve task ownership and dependencies, and qualify coordinator source proof on protected main. Independently accept the actual owner output and run default verification before publication. Verify immutable release readback before dependent tasks consume the pin. Q0 through Q5 continue to govern their respective decisions.

## Risks / Trade-offs

Local metrics can disagree with the previous provider. The crosswalk and known-bad cases must demonstrate what each selected check stands for. A missing criterion or unavailable outcome blocks release. Treat changed-source measures as valid only for the recorded base and reviewed candidate. Keep the existing private plan and protected coordinator conditions intact.
