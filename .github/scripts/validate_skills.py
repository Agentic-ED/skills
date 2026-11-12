#!/usr/bin/env python3
"""Validate every skill in the repo.

Layout:  <guild>/<skill-name>/SKILL.md
Ignored: top-level folders starting with "_" or "." (e.g. _template, .github, .claude)

Checks
  - SKILL.md starts with a YAML frontmatter block
  - `name`: required, lowercase letters/digits/hyphens, <= 64 chars, matches the folder name
  - `description`: required, non-empty string, <= 1024 chars
  - optional `compatibility` <= 500 chars; optional `metadata` is a mapping
  - skill names are unique across guilds
  - each guild folder has a README.md and a CODEOWNERS entry

Usage: python3 .github/scripts/validate_skills.py [path-to-skill-dir ...]
Exit code 1 if any check fails.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def guild_dirs() -> list[Path]:
    return sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    )


def codeowners_paths() -> set[str]:
    path = ROOT / "CODEOWNERS"
    if not path.exists():
        return set()
    out = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.add(line.split()[0].strip("/"))
    return out


def check_skill(skill_dir: Path) -> list[str]:
    rel = skill_dir.relative_to(ROOT)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{rel}: missing SKILL.md"]

    match = FRONTMATTER_RE.match(skill_md.read_text(encoding="utf-8"))
    if not match:
        return [f"{rel}/SKILL.md: must start with a '---' YAML frontmatter block"]
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"{rel}/SKILL.md: invalid YAML frontmatter: {e}"]
    if not isinstance(fm, dict):
        return [f"{rel}/SKILL.md: frontmatter must be a mapping"]

    errors = []
    name = fm.get("name")
    if not isinstance(name, str) or not name:
        errors.append(f"{rel}/SKILL.md: `name` is required")
    else:
        if len(name) > 64 or not NAME_RE.match(name):
            errors.append(f"{rel}/SKILL.md: `name` must be lowercase letters, digits and hyphens, max 64 chars (got {name!r})")
        if name != skill_dir.name:
            errors.append(f"{rel}/SKILL.md: `name` ({name!r}) must match folder name ({skill_dir.name!r})")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{rel}/SKILL.md: `description` is required")
    elif len(desc) > 1024:
        errors.append(f"{rel}/SKILL.md: `description` is {len(desc)} chars (max 1024)")
    elif "TODO" in desc:
        errors.append(f"{rel}/SKILL.md: `description` still contains TODO from the template")

    compat = fm.get("compatibility")
    if compat is not None and (not isinstance(compat, str) or len(compat) > 500):
        errors.append(f"{rel}/SKILL.md: `compatibility` must be a string, max 500 chars")
    meta = fm.get("metadata")
    if meta is not None and not isinstance(meta, dict):
        errors.append(f"{rel}/SKILL.md: `metadata` must be a mapping")
    return errors


def main(argv: list[str]) -> int:
    errors: list[str] = []
    owned = codeowners_paths()

    if argv:
        skills = [Path(a).resolve() for a in argv]
    else:
        skills = []
        for guild in guild_dirs():
            rel = guild.relative_to(ROOT).as_posix()
            if not (guild / "README.md").exists():
                errors.append(f"{rel}/: guild folder needs a README.md (what the guild covers, who maintains it)")
            if rel not in owned:
                errors.append(f"{rel}/: add a CODEOWNERS line for this guild, e.g. `/{rel}/ @Agentic-ED/{rel}-guild`")
            skills += sorted(p for p in guild.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))

    seen: dict[str, Path] = {}
    for skill in skills:
        errors += check_skill(skill)
        if skill.name in seen:
            errors.append(f"{skill.relative_to(ROOT)}: skill name duplicates {seen[skill.name].relative_to(ROOT)}")
        seen[skill.name] = skill

    for e in errors:
        print(f"::error::{e}" if "GITHUB_ACTIONS" in os.environ else f"✗ {e}")
    print(f"Checked {len(skills)} skill(s): {'FAILED' if errors else 'OK'} ({len(errors)} error(s))")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
