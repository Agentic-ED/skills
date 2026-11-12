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

| Guild (mascot) | Area | Focus |
|---|---|---|
| The Parliament (owl) | [Certification](certification/MANIFESTO.md) | Credentialing and certification exams: job task analysis, blueprints, item writing, SME review, standard setting, and exam quality. |
| The Colony (beaver) | [Curriculum Development](curriculum-development/MANIFESTO.md) | Building programs and course sequences: learning outcomes, scope and sequence, alignment maps, and curriculum reviews. |
| The Kaleidoscope (butterfly) | [Instructional Design](instructional-design/MANIFESTO.md) | Designing learning experiences: needs analysis, learning objectives, activities, storyboards, and assessment design. |
| The Romp (otter) | [Training](training/MANIFESTO.md) | Live and virtual instructor-led training: facilitator guides, workshop agendas, activities, and train-the-trainer. |
| The Exaltation (lark) | [Customer Education](customer-education/MANIFESTO.md) | Teaching customers to succeed with a product: academies, onboarding curricula, product courses, and help-center learning paths. |
| The Caravan (camel) | [Customer Enablement](customer-enablement/MANIFESTO.md) | Equipping customer-facing teams and customer champions: adoption playbooks, admin training, and success plans. |
| The Charm (hummingbird) | [Sales Enablement](sales-enablement/MANIFESTO.md) | Helping sellers sell: product messaging training, talk tracks, objection handling, role-plays, and ramp plans. |
| The Murmuration (starling) | [Partner Enablement](partner-enablement/MANIFESTO.md) | Training partners, resellers, and SIs: partner learning paths, technical accreditation, and co-selling playbooks. |
| The Wisdom (wombat) | [Learning & Development](learning-and-development/MANIFESTO.md) | Employee growth inside organizations: onboarding, leadership development, skills frameworks, and career paths. |
| The Sleuth (bear) | [Data & Telemetry](data-telemetry/MANIFESTO.md) | Measuring learning: xAPI/LMS data, learning analytics, evaluation (e.g. Kirkpatrick levels), dashboards, and impact reports. |
| The Dazzle (zebra) | [Learning Marketing](learning-marketing/MANIFESTO.md) | Getting learners to show up: course launch campaigns, landing pages, learner communications, and enrollment growth. |
| The Herd (alpaca) | [Learning Operations](learning-operations/MANIFESTO.md) | Running the learning function: LMS administration, enrollment and compliance tracking, vendor management, and process docs. |
| The Bloom (jellyfish) | [Media & Visual Design](media-visual-design/MANIFESTO.md) | Visual and multimedia learning assets: slide design, video scripts, infographics, accessibility of media, and brand consistency. |
| The Bouquet (pheasant) | [Content & Technical Writing](content-technical-writing/MANIFESTO.md) | Clear learning and product content: job aids, how-to guides, documentation, style guides, and plain-language editing. |
| The Memory (elephant) | [Knowledge Management](knowledge-management/MANIFESTO.md) | Capturing and finding what an organization knows: knowledge bases, taxonomies, SME interviews, and content lifecycle. |
| The Ostentation (peacock) | [Community & Events](community-events/MANIFESTO.md) | Learning communities and events: conferences, webinars, cohort programs, community programs, and event content. |
| The Flock (goose) | [Newcomers](newcomers/MANIFESTO.md) | Welcoming first-time contributors and people new to AI in education: starter skills, learning-by-example, and good-first-issues. |
| The Convocation (eagle) | [Maintainers](maintainers/MANIFESTO.md) | Stewarding this repository: review standards, release notes, quality audits across guilds, and contributor experience. |

<!-- One row per guild folder. Each guild's MANIFESTO.md lists its maintainers and skills. -->

Want a new guild? See [Starting a guild](CONTRIBUTING.md#starting-a-guild).

## Contributing

New skills and improvements are welcome — read [CONTRIBUTING.md](CONTRIBUTING.md). Start from [`_template/SKILL.md`](_template/SKILL.md). Every PR is checked automatically and reviewed by the owning guild.

## License

[Apache 2.0](LICENSE)
