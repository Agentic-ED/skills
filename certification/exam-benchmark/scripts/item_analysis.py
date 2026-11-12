#!/usr/bin/env python3
"""Classical test theory item analysis for an exam form. Standard library only.

Inputs
  responses.csv  one row per candidate: candidate_id, then one column per item ID.
                 Cells are the chosen option (A/B/C/D...) or 1/0 if already scored.
                 Blank = omitted (scored 0).
  key.csv        (needed when responses are letters) columns: item_id, key[, domain]
                 Multiple-response keys: letters joined with no separator, e.g. "AC";
                 the response must match exactly. `domain` enables blueprint coverage.

Usage
  python3 item_analysis.py responses.csv [key.csv] [--out items.csv]

Output: a Markdown report on stdout (form stats, flagged items, per-item table,
distractor analysis, domain coverage) and optionally a per-item CSV.

Flags (common CTT rules of thumb; programs set their own thresholds):
  p < 0.30 hard · p > 0.90 easy · corrected r_pb < 0.20 weak · r_pb < 0 negative
  distractor chosen by < 5% (non-functioning) · distractor with r_pb > 0 (attracts strong candidates)
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics as st
import sys
from collections import Counter, defaultdict


def pearson(x: list[float], y: list[float]) -> float | None:
    if len(x) < 2:
        return None
    sx, sy = st.pstdev(x), st.pstdev(y)
    if sx == 0 or sy == 0:
        return None
    mx, my = st.fmean(x), st.fmean(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) * sx * sy)


def load(responses_path: str, key_path: str | None):
    with open(responses_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    header, data = rows[0], [r for r in rows[1:] if any(c.strip() for c in r)]
    items = header[1:]
    raw = {it: [(r[i + 1].strip().upper() if i + 1 < len(r) else "") for r in data] for i, it in enumerate(items)}

    key, domain = {}, {}
    if key_path:
        with open(key_path, newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                key[r["item_id"].strip()] = r["key"].strip().upper()
                if r.get("domain"):
                    domain[r["item_id"].strip()] = r["domain"].strip()

    scored = {}
    for it in items:
        vals = raw[it]
        if it in key:
            scored[it] = [1.0 if v == key[it] else 0.0 for v in vals]
        elif all(v in ("0", "1", "") for v in vals):
            scored[it] = [1.0 if v == "1" else 0.0 for v in vals]
        else:
            sys.exit(f"Item {it!r} has letter responses but no key in key.csv")
    return items, raw, key, domain, scored, len(data)


def analyze(items, raw, key, domain, scored, n):
    totals = [sum(scored[it][c] for it in items) for c in range(n)]
    k = len(items)
    # Options seen anywhere on the form (single letters), so a distractor nobody chose still shows up at 0%.
    form_options = {v for it in items if it in key for v in raw[it] if len(v) == 1 and v.isalpha()}
    out = []
    for it in items:
        s = scored[it]
        p = st.fmean(s)
        rest = [t - x for t, x in zip(totals, s)]
        rpb = pearson(s, rest)
        flags = []
        if p < 0.30:
            flags.append("hard")
        if p > 0.90:
            flags.append("easy")
        if rpb is None:
            flags.append("no variance")
        elif rpb < 0:
            flags.append("NEGATIVE discrimination — check key")
        elif rpb < 0.20:
            flags.append("weak discrimination")

        distractors = []
        if it in key:
            counts = Counter(raw[it])
            seen = {o for o in counts if o}
            if len(key[it]) == 1:  # single-answer item: assume the form's full option set
                seen |= form_options
            options = sorted(o for o in seen if o != key[it])
            for o in options:
                chose = [1.0 if v == o else 0.0 for v in raw[it]]
                share = counts[o] / n
                d_r = pearson(chose, rest)
                note = []
                if share < 0.05:
                    note.append("non-functioning (<5%)")
                if d_r is not None and d_r > 0:
                    note.append("attracts high scorers — possible second key")
                    flags.append(f"distractor {o} r_pb>0")
                distractors.append((o, share, d_r, ", ".join(note)))
            omit = counts.get("", 0) / n
            if omit >= 0.05:
                flags.append(f"omit rate {omit:.0%}")
        out.append({"item": it, "domain": domain.get(it, ""), "key": key.get(it, ""), "p": p,
                    "rpb": rpb, "flags": flags, "distractors": distractors})

    var_total = st.pvariance(totals) if n > 1 else 0.0
    sum_pq = sum(st.fmean(scored[it]) * (1 - st.fmean(scored[it])) for it in items)
    kr20 = (k / (k - 1)) * (1 - sum_pq / var_total) if k > 1 and var_total > 0 else None
    sd = math.sqrt(var_total)
    sem = sd * math.sqrt(1 - kr20) if kr20 is not None and kr20 <= 1 else None
    form = {"candidates": n, "items": k, "mean": st.fmean(totals) if n else 0, "sd": sd,
            "kr20": kr20, "sem": sem, "min": min(totals, default=0), "max": max(totals, default=0)}
    return form, out


def fmt(x, nd=2):
    return "—" if x is None else f"{x:.{nd}f}"


def report(form, out):
    print("# Exam item analysis\n")
    print("## Form statistics")
    print(f"- Candidates: {form['candidates']} · Items: {form['items']}")
    print(f"- Mean raw score: {fmt(form['mean'])} ({fmt(100 * form['mean'] / max(form['items'], 1), 1)}%) · SD: {fmt(form['sd'])} · Range: {form['min']:.0f}–{form['max']:.0f}")
    print(f"- Reliability (KR-20): {fmt(form['kr20'])} · SEM: {fmt(form['sem'])} raw points")
    if form["candidates"] < 100:
        print(f"- ⚠️ Only {form['candidates']} candidates — item statistics are unstable below ~100; treat flags as prompts for review, not verdicts.")

    flagged = [r for r in out if r["flags"]]
    print(f"\n## Flagged items ({len(flagged)} of {len(out)})")
    for r in flagged:
        print(f"- **{r['item']}** (p={fmt(r['p'])}, r_pb={fmt(r['rpb'])}): {'; '.join(r['flags'])}")
    if not flagged:
        print("- None")

    print("\n## All items")
    print("| Item | Domain | Key | p | Corrected r_pb | Flags |")
    print("|---|---|---|---|---|---|")
    for r in out:
        print(f"| {r['item']} | {r['domain']} | {r['key']} | {fmt(r['p'])} | {fmt(r['rpb'])} | {'; '.join(r['flags'])} |")

    if any(r["distractors"] for r in out):
        print("\n## Distractor analysis")
        print("| Item | Option | Chosen by | r_pb | Note |")
        print("|---|---|---|---|---|")
        for r in out:
            for o, share, d_r, note in r["distractors"]:
                print(f"| {r['item']} | {o} | {share:.0%} | {fmt(d_r)} | {note} |")

    by_dom = defaultdict(list)
    for r in out:
        if r["domain"]:
            by_dom[r["domain"]].append(r)
    if by_dom:
        print("\n## Domain coverage")
        print("| Domain | Items | % of form | Mean p |")
        print("|---|---|---|---|")
        for d, rs in sorted(by_dom.items()):
            print(f"| {d} | {len(rs)} | {100 * len(rs) / len(out):.0f}% | {fmt(st.fmean(x['p'] for x in rs))} |")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("responses")
    ap.add_argument("key", nargs="?")
    ap.add_argument("--out", help="write per-item statistics CSV here")
    a = ap.parse_args()
    form, out = analyze(*load(a.responses, a.key))
    report(form, out)
    if a.out:
        with open(a.out, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["item", "domain", "key", "p", "corrected_rpb", "flags"])
            for r in out:
                w.writerow([r["item"], r["domain"], r["key"], f"{r['p']:.4f}",
                            "" if r["rpb"] is None else f"{r['rpb']:.4f}", "; ".join(r["flags"])])


if __name__ == "__main__":
    main()
