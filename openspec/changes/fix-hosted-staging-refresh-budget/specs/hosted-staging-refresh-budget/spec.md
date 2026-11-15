## Purpose

Define a bounded protected-staging refresh across durable cleanup registration
while retaining complete current authority, original time and single-start scope.

## ADDED Requirements

### Requirement: Complete protected observations bracket registration

Protected staging SHALL perform one complete current observation before any
reservation and another after independently acknowledged cleanup registration
and before opening the start request. Both SHALL authenticate the same selected
plan, actual first run/attempt, eligible original-human review, source/control/
hold, current operator context and protection. A failed refresh SHALL preserve
cleanup ownership without worker execution or a replacement start.

#### Scenario: Authority changes while registration blocks

- **WHEN** hold, source, control, context, review, run or protection changes during registration
- **THEN** fresh independent observations refuse before the one worker start

#### Scenario: Complete current authority survives registration

- **WHEN** both full observations and the independent grant/lease remain valid
- **THEN** exactly one bounded measured inert launch is eligible

### Requirement: Staging has an explicit bounded shared allocation

Only trusted protected-staging entry SHALL select on a fresh decision at most two
complete observations, eight correlation reads, six protection reads, eight
source reads, four control reads, twenty-six total GitHub reads and sixteen
private operations. Each correlation reader SHALL retain at most four requests;
each protection observation SHALL retain at most two bounded policy pages.
Ordinary admission SHALL retain 3/13 and private twelve; accepted finalization
SHALL retain six/18/28 and private twelve. ARM/key limits SHALL remain 24/3.

#### Scenario: Observation or reader allocation exhausted

- **WHEN** a third observation, fifth request through one reader, ninth aggregate correlation request or any group/total/private maximum would be exceeded
- **THEN** refusal occurs before credentials or I/O without a new ledger or stale reuse

#### Scenario: A worker or existing decision requests broader accounting

- **WHEN** untrusted input, late upgrade, reconstruction, join or counter regression attempts to change authority
- **THEN** no additional budget is obtained and ordinary/finalization rules remain unchanged

### Requirement: Original time and earliest expiry reach the host

Both observations and all clients SHALL retain the same original ten-second wall
and monotonic decision, earliest case/grant/lease/source expiry and five-second
connect bound. The start request SHALL carry an earlier expiry found by the
second observation. No callback, polling response or operation SHALL renew it.

#### Scenario: Registration or second observation expires

- **WHEN** either original clock fails or a source/hold/context expiry becomes earlier
- **THEN** the request refuses or reaches the host with that earlier bound and no execution after expiry

### Requirement: Source candidate and operational authority remain distinct

The amendment SHALL preserve v1/default refusal, neutral contracts/pins and the
protected workflow graph. Status recovery SHALL remain read-only, at most six
reads over sixty seconds and earlier authority; no source qualification SHALL
commission setup, dispatch or later runtime tasks.

#### Scenario: Isolated source qualification succeeds

- **WHEN** local and hosted candidate checks pass
- **THEN** owner source ratification and T012S-V/T013 operational gates remain separate
