---
name: lint-skill
description: Check one or all Agentic-ED skills against the repo's rules — runs the CI frontmatter validator, then reviews quality against the CONTRIBUTING checklist. Use before opening a PR, or when asked to lint, check, validate, or review a skill.
argument-hint: "[<guild>/<skill-name>]"
---

# Lint skill

Two passes: the automated check CI runs, then a quality review CI can't do.

## 1. Automated check
- One skill: `python3 .github/scripts/validate_skills.py <guild>/<skill-name>`
- Whole repo (no argument): `python3 .github/scripts/validate_skills.py`
If `pyyaml` is missing, tell the user to `pip install pyyaml`. Fix structural errors (name mismatch, missing description, missing CODEOWNERS line) directly; they're unambiguous.

## 2. Quality review
Read the skill's `SKILL.md` and any `references/`. Report each item as ✅ / ⚠️ with a one-line reason:

- **Triggering**: does `description` say both *what* and *when*? Would it fire on the obvious requests and stay quiet on neighbors? Suggest a rewrite if not.
- **Instructions**: direct, ordered steps; says which inputs to ask for; defines the output format; includes a realistic example; no leftover TODOs.
- **Size**: SKILL.md under ~500 lines; long material in `references/`.
- **Education quality**: age/grade-appropriate, accessible, tells the agent not to invent facts/citations/standards codes.
- **Safety & privacy**: no student data, personal info, secrets, or unlicensed copyrighted content.
- **Registration**: listed in its guild `MANIFESTO.md` skills table; has a `README.md`; `icon.png` present (recommended).

Do not rewrite instructions or examples without asking — propose concrete edits and let the contributor choose. End with "Ready for PR" or the list of blockers.
