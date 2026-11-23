# Rebuttal skeleton + worked example

## Structure (top → bottom = most decision-relevant first)

```
1. Summary & thanks            ← Tip 1, 17. 2-3 sentences: restate the agreed
                                  strengths (quote the reviewers' own words), thank
                                  specific effort.

2. Common concerns (all RACs)  ← Tip 10, 7. Answer each concern >1 reviewer raised,
   - C1 ...                       once, up front. This is usually where the paper's
   - C2 ...                       central rebuttal lives.

3. Per-reviewer responses      ← Tip 2 order WITHIN each reviewer by strongest-answer-
   To Reviewer A (scores)         first; lead with the reviewer whose concerns you
     - Q: <quote> A: <bold> ...   answer most decisively. Tip 3 format throughout.
   To Reviewer B ...
   To Reviewer C ...

4. Note to the Area Chair      ← THE part beginners omit. Decision-oriented summary:
   - Standing (scores, no ethics flags)   consensus strengths, how the two/three
   - How each concern was addressed        shared concerns were addressed (not
   - Scope of the claim                     deferred), scope of the contribution,
   - Any calibration flag (Tip 16)          any bad-faith/miscalibration flag, and a
   - Request                                clear ask.
```

Every block must pass the neutral-third-party test (Tip 8): self-contained, restates
setup/acronyms, and makes the resolution legible without the paper.

## Micro-templates

**Direct answer (Tip 3):**
> *Reviewer: "Are results averaged over runs?"*
> **Yes** — all numbers are means over 5 seeds (setup in §4.1); std < 0.4 in every cell.

**Already-in-paper (Tip 9), no new data needed:**
> This is reported in §4.2 / Table 3, L341: [restate the number]. We will make it more
> prominent.

**Stat instead of argument (Tip 12 + 13 — compute, don't promise):**
> We ran the ablation the reviewer suggested: it changes accuracy by **+0.3 (n.s.,
> p=0.41)**, confirming the effect is not driving our result. We add this as Table X.

**Transparent limitation (Tip 15):**
> The venue does not permit new large-scale runs during the response period. On the
> subset we could run (N=…), the trend holds: [number]. We flag the full study as a
> camera-ready addition and state this honestly in Limitations.

**Null/weaker-than-hoped result (Tip 15 + 12):**
> On the enlarged set the effect is **directional but not significant** (Δ=…, 95% CI
> […]). We therefore reframe the claim from "significantly increases X" to "shifts X in
> the expected direction," and report the effect size rather than a p-value.

**Decomposition anchor (Tip 9 + 12) — "which part fails?" asked about an
already-reported aggregate:**
> The data is already in the paper: Appendix Table X scores all five components and
> reports their mean. You are right that the mean hides which one fails, so we
> decompose it below — the bottom row reproduces Table X's column exactly, so this is
> an analysis of *reported* results, not new claims.

Anchoring the new breakdown to a number the reviewer can verify in the submitted PDF
makes it credible *and* earns credit for the original table.

**Note to AC (the decision-oriented close):**
> All reviewers credit [consensus strength]. The two shared concerns — [C1], [C2] —
> are addressed with new numbers in this response, not deferred: [one-line each]. We do
> not claim [out-of-scope thing]; the contribution is [scoped claim]. We believe this
> clears the bar for [decision]; at minimum it is a strong [fallback decision].

**Silent-reviewer note (some reviewers haven't replied as the window closes):**
> While Reviewers [A] and [B] may still respond during the remaining discussion
> period, we would be grateful if the AC could also weigh the evidence already posted:
> [A]'s main concern ([X]) is addressed by [computed artifact]; [B]'s request for [Y]
> is addressed by [computed artifact].

Names each silent reviewer's top concern and the *artifact* (not prose) that answers
it — so a no-show reviewer can't read as an unaddressed reviewer.

## AC dashboard: two summary tables

The Note-to-AC lands hardest when "how each concern was addressed" is two compact
tables the AC can scan in seconds, instead of a paragraph. (Pattern from a real
author response whose score rose during the discussion period; **all values below
are invented** — fill in your own.)

**Table A — reviewer standing.** One row per reviewer. Show score *movement*, not
just scores — a raise after the response is the strongest signal an AC can get, so
make it impossible to miss; "no reply yet" and "replied, unchanged" are information
too (see the silent-reviewer note). "W / S" = counts of that reviewer's numbered
Weaknesses / Suggestions — the same labels the Table B columns cite.

| Reviewer | Overall (pre → post response) | Other scores | W / S |
|---|---|---|---|
| R1 | 3 → 3 (replied; concerns marked resolved) | Confidence 4 | 3 W, 2 S |
| R2 | 3.5 → no reply yet | Confidence 3 | 4 W, 1 S |
| R3 | 2.5 → **3 ↑** (raised after our response) | Confidence 4 | 6 W, 2 S |

**Table B — concern-coverage matrix.** One row per *consolidated* concern, ordered
by priority; reviewer columns cite each reviewer's own W/S numbering. (If a venue's
reviews are unnumbered free prose, invent short stable labels — "baselines",
"stats" — and use them consistently in the per-reviewer sections too.) This is
Tips 2 + 10 + 11 in table form.

| Priority | Concern / suggestion | R1 | R2 | R3 | Done? | Evidence in this response |
|---|---|---|---|---|---|---|
| High | Comparison with prior tools / SOTA | W3 | – | W1 | ✓ | 2 new baseline tables |
| High | Statistical support for claim [X] | – | W1, S2 | – | ✓ | 5-seed study, 95% CIs |
| Medium | Component-level failure analysis | W1 | – | S3 | ✓ | per-component breakdown table |
| Medium | Reproducibility | – | W4 | W5 | ✓ | pinned versions, code release |
| Low | Typos / figure fixes | S2 | – | S1 | ✓ | manuscript swept |

Rules that make the matrix work:

- **Consolidate**: shared concerns collapse into one row (Tip 10); the reviewer
  columns keep each reviewer's own W/S labels so everyone finds their concern (11).
- **Priority order** the rows (Tip 2) — the AC reads top-down; the first row is your
  strongest answer to the biggest objection.
- **"Done?" means done**: ✓ only when the evidence is *in the response* (Tip 13).
  Honestly deferred items get a scoped label ("camera-ready") instead — one honest
  open cell buys credibility for every ✓ (Tip 15).
- **Evidence column points at artifacts** — a table, a CI, an ablation — never
  "see our response to W2".

A compilable LaTeX skeleton with both tables, per-reviewer colour coding, and
shaded quote boxes is in [../assets/rebuttal-template.tex](../assets/rebuttal-template.tex).

## Pre-submission checklist

- [ ] Every itemized concern has a response (cross-check the spreadsheet).
- [ ] Opens positive (1); closes with an AC-facing decision summary.
- [ ] AC close includes the standing table and concern-coverage matrix (or their
      one-paragraph equivalent when space forbids tables).
- [ ] Ordered strongest-first, not reviewer-order (2).
- [ ] Every disagreement is backed by a number, not an adjective (12).
- [ ] No "we will add X" without the X already in the response (13).
- [ ] Every response passes the neutral-third-party test (8).
- [ ] Placeholders all filled with computed values — none left as promises.
- [ ] Claims match what the data actually shows — no silent overclaim (13, 15).
- [ ] Real reviewer effort acknowledged (17); tone collaborative (4, 18).
- [ ] Within the venue's length/format limit.
