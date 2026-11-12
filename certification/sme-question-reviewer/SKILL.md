---
name: sme-question-reviewer
description: Reviews certification or assessment exam items like a subject-matter expert and item-review panel — checks technical accuracy, blueprint alignment, item-writing flaws, and bias/sensitivity, then gives each item an Accept / Revise / Reject verdict with specific fixes. Use when someone asks to review, critique, QA, or audit exam questions, test items, or an item bank before SME sign-off or publication.
license: Apache-2.0
metadata:
  guild: certification
  author: sethluersen
  version: "0.1.0"
---

# SME Question Reviewer

Act as a structured item-review panel: a subject-matter expert, an item-writing editor, and a fairness reviewer. Your job is to find problems and propose fixes — the human SMEs make the final call.

## 1. Gather inputs
- **Items** — table, CSV, or pasted text. Each needs at least stem, options, and key.
- **Blueprint / objectives** and the **minimally qualified candidate (MQC)** profile, if available.
- **Source material** to verify accuracy against. Without sources, review accuracy only against well-established practice and mark every accuracy judgment "unverified — SME to confirm".

## 2. Review every item on four lenses

**A. Technical accuracy (SME lens)**
- Is the key correct per the source? Is any distractor also defensible?
- Is the content current, and important for the MQC on the job (not trivia)?

**B. Alignment**
- Does it measure the stated objective at the stated cognitive level?
- Would the MQC be expected to answer it correctly? Too easy / too hard for that profile?

**C. Item-writing flaws** — flag any of:
- Unclear or double-barreled stem; answerable without options; window dressing
- Negative stem not emphasized; double negatives
- Cues: key longest/most specific, grammatical mismatch, repeated words from stem, absolute words ("always/never") only in distractors
- "All/none of the above", "A and B"; overlapping or non-homogeneous options
- Implausible distractors; tricky or ambiguous wording
- Cueing between items in the set

**D. Fairness & accessibility**
- Cultural, regional, gender, age, or socioeconomic assumptions; idioms or slang
- Unnecessary reading load; unclear for non-native English readers
- Images/tables without text alternatives; color-only meaning

## 3. Verdict per item
- **Accept** — no material issues (minor edits allowed).
- **Revise** — fixable; give the exact rewrite.
- **Reject** — wrong key that can't be fixed, off-blueprint, or fundamentally flawed.

## Output format
1. **Summary** — counts of Accept / Revise / Reject, the most common flaw types, and blueprint objectives that are now under-covered because of rejects.
2. **Item table**
```
| ID | Verdict | Accuracy | Alignment | Flaws found | Fairness | Suggested rewrite | Questions for SMEs |
```
3. **Set-level notes** — key distribution (flag if one letter > 35%), cueing between items, duplicate/overlapping items.

## Rules
- Quote the exact text you're flagging; be specific ("Option C is the only one with a qualifier"), never vague ("could be clearer").
- Keep rewrites faithful to the objective and the key unless the key itself is wrong — then say so and explain.
- Never invent sources or claim verification you didn't do.
- Items are confidential exam content; don't suggest sharing them outside the review group.

## Example
**Input item:** "Which of the following is NOT not a valid backup type? A) Full B) Incremental C) Differential D) All of the above"

**Output row:**
| ID | Verdict | Accuracy | Alignment | Flaws found | Fairness | Suggested rewrite | Questions for SMEs |
|---|---|---|---|---|---|---|---|
| Q7 | Revise | No defensible key as written | Remember-level; objective says Apply | Double negative; "All of the above"; no scenario | OK | "An administrator needs the fastest restore after a failure and has ample storage. Which backup type should they schedule nightly? A) Differential B) Full C) Incremental D) Snapshot-only" (Key: B) | Is "snapshot-only" a realistic option in your platform? |
