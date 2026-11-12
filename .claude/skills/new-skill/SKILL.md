---
name: new-skill
description: Scaffold a new Agentic-ED skill from _template/ into the right guild folder and help fill it in. Use when a contributor wants to create, start, or add a new skill to this repo.
argument-hint: "<guild>/<skill-name>"
---

# New skill

Create `<guild>/<skill-name>/SKILL.md` from `_template/SKILL.md` and work with the contributor to fill it in.

## Steps

1. **Parse `$ARGUMENTS`** as `<guild>/<skill-name>`. If missing, list existing guild folders (top-level dirs not starting with `_` or `.`) and ask which guild and what the skill should do. Derive a kebab-case name (lowercase, digits, hyphens, ≤ 64 chars) and confirm it.
2. **Check for duplicates**: search existing `*/*/SKILL.md` names and descriptions for overlapping skills. If one is close, show it and ask whether to improve that one instead.
3. **New guild?** If `<guild>/` doesn't exist, stop and point to "Starting a guild" in CONTRIBUTING.md — creating a guild needs a GitHub team and maintainer sign-off. Only scaffold it (README.md, CODEOWNERS line, README index row) if the contributor confirms the guild was approved.
4. **Copy the template**: `cp -r _template <guild>/<skill-name>`; set `name`, `metadata.guild`, and `metadata.author` (ask for their GitHub handle).
5. **Interview, then write.** Ask the contributor, briefly: who uses it (role, grade level), 2–3 example requests, what a great output looks like, and what it must never do. Fill every TODO from their answers:
   - `description`: what it does + when to use it, written for the model, ≤ 1024 chars.
   - Steps as direct instructions; an explicit output format; one realistic example.
   - Move anything long (standards lists, rubrics, exemplars) to `references/*.md` and link it.
6. **Register it** in `<guild>/README.md`'s skill list.
7. **Validate**: run `python3 .github/scripts/validate_skills.py` and fix errors. Remind the contributor to test the skill on 3+ real prompts and to use the PR checklist in CONTRIBUTING.md.
