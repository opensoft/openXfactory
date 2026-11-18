"""#869: `corpus.discover_repos` reaches the root-level governed products.

`ROOT_LEVEL_GOVERNED_PRODUCTS` has named `openAvatar` and `openXwallet` as
governed repositories since `split-openxwallet-repo` § 11.2, and two widened
sites read it. `discover_repos` — the enumerator that decides which
repositories an aggregation-rooted sweep actually MEASURES — was not one of
them, so `doc-health.py --repo-root <aggregation>` swept `openxFactory` plus
`xFactories/*` and nothing else. Measured on the 2026-09-09 estate runs (#765,
#731, #859): both products had to be measured by separate `--single-repo`
invocations to be measured at all.

The aggregation fixtures here are built with `tmp_path` rather than checked in,
because what is under test is DIRECTORY SHAPE — present/absent, materialized/
unmaterialized — which a fixture tree cannot express (an empty directory does
not survive git, and a nested `.git` marker in a checked-in fixture is its own
hazard).
"""

from __future__ import annotations

import pytest

from doc_health import corpus
from doc_health import ideation_routing


def _repo(path):
    """A materialized submodule checkout: a directory carrying `.git`.

    `.git` is a FILE in a submodule worktree and a directory in a plain clone;
    `discover_repos` tests `exists()`, so a file is the honest fixture."""
    path.mkdir(parents=True, exist_ok=True)
    (path / ".git").write_text("gitdir: ../.git/modules/x\n", encoding="utf-8")
    return path


@pytest.fixture
def agg(tmp_path):
    """An aggregation root with openxFactory and two pinned domain repos."""
    _repo(tmp_path / "openxFactory")
    _repo(tmp_path / "xFactories" / "MedxFactory")
    _repo(tmp_path / "xFactories" / "codexFactory")
    return tmp_path


def _names(root):
    return [name for name, _path in corpus.discover_repos(root)]


def test_a_materialized_root_level_product_is_enumerated(agg):
    """The #869 fix: `openXwallet/` beside `openxFactory/` is swept."""
    _repo(agg / "openXwallet")
    names = _names(agg)
    assert "openXwallet" in names
    assert dict(corpus.discover_repos(agg))["openXwallet"] == agg / "openXwallet"


def test_an_absent_root_level_product_is_skipped_silently(agg):
    """An aggregation that does not pin the product, or a checkout that has
    not materialized it, enumerates without it and without complaint — the
    enumerator's job is to list what is here, not to audit the pin set."""
    assert "openXwallet" not in _names(agg)
    assert "openAvatar" not in _names(agg)


def test_an_unmaterialized_root_level_product_is_skipped(agg):
    """An unmaterialized submodule leaves an EMPTY DIRECTORY behind. Admitting
    it would put a repository into `repo_paths`, `capabilities` and the report
    that contributes no document — a repository the run claims to have
    measured and did not."""
    (agg / "openXwallet").mkdir()
    assert "openXwallet" not in _names(agg)


def test_both_allowlisted_products_are_enumerated_when_both_are_present(agg):
    _repo(agg / "openAvatar")
    _repo(agg / "openXwallet")
    assert {"openAvatar", "openXwallet"} <= set(_names(agg))


def test_the_allowlist_is_the_rule_and_not_the_root_directory_listing(agg):
    """AN ALLOWLIST, NOT A RULE (`ROOT_LEVEL_GOVERNED_PRODUCTS`' own comment).
    "Every root-level pin is a governed repository" is one line shorter and
    would enrol the nine `installs/*` runtime repositories, each of which is
    classified `external` on purpose."""
    _repo(agg / "openNotAProduct")
    _repo(agg / "installs" / "agenttower")
    names = _names(agg)
    assert "openNotAProduct" not in names
    assert "agenttower" not in names
    assert not any(n.startswith("installs") for n in names)


def test_a_root_product_id_is_the_bare_name_never_xfactories_prefixed(agg):
    """The two widened sites must agree about a product's ID.
    `ideation_routing._governed_repo_ids` anticipated this widening and
    tolerates an allowlisted name in `repo_paths` unprefixed — "a silent
    `xFactories/openXwallet` would be a repository that exists nowhere" — so
    the round trip through it is the agreement, pinned."""
    _repo(agg / "openXwallet")
    repo_paths = dict(corpus.discover_repos(agg))
    assert "openXwallet" in repo_paths
    ids = ideation_routing._governed_repo_ids(
        type("Ctx", (), {"repo_paths": repo_paths})())
    assert "openXwallet" in ids
    assert "xFactories/openXwallet" not in ids
    assert "xFactories/MedxFactory" in ids


def test_the_xfactories_container_behaviour_is_unchanged(agg):
    """The widening adds a source; it changes none of the existing one.
    Children are admitted sorted, on the same materialization check, and a
    non-repository directory under the container is still skipped."""
    (agg / "xFactories" / "not-a-repo").mkdir()
    _repo(agg / "openXwallet")
    names = _names(agg)
    assert "not-a-repo" not in names
    assert [n for n in names if n in ("MedxFactory", "codexFactory")] == [
        "MedxFactory", "codexFactory"]
    assert names[0] == "openxFactory", "openxFactory stays the first entry"


def test_openxfactory_keeps_its_laxer_admission(tmp_path):
    """A DELIBERATE ASYMMETRY, pinned so it is not "tidied" away: openxFactory
    is the aggregation's anchor rather than one repository among many, and
    every fixture aggregation in this suite is a plain directory tree with no
    `.git` anywhere. Requiring materialization of it would make those
    unreadable."""
    (tmp_path / "openxFactory").mkdir()
    assert _names(tmp_path) == ["openxFactory"]


def test_an_aggregation_with_nothing_in_it_enumerates_nothing(tmp_path):
    assert corpus.discover_repos(tmp_path) == []


@pytest.mark.parametrize("mount", ["openXfactory", "openxFactory"])
def test_neutral_checkout_mount_preserves_the_corpus_identity(tmp_path, mount):
    checkout = tmp_path / mount
    checkout.mkdir()
    assert corpus.discover_repos(tmp_path) == [("openxFactory", checkout)]


@pytest.mark.parametrize("mount", ["codeXfactory", "codexFactory"])
def test_engineering_checkout_keeps_the_catalog_repository_id(tmp_path, mount):
    checkout = _repo(tmp_path / "xFactories" / mount)
    assert corpus.discover_repos(tmp_path) == [("codexFactory", checkout)]


@pytest.mark.parametrize("mount", ["openXfactory", "openxFactory"])
def test_notebook_dry_run_opens_the_selected_mount(tmp_path, monkeypatch, mount):
    from types import SimpleNamespace

    from doc_health import runner

    checkout = tmp_path / mount
    script = checkout / runner.SYNC_SCRIPT
    script.parent.mkdir(parents=True)
    script.touch()
    calls = []

    def run(argv, **kwargs):
        calls.append((argv, kwargs.get("cwd")))
        return SimpleNamespace(returncode=0, stdout="fixture plan")

    monkeypatch.setattr(runner.subprocess, "run", run)
    assert runner._real_notebook_dryrun(tmp_path)() == "fixture plan"
    assert calls == [
        (["nlm", "notebook", "list"], None),
        (["python3", str(script), "."], tmp_path),
    ]


def test_empty_canonical_alias_does_not_hide_a_legacy_checkout(tmp_path):
    for path in ("openXfactory", "xFactories/codeXfactory"):
        (tmp_path / path).mkdir(parents=True)
    neutral = _repo(tmp_path / "openxFactory")
    engineering = _repo(tmp_path / "xFactories/codexFactory")
    assert corpus.discover_repos(tmp_path) == [
        ("openxFactory", neutral), ("codexFactory", engineering)]


@pytest.mark.parametrize("recorded", ["openxFactory", "openXfactory"])
def test_two_materialized_mounts_use_the_recorded_checkout(tmp_path, recorded):
    import subprocess

    from doc_health.factory_checkout_paths import checkout_name

    for mount in ("openxFactory", "openXfactory"):
        _repo(tmp_path / mount)

    def git(*args):
        return subprocess.run(["git", "-C", str(tmp_path), *args],
                              capture_output=True, text=True, check=True)

    git("init", "-q")
    (tmp_path / ".gitmodules").write_text(
        f'[submodule "openxFactory"]\n\tpath = {recorded}\n'
        "\turl = git@github.com:opensoft/openXfactory.git\n",
        encoding="utf-8")
    git("add", ".gitmodules")
    git("update-index", "--add", "--cacheinfo", f"160000,{'a' * 40},{recorded}")
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
        "-c", "commit.gpgsign=false", "commit", "-qm", "record neutral provider")
    assert corpus.discover_repos(tmp_path) == [("openxFactory", tmp_path / recorded)]
    assert checkout_name(tmp_path / recorded) == "openxFactory"
    standalone = tmp_path.parent / "standalone" / "openXfactory"
    assert checkout_name(standalone) == "openXfactory"


def test_dashboard_refresh_default_follows_the_neutral_mount(tmp_path):
    from ideation_dashboard.dashboard_refresh_lane import _corpus_checkout

    canonical = tmp_path / "openXfactory"
    canonical.mkdir()
    assert _corpus_checkout(tmp_path, None) == canonical
    assert _corpus_checkout(tmp_path, "explicit") == tmp_path / "explicit"
