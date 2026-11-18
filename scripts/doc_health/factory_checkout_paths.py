"""Translate the two assembly mount spellings while preserving stored source IDs."""

from pathlib import Path
import subprocess


RENAMED_MOUNTS = {
    Path("openxFactory"): Path("openXfactory"),
    Path("xFactories/codexFactory"): Path("xFactories/codeXfactory"),
}


def logical_path(relative: Path) -> Path:
    """Return the stable repository-relative key used by existing artifacts."""
    for legacy, canonical in RENAMED_MOUNTS.items():
        if relative.is_relative_to(canonical):
            return legacy / relative.relative_to(canonical)
    return relative


def _recorded_mount(root: Path, legacy: Path, canonical: Path) -> Path | None:
    result = subprocess.run(
        ["git", "-C", str(root.resolve()), "ls-tree", "HEAD", "--",
         str(legacy), str(canonical)],
        capture_output=True, text=True, check=False,
    )
    entries = result.stdout.splitlines()
    if result.returncode or len(entries) != 1 or not entries[0].startswith("160000 commit "):
        return None
    return Path(entries[0].split("\t", 1)[1])


def _local_mount(root: Path, legacy: Path, canonical: Path) -> Path:
    previous, current = root / legacy, root / canonical
    if not current.is_dir():
        return previous
    if not previous.is_dir() or previous.resolve() == current.resolve():
        return current
    if not (previous / ".git").exists():
        return current
    if not (current / ".git").exists():
        return previous
    recorded = _recorded_mount(root, legacy, canonical)
    if recorded is None:
        raise ValueError(f"cannot choose between independent checkouts {previous} and {current}")
    return root / recorded


def checkout_path(root: Path, relative: Path | str) -> Path:
    """Find the mounted path for a recorded key on either assembly revision."""
    relative = Path(relative)
    for legacy, canonical in RENAMED_MOUNTS.items():
        if relative.is_relative_to(legacy):
            return _local_mount(root, legacy, canonical) / relative.relative_to(legacy)
    return root / relative


def checkout_name(path: Path) -> str:
    """Keep historical report IDs for the two registered assembly mounts."""
    root = path.parent.parent if path.parent.name == "xFactories" else path.parent
    relative = path.relative_to(root)
    legacy = logical_path(relative)
    if legacy != relative and (root / ".gitmodules").is_file():
        if _recorded_mount(root, legacy, relative) == relative:
            return legacy.name
    return path.name
