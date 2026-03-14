#!/usr/bin/env python3
"""Report exact duplicate files inside a directory using SHA-256."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import os
from collections import defaultdict
from pathlib import Path


def should_ignore(rel_path: str, ignore_globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel_path, pattern) for pattern in ignore_globs)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find exact duplicate files inside a folder by SHA-256."
    )
    parser.add_argument("--base", required=True, help="Base directory to scan")
    parser.add_argument(
        "--ignore-glob",
        action="append",
        default=[],
        help="Glob pattern relative to base to skip. Repeatable.",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include dotfiles and files inside hidden directories.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    base = Path(args.base).expanduser().resolve()
    if not base.is_dir():
        parser.error(f"Base directory does not exist: {base}")

    hashes: dict[str, list[str]] = defaultdict(list)

    for root, dirs, files in os.walk(base):
        root_path = Path(root)
        rel_root = root_path.relative_to(base)

        if not args.include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            files = [f for f in files if not f.startswith(".")]

        for name in files:
            full_path = root_path / name
            rel_path = str((rel_root / name).as_posix()) if rel_root != Path(".") else name

            if should_ignore(rel_path, args.ignore_glob):
                continue

            try:
                digest = sha256_file(full_path)
            except OSError as exc:
                print(f"[skip] {rel_path}: {exc}")
                continue

            hashes[digest].append(rel_path)

    duplicate_groups = [(digest, sorted(paths)) for digest, paths in hashes.items() if len(paths) > 1]
    duplicate_groups.sort(key=lambda item: item[1][0])

    if not duplicate_groups:
        print("No exact duplicates found.")
        return 0

    for digest, paths in duplicate_groups:
        print(digest)
        for rel_path in paths:
            print(f"  {rel_path}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
