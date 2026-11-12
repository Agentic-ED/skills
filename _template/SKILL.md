---
name: my-skill-name
description: TODO — one or two sentences saying what this skill does AND when Claude should use it (the triggers). Write it for the model, e.g. "Builds a rubric aligned to stated learning objectives. Use when an educator asks for a rubric, grading criteria, or scoring guide."
license: Apache-2.0
metadata:
  guild: TODO-guild-folder
  author: TODO-github-handle
  version: "0.1.0"
---

# My Skill Name

<!--
Copy this folder to <guild>/<your-skill-name>/ and rename `name` above to match the folder.
Keep this file under ~500 lines; move long reference material into references/*.md
and link to it, so Claude only loads it when needed.
-->

## When to use
- TODO: the situations / requests this skill handles.
- TODO: what it should NOT be used for (point to a better skill if one exists).

## Inputs to gather
Ask the user only for what is missing:
- TODO: e.g. grade level, subject, learning objectives, length.

## Steps
1. TODO: first step Claude takes.
2. TODO: …
3. Check the output against the quality checklist below before returning it.

## Output format
TODO: exact structure of what Claude produces (headings, table columns, file type).

## Quality checklist
- [ ] Age/grade-appropriate language
- [ ] Aligned to the stated objectives
- [ ] Accessible (plain language, alt text for images, no color-only meaning)
- [ ] No invented facts, citations, or standards codes

## Example
**User:** TODO: a realistic request.

**Result:** TODO: a short excerpt of a good output.
