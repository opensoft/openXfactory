"""Fail-closed, import-safe boundaries for the maintained AT-R1 replay driver."""
from __future__ import annotations

from contextlib import ExitStack
import html
import os
from pathlib import Path
import re
import stat
import urllib.parse

PRIVATE_COPY_LIMIT = 1024 * 1024


class PreflightError(ValueError):
    """The replay cannot safely reach an acceptance verdict."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PreflightError(message)


def prepare_output_directory(raw: str, label: str) -> Path:
    require(label in ("a", "b"), "the replay label must be a or b")
    try:
        out = Path(raw).resolve()
        require(out.is_relative_to(Path.cwd().resolve()),
                "the output must stay inside the invocation directory")
        out.mkdir(mode=0o700, parents=True, exist_ok=True)
        info = out.stat()
        require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.getuid()
                and stat.S_IMODE(info.st_mode) == 0o700,
                "the output must be this user's private mode-700 directory")
        require(not os.path.lexists(out / f"{label}-result.json"),
                "the output already holds a result; use a new evidence directory")
    except (OSError, RuntimeError) as exc:
        raise PreflightError("the invocation output cannot be safely prepared") from exc
    return out


def write_output(out: Path, name: str, data: bytes) -> Path:
    require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", name) is not None,
            "the output filename is not a plain safe name")
    try:
        with ExitStack() as stack:
            directory = os.open(out, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            stack.callback(os.close, directory)
            info = os.fstat(directory)
            require(info.st_uid == os.getuid()
                    and stat.S_IMODE(info.st_mode) == 0o700,
                    "the output directory is not private")
            # New evidence is never allowed to truncate a prior receipt or
            # follow a file symlink/hardlink supplied by another operation.
            descriptor = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL
                                 | os.O_NOFOLLOW, 0o600, dir_fd=directory)
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(data)
    except OSError as exc:
        raise PreflightError("a new output file could not be written safely") from exc
    return out / name


def _private_descriptor(info, mode: int, directory: bool) -> None:
    correct_type = stat.S_ISDIR(info.st_mode) if directory else stat.S_ISREG(info.st_mode)
    require(correct_type and info.st_uid == os.getuid()
            and stat.S_IMODE(info.st_mode) == mode,
            f"the private copy component is not this user's own mode-{mode:o} "
            + ("directory" if directory else "regular file"))


def read_private_copy(copy: str, port: int) -> str:
    declared = os.environ.get("OPENDOX_STATE_DIR")
    if not declared:
        raise PreflightError("OPENDOX_STATE_DIR must declare the private state root")
    require(1 <= port <= 65535, "the private copy port is invalid")
    try:
        state = Path(declared).resolve(strict=True)
        expected = state / "console" / f"{port}.html"
        # The CLI cannot repoint the read to a different state/file. Resolve
        # the trusted state, then open only fixed names relative to its fds.
        supplied = Path(os.path.abspath(copy))
        require(supplied == expected, "the copy is not the declared private console file")
        with ExitStack() as stack:
            root_fd = os.open(state, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            stack.callback(os.close, root_fd)
            _private_descriptor(os.fstat(root_fd), 0o700, True)
            console_fd = os.open("console", os.O_RDONLY | os.O_DIRECTORY
                                 | os.O_NOFOLLOW, dir_fd=root_fd)
            stack.callback(os.close, console_fd)
            _private_descriptor(os.fstat(console_fd), 0o700, True)
            descriptor = os.open(f"{port}.html", os.O_RDONLY | os.O_NOFOLLOW
                                 | os.O_NONBLOCK, dir_fd=console_fd)
            with os.fdopen(descriptor, "rb") as stream:
                _private_descriptor(os.fstat(stream.fileno()), 0o600, False)
                raw = stream.read(PRIVATE_COPY_LIMIT + 1)
            require(len(raw) <= PRIVATE_COPY_LIMIT, "the private copy exceeds its size limit")
            text = raw.decode("utf-8")
    except (OSError, UnicodeError, RuntimeError) as exc:
        raise PreflightError("the declared private copy cannot be safely read") from exc
    require(all(match.start() > 0 and text[match.start() - 1] == "#"
                for match in re.finditer("console_token=", text)),
            "the private copy puts the token outside a fragment")
    target = re.search(r"""(?i)http-equiv=["']?refresh["']?\s+content=["']\s*\d+\s*;\s*url=([^"']+)""", text)
    if target is None:
        raise PreflightError("the private copy forwards to no page")
    try:
        url = urllib.parse.urlsplit(html.unescape(target.group(1)))
    except ValueError as exc:
        raise PreflightError("the private copy has an invalid forwarding URL") from exc
    require((url.scheme, url.netloc, url.path, url.query)
            == ("http", f"127.0.0.1:{port}", "/index.html", ""),
            "the private copy does not forward to this server's index with an empty query")
    token = urllib.parse.parse_qs(url.fragment).get("console_token", [""])[0]
    require(bool(token), "the opened URL carries no token in its fragment")
    return token


def opened_through(copy: str, copy_url: str | None) -> str:
    if not copy_url:
        return Path(copy).as_uri()
    try:
        parts = urllib.parse.urlsplit(copy_url)
    except ValueError as exc:
        raise PreflightError("the printed console URL is invalid") from exc
    require(parts.scheme == "file" and parts.netloc in ("", "localhost")
            and not parts.query and not parts.fragment,
            "the printed console URL is not a plain file URL")
    named = Path(os.path.abspath(urllib.parse.unquote(parts.path)))
    require(named == Path(copy), "the printed console URL does not name the private copy")
    require("console_token" not in copy_url, "the printed console URL carries the token")
    return copy_url
