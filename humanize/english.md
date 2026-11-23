# Humanize :english — Remove AI Voice

Rewrite English prose so it reads like a specific human wrote it. Based on Wikipedia's "Signs of AI writing", humanizer, unslop, and direct-statement rules — deduplicated into one catalog.

## Process

1. **Scan** for patterns below (clusters, not lone tells).  
2. **Draft rewrite** — preserve every fact; vary sentence length; prefer *is/are/has*.  
3. **Self-audit** — "What still reads as AI?" and "Did I invent any fact?" Fix both.  
4. **Final pass** — zero em/en dashes (unless user's sample uses them); read aloud.

## Direct statement rule (hard ban)

**Say what it IS, not what it is NOT.**

Ban negation-pivot sentences used to define or emphasize. Delete the negated half; keep the affirmative claim.

| Ban | Rewrite toward |
|-----|----------------|
| not X, but Y | Y, stated directly |
| not just X, it's Y | state Y; if X mattered, say it in a separate affirmative sentence |
| rather than X, Y | Y |
| This isn't about X, it's about Y | Name what it is about |
| It's not X. It's Y. (two-sentence split) | one affirmative sentence |
| X, not Y (trailing negation) | X alone, or explain the contrast affirmatively |

**Chinese equivalents** (when editing mixed text): 不是…而是…, 与其说…不如说…, 不仅仅是…更是… — same rule.

**Exemptions (rare, max one per piece):** direct quotation; factual boundary where negation is the point ("granularity is per-dataset, not per-tenant" → "granularity is per-dataset; tenant scope does not apply"); deliberate dialogue.

**Self-check:** grep for `not .* but`, `not just`, `rather than`, `isn't about`, split It's-not/It's pairs. Any hit → rewrite.

## Adding soul

Sterile prose is as loud as slop. When voice fits (blog, essay, opinion — not encyclopedic/legal):

- Have opinions; react to facts  
- High burstiness: mix 3-word punches with 30-word runs; occasional fragments  
- Specific sensory detail, not "concerning"  
- Mixed feelings, asides, self-corrections  
- End without a tidy motivational bow  

## Pattern catalog

### Content (C1–C6)

| ID | Pattern | Fix |
|----|---------|-----|
| C1 | Significance inflation — testament, pivotal, underscores, evolving landscape, indelible mark | State what happened |
| C2 | Notability lists — cited in NYT, BBC, FT without context | One source + what it said, or cut |
| C3 | Superficial -ing — highlighting, ensuring, fostering, showcasing | Delete clause or expand with source |
| C4 | Promotional — nestled, vibrant, breathtaking, must-visit, groundbreaking (figurative) | Neutral facts |
| C5 | Vague attributions — experts argue, industry reports | Name source or cut |
| C6 | Formulaic challenges — Despite challenges… continues to thrive | Specific problems or cut |

### Language (L1–L12)

| ID | Pattern | Fix |
|----|---------|-----|
| L1 | AI vocabulary — Tier-1: delve, tapestry, testament, underscore, leverage, multifaceted, realm, interplay, "it's worth noting", "in today's landscape". Tier-2 if dense: crucial, pivotal, vibrant, foster, showcase, moreover, utilize | Plain words; one Tier-3 word (key, important) alone is fine |
| L2 | Copula avoidance — serves as, stands as, boasts, features | is / are / has |
| L3 | Negative parallelisms — not only…but…, it's not just X it's Y | Direct statement (see above) |
| L4 | Rule of three — forced triads of abstract nouns | Natural count |
| L5 | Synonym cycling — protagonist / main character / central figure | Pick one term |
| L6 | False ranges — from X to Y (not a scale) | List topics |
| L7 | Em/en dash ban — **zero** `—` `–` in final text | Period, comma, colon, or restructure. Sample override only via voice calibration |
| L8 | Bold / emoji / inline-header lists — **Label:** restates label | Prose or one bold term per section |
| L9 | Title Case headings | Sentence case |
| L10 | Curly quotes | Straight `"` unless author uses curly |
| L11 | Passive / subjectless — No configuration needed. Results preserved automatically. | Name actor: You don't need… / The system preserves… |
| L12 | Hyphenated-pair overuse — the report is high-quality | Hyphenate before noun; drop after (high quality) |

### Communication (M1–M3)

| ID | Pattern | Fix |
|----|---------|-----|
| M1 | Chatbot artifacts — I hope this helps, Of course!, Would you like, Here is a | Delete |
| M2 | Cutoff / gap-fill — While details are limited… maintains a low profile | State unknown or cut; never invent filler |
| M3 | Sycophantic — Great question!, You're absolutely right! | Answer directly |

### Filler & craft (F1–F10)

| ID | Pattern | Fix |
|----|---------|-----|
| F1 | Filler — in order to, due to the fact that, at this point in time | Shorten |
| F2 | Stacked hedging — could potentially possibly | One qualifier |
| F3 | Generic upbeat endings — future looks bright, exciting times ahead | End on last concrete fact |
| F4 | Signposting — Let's dive in, Here's what you need to know | Start with content |
| F5 | Fragmented headers — heading + one line restating heading | Cut echo line |
| F6 | Diff-anchored docs — was added to replace… | Describe current state |
| F7 | Staccato drama — five clipped fragments in a row | Merge; one short sentence is fine |
| F8 | Aphorism formulas — X is the currency of Y, not a tool but a mirror | Concrete claim |
| F9 | Rhetorical openers — Honestly? Look. The thing is. (fake candor) | Say the point |
| F10 | Low density — In other words / Put simply restating same idea | One pass, cut repeats |

### Plain speech (unslop)

- **Abstract metaphor nouns** — substrate, wedge, vector, modality, paradigm, bedrock → concrete word  
- **Mechanism over vibe** — "SQL you can read" → show `.toSQL()` output  
- **Plain word** — utilize/leverage/facilitate → use/help  
- **Adverb + weak verb** — significantly improves → measured delta  

## Burstiness target

Never 3+ consecutive sentences of similar length. Mix ~5-word, ~18-word, and ~35-word sentences in each paragraph.

## False positives — do NOT flag alone

Perfect grammar; one em dash; one *however*; curly quotes from macOS/Word; formal vocabulary that isn't Tier-1; letter salutations; quoted AI examples being critiqued.

## Preserve — human signals

Hard-to-fabricate specifics; unresolved tension; era-bound slang; deliberate fragments; pre-2022 edits.

## Example

**Before:**  
> Additionally, this pivotal initiative underscores our commitment to fostering innovation in today's evolving landscape—it's not just about technology, but about culture.

**After:**  
> The initiative funds two internal tools and a weekly demo slot. Team culture shapes how those tools get used; the budget line is explicit in Appendix B.

**Direct-statement fix:**  
> It's not a tool, but a platform.  
→ **It's a platform that hosts and manages your models.**
