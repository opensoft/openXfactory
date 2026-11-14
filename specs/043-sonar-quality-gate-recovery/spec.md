# Sonar quality gate recovery

Status: draft

Restore computation for opensoft_openxFactory under the existing six-condition
Sonar way gate. Preserve original analysis/issue history, rules, thresholds,
source scope, billing, visibility and active session state. A computed failure
is reported truthfully and is not waived.

Acceptance: the earliest retained analysis is the fixed reference; a fresh
main analysis has a computed gate; each condition and any missing measurement
is explicit; preservation readback matches the operating baseline.
