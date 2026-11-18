"""Translate the two assembly mount spellings while preserving stored source IDs."""

from pathlib import Path


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


def checkout_path(root: Path, relative: Path | str) -> Path:
    """Find the mounted path for a recorded key on either assembly revision."""
    relative = Path(relative)
    for legacy, canonical in RENAMED_MOUNTS.items():
        if not relative.is_relative_to(legacy):
            continue
        mounted = root / canonical
        if mounted.is_dir() and (
            (mounted / ".git").exists() or not (root / legacy / ".git").exists()
        ):
            return mounted / relative.relative_to(legacy)
    return root / relative
