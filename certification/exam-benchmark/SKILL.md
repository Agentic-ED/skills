---
name: exam-benchmark
description: Benchmarks a certification exam form and its items — blueprint coverage, cognitive-level mix, key balance, and (when response data is available) classical item statistics such as difficulty, discrimination, distractor performance, KR-20 reliability, and SEM — then recommends which items to keep, revise, or retire. Use when someone shares exam results or pilot/beta data, asks how an exam or its items are performing, wants an item analysis, or asks whether a form is ready to launch.
license: Apache-2.0
compatibility: Item statistics need Python 3.9+ (standard library only) to run scripts/item_analysis.py.
metadata:
  guild: certification
  author: sethluersen
  version: "0.1.0"
---

# Exam Benchmark

Evaluate an exam form against its blueprint and, when candidate data exists, against standard psychometric benchmarks. **Compute statistics with the script — never estimate or invent numbers.**

## 1. Gather inputs
- **Exam form** — items with keys, and per-item domain/objective and cognitive level if available.
- **Blueprint** — domains with target weights (% or item counts).
- **Response data (optional)** — a CSV with one row per candidate: `candidate_id`, then one column per item ID holding the chosen option (A/B/C/D…) or 1/0 if already scored. Plus a key CSV `item_id,key[,domain]` when responses are letters. If the data is in another shape (LMS export, xlsx), reshape it to this first and show the user the mapping.
- **Context** — beta/pilot vs. live, candidate count, and cut score if one is set.

## 2. Form review (no data needed)
Report:
- **Blueprint coverage** — actual vs. target items per domain; flag any domain off by more than ±5 percentage points or missing.
- **Cognitive mix** — % Remember / Understand / Apply / Analyze; flag if recall-level items dominate a certification form.
- **Key balance** — distribution of correct-answer positions; flag any letter above 35% or long runs of the same key.
- **Overlap and cueing** — items that test the same fact or give away each other's answers.

## 3. Item statistics (when response data exists)
Run:
```bash
python3 scripts/item_analysis.py responses.csv key.csv --out item_stats.csv
```
(path is relative to this skill's folder). It reports form statistics (mean, SD, KR-20, SEM), per-item difficulty (p) and corrected point-biserial, distractor analysis, and domain coverage, with flags.

Interpret with these common rules of thumb (programs may set their own):
| Statistic | Healthy | Review |
|---|---|---|
| Difficulty p | 0.30–0.90 | < 0.30 too hard / possible miskey; > 0.90 too easy |
| Corrected point-biserial | ≥ 0.20 | 0.10–0.19 weak; < 0 likely miskey or flawed |
| Distractor | chosen by ≥ 5%, negative r_pb | < 5% non-functioning; positive r_pb = possible second correct answer |
| KR-20 (high-stakes cert) | ≥ 0.80 (≥ 0.90 ideal) | < 0.70 form too unreliable for pass/fail decisions |

Small samples: below ~100 candidates, treat statistics as signals for SME review, not verdicts — say so explicitly.

## 4. Recommendations
For every flagged item, recommend one of:
- **Keep** — statistics fine, or flag explained by the MQC profile.
- **Revise** — name the specific fix (e.g. replace non-functioning distractor D; reword stem).
- **Check key / SME review** — negative discrimination or a distractor with positive r_pb.
- **Retire** — unfixable, off-blueprint, or compromised.

Then form-level: is it ready to launch? What would raise reliability (e.g. replacing weak items, adding items to under-covered domains)? If a cut score is provided, report the pass rate and note the SEM band around the cut. Recommend a formal standard-setting study (e.g. modified Angoff) if no defensible cut score exists — don't set one yourself.

## Output format
1. Executive summary (5 bullets max): readiness verdict, reliability, biggest risks.
2. Form review tables (coverage, cognitive mix, key balance).
3. Item statistics table + flagged-item recommendations.
4. Next steps, with owners where known (SMEs, psychometrician, program manager).

## Rules
- Every number in the report must come from the script output or the user's data — never made up or "typical".
- Don't make pass/fail or legal-defensibility claims; recommend a qualified psychometrician for high-stakes decisions.
- Candidate data is personal data: work with anonymized IDs, don't print individual candidate scores unless asked, and remind the user not to share raw response files publicly.
