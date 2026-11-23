# Model-Specific AI Voice Fingerprints & Counter-Surgery Guide

> **Module Cross-Navigation ([../SKILL.md](../SKILL.md)):** Pair these generator-specific counter-surgeries with language-track catalogs ([../english.md](../english.md), [../chinese.md](../chinese.md), [bilingual-tech-writing.md](bilingual-tech-writing.md)), genre register rules ([../paper-boundaries.md](../paper-boundaries.md), [academic-prose-and-rebuttal.md](academic-prose-and-rebuttal.md), [genres-playbook.md](genres-playbook.md)), and the 3-Pass scoring rubric ([methodology-and-audit.md](methodology-and-audit.md)).

Generic AI-cleanup lists catch 2023-era boilerplate (*delve*, *tapestry*, *in today's fast-paced world*), yet miss modern drafts completely. Frontier models no longer sound like a single undifferentiated chatbot. Post-training recipes—RLHF preference datasets, Constitutional AI rubrics, Direct Preference Optimization (DPO), Group Relative Policy Optimization (GRPO), and hidden Chain-of-Thought (CoT) reasoning traces—stamp each model family with a distinct rhetorical persona.

Use this reference when:
1. **You know which model generated or polished the draft** and want surgical removal of that family's blind spots.
2. **A draft passes basic Tier-1 vocabulary checks** yet still triggers instant reader recognition (*"this reads like Claude Sonnet"*, *"一股浓浓的 DeepSeek 味"*, *"typical Gemini textbook list"*).
3. **You are writing system prompts or multi-model editing pipelines** and need preventive constraints tailored to a specific generator.

---

## Part I: The Science of LLM Stylometry & Rapid Triage

### 1. Why Model Fingerprints Persist

Recent stylometry and model-attribution research proves that LLM voices are structural, not merely lexical:

* **High-Accuracy Multi-Model Attribution (*Idiosyncrasies in Large Language Models*, Sun et al., 2025, arXiv:2502.12150):** Fine-tuned embedding classifiers separate five frontier families (ChatGPT, Claude, Gemini, Grok, DeepSeek) with **97.1% accuracy** on held-out text. Crucially, attribution remains well above chance *even when prompts ban Markdown/bolding or when another LLM paraphrases or translates the output*. Fingerprints live in word-level token distributions, clause-ordering habits, and semantic framing—not just surface formatting.
* **Phylogenetic Slop Forensics (*EQ-Bench / Slop Profile*, Sam Paech, 2024–2026):** Comparing model outputs against human corpora across three axes—**Slop Words** (over-represented single tokens), **Slop Trigrams** (clichéd 3-word collocations like *"air hung thick"* or *"voice barely audible"*), and **Contrast Regexes** (*"not just X, but Y"*)—constructs evolutionary lineage trees of LLMs. When a lab switches synthetic training-data suppliers (for example, DeepSeek shifting segments of synthetic post-training from OpenAI-like outputs toward Gemini-like distributions), the lexical mutation tree visibly jumps branches.
* **Short-Sample Syntactic Signatures (*StyloMetrix* benchmarks, Przystalski et al., 2025):** Tree-based classifiers using human-interpretable syntactic features (participial clause ratios, function-word frequencies, sentence-length variance, and punctuation entropy) identify source model families reliably in samples as short as **10 sentences**.

### 2. Where Each Layer of "AI Voice" Comes From

| Training Stage | Linguistic Artifact Introduced | Why Word-Swap Alone Fails |
| :--- | :--- | :--- |
| **Pre-training Mix & Filtering** | Baseline register bias (web essays, GitHub docs, WeChat/Zhihu high-upvote posts, textbooks) | Shapes default paragraph geometry and argument order |
| **Supervised Fine-Tuning (SFT)** | Curator "house style" (numbered bold lists, executive-summary intros, symmetrical subheadings) | Survives synonym replacement because the skeleton stays rigid |
| **RLHF / DPO / Constitutional AI** | Sycophancy, conflict-averse hedging, therapy-speak (*sit with*, *unpack*), moralizing codas | Human raters reward polite, scannable, empathetic-sounding completions in 30-second side-by-side evals |
| **Reasoning RL (CoT / GRPO)** | Stepwise dialectic residue, parenthetical edge-case qualifiers, leaked `<think>` transitions (*Wait,*, *换个角度*) | Internal verification habits bleed into external prose |
| **Synthetic Distillation** | Cross-family chimera tells (e.g., open-weights Llama/Qwen weights echoing GPT-4o contrasts or R1 aphorisms) | Requires dual-family scrubbing (host syntax + teacher vocabulary) |

### 3. Rapid Model-ID Triage Matrix ("Who Wrote This Draft?")

Scan any suspect 300-word sample against these six diagnostic axes before choosing a surgery protocol:

| Diagnostic Axis | OpenAI (GPT-4o / 4.5 / o3 / GPT-5) | Anthropic Claude (3.5 / 3.7 / 4 Sonnet & Opus) | Google Gemini (2.5 / 3 / 4 Pro & Flash) | Chinese Frontier (DeepSeek / Qwen / Kimi / Doubao) | Open-Weights (Llama 3–4 / Mistral) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Persona Archetype** | Eager TED-talker (4o) or clinical spec-sheet engineer (o3/GPT-5) | Earnest *Substack* essayist & mindful therapist | Enthusiastic textbook author & curriculum designer | 赛博鲁迅/野生文豪 (R1), 大厂高管 (Qwen), 文科助教 (Kimi), 热情搭子 (Doubao) | Polite customer-support agent (Llama) or brisk Euro-consultant (Mistral) |
| **Opening Gambit** | Contrast hook or upfront *"Definitions & Scope"* block | Faux-candid pivot: *"Here's the thing:"*, *"Look,"*, *"Truth is,"* | Pedagogical setup: *"To understand X, we first need to look at Y."* | 宏大时代背景 / *"先说结论"* / *"这个问题问到点子上了"* | *"Sure! Here is..."* or flat restatement of the user prompt |
| **Paragraph Geometry** | Uniform 3–4 sentence blocks; heavy mid-clause `—` (4o) or nested bullets (o3/5) | Metronomic alternation + isolated **1-line dramatic paragraphs** | Short intro → **numbered bold-lead list** (`1. **Label:** ...`) → takeaway box | 四字对仗小标题 + 排比三段论 + 独立金句短行 | Highly uniform 4–5 sentence paragraphs; rigid 3-bullet summaries |
| **Signature Punctuation** | Pair/single em dashes (`—`), parenthetical `(e.g., ..., specifically ...)` | Dramatic fragment + colon (`The catch: trust.`), question-mark pivots (`And honestly?`) | Bold-colon anchors (`**Scalability:**`), bulleted sub-lists | 破折号拔高（`——`）、引号造概念（`“颗粒度”`）、Emoji 点缀（豆包） | Standard commas + predictable `Furthermore,` / `Moreover,` sentence starters |
| **Signature Lexical Crutches** | *not just X—it's Y*, *underscores*, *ensuring*, *holding X constant* | *genuinely*, *unpack*, *sit with*, *worth naming*, *quietly [verb]-ing*, *load-bearing*, *that's not nothing* | *Think of X like a...*, *At its core*, *Here is a breakdown*, *Ultimately* | *不是A而是B*、*底层逻辑*、*拆解*、*赋能*、*稳稳接住*、四字成语连击 | *Moreover*, *Crucially*, *It is important to note*, *comprehensive* |
| **Closing Habit** | Punchy TED-style synthesis or safe-completion boundary caveat | Quietly philosophical, slightly melancholic one-liner | Teacherly recap: *"By balancing A and B, teams can..."* | 价值升华（*"静悄悄的革命才刚刚开始"* / *"未来可期"*） | Helpful sign-off or balanced *"both sides matter"* moral bow |

---

## Part II: OpenAI Family (GPT-4o, GPT-4.5, o1/o3 Series, GPT-5)

Treating "OpenAI style" as a monolith fails because OpenAI's lineup split into **conversational/creative models** (GPT-4o, GPT-4.5), **explicit CoT reasoning models** (o1, o3, o3-pro), and **routed safe-completion flagships** (GPT-5). Each requires different incisions.

### 1. Sub-Family Fingerprints

#### A. GPT-4o: The Contrast-Addicted People-Pleaser
* **Relentless Negative Parallelism:** Overuses antithetical pivots to manufacture insight: *"It's not about writing more code—it's about building the right abstractions."* / *"This isn't a bug; it's a structural blind spot."*
* **Breathless Em-Dash Chains:** Stuffs explanatory appositives or dramatic twists behind `—` once or twice per paragraph.
* **Participial Tail Clauses:** Appends weak `-ing` commentary onto factual clauses (*"...reducing cold-start latency by 40%, underscoring the value of regional caching and ensuring a seamless experience"*).
* **Sycophantic Ally Framing:** Opens collaborative edits or responses with *"That's a sharp distinction"* or *"You're tapping into a real tension here."*
* **Chinese GPT-4o Variant:** Heavy English-to-Chinese calque syntax (*"这不仅仅关乎效率——它更关乎我们如何重新定义协作的边界"*), dense `——` pivots, and Western abstract nouns (*景观、张力、叙事、锚点*).

#### B. GPT-4.5: The Frictionless Editorial Minimalist
* **Low Tier-1 Slop, High Structural Polish:** Rarely drops *delve* or *tapestry*, and handles subtext better than 4o. Its tell is **frictionless symmetry**: every paragraph lands with magazine-copy smoothness, balanced clause weights, and understated diplomatic hedging (*"Perhaps the harder question is..."*, *"In practice, the picture is quieter"*).
* **Conflict Rounding:** Sands off angry, weird, or hyper-specific authorial edges into polite *Atlantic*-style generality unless explicitly anchored to raw facts.

#### C. o1 / o3 / o3-pro: The Clinical Spec-Sheet Pragmatist
* **Zero Fluff, High Taxonomic Rigidity:** Reasoning models drop chatty warmth and write like a strict Staff Engineer grading an architecture doc.
* **Parenthetical Precision Overload:** Packs sentences with inline scope guards: `(assuming uniform key distribution)`, `(i.e., p99 > 200ms, not median)`, `(specifically under write-heavy contention)`.
* **Enumerated Branching:** Turns narrative prose into decision trees (`Case 1 / Case 2`, `If X holds -> Y; otherwise -> Z`) even when the reader asked for an essay or blog post.
* **Abrupt Landings:** Stops dead once the logical derivation finishes, or tacks on a dry verification checklist.

#### D. GPT-5: The Routed Safe-Completion Architect
* **Upfront Boundary & Rubric Partitioning:** Before making a claim, GPT-5 compulsively separates **definitions, scope assumptions, empirical evidence, and edge-case caveats** into neat linear blocks.
* **Risk-Hedged Precision:** Replaces bold authorial claims with scoped conditionals (*"Under standard production workloads, X generally outperforms Y, provided Z remains bounded"*). Excellent for compliance docs; lethal to voice-driven essays or chaotic creative drafts.

### 2. Diagnostic Checklist (OpenAI Forensic Scan)

Flag the text for OpenAI counter-surgery if **3 or more** appear within 400 words:
- [ ] **Contrast pivot:** Any variant of `not X, but Y` / `isn't about X—it's about Y` / `与其说…不如说…` / `不是…而是…`.
- [ ] **Em-dash density:** More than zero em dashes (`—` / `——`) when no user voice sample authorizes them.
- [ ] **Participial tail:** Clause ending in `, highlighting...`, `, underscoring...`, `, ensuring...`, `, reflecting...`.
- [ ] **Parenthetical tax:** Three or more `(e.g., ...)` / `(i.e., ...)` / `(specifically ...)` insertions in one section (o1/o3/GPT-5 tell).
- [ ] **Upfront scope throat-clearing:** Opening paragraph defines terms nobody asked to define before stating the thesis (GPT-5 tell).
- [ ] **Tricolon cadence:** Three parallel adjectives, verbs, or abstract nouns marched in lockstep (*"fast, predictable, and resilient"*).
- [ ] **Copula dodge:** Uses *serves as*, *stands as*, *represents*, or *acts as* where *is* works.
- [ ] **TED-talk closer:** Final sentence zooms out to industry destiny or team philosophy instead of stopping on the last concrete fact.

### 3. Generation-Time Counter-Prompt (OpenAI Family)

Prepend to System / Developer instructions when generating prose with GPT-4o, o3, or GPT-5:

```text
Write in direct, asymmetrical prose with concrete nouns and finite verbs.
Hard constraints:
1. Zero negative parallelisms ("not X, but Y", "isn't about X, it's about Y", "rather than X, Y"). State only what something IS.
2. Zero em dashes (—) and zero en dashes (–). Use periods, commas, or colons.
3. Zero trailing participial commentary (", highlighting...", ", ensuring...", ", underscoring..."). Cut the tail or give the fact its own sentence with a named actor.
4. Do not partition the response into "Definitions / Assumptions / Caveats" blocks unless writing a formal specification. Start directly with the sharpest concrete claim.
5. Limit parenthetical qualifiers (e.g., i.e., specifically) to at most one per 500 words; fold necessary constraints into plain clauses.
6. End on a specific fact, metric, or unresolved operational detail—never on a philosophical summary.
```

### 4. Post-Generation Counter-Surgery Rules

1. **Collapse every negation pivot:** Delete the *"It's not X"* half; fuse any real contrast into two concrete factual sentences (*"Legacy queues drop packets at 80k msg/s. Ring buffers hold zero-loss throughput to 420k."*).
2. **Amputate `-ing` tails:** Strike everything after the final comma when it starts with *highlighting, underscoring, demonstrating, fostering, ensuring*. If a real metric sits inside the tail, promote it to an active verb (*"Regional caching cut cold-start latency by 40% and kept p99 under 90ms."*).
3. **Unpack o3/GPT-5 parentheses:** Convert `(specifically when WAL segments exceed 4GB)` into normal syntax (*"when WAL segments pass 4GB"*) or cut it if obvious from context.
4. **Delete the setup paragraph:** On GPT-5 drafts, read paragraph 2 first. In 80% of cases, paragraph 1 is pure scope-hedging throat-clearing—delete it whole.

### 5. Before-vs-After Surgery Examples

#### Example 2A: GPT-4o Essay / Tech Blog Voice (English)

**Before (Raw GPT-4o):**
> Observability isn't just about collecting more metrics and logs—it's about cultivating a shared mental model of production reality. In modern distributed architectures—where a single user request can fan out across dozens of microservices—traditional dashboards serve as little more than comforting wallpaper, masking tail-latency spikes and underscoring the gap between green SLAs and frustrated users. Teams that thrive don't merely buy better tooling; they instrument business-level invariants directly into trace spans, ensuring faster incident triage and fostering genuine engineering ownership.

**Diagnosis:** Two negative parallelisms (*isn't just about... it's about*; *don't merely... they*), double em-dash parenthetical, copula dodge (*serve as*), two participial tails (*masking... underscoring...*; *ensuring... fostering...*), motivational closer.

**After (Counter-Surgery Applied):**
> Dashboards lie when a single checkout request touches forty microservices. Aggregate SLAs stay bright green while 2% of paying customers stare at a spinning button for eleven seconds. Adding more log volume rarely helps. The teams that find root causes in five minutes tag every trace span with business invariants: cart ID, payment gateway region, and retry count. When a deploy breaks checkout in Frankfurt, on-call engineers query failed carts directly instead of guessing from CPU graphs.

#### Example 2B: o3 / GPT-5 Over-Scoped Engineering Prose (English)

**Before (Raw o3 / GPT-5):**
> **Scope & Definitions:** Before evaluating local-first sync engines, it is necessary to distinguish between optimistic UI mutation (client-side state commit prior to server ACK) and deterministic conflict resolution (convergence guarantees across concurrent replicas, e.g., via CRDTs or operational transformation).
>
> Under low-concurrency regimes (specifically <= 3 active editors per document and network RTT < 150ms), server-authoritative rebase protocols generally provide lower memory overhead (avoiding tombstone bloat) while maintaining acceptable perceived latency. Conversely, under prolonged offline partitions (e.g., mobile field work), state-based CRDTs become strictly necessary despite their metadata tax (typically 2x–5x raw payload size).

**Diagnosis:** Upfront *Scope & Definitions* rubric header, four heavy parenthetical blocks in two paragraphs, stiff *it is necessary to distinguish / Conversely* scaffolding.

**After (Counter-Surgery Applied):**
> Most collaborative web apps do not need CRDTs. When two or three teammates edit a shared doc over office Wi-Fi, a server-authoritative rebase loop feels instant and avoids the 2x–5x metadata bloat that CRDT tombstones carry in memory. CRDTs earn their keep only when clients go offline for hours—field inspectors on tablets in basements, or commuters editing on subway lines—and still expect clean merges without conflict dialogs when they reconnect.

---

## Part III: Anthropic Claude Family (Claude 3.5 / 3.7 / 4 Sonnet & Opus)

Claude rarely sounds like a stiff corporate press release. Instead, Anthropic's Constitutional AI and literary/essayistic preference tuning gave Claude a recognizable **"Earnest *Substack* Essayist / Mindful Therapist"** persona. Readers on Hacker News, LessWrong, X, and `r/ClaudeAI` clock raw Claude prose within ten lines—even when zero classic ChatGPT buzzwords appear.

### 1. Signature Claude-isms Catalog

#### A. Faux-Candid Conversational Interrupters
Claude simulates intimacy by interrupting itself mid-argument with staged candor:
* *"Here's the thing:"* / *"Here's the part nobody talks about:"* / *"Here's where it gets interesting:"*
* *"Look,"* / *"Truth is,"* / *"Let's be honest about what's happening here."*
* *"And honestly?"* / *"The uncomfortable truth?"* (rhetorical fragment questions)

#### B. Therapy-Speak & Contemplative Verbs
Claude treats software bugs, market shifts, and academic arguments like emotional breakthroughs in couples therapy:
* **"Unpack":** *"Let's unpack why this abstraction leaks."*
* **"Sit with":** *"We have to sit with that tension for a moment."*
* **"Worth naming / worth pausing on":** *"There's a tension here that's worth naming explicitly."*
* **"Grapple with / reckon with / hold":** *"Engineers are still reckoning with what that means."*
* **Architectural/tactile intellectualism (heavy in 3.7 & 4 Sonnet/Opus):** *"load-bearing"* (*"That assumption is doing a lot of load-bearing work"*), *"the shape of the problem"*, *"doing heavy lifting"*, *"texture"*.

#### C. Intensifier & Litotes Crutches
* **"Genuinely":** Claude's single highest-frequency tell (*"genuinely hard"*, *"genuinely novel"*, *"genuinely useful"*). Used to insist it isn't exaggerating—which immediately signals it is an LLM.
* **"Quietly [verb]-ing":** *"quietly reshaping"*, *"quietly load-bearing"*, *"quietly broken"*.
* **Double-negative understatement (litotes):** *"And that's not nothing."* / *"Which is no small thing."*

#### D. Staccato 1-Line Paragraph Drama & The Colon Punchline
* **Metronomic Single-Line Paragraphs:** Claude builds a 3-sentence paragraph, then drops an isolated 5-to-9-word sentence on its own line for theatrical gravitas:
  > *And then the cache expired.*
  > *That changes everything.*
  > *Nobody wanted to own the migration.*
* **Fragment-Colon Punchlines:** Short noun phrase + colon + dramatic reveal:
  > *The catch: nobody measured memory bandwidth.*
  > *The result: silent data loss.*
  > *One problem: physics.*

#### E. Generation Splits Inside Claude (3.5 vs. 3.7 Extended Thinking vs. Claude 4 Sonnet/Opus)
* **Claude 3.5 Sonnet:** Brisk, warm, high frequency of *"Here's the thing"* and *"genuinely"*, eager to organize messy notes into clean narrative arcs.
* **Claude 3.7 Sonnet (Extended Thinking):** Prone to **self-correcting mid-paragraph caveats** (*"Wait—that framing oversimplifies slightly, because..."*) and exhaustive edge-case hedging born from long internal thinking blocks.
* **Claude 4 Sonnet & Opus:** Higher literary polish; **Opus** leans toward lyrical, slightly melancholic essayism (*"the quiet weight of legacy code"*, *"something irreducibly human"*), architectural metaphors (*"load-bearing"*), and symmetrical circular endings that echo the opening image.
* **Chinese Claude Voice (中文温和随笔/反思腔):** Reads like a polite humanities columnist: *"说到底，……"*, *"某种程度上"*, *"这背后其实藏着一个容易被忽视的问题"*, *"值得我们停下来想一想"*, *"诚然……但……"*, *"并非偶然"*, paired with frequent single-sentence paragraphs.

### 2. Diagnostic Checklist (Claude Forensic Scan)

Flag the draft for Claude counter-surgery if **3 or more** appear:
- [ ] **Faux-candor pivot:** *Here's the thing*, *Here's where it gets interesting*, *And honestly?*, *Look,*, *说到底*.
- [ ] **Therapy/essay verb:** *unpack*, *sit with*, *worth naming*, *reckon with*, *grapple with*, *值得停下来想一想*.
- [ ] **Adverb crutch:** *genuinely*, *quietly*, *deeply*, *fundamentally* modifying ordinary adjectives/verbs.
- [ ] **Litotes tag:** *That's not nothing*, *no small feat*, *doing a lot of heavy lifting*, *load-bearing* (used figuratively).
- [ ] **Staccato 1-liners:** Two or more isolated single-sentence paragraphs within 500 words used for dramatic pause.
- [ ] **Fragment-colon reveal:** `The catch: ...`, `The problem: ...`, `The takeaway: ...`, `答案很简单：……`.
- [ ] **Circular lyrical coda:** Final paragraph callbacks poetically to the opening anecdote with understated melancholy.

### 3. Generation-Time Counter-Prompt (Claude Family)

Prepend when drafting or editing with Claude 3.5 / 3.7 / 4 Sonnet or Opus:

```text
Write as a domain practitioner reporting facts and concrete mechanisms—not as a reflective essayist or coach.
Banned phrases and constructions:
- Never use conversational stage whispers: "Here's the thing", "Here's where it gets interesting", "Look,", "Truth is,", "And honestly?", "Let's be real", "说到底", "值得停下来想一想".
- Never use therapy or meta-commentary verbs: "unpack", "sit with", "worth naming", "reckon with", "grapple with", "hold space", "that's not nothing", "doing heavy lifting", or figurative "load-bearing".
- Ban the adverbs "genuinely", "quietly", and "fundamentally". Let numbers and concrete nouns carry emphasis.
- Ban isolated one-sentence paragraphs used for dramatic pacing, and ban fragment-colon punchlines ("The catch: ...", "The result: ..."). Group related claims into full, unevenly sized paragraphs (4–7 sentences mixed with 2–3 sentence paragraphs).
- Do not close with a quiet philosophical reflection or circular callback to the opening. Stop when the technical or factual argument is complete.
```

### 4. Post-Generation Counter-Surgery Rules

1. **Delete every stage-whisper opener:** Strip *"Here's the thing:"* and *"And honestly?"*—the clause that follows almost always stands stronger on its own.
2. **Merge staccato 1-liners back into neighbor paragraphs:** Pull isolated dramatic sentences up into the preceding paragraph as its final clause, or attach them to the concrete evidence that follows.
3. **Replace *genuinely / quietly / load-bearing* with measurements or mechanisms:** Change *"a genuinely tricky concurrency bug in a quietly load-bearing service"* to *"a race condition in the billing webhook worker that processes 90% of renewals"*.
4. **Convert fragment-colons into normal verbs:** Change *"The catch: index rebuilds lock the table."* to *"Rebuilding the index locks the table for twenty minutes."*
5. **Lop off the Opus melancholic bow:** Check the last two sentences. If they zoom out to human nature, craft, or *"the quiet reality of building software"*, cut both.

### 5. Before-vs-After Surgery Examples

#### Example 3A: Claude 3.7 / 4 Opus Reflective Tech Essay (English)

**Before (Raw Claude):**
> Everyone talks about migrating off monoliths like it's a routing problem.
>
> Here's the thing: the code is rarely the hard part. What makes legacy migrations genuinely brutal is the organizational memory quietly baked into ten-year-old `if` statements—little patches written at 2 a.m. for enterprise contracts nobody on the current team remembers signing.
>
> It's worth naming that tension before you draw a single microservice box. Because when you delete a weird validation branch you don't understand, you aren't cleaning up tech debt.
>
> You're pulling out a load-bearing wall.
>
> The catch: your staging suite won't tell you until quarter-end billing runs. And honestly? Sitting with that uncertainty is what separates senior systems work from greenfield résumé-driven architecture.

**Diagnosis:** *Here's the thing*, *genuinely*, *quietly*, *It's worth naming that tension*, negative pivot (*you aren't X. You're Y*), figurative *load-bearing wall* as a dramatic 1-line paragraph, *The catch:*, *And honestly?*, *Sitting with that uncertainty*, preachy closer.

**After (Counter-Surgery Applied):**
> Routing traffic out of a monolith is straightforward; deciphering ten-year-old `if` branches in the billing module is where rewrites stall. Half of those branches look like dead code until you trace them back to custom SLA clauses in three enterprise contracts from 2018. Staging tests rarely cover those paths because nobody mocked the legacy EDI payloads. Delete an ugly validation check on Tuesday and everything stays green until quarter-end invoicing misfires on March 31. Before splitting any service boundary, audit production branch hit-counts over a full billing quarter so you know which quirks still move money.

#### Example 3B: Claude Chinese Reflective Prose (中文温和随笔腔)

**Before (Raw Claude CN):**
> 很多人以为做开源项目最难的是写出漂亮的第一版代码。
>
> 但说到底，真正决定一个项目生死的，从来不是发布那天的 Star 数。
>
> 真正难的，是在热度退去之后的第三个月，面对几十个边界模糊的 Issue，依然能耐着性子守住架构的克制。这背后其实藏着一种很容易被忽视的张力：用户的短期需求是发散的，而好工具的核心抽象必须是收敛的。某种程度上，学会对合理但越界的 PR 说“不”，这本身就是一件很有分量的事。值得每一个维护者停下来想一想。

**Diagnosis:** Single-line paragraph drama, *说到底*, *从来不是…真正难的是…*, *这背后其实藏着…容易被忽视的张力*, *某种程度上*, *这本身就是一件很有分量的事* (*that's not nothing* calque), *值得…停下来想一想*.

**After (Counter-Surgery Applied):**
> 开源项目最熬人的阶段是发布三个月后。新奇感过了，Issue 区堆满各种顺手提的功能请求：有人要内置鉴权，有人要兼容老版本配置，每个需求单看都挺合理。全盘照收只要半年，原本三千行就能讲清楚的核心库就会膨胀成没人敢改的缝合怪。维护者最硬的基本功就是拒掉八成越界 PR，哪怕对方态度再诚恳、代码写得再干净，只要偏离定位就不合入主干。

---

## Part IV: Google Gemini Family (Gemini 2.5, Gemini 3, Gemini 4)

Google's RLHF rubric heavily rewards **scannability, instructional clarity, and exhaustive sub-topic coverage**. Consequently, raw Gemini outputs—across Flash and Pro tiers from 2.5 through 3 and 4—default to an **"Enthusiastic Textbook Author / Corporate Curriculum Designer"** voice. Even when asked a casual two-sentence question, unprompted Gemini tries to hand you a laminated study guide.

### 1. Signature Gemini-isms Catalog

#### A. Compulsive Numbered Bold Lead-In Lists
Gemini's loudest structural tell is breaking continuous thought into `1. **Bold Noun Phrase:** Sentence that repeats the bold noun phrase`:
> 1. **Memory Locality:** Memory locality refers to how closely data is packed in cache lines...
> 2. **Lock Contention:** Lock contention occurs when multiple threads compete...

#### B. Explicit Pedagogical Signposting
Gemini narrates its own outline like a lecturer advancing slides:
* *"To understand X, we first need to look at Y."*
* *"Here is a breakdown of the core mechanisms driving this shift:"*
* *"Let's break this down into three key dimensions:"*
* *"At its core, [Topic] boils down to..."*
* *"Ultimately, choosing between A and B depends on your specific workload."*

#### C. Unsolicited Everyday Analogies ("The Waiter Reflex")
Even when addressing staff engineers or PhD researchers, Gemini reflexively inserts freshman-level analogies:
* *"Think of an event loop like a single waiter managing ten restaurant tables..."*
* *"Imagine a giant public library where nobody returns books to the desk..."*
* Chinese equivalent: *"简单来说，我们可以把共识算法想象成一群人在微信群里投票决定今晚吃什么……"*

#### D. Exhaustive Taxonomic Bucketing ("Even-Handed Encyclopedia Syndrome")
With massive context windows, Gemini 2.5 Pro, 3, and 4 summarize long documents cleanly—yet suffer from **editorial flatness**. Instead of foregrounding the single anomalous finding that matters, Gemini groups everything into symmetrical buckets (*Technical Factors / Operational Factors / Cultural Factors* or *Short-Term / Medium-Term / Long-Term*), giving equal paragraph weight to critical blockers and trivial housekeeping.

#### E. Chinese Gemini Voice (中文科普讲义 / 培训课件腔)
Reads like a polished corporate training deck: opens with *"简单来说，X 的核心逻辑可以拆解为以下几个方面："*, stacks numbered bold bullets with colons (`1. **吞吐量瓶颈：** ……`), sprinkles analogies (*"打个比方"*), and closes with *"总而言之，在实际落地时需要根据具体场景权衡利弊。"*

### 2. Diagnostic Checklist (Gemini Forensic Scan)

Flag the draft for Gemini counter-surgery if **3 or more** appear:
- [ ] **Bold-anchor list:** Three or more numbered or bulleted items starting with `**Concept Name:**` followed by a definition sentence.
- [ ] **Slide-advance signpost:** *Here is a breakdown*, *To understand X, we must first*, *Let's break this down*, *下面我们从三个维度来解析*.
- [ ] **Freshman analogy:** *Think of X like a...*, *Imagine a...*, *打个比方，就像……* in a piece aimed at domain peers.
- [ ] **Boilerplate essence phrase:** *At its core,*, *Simply put,*, *归根结底*.
- [ ] **Symmetrical 3-pillar taxonomy:** Splitting a messy reality into *People / Process / Technology* or *Speed / Cost / Quality* buckets with identical bullet counts.
- [ ] **Non-committal consultant closer:** *Ultimately, the right choice depends on your specific needs and trade-offs.*

### 3. Generation-Time Counter-Prompt (Gemini Family)

Prepend when drafting articles, essays, or technical memos with Gemini 2.5 / 3 / 4:

```text
Write in continuous, cohesive paragraphs for an audience of experienced domain peers.
Strict formatting and style rules:
1. NO numbered lists or bulleted lists with "**Bold Label:**" lead-ins. Weave distinctions into prose paragraphs using concrete transitions.
2. NO pedagogical signposting ("Here is a breakdown", "To understand X, we must first", "At its core", "Let's explore", "In summary"). Start directly inside the subject matter.
3. NO everyday analogies ("Think of X like a restaurant waiter / library / highway"). Explain mechanisms directly using domain terminology.
4. Take a clear analytical hierarchy: spend 70% of the space on the primary bottleneck or sharpest insight instead of giving equal coverage to minor secondary factors.
5. Never end with "Ultimately, choosing X vs. Y depends on your specific use case." State exact decision thresholds (numbers, scale limits, or failure modes) and stop.
```

### 4. Post-Generation "De-Scaffolding" Surgery Rules

1. **Melt bold-header lists into prose:** Delete the numbers and bold colons (`1. **Latency:** Latency increases when...` → `Tail latency jumps when...`). Fuse short related items into one dense paragraph; give the dominant mechanism its own full paragraph.
2. **Excise the analogy paragraph:** Delete any *"Think of X like..."* block outright unless the user explicitly asked for a beginner explainer.
3. **Kill outline narration:** Cut every sentence whose grammatical subject is *this section*, *the breakdown below*, or *we* (*"First, we need to examine..."*).
4. **Replace *"depends on your use case"* with hard thresholds:** Change *"Ultimately, you must balance consistency and latency"* to *"Use synchronous quorum writes for ledger balances; use async replication with a 500ms staleness budget for feed counters."*

### 5. Before-vs-After Surgery Examples

#### Example 4A: Gemini Technical Explainer (English)

**Before (Raw Gemini Pro):**
> To understand why vector indexes degrade under heavy streaming updates, we first need to look at how HNSW graphs organize memory. Think of an HNSW index like a multi-story express highway system: top layers have few exits for fast long-distance jumps, while the ground floor connects every local street.
>
> Here is a breakdown of the three core bottlenecks during high-churn ingestion:
> 1. **Graph Repair Overhead:** Graph repair overhead occurs when deleted nodes leave broken neighbor pointers, forcing background threads to rewire edges.
> 2. **Memory Fragmentation:** Because HNSW stores variable-length adjacency lists in RAM, frequent inserts and tombstones fragment allocator pages.
> 3. **Cache Thrashing:** Random pointer chasing across non-contiguous graph nodes causes high L3 cache miss rates during concurrent reads.
>
> Ultimately, choosing between HNSW and disk-backed IVF-PQ indexes depends on your specific latency requirements and update volume.

**Diagnosis:** Textbook setup (*To understand X, we first need to look at*), highway analogy, *Here is a breakdown of the three core bottlenecks*, `1. **Bold Label:**` echo definitions, consultant closer (*Ultimately, choosing... depends on your specific...*).

**After (Counter-Surgery Applied):**
> HNSW indexes shine on static datasets and fall apart when you delete and re-insert 10% of your vectors every hour. Each deletion leaves tombstone nodes wired into the proximity graph; clearing them forces background workers to lock neighbor lists and recompute edges while live queries are chasing pointers across the same RAM pages. Because those adjacency lists sit at scattered heap addresses, concurrent reads suffer L3 cache misses on almost every hop, pushing p99 search latency from 8ms past 90ms. If your workload mutates more than 5% of vectors per hour and can tolerate 15–25ms query times, partitioned IVF-PQ on NVMe beats in-memory HNSW at a fraction of the RAM bill.

#### Example 4B: Gemini Chinese Analytical Digest (中文科普讲义腔)

**Before (Raw Gemini CN):**
> 简单来说，要理解为什么很多企业级 Agent 项目在 Demo 阶段表现惊艳、上线后却频频翻车，我们可以把它比作“在温室里学开车”与“在晚高峰闹市区送外卖”的区别。核心痛点主要体现在以下三个维度：
>
> 1. **长链路误差累积：** 长链路误差累积是指当单步工具调用准确率为 95% 时，连续执行 10 步后的整体成功率会跌至 60% 以下。
> 2. **脏数据与异常返回：** 真实业务接口经常返回格式不规范的报错信息，导致模型解析失败。
> 3. **权限与回滚缺失：** 一旦 Agent 误操作写入脏数据，缺乏事务回滚机制会带来业务风险。
>
> 总而言之，团队在推进 Agent 落地时，需要根据自身的业务容错率，在自主性与确定性之间找到最佳平衡点。

**Diagnosis:** *简单来说，要理解……我们可以把它比作……*, *核心痛点主要体现在以下三个维度*, 1-2-3 bold-colon echo definitions, *总而言之……在A与B之间找到最佳平衡点*.

**After (Counter-Surgery Applied):**
> 企业 Agent 从内部演示走到生产环境，死得最快的地方是十步以上的工具调用链。就算单步调用准确率做到 95%，串跑十步的端到端成功率也只剩 59.8%。更麻烦的是线上老系统的接口从来不按文档出牌——HTTP 状态码返回 200，正文里却塞一段中文报错字符串，模型当场开始瞎猜参数重试。没有幂等键和补偿回滚兜底，写库类工具根本不敢放开自动执行。目前能稳定跑在线上的方案，基本都把固定流程收回到确定性状态机里，只留意图路由和非结构化字段抽取两步交给模型。

---

## Part V: Chinese Frontier Models (DeepSeek-R1/V3, Qwen, Kimi, Doubao)

Generic translated English de-slopping checklists miss 70% of native Chinese LLM tells. Chinese frontier models were post-trained on distinct slices of the Chinese internet—WeChat viral essays (微信公众号爆款), high-upvote Zhihu analyses (知乎万字长文), enterprise/civil-service reports (大厂周报与体制内公文), and Xiaohongshu lifestyle copy (小红书种草贴). Each family exhibits an unmistakable native fingerprint.

### 1. DeepSeek-R1 & DeepSeek-V3: "赛博鲁迅 / 野生文豪 + 思维链外溢"

DeepSeek-R1 (and V3 derivatives) combines fierce logical density with an over-dramatic literary streak that Chinese communities instantly dub **"DeepSeek 味"**.

#### A. Reasoning-Trace (`<think>`) Leakage & CoT Dialectic Residue
* **Raw Tag / Token Leakage:** Misconfigured API wrappers, streaming parsers, or R1-distilled smaller weights leak raw internal reasoning directly into body text: opening with `Wait,`, `Let's re-evaluate`, `Hmm,`, `不对，这里要换个角度想`, `让我重新梳理一下用户的需求`, or leaving unclosed `</think>` tags.
* **Structural CoT Residue:** Even when `<think>` blocks are stripped cleanly, R1's final prose often mirrors its internal GRPO self-debate—arguing with an imaginary opponent step-by-step (*"你可能会问……但事实果真如此吗？恰恰相反……"*) or over-explaining every intermediate deduction.

#### B. 公众号金句腔 & 宏大叙事拔高 (Civilizational Melodrama)
* **Grand-Narrative Inflation:** Give DeepSeek a mundane topic—fixing a CSS layout bug, running a campus coffee stand, or refactoring a cron job—and it escalates within two paragraphs to **civilizational destiny**: *时代的尘埃、历史的十字路口、硅基荒原、命运的齿轮、认知的边界、降维打击、一场静悄悄的革命*.
* **Aphorism Addiction (金句癖):** Ends sections with quotable-sounding but hollow epigrams:
  * *"在不确定性的迷雾中，寻找那枚确定的锚点。"*
  * *"所有命运馈赠的捷径，早已在暗中标好了算力的价格。"*
  * *"时代抛弃你的时候，连一句报错都不会打印。"*
  * *"稳稳地接住每一个普通人的焦虑。"*

#### C. 强迫症式对仗小标题 & 四字成语轰炸
* **Hyper-Symmetrical Headings:** DeepSeek compulsively formats H2/H3 headings into matching character counts with colons:
  * `一、破局之道：从流量内卷到价值深耕`
  * `二、重构底座：从单点突破到生态闭环`
  * `三、终局思维：从工具理性到人文回归`
* **Four-Character Idiom Barrages (四字词飞镖):** Stacks 3–5 four-character idioms per paragraph (*毋庸置疑、息息相关、重中之重、双管齐下、破茧成蝶、裹足不前、振聋发聩*), smoothing out natural spoken Chinese rhythm into ceremonial drumbeats.

#### D. 破折号（`——`）电击癖 & “不是A，而是B”成瘾
* Uses Chinese double em dashes (`——`) every few sentences to force a dramatic pause or redefine a noun (*"这不仅是一次版本更新——更是一场关于信任的重新立约"*).
* Relentlessly deploys `不是……而是……` / `从来不是……而是……` / `与其说是……不如说是……`.
* *Note on DeepSeek in English:* Slop-forensics phylogeny shows DeepSeek's English prose carries a hybrid OpenAI + Gemini synthetic vocabulary footprint, heavy contrast pivots, and unusually dramatic metaphors (*"a quiet tectonic shift"*, *"crucible"*, *"razor's edge"*).

---

### 2. Qwen / 通义千问: "大厂高管周报 + 体制内公文正规军"

Alibaba's Qwen family excels at structured instruction following, coding, and enterprise documentation, defaulting to a **"Senior Corporate Director / Civil-Service Report"** register.

* **大厂黑话矩阵 (Internet-Giant Jargon):** High unprompted density of *颗粒度、拆解、抓手、闭环、赋能、组合拳、底层逻辑、方法论、沉淀、对齐、感知、心智、水位、打法、全链路*.
* **公文与汇报体框架:** Opens with *"在……的大背景下，随着……的深入推进"*; structures body text around *"围绕三大核心目标，重点抓好以下四方面工作"*; closes with *"稳步推进、持续赋能、实现高质量发展"*.
* **滴水不漏的对称中庸:** Loves three-way diplomatic balancing (`既要保证……，又要兼顾……，还要防范……`), leaving zero personal edge, slang, or concrete vulnerability.

---

### 3. Kimi / 月之暗面: "温和文科助教 + 知乎高赞读书笔记腔"

Tuned heavily for long-document digestion and readable synthesis, Kimi defaults to a **"Gentle Humanities TA / Top-Upvoted Zhihu Explainer"** voice.

* **知乎拆解套路:** Opens or transitions with *"先说结论："*, *"很多人容易忽略一个关键细节："*, *"不妨换个角度来看这个问题"*, *"如果把时间线拉长，你会发现……"*.
* **过渡连接词泛滥:** Glues paragraphs together with dense connective tissue: *首先、其次、再者、与此同时、换句话说、更为关键的是、总而言之、综上所述*.
* **长文温和磨平效应:** When summarizing 100-page PDFs or messy transcripts, Kimi smooths sharp disagreements, ugly failures, and weird outliers into gentle, well-mannered prose (*"温柔而坚定"*, *"在某种意义上达成了微妙的平衡"*).

---

### 4. Doubao / 豆包: "字节系高情商生活搭子 + 小红书/客服热情腔"

Optimized for low-friction daily chat, voice interaction, and social copy, Doubao defaults to **"High-EQ Cheerleader / Xiaohongshu Copywriter"**.

* **高情绪价值客服开场:** Reflexively praises or comforts the user before answering: *"这个问题问得太到位了！"*, *"太棒了，咱们一起来捋一捋"*, *"别急，其实这件事没那么复杂"*.
* **小红书网感模板:** Heavy emoji confetti (✨🔥💡📌🙌), exaggerated hooks (*"家人们谁懂啊"*, *"宝子们听我一句劝"*, *"狠狠拿捏"*, *"干货满满建议收藏"*), and exclamation-mark inflation (`！` at the end of every third sentence).
* **“顺得有点假”的无毛刺口语:** Uses brisk colloquial Chinese, yet every sentence lands with unnatural cheerfulness and tidy 1-2-3 takeaways—zero genuine hesitation, irritation, or rough domain grit.

---

### 5. Side-by-Side Chinese Model Forensic Checklist

| 诊断信号 (Signal) | DeepSeek (R1/V3) | Qwen (通义千问) | Kimi (月之暗面) | Doubao (豆包) |
| :--- | :--- | :--- | :--- | :--- |
| **思维链残留 (`Wait,` / `换个角度`)** | **极高** (API/蒸馏版重灾区) | 低 (QwQ 推理版偶见) | 低 (k1.5 推理版偶见) | 低 |
| **四字对仗小标题 (`破局之道：从X到Y`)** | **极高 (标志性口癖)** | 高 (偏公文四字词) | 中 | 低 (偏口语问句标题) |
| **破折号金句拔高 (`——这是一场…`)** | **极高** | 低 | 中 | 低 |
| **大厂黑话 (`颗粒度/抓手/闭环/拆解`)** | 中 | **极高** | 中 | 中 |
| **连接词体操 (`首先/其次/再者/综上所述`)** | 低–中 | 高 | **极高** | 中 |
| **客服捧场与感叹号 (`太棒了！` + Emoji)** | 极低 | 极低 | 低 | **极高** |

---

### 6. Generation-Time Counter-Prompts (Chinese Frontier Models)

#### A. Anti-DeepSeek-Slop & Anti-CoT-Leakage Prompt (专治 DeepSeek 金句、对仗与思维链外溢)

```text
直接输出最终正文，绝对禁止在正文中暴露任何思考过程、自我反驳或类似“Wait”“Let's”“让我看看”“换个角度想”的推理痕迹。
文风硬约束（违者重写）：
1. 严禁宏大叙事与金句拔高：禁止出现“时代浪潮、历史十字路口、硅基、命运齿轮、锚点、底色、静悄悄的革命、稳稳接住、降维打击”等词，写具体的人、数字、报错、时间点和动作。
2. 严禁对仗小标题：小标题必须长短不一、用大白话直陈事实（如“把同步导出改成异步队列”），严禁写成“一、破局之道：从X到Y”或四字词对称结构。
3. 严禁“不是A，而是B”“与其说A，不如说B”“不仅是A，更是B”句式；直接说它是什么。
4. 全文破折号（——）清零；四字成语全文不超过 2 个，禁止四字词连用。
5. 结尾停在最后一个具体事实或待解问题上，严禁升华主题或展望未来。
```

#### B. Anti-Qwen/Kimi/Doubao Jargon & Template Prompt (专治大厂黑话、知乎套路与热情客服腔)

```text
用一线业务/技术人员跟同事复盘的平实口吻写作，删掉一切客套开场和总结陈词。
硬约束：
1. 零客套与零 Emoji：严禁“这个问题很好”“咱们一起来看看”“家人们/宝子们”，正文不准出现任何表情符号，感叹号全文清零。
2. 拉黑互联网与公文黑话：严禁使用“赋能、抓手、闭环、颗粒度、拆解、底层逻辑、组合拳、沉淀、对齐、水位、全方位、多维度、稳步推进”。换成具体的动作、指标或代码逻辑。
3. 禁用机械连接词：禁止用“首先、其次、再者、与此同时、总而言之、综上所述”串段落；禁止“既要…又要…还要…”对称排比。
4. 打破均匀段落：允许两句话一段与六七句话一段交替，把最核心的结论或踩坑细节直接放在第一句。
```

---

### 7. Post-Generation Counter-Surgery Rules (Chinese Models)

1. **Scrub `<think>` & dialectic scaffolding:** Regex-strip any leaked `<think>...</think>` blocks plus self-Q&A transitions (*"那么问题来了……事实果真如此吗？"* → state the counter-fact directly).
2. **Smash symmetrical headings (破除对仗小标题):** Rewrite every `四字词：从X到Y` heading into an asymmetrical verb-object or plain noun phrase (`二、重构底座：从单点工具到协同闭环` → `把三个脚本合并成一套统一配置`).
3. **Purge `——` and `不是…而是…`:** Replace `——` with periods or commas; delete the negated clause in every `不是A，而是B`.
4. **De-idiomize 4-character clusters:** Wherever two or more 4-character idioms appear in one sentence (*毋庸置疑，这与系统稳定性息息相关*), replace both with plain spoken verbs (*这事直接决定系统稳不稳定*).
5. **Translate Qwen jargon into concrete mechanics:** *对齐颗粒度* → *把接口字段定义核对一致*; *形成业务闭环* → *跑通从下单到退款对账的全流程*; *沉淀方法论* → *整理成两页排查清单*.
6. **Deflate Doubao cheerleading & Kimi glue:** Delete opening praise, strip all `✨🔥💡` emojis and `！`, and delete paragraph-leading *首先 / 其次 / 再者 / 综上所述*.

---

### 8. Before-vs-After Surgery Examples (Chinese Models)

#### Example 5A: DeepSeek-R1 宏大叙事 + 对仗小标题 + 破折号金句腔

**Before (Raw DeepSeek-R1):**
> ### 一、 困局之殇：从算力狂飙到工程泥潭
> 在大模型浪潮席卷全球的今天，无数团队正站在历史的十字路口。我们曾以为参数量的指数级跃升能抚平一切业务褶皱——但现实却给出了一记振聋发聩的耳光。真正决定 AI 应用生死的，从来不是实验室里光鲜亮丽的榜单分数，而是生产环境中那些沉默而琐碎的工程细节。
>
> 当延迟飙升、幻觉频发，那些堆砌起来的华丽 Prompt 瞬间化作硅基荒原上的泡沫。在不确定性的迷雾中，唯有回归工程常识，才能找到那枚确定的锚点。这场静悄悄的突围，才刚刚开始。

**Diagnosis:** Symmetrical `四字词：从X到Y` heading, *浪潮席卷 / 历史的十字路口*, `——` melodrama (*振聋发聩的耳光*), *从来不是……而是……*, *硅基荒原 / 不确定性的迷雾 / 确定的锚点*, *这场静悄悄的突围，才刚刚开始*.

**After (Counter-Surgery Applied):**
> ### 线上延迟和幻觉比榜单分数难啃得多
> 去年我们把内部客服模型从 7B 换到 72B，测试集准确率涨了 9 个点，结果上线第一周就被业务方投诉到回滚。高峰期首字延迟从 0.8 秒飙到 6.5 秒，用户等不及直接关页面；更要命的是促销规则一改，旧知识库没及时刷新，模型照着过期条款给客户乱承诺退差价。靠改写几百字的系统提示词根本压不住这类事故。最后真正管用的全是苦活：做缓存分级把高频问答截流在模型前面，再给退款金额加上硬编码规则校验。

#### Example 5B: Qwen / Kimi 大厂周报黑话 + 知乎连接词套路

**Before (Raw Qwen / Kimi):**
> 在当前降本增效的大背景下，如何进一步打通研发效能闭环，已成为技术团队的重中之重。首先，我们需要对现有的 CI/CD 流水线进行全方位的颗粒度拆解，识别出影响构建速度的核心卡点。其次，通过引入增量编译与分布式缓存这套组合拳，全方位赋能一线研发同学，缩短反馈周期。再者，既要追求极致的发布效率，又要筑牢线上稳定性的水位线。综上所述，只有将工程工具沉淀为可复用的底层方法论，才能实现研发效能的螺旋式上升。

**Diagnosis:** *在……大背景下*, *闭环 / 重中之重 / 颗粒度拆解 / 卡点 / 组合拳 / 全方位赋能 / 水位线 / 沉淀 / 底层方法论 / 螺旋式上升*, *首先 / 其次 / 再者 / 综上所述*, *既要……又要……*.

**After (Counter-Surgery Applied):**
> 后端主仓库现在的 CI 构建一次要跑 38 分钟，开发提个两行代码的修复也得干等半小时。上周排查下来，七成时间耗在全量拉取依赖和重复跑未改动模块的单元测试上。这个月准备先改两件事：把 Maven 依赖缓存挂到本地宿主机盘，再按 Git 变更目录只触发受影响模块的测试集，目标先把合并前流水线压到 10 分钟以内。灰度阶段的自动回滚阈值保持不变，报错率超 0.5% 照常停发。

#### Example 5C: Doubao 热情搭子 + 小红书网感腔

**Before (Raw Doubao):**
> 这个问题问得太棒了！🙌 很多刚读研的宝子们在看英文顶会论文时都会一头雾水，别焦虑，这真的超级正常！✨ 今天咱们就一起来拆解一下超实用的“三遍读论文法”，干货满满建议先码住收藏哦！💡
> 1. **第一遍海选扫读🔥：** 只看标题、摘要和图表，5分钟快速拿捏这篇论文到底值不值得精读！
> 2. **第二遍顺藤摸瓜📌：** 跳过复杂的数学公式推导，重点看作者是怎么设计实验打败 Baseline 的！
> 只要坚持练上二十篇，相信你一定能轻松捅破科研窗户纸，未来可期，冲就完事啦！💪

**Diagnosis:** Sycophantic opener (*这个问题问得太棒了！*), *宝子们 / 拿捏 / 干货满满建议先码住收藏 / 冲就完事啦*, heavy emoji confetti (`🙌✨💡🔥📌💪`), exclamation mark on every single sentence, motivational closer.

**After (Counter-Surgery Applied):**
> 刚进组看顶会论文，最忌讳从第一行逐词查字典啃到最后一页。省力气的读法是分三趟：第一趟花五分钟只扫标题、摘要和主架构图，判断跟手头课题没关系就直接关掉；第二趟越过定理证明，直接翻到实验表和消融实验，看它在哪个数据集上涨了点、去掉哪个模块掉得最狠；只有确定要复现或者借用它的思路时，第三趟才回过头对着开源代码把公式细节抠明白。精读够二十篇同方向论文，基本就能一眼看出哪段是在凑篇幅、哪张表才是真本事。

---

## Part VI: Open-Weights Models (Llama 3–4 & Mistral Family)

Open-weights models deployed via local inference, vLLM, or cloud endpoints exhibit distinct **"RLHF Assistant Wrapper"** and **"Synthetic Distillation"** fingerprints compared against proprietary frontier labs.

### 1. Meta Llama Family (Llama 3 / 3.1 / 3.3 / 4 Instruct)

* **Chat-Wrapper Bookends:** Smaller and mid-sized Instruct checkpoints (8B–70B) frequently leak polite customer-service bookends unless constrained: *"Sure, here is the revised section:"* at the top, and *"I hope this helps! Let me know if you would like me to adjust the tone."* at the bottom.
* **Metronomic Paragraph Uniformity:** Because Llama post-training leans heavily on synthetic preference pairs generated from predecessor Llama checkpoints, raw Instruct prose settles into remarkably uniform 4-sentence paragraphs with flat sentence-length variance.
* **Heavy Discourse-Marker Glue:** High density of sentence-initial `Furthermore,`, `Moreover,`, `Additionally,`, `Consequently,`, `It is important to note that`, and `In conclusion,`.
* **Safety-Tuned Moralizing Codas:** In opinion essays, historical analyses, or creative fiction, standard Llama Instruct weights tend to sand off moral ambiguity and append a sanitized, balanced *"Ultimately, mutual respect and careful regulation are essential"* lecture at the end.

### 2. Mistral Family (Mistral Large, Medium, Nemo, Small)

* **Brisk Continental Conciseness:** Mistral models generally produce punchier sentence-length variation and fewer sycophantic therapyisms than Claude or Llama—making them popular in open-weights creative writing.
* **Compulsive Bullet Compartmentalization:** On expository or analytical prompts, Mistral Instruct aggressively fragments prose into crisp, dry Markdown bullet hierarchies with short headers, reading like a French management-consulting slide deck.
* **Formal Lexical Drift:** Occasionally slips formal Romance-cognate verbs and nouns (*ameliorate*, *pertinent*, *vis-à-vis*, *modalities*, *valorize*) into otherwise plain English technical prose.

### 3. Distilled & Fine-Tuned Chimera Models (Critical Caveat)

Many popular open-weights checkpoints (`DeepSeek-R1-Distill-Llama-70B`, `DeepSeek-R1-Distill-Qwen-32B`, or community SFT tunes trained on GPT-4o / Claude outputs) carry **dual-family chimera tells**:
* A `Distill-Qwen` checkpoint will exhibit **DeepSeek-R1 reasoning leakage and contrast aphorisms** wrapped inside **Qwen's enterprise vocabulary**.
* Community RP/creative fine-tunes trained on synthetic GPT-4o/Claude datasets concentrate **EQ-Bench Slop Trigrams** (*"let out a breath she didn't know she was holding"*, *"a tapestry of shadows"*, *"voice barely above a whisper"*) at 5x–10x human baseline rates.

### 4. Diagnostic Checklist (Llama & Mistral Forensic Scan)

Flag the draft for Open-Weights counter-surgery if **3 or more** appear:
- [ ] **Assistant chat wrapper:** Opening *"Sure! Here is..."* / *"Certainly!"* or closing *"I hope this helps! Let me know if..."*.
- [ ] **Discourse-marker stacking:** Three or more sentences starting with *Furthermore,*, *Moreover,*, *Additionally,*, *Consequently,*, or *In conclusion,* in one page.
- [ ] **4-sentence block monotony:** Consecutive paragraphs with nearly identical word counts (75–95 words) and zero short-sentence variation (Llama Instruct signature).
- [ ] **Dry bullet fragmentation:** Turning an essayistic or narrative prompt into terse consulting-deck sub-bullets without transitions (Mistral Instruct signature).
- [ ] **Romance-cognate stiffness:** Unprompted *ameliorate*, *pertinent*, *vis-à-vis*, *modalities*, or *valorize* in everyday technical prose (Mistral signature).
- [ ] **Chimera tells:** `<think>` residue or aphoristic contrasts colliding with generic assistant transitions (`Distill-Llama` / `Distill-Qwen` checkpoints).
- [ ] **Unsolicited moral coda:** Closing an analytical or fictional draft with a safety-tuned *"Ultimately, responsible governance and mutual respect remain vital"* lecture.

### 5. Generation-Time Counter-Prompt (Llama / Mistral)

```text
Output ONLY the requested body text—zero conversational preamble ("Sure, here is...") and zero closing offers ("Let me know if...").
Style constraints:
1. Ban sentence-initial transition crutches: "Furthermore,", "Moreover,", "Additionally,", "Consequently,", "It is important to note", "In conclusion,". Connect sentences through shared subjects and cause-and-effect verbs instead.
2. Break paragraph uniformity: alternate short 2-sentence paragraphs with longer 6-sentence paragraphs, and vary sentence length from 5 words to 30+ words.
3. Do not convert prose arguments into Markdown bullet lists unless explicitly asked for a checklist, and avoid stiff formalisms ("ameliorate", "modalities", "vis-à-vis").
4. Never append an ethical disclaimer, "both sides" balancing paragraph, or uplifting moral lesson at the end.
```

### 6. Post-Generation Counter-Surgery Rules

1. **Strip chat bookends:** Delete everything above the first substantive claim and below the last concrete fact.
2. **Delete transition adverbs at sentence starts:** Strike `Furthermore, `, `Moreover, `, `Additionally, `, and `In conclusion, `. In 95% of cases, the two sentences already connect cleanly without glue; where they don't, link them by repeating the concrete noun subject.
3. **Shatter 4-sentence Llama blocks:** Combine two adjacent medium sentences with a semicolon or active participle, then follow with a blunt 6-word sentence to break the metronome.
4. **Re-hydrate Mistral slide bullets & swap stiff cognates:** Stitch dry bullet fragments back into cause-and-effect narrative paragraphs, and swap *ameliorate / modalities / vis-à-vis* for *fix / modes / compared with*.
5. **Dual-scrub distilled chimeras:** On `R1-Distill` outputs, run DeepSeek `<think>` + contrast scrubbing *first*, then strip Llama/Qwen transition glue *second*.

### 7. Before-vs-After Surgery Examples

#### Example 6A: Llama Instruct Uniformity & Discourse-Marker Glue

**Before (Raw Llama Instruct):**
> Sure! Here is an overview of why SQLite works well for single-node web services:
>
> SQLite has gained significant traction for production web applications running on a single virtual machine. Furthermore, because the database engine runs in-process with the application, queries avoid network round-trip serialization overhead entirely. Moreover, enabling Write-Ahead Logging (WAL) mode allows concurrent readers to proceed without blocking behind a single active writer. Additionally, backups become straightforward file-copy or `.backup` stream operations to object storage. In conclusion, while SQLite is not designed for multi-region write scaling, it is important to note that it provides a reliable and cost-effective architecture for many modern workloads.

**Diagnosis:** *"Sure! Here is..."* wrapper, uniform sentence lengths (16–24 words each), four consecutive stacked discourse markers (*Furthermore, Moreover, Additionally, In conclusion*), *"it is important to note that"*, generic wrap-up.

**After (Counter-Surgery Applied):**
> Running SQLite in WAL mode on a single NVMe box eliminates the network hop that eats most Postgres query time. A `SELECT` over indexed local pages finishes in microseconds; you can run 200 queries to render one HTML page and still answer in under 15ms. Readers never block each other, and one writer commits serially up to tens of thousands of transactions per second if you batch writes inside short transactions. Nightly backups stream incremental WAL frames straight to S3 via Litestream. You give up multi-node write failover, which is a trade most internal tools and regional SaaS apps should take gladly.

#### Example 6B: Mistral Bullet Compartmentalization & Formal Lexical Drift

**Before (Raw Mistral Large):**
> Incident postmortems fail to ameliorate repeat outages when organizations treat them as compliance artifacts vis-à-vis engineering learning loops.
> - **Blame attribution:** Focusing on human operator error obscures systemic tooling gaps.
> - **Action-item decay:** Remediation tickets lacking explicit owners and SLA deadlines rarely reach completion.
> - **Follow-up modalities:** Asynchronous document distribution yields lower retention than live adversarial tabletop reviews.

**Diagnosis:** Stiff Romance formalisms (*ameliorate*, *vis-à-vis*, *modalities*), abrupt slide-deck bulletization of an essay paragraph, passive nominalizations (*Asynchronous document distribution yields...*).

**After (Counter-Surgery Applied):**
> Postmortems stop preventing repeat outages the moment teams treat them like insurance paperwork. Naming the engineer who pasted the wrong command hides the real bug: a deploy script that accepted an unquoted wildcard against production. Even strong root-cause writeups rot when remediation tickets land in the backlog without a single owner and a two-week deadline. Teams that actually cut repeat incidents skip passive doc links and run a thirty-minute live review where peers poke holes in the fix.

---

## Part VII: Cross-Model De-Slopping Workflows & Guardrails

### 1. The "Persona Substitution Trap" in Multi-Model Editing

A common failure mode in AI-assisted writing is **single-blind model relay**: generating a draft in GPT-4o and pasting it into Claude with *"Make this sound more human."*
* **What actually happens:** Claude dutifully deletes GPT-4o's *underscores*, *fostering*, and mid-sentence em dashes—and immediately injects *"Here's the thing:"*, *"genuinely"*, *"sit with that tension"*, and three dramatic one-line paragraphs. You traded an OpenAI fingerprint for an Anthropic fingerprint.

### 2. The 3-Step Cross-Family Scrubbing Protocol

When using an LLM to de-slop text (whether generated by itself or another model), run an **Adversarial Cross-Family Pass**:

1. **Step 1 — Identify Source Family (or Chimera Pair):** Run the Rapid Triage Matrix (Part I.3) to spot the dominant generator (e.g., Gemini numbered-bold scaffolding or DeepSeek symmetric headings).
2. **Step 2 — Apply Both Source Surgery AND Editor Restraint:** Feed the draft to your editor model alongside:
   * The **Post-Generation Surgery Rules** of the *source* model family, **AND**
   * The **Generation-Time Counter-Prompt** of the *editor* model family (so the editor cannot stamp its own signature onto the rewrite).
3. **Step 3 — Deterministic Regex & Rhythm Audit:** Run a mechanical final sweep before trusting the output:
   * Search for `—` / `——`, `not .* but`, `不是.*而是`, `Here's the thing`, `genuinely`, `unpack`, `sit with`, `At its core`, `Furthermore`, `Moreover`, `首先.*其次`, `颗粒度`, `赋能`, `<think>`.
   * Check paragraph silhouettes visually: if every paragraph is 4 lines tall (Llama/GPT) or littered with 1-line dramatic islands (Claude) or bold-colon lists (Gemini), merge and split manually.

### 3. Narrative & Creative Writing Slop Quarantine (Cross-Model Attractors)

Across GPT-4o, Claude, Gemini, DeepSeek, and Llama, creative writing prompts converge on identical training-data attractors documented by EQ-Bench *Slop Forensics*. Ban these outright in fiction, case studies, and illustrative scenarios unless supplied by the user:

* **Over-Represented Character & Persona Names:** *Elara, Lyra, Kael, Thorne, Vance, Silas, Marcus, Maya, Aria, Evelyn, Leo*, and default *Dr. Sarah Chen / Alex Rivera* in tech vignettes. Pick mundane, culturally grounded names from real census distributions.
* **Sensory & Action Slop Trigrams:**
  * *"let out a breath [he/she] didn't realize [he/she] was holding"*
  * *"the air hung thick with [tension / unspoken words / ozone]"*
  * *"a testament to..."* / *"a stark reminder"*
  * *"voice barely above a whisper"* / *"a ghost of a smile"*
  * *"neon-drenched"* / *"concrete jungle"* / *"hum of fluorescent lights"* (in every tech-office opening scene)
  * Chinese fiction/essay equivalents: *眼神里闪过一丝不易察觉的……*、*嘴角勾起一抹弧度*、*空气仿佛在这一刻凝固*、*指尖微凉*、*命运的齿轮开始转动*.

### 4. Anti-Overcorrection Guardrails (Do Not Break Good Writing)

Aggressive de-slopping goes wrong when editors over-steer into artificial informality or strip legitimate technical structure. Enforce four guardrails:

1. **The Anti-Cringe Rule (No Fake "Human" Cosplay):**
   * Never inject forced typos, lowercase-only affectation, performative profanity, or dated internet slang (*"ngl"*, *"tbh"*, *"lowkey"*, *"咱就是说"*, *"家人们"*, *"绝绝子"*, *"苦笑不得"*) to "lower AI detection scores." Forced slang screams *prompted AI* louder than formal prose ever did. Real human authority comes from **specific mechanisms, exact numbers, concrete failure modes, and asymmetrical rhythm**.
2. **Domain Register Protection:**
   * o3/GPT-5's explicit assumption blocks, Qwen's formal regulatory phrasing, and Gemini's numbered sequences are **defects in essays and blogs**, yet **mandatory in RFCs, formal proofs, security advisories, legal contracts, and runbooks**. Strip empty meta-signposting (*"Here is a breakdown of the steps:"*), keep genuine operational numbering (`Step 1: Drain regional traffic before rotating keys`).
3. **Cluster Threshold over Single-Word Paranoia:**
   * Do not mutilate natural prose over one isolated word. Human writers occasionally write *genuinely*, *quietly*, *ultimately*, or *换句话说*. Intervene when **3+ family tells cluster in the same section** or repeat as a structural tic across paragraphs.
4. **Strict Fact, Quote, & Code Immutability:**
   * Counter-surgery alters **framing, syntax, rhythm, and empty scaffolding only**. Never invent metrics to look concrete (use `[TODO: exact latency]` if unknown and user asks for placeholders, otherwise state the known fact plainly), never alter quoted speech or citations, and never touch identifiers inside code blocks or LaTeX math.
