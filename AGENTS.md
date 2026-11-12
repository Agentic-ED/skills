# Agent rules — Agentic-ED Skills

This repo is a library of Agent Skills for education. You are most likely here to add or improve a skill. Read `CONTRIBUTING.md` first; these rules are the short, binding version.

## Layout
- Skills live at `<guild>/<skill-name>/SKILL.md`. Never put a skill at the repo root or nest it deeper.
- Folders starting with `_` or `.` are not skills (`_template/`, `.github/`, `.claude/`).
- `.claude/skills/` holds contributor tooling (`new-skill`, `lint-skill`) — not published skills.

## Writing a skill
- Start from `_template/SKILL.md`. Frontmatter `name` must equal the folder name: lowercase, digits, hyphens, ≤ 64 chars.
- `description` (≤ 1024 chars) must state what the skill does **and** when to use it — it is the only part the agent sees before deciding to load the skill.
- Keep `SKILL.md` under ~500 lines. Put long reference material in `references/*.md` and link to it from SKILL.md.
- Write instructions as direct steps for the agent. Include an output format and a concrete example.
- Audience is educators and learners: plain language, age-appropriate, accessible. Never invent facts, citations, or standards codes; tell the agent to say when it is unsure.
- Never include student data, personal information, secrets, or copyrighted material without permission.

## Boundaries
- Only edit the guild folder you were asked to work in. Do not edit `CODEOWNERS`, `.github/`, `LICENSE`, or `_template/` unless explicitly asked.
- When you add a skill, also add it to that guild's `README.md`. When you add a guild, also add a CODEOWNERS line and a row in the root README guild index.

## Before you finish
Run `python3 .github/scripts/validate_skills.py` (requires `pyyaml`) and fix every error. CI runs the same check on every PR.
