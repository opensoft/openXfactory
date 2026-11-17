# Production storage decision for the autonomous-run packet

Status: draft
Kind: financial-options
Prepared: 2026-11-17
Decision: no production spending exception accepted

## Current constraint and actual observation

Brett selected no new recurring production spend when preparing the final
authorization packet. This choice is not silently changed. The previously
accepted USD 10 QA storage envelope remains separate and grants no production
allowance.

Read-only provider/Kubernetes observation at 2026-11-17T04:04:03.848028Z found
25 bound QA volumes and 23 bound production volumes, no Available/Released PV,
and eighteen attached disks in each selected AKS node resource group. A scoped
subscription-wide Resource Graph check at 2026-11-17T04:14:13.159609Z found the
same eighteen disk resources per subscription and no unattached candidate.
No existing connectivity volume was identified. ARG is an index; any selected
resource would still need direct current-state verification before use.

This establishes no freely admissible dedicated state allocation. It does not
grant adoption of an unrelated bound volume or prove that all existing file
systems are full. Any proposed reuse needs its own actual ownership, capacity,
isolation, filesystem and non-destructive handoff evidence. EmptyDir/node-local
scratch and shared customer state are not substitutes for qualified durability.

## Two mutually exclusive financial choices

| Choice | Effect |
| --- | --- |
| Keep USD 0 new recurring production spend | Use only actually verified, already funded and specifically owned eligible capacity. Source/QA work can continue; production cannot activate if none is admitted. Do not create a billed production disk, tier, account or plan |
| Explicit storage-only exception, at most USD 20 per month before tax | Permit only the bounded state/backup quantities below after the final authorization and all operating gates; keep new compute, node pools, IPs, DNS zones, storage accounts, private endpoints and paid logging prohibited |

The second choice is proposed for review, not accepted by this document.
It cannot be selected by the agent in place of Brett's existing USD 0 choice.

## Minimal internal production allocation, if the exception is selected

- Four permanent 4-GiB Standard SSD LRS disks: two isolated managed Headscale
  state volumes, one product operation journal and one independently restored
  current entitlement/revocation store.
- Up to two additional 4-GiB quarantine/recovery targets; maximum six allocated
  disks at any time, with sequential drills.
- At most sixteen billed GB of Standard LRS snapshots and five billed GB of
  Hot LRS backup/evidence objects, including retained versions.
- At most 100,000 combined object writes/list/create operations and 100,000
  combined reads/other operations per billing month.
- Single-writer, ext4-compatible state; current authority never restored from
  old runtime snapshots. No adoption of unrelated data or default-class change.
- Existing regular production compute only. Actual CPU/memory/disk-attachment
  admission and compatible existing network/custody services remain required.

No resource is provisioned by selecting a financial envelope. The final
current C-03 target plan closes names, actor, channel, data and cleanup controls.

## Fresh retail observation and estimate

Official [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices)
rows were retrieved on 2026-11-17T04:18:46.142776+00:00 for Central US, USD,
Consumption pricing. Product filters were Standard SSD Managed Disks, Standard
HDD Managed Disks and General Block Blob v2. Exact returned rows and queries
are retained in the private preparation audit; no billing credentials were used.

| Meter | Observed retail rate | Conservative 31-day-month maximum |
| --- | --- | --- |
| E1 LRS Disk, 4 GiB | USD 0.30 / disk-month | 6 x 0.30 x 744/730 = USD 1.8346 |
| E4 LRS Disk Operations meter used for small Standard SSD transactions | USD 0.002 / 10,000 | 6 x 13,600 hourly billable transactions x 744 hours = USD 12.1421 |
| LRS Snapshots | USD 0.05 / used GB-month | 16 x 0.05 x 744/730 = USD 0.8154 |
| Hot LRS Data Stored, first tier | USD 0.0184 / GB-month | 5 x 0.0184 x 744/730 = USD 0.0938 |
| Hot LRS writes/list allowance | USD 0.05 / 10,000 writes, reserved at that rate | USD 0.5000 |
| Hot reads/other allowance | USD 0.004 / 10,000 reads, reserved at that rate | USD 0.0400 |
| Four permanent disks plus the same retained-capacity/operation reservations | | USD 10.7669 |
| Six disks reserved for the full month plus all listed reservations | | USD 15.4258 |
| Proposed storage-only ceiling | | USD 20 / month before tax |

The [managed-disk pricing page](https://azure.microsoft.com/en-us/pricing/details/managed-disks/)
lists the E1 LRS cap as 13,600 paid transactions per hour, also confirmed by
[Microsoft's billing-cap announcement](https://techcommunity.microsoft.com/blog/azurestorageblog/cost-saving-with-standard-ssd-billing-caps/3758792).
Its FAQ retains a contradictory 6,800 example; that older figure is not used
as a conservative provider cap. E1 Disk capacity is
not the cheaper E1 Disk Mount meter; shared-disk extra mounts are not used.
The current subscription's meter mapping, tax/discount treatment and actual
supported SKU/zone must be reconciled before admission. These are retail
estimates, not an invoice, automatic Azure spending cap or compatibility proof.

The calculation reserves 744 hours for a 31-day month and conservatively
scales the monthly disk/snapshot/object capacity rates by 744/730 as well.
Totals use unrounded inputs and displayed maxima round upward. The original
USD 9.3031/6,800-transaction draft estimate and its USD 10 financial question
are superseded; that estimate cannot justify a spending grant. The monthly storage envelope, if explicitly approved, supports the ongoing service after agent authority expires; Brett remains accountable for its custody, retention and recurring cost at handoff.

The ceiling excludes network transfer, new networking tiers and other services.
They are not implicitly free: use an actually eligible already funded/included
route or stop for a new decision. Azure budget alerts alone do not enforce the
ceiling. Admission caps, allocation/transaction/retention tracking, authorized
cleanup and readback must prevent new work before limits are exceeded.

## Authority boundary

All current PRs remain draft. No provisioning, operation, enrollment, publication
or Q0-Q5 acceptance is granted by this options packet. The final human ruling
must select the financial mode explicitly.
