# Contributing to Agentic-ED Skills

Thanks for helping educators get more out of AI. This guide covers how skills are organized, how to propose one, and what reviewers look for.

## How the repo is organized

```
<guild>/                 # one folder per guild, owned in CODEOWNERS
  MANIFESTO.md           # required — focus, principles, maintainers, skills table
  <skill-name>/
    SKILL.md             # required — frontmatter + instructions for the agent
    README.md            # required — human-facing overview (used by the website)
    icon.png             # recommended — square PNG, 512×512, the guild mascot style
    references/          # optional — longer material loaded only when needed
    scripts/ assets/     # optional — helper scripts, templates, examples
_template/               # copy this folder to start (SKILL.md + README.md)
```

Guilds and their mascots are listed in the [README guild index](README.md#guild-index).

## PR flow

1. **Open an issue first** for a new skill (or comment on an existing one) so the guild can confirm it fits and isn't a duplicate.
2. **Fork and branch**: `git switch -c add-<skill-name>`.
3. **Copy the template**: `cp -r _template <guild>/<skill-name>` and fill in every `TODO`. (In Claude Code you can run `/new-skill` to do this for you.)
4. **Test it for real**: install the skill locally (see README) and try it on at least three realistic requests, including one where it should *not* trigger. Note what you tried in the PR.
5. **Validate**: `python3 .github/scripts/validate_skills.py` (or `/lint-skill` in Claude Code). CI runs the same check on every PR.
6. **Open the PR** using the checklist below. CODEOWNERS automatically requests review from the owning guild.
7. **Review by guild**: at least one guild maintainer approves. Changes to `.github/`, `_template/`, or `CODEOWNERS` need a repo maintainer.

## Skill checklist

Copy into your PR description:

```markdown
- [ ] Folder is `<guild>/<skill-name>/` and `name` in frontmatter matches the folder
- [ ] `description` says what the skill does AND when to use it (≤ 1024 chars)
- [ ] `metadata.guild` and `metadata.author` filled in
- [ ] SKILL.md is under ~500 lines; long material moved to `references/`
- [ ] Tested on 3+ realistic prompts (list them), including one it should NOT trigger on
- [ ] Output is age/grade-appropriate, accessible, and invents no facts, citations, or standards codes
- [ ] No student data, personal information, or copyrighted material without permission
- [ ] Skill has a README.md (copy `_template/README.md`) and an icon.png (recommended, square PNG, 512×512)
- [ ] Guild MANIFESTO.md skills table lists the new skill
- [ ] `python3 .github/scripts/validate_skills.py` passes
```

## Starting a guild

A guild is a group that owns one area (for example assessment, lesson planning, accessibility).

1. Open an issue proposing the guild: its focus, at least two maintainers, and two or three starter skills.
2. A repo maintainer creates the GitHub team `@Agentic-ED/<guild>-guild`.
3. In your PR: add `<guild>/MANIFESTO.md` (copy an existing guild's as a starting point), a CODEOWNERS line `/<guild>/ @Agentic-ED/<guild>-guild`, and a row in the README guild index.

## Code of conduct

Be kind, assume good intent, and center learners. Maintainers may close PRs or issues that don't follow this.

## License

By contributing you agree your contribution is licensed under the [Apache 2.0 License](LICENSE).
