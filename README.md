# Agentic-ED Skills

Open-source [Agent Skills](https://agentskills.io) for education — reusable instructions that teach Claude (and other agents that support `SKILL.md`) how to do specific teaching and learning tasks well: planning lessons, building rubrics, giving feedback, designing courses, and more.

Skills are written and reviewed by **guilds** — groups of educators and builders who own one area. Every skill is a folder with a `SKILL.md` file, so you can read exactly what it tells the agent to do.

Browse them on the website: <https://github.com/Agentic-ED/website> (site coming soon).

## Install

Every skill lives at `<guild>/<skill-name>/`. Grab the repo once:

```bash
git clone https://github.com/Agentic-ED/skills.git agentic-ed-skills
```

### Claude Code

Copy a skill into your personal skills (all projects) or a project's skills (shared with your team via git):

```bash
cp -r agentic-ed-skills/<guild>/<skill-name> ~/.claude/skills/        # just you
cp -r agentic-ed-skills/<guild>/<skill-name> .claude/skills/          # this project
```

Claude picks it up automatically; you can also run it directly with `/<skill-name>`.

### Claude apps (claude.ai, Desktop, mobile)

1. Zip the skill folder: `cd agentic-ed-skills/<guild> && zip -r <skill-name>.zip <skill-name>`
2. In Claude, open **Settings → Skills**, choose **Upload skill**, and select the zip. (Skills must be enabled for your plan / organization.)

### Claude API

Upload the skill folder with the Skills API and attach it to requests that use the code-execution tool. See the [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

### Other agents

Any agent that supports the open `SKILL.md` format can use these folders as-is — copy the skill folder into that agent's skills directory (check its docs for the location).

## Guild index

| Guild | Folder | Focus | Maintainers |
|---|---|---|---|
| _No guilds yet_ | | [Start one](CONTRIBUTING.md#starting-a-guild) | |

<!-- Add one row per guild folder, alphabetical. Each guild folder's README.md lists its skills. -->

## Contributing

New skills and improvements are welcome — read [CONTRIBUTING.md](CONTRIBUTING.md). Start from [`_template/SKILL.md`](_template/SKILL.md). Every PR is checked automatically and reviewed by the owning guild.

## License

[Apache 2.0](LICENSE)
