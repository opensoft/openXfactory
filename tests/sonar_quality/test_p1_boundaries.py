"""Counterexamples use disposable synthetic state; no browser/provider is used."""
from __future__ import annotations

import fcntl
import importlib.util
import json
import os
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(autouse=True)
def private_synthetic_creation():
    """Valid synthetic private state; unsafe-mode cases set their own modes."""
    previous = os.umask(0o077)
    try:
        yield
    finally:
        os.umask(previous)


@pytest.fixture
def auth(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "p1_auth_test_support", ROOT / "tests/notebooklm/test_nlm_auth.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setenv("NOTEBOOKLM_MCP_CLI_PATH", str(tmp_path / "native-store"))
    return module.nlm_auth


def save(auth, store, profile="safe"):
    return auth.write_native_profile(
        profile, [{"name": "synthetic", "value": "synthetic"}],
        "synthetic-csrf", "synthetic-session", store=store)


@pytest.mark.parametrize("name", ["../escape", "../../escape", ".", "..",
                                  "a/b", "a\\b", "--help", "", "a\nb"])
def test_profile_names_refuse_before_creating_state(auth, tmp_path, name):
    with pytest.raises((ValueError, OSError)):
        save(auth, tmp_path / "store", name)
    assert not (tmp_path / "store").exists()


def test_absolute_profile_refuses_before_creating_state(auth, tmp_path):
    with pytest.raises((ValueError, OSError)):
        save(auth, tmp_path / "store", str(tmp_path / "outside"))
    assert not (tmp_path / "store").exists()
    assert not (tmp_path / "outside").exists()


@pytest.mark.parametrize("target", ["store", "profiles", "profile"])
def test_linked_profile_ancestors_refuse(auth, tmp_path, target):
    store = tmp_path / "store"
    outside = tmp_path / "outside"
    outside.mkdir()
    if target == "store":
        store.symlink_to(outside, target_is_directory=True)
    elif target == "profiles":
        store.mkdir()
        (store / "profiles").symlink_to(outside, target_is_directory=True)
    else:
        (store / "profiles").mkdir(parents=True)
        (store / "profiles/safe").symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        save(auth, store)
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("leaf", ["cookies.json", "metadata.json"])
@pytest.mark.parametrize("kind", ["symlink", "hardlink"])
def test_linked_credential_files_refuse_without_any_write(auth, tmp_path, leaf, kind):
    store = tmp_path / "store"
    pdir = store / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original-cookie"]')
    (pdir / "metadata.json").write_text('{"email": "synthetic@example.invalid"}')
    outside = tmp_path / "outside.json"
    outside.write_text('{"synthetic": "original"}')
    (pdir / leaf).unlink()
    if kind == "symlink":
        (pdir / leaf).symlink_to(outside)
    else:
        os.link(outside, pdir / leaf)
    original = {p.name: p.read_bytes() for p in pdir.iterdir()}
    with pytest.raises((ValueError, OSError)):
        save(auth, store)
    assert outside.read_text() == '{"synthetic": "original"}'
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == original


def test_busy_profile_writer_refuses_without_touching_state(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original"]')
    descriptor = os.open(pdir, os.O_RDONLY | os.O_DIRECTORY)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises((ValueError, OSError)):
            save(auth, tmp_path)
        assert (pdir / "cookies.json").read_text() == '["original"]'
        assert sorted(p.name for p in pdir.iterdir()) == ["cookies.json"]
    finally:
        os.close(descriptor)


def test_wrong_account_keeps_modes_and_all_native_bytes(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    pdir.chmod(0o700)
    (pdir / "cookies.json").write_text('["original"]')
    (pdir / "metadata.json").write_text('{"email": "stored@example.invalid", "unknown": 42}')
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    with pytest.raises(auth.AccountMismatch):
        auth.write_native_profile("safe", [], "new", "new",
                                  email="different@example.invalid", store=tmp_path)
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before
    assert pdir.stat().st_mode & 0o777 == 0o700


def refuse_extractor(*args, **kwargs):
    raise AssertionError("unsafe input reached extractor/browser setup")


def test_browser_path_outside_invocation_refuses_before_setup(auth, tmp_path, monkeypatch):
    cwd = tmp_path / "invocation"
    cwd.mkdir()
    monkeypatch.chdir(cwd)
    monkeypatch.setattr(auth, "_load_cli_extractors", refuse_extractor)
    monkeypatch.setattr(sys, "argv", ["nlm_auth.py", "refresh",
                                     "--profile-dir", str(tmp_path / "outside")])
    with pytest.raises((ValueError, OSError)):
        auth.main()
    assert not (tmp_path / "outside").exists()


@pytest.mark.parametrize("marker", ["SingletonLock", "SingletonSocket",
                                   "SingletonCookie", "DevToolsActivePort"])
def test_occupied_browser_profile_refuses_before_setup(auth, tmp_path, monkeypatch, marker):
    monkeypatch.chdir(tmp_path)
    browser = tmp_path / "browser"
    browser.mkdir()
    (browser / marker).write_text("synthetic-live-owner")
    monkeypatch.setattr(auth, "_load_cli_extractors", refuse_extractor)
    monkeypatch.setattr(sys, "argv", ["nlm_auth.py", "refresh", "--profile-dir", str(browser)])
    with pytest.raises((ValueError, OSError)):
        auth.main()
    assert (browser / marker).read_text() == "synthetic-live-owner"
    assert browser.stat().st_mode & 0o777 == 0o700


def test_legitimate_profile_keeps_unknown_keys_and_private_creation(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "metadata.json").write_text('{"email": "stored@example.invalid", "unknown": {"x": 42}}')
    save(auth, tmp_path)
    metadata = json.loads((pdir / "metadata.json").read_text())
    assert metadata["email"] == "stored@example.invalid"
    assert metadata["unknown"] == {"x": 42}
    assert metadata["csrf_token"] == "synthetic-csrf"
    assert metadata["session_id"] == "synthetic-session"
    assert pdir.stat().st_mode & 0o777 == 0o700
    assert all(p.stat().st_mode & 0o777 == 0o600 for p in pdir.iterdir())


def test_fifo_metadata_refuses_before_read_or_write(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    os.mkfifo(pdir / "metadata.json")
    (pdir / "cookies.json").write_text('["original"]')
    with pytest.raises((ValueError, OSError)):
        auth.read_profile_metadata(pdir)
    with pytest.raises((ValueError, OSError)):
        save(auth, tmp_path)
    assert (pdir / "cookies.json").read_text() == '["original"]'


def test_second_staging_failure_keeps_native_pair_and_cleans_temporaries(auth, tmp_path, monkeypatch):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original"]')
    (pdir / "metadata.json").write_text('{"unknown": 42}')
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    from scripts import safe_tooling_io as io
    original = os.open
    staged = []

    def full_disk(path, flags, *args, **kwargs):
        if str(path).startswith(".nlm-"):
            staged.append(path)
            if len(staged) == 2:
                raise OSError("synthetic disk full while staging second file")
        return original(path, flags, *args, **kwargs)

    monkeypatch.setattr(io.os, "open", full_disk)
    # supports_dir_fd records built-ins, so this fault injection patches the
    # already-checked capability probe rather than weakening production checks.
    monkeypatch.setattr(io, "_require_descriptors", lambda: None)
    with pytest.raises(OSError, match="synthetic disk full"):
        save(auth, tmp_path)
    assert len(staged) == 2
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before


def test_credential_temp_files_are_private_at_creation_under_permissive_umask(auth, tmp_path, monkeypatch):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    from scripts import safe_tooling_io as io
    original = os.open
    modes = []

    def inspect_creation(path, flags, *args, **kwargs):
        fd = original(path, flags, *args, **kwargs)
        if str(path).startswith(".nlm-"):
            modes.append(os.fstat(fd).st_mode & 0o777)
        return fd

    monkeypatch.setattr(io.os, "open", inspect_creation)
    monkeypatch.setattr(io, "_require_descriptors", lambda: None)
    before = os.umask(0)
    try:
        save(auth, tmp_path)
    finally:
        os.umask(before)
    assert modes == [0o600, 0o600]


def test_foreign_writable_store_refuses_without_creating_profile(auth, tmp_path):
    store = tmp_path / "store"
    store.mkdir()
    store.chmod(0o777)
    with pytest.raises((ValueError, OSError)):
        save(auth, store)
    assert list(store.iterdir()) == []


def test_browser_invocation_root_itself_is_not_a_dedicated_profile(auth, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises((ValueError, OSError)):
        with auth.prepare_browser_profile(str(tmp_path)):
            pytest.fail("invocation root accepted")
    assert tmp_path.stat().st_mode & 0o777 == 0o700


def test_safe_browser_subdirectory_is_created_privately_without_startup(auth, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    chosen = tmp_path / "browser"
    with auth.prepare_browser_profile(str(chosen)) as anchored:
        assert os.path.samestat(anchored.stat(), chosen.stat())
    assert chosen.stat().st_mode & 0o777 == 0o700


@pytest.mark.parametrize("name", ["../escape", "a/b", "a\\b", "..", "", "\x00"])
def test_private_file_api_refuses_escaping_labels_before_staging(tmp_path, name):
    from scripts import safe_tooling_io as io
    with io.directory_handle(tmp_path, private=True) as descriptor:
        with pytest.raises(io.UnsafePath):
            io.atomic_private_files(descriptor, {name: b"synthetic"},
                                    expected={name: None})
    assert list(tmp_path.iterdir()) == []


def test_descriptor_walk_has_no_weaker_unsupported_fallback(tmp_path, monkeypatch):
    from scripts import safe_tooling_io as io
    monkeypatch.setattr(io, "fcntl", None)
    with pytest.raises(io.UnsafePath):
        with io.directory_handle(tmp_path / "state", create=True, private=True):
            pytest.fail("unsupported platform opened state")
    assert not (tmp_path / "state").exists()


def test_held_directory_is_not_redirected_by_parent_substitution(tmp_path):
    from scripts import safe_tooling_io as io
    selected = tmp_path / "selected"
    parked = tmp_path / "parked"
    outside = tmp_path / "outside"
    selected.mkdir()
    outside.mkdir()
    (outside / "metadata.json").write_bytes(b"outside sentinel")
    with io.directory_handle(selected, private=True) as descriptor:
        selected.rename(parked)
        selected.symlink_to(outside, target_is_directory=True)
        io.atomic_private_files(descriptor, {"metadata.json": b"new private bytes"},
                                expected={"metadata.json": None})
    assert (parked / "metadata.json").read_bytes() == b"new private bytes"
    assert (outside / "metadata.json").read_bytes() == b"outside sentinel"


def test_native_metadata_update_during_staging_is_preserved(auth, tmp_path, monkeypatch):
    from scripts import safe_tooling_io as io
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original"]')
    (pdir / "metadata.json").write_text('{"original": true}')
    original = os.open
    updated = []

    def concurrent_writer(path, flags, *args, **kwargs):
        if str(path).startswith(".nlm-") and not updated:
            (pdir / "metadata.json").write_text('{"concurrent": "must survive"}')
            updated.append(True)
        return original(path, flags, *args, **kwargs)

    monkeypatch.setattr(io.os, "open", concurrent_writer)
    monkeypatch.setattr(io, "_require_descriptors", lambda: None)
    with pytest.raises(io.UnsafePath, match="changed"):
        save(auth, tmp_path)
    assert (pdir / "cookies.json").read_text() == '["original"]'
    assert (pdir / "metadata.json").read_text() == '{"concurrent": "must survive"}'
    assert sorted(p.name for p in pdir.iterdir()) == ["cookies.json", "metadata.json"]


def test_serialization_failure_keeps_profile_modes_and_bytes(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    pdir.chmod(0o700)
    (pdir / "cookies.json").write_text('["original"]')
    (pdir / "metadata.json").write_text('{"unknown": 42}')
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    with pytest.raises(TypeError):
        auth.write_native_profile("safe", [object()], "new", "new", store=tmp_path)
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before
    assert pdir.stat().st_mode & 0o777 == 0o700


def test_oversized_metadata_refuses_before_cookie_write(auth, tmp_path):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original"]')
    payload = b" " * (1024 * 1024 + 1)
    (pdir / "metadata.json").write_bytes(payload)
    with pytest.raises((ValueError, OSError)):
        save(auth, tmp_path)
    assert (pdir / "cookies.json").read_text() == '["original"]'
    assert (pdir / "metadata.json").read_bytes() == payload


def test_browser_directory_link_is_refused_without_outside_changes(auth, tmp_path, monkeypatch):
    cwd = tmp_path / "invocation"
    outside = tmp_path / "outside"
    cwd.mkdir()
    outside.mkdir()
    (cwd / "browser").symlink_to(outside, target_is_directory=True)
    monkeypatch.chdir(cwd)
    with pytest.raises((ValueError, OSError)):
        with auth.prepare_browser_profile(str(cwd / "browser")):
            pytest.fail("linked browser accepted")
    assert list(outside.iterdir()) == []


def test_default_private_browser_state_is_authorized_independently_from_cwd(auth, tmp_path, monkeypatch):
    cwd = tmp_path / "invocation"
    cwd.mkdir()
    default = tmp_path / "private-default"
    monkeypatch.chdir(cwd)
    monkeypatch.setattr(auth, "DEFAULT_PROFILE_DIR", str(default))
    with auth.prepare_browser_profile(str(default)) as anchored:
        assert os.path.samestat(anchored.stat(), default.stat())
    assert default.stat().st_mode & 0o777 == 0o700


@pytest.mark.parametrize("leaf", ["cookies.json", "metadata.json"])
@pytest.mark.parametrize("mode", [0o400, 0o660])
def test_read_only_or_shared_write_credential_targets_preserve_native_state(auth, tmp_path, leaf, mode):
    pdir = tmp_path / "profiles/safe"
    pdir.mkdir(parents=True)
    (pdir / "cookies.json").write_text('["original"]')
    (pdir / "metadata.json").write_text('{"unknown": 42}')
    (pdir / leaf).chmod(mode)
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    with pytest.raises((ValueError, OSError)):
        save(auth, tmp_path)
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before
    assert (pdir / leaf).stat().st_mode & 0o777 == mode


@pytest.mark.parametrize("target", ["store", "profiles", "profile", "cookies.json", "metadata.json"])
def test_readable_private_state_refuses_before_setup_without_mode_changes(auth, tmp_path, monkeypatch, target):
    store = tmp_path / "store"
    pdir, _ = save(auth, store)
    selected = {"store": store, "profiles": pdir.parent, "profile": pdir}.get(target, pdir / target)
    mode = 0o755 if selected.is_dir() else 0o644
    selected.chmod(mode)
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    monkeypatch.setenv("NOTEBOOKLM_MCP_CLI_PATH", str(store))
    monkeypatch.setattr(auth, "_load_cli_extractors", refuse_extractor)
    monkeypatch.setattr(sys, "argv", ["nlm_auth.py", "refresh", "--profile", "safe", "--cdp-url", "http://127.0.0.1:9444"])
    with pytest.raises(ValueError, match="private"):
        auth.main()
    assert selected.stat().st_mode & 0o777 == mode
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before


def test_preflight_missing_store_is_read_only(auth, tmp_path):
    store = tmp_path / "not-created"
    token = auth.profile_generation("safe", store)
    assert token[1:] == (None, (None, None))
    assert not store.exists()


def test_preflight_inspects_existing_ancestors_even_when_profile_is_missing(auth, tmp_path):
    store = tmp_path / "store"
    store.mkdir(mode=0o755)
    store.chmod(0o755)
    with pytest.raises(ValueError, match="private"):
        auth.profile_generation("safe", store)
    assert not (store / "profiles").exists()


def test_older_capture_cannot_replace_newer_credentials(auth, tmp_path):
    store = tmp_path / "store"
    pdir, _ = save(auth, store)
    older = auth.profile_generation("safe", store)
    newer = auth.profile_generation("safe", store)
    auth.write_native_profile("safe", [], "newer-csrf", "newer-session",
                              store=store, expected_generation=newer)
    before = {p.name: p.read_bytes() for p in pdir.iterdir()}
    with pytest.raises(ValueError, match="since capture began"):
        auth.write_native_profile("safe", [], "older-csrf", "older-session",
                                  store=store, expected_generation=older)
    assert {p.name: p.read_bytes() for p in pdir.iterdir()} == before


def test_browser_anchor_survives_original_path_substitution(auth, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    browser, parked, outside = (tmp_path / name for name in ("browser", "parked", "outside"))
    outside.mkdir()
    with auth.prepare_browser_profile(str(browser)) as anchored:
        browser.rename(parked)
        browser.symlink_to(outside, target_is_directory=True)
        # Exercise a separate process, like Playwright's driver/browser.
        import subprocess
        subprocess.run([sys.executable, "-c",
                        "import pathlib,sys; (pathlib.Path(sys.argv[1])/'synthetic').write_text('anchored')",
                        str(anchored)], check=True)
        assert (parked / "synthetic").read_text() == "anchored"
        assert list(outside.iterdir()) == []
    assert not anchored.exists()


@pytest.mark.parametrize("cdp,mode,existing", [
    (False, "bootstrap", True), (False, "refresh", False),
    (True, "refresh", True), (True, "refresh", False),
])
def test_main_keeps_profile_anchor_and_closes_only_owned_browser(
        auth, tmp_path, monkeypatch, cdp, mode, existing):
    from contextlib import contextmanager
    from types import SimpleNamespace
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(auth, "_load_cli_extractors", lambda _: (None, None))
    monkeypatch.setattr(auth, "_load_email_extractor", lambda _: None)
    monkeypatch.setattr(auth.time, "sleep", lambda _: None)
    events = []
    page = SimpleNamespace(url=auth.NB_URL, goto=lambda *a, **k: events.append("navigate"))
    context = SimpleNamespace(pages=[page] if existing else [], new_page=lambda: page,
                              close=lambda: events.append("close"))
    browser = SimpleNamespace(contexts=[context] if existing else [], new_context=lambda: context)
    anchor = []

    def launch(path, **kwargs):
        assert Path(path).is_dir()
        anchor.append(Path(path))
        return context

    @contextmanager
    def driver():
        yield SimpleNamespace(chromium=SimpleNamespace(
            launch_persistent_context=launch, connect_over_cdp=lambda _: browser))
        events.append("driver-stop")

    def capture(*args, **kwargs):
        if not cdp:
            assert anchor[0].is_dir()
        assert kwargs["expected_generation"] == auth.profile_generation("safe")
        events.append("capture")
        return 0

    monkeypatch.setattr(auth, "sync_playwright", driver)
    monkeypatch.setattr(auth, "extract_and_save", capture)
    argv = ["nlm_auth.py", mode, "--profile", "safe", "--profile-dir",
            str(tmp_path / "browser"), "--channel", "bundled"]
    if cdp:
        argv += ["--cdp-url", "http://127.0.0.1:9444"]
    monkeypatch.setattr(sys, "argv", argv)
    assert auth.main() == 0
    assert events[-1] == "driver-stop"
    if cdp:
        assert "close" not in events
        assert not (tmp_path / "browser").exists()
    else:
        assert events.index("close") < events.index("driver-stop")
        assert not anchor[0].exists()
