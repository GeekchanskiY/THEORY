#!/usr/bin/env python3
"""Regenerate the vault snapshot section in README.md."""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"
SKIP_DIRS = {".git", ".obsidian", ".idea", ".github", "scripts"}
TODO_RE = re.compile(r"TODO")
STATS_START = "<!-- vault-stats:start -->"
STATS_END = "<!-- vault-stats:end -->"

INTRO = """My theory database. Written using [Obsidian](https://obsidian.md).

Notes on computer science, programming languages, software architecture, networks, and related topics.
"""


def iter_notes() -> list[Path]:
    notes: list[Path] = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in files:
            if not name.endswith(".md"):
                continue
            path = Path(root) / name
            if path.resolve() == README_PATH.resolve():
                continue
            notes.append(path)
    return sorted(notes)


def top_folder(path: Path) -> str:
    rel = path.relative_to(REPO_ROOT)
    if len(rel.parts) == 1:
        return "(root)"
    return rel.parts[0]


def collect_stats() -> dict:
    notes = iter_notes()
    empty = 0
    short = 0
    todo_files = 0
    todo_hits = 0
    folders: Counter[str] = Counter()

    for path in notes:
        text = path.read_text(encoding="utf-8", errors="replace")
        folders[top_folder(path)] += 1
        if not text.strip():
            empty += 1
        if len(text) < 200:
            short += 1
        hits = len(TODO_RE.findall(text))
        if hits:
            todo_files += 1
            todo_hits += hits

    return {
        "notes": len(notes),
        "empty": empty,
        "short": short,
        "todo_files": todo_files,
        "todo_hits": todo_hits,
        "folders": folders,
    }


def render_stats(stats: dict) -> str:
    folder_rows = "\n".join(
        f"| {name} | {count} |"
        for name, count in sorted(stats["folders"].items(), key=lambda item: (-item[1], item[0].lower()))
    )
    return f"""{STATS_START}
## Vault snapshot

Auto-generated on {date.today().isoformat()}. Do not edit this section by hand — it is refreshed when notes change.

| Metric | Count |
| --- | ---: |
| Notes | {stats["notes"]} |
| Empty files | {stats["empty"]} |
| Under 200 characters | {stats["short"]} |
| Files with TODO | {stats["todo_files"]} |
| TODO mentions | {stats["todo_hits"]} |

Empty files are also included in the under-200-character count. Root `README.md` is not counted as a note.

### Notes by folder

| Folder | Notes |
| --- | ---: |
{folder_rows}
{STATS_END}
"""


def upsert_readme(stats_block: str) -> bool:
    if README_PATH.exists():
        current = README_PATH.read_text(encoding="utf-8")
    else:
        current = INTRO

    if STATS_START in current and STATS_END in current:
        before, rest = current.split(STATS_START, 1)
        _, after = rest.split(STATS_END, 1)
        updated = before.rstrip() + "\n\n" + stats_block + after.lstrip("\n")
        if not before.strip():
            updated = INTRO.rstrip() + "\n\n" + stats_block
    else:
        intro = current.rstrip() if current.strip() else INTRO.rstrip()
        updated = intro + "\n\n" + stats_block

    if not updated.endswith("\n"):
        updated += "\n"

    if README_PATH.exists() and README_PATH.read_text(encoding="utf-8") == updated:
        return False
    README_PATH.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    os.chdir(REPO_ROOT)
    changed = upsert_readme(render_stats(collect_stats()))
    print("README.md updated" if changed else "README.md already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
