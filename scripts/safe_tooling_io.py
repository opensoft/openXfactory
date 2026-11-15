"""Descriptor-relative filesystem operations for maintained security tooling."""
from __future__ import annotations

from contextlib import contextmanager
import os
import re
from pathlib import Path
import secrets
import stat

try:
    import fcntl
except ImportError:  # No weaker path-based fallback.
    fcntl = None


class UnsafePath(ValueError):
    """The selected filesystem object has no acceptable authority."""


def _require_descriptors():
    if (fcntl is None or not hasattr(os, "O_NOFOLLOW")
            or not hasattr(os, "O_DIRECTORY")
            or not {os.open, os.mkdir, os.stat, os.unlink} <= os.supports_dir_fd):
        raise UnsafePath("safe POSIX filesystem operations are unavailable")


def _component(name):
    if (not isinstance(name, str) or not name or name in (".", "..")
            or any(ord(character) in (0, 47, 92) for character in name)):
        raise UnsafePath("file name must be one component")
    return name


def _private_directory(fd):
    info = os.fstat(fd)
    if info.st_uid != os.geteuid() or info.st_mode & 0o077:
        raise UnsafePath("private directory is foreign-owned or accessible by others")


@contextmanager
def directory_handle(path, *, create=False, private=False):
    """Walk every component without following links and retain the final inode."""
    _require_descriptors()
    path = Path(path).expanduser().absolute()
    if ".." in path.parts:
        raise UnsafePath("parent path components are not authorized")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(path.anchor, flags)
    try:
        for component in path.parts[1:]:
            try:
                child = os.open(component, flags, dir_fd=fd)
            except FileNotFoundError:
                if not create:
                    raise
                os.mkdir(component, 0o700, dir_fd=fd)
                child = os.open(component, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        if private:
            _private_directory(fd)
        yield fd
    finally:
        os.close(fd)


@contextmanager
def private_child(parent_fd, name, *, create=False):
    _require_descriptors()
    # Native profiles use the same bounded identifier grammar at the sink.
    # A descriptor confines the parent; this grammar also rules out absolute
    # paths, separators, dot components and control characters in the leaf.
    if not isinstance(name, str) or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", name) is None:
        raise UnsafePath("private child must be a bounded profile identifier")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    try:
        fd = os.open(name, flags, dir_fd=parent_fd)
    except FileNotFoundError:
        if not create:
            raise
        os.mkdir(name, 0o700, dir_fd=parent_fd)
        fd = os.open(name, flags, dir_fd=parent_fd)
    try:
        _private_directory(fd)
        yield fd
    finally:
        os.close(fd)


@contextmanager
def exclusive_writer(directory_fd):
    try:
        fcntl.flock(directory_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise UnsafePath("profile already has an active writer") from exc
    try:
        yield
    finally:
        fcntl.flock(directory_fd, fcntl.LOCK_UN)


def _owned_regular(info, *, writable=False):
    if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid()
            or info.st_nlink != 1 or info.st_mode & 0o077):
        raise UnsafePath("private file must be regular, owned, private and single-link")
    if writable and not info.st_mode & stat.S_IWUSR:
        raise UnsafePath("read-only credential state cannot be replaced")


def target_signature(directory_fd, name):
    _component(name)
    try:
        info = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None
    _owned_regular(info, writable=True)
    return info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns


def read_private_file(directory_fd, name, *, limit=1024 * 1024):
    _component(name)
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                     dir_fd=directory_fd)
    except FileNotFoundError:
        return None
    with os.fdopen(fd, "rb") as stream:
        _owned_regular(os.fstat(stream.fileno()))
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise UnsafePath("private metadata exceeds the bounded read size")
    return data


def atomic_private_files(directory_fd, contents, *, expected):
    """Stage every file privately, then replace individual native-format files."""
    for name in contents:
        _component(name)
    staged = {}
    try:
        for name, data in contents.items():
            temporary = ".nlm-" + secrets.token_hex(16)
            fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL
                         | os.O_NOFOLLOW, 0o600, dir_fd=directory_fd)
            staged[name] = temporary
            with os.fdopen(fd, "wb") as stream:
                os.fchmod(stream.fileno(), 0o600)
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
        for name in contents:
            if target_signature(directory_fd, name) != expected[name]:
                raise UnsafePath("native profile changed while preparing its update")
        for name, temporary in staged.items():
            os.replace(temporary, name, src_dir_fd=directory_fd,
                       dst_dir_fd=directory_fd)
        os.fsync(directory_fd)
    finally:
        for temporary in staged.values():
            try:
                os.unlink(temporary, dir_fd=directory_fd)
            except FileNotFoundError:
                pass
