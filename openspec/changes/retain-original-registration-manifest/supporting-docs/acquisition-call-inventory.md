# Proposed acquisition call inventory

This is an explicit source inventory and derivation, not an executed runtime trace.
The frozen parent policy and its measured handoff/cleanup evidence are unchanged.

| Work | Network/credential cost | Retention and authority |
| --- | --- | --- |
| Existing primary register + independent ack-stage | Existing calls only; no added inventory | Capture actual descriptor/provenance in existing original start-consumed transaction |
| New runner POST /v2/registration/claim | One prepaid RPC; zero nested network, provider, signing, mint or credential observations | Controller validates its original private store and consumes one original launch row; bounded local transactions keep original clock/identity rules |
| Existing selected handoff |12+2N physical private units, unchanged fixed nested prepayment | Original actual-run authorities and full admission remain mandatory |
| Existing original cleanup plus audit |2+5N, max17, unchanged | Separate original scope/authorization; no claim reset |
| Existing authorized audit-only |1+N, max4, unchanged | No mutation replay |

Thus acquisition plus handoff is13+2N: N1=15, N2=17, N3=19. The added1 is a planned
transport, not a measured result or hidden callback. No extra RPC is credited as
local work; no credential or provider query may be introduced inside the handler.
Capture/claim identity/SQLite/high-water work is separately measured against the
existing one-second transaction and original operation windows, never treated as
unbounded free work. Complete actual source callbacks/transport must be counted.

The actual runner-local proof, all qualification observations and cleanup still
must fit qualification39 and their original distinct scopes, pools and deadlines.
This document does not prove that fit and supplies no exception. Any additional
work, allocation conflict or deadline/body mismatch stops implementation for a
further governed correction. Preserve ordinary/private12 and old policy refusals.
