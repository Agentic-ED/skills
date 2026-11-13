# Agentic-ED Skills

The index of every AgenticED guild. Each guild keeps its skills and agents in its own repo; this repo mounts all of them as git submodules so you can get everything in one clone.

## Get everything

```bash
git clone --recurse-submodules https://github.com/Agentic-ED/skills.git
```

Already cloned? `git submodule update --init`. To pull the latest from every guild: `git submodule update --remote`.

Each guild repo keeps skills in `skills/<skill>/` and agents in `agents/<agent>/`. To use a skill, copy its folder into your assistant's skills directory; its README lists install steps and dependencies.

## Guilds

| Guild | Practice | Repo |
|---|---|---|
| The Parliament | Certification | [parliament-certification](https://github.com/Agentic-ED/parliament-certification) |
| The Ostentation | Community and events | [ostentation-community-events](https://github.com/Agentic-ED/ostentation-community-events) |
| The Bouquet | Content and technical writing | [bouquet-content-technical-writing](https://github.com/Agentic-ED/bouquet-content-technical-writing) |
| The Pride | Content As Code | [pride-content-as-code](https://github.com/Agentic-ED/pride-content-as-code) |
| The Colony | Curriculum development | [colony-curriculum-development](https://github.com/Agentic-ED/colony-curriculum-development) |
| The Exaltation | Customer education | [exaltation-customer-education](https://github.com/Agentic-ED/exaltation-customer-education) |
| The Caravan | Customer enablement | [caravan-customer-enablement](https://github.com/Agentic-ED/caravan-customer-enablement) |
| The Sleuth | Data and telemetry | [sleuth-data-telemetry](https://github.com/Agentic-ED/sleuth-data-telemetry) |
| The Kaleidoscope | Instructional design | [kaleidoscope-instructional-design](https://github.com/Agentic-ED/kaleidoscope-instructional-design) |
| The Memory | Knowledge management | [memory-knowledge-management](https://github.com/Agentic-ED/memory-knowledge-management) |
| The Wisdom | Learning and development | [wisdom-learning-and-development](https://github.com/Agentic-ED/wisdom-learning-and-development) |
| The Herd | Learning management systems (LMS) | [herd-learning-management-systems](https://github.com/Agentic-ED/herd-learning-management-systems) |
| The Dazzle | Learning marketing and promotion | [dazzle-learning-marketing](https://github.com/Agentic-ED/dazzle-learning-marketing) |
| The Hive | Learning operations | [hive-learning-operations](https://github.com/Agentic-ED/hive-learning-operations) |
| The Convocation | Maintainers and governance | [convocation-maintainers](https://github.com/Agentic-ED/convocation-maintainers) |
| The Bloom | Media and visual design | [bloom-media-visual-design](https://github.com/Agentic-ED/bloom-media-visual-design) |
| The Murmuration | Partner enablement | [murmuration-partner-enablement](https://github.com/Agentic-ED/murmuration-partner-enablement) |
| The Charm | Sales enablement | [charm-sales-enablement](https://github.com/Agentic-ED/charm-sales-enablement) |
| The Romp | Training | [romp-training](https://github.com/Agentic-ED/romp-training) |

To contribute a skill, open a pull request in the guild's repo (see its CONTRIBUTING.md), not here. This repo only tracks which guild repos exist and which commit of each is published.
