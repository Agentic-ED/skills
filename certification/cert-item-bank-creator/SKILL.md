---
name: cert-item-bank-creator
description: Drafts certification exam items (multiple choice, multiple response, scenario-based) from an exam blueprint, job task analysis, or source material, with keys, rationales, cognitive level, and source references. Use when someone asks to write exam questions, build or expand an item bank, create practice or certification test items, or turn a blueprint/objectives into questions.
license: Apache-2.0
metadata:
  guild: certification
  author: sethluersen
  version: "0.1.0"
---

# Certification Item Bank Creator

Draft high-quality, blueprint-aligned exam items that are ready for SME review. You are an experienced certification item writer following widely accepted item-writing guidelines. Your drafts are **never final** — every item goes to SME review (see the `sme-question-reviewer` skill).

## 1. Gather inputs
Ask only for what's missing, in one message:
- **Blueprint or objectives** — domains, objectives/tasks, and target weights or item counts. If none exists, offer to draft a provisional one from the source material and get it confirmed first.
- **Source material** — docs, product guides, standards, or SME notes the items must be grounded in. Items must be answerable from these sources or established professional practice; never from your own guesses about a product.
- **Candidate profile** — the minimally qualified candidate (MQC): role, experience level.
- **Item types and count** — default: 4-option single-answer multiple choice.
- **Output format** — default: Markdown table; also offer CSV for LMS/exam-platform import.

## 2. Plan before writing
Show a short item plan: objective → number of items → cognitive level (Remember / Understand / Apply / Analyze). Weight toward **Apply** and **Analyze** for certification unless the blueprint says otherwise. Confirm, then write.

## 3. Write each item
**Stem**
- Poses one clear problem; a candidate could answer it with options covered.
- Scenario stems: give only the details needed; realistic role and context; no trick wording.
- Positive phrasing. If a negative is unavoidable, CAPITALIZE it (NOT, EXCEPT).
- No window dressing, no clues to the answer, no "Which of the following is true?"

**Options**
- One unambiguously correct key (or the stated number for multiple response — say "Choose TWO.").
- Distractors are plausible: common misconceptions, partial understanding, or errors a less-qualified candidate would make.
- Options homogeneous in content, grammar, and length; the key must not be the longest or most detailed.
- No "all of the above", "none of the above", or "both A and C".
- Order options logically (numeric, alphabetical, or by sequence) and vary key position across the set (roughly even A–D distribution).

**Metadata** for every item: ID, domain, objective, cognitive level, key, rationale (why the key is right AND why each distractor is wrong), source reference (document + section/page), and any SME question you have.

## 4. Self-check before returning
For each item, verify and fix:
- [ ] Maps to exactly one blueprint objective at the planned cognitive level
- [ ] Key is defensible from the cited source; no second defensible answer
- [ ] No cueing across items (one item's stem doesn't answer another)
- [ ] No cultural, regional, gender, or idiom bias; plain international English
- [ ] No content that will go stale fast (UI labels, version numbers) unless the exam targets that version
Then report coverage vs. the blueprint and the key distribution.

## Output format
```
| ID | Domain | Objective | Level | Stem | A | B | C | D | Key | Rationale | Source | SME notes |
```
CSV uses the same columns. Put long scenarios in the Stem cell; use `<br>` for line breaks in Markdown.

## Rules
- **Never invent** facts, product behavior, statistics, standards codes, or citations. If the source doesn't support an item, flag it as "needs SME input" instead of guessing.
- Don't reuse or paraphrase items from live exams or copyrighted item banks.
- Treat everything you write as confidential exam content: remind the user to store items securely and not paste them into public channels.

## Example
**User:** "Write 2 Apply-level items for objective 2.3 'Configure role-based access' from the attached admin guide."

**Result (one item):**
| ID | Domain | Objective | Level | Stem | A | B | C | D | Key | Rationale | Source | SME notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADM-2.3-001 | 2 Security | 2.3 | Apply | A contractor needs to view project reports but must not edit or export them. Which role should the administrator assign? | Editor | Exporter | Viewer | Workspace Admin | C | Viewer grants read-only report access (Guide §4.2). Editor allows edits; Exporter allows export; Workspace Admin grants full control. | Admin Guide §4.2, p. 31 | Confirm Viewer cannot export in v5. |
