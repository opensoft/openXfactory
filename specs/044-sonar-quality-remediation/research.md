# Research decisions
Status: draft

- Automatic Sonar analysis cannot import coverage. Use CI in the same project,
  preserving its reference, history, profiles and six-condition gate.
- Existing organization SONAR_TOKEN visibility is all repositories; no new
  credential publication, access grant or billing change is needed.
- All owned Python lies in five source roots plus root tests. Conservatively
  measure all five roots. Genuine extra tests are the avatar experiment
  conftest/tests and two private-connectivity test modules; do not classify
  all historical specs or evidence as tests.
- The only surviving JavaScript source predates the September baseline. It
  remains analyzed; no artificial LCOV is produced.
- Coverage 7.16.2 supports process-start and subprocess instrumentation.
  Installation is isolated in the bench for measurement and ephemeral CI.
  Namespace modules and zero-hit production files must remain visible.
- Source S8707 guidance requires canonical CLI path containment beneath the
  invocation working directory. Private state has its own declared root and
  fixed console filename, plus owner/mode/descriptor checks.
- Git operand hardening uses positive ref validation, end-of-options and a
  single full hexadecimal commit result. Do not invent an exploit from old
  probes that already refuse.
- The maintained browser replay driver uses asserts for security checks,
  which optimization removes. Replace them with explicit fail-closed checks.
  Preserve every historical run receipt and its original driver preimage.
- The sealed validator can use its read-only judged mount as CWD while
  retaining private tmpfs scratch and all existing containment options.
- Flagged source files are not closed release inventory members. Separate
  analysis requirements do not change the two existing runtime lock members.

Sources: [Python coverage](https://docs.sonarsource.com/sonarqube-cloud/analyzing-source-code/test-coverage/python-test-coverage),
[source/test scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope),
[coverage subprocess configuration](https://coverage.readthedocs.io/en/7.16.2/config.html#run-patch).
