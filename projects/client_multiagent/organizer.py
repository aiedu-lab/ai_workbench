#!/usr/bin/env python3
"""
Organize files in a directory into subdirectories by creation month (YYYY-MM).
Files are moved, not deleted. Subdirectories are never touched.
"""

import shutil
import argparse
from datetime import datetime
from pathlib import Path


def get_file_date(path: Path) -> datetime:
    stat = path.stat()
    # st_birthtime is available on macOS; fall back to st_mtime on Linux
    timestamp = getattr(stat, "st_birthtime", None) or stat.st_mtime
    return datetime.fromtimestamp(timestamp)


def organize(source_dir: Path, dry_run: bool) -> None:
    if not source_dir.is_dir():
        raise ValueError(f"Not a directory: {source_dir}")

    moved = 0
    skipped = 0

    for entry in sorted(source_dir.iterdir()):
        if entry.is_dir():
            continue  # never touch subdirectories

        file_date = get_file_date(entry)
        folder_name = file_date.strftime("%Y-%m")
        dest_dir = source_dir / folder_name
        dest_path = dest_dir / entry.name

        if dest_path.exists():
            print(f"  SKIP  {entry.name} -> {folder_name}/ (destination already exists)")
            skipped += 1
            continue

        print(f"  {'MOVE' if not dry_run else 'DRY '} {entry.name} -> {folder_name}/")

        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(entry), dest_path)

        moved += 1

    print(f"\n{'Would move' if dry_run else 'Moved'} {moved} file(s), skipped {skipped}.")


def main():
    parser = argparse.ArgumentParser(
        description="Move files into YYYY-MM subdirectories based on creation date."
    )
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would happen without moving any files",
    )
    args = parser.parse_args()

    source = Path(args.directory).expanduser().resolve()
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Organizing: {source}\n")
    organize(source, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
