# The 18 tactics — full detail with examples

From Parikh, Batra & Lee, *How we write rebuttals*. "RAC" = Reviewer/Area Chair.
Each tip: the rule, why it works, and how to apply it.

### 1. Start positive
Open with a short summary that highlights the positive feedback across reviews.
Readers (especially the AC) should not lose sight of the strengths while wading
through your responses to the negatives. One or two sentences is enough.

### 2. Order matters
**Start with the biggest concerns that you have good answers for, and work your way
down to less clear-cut responses and minor points.** Do *not* order strictly by
reviewer or by review order. The first thing the AC reads should be your strongest
rebuttal to the most important objection.

### 3. Let reviewers speak, then respond directly
Quote the concern concisely and completely, then give the **direct answer first**
(often a bolded Yes/No or single line), *then* elaborate.
- *"Are these averaged across multiple runs?"* → **Yes**, averaged across 5 seeds.
- *"Are segmentation masks used during training?"* → **No**, only for evaluation.
- Complex case: quote → bold direct answer → specifics (quantitative comparison,
  dataset sizes, etc.).

### 4. Be conversational
Plain, conversational language is easier to follow and **less likely to read as
combative** than stiff formal prose.

### 5. Respond to the intent of questions
Answer what *motivated* the question, not just the literal text. *"Why didn't you
evaluate on GLORP3?"* usually questions your evaluation's adequacy in general —
answer the specific ask **and** remind the AC of the breadth you *do* have (X, Y, Z).

### 6. Don't be afraid of emphasis
Use tone/formatting to direct attention: *"Row 2 in Table 4 shows **exactly** that."*
/ *"We do **NOT** need a human-in-the-loop at test time."* Emphasis guides a skimming AC.

### 7. Feel free to set the stage
If *all* reviewers missed a central point, spend a couple of lines on a crisp recap of
the main idea before responding — realign everyone before arguing specifics.

### 8. Keep things self-contained
Assume the AC remembers little and won't re-read the paper. Re-introduce acronyms,
restate the experimental setup you're referring to. Each response should stand alone.
(This is the operational form of the neutral-third-party test.)

### 9. But get credit for details already included
If a reviewer asked for something already in the paper, cite it precisely **and restate
it**: *"As described in L341, 746, 772 … [restate the detail]."* This shows the detail
wasn't missing and builds credibility — without sounding dismissive.

### 10. Consolidate common concerns
When multiple reviewers raise the same/related point, answer it once, up front, for all
of them. Saves space and reads as coherent. (Pairs with a "Common concerns" section.)

### 11. Color-code reviewers
Use consistent formatting/labels so a reviewer can quickly find the parts relevant to
them — especially once you've merged and reordered responses away from review order.

### 12. Stats speak louder than words
**Every time you disagree with a reviewer, ask whether you can settle it with data.**
Give the AC numbers/stats, not adjectives. A measured result ends an argument that
prose only prolongs.

### 13. Don't promise, *do*
Instead of "We will discuss/add X in the paper," **put the discussion/number in the
rebuttal now**, then add that you'll incorporate it. This proves the change is real and
already done. The single most important tip for experiment-bearing rebuttals.

### 14. Be receptive and reasonable
Try reviewer suggestions **experimentally** rather than arguing why they won't work —
"maybe it will!" Most ACs appreciate the good-faith attempt, and it's simply the
collegial thing to do.

### 15. Be transparent
Acknowledge limits directly: venue forbids new experiments → say so; no good intuition
for a trend → say so and note it's under investigation; not enough GPUs → be honest; a
result came out null → report it honestly and reframe. Transparency builds trust;
overclaiming destroys it.

### 16. Shine a spotlight on bad-faith reviewing
If a review is unreasonable/unsubstantiated, make sure the *other* RACs and the AC see
it so they can discount it — point out the specific unsupported claims and reference
other reviewers who disagree. Do this surgically and evidence-based, never as a rant.

### 17. Acknowledge reviewer efforts
Thank reviewers who went above and beyond — detailed typo lists, relevant-work pointers,
constructive future-work ideas. At least a short blurb. Costs nothing, earns goodwill.

### 18. Don't forget the humans
This is a **socio-political** interaction, not only a scientific one. Decide: be
argumentative and risk a reviewer digging in against you, or find common ground.
Naming points where you *agree* with the reviewer helps the latter. Default to
building common ground unless (16) applies.

---

## Quick mapping: concern type → tips to reach for

| Situation | Reach for |
|---|---|
| Reviewer misread / missed a detail | 3, 8, 9 |
| Reviewer wants a new experiment/baseline | 13, 14, 12 |
| Reviewer disagrees on a claim | 12, 6 |
| Multiple reviewers, same concern | 10, 7 |
| Venue/compute limits block the ask | 15 |
| A result is null / weaker than hoped | 15, 12 (report honestly, reframe) |
| Review is unfair/unsubstantiated | 16, 15 |
| Reviewer gave real effort | 17, 18 |
| Writing for the decision-maker | 1, 2, 5, 8 (AC-facing) |
