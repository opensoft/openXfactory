#!/usr/bin/env python3
"""Read-only verifier for 043. Structural verification never grants acceptance.

The operator supplies PC_EVIDENCE_TRUST (commit:relative/path) and
PC_EVIDENCE_TRUST_SHA256 through an independently reviewed custody channel.
These are trust anchors, NOT receipt fields or discovered defaults. The pinned
manifest freezes bindings, owner repositories, actual commands/subchecks, scope,
authority, original outputs and history. Its reviewer must authenticate those
outputs and decisions. A hash or GitHub URL alone does not establish approval.
No production manifest is commissioned by this implementation.

PC_EVIDENCE_ROOTS is a machine-local JSON map of canonical owner aliases to
existing clones, for foreign Git-object reachability. No network calls occur.
Missing trust, objects, decisions or observations fail closed. This program
never executes the commands in evidence, writes files, or probes a target.
"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from datetime import datetime, timezone


FEATURE = "043-private-connectivity-production"
FEATURE_PATH = "specs/" + FEATURE
COORDINATOR = "opensoft/openxfactory"
HISTORICAL_CONTROL_ERROR = "unaccepted historical control"
T010_CUSTODY_SUCCESSOR = "93cf7d7f7b4e228220ca8d04f4cc351ac16c56a66f3722d4d214aebbca2918cc"
DEFINITION = T010_CUSTODY_SUCCESSOR
LEGACY_DEFINITION = "66db63ec98e366f141230d22e6e4e159916bb997f159916159dcc7b6ae3f32d0"
LEGACY_CONTROL_SHA256 = "0dc18a4053e07fd484534dcd4b572a5f8c6b72718b6901ac1323298d4ec7243e"
LEGACY_READER_SHA256 = "0ce860921467e94e942274905c45c99295a830a3f14b8a0b66ddb944103f697f"
# Closed source history accepted before this exact T018 scope refinement.
C37_DEFINITION = "c37f19af3ebe6340ce417286d54875f40a201f86e41d22077b676044f7f44431"
C37_READER = {
    "repository": COORDINATOR,
    "commit": "98a20eeeb6435f4bcd195fe86d2221e27fb3de5b",
    "path": "specs/043-private-connectivity-production/verify-evidence.py",
    "sha256": "2f7327b038f4ba54e3653b0f0247c18da87713220b2cba9ed11dc515407a597b"
}
C37_CONTROLS = {
    "source-ci": {
        "reference": {
            "repository": COORDINATOR,
            "commit": "698bf83671be642421fb28987c820fe36b49b0a6",
            "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
            "sha256": "31aa0576d1c9c0ac99ccf6faa14b038b0a74e985568ab5645f543d75de13bb35"
        },
        "content_sha256": "c8be9c1d56f7fd7dbbaca5ca4c3f416ae03f7e1855722fb4aa0e54e5a6f3ef54"
    },
    "package": {
        "reference": {
            "repository": COORDINATOR,
            "commit": "c4e380b43e27093a2a3b99264a3fb52a6cf36c21",
            "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
            "sha256": "902903efb19398d014ef2c84acd6afa227c0cc97ee4df87f5d9cecf56fd29816"
        },
        "content_sha256": "f9d89883516aa147f3b0054b7132f1f53b66bd948c2c5834b2d9a4cea3dd3332"
    }
}

# Exact accepted source history before the cut-validation scope refresh.
DEFINITION_2A46 = "2a46a5420c9f90f5ace72e8482b0fa0541b55f733bd6ad7a8e53ebb99215d796"
READER_2A46 = {
    "repository": COORDINATOR,
    "commit": "8ac068510936c97d21ace2b923ad00c0a6238b68",
    "path": "specs/043-private-connectivity-production/verify-evidence.py",
    "sha256": "e2aae8286af91d0ae04b99498da52ace1da69e3adfd0adc8df45437d8079ac6f"
}
CONTROLS_2A46 = {
    "source-ci": {
        "reference": {
            "repository": COORDINATOR,
            "commit": "8ac068510936c97d21ace2b923ad00c0a6238b68",
            "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
            "sha256": "e42735845944bb5c36d46a4648c56ab9bd4b0dfd82d4bc3a5b7128b08c6b89bf"
        },
        "content_sha256": "e49a5a8eb773dadd05ac345baf7eaf9ba5d019f6fb4d128580667a4b617577db"
    },
    "hosted": {
        "reference": {
            "repository": COORDINATOR,
            "commit": "1fb3a6a8188a4b051693ac2cd93920f4e69b0d0b",
            "path": "specs/043-private-connectivity-production/evidence/commissioning.json",
            "sha256": "02158d50df76a25eed4b1cd046bef3bf724aa21c0e9763b3352a02a60ac9a326"
        },
        "content_sha256": "f91b58db2fe5302a9c08e9fc2bafbeb3f9947ce4351dcadf5e450bd6eeb6bdc6"
    }
}

FIXED_REPOSITORIES = {"C": COORDINATOR, "L": "opensoft/headscale-install", "I": "opensoft/xfactory-installer",
                      "H": "opensoft/openxsoft-hosted-services"}
SCOPE_FIELDS = frozenset("run candidate profile customer site network domain environment target region offering phase offer wave".split())
REF_FIELDS = frozenset(("repository", "commit", "path", "sha256"))
INSTANCE_TASKS = frozenset(f"T{i:03}" for i in range(57, 65))
COMMISSIONING_PATH = FEATURE_PATH + "/evidence/commissioning.json"
AUTHENTICATION_PATH = "openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md"

# The custody transition keeps one accepted predecessor and one original T010 scope proof.
T010_CUSTODY_PREDECESSOR = {
    "reference": {
        "repository": COORDINATOR,
        "commit": "9da72c839c5904876d0ccdf0af4997ec5fb42eed",
        "path": COMMISSIONING_PATH,
        "sha256": "9493a7f106a0306bbb1e057a84b0673d9468f4b320f32cb507f5b062f5195248",
    },
    "definition": "281fdf8a64a6d3851a775d558bc95fcf2899d162bc6c2a615bdc88657fcc9421",
    "reader": {
        "repository": COORDINATOR,
        "commit": "9da72c839c5904876d0ccdf0af4997ec5fb42eed",
        "path": FEATURE_PATH + "/verify-evidence.py",
        "sha256": "87f2c99e7e6f481af1b2cc0d79e78d62e9cc105ca18c46a273cff5c2fe29ee9c",
    },
    "content_sha256": "c32b7c97e96a3cdde3bf1ac2c202eac854bede4b7119267062aff795c6197516",
}
T010_ORIGINAL_SCOPE_DECISION = "4f7060b31899c5b1a04452bd8b968edc42e9de04d47d6204287792c9c1e0cbcb"
T010_ORIGINAL_SCOPE_PROOF = {
    "repository": COORDINATOR,
    "commit": "5d82621d28fe94a9f0bef663015dcc8cd2f6d10f",
    "path": FEATURE_PATH + "/evidence/T010.json",
    "sha256": "8060207aca399a81340fb992271e1358b605f4d38bd6842721c154ef779f8619",
}


DELEGATION_ROOT_REF = {
    "repository": COORDINATOR,
    "commit": "d2528306ab6fe95c9235073f10c9150822b3f86e",
    "path": "openspec/changes/authorize-private-connectivity-internal-production/review/human-root-grant.json",
    "sha256": "57d5d91c35a7db3bf6030572841cd836137749aff4c27a29e8081d8d201704aa",
}
# Activation is a separate reviewed protected-base act. No environment or
# receipt field can supply a producer while this is None.
DELEGATION_PRODUCER_REF = {'repository': 'opensoft/openxfactory', 'commit': 'ba911daab0ed791641e19d7954f5b625a9b3c81c', 'path': 'specs/043-private-connectivity-production/attest-delegated-evidence.py', 'sha256': 'da4ab3aca3759eb4b9c2b97bfffb621351201d0b969305125d62f78097a1e5f5'}
# Only actual outputs independently qualified and landed on the protected base
# may enter this register. Producer activation alone grants no output authority.
# Key: canonical subject SHA-256. Value: exact whole immutable output reference.
DELEGATED_ATTESTATIONS = {
    "a8fe2c36d22fc1a08bdac7619aa84122ba23fa22d6728db5c7dccf19211aca2f": T010_ORIGINAL_SCOPE_PROOF,
    "ed53795c4d54152860abd38a15338449a24e3069dff3ec0483d66f741fbb2acd": {
        "commit": "169d16217150264ce7a5cc9a21ff055172376499",
        "path": "specs/043-private-connectivity-production/evidence/T010.json",
        "repository": "opensoft/openxfactory",
        "sha256": "97a01cdd2bc56897aee1e9e9898218aa5d260bc0562af3444de47dab7ac9b348"
    }
}


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def commissioning_digest(value):
    # The review pointer and mechanically derived inventory are control metadata.
    # Every binding, object, source, output and authority remains authenticated.
    return digest(canonical_json({key: item for key, item in value.items() if key not in ("review", "pin_inventory")}))


class EvidenceError(ValueError):
    """An evidence obligation was not met."""


def require(condition, message):
    if not condition:
        raise EvidenceError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def decode(data):
    def reject(value):
        raise EvidenceError("non-finite JSON value: " + value)
    try:
        result = json.loads(data, object_pairs_hook=pairs, parse_constant=reject)
        def inspect(value):
            if isinstance(value, float):
                require(math.isfinite(value), "non-finite JSON number")
            elif isinstance(value, dict):
                for child in value.values(): inspect(child)
            elif isinstance(value, list):
                for child in value: inspect(child)
        inspect(result)
        return result
    except (ValueError, UnicodeError) as exc:
        raise EvidenceError("invalid JSON: " + str(exc)) from exc


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), label + " must be text")
    return value


def relative(value):
    text(value, "path")
    path = PurePosixPath(value)
    require(not path.is_absolute() and "\\" not in value and ":" not in value
            and path.as_posix() == value and all(p not in (".", "..") for p in value.split("/")),
            "unsafe relative path")
    return value


def finite(value, label, minimum=0):
    require(type(value) in (int, float) and (type(value) is int or math.isfinite(value)) and value >= minimum,
            label + " must be finite and field-valid")
    return value


def timestamp(value):
    text(value, "timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        require(result.tzinfo is not None, "timestamp requires timezone")
        return result.astimezone(timezone.utc)
    except ValueError as exc:
        raise EvidenceError("invalid timestamp") from exc


def scope(value):
    require(isinstance(value, dict) and set(value) == SCOPE_FIELDS, "incomplete or unknown scope")
    for key, item in value.items():
        text(item, "scope " + key)
    return value


def reference(value):
    require(isinstance(value, dict) and set(value) == REF_FIELDS, "immutable reference required")
    text(value["repository"], "repository")
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value["repository"]), "invalid repository")
    require(isinstance(value["commit"], str) and re.fullmatch(r"[0-9a-f]{40}", value["commit"]), "exact commit required")
    require(isinstance(value["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", value["sha256"]), "exact SHA-256 required")
    relative(value["path"])
    return value


def canonical_origin(value):
    value = value.strip().removesuffix(".git").rstrip("/")
    for prefix in ("https://github.com/", "git@github.com:", "ssh://git@github.com/"):
        if value.startswith(prefix):
            value = value[len(prefix):]
            break
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value), "canonical GitHub origin required")
    return value.lower()


class GitStore:
    """Only fixed, local Git read operations; never execute an evidence command."""

    def __init__(self, roots):
        self.roots = {name.lower(): Path(root).resolve(strict=True) for name, root in roots.items()}
        for name, root in self.roots.items():
            require(canonical_origin(self.git(root, "config", "--get", "remote.origin.url").decode()) == name,
                    "owner root/origin mismatch")

    @staticmethod
    def git(root, *arguments):
        environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        environment.update(GIT_NO_LAZY_FETCH="1", GIT_TERMINAL_PROMPT="0", GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        result = subprocess.run(
            ["git", "--no-optional-locks", "--no-replace-objects", "--no-pager", "-C", str(root), *arguments],
            capture_output=True, check=False, env=environment,
        )
        require(result.returncode == 0, "local Git object or repository unavailable")
        return result.stdout

    def root(self, repository):
        require(repository.lower() in self.roots, "owner repository unavailable")
        return self.roots[repository.lower()]

    def blob(self, ref):
        reference(ref)
        root = self.root(ref["repository"])
        revision, path = ref["commit"], ref["path"]
        require(self.git(root, "cat-file", "-t", revision).strip() == b"commit", "reference is not a commit")
        # Walk every tree component; never follow a symlink or a gitlink.
        parts = path.split("/")
        for end in range(1, len(parts) + 1):
            name = "/".join(parts[:end])
            row = self.git(root, "ls-tree", "-z", revision, "--", name).split(b"\0")[0]
            header, separator, actual = row.partition(b"\t")
            require(separator and actual.decode() == name, "object path unavailable")
            mode = header.split()[0]
            require(mode in ((b"100644", b"100755") if end == len(parts) else (b"040000",)),
                    "symlink, gitlink or non-blob reference")
        data = self.git(root, "cat-file", "blob", revision + ":" + path)
        require(digest(data) == ref["sha256"], "immutable content digest mismatch")
        return data

    def changed(self, source):
        root = self.root(source["repository"])
        for field in ("base", "revision"):
            require(re.fullmatch(r"[0-9a-f]{40}", source[field]) is not None, "exact source commit required")
            require(self.git(root, "cat-file", "-t", source[field]).strip() == b"commit", "source is not commit")
        raw = self.git(root, "diff-tree", "-r", "--no-ext-diff", "--no-textconv", "--no-renames",
                       "--name-only", "-z", source["base"], source["revision"], "--")
        return {item.decode() for item in raw.split(b"\0") if item}


def load_contract(root):
    """Bind all 68 rows, command/file envelopes and 16 inputs to the T006 freeze."""
    feature = root / FEATURE_PATH
    def read(path):
        relative(path)
        target = feature / path
        require(target.resolve().is_relative_to(feature.resolve()) and not target.is_symlink(), "unsafe contract input")
        return target.read_bytes()
    return _load_contract(read, DEFINITION)


def _load_contract(read, definition):
    contract = read("contracts/task-evidence.md").decode("utf-8")
    task_text = read("tasks.md").decode("utf-8")
    body, marker, footer = contract.partition("\n## T005 review freeze")
    require(marker, "missing reviewed definition freeze")
    inputs = {}
    for path, expected in re.findall(r"^\| ([^|]+?) \| ([0-9a-f]{64}) \|$", footer, re.M):
        relative(path)
        data = body.encode() if path == "contracts/task-evidence.md" else read(path)
        inputs[path] = digest(data)
        require(inputs[path] == expected, "changed frozen contract input: " + path)
    rows = re.findall(r"^\| T\d{3} \|.*$", body, re.M)
    lines = re.findall(r"^- \[[ xX]\] T\d{3} .*$", task_text, re.M)
    frozen = {"inputs": inputs, "registry": rows,
              "tasks": [re.sub(r"^- \[[ xX]\]", "- [ ]", line) for line in lines]}
    require(len(inputs) == 16 and len(rows) == len(lines) == 68, "incomplete frozen registry")
    require(digest(json.dumps(frozen, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()) == definition,
            "unreviewed task/case/file/command definitions")
    tasks = {}
    for row, line in zip(rows, lines):
        task, owner, kind, deps, cases = [part.strip() for part in row.strip("|").split("|")]
        require(line.startswith("- [") and line[6:10] == task, "task order mismatch")
        files, command = line.split(" — files: ")[1].split(" — verify: ")
        tasks[task] = {"owner": owner, "class": kind, "dependencies": [] if deps == "none" else deps.split(", "),
                       "cases": cases.split(", "), "files": re.findall(r"`([^`]+)`", files),
                       "command": command.strip("`")}
    return tasks



def _same_reference(actual, expected):
    reference(actual)
    return {**actual, "repository": actual["repository"].lower()} == expected


def _pinned_blob(store, ref):
    raw = store.blob(reference(ref))
    require(isinstance(raw, bytes) and digest(raw) == ref["sha256"],
            "delegation immutable digest mismatch")
    return raw


def load_delegation_root(store, ref, at, *, revoked=()):
    require(_same_reference(ref, DELEGATION_ROOT_REF), "unaccepted delegation root")
    root = decode(_pinned_blob(store, DELEGATION_ROOT_REF))
    require(root["schema"] == "043-human-delegation-root-v1"
            and root["decision"] == "accepted" and root["human"] == "Brett Heap"
            and root["feature"] == FEATURE and root["customer"] == "Opensoft Inc"
            and root["delegate"]["actor"] == "Codex"
            and root["delegate"]["chat"] == "01a1c061-ee6e-7e61-9db4-280a724e05c2",
            "wrong human delegation root")
    require(isinstance(at, datetime) and at.tzinfo is not None and at.utcoffset() is not None,
            "aware delegation root decision time required")
    start, end = timestamp(root["approved_at"]), timestamp(root["expires_at"])
    require((end - start).total_seconds() == 30 * 24 * 60 * 60 and start <= at < end,
            "decision outside human-root validity")
    require(isinstance(revoked, (list, tuple, set, frozenset)) and root["id"] not in revoked,
            "delegation root revoked")
    policy = root["policy"]
    require(policy["repository"] == COORDINATOR
            and policy["commit"] == "a66cfe601407818dbd04f294bbaf92af15246e22"
            and len(policy["members"]) == 8, "wrong root policy")
    for member in policy["members"]:
        require(member["repository"] == COORDINATOR and member["commit"] == policy["commit"],
                "foreign root policy")
        _pinned_blob(store, member)
    return root


def require_delegation_producer(store, ref):
    require(DELEGATION_PRODUCER_REF is not None, "delegation producer is not activated")
    require(_same_reference(ref, DELEGATION_PRODUCER_REF)
            and ref["repository"].lower() == COORDINATOR
            and ref["path"] == FEATURE_PATH + "/attest-delegated-evidence.py",
            "unaccepted delegation producer")
    return _pinned_blob(store, DELEGATION_PRODUCER_REF)



REVIEW_ROLES = frozenset((
    "architecture", "performance", "security", "qa", "static", "contracts",
    "integrity", "reliability", "maintainability",
))


def require_independent_review(store, ref, subject, reviewed_at):
    review = decode(_pinned_blob(store, ref))
    require(set(review) == {"schema", "subject", "reviewed_at", "roles"}
            and review["schema"] == "043-independent-review-v1"
            and review["subject"] == subject, "independent review subject mismatch")
    require(timestamp(review["reviewed_at"]) <= reviewed_at, "independent review after decision")
    roles = review["roles"]
    require(isinstance(roles, dict) and set(roles) == REVIEW_ROLES, "nine independent review roles required")
    identities = set()
    for result in roles.values():
        require(isinstance(result, dict) and set(result) == {"reviewer", "verdict", "report"}
                and result["verdict"] == "clear", "unresolved independent review")
        identities.add(text(result["reviewer"], "independent reviewer"))
        text(result["report"], "actual independent review report")
    require(len(identities) == len(REVIEW_ROLES), "distinct independent reviewers required")


def ci_identity(repository, run_id, job_id, revision):
    require(canonical_origin(repository) == repository.lower()
            and type(run_id) is int and run_id > 0 and type(job_id) is int and job_id > 0
            and isinstance(revision, str) and re.fullmatch("[0-9a-f]{40}", revision),
            "invalid actual provider CI identity")
    return repository.lower(), run_id, job_id, revision


def require_provider_observations(observations, expected, source=None, reviewed_at=None):
    require(isinstance(observations, list), "provider observation list required")
    found = {}
    for observation in observations:
        require(isinstance(observation, dict)
                and set(observation) == {"run", "job", "log_sha256", "suites"}, "closed provider observation required")
        run, job = observation["run"], observation["job"]
        identity = ci_identity(run["repository"]["full_name"], run["id"], job["id"], run["head_sha"])
        require(identity not in found, "duplicate provider CI observation")
        require(job["run_id"] == run["id"] and job["head_sha"] == run["head_sha"]
                and run["run_attempt"] == job["run_attempt"]
                and run["status"] == job["status"] == "completed"
                and run["conclusion"] == job["conclusion"] == "success",
                "failed or mismatched actual provider run/job/head")
        require(isinstance(reviewed_at, datetime) and reviewed_at.tzinfo is not None
                and timestamp(run["created_at"]) <= timestamp(job["started_at"])
                <= timestamp(job["completed_at"]) <= timestamp(run["updated_at"]) <= reviewed_at,
                "actual provider completion must precede authentication")
        require(isinstance(job["steps"], list) and job["steps"]
                and any(step.get("conclusion") == "success" for step in job["steps"])
                and all(step.get("conclusion") in ("success", "skipped") for step in job["steps"]),
                "failed or absent actual provider steps")
        require(isinstance(observation["log_sha256"], str)
                and re.fullmatch("[0-9a-f]{64}", observation["log_sha256"]), "actual provider log digest required")
        require(isinstance(observation["suites"], dict) and observation["suites"]
                and all(type(count) is int and count > 0 for count in observation["suites"].values()),
                "actual provider collected suite counts required")
        found[identity] = observation
    extras = set(found) - set(expected)
    require(set(expected) <= set(found), "missing actual provider CI observation")
    if source is None:
        require(not extras, "unknown actual provider CI observation")
    else:
        matching = [item for identity, item in found.items()
                    if identity[0] == COORDINATOR and identity[3] == source["revision"]]
        lanes = {}
        for item in matching:
            path = item["run"]["path"].split("@", 1)[0]
            require(path in (".github/workflows/pytest-suite.yml", ".github/workflows/doc-health-py314.yml")
                    and path not in lanes, "unknown or duplicate actual source lane")
            lanes[path] = item
            require_proof_steps(item, path)
        require(set(lanes) == {".github/workflows/pytest-suite.yml", ".github/workflows/doc-health-py314.yml"},
                "both actual private-proof source lanes required")
        primary = lanes[".github/workflows/pytest-suite.yml"]
        secondary = lanes[".github/workflows/doc-health-py314.yml"]
        secondary_suites = {FEATURE_PATH + "/tests/" + name: primary["suites"][FEATURE_PATH + "/tests/" + name]
                            for name in ("test_source_roots.py", "test_delegated_evidence.py")}
        require(secondary["suites"] == secondary_suites, "Python 3.14 suite collection mismatch")
        require(len(extras) == 1 and found[next(iter(extras))] is secondary,
                "unknown provider observation outside required source lanes")
    for identity, suites in expected.items():
        require(found[identity]["suites"] == suites, "actual provider collection differs from authenticated output")


def require_proof_steps(observation, workflow):
    test_step = ("Run private-connectivity production source suites (043)"
                 if workflow.endswith("pytest-suite.yml") else "Exercise source proof under Python 3.14 (043)")
    names = ["Require the commissioned App identity (043)", "Mint scoped Opensoft source read token (043)",
             "Prepare commit-only owner roots with the reviewed producer (043)",
             "Revoke source tokens before any tests (043)", test_step, "Remove ephemeral source proof (043)"]
    steps = observation["job"]["steps"]
    selected = []
    for name in names:
        actual = [step for step in steps if step.get("name") == name]
        require(len(actual) == 1 and actual[0]["conclusion"] == "success",
                "actual source proof/cleanup step missing or failed")
        selected.append(actual[0]["number"])
    require(all(type(number) is int and number > 0 for number in selected)
            and selected == sorted(set(selected)), "source credentials not revoked before candidate tests")


def require_delegated_review(store, ref, subject, now, revoked=(), expected_ci=None, source=None):
    approved = DELEGATED_ATTESTATIONS.get(digest(canonical_json(subject)))
    require(approved is not None and _same_reference(ref, approved),
            "delegated output is not independently qualified")
    attestation = decode(_pinned_blob(store, ref))
    require(isinstance(attestation, dict) and set(attestation) == {
        "schema", "actor", "accountable_owner", "root", "producer", "reviewed_at",
        "subject", "independent_review", "provider_observations", "evidence"},
        "closed delegated attestation required")
    require(attestation["schema"] == "043-delegated-attestation-v1"
            and attestation["actor"] == "Codex" and attestation["accountable_owner"] == "Brett Heap"
            and attestation["subject"] == subject, "delegated actor/subject mismatch")
    reviewed_at = timestamp(attestation["reviewed_at"])
    require(reviewed_at <= now, "future delegated review")
    load_delegation_root(store, attestation["root"], reviewed_at, revoked=revoked)
    require_delegation_producer(store, attestation["producer"])
    require_independent_review(store, attestation["independent_review"], subject, reviewed_at)
    require_provider_observations(attestation["provider_observations"], expected_ci or {}, source, reviewed_at)
    evidence = attestation["evidence"]
    require(isinstance(evidence, list) and evidence, "actual delegated evidence references required")
    identities = set()
    for item in evidence:
        _pinned_blob(store, item)
        identities.add(canonical_json(reference(item)))
    require(len(identities) == len(evidence), "duplicate delegated evidence reference")
    return reviewed_at


def fixed_c37_control(ref):
    normalized = {**ref, "repository": ref["repository"].lower()}
    return next((item for item in C37_CONTROLS.values() if normalized == item["reference"]), None)


def fixed_2a46_control(ref):
    normalized = {**ref, "repository": ref["repository"].lower()}
    return next((item for item in CONTROLS_2A46.values() if normalized == item["reference"]), None)


def historical_source_parameters(ref):
    predecessor = T010_CUSTODY_PREDECESSOR
    if _same_reference(ref, predecessor["reference"]):
        return predecessor, predecessor["definition"], predecessor["reader"]
    selected = fixed_2a46_control(ref)
    if selected is not None:
        return selected, DEFINITION_2A46, READER_2A46
    selected = fixed_c37_control(ref)
    require(selected is not None, HISTORICAL_CONTROL_ERROR)
    return selected, C37_DEFINITION, C37_READER


def validate_historical_binding(key, ref):
    reference(ref)
    if _same_reference(ref, T010_CUSTODY_PREDECESSOR["reference"]):
        require(key == "T010", "unaccepted historical task")
        return
    selected_2a46 = fixed_2a46_control(ref)
    if key in {"T013", "T021", "T022"}:
        require(selected_2a46 is not None and
                (key != "T013" or selected_2a46 == CONTROLS_2A46["hosted"]),
                "unaccepted historical task")
        return
    selected = fixed_c37_control(ref)
    require(selected_2a46 is not None
            or (ref["sha256"] == LEGACY_CONTROL_SHA256 and key != "T020")
            or (selected is not None and (key != "T020" or selected == C37_CONTROLS["package"])),
            HISTORICAL_CONTROL_ERROR)


def historical_verifier(store, ref, now=None, *, prepare=False):
    """Use only the fixed accepted source control and its original frozen reader."""
    reference(ref)
    require(ref["repository"].lower() == COORDINATOR and ref["path"] == COMMISSIONING_PATH,
            HISTORICAL_CONTROL_ERROR)
    value = decode(store.blob(ref))
    if ref["sha256"] == LEGACY_CONTROL_SHA256:
        definition = LEGACY_DEFINITION
        reader_ref = {"repository": COORDINATOR, "commit": ref["commit"],
                      "path": FEATURE_PATH + "/verify-evidence.py", "sha256": LEGACY_READER_SHA256}
    else:
        selected, definition, reader_ref = historical_source_parameters(ref)
        require(commissioning_digest(value) == selected["content_sha256"], "unaccepted historical core")
    require(value["definition"] == definition, "unaccepted historical definition")
    root = store.root(COORDINATOR)
    tasks = _load_contract(lambda path: store.git(root, "show", ref["commit"] + ":" + FEATURE_PATH + "/" + relative(path)),
                           definition)
    code = store.blob(reader_ref)
    namespace = {"__name__": "_pc043_fixed_historical_reader", "__file__": __file__}
    exec(compile(code, "<authenticated historical 043 reader>", "exec"), namespace)
    verifier = namespace["Verifier"](tasks, store, ref, now, prepare=prepare)
    verifier.definition = definition
    return verifier


def verify_t010_transition_predecessor(provider, store, protected_base, now=None):
    """Verify T010 only while the qualified protected base still selects its predecessor."""
    ref = T010_CUSTODY_PREDECESSOR["reference"]
    provider.qualified_base(protected_base)
    active = provider.content(COMMISSIONING_PATH, protected_base)
    require(digest(active) == ref["sha256"], "protected main no longer selects the T010 predecessor")
    historical_verifier(store, ref, now).verify("T010")
    provider.qualified_base(protected_base)
    branch = provider.get("repos/" + COORDINATOR + "/branches/main")
    require(branch.get("protected") is True and branch.get("commit", {}).get("sha") == protected_base,
            "protected main changed during T010 predecessor verification")


def make_verifier(tasks, store, ref, now=None, *, prepare=False):
    known = ({LEGACY_CONTROL_SHA256} | {item["reference"]["sha256"] for item in C37_CONTROLS.values()}
             | {item["reference"]["sha256"] for item in CONTROLS_2A46.values()})
    if ref.get("sha256") in known:
        return historical_verifier(store, ref, now, prepare=prepare)
    return Verifier(tasks, store, ref, now, prepare=prepare)


class Verifier:
    def __init__(self, tasks, store, trust_reference, now=None, *, prepare=False):
        self.tasks, self.store = tasks, store
        self.definition = DEFINITION
        self.now = now or datetime.now(timezone.utc)
        require(trust_reference["repository"].lower() == COORDINATOR, "trust must belong to coordinator")
        self.trust_reference = reference(trust_reference)
        self.trust = decode(store.blob(self.trust_reference))
        t = self.trust
        require(t["schema"] == "043-reviewed-trust-v1" and t["feature"] == FEATURE and t["definition"] == DEFINITION,
                "wrong commissioning manifest")
        require(t["custodian"] == "Brett Heap", "uncommissioned evidence custodian")
        require(t["repositories"].get("C", "").lower() == COORDINATOR, "wrong coordinator identity")
        for alias, repository in t["repositories"].items():
            require(alias in "CLIHOD" and len(alias) == 1, "unknown owner alias")
            require(canonical_origin(repository) == repository.lower(), "invalid canonical repository")
            require(alias not in FIXED_REPOSITORIES or repository.lower() == FIXED_REPOSITORIES[alias], "wrong canonical component owner")
        self.objects = {}
        self.authenticated, self.authenticated_at = True, None
        self.delegated_source_authenticated = False
        self.delegated_root_id = None
        require(trust_reference["path"] != COMMISSIONING_PATH or "source_container" in t,
                "source commissioning container required")
        if "source_container" in t:
            require(trust_reference["path"] == COMMISSIONING_PATH, "wrong source commissioning path")
            self.source_container(t["source_container"])
            self.authentication(prepare)
        else:
            require(store.blob(reference(t["review"])).strip(), "missing independent custody review")
        self.active, self.cache = set(), set()
        legacy = t.get("historical_controls", {})
        require(isinstance(legacy, dict) and set(legacy) <= {f"T{i:03}" for i in range(1, 14)} | {"T016", "T020", "T021", "T022"},
                "unaccepted historical task")
        for key, ref in legacy.items():
            validate_historical_binding(key, ref)

    def source_container(self, container):
        require(isinstance(container, dict) and set(container) == {"schema", "objects"}
                and container["schema"] == "043-source-container-v1", "wrong source container")
        objects = container["objects"]
        require(isinstance(objects, dict) and objects, "closed source object table required")
        for name, entry in objects.items():
            require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", name), "invalid opaque object identity")
            require(isinstance(entry, dict) and set(entry) == {"tasks", "evidence_class", "value"}
                    and entry["evidence_class"] == "source", "source-only contained object required")
            tasks = entry["tasks"]
            require(isinstance(tasks, list) and tasks and len(tasks) == len(set(tasks))
                    and all(task in self.tasks and 1 <= int(task[1:]) <= 10
                            and self.tasks[task]["owner"] == "C" for task in tasks), "contained object outside E bootstrap scope")
            require(isinstance(entry["value"], dict), "contained object must be JSON object")
        self.objects = objects
        # Validate even unused objects. A caller cannot hide missing/cyclic refs
        # in a branch that the selected receipt happens not to traverse.
        visited = set()
        def visit(value, active):
            if isinstance(value, dict):
                if "object" in value:
                    require(set(value) == {"object"} and isinstance(value["object"], str)
                            and value["object"] in objects, "unknown or malformed contained reference")
                    name = value["object"]
                    require(name not in active, "cyclic contained reference")
                    if name not in visited:
                        visit(objects[name]["value"], active | {name})
                        visited.add(name)
                else:
                    for child in value.values(): visit(child, active)
            elif isinstance(value, list):
                for child in value: visit(child, active)
        for name, entry in objects.items():
            visit(entry["value"], {name})
        visit({key: item for key, item in self.trust.items() if key != "source_container"}, set())

    def authentication(self, prepare):
        ref = reference(self.trust["review"])
        require(ref["repository"].lower() == COORDINATOR and ref["path"] == AUTHENTICATION_PATH,
                "wrong source authentication owner/path")
        blocks = re.findall(rb"^```json\r?\n(.*?)^```[ \t]*$", self.store.blob(ref), re.M | re.S)
        require(len(blocks) == 1, "one source authentication JSON block required")
        review = decode(blocks[0])
        if review.get("schema") == "043-delegated-source-authentication-v1":
            self.delegated_authentication(review)
            return
        require(set(review) == {"schema", "decision", "custodian", "reviewed_manifest", "content_sha256", "reviewed_at"}
                and review["schema"] == "043-source-authentication-v1" and review["custodian"] == "Brett Heap",
                "wrong source authentication record")
        self.authenticated = review["decision"] == "accepted"
        if not self.authenticated:
            require(prepare and review["decision"] == "pending", "actual custodian authentication pending")
            return
        reviewed = reference(review["reviewed_manifest"])
        require(reviewed["repository"].lower() == COORDINATOR and reviewed["path"] == COMMISSIONING_PATH,
                "wrong reviewed source manifest")
        prior = decode(self.store.blob(reviewed))
        require(review["content_sha256"] == commissioning_digest(prior) == commissioning_digest(self.trust),
                "source authentication content mismatch")
        self.authenticated_at = timestamp(review["reviewed_at"])
        require(self.authenticated_at <= self.now, "future custodian authentication")

    def delegated_authentication(self, review):
        require(set(review) == {"schema", "decision", "actor", "accountable_owner",
                                "reviewed_manifest", "content_sha256", "attestation"}
                and review["decision"] == "accepted" and review["actor"] == "Codex"
                and review["accountable_owner"] == "Brett Heap", "wrong delegated source authentication")
        reviewed = reference(review["reviewed_manifest"])
        require(reviewed["repository"].lower() == COORDINATOR and reviewed["path"] == COMMISSIONING_PATH,
                "wrong reviewed source manifest")
        prior = decode(_pinned_blob(self.store, reviewed))
        require(review["content_sha256"] == commissioning_digest(prior) == commissioning_digest(self.trust),
                "delegated source authentication content mismatch")
        subject = {"kind": "source-authentication", "definition": self.definition,
                   "reviewed_manifest": reviewed, "content_sha256": review["content_sha256"]}
        expected = {}
        for key, binding in self.trust["bindings"].items():
            if key in self.trust.get("historical_controls", {}):
                continue
            output = self.read(self.read(binding["record"], binding)["output"], binding)
            self.ci(output, binding)
            for suite, run in output["ci"].items():
                identity = ci_identity(run["repository"], run["run_id"], run["job_id"], run["revision"])
                previous = expected.setdefault(identity, {}).setdefault(suite, run["collected"])
                require(previous == run["collected"], "conflicting actual CI collection")
        self.authenticated_at = require_delegated_review(
            self.store, review["attestation"], subject, self.now,
            self.trust["revoked_authorities"], expected, self.trust["bindings"]["T010"]["source"])
        self.authenticated = True
        self.delegated_source_authenticated = True
        self.delegated_root_id = "pc043-internal-20261117-e995d2290328"

    def blob(self, ref, binding=None):
        if isinstance(ref, dict) and "object" in ref:
            require(set(ref) == {"object"} and isinstance(ref["object"], str) and ref["object"] in self.objects,
                    "unanchored or malformed contained reference")
            require(binding is not None and binding["owner"] == "C" and binding["scope"]["phase"] == "source"
                    and 1 <= int(binding["task"][1:]) <= 10, "contained reference outside E source scope")
            entry = self.objects[ref["object"]]
            require(binding["task"] in entry["tasks"], "contained object task substitution")
            return canonical_json(entry["value"])
        return self.store.blob(reference(ref))

    def read(self, ref, binding=None):
        return decode(self.blob(ref, binding))

    def delegated_decision(self, decision, binding, start=None, end=None, *, post_run=False):
        if "delegation" not in decision and decision.get("actor") != "Codex" and decision.get("owner") != "Codex":
            return
        require(decision.get("actor") == decision.get("owner") == "Codex"
                and decision.get("accountable_owner") == "Brett Heap" and "delegation" in decision,
                "distinct delegated decision actor required")
        require(int(binding["task"][1:]) <= 61 and decision.get("kind") not in ("C-11", "C-12")
                and binding["scope"]["phase"] in ("source", "staging", "production"),
                "deferred external Q5/task decision")
        if binding["scope"]["phase"] != "source":
            require(binding["scope"]["customer"] == "Opensoft Inc", "delegation is internal-only")
        subject = {"kind": "decision", "definition": self.definition,
                   "record_sha256": digest(canonical_json({key: value for key, value in decision.items()
                                                         if key != "delegation"}))}
        if (self.definition == T010_CUSTODY_SUCCESSOR and binding["task"] == "T010" and not post_run
                and decision.get("kind") == "C-01" and subject["record_sha256"] == T010_ORIGINAL_SCOPE_DECISION
                and binding["scope"]["phase"] == decision["scope"]["phase"] == "source"
                and _same_reference(decision["delegation"], T010_ORIGINAL_SCOPE_PROOF)):
            subject["definition"] = T010_CUSTODY_PREDECESSOR["definition"]
        reviewed = require_delegated_review(self.store, decision["delegation"], subject, self.now,
                                           self.trust["revoked_authorities"])
        root = load_delegation_root(self.store, DELEGATION_ROOT_REF, reviewed,
                                    revoked=self.trust["revoked_authorities"])
        self.delegated_root_id = root["id"]
        if post_run:
            require(end is not None and end <= reviewed
                    and timestamp(decision["reviewed_at"]) == reviewed,
                    "delegated admission must follow actual output")
            return
        if start is not None:
            require(timestamp(root["approved_at"]) <= start and reviewed <= start,
                    "delegated execution before grant/root")
        if end is not None:
            require(end < timestamp(root["expires_at"]), "execution after delegation expiry")
        if binding["scope"]["phase"] in ("staging", "production"):
            begin, expiry = timestamp(decision["valid_from"]), timestamp(decision["valid_until"])
            require(timestamp(root["approved_at"]) <= begin < expiry <= timestamp(root["expires_at"]),
                    "delegated runtime grant exceeds human-root window")

    def current_delegation(self):
        require(self.delegated_root_id is None or self.delegated_root_id not in self.trust["revoked_authorities"],
                "delegation root revoked")

    def validity(self, decision, expected_scope, start=None, end=None, historical=False, source_lifetime=False, binding=None):
        """Source permissions may persist; execution channels remain time-bounded."""
        begin = timestamp(decision["valid_from"])
        expiry = (None if source_lifetime and expected_scope["phase"] == "source"
                  and decision["valid_until"] == "until-superseded"
                  else timestamp(decision["valid_until"]))
        require(expiry is None or begin < expiry, "invalid authority validity period")
        identity = decision["id"]
        closure = self.trust.get("completed_authorities", {}).get(identity)
        revoked = identity in self.trust["revoked_authorities"]
        if historical:
            require(start is not None and end is not None and begin <= start <= end
                    and (expiry is None or end < expiry),
                    "authority cannot retroactively authorize effects")
            if closure is not None:
                proof = self.read(closure, binding)
                require(proof["kind"] == "authority-closure" and proof["authority_id"] == identity
                        and proof["scope"] == expected_scope and proof["disposition"] == "completed",
                        "invalid completion closure")
                text(proof["owner"], "actual closing owner")
                require(end <= timestamp(proof["closed_at"]) <= self.now, "closure does not cover original run")
            require(not revoked or closure is not None, "revoked authority without completion closure")
        else:
            require(not revoked and closure is None, "revoked or closed authority")
            require(begin <= self.now and (expiry is None or self.now < expiry), "authority expired or not current")
            if start is not None:
                require(begin <= start <= end and (expiry is None or end < expiry),
                        "later authority cannot authorize an earlier run")
        return begin, expiry

    def decision(self, ref, binding, kind, start=None, end=None, historical=False, source_lifetime=False, post_run=False):
        decision = self.read(ref, binding)
        require(decision["kind"] == kind and decision["decision"] == "accepted", "required decision is not accepted")
        expected_scope = binding.get("decision_scopes", {}).get(kind, binding["scope"])
        require(scope(decision["scope"]) == expected_scope, "required decision scope mismatch")
        if (binding["scope"]["phase"] in ("staging", "production")
                and kind in ("C-03", "C-08", "C-09", "C-10", "C-11", "C-12", "C-13")):
            require(decision["scope"]["phase"] == binding["scope"]["phase"], "live decision phase mismatch")
        text(decision["owner"], "actual approving owner")
        self.delegated_decision(decision, binding, start, end, post_run=post_run)
        self.validity(decision, expected_scope, start, end, historical, source_lifetime, binding)
        return decision

    def authority(self, ref, binding, start=None, end=None, resume=False, historical=False):
        decision = self.read(ref, binding)
        require(decision["decision"] == "accepted" and decision["scope"] == binding["scope"], "authority scope/status mismatch")
        text(decision["owner"], "actual decision owner")
        require(decision["roles"] == binding["roles"] and bool(decision["roles"]), "required named roles missing")
        mode = decision["mode"]
        require(mode in ("source", "managed-pull", "managed-push", "customer"), "unknown authority channel")
        if binding["scope"]["phase"] in ("staging", "production"):
            require(mode != "source", "source authority cannot authorize live evidence")
        source_lifetime = mode == "source" and binding["scope"]["phase"] == "source"
        # A source repair reviews completed reruns; the original execution
        # authority is independently checked before this remediation path.
        source_review = resume and source_lifetime
        self.delegated_decision(decision, binding, start, end, post_run=source_review)
        self.validity(decision, binding["scope"], start, end, historical, source_lifetime, binding)
        if mode.startswith("managed-"):
            self.decision(decision["request"], binding, "request", start, end, historical)
            field = "grant" if mode == "managed-push" else "reviewed_merge"
            self.decision(decision[field], binding, field, start, end, historical)
        if mode == "customer":
            self.decision(decision["consent"], binding, "consent", start, end, historical)
        required = binding["decisions"]
        require(set(decision["decisions"]) == set(required), "required gate decisions missing/extra")
        if resume:
            require("C-13" in required, "fresh resume decision missing")
        for item in required:
            self.decision(decision["decisions"][item], binding, item, start, end, historical,
                          source_lifetime=binding["scope"]["phase"] == "source",
                          post_run=source_review and item == "C-13")
        return decision

    def evidence_authority(self, binding, record):
        """Admit historical results without keeping an execution grant open."""
        require(record["authority"] == binding["authority"], "record authority mismatch")
        require(record.get("admission") == binding.get("admission"), "record admission mismatch")
        output = self.read(record["output"], binding)
        start, end = timestamp(output["started_at"]), timestamp(output["ended_at"])
        require(start <= end <= self.now, "invalid/future actual run")
        commissioned_source = bool(self.objects) and binding["task"] in {f"T{i:03}" for i in range(1, 11)}
        if commissioned_source:
            require(self.authenticated and end <= self.authenticated_at, "output not authenticated after actual run")
            original = output["original"]
            require(isinstance(original, dict) and set(original) == {
                "command", "repository", "source_revision", "started_at", "ended_at", "exit_code",
                "stdout", "original_sha256", "export_sha256", "redaction_method"}, "original command/output provenance required")
            require(original["command"] == binding["command"] and original["repository"].lower() == binding["source"]["repository"].lower()
                    and original["source_revision"] == binding["source"]["revision"], "original command/source identity mismatch")
            require(original["started_at"] == output["started_at"] and original["ended_at"] == output["ended_at"]
                    and type(original["exit_code"]) is int and original["exit_code"] == output["exit_code"],
                    "original timing/exit identity mismatch")
            require(isinstance(original["stdout"], str) and original["export_sha256"] == digest(original["stdout"].encode()),
                    "original output export digest mismatch")
            require(isinstance(original["original_sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", original["original_sha256"]),
                    "original raw output digest required")
            text(original["redaction_method"], "actual redaction method")
            if original["redaction_method"] == "none":
                require(original["original_sha256"] == original["export_sha256"], "unredacted original output digest mismatch")
        historical = binding.get("admission") is not None
        if historical:
            admission = self.read(binding["admission"], binding)
            require(admission["kind"] == "evidence-admission" and admission["decision"] == "accepted"
                    and scope(admission["scope"]) == binding["scope"], "invalid evidence admission scope/status")
            roles = binding["admission_roles"]
            require(isinstance(roles, list) and roles and all(isinstance(role, str) and role.strip() for role in roles)
                    and len(roles) == len(set(roles)) and admission["roles"] == roles, "required admission roles missing")
            text(admission["owner"], "actual admitting owner")
            self.delegated_decision(admission, binding, start, end, post_run=True)
            begin, expiry = self.validity(admission, binding["scope"],
                                          source_lifetime=binding["scope"]["phase"] == "source", binding=binding)
            reviewed = timestamp(admission["reviewed_at"])
            require(end <= reviewed <= self.now and begin <= reviewed and (expiry is None or reviewed < expiry),
                    "invalid evidence review time")
            require(admission["authority"] == binding["authority"]
                    and admission["reviewed_output_sha256"] == digest(self.blob(record["output"], binding)),
                    "admission is not for original authority/output")
        elif (commissioned_source and self.delegated_source_authenticated
              and binding["scope"]["phase"] == "source"
              and binding["task"] not in self.trust.get("historical_controls", {})):
            # Registered authentication admits these exact completed source outputs.
            historical = True
        self.authority(binding["authority"], binding, start, end, historical=historical)
        return output, start, end, historical

    def binding(self, key):
        require(key in self.trust["bindings"], "uncommissioned task/instance")
        binding = self.trust["bindings"][key]
        task, separator, instance = key.partition("@")
        require(task in self.tasks, "unknown task")
        require(binding["task"] == task and binding["instance"] == (instance if separator else None), "binding identity mismatch")
        require(not separator or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", instance), "invalid opaque instance identity")
        require(not separator or task in INSTANCE_TASKS, "task has no child instances")
        scope(binding["scope"])
        roles = binding["roles"]
        require(isinstance(roles, list) and roles and all(isinstance(role, str) and role.strip() for role in roles)
                and len(roles) == len(set(roles)), "actual named owner roles required")
        number = int(task[1:])
        expected_phase = "staging" if 50 <= number <= 56 else "production" if 57 <= number <= 64 else "source"
        require(binding["scope"]["phase"] == expected_phase, "wrong task evidence phase")
        definition = self.tasks[task]
        require(binding["owner"] == definition["owner"] and binding["class"] == definition["class"], "owner/evidence class mismatch")
        require(set(binding["cases"]) == set(definition["cases"]), "required frozen cases changed")
        expected_deps = set(definition["dependencies"])
        require(set(binding["dependencies"]) == expected_deps, "required frozen dependencies changed")
        for predecessor, selected in binding["dependencies"].items():
            require(selected.split("@")[0] == predecessor, "substituted predecessor")
            if task not in INSTANCE_TASKS and predecessor in INSTANCE_TASKS:
                require(selected == predecessor, "non-instance task requires aggregate completion")
            if task in INSTANCE_TASKS and predecessor in INSTANCE_TASKS:
                require("@" in selected, "child cannot borrow an aggregate")
                old_scope = self.trust["bindings"][selected]["scope"]
                # Exact, separately reviewed transitions permit a canary-to-wave
                # scope expansion. Without one, target/customer identity is fixed.
                expected = binding.get("transitions", {}).get(predecessor, binding["scope"])
                require(old_scope == expected, "unapproved child scope transition")
            if 52 <= number <= 57:
                previous = self.trust["bindings"][selected]["scope"]
                require(previous["candidate"] == binding["scope"]["candidate"], "candidate changed across gate dependency")
                if number <= 56:
                    require(previous["run"] == binding["scope"]["run"], "mixed staging run")
        if task in INSTANCE_TASKS:
            require(separator and instance in self.trust["instances"].get(task, []), "missing commissioned instance")
            for predecessor in binding["dependencies"].values():
                if "@" in predecessor:
                    other = self.trust["bindings"][predecessor]["scope"]
                    for field in ("candidate", "profile", "offering", "phase", "offer"):
                        require(other[field] == binding["scope"][field], "foreign offering/candidate/profile predecessor")
            if task in ("T057", "T058"):
                require("C-09" in binding["decisions"], "canary requires C-09")
            if task == "T061":
                require("C-10" in binding["decisions"], "observation acceptance requires C-10")
            if task in ("T062", "T063", "T064"):
                require("C-11" in binding["decisions"], "offer requires C-11")
                if binding["scope"]["wave"] != "not-applicable":
                    require("C-12" in binding["decisions"], "wave requires C-12")
        if task == "T050":
            require({"C-03", "C-07"} <= set(binding["decisions"]), "staging preparation decisions incomplete")
        if task == "T051":
            require(set(f"C-{i:02}" for i in range(3, 9)) <= set(binding["decisions"]), "Q1 decisions incomplete")
        if binding["scope"]["phase"] in ("staging", "production"):
            custody = self.trust.get("live_custody", {})
            require(custody.get("kind") == "protected" and custody.get("decision") == "C-08" and "C-08" in binding["decisions"],
                    "source-only custody cannot admit live evidence")
            require(binding["metrics"] and binding["observation"], "live numeric limits/observation missing")
        else:
            require(self.trust["custody"]["kind"] == "source-git", "unaccepted source custody")
        if int(task[1:]) < 10:
            require(binding["command"] == definition["command"], "bootstrap original command mismatch")
        else:
            require("verify-evidence.py" not in binding["command"], "self-verification is not an owner execution output")
        text(binding["command"], "approved owner command")
        return binding

    def source(self, value, binding):
        require(value == binding["source"], "tested revision or source mismatch")
        require(value["repository"].lower() == self.trust["repositories"][binding["owner"]].lower(), "source owner mismatch")
        allowed = binding["files"]
        require(allowed and len(allowed) == len(set(allowed)), "exact accepted file list required")
        envelopes = self.tasks[binding["task"]]["files"]
        for name in allowed:
            relative(name)
            require(any(name == p or (p.endswith("/") and name.startswith(p)) for p in envelopes), "file outside candidate envelope")
        changed = self.store.changed(value)
        require(changed <= set(allowed), "source diff exceeds exact accepted scope")
        if binding["task"] in ("T007", "T008", "T009"):
            require(changed, "bootstrap source implementation has no exact diff")

    def cases(self, output, binding):
        cases = output["cases"]
        require(isinstance(cases, list), "case array required")
        indexed = {}
        for case in cases:
            require(case["id"] not in indexed, "duplicate case")
            indexed[case["id"]] = case
            require(case["scope"] == binding["scope"] and case["source"] == binding["source"], "mixed case scope/source")
        require(set(indexed) == set(binding["cases"]), "missing/unknown frozen cases")
        for name, specs in binding["cases"].items():
            require(specs and len({s["id"] for s in specs}) == len(specs), "closed subchecks required")
            checks = indexed[name]["checks"]
            require(len(checks) == len(specs) and {c["id"] for c in checks} == {s["id"] for s in specs}, "missing/duplicate/unknown subchecks")
            actual = {c["id"]: c for c in checks}
            for spec in specs:
                check = actual[spec["id"]]
                kind = spec["kind"]
                require(kind in ("equal", "deny", "maximum", "minimum"), "unknown expected outcome type")
                if kind in ("maximum", "minimum"):
                    measured = finite(check["observed"], "measurement")
                    limit = finite(spec["expected"], "approved limit")
                    text(spec["unit"], "measurement unit")
                    text(spec["event"], "measurement event")
                    require(check["unit"] == spec["unit"] and check["event"] == spec["event"], "measurement units/event mismatch")
                    anchor = timestamp(output["events"][check["event"]])
                    require(timestamp(output["started_at"]) <= anchor <= timestamp(output["ended_at"]), "measurement event outside run")
                    require(measured <= limit if kind == "maximum" else measured >= limit, "approved numeric limit exceeded")
                else:
                    require(type(check["observed"]) is type(spec["expected"]) and check["observed"] == spec["expected"], "expected/observed mismatch")
                if kind == "deny":
                    require(spec["expected"] == "denied", "denial must be observed")
                    control = actual.get(spec["control"])
                    require(control is not None and control["observed"] == "allowed", "legitimate positive control missing/failed")
                if "neighbor" in spec:
                    require(spec["neighbor"] in actual and actual[spec["neighbor"]]["observed"] == "available", "authorized neighbor missing/failed")

    def observations(self, output, binding):
        require(set(output["metrics"]) == set(binding["metrics"]), "numeric metric inventory mismatch")
        for name, limits in binding["metrics"].items():
            measurement = output["metrics"][name]
            value = finite(measurement["value"], name)
            lo, hi = finite(limits["minimum"], "minimum"), finite(limits["maximum"], "maximum")
            text(limits["unit"], "metric unit")
            text(limits["event"], "metric event")
            require(lo <= value <= hi, "metric outside approved bounds")
            require(measurement["unit"] == limits["unit"] and measurement["event"] == limits["event"], "metric unit/event mismatch")
            anchor = timestamp(output["events"][limits["event"]])
            require(timestamp(output["started_at"]) <= anchor <= timestamp(output["ended_at"]), "metric event outside actual run")
        observation = binding["observation"]
        if observation is None:
            require(output["coverage"] is None, "uncommissioned observation window")
            return
        coverage = output["coverage"]
        require(coverage["window"] == observation["window"], "wrong observation window")
        start, end = map(timestamp, coverage["window"])
        require(timestamp(output["started_at"]) <= start < end <= timestamp(output["ended_at"]), "observation outside run")
        max_gap = finite(observation["max_gap_seconds"], "gap")
        minimum = finite(observation["minimum_observed_seconds"], "minimum observed", minimum=0.000001)
        cursor, observed = start, 0
        require(coverage["intervals"], "no monitoring coverage")
        for interval in coverage["intervals"]:
            begin, finish = map(timestamp, interval)
            require(cursor <= begin < finish <= end, "overlapping/out-of-window monitoring")
            require((begin - cursor).total_seconds() <= max_gap, "monitoring gap exceeds approved limit")
            observed += (finish - begin).total_seconds()
            cursor = finish
        require((end - cursor).total_seconds() <= max_gap and observed >= minimum, "omitted monitoring time is not healthy observation")

    def ci(self, output, binding):
        required = binding["ci"]
        require(isinstance(required, dict), "closed required CI inventory")
        if self.tasks[binding["task"]]["class"].startswith("CI-"):
            require(required, "required exact-head CI collection missing")
        if binding["task"] == "T010":
            require({FEATURE_PATH + "/tests/" + name for name in ("test_evidence.py", "test_evidence_pins.py", "test_source_roots.py", "test_delegated_evidence.py")} == set(required), "feature suites not explicitly collected")
        actual = output["ci"]
        require(set(actual) == set(required), "missing/unknown CI suites")
        for suite, count in required.items():
            run = actual[suite]
            require(type(count) is int and count > 0, "positive collected count required")
            require(run["repository"] == binding["source"]["repository"] and run["revision"] == binding["source"]["revision"], "CI is not exact owner/head")
            require(run["conclusion"] == "success" and run["required"] is True and run["collected"] == run["passed"] == count
                    and type(run["collected"]) is int and type(run["passed"]) is int
                    and type(run["skipped"]) is int and run["skipped"] == 0, "missing/failed/uncollected/waived CI")
            for field in ("run_id", "job_id"):
                require(type(run[field]) is int and run[field] > 0, "actual GitHub run/job identity required")

    def prior_acceptance(self, key, start, message):
        self.verify(key)
        binding = self.binding(key)
        record = self.read(binding["record"], binding)
        _, _, end, _ = self.evidence_authority(binding, record)
        accepted_at = (timestamp(self.read(binding["admission"], binding)["reviewed_at"])
                       if binding.get("admission") else end)
        require(end <= start and accepted_at <= start, message)

    def verify(self, key, supplied=None):
        self.current_delegation()
        require(self.authenticated, "actual custodian authentication pending")
        if key in INSTANCE_TASKS:
            aggregate_ref = reference(self.trust["aggregates"][key])
            self.aggregate(key, self.store.blob(aggregate_ref) if supplied is None else supplied)
            return
        require(key not in self.active, "cyclic evidence dependency")
        binding = self.binding(key)
        ref = binding["record"]
        data = self.blob(ref, binding)
        if supplied is not None:
            require(supplied == data, "receipt differs from independently reviewed immutable reference")
        record = decode(data)
        # Current admission and original execution validity are checked even on cache hits.
        output, start, end, historical = self.evidence_authority(binding, record)
        if key in self.trust.get("historical_controls", {}):
            prior = historical_verifier(self.store, self.trust["historical_controls"][key], self.now)
            require(binding == prior.binding(key), "historical binding changed")
            # Keep the frozen graph/original objects, but apply current authority
            # state throughout its dependency traversal, including cache rechecks.
            prior.trust["revoked_authorities"] = prior.trust["revoked_authorities"] + self.trust["revoked_authorities"]
            prior.trust["completed_authorities"] = {**prior.trust.get("completed_authorities", {}),
                                                    **self.trust.get("completed_authorities", {})}
            prior.objects = {**self.objects, **prior.objects}
            try:
                prior.verify(key, data)
            except ValueError as exc:
                raise EvidenceError(str(exc)) from exc
            self.cache.add(key)
            return
        if key in self.cache:
            return
        self.active.add(key)
        task = binding["task"]
        bootstrap = int(task[1:]) < 10
        require(record["schema"] == ("043-bootstrap-import-v1" if bootstrap else "043-task-evidence-v1"), "wrong evidence/import kind")
        if bootstrap:
            require("object" in ref or not re.fullmatch(r"T00[1-9]\.json", PurePosixPath(ref["path"]).name), "fabricated bootstrap task receipt")
        else:
            reference(ref)
            require(ref["path"] in binding["files"] and ref["repository"].lower() == self.trust["repositories"][binding["owner"]].lower(), "receipt outside exact accepted owner scope")
        for field, expected in (("task", task), ("instance", binding["instance"]), ("owner", binding["owner"]),
                                ("evidence_class", binding["class"]), ("scope", binding["scope"]), ("command", binding["command"]),
                                ("authority", binding["authority"]), ("history", binding["history"])):
            require(record[field] == expected, "record " + field + " mismatch")
        text(record["attempt"], "attempt identity")
        require(record["verdict"] == "pass", "failed/blocked evidence cannot satisfy a dependency")
        self.source(record["source"], binding)
        require(record["artifacts"] == binding["artifacts"] and record["artifacts"], "original source/governance artifacts missing")
        artifact_data = {a["path"]: self.store.blob(reference(a)) for a in record["artifacts"]}
        for artifact in record["artifacts"]:
            require(artifact["repository"] == record["source"]["repository"] and artifact["commit"] == record["source"]["revision"], "artifact is not tested source")
        if bootstrap:
            required_artifacts = set()
            for envelope in self.tasks[task]["files"]:
                if envelope.endswith("/"):
                    if envelope.startswith("openspec/"):
                        required_artifacts.update((envelope + "proposal.md", envelope + ".openspec.yaml"))
                else:
                    required_artifacts.add(envelope)
            require(required_artifacts <= set(artifact_data), "original bootstrap source/governance artifact missing")
        if task == "T002":
            baseline_path = FEATURE_PATH + "/evidence/baseline.json"
            require(baseline_path in artifact_data, "original historical baseline missing")
            baseline = decode(artifact_data[baseline_path])
            require(baseline["authorizes_production"] is False and baseline["evidence_class"] == "historical-lab", "lab cannot grant production authority")
            old = "specs/040-private-connectivity/evidence/T021.json"
            require(old in artifact_data and digest(artifact_data[old]) == baseline["evidence_sha256"], "historical content identity mismatch")
        if task == "T006":
            base = "openspec/changes/commission-private-connectivity-production-evidence/"
            require(b"Status: ratified" in artifact_data.get(base + "proposal.md", b"")
                    and b"Ratified:" in artifact_data.get(base + "review/ratification.md", b"")
                    and b"approved_by:" in artifact_data.get(base + ".openspec.yaml", b""), "actual E ratification/source provenance missing")
        for field in ("task", "instance", "scope", "source", "command"):
            require(output[field] == record[field], "actual output " + field + " mismatch")
        require(type(output["exit_code"]) is int and output["exit_code"] == 0, "missing/nonzero owner command result")
        self.cases(output, binding)
        self.observations(output, binding)
        self.ci(output, binding)
        require(record["dependencies"] == {dep: (self.trust["aggregates"][selected] if selected in INSTANCE_TASKS else self.trust["bindings"][selected]["record"])
                                           for dep, selected in binding["dependencies"].items()}, "immutable dependency substitution")
        # Every child still depends on the complete program Q2; no partial union.
        if task in INSTANCE_TASKS:
            self.prior_acceptance("T056", start, "Q2 acceptance must precede production execution")
        for selected in binding["dependencies"].values():
            if 50 <= int(task[1:]) <= 64:
                self.prior_acceptance(selected, start, "accepted dependency must precede consuming execution")
            else:
                self.verify(selected)
        if task in INSTANCE_TASKS:
            if binding["scope"]["offering"] in ("local-managed", "hosted-domain"):
                eligibility = binding["eligibility"]
                eligible = self.binding(eligibility)
                require(eligible["scope"]["offering"] == "hosted-headscale", "managed service eligibility missing")
                for field in SCOPE_FIELDS - {"offering", "domain", "profile"}:
                    require(eligible["scope"][field] == binding["scope"][field], "managed service is not eligible in this phase/scope")
                require(eligible["task"] == task, "managed service eligibility phase mismatch")
                self.prior_acceptance(eligibility, start, "managed service eligibility must precede attachment execution")
            if task == "T063" and binding["scope"]["wave"] != "not-applicable":
                offer = self.binding(binding["offer_admission"])
                require(offer["task"] == "T063" and offer["scope"]["wave"] == "not-applicable", "wave requires prior offer admission")
                for field in ("offer", "offering", "candidate", "profile", "phase"):
                    require(offer["scope"][field] == binding["scope"][field], "wrong corresponding offer admission")
                self.prior_acceptance(binding["offer_admission"], start, "offer admission must precede wave execution")
        for prior in record["history"]:
            failed = self.read(prior, binding)
            require(failed["verdict"] in ("fail", "blocked") and failed["task"] == task
                    and failed["scope"] == record["scope"] and failed["attempt"] != record["attempt"], "failed/blocked attempt history lost or substituted")
        if record["history"]:
            require(record["remediation"] == binding["remediation"], "reviewed remediation missing")
            resumed = self.authority(record["remediation"], binding, start, end, resume=True, historical=historical)
            resume = self.read(resumed["decisions"]["C-13"], binding)
            require(resume["reruns"] == binding["resume_outputs"] and record["output"] in resume["reruns"], "reviewed affected rerun outputs missing")
            for rerun in resume["reruns"]:
                self.blob(rerun, binding)
        require(record["incidents"] == binding["incidents"], "incident history omitted")
        for incident in record["incidents"]:
            closed = self.decision(incident, binding, "incident-closure")
            require(closed["reruns"], "affected/adjacent reruns missing")
            for rerun in closed["reruns"]:
                self.blob(rerun, binding)
        self.active.remove(key)
        self.cache.add(key)

    def aggregate(self, task, data):
        self.current_delegation()
        require(self.authenticated, "actual custodian authentication pending")
        require(task in INSTANCE_TASKS, "task has no aggregate instances")
        record = decode(data)
        instances = self.trust["instances"].get(task, [])
        require(instances and len(instances) == len(set(instances)), "commissioned instance inventory required")
        ref = reference(self.trust["aggregates"][task])
        owner = self.tasks[task]["owner"]
        prefix = FEATURE_PATH + "/evidence/" if owner == "C" else "evidence/private-connectivity-production/"
        require(ref["path"] == prefix + task + ".json" and ref["repository"].lower() == self.trust["repositories"][owner].lower(), "aggregate outside accepted owner scope")
        require(data == self.store.blob(ref), "aggregate differs from reviewed immutable reference")
        expected = {instance: self.trust["bindings"][task + "@" + instance]["record"] for instance in instances}
        body = {key: value for key, value in record.items() if key != "pin_inventory"}
        require(body == {"schema": "043-instance-aggregate-v1", "task": task, "children": expected}, "missing/foreign/duplicate aggregate child")
        for instance in instances:
            self.verify(task + "@" + instance)
        if task == "T061" and (self.delegated_root_id is not None or "internal_program" in self.trust):
            require("internal_program" in self.trust, "internal delegated root requires program handoff")
            self.internal_handoff(instances, expected)

    def internal_handoff(self, instances, expected):
        marker = self.trust["internal_program"]
        require(isinstance(marker, dict) and set(marker) == {"root", "handoff"},
                "closed internal-program marker required")
        require(_same_reference(marker["root"], DELEGATION_ROOT_REF), "wrong internal program root")
        ref = reference(marker["handoff"])
        require(ref["repository"].lower() == COORDINATOR
                and ref["path"] == FEATURE_PATH + "/review/internal-production-handoff.md",
                "wrong internal handoff owner/path")
        raw = _pinned_blob(self.store, ref)
        blocks = re.findall(rb"^```json\r?\n(.*?)^```[ \t]*$", raw, re.M | re.S)
        require(len(blocks) == 1, "one internal handoff JSON block required")
        handoff = decode(blocks[0])
        require(isinstance(handoff, dict) and set(handoff) == {
            "schema", "root", "accepted_at", "offerings", "releases", "operations", "attestation"}
            and handoff["schema"] == "043-internal-program-handoff-v1"
            and _same_reference(handoff["root"], DELEGATION_ROOT_REF), "wrong internal handoff")
        groups = {"local-headscale": {}, "hosted-headscale": {}, "hosted-domain": {}}
        for instance in instances:
            binding = self.binding("T061@" + instance)
            require(binding["scope"]["customer"] == "Opensoft Inc"
                    and binding["scope"]["phase"] == "production", "internal handoff includes foreign customer/phase")
            offering = binding["scope"]["offering"]
            group = "local-headscale" if offering in ("local-local", "local-managed") else offering
            require(group in groups, "unknown internal offering")
            groups[group][instance] = expected[instance]
        require(all(groups.values()) and handoff["offerings"] == groups,
                "all three actual accepted internal offerings required")
        accepted = timestamp(handoff["accepted_at"])
        load_delegation_root(self.store, marker["root"], accepted,
                             revoked=self.trust["revoked_authorities"])
        for instance in instances:
            self.prior_acceptance("T061@" + instance, accepted,
                                  "actual child acceptance must precede internal handoff")
        releases = {owner: self.binding(task)["record"] for owner, task in
                    (("C", "T019"), ("L", "T023"), ("I", "T027"), ("H", "T033"), ("D", "T042"), ("O", "T048"))}
        require(handoff["releases"] == releases, "current release/readback task references required")
        for task in ("T019", "T023", "T027", "T033", "T042", "T048"):
            self.prior_acceptance(task, accepted, "actual release/readback must precede internal handoff")
        operations = handoff["operations"]
        require(isinstance(operations, dict) and set(operations) == {
            "onboarding", "monitoring", "support", "rollback", "custody"}, "complete usable operator handoff required")
        for item in operations.values():
            require(reference(item)["repository"].lower() in {
                value.lower() for value in self.trust["repositories"].values()}, "foreign operator handoff")
            require(_pinned_blob(self.store, item).strip(), "empty operator handoff")
        subject = {"kind": "internal-program-handoff", "definition": self.definition,
                   "content_sha256": digest(canonical_json({key: value for key, value in handoff.items()
                                                          if key != "attestation"}))}
        reviewed = require_delegated_review(self.store, handoff["attestation"], subject, self.now,
                                           self.trust["revoked_authorities"])
        require(reviewed == accepted, "internal handoff acceptance time mismatch")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--instance")
    parser.add_argument("record", type=Path)
    arguments = parser.parse_args(argv)
    try:
        root = Path(__file__).resolve().parents[2]
        tasks = load_contract(root)
        require(arguments.task in tasks, "unknown task")
        anchor = os.environ.get("PC_EVIDENCE_TRUST", "")
        revision, separator, path = anchor.partition(":")
        require(separator, "independently approved PC_EVIDENCE_TRUST is required")
        roots = decode(os.environ.get("PC_EVIDENCE_ROOTS", "{}"))
        require(isinstance(roots, dict) and COORDINATOR not in {k.lower() for k in roots}, "coordinator root cannot be overridden")
        roots[COORDINATOR] = str(root)
        store = GitStore(roots)
        trust_ref = {"repository": COORDINATOR, "commit": revision, "path": path,
                     "sha256": os.environ.get("PC_EVIDENCE_TRUST_SHA256", "")}
        verifier = make_verifier(tasks, store, trust_ref)
        owner = tasks[arguments.task]["owner"]
        owner_root = store.root(verifier.trust["repositories"][owner])
        record_path = arguments.record.absolute()
        require(record_path.resolve().is_relative_to(owner_root), "record outside accepted owner root")
        relative_path = record_path.relative_to(owner_root)
        require(all(not p.is_symlink() for p in (owner_root.joinpath(*relative_path.parts[:i]) for i in range(1, len(relative_path.parts) + 1))), "receipt symlink forbidden")
        data = record_path.read_bytes()
        if arguments.task in INSTANCE_TASKS and arguments.instance is None:
            require(relative_path.as_posix() == verifier.trust["aggregates"][arguments.task]["path"], "wrong accepted aggregate path")
            verifier.aggregate(arguments.task, data)
        else:
            key = arguments.task + ("@" + arguments.instance if arguments.instance else "")
            binding = verifier.binding(key)
            require(relative_path.as_posix() == binding["record"]["path"], "wrong accepted receipt path")
            if arguments.instance:
                prefix = (FEATURE_PATH + "/evidence/" if owner == "C" else "evidence/private-connectivity-production/") + "instances/" + arguments.task + "/"
                require(relative_path.as_posix().startswith(prefix), "child outside accepted instance area")
            verifier.verify(key, data)
        print(arguments.task + ": structurally verified; owner/gate acceptance remains independent")
        return 0
    except (EvidenceError, OSError, KeyError, TypeError, AttributeError, RecursionError) as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
