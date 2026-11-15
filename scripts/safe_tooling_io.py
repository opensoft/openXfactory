"""Descriptor-relative filesystem operations for maintained security tooling."""
from __future__ import annotations

from contextlib import contextmanager
import os
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
    _component(name)
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
        raise UnsafePath("directory already has an active writer") from exc
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


# Non-secret maintained artifacts retain their normal access mode. These APIs
# take trusted library-selected paths/roots; CLI entrypoints additionally bind
# every model-supplied operand to the controller's invocation scope below.
_ARTIFACT_LIMIT = 16 * 1024 * 1024


def _absolute_operand(path):
    result = Path(path).expanduser()
    if ".." in result.parts:
        raise UnsafePath("parent path components are not authorized")
    return result.absolute()


def _artifact_location(path, root=None):
    path = _absolute_operand(path)
    root = _absolute_operand(root) if root is not None else path.parent
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise UnsafePath("artifact is outside its declared root") from exc
    for component in relative.parts:
        _component(component)
        if any(ord(character) < 32 for character in component):
            raise UnsafePath("control characters are not valid artifact names")
    return path


def _regular_artifact(info, *, writing=False):
    if (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1
            or info.st_mode & 0o7000):
        raise UnsafePath("artifact must be a regular single-link file")
    if writing and (info.st_uid != os.geteuid()
                    or not info.st_mode & stat.S_IWUSR or info.st_mode & 0o022):
        raise UnsafePath("artifact is foreign-owned, shared-write or read-only")


def _signature(info):
    if info is None:
        return None
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns,
            info.st_ctime_ns, info.st_mode, info.st_uid)


def _artifact_stat(directory_fd, name):
    try:
        info = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None
    _regular_artifact(info)
    return info


def _artifact_bytes(directory_fd, name, *, allow_missing=False):
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                     dir_fd=directory_fd)
    except FileNotFoundError:
        if allow_missing:
            return None, None
        raise
    with os.fdopen(fd, "rb") as stream:
        before = os.fstat(stream.fileno())
        _regular_artifact(before)
        data = stream.read(_ARTIFACT_LIMIT + 1)
        after = os.fstat(stream.fileno())
    if len(data) > _ARTIFACT_LIMIT:
        raise UnsafePath("artifact exceeds the bounded read size")
    if _signature(before) != _signature(after):
        raise UnsafePath("artifact changed while it was being read")
    return data, after


def validate_artifact_path(path, *, root=None, directory=False,
                           writing=False, required=False):
    """Inspect existing components without creating anything or following links."""
    path = _artifact_location(path, root)
    _require_descriptors()
    fd = os.open(path.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        parts = path.parts[1:]
        for index, name in enumerate(parts):
            _component(name)
            try:
                info = os.stat(name, dir_fd=fd, follow_symlinks=False)
            except FileNotFoundError:
                if required:
                    raise UnsafePath("required artifact location is absent")
                return path
            final = index == len(parts) - 1
            if not final or directory:
                if not stat.S_ISDIR(info.st_mode):
                    raise UnsafePath("artifact directory is linked or non-regular")
                child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                dir_fd=fd)
                os.close(fd)
                fd = child
                if final and writing and (info.st_uid != os.geteuid()
                                          or not info.st_mode & stat.S_IWUSR):
                    raise UnsafePath("artifact directory is foreign-owned or read-only")
            else:
                _regular_artifact(info, writing=writing)
        return path
    finally:
        os.close(fd)


def invocation_operand(value, *, directory=False, writing=False, required=False,
                       allow_runner_temp=False):
    """Return a canonical operand under controller-owned invocation authority."""
    root = Path.cwd().resolve()
    selected = _absolute_operand(value)
    # A verified spelling of the root is only an alias: all later operations
    # use the canonical root, never the supplied alias or its mutable target.
    relative = None
    for ancestor in reversed((selected, *selected.parents)):
        try:
            same_root = ancestor.resolve() == root
        except (OSError, RuntimeError):
            same_root = False
        if same_root:
            relative = selected.relative_to(ancestor)
            break
    if relative is None:
        scratch = os.environ.get("RUNNER_TEMP") if allow_runner_temp else None
        if scratch:
            trusted = _absolute_operand(scratch).resolve()
            if trusted == Path(trusted.anchor):
                raise UnsafePath("CI scratch root cannot be a filesystem root")
            try:
                selected.relative_to(trusted)
            except ValueError:
                pass
            else:
                validate_artifact_path(trusted, directory=True, writing=True, required=True)
                return validate_artifact_path(selected, root=trusted, directory=directory,
                                              writing=writing, required=required)
        raise UnsafePath("operand is outside the invocation root")
    canonical = _artifact_location(root / relative, root)
    return validate_artifact_path(canonical, root=root, directory=directory,
                                  writing=writing, required=required)


def bind_cli_paths(namespace, *, paths=(), directories=(), outputs=(),
                   required=()):
    for name in paths:
        value = getattr(namespace, name, None)
        if value is not None:
            selected = invocation_operand(
                value, directory=name in directories, writing=name in outputs,
                required=name in required, allow_runner_temp=name in outputs)
            setattr(namespace, name, str(selected))


def operator_input_operand(value, *, setting, default):
    """A model operand can name the configured input, never choose another policy."""
    configured = os.environ.get(setting)
    if configured is None:
        configured = default
    if configured is None:
        raise UnsafePath("no operator-selected policy input is configured")
    expected = _absolute_operand(configured)
    # Parent aliases belong to trusted launch configuration; preserve the
    # expected leaf so linked policy files still refuse.
    expected = expected.parent.resolve() / expected.name
    supplied = _absolute_operand(value)
    try:
        matches = supplied.resolve() == expected.resolve()
    except (OSError, RuntimeError):
        matches = False
    if not matches:
        raise UnsafePath("policy operand differs from operator configuration: " + setting)
    return validate_artifact_path(expected)


def ensure_artifact_directory(path, *, root=None):
    path = _artifact_location(path, root)
    validate_artifact_path(path, root=root, directory=True, writing=True)
    try:
        with directory_handle(path, create=True):
            pass
    except OSError as exc:
        # Namespace substitution must not turn into an optional worker skip.
        import errno
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            raise UnsafePath("artifact directory was substituted") from exc
        raise
    return path


def read_artifact_text(path, *, root=None):
    path = _artifact_location(path, root)
    validate_artifact_path(path, root=root)
    try:
        with directory_handle(path.parent) as descriptor:
            data, _info = _artifact_bytes(descriptor, path.name)
    except OSError as exc:
        import errno
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            raise UnsafePath("artifact was substituted") from exc
        raise
    return data.decode("utf-8")


def update_artifact_text(path, transform, *, root=None, create=False):
    """Hold the original and its parent while preparing a compare-and-replace."""
    path = _artifact_location(path, root)
    validate_artifact_path(path, root=root)
    temporary = None
    try:
        with directory_handle(path.parent) as descriptor:
            with exclusive_writer(descriptor):
                before_bytes, before = _artifact_bytes(
                    descriptor, path.name, allow_missing=create)
                original = "" if before_bytes is None else before_bytes.decode("utf-8")
                updated = transform(original)
                if not isinstance(updated, str):
                    raise TypeError("artifact transform must return text")
                if updated == original and before is not None:
                    return False
                if before is not None:
                    _regular_artifact(before, writing=True)
                temporary = ".artifact-" + secrets.token_hex(16)
                try:
                    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL
                                 | os.O_NOFOLLOW, 0o600, dir_fd=descriptor)
                    with os.fdopen(fd, "wb") as stream:
                        stream.write(updated.encode("utf-8"))
                        stream.flush()
                        os.fchmod(stream.fileno(),
                                  stat.S_IMODE(before.st_mode) if before else 0o644)
                        os.fsync(stream.fileno())
                    if _signature(_artifact_stat(descriptor, path.name)) != _signature(before):
                        raise UnsafePath("artifact changed while preparing its update")
                    os.replace(temporary, path.name, src_dir_fd=descriptor,
                               dst_dir_fd=descriptor)
                    temporary = None
                    os.fsync(descriptor)
                finally:
                    if temporary is not None:
                        os.unlink(temporary, dir_fd=descriptor)
                return True
    except OSError as exc:
        import errno
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            raise UnsafePath("artifact was substituted") from exc
        raise


def write_artifact_text(path, text, *, root=None):
    return update_artifact_text(path, lambda _original: text, root=root, create=True)
