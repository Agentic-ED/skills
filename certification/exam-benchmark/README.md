# Exam Benchmark

**Guild:** [Certification — The Parliament 🦉](../MANIFESTO.md)

Checks whether an exam form is ready: blueprint coverage, cognitive-level mix, and answer-key balance — and, if you have candidate responses, real item statistics (difficulty, discrimination, distractor performance, KR-20 reliability, SEM) with keep / revise / retire recommendations.

## Who it's for
Certification managers, psychometricians, and exam developers reviewing beta/pilot results or live exam performance.

## What you give it
- The exam form with keys (and domains/objectives if you have them)
- The blueprint with target weights
- Optional: candidate responses as CSV (`candidate_id, Q1, Q2, …`) plus a key file (`item_id,key,domain`)

## What you get
- Readiness summary and biggest risks
- Coverage vs. blueprint, cognitive mix, key-position balance
- Item statistics computed by an included script (no estimated numbers)
- Flagged items with specific recommendations, e.g. "Q12: distractor B attracts high scorers — check the key"

## Run the analysis yourself
```bash
python3 scripts/item_analysis.py responses.csv key.csv --out item_stats.csv
```
Python 3.9+, standard library only. Run with `-h` for input formats.

## Try it
> "Here are the beta results for our Associate exam (240 candidates) and the blueprint. Which items should we fix before launch?"

> "Benchmark this 60-item form against our blueprint — we don't have candidate data yet."

## Works well with
- [`cert-item-bank-creator`](../cert-item-bank-creator/) — write replacement items
- [`sme-question-reviewer`](../sme-question-reviewer/) — review flagged items with SMEs

## Limits
Uses classical test theory rules of thumb, not IRT. Under ~100 candidates, statistics are unstable and treated as signals only. It won't set cut scores — it recommends a standard-setting study instead.
