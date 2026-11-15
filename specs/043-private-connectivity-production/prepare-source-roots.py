#!/usr/bin/env python3
"""Bounded CI commit proof preparation. No task, release or rollout acceptance.

Planning/checking are offline. History reads only public coordinator retention
objects; prepare performs explicitly scoped private GitHub reads. Credentialed execution uses an authenticated producer selected by the
trusted base, never the candidate's script. Private stores are ephemeral, bare
and commit-only; full source evidence verification uses separate owner clones.
"""

import argparse
import base64
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from urllib import request


LOCAL = "opensoft/openxfactory"
FEATURE = "specs/043-private-connectivity-production"
EVIDENCE_DIRECTORY = FEATURE + "/evidence"
GITHUB = "https://github.com/"
FETCH_PREFIX = ("fetch", "--no-tags", "--depth=1", "--filter=tree:0", "origin")
PUBLIC_FETCH_PREFIX = ("fetch", "--no-tags", "--no-recurse-submodules", "--no-write-fetch-head", GITHUB + LOCAL + ".git")
COMMISSIONING = FEATURE + "/evidence/commissioning.json"
SELF = FEATURE + "/prepare-source-roots.py"
AUTHENTICATION = "openspec/changes/commission-private-connectivity-production-evidence/review/commissioning-authentication.md"
REPOSITORIES = {"opensoft/headscale-install": 1452848226, "opensoft/xfactory-installer": 1296028330,
                "opensoft/openxsoft-hosted-services": 1452848362, "opensoft/opsxfactory": 1284702188,
                "codexfactory/codexfactory": 1281785369}
INSTALLATIONS = {"opensoft": "145372182", "codexfactory": "160352673"}
TASKS = {"T010", "T011", "T012", "T013", "T014", "T015", "T016", "T017", "T018", "T019", "T027", "T042",
         "T049", "T051", "T056", "T057", "T061", "T062", "T064", "T065", "T066", "T067", "T068"}
CHILDREN = {"T057", "T061", "T062", "T064"}
PIN = re.compile(r"[0-9a-f]{40}")
TOKEN = re.compile(r"(?<![0-9A-Za-z])[0-9a-f]{40}(?![0-9A-Za-z])")
MARKER = ".pc043-commit-proof"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def decode(raw):
    value = json.loads(raw, object_pairs_hook=pairs,
                       parse_constant=lambda value: (_ for _ in ()).throw(ValueError("non-finite JSON")))
    def inspect(item):
        if isinstance(item, float): require(math.isfinite(item), "non-finite JSON")
        elif isinstance(item, dict):
            for child in item.values(): inspect(child)
        elif isinstance(item, list):
            for child in item: inspect(child)
    inspect(value)
    return value


def git_environment(token=None):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and
           k not in {"GH_TOKEN", "GITHUB_TOKEN", "PC_OPENSOFT_TOKEN", "PC_DOMAIN_TOKEN"}}
    env.update(GIT_NO_LAZY_FETCH="1", GIT_TERMINAL_PROMPT="0", GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
    if token:
        env.update(GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                   GIT_CONFIG_VALUE_0="AUTHORIZATION: basic " + base64.b64encode(("x-access-token:" + token).encode()).decode())
    return env


def proof_git_arguments(arguments):
    """Reconstruct only the finite proof operations, never arbitrary CLI options."""
    require(isinstance(arguments, (list, tuple)) and all(isinstance(a, str) for a in arguments),
            "invalid Git proof operation")
    fixed = (("config", "--get", "remote.origin.url"), ("rev-parse", "--is-bare-repository"),
             ("cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype)"),
             ("init", "--bare", "-q"))
    for operation in fixed:
        if tuple(arguments) == operation:
            return list(operation)
    match arguments:
        case ["rev-parse", "--verify", revision]:
            require(re.fullmatch(r"(?:HEAD|[0-9a-f]{40})\^\{commit\}", revision), "invalid proof revision")
            return ["rev-parse", "--verify", "--end-of-options", revision]
        case ["ls-tree", "-r", "--name-only", revision, "--", path]:
            require(PIN.fullmatch(revision) and path == EVIDENCE_DIRECTORY, "invalid proof listing")
            return ["ls-tree", "-r", "--name-only", revision, "--", EVIDENCE_DIRECTORY]
        case ["ls-tree", revision, "--", path]:
            require(PIN.fullmatch(revision) and proof_blob_path(path), "invalid proof tree path")
            return ["ls-tree", revision, "--", path]
        case ["show", blob] | ["cat-file", "-s", blob]:
            revision, separator, path = blob.partition(":")
            require(PIN.fullmatch(revision) and separator and proof_blob_path(path), "invalid proof blob")
            blob = revision + ":" + path
            return (["show", "--no-ext-diff", "--no-textconv", blob] if arguments[0] == "show" else
                    ["cat-file", "-s", blob])
        case ["remote", "add", "origin", url]:
            for owner in REPOSITORIES:
                allowed = GITHUB + owner + ".git"
                if url == allowed:
                    return ["remote", "add", "origin", allowed]
        case ["fetch", *rest]:
            return proof_fetch_arguments(arguments)
    raise ValueError("unregistered Git proof operation")


def proof_blob_path(path):
    return path in {SELF, AUTHENTICATION} or registered(path)


def proof_fetch_arguments(arguments):
    pins = arguments[5:]
    require(1 <= len(pins) <= 256, "invalid proof fetch bound")
    if tuple(arguments[:5]) == PUBLIC_FETCH_PREFIX:
        require(all(re.fullmatch(r"refs/retention/pins/([0-9a-f]{40}):refs/retention/pins/\1", pin) for pin in pins),
                "invalid public retention ref")
        return [*PUBLIC_FETCH_PREFIX, *pins]
    require(tuple(arguments[:5]) == FETCH_PREFIX and all(PIN.fullmatch(pin) for pin in pins), "invalid proof fetch pins")
    return [*FETCH_PREFIX, *pins]


def run_git(root, arguments, token=None):
    directory = str(Path(root).resolve(strict=True))
    require(Path(directory).is_dir(), "Git proof root must be a directory")
    operation = proof_git_arguments(arguments)
    require(not token or tuple(operation[:5]) == FETCH_PREFIX, "proof credentials are fetch-only for private commit stores")
    public = (tuple(operation[:5]) == PUBLIC_FETCH_PREFIX)
    headers = ["-c", "http.extraheader=", "-c", "http.https://github.com/.extraheader="] if public else []
    try:
        process = subprocess.run(["git", "--no-optional-locks", "--no-replace-objects", "-c", "core.hooksPath=/dev/null",
                                  "-c", "credential.helper=", "-c", "protocol.allow=never", "-c", "protocol.https.allow=always",
                                  *headers, *operation], cwd=directory, env=git_environment(token), capture_output=True,
                                 timeout=90, check=False)
    except subprocess.TimeoutExpired as exc:
        raise ValueError("bounded Git proof operation timed out") from exc
    # Never print Git's stderr: a remote/credential helper might echo credentials.
    require(process.returncode == 0, "Git proof operation failed")
    return process.stdout


def origin(root):
    value = run_git(root, ["config", "--get", "remote.origin.url"]).decode().strip().removesuffix(".git").rstrip("/")
    for prefix in (GITHUB, "git@github.com:", "ssh://git@github.com/"):
        if value.startswith(prefix):
            name = value[len(prefix):]
            require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name), "invalid canonical proof owner")
            return name.lower()
    raise ValueError("canonical GitHub proof origin required")


def registered(path):
    if path == COMMISSIONING:
        return True
    prefix = FEATURE + "/evidence/"
    if not path.startswith(prefix):
        return False
    parts = path[len(prefix):].split("/")
    return ((len(parts) == 1 and parts[0].removesuffix(".json") in TASKS and parts[0].endswith(".json")) or
            (len(parts) == 3 and parts[0] == "instances" and parts[1] in CHILDREN and
             re.fullmatch(r"[A-Za-z0-9_.-]+\.json", parts[2]) is not None))


def inventory_plan(root, revision="HEAD"):
    require(origin(root) == LOCAL, "coordinator origin mismatch")
    revision = run_git(root, ["rev-parse", "--verify", revision + "^{commit}"]).decode().strip()
    paths = run_git(root, ["ls-tree", "-r", "--name-only", revision, "--", EVIDENCE_DIRECTORY]).decode().splitlines()
    result = {}
    for path in paths:
        if not registered(path):
            continue
        mode = run_git(root, ["ls-tree", revision, "--", path]).split()[0]
        require(mode == b"100644", "linked/non-regular evidence refused")
        require(int(run_git(root, ["cat-file", "-s", revision + ":" + path])) <= 16 * 1024 * 1024,
                "evidence exceeds bounded source proof input")
        value = decode(run_git(root, ["show", revision + ":" + path]))
        require(isinstance(value, dict) and isinstance(value.get("pin_inventory"), list), "missing inventory")
        seen = set()
        for row in value["pin_inventory"]:
            require(isinstance(row, dict) and isinstance(row.get("repository"), str), "invalid inventory row")
            owner = row["repository"].lower()
            require(owner == LOCAL or owner in REPOSITORIES, "uncommissioned proof owner")
            field = "openxfactory_commit" if owner == LOCAL else "foreign_commit"
            require(set(row) == {"repository", field} and isinstance(row[field], str) and PIN.fullmatch(row[field]),
                    "invalid full commit inventory")
            identity = (owner, row[field]); require(identity not in seen, "duplicate inventory row"); seen.add(identity)
            result.setdefault(owner, set()).add(row[field])
        content = {key: item for key, item in value.items() if key != "pin_inventory"}
        require({pin for owner, pin in seen} == set(TOKEN.findall(json.dumps(content, sort_keys=True))),
                "inventory token coverage changed before preparation")
    require(all(len(pins) <= 256 for pins in result.values()), "source proof commit bound exceeded")
    return {owner: sorted(pins) for owner, pins in sorted(result.items())}


def discover(root, revision="HEAD"):
    return {owner: pins for owner, pins in inventory_plan(root, revision).items() if owner != LOCAL}


def hydrate_history(root, runner=run_git):
    """Restore declared public Git objects without credentials or shallow/working-tree changes."""
    pins = inventory_plan(root).get(LOCAL, [])
    missing = []
    for pin in pins:
        try:
            require(run_git(root, ["rev-parse", "--verify", pin + "^{commit}"]).decode().strip() == pin,
                    "public evidence commit mismatch")
        except ValueError:
            missing.append(pin)
    if missing:
        refs = ["refs/retention/pins/" + pin + ":refs/retention/pins/" + pin for pin in missing]
        runner(root, [*PUBLIC_FETCH_PREFIX, *refs])
        for pin in missing:
            require(run_git(root, ["rev-parse", "--verify", pin + "^{commit}"]).decode().strip() == pin,
                    "public retained evidence unavailable")
    return missing


def _blob(root, ref, path):
    require(isinstance(ref, dict) and set(ref) == {"repository", "commit", "path", "sha256"} and
            ref["repository"].lower() == LOCAL and ref["path"] == path and PIN.fullmatch(ref["commit"]) and
            re.fullmatch(r"[0-9a-f]{64}", ref["sha256"]), "invalid producer reference")
    row = run_git(root, ["ls-tree", ref["commit"], "--", path]).split()
    require(row and row[0] in (b"100644", b"100755"), "producer path unavailable")
    data = run_git(root, ["show", ref["commit"] + ":" + path])
    require(hashlib.sha256(data).hexdigest() == ref["sha256"], "producer content mismatch")
    return data


def _core(value):
    return hashlib.sha256(json.dumps({k: v for k, v in value.items() if k not in {"review", "pin_inventory"}},
                                   sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def producer(root, base, destination, needed):
    if not needed:
        return None
    try:
        require(PIN.fullmatch(base), "immutable producer base required")
        value = decode(run_git(root, ["show", base + ":" + COMMISSIONING]))
        require(value["schema"] == "043-reviewed-trust-v1" and value["feature"] == "043-private-connectivity-production",
                "wrong source producer control")
        review = _blob(root, value["review"], AUTHENTICATION)
        blocks = re.findall(rb"^```json\r?\n(.*?)^```[ \t]*$", review, re.M | re.S)
        require(len(blocks) == 1, "producer authentication block required")
        auth = decode(blocks[0])
        require(set(auth) == {"schema", "decision", "custodian", "reviewed_manifest", "content_sha256", "reviewed_at"} and
                auth["schema"] == "043-source-authentication-v1" and auth["decision"] == "accepted" and
                auth["custodian"] == "Brett Heap", "producer not authenticated")
        reviewed_at = datetime.fromisoformat(auth["reviewed_at"].replace("Z", "+00:00"))
        require(reviewed_at.tzinfo is not None and reviewed_at <= datetime.now(timezone.utc), "future producer authentication")
        reviewed = decode(_blob(root, auth["reviewed_manifest"], COMMISSIONING))
        require(_core(value) == _core(reviewed) == auth["content_sha256"], "producer authentication mismatch")
        code = _blob(root, value["source_ci_producer"], SELF)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("trusted base has no authenticated source-CI producer") from exc
    require(not destination.is_symlink(), "linked producer destination")
    if destination.exists():
        require(destination.is_file() and destination.read_bytes() == code, "producer destination changed")
    else:
        destination.write_bytes(code)
    destination.chmod(0o600)
    return str(destination)


def check_population(path, pins):
    require(run_git(path, ["rev-parse", "--is-bare-repository"]).strip() == b"true", "proof must be bare")
    rows = run_git(path, ["cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype)"]).decode().splitlines()
    require(set(rows) == {pin + " commit" for pin in pins}, "proof contains missing/extra commits or private trees/blobs")


def validate_roots(coordinator, needed, raw):
    mapping = decode(raw)
    require(isinstance(mapping, dict) and set(mapping) == set(needed) and set(mapping) <= set(REPOSITORIES),
            "missing/unknown proof roots or coordinator override")
    identities = {coordinator.resolve()}
    for owner, value in mapping.items():
        require(isinstance(value, str), "invalid proof root")
        path = Path(value)
        require(path.is_absolute() and not path.is_symlink(), "absolute independent proof root required")
        resolved = path.resolve(strict=True)
        require(resolved not in identities and not resolved.is_relative_to(coordinator.resolve()), "aliased coordinator/owner proof")
        identities.add(resolved)
        require(origin(resolved) == owner, "wrong owner proof origin")
        check_population(resolved, needed[owner])
    return mapping


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("credentialed redirect refused")


def installation_repositories(token):
    req = request.Request("https://api.github.com/installation/repositories?per_page=100",
                          headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                                   "X-GitHub-Api-Version": "2022-11-28"})
    with request.build_opener(NoRedirect).open(req, timeout=20) as response:
        value = decode(response.read(1024 * 1024 + 1))
    require(value["total_count"] == len(value["repositories"]) <= len(REPOSITORIES), "incomplete/excess token scope")
    return value["repositories"]


def prepare(root, needed, directory, tokens, *, identities, api=installation_repositories, runner=run_git):
    require(needed == discover(root), "candidate inventory changed after planning")
    require(set(needed) <= set(REPOSITORIES) and needed, "closed nonempty owner proof required")
    groups = {owner.split("/")[0] for owner in needed}
    require(identities.get("app_id") == "4253636" and identities.get("app_slug") == "openxfactory", "wrong App identity")
    require(set(tokens) == groups and all(tokens.values()), "missing/extra private read token")
    for group in groups:
        require(identities.get(group) == INSTALLATIONS[group], "wrong installation identity")
        wanted = {name for name in needed if name.startswith(group + "/")}
        actual = api(tokens[group])
        require(len(actual) == len(wanted) and {r["full_name"].lower() for r in actual} == wanted and
                all(r["id"] == REPOSITORIES[r["full_name"].lower()] for r in actual), "token repository scope/identity mismatch")
    require(not directory.exists() and not directory.is_symlink(), "proof directory already exists")
    directory.mkdir(mode=0o700)
    (directory / MARKER).write_text("043-commit-proof-v1\n")
    mapping = {}
    try:
        for owner, pins in needed.items():
            path = directory / owner.replace("/", "--")
            path.mkdir(mode=0o700)
            runner(path, ["init", "--bare", "-q"])
            runner(path, ["remote", "add", "origin", GITHUB + owner + ".git"])
            runner(path, [*FETCH_PREFIX, *pins], tokens[owner.split("/")[0]])
            check_population(path, pins)
            mapping[owner] = str(path.resolve())
        return validate_roots(root, needed, json.dumps(mapping))
    except BaseException:
        cleanup(directory)
        raise


def cleanup(directory):
    require(not directory.is_symlink(), "linked proof cleanup refused")
    if directory.exists():
        require(directory.is_dir() and (directory / MARKER).is_file() and not (directory / MARKER).is_symlink() and
                (directory / MARKER).read_text() == "043-commit-proof-v1\n", "unowned proof cleanup refused")
        shutil.rmtree(directory)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("plan", "prepare", "cleanup", "history"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--base")
    parser.add_argument("--directory", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        parent = args.directory.parent.resolve(strict=True)
        require(parent == Path(os.environ["RUNNER_TEMP"]).resolve(strict=True), "proof must belong to runner temporary storage")
        require(args.directory.name == "pc043-source-proof", "unexpected proof directory")
        if args.mode == "history":
            hydrate_history(args.root); return 0
        if args.mode == "cleanup":
            cleanup(args.directory); return 0
        needed = discover(args.root)
        if args.mode == "plan":
            require(args.base, "trusted base revision required")
            script = parent / "pc043-reviewed-producer.py"
            selected = producer(args.root, args.base, script, needed)
            with open(os.environ["GITHUB_OUTPUT"], "a") as out:
                out.write("required=" + str(bool(needed)).lower() + "\n")
                out.write("producer=" + (selected or "") + "\n")
                for group in INSTALLATIONS:
                    out.write(group + "=" + ",".join(name.split("/")[1] for name in needed if name.startswith(group + "/")) + "\n")
        else:
            tokens = {group: os.environ[name] for group, name in (("opensoft", "PC_OPENSOFT_TOKEN"), ("codexfactory", "PC_DOMAIN_TOKEN"))
                      if os.environ.get(name)}
            identities = {"app_id": os.environ.get("PC_APP_ID"), "app_slug": os.environ.get("PC_APP_SLUG"),
                          "opensoft": os.environ.get("PC_OPENSOFT_INSTALLATION"), "codexfactory": os.environ.get("PC_DOMAIN_INSTALLATION")}
            mapping = prepare(args.root, needed, args.directory, tokens, identities=identities)
            with open(os.environ["GITHUB_ENV"], "a") as out:
                out.write("PC_SOURCE_PROOF_ROOTS=" + json.dumps(mapping, separators=(",", ":")) + "\n")
        return 0
    except (ValueError, OSError, KeyError, TypeError, RecursionError):
        # Never include exception text originating from HTTP/Git credentials.
        print("BLOCKED: source proof prerequisites or bounded operation failed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
