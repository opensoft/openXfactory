# Tasks: Sonar quality gate recovery

Status: draft

- [x] T001 [O] Capture the missing definition, existing gate and earliest retained analysis; files: this feature's evidence; verify: authenticated readback and pinned strict change validation.
- [x] T002 [O] Restore the fixed historical reference without relaxing any gate input; files: service configuration and this feature's evidence; verify: exact analysis marker, unchanged gate/settings/history.
- [x] T003 [O] Observe fresh actual-main computation and record all conditions, measurements and limitations; files: evidence.md; verify: actual revision and computed verdict, no neutral/upload substitution.
- [x] T004 [O] Publish evidence and verify operating state preservation; files: README.md, tests/sequenced_after/corpus-ledger.yaml, this feature; verify: required exact-head checks, Codex receipt and preservation readback.

Implementation, service readback and preservation evidence are complete.
Current-head CI and Codex review remain mandatory publication guards on PR
#1315; no failed check may be bypassed to land this record.
