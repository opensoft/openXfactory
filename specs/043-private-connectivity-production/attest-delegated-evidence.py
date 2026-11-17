#!/usr/bin/env python3
"""Bounded 043 source-evidence attestor; use only its qualified protected-base copy.

GET-only GitHub readback authenticates actual run/job/head/step/collection
metadata. It never runs a candidate command, provisions a target, mints a token,
or changes GitHub settings. Output is one review artifact on stdout; publishing
it and default task verification remain separate operations.
"""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

COORDINATOR = "opensoft/openxfactory"
FEATURE = "specs/043-private-connectivity-production"
MARKER = "PC043-SUITES "
OPTIONAL_SKIPPED = frozenset(("Sourcery review",))


class AttestationError(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise AttestationError(message)


def decode(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    def reject(_):
        raise AttestationError("non-finite JSON value")
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=reject)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class GitHub:
    def __init__(self, runner=subprocess.run):
        self.runner = runner

    def get(self, path, *, raw=False):
        need(path.startswith("repos/") and "\n" not in path and "#" not in path,
             "fixed GitHub GET resource required")
        env = {key: value for key, value in os.environ.items()
               if key not in ("GH_REPO", "GH_BROWSER", "GH_EDITOR", "GITHUB_API_URL")}
        env.update(GH_HOST="github.com", GH_PROMPT_DISABLED="1")
        result = self.runner(["gh", "api", "--hostname", "github.com", "--method", "GET", path],
                             capture_output=True, timeout=45, env=env, check=False)
        need(result.returncode == 0, "GitHub GET unavailable; no attestation issued")
        return result.stdout if raw else decode(result.stdout)

    def content(self, path, revision):
        need(re.fullmatch("[0-9a-f]{40}", revision), "exact protected-base revision required")
        value = self.get("repos/" + COORDINATOR + "/contents/" + quote(path, safe="/") + "?ref=" + revision)
        need(value.get("type") == "file" and value.get("encoding") == "base64",
             "protected-base file unavailable")
        return base64.b64decode(value["content"], validate=False)

    def qualified_base(self, revision):
        branch = self.get("repos/" + COORDINATOR + "/branches/main")
        need(branch.get("protected") is True and branch["commit"]["sha"] == revision,
             "selected base is not current protected main")
        checks = self.get("repos/" + COORDINATOR + "/commits/" + revision + "/check-runs?per_page=100")
        need(checks["total_count"] == len(checks["check_runs"]) and checks["total_count"] > 0,
             "complete actual protected-base check set required")
        names = {item["name"] for item in checks["check_runs"]}
        need({"pytest-suite", "doc-health-py314"} <= names, "actual required source lanes missing on main")
        for item in checks["check_runs"]:
            need(item["head_sha"] == revision and item["status"] == "completed"
                 and (item["conclusion"] == "success"
                      or item["name"] in OPTIONAL_SKIPPED and item["conclusion"] == "skipped"),
                 "protected-base checks not fully successful")
        sonar = [item for item in checks["check_runs"] if item["name"] == "sonar-analysis"]
        need(len(sonar) == 1, "evaluated main Sonar check missing")
        details = re.fullmatch(r"https://github[.]com/opensoft/openxfactory/actions/runs/[0-9]+/job/([0-9]+)",
                               sonar[0].get("details_url", ""), re.IGNORECASE)
        need(details is not None, "actual main Sonar job identity required")
        job = self.get("repos/" + COORDINATOR + "/actions/jobs/" + details.group(1))
        need(job["head_sha"] == revision and job["status"] == "completed" and job["conclusion"] == "success",
             "actual main Sonar job incomplete")
        required_steps = ("Analyze and wait for the existing quality gate",
                          "Verify evaluated conditions and exact main source", "Publish evaluated gate receipt")
        for name in required_steps:
            selected = [step for step in job["steps"] if step["name"] == name]
            need(len(selected) == 1 and selected[0]["conclusion"] == "success",
                 "main Sonar gate not actually evaluated")

    def observation(self, repository, run_id, job_id, suites):
        need(re.fullmatch("[a-z0-9_.-]+/[a-z0-9_.-]+", repository)
             and type(run_id) is int and run_id > 0 and type(job_id) is int and job_id > 0,
             "canonical owner and numeric provider IDs required")
        prefix = "repos/" + repository + "/actions/"
        run = self.get(prefix + "runs/" + str(run_id))
        job = self.get(prefix + "jobs/" + str(job_id))
        need(run["run_attempt"] == job["run_attempt"], "stale job attempt")
        logs = self.get(prefix + "jobs/" + str(job_id) + "/logs", raw=True)
        found = []
        for line in logs.decode("utf-8").splitlines():
            if MARKER in line:
                found.append(decode(line.split(MARKER, 1)[1]))
        need(len(found) == 1 and set(found[0]) == {"schema", "source_revision", "suites"}
             and found[0]["schema"] == "043-collected-suites-v1"
             and found[0]["source_revision"] == run["head_sha"] and found[0]["suites"] == suites,
             "actual measured source collection missing or mismatched")
        return dict(run=run, job=job, log_sha256=sha(logs), suites=suites)

    def secondary(self, revision, suites):
        value = self.get("repos/" + COORDINATOR
                         + "/actions/workflows/doc-health-py314.yml/runs?head_sha=" + revision + "&per_page=100")
        need(value["total_count"] == len(value["workflow_runs"]) and value["total_count"] > 0,
             "complete exact-head Python 3.14 run set required")
        runs = [item for item in value["workflow_runs"] if item["head_sha"] == revision]
        need(runs, "exact-head Python 3.14 lane missing")
        run = max(runs, key=lambda item: item["id"])
        need(run["status"] == "completed" and run["conclusion"] == "success",
             "latest exact-head Python 3.14 lane incomplete or failed")
        jobs = self.get("repos/" + COORDINATOR + "/actions/runs/" + str(run["id"])
                        + "/attempts/" + str(run["run_attempt"]) + "/jobs?per_page=100")
        need(jobs["total_count"] == len(jobs["jobs"]), "complete source job list required")
        selected = [job for job in jobs["jobs"] if job["name"] == "doc-health-py314"]
        need(len(selected) == 1, "one exact Python 3.14 source job required")
        return self.observation(COORDINATOR, run["id"], selected[0]["id"], suites)


def load_protected_reader(provider, base, script_path):
    provider.qualified_base(base)
    own = Path(script_path).read_bytes()
    companion = Path(script_path).with_name("verify-evidence.py")
    need(provider.content(FEATURE + "/attest-delegated-evidence.py", base) == own,
         "attestor is not the selected protected-base bytes")
    need(provider.content(FEATURE + "/verify-evidence.py", base) == companion.read_bytes(),
         "reader is not the selected protected-base bytes")
    spec = importlib.util.spec_from_file_location("qualified_043_reader", companion)
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)
    need(reader.DELEGATION_PRODUCER_REF is not None, "qualified producer activation pending")
    ref = reader.DELEGATION_PRODUCER_REF
    need(ref["repository"] == COORDINATOR and ref["path"] == FEATURE + "/attest-delegated-evidence.py"
         and ref["sha256"] == sha(own) and re.fullmatch("[0-9a-f]{40}", ref["commit"]),
         "qualified producer identity mismatch")
    comparison = provider.get("repos/" + COORDINATOR + "/compare/" + ref["commit"] + "..." + base)
    need(comparison["status"] in ("ahead", "identical")
         and comparison["merge_base_commit"]["sha"] == ref["commit"],
         "qualified producer is not protected-base history")
    return reader


def collect_expected(module, reader):
    expected = {}
    evidence = [reader.trust_reference]
    for key, binding in reader.trust["bindings"].items():
        if key in reader.trust.get("historical_controls", {}):
            continue
        record = reader.read(binding["record"], binding)
        output = reader.read(record["output"], binding)
        reader.ci(output, binding)
        need(type(output["exit_code"]) is int and output["exit_code"] == 0,
             "actual owner command did not pass")
        need(reader.now >= module.timestamp(output["ended_at"]), "future actual owner output")
        if set(record["output"]) == {"repository", "commit", "path", "sha256"}:
            evidence.append(record["output"])
        for suite, run in output["ci"].items():
            identity = (run["repository"].lower(), run["run_id"], run["job_id"], run["revision"])
            previous = expected.setdefault(identity, {}).setdefault(suite, run["collected"])
            need(previous == run["collected"], "inconsistent CI output collection")
    return expected, list({json.dumps(ref, sort_keys=True): ref for ref in evidence}.values())


def attest(module, tasks, store, manifest_ref, review_ref, provider, now):
    module.load_delegation_root(store, module.DELEGATION_ROOT_REF, now)
    module.require_delegation_producer(store, module.DELEGATION_PRODUCER_REF)
    reader = module.Verifier(tasks, store, manifest_ref, now=now, prepare=True)
    subject = dict(kind="source-authentication", definition=module.DEFINITION,
                   reviewed_manifest=manifest_ref, content_sha256=module.commissioning_digest(reader.trust))
    module.require_independent_review(store, review_ref, subject, now)
    expected, evidence = collect_expected(module, reader)
    observations = [provider.observation(repository, run_id, job_id, suites)
                    for (repository, run_id, job_id, _), suites in expected.items()]
    source = reader.trust["bindings"]["T010"]["source"]
    primary = next((item for item in observations
                    if item["run"]["repository"]["full_name"].lower() == COORDINATOR
                    and item["run"]["head_sha"] == source["revision"]), None)
    need(primary is not None, "actual primary source lane required")
    secondary_suites = {FEATURE + "/tests/" + name: primary["suites"][FEATURE + "/tests/" + name]
                        for name in ("test_source_roots.py", "test_delegated_evidence.py")}
    observations.append(provider.secondary(source["revision"], secondary_suites))
    module.require_provider_observations(observations, expected, source, now)
    return dict(schema="043-delegated-attestation-v1", actor="Codex", accountable_owner="Brett Heap",
                root=module.DELEGATION_ROOT_REF, producer=module.DELEGATION_PRODUCER_REF,
                reviewed_at=now.isoformat(), subject=subject, independent_review=review_ref,
                provider_observations=observations, evidence=evidence)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="independently selected, fully qualified protected main commit")
    parser.add_argument("--root", required=True, type=Path, help="coordinator data tree; never imported")
    parser.add_argument("--roots", required=True, type=Path, help="operator-supplied canonical local owner-root map")
    parser.add_argument("--manifest", required=True, help="immutable manifest reference as JSON")
    parser.add_argument("--independent-review", required=True, help="immutable nine-role review reference as JSON")
    args = parser.parse_args()
    provider = GitHub()
    module = load_protected_reader(provider, args.base, Path(__file__))
    roots = decode(args.roots.read_bytes())
    need(isinstance(roots, dict) and roots.get(COORDINATOR) == str(args.root),
         "independently selected coordinator root required")
    store = module.GitStore(roots)
    tasks = module.load_contract(args.root)
    result = attest(module, tasks, store, module.reference(decode(args.manifest)),
                    module.reference(decode(args.independent_review)), provider, datetime.now(timezone.utc))
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (AttestationError, ValueError, KeyError, OSError, subprocess.SubprocessError) as exc:
        # Never echo provider response bodies, credentials or private command output.
        reason = str(exc) if isinstance(exc, AttestationError) else type(exc).__name__
        print("043 delegated attestation refused: " + reason, file=sys.stderr)
        raise SystemExit(1)
