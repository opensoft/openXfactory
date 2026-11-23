# Complete proposed first-pilot call inventory

Status: source schedule, not full runtime qualification. Date: 2026-11-23 America/La_Paz.

## Selected scope

Three VMs, three OS disks, three NICs, one control public IP, one VNet and three
role-specific NSGs give 14 ephemeral resources and 16 dependency edges. NSG names
are nsg-wallet-mfa-{control,gate,worker}-qa-01. Each NSG depends on its own NIC and
the VNet; VNet depends on all three NICs; control IP on control NIC; each disk/NIC
on its VM. Three subnets are VNet properties, never separate delete targets.
The [machine record](call-inventory.json) fixes every prospective path, dependency
and preserved scope slot. These are planning names, not deployed IDs or a grant.

Twelve retained ARM observation slots cover the two retained disks, managed image,
vault, evidence storage, watchdog function/plan/storage/identity and three parent
RGs. Three protected-state slots cover permanent namespace, registration/action
and runtime authority/replay state. All actual issued credential handles must be
registered (maximum16); missing/unsupported revocation/refusal evidence prevents
complete. Runtime/P06 retirement keeps its own original grants; this policy grants
no new credential-revocation API or fresh signing use. P07 observes those outcomes.

## Every planned call centre

Columns count actual attempted exchanges or physical state calls, not semantic
successes. The façade line charges the separate RPC in addition to each backend
call. Existing per-kind costs are a conservative sum of measured P03 controls;
new orchestration lines are explicit proposed bounds. They are not fabricated
measurements of a P07 service that has not been implemented.

### Registration

| Call centre | Private | ARM | Namespace | Journal | Basis |
| --- | ---: | ---: | ---: | ---: | --- |
| selected authority and source | 8 | 0 | 0 | 0 | proposed schedule |
| namespace exact-set inspection | 0 | 0 | 28 | 0 | proposed schedule |
| one registration claim and acknowledged readback | 0 | 0 | 0 | 6 | proposed schedule |
| P02 reservation sensitivity allowance; no authorization to rerun P02 | 0 | 0 | 17 | 0 | existing source formula; separately owned P02 normally outside P07 |
| genuine run-link registration | 6 | 0 | 28 | 4 | proposed schedule |
| authenticated state-facade exchanges, one per modeled namespace/journal backend call | 83 | 0 | 0 | 0 | proposed conservative remote-facade schedule; backend calls remain separately counted |
| Modeled total | 97 | 0 | 73 | 10 | Proposed schedule |
| Selected hard cap | 128 | 0 | 128 | 32 | Independently enforced, no borrowing |

### Cleanup

| Call centre | Private | ARM | Namespace | Journal | Basis |
| --- | ---: | ---: | ---: | ---: | --- |
| close write/run admission | 4 | 0 | 0 | 4 | proposed schedule |
| per-kind retirement core | 142 | 58 | 228 | 0 | conservative sum of measured old per-resource costs; historical receipt-cache reuse can only lower this line |
| distinct historic creation terminal receipts | 14 | 0 | 0 | 0 | existing source upper bound |
| at most three original-create and three original-delete polls per resource | 84 | 84 | 0 | 0 | proposed finite original-operation schedule, never a resend |
| uncertain conditional-write read-only reloads | 0 | 0 | 28 | 0 | existing source upper bound: one reload per each of two transitions |
| same-owner original-state reconstruction | 0 | 0 | 56 | 28 | proposed schedule |
| new action/terminal bookkeeping | 0 | 0 | 0 | 64 | proposed schedule |
| owner plus at most three duplicate trigger deliveries | 4 | 0 | 0 | 12 | proposed schedule |
| two current outcome reads for at most sixteen actual registered credentials | 32 | 0 | 0 | 0 | proposed schedule |
| authenticated state-facade exchanges, one per modeled namespace/journal backend call | 420 | 0 | 0 | 0 | proposed conservative remote-facade schedule; backend calls remain separately counted |
| Modeled total | 700 | 142 | 312 | 108 | Proposed schedule |
| Selected hard cap | 768 | 160 | 512 | 128 | Independently enforced, no borrowing |

### Observation

| Call centre | Private | ARM | Namespace | Journal | Basis |
| --- | ---: | ---: | ---: | ---: | --- |
| independent current resource absence | 14 | 14 | 28 | 0 | proposed schedule |
| twelve retained ARM objects and three protected-state objects | 12 | 12 | 6 | 0 | proposed schedule |
| independent current refusal evidence for actual registered credentials | 16 | 0 | 0 | 0 | proposed schedule |
| current observer identity and authority | 4 | 0 | 0 | 0 | proposed schedule |
| original operation and exact-set crosscheck | 14 | 0 | 28 | 0 | proposed schedule |
| immutable final result and independent audit | 4 | 0 | 0 | 4 | proposed schedule |
| authenticated state-facade exchanges, one per modeled namespace/journal backend call | 66 | 0 | 0 | 0 | proposed conservative remote-facade schedule; backend calls remain separately counted |
| Modeled total | 130 | 26 | 62 | 4 | Proposed schedule |
| Selected hard cap | 192 | 48 | 128 | 32 | Independently enforced, no borrowing |

## Byte and clock checks

The unchanged parsers accept the complete synthetic 14-resource records:

| Record | Complete canonical bytes |
| --- | ---: |
| reservation | 8056 |
| provisioned | 9855 |
| final_link | 716 |
| setup_receipt | 4720 |
| run_receipt | 5908 |

All fit the unchanged16,384-byte cap. Fixture refs/incarnations are explicitly
synthetic; this is parser/serialization compatibility, not service provenance.
All-maximal Ref/path strings are not guaranteed to fit; oversize input refuses.

The [policy](accounting-policy.md) selects 30-second original registration
transactions, one300-second original cleanup, one separately authorized60-second
read-only observation, <=10-second calls and16MiB total application bytes partitioned
1/12/3MiB. Parent approval/original cleanup deadline always clips these maxima.
No new UTC window or live timing guarantee exists. Old proof/readback limits stay.

## Reproduction and outstanding qualification

Run the source-only [deriver](derive-inventory.py) with the openXwallet checkout
as --adapter-root, using its existing locked test environment. It imports unchanged
closed parsers and pure planning fixture helpers, makes no network/provider call,
prints the JSON inventory and writes no files. Compare its complete output with
call-inventory.json. The small earlier real-clock attempt remains a retained fixture
diagnostic; no failed run is promoted to a new full positive.

Existing six-kind scope/counter measurements remain in [eligibility](eligibility.md).
This full source schedule resolves which calls/graphs/pools must be implemented;
actual physical accounting, timing, loss/ambiguity, worker exclusion, current
authenticated observation, privacy and independent teardown remain mandatory
post-ratification P07 gates. The full/native/hosted source qualification of old
runtime code is separate from those future runtime tests. No P07 task closes here.

Setup/dispatch unauthorized; feedback deferred; blocked writes unreplayed.
