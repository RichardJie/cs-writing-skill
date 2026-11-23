# Humanize :english — Remove AI Voice (Definitive English De-AI Guide)

Rewrite English prose so it reads like a specific, thinking human wrote it at full attention.

> **Module Cross-Navigation ([SKILL.md](SKILL.md)):**
> - **Academic Narrative & Papers:** Apply [paper-boundaries.md](paper-boundaries.md) (Press-Conference Principle) *before* sentence-level de-slopping, paired with [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md).
> - **Model-Specific Fingerprints:** When scrubbing GPT-4o/o3/GPT-5, Claude Sonnet/Opus, Gemini, DeepSeek, or Llama/Mistral drafts, pair with [references/model-fingerprints.md](references/model-fingerprints.md).
> - **Genre-Specific Playbooks:** For READMEs, postmortems, LinkedIn/X/Substack, cold emails, SOPs, resumes, PRDs, video scripts, and fiction, pair with [references/genres-playbook.md](references/genres-playbook.md).
> - **3-Pass Engine & 100-Point Audit:** See [references/methodology-and-audit.md](references/methodology-and-audit.md).

This guide synthesizes and deduplicates five empirical and editorial lineages into one operational specification:

1. **Wikipedia WikiProject AI Cleanup (`WP:AISIGNS`)** — crowdsourced forensic catalog of unvetted LLM prose across millions of encyclopedic edits.
2. **Computational LLM Stylometry** — excess-vocabulary frequency spikes documented by Kobak et al. (*Science Advances*, "Delving into ChatGPT usage in academic writing through excess vocabulary") and Liang et al. ("Monitoring AI-Modified Content at Scale" across ICLR/NeurIPS peer reviews and scientific abstracts).
3. **Open-Source Anti-Slop & Humanizer Toolkits** — `blader/humanizer`, `unslop`, `stop-slop`, and direct-statement rule catalogs.
4. **Classic English Prose Craft** — George Orwell (*Politics and the English Language*), William Strunk Jr. & E.B. White (*The Elements of Style*), William Zinsser (*On Writing Well*), Paul Graham (*Write Simply*, *Write Like You Talk*), Joseph M. Williams (*Style: Lessons in Clarity and Grace*), Helen Sword (*Zombie Nouns*), and Gary Provost (*100 Ways to Improve Your Writing*).
5. **ESL / Bilingual De-Slopping Practice** — rescuing non-native technical and academic drafts from trading minor L2 awkwardness for heavy synthetic "GPTese."

---

## 1. Execution Process & Operating Principles

Run every `:english` rewrite through four sequential passes. Never try to fix vocabulary, structure, rhythm, and punctuation in a single blind regeneration.

1. **Scan (Cluster Diagnosis)** — Flag patterns from the catalog below (`C1–C6`, `L1–L12`, `M1–M3`, `F1–F10`). Hunt **clusters**, not lone tells: one *"crucial"* or one *"however"* in 600 words is normal human writing; three Tier-1 words, a negative parallelism, two participial `-ing` tails, and four em dashes in two paragraphs is unmistakable slop.
2. **Draft Rewrite (Structural & Lexical Surgery)** — Preserve every verifiable fact, number, date, name, quote, and citation. State what things *are* rather than what they are *not*. Prefer plain copulas (*is / are / has*) or concrete physical verbs over inflated substitutes. Vary sentence length deliberately across every paragraph.
3. **Self-Audit (Fact & Slop Verification)** — Ask two hard questions: *"What still reads like an LLM hedging or performing significance?"* and *"Did I invent, extrapolate, or round any fact?"* Fix both immediately. Run the Direct-Statement grep checks (Section 4.4) and Vocabulary checks (Section 3).
4. **Final Pass (Punctuation & Ear Test)** — Enforce **zero** prose em dashes (`—`), prose en dashes (`–`), and double-hyphen dash substitutes (`--`), unless the user supplied a writing sample that explicitly uses them. Read the result aloud: anywhere you run out of breath or sound like a press release, cut or split.

### Register & Voice Calibration Hierarchy

- **User writing sample wins first.** If the user provides a sample of their own prose, match their sentence length, contraction habits, person (`I` vs. `we` vs. impersonal), and punctuation preferences over default bans.
- **Register governs temperature.**
  - *Encyclopedic, legal, specification, API reference, academic methods:* neutral, dry, high-density, zero cheerleading, zero forced slang.
  - *Essays, engineering blogs, postmortems, columns, memos:* opinionated, specific, rhythmically varied, willing to admit trade-offs or uncertainty.
- **Preserve information, never paragraph geometry.** Merge three repetitive AI paragraphs into two tight sentences, or split one bloated 45-word clause pileup into a crisp setup and a punchline.

---

## 2. Master Pattern Catalog (`C1–C6`, `L1–L12`, `M1–M3`, `F1–F10`)

Every diagnostic ID from the core `humanize` specification is preserved below with expanded forensic markers and deterministic fixes.

### 2.1 Content Patterns (`C1–C6`)

| ID | Pattern | Telltale Surface Markers | Root Pathology & Deterministic Fix |
|----|---------|--------------------------|------------------------------------|
| **C1** | **Significance inflation** | *stands as a testament to, plays a pivotal role, underscores the importance, evolving landscape, indelible mark, watershed moment, vital cornerstone, transformative impact* | LLMs cannot state a plain event without grading its historical importance. **Fix:** Delete the importance claim; state the concrete event, metric, date, or mechanism and let the reader judge weight. |
| **C2** | **Notability name-dropping lists** | *featured in The New York Times, BBC, Financial Times, and Forbes; widely cited across top venues* (with zero substance) | Mimics PR boilerplates and Wikipedia notability defenses. **Fix:** Keep one primary source and state *what it actually reported*, or delete the list. |
| **C3** | **Superficial `-ing` tail clauses** | *, highlighting X; , underscoring Y; , ensuring Z; , fostering A; , showcasing B; , paving the way for C; , reflecting a broader trend* | Sentence-final present participles tacked onto a complete clause to manufacture fake analytical depth. **Fix:** Cut the comma + `-ing` clause outright, or promote it into an independent sentence backed by a specific fact or citation (see Section 5.1). |
| **C4** | **Promotional / brochure puffery** | *nestled in the heart of, vibrant hub, breathtaking, must-visit, groundbreaking, cutting-edge, world-class, rich cultural heritage, seamless experience* | Training bias from travel copy, SaaS landing pages, and press releases. **Fix:** Replace evaluative adjectives with verifiable physical, architectural, or quantitative attributes. |
| **C5** | **Vague attributions (weasel authority)** | *experts argue, industry reports suggest, observers note, critics contend, many researchers believe, it is widely recognized* | Simulates balanced sourcing when the model has no citation. **Fix:** Name the exact author, paper, institution, or report + year; if none exists in the source text, delete the attribution or state the claim only if already substantiated. |
| **C6** | **Formulaic "Despite challenges" arc** | *Despite facing significant challenges… continues to thrive; While obstacles remain, the initiative has resiliently…* | Pre-baked concessive essay template. **Fix:** Name the exact failure mode, bottleneck, or cost with numbers, or cut the concession entirely. |

### 2.2 Language & Grammar Patterns (`L1–L12`)

| ID | Pattern | Telltale Surface Markers | Root Pathology & Deterministic Fix |
|----|---------|--------------------------|------------------------------------|
| **L1** | **AI vocabulary spikes** | **Tier-1 (kill on sight):** *delve, tapestry, testament, underscore, leverage (v.), multifaceted, realm, interplay, beacon, embark, spearhead, burgeoning, poised, "it's worth noting", "in today's landscape"*. **Tier-2 (kill when clustered):** *crucial, pivotal, vibrant, foster, showcase, moreover, furthermore, utilize, holistic, nuanced, seamlessly, robust, meticulous, intricate, commendable*. | Post-RLHF lexical mode collapse (see Section 3). **Fix:** Replace with concrete domain verbs/nouns or everyday English (*use, build, test, show, field, part*). One isolated Tier-3 word (*key, important, main*) is fine. |
| **L2** | **Copula avoidance** | *serves as, stands as, functions as, acts as, boasts, features, sports, represents a, marks a* | Programmatic allergy to plain *"to be"* and *"to have."* **Fix:** Restore `is`, `are`, `was`, `were`, `has`, `have`, or use a literal physical verb (see Section 5.2). |
| **L3** | **Negative parallelisms** | *not X, but Y; not just X, it's Y; not only… but also…; rather than X, Y; This isn't about X—it's about Y; less about X and more about Y* | Manufactured rhetorical contrast (antithesis addiction). **Fix:** Hard ban. Delete the negated half and state the affirmative claim directly (see Section 4). |
| **L4** | **Rule-of-three tricolons** | *fast, scalable, and secure; innovation, efficiency, and growth; analyze, synthesize, and deploy* | Statistical preference for symmetric triads in adjectives, verbs, and abstract nouns. **Fix:** Use the true count of items: one exact point, two asymmetric facts, or a complete four-item spec (see Section 5.3). |
| **L5** | **Synonym cycling ("elegant variation")** | Referring to the same entity in four consecutive sentences as *the cache -> the storage layer -> the in-memory buffer -> this mechanism* (or *protagonist / main character / central figure*) | Misapplied creative-writing rule against word repetition, causing severe referential ambiguity in technical and analytical prose. **Fix:** Pick one canonical noun and repeat it (or use a clean pronoun `it`/`they`). |
| **L6** | **False ranges** | *from startups to healthcare; ranging from Rust macros to developer burnout; from strategic vision to daily standups* | `From X to Y` used where X and Y do not sit on a shared, continuous scale. **Fix:** Reserve `from X to Y` for genuine numeric, temporal, geographic, or hierarchical endpoints; otherwise list the items directly (see Section 5.4). |
| **L7** | **Em/en dash overuse (Hard Ban)** | Prose `—` (em dash), `–` (en dash as parenthetical/range crutch), or `--` between clauses | LLMs use dashes as grammatical duct tape to splice loosely related thoughts without choosing a real syntactic relation. **Fix:** **Zero** `—` or `–` in final prose. Convert to a period, comma, colon, parentheses, or restructured clause (see Section 5.5). Sample override applies *only* when calibrating to a user's own dash-heavy sample. |
| **L8** | **Bold / emoji / inline-header lists** | `🚀 **Scalability:** Scalability ensures that the system scales...` | RLHF formatting reward for scannable "structured" chat answers. **Fix:** Convert decorative bullet walls back into connected prose paragraphs; if a list is genuinely tabular/enumerative, drop emojis and never echo the bold label in the sentence that follows; cap inline bolding at zero or one key term per section. |
| **L9** | **Title Case headings** | `### Understanding The Core Architectural Trade-Offs And Future Directions` | Content-marketing / SEO blog template habit. **Fix:** Use **Sentence case** for all section headings (`### Core architectural trade-offs`), capitalizing only the first word, proper nouns, and standard acronyms. |
| **L10** | **Curly / smart quotes** | `“...”` and `‘...’` injected into Markdown/code-adjacent text | Tokenizer preference for typographic quotation marks in web-scraped books/articles while humans typing in Markdown/editors produce straight ASCII quotes. **Fix:** Normalize to straight `"` and `'` unless matching an author's established typographic pipeline. |
| **L11** | **Passive / subjectless evasion** | *No configuration needed. Results are preserved automatically. Consideration was given to latency.* | Hides who performs the action or who bears responsibility. **Fix:** Name the concrete actor as the grammatical subject: *You don't need to configure anything. The worker writes results to disk.* |
| **L12** | **Hyphenated-pair overuse** | *The report is high-quality; a data-driven, future-proof, enterprise-grade, human-centric workflow* | Two errors combined: (a) wrongly hyphenating predicate compounds after the noun, and (b) stacking synthetic marketing compound modifiers. **Fix:** Hyphenate compound modifiers *before* a noun (*a high-quality report*), drop the hyphen *after* the noun (*the report is high quality*), and purge empty `-driven` / `-centric` / `-ready` buzz-compounds. |

### 2.3 Communication & Chatbot Artifacts (`M1–M3`)

| ID | Pattern | Telltale Surface Markers | Root Pathology & Deterministic Fix |
|----|---------|--------------------------|------------------------------------|
| **M1** | **Chatbot wrapper artifacts** | *Certainly!, Of course!, Here is a revised version:, I hope this helps!, Let me know if you'd like me to adjust the tone, Happy to help!* | Leftover assistant turn-taking framing leaked into document prose. **Fix:** Delete 100% of conversational wrappers. Start at the first word of the text itself; end at the last word of the text. |
| **M2** | **Cutoff disclaimers & speculative gap-fill** | *While specific details remain limited in public sources…, maintains a relatively low profile, As of my last knowledge update…* | When an LLM lacks facts about a person or system, it invents dignified-sounding fog to conceal ignorance. **Fix:** State only verified facts from the input; if something is unknown and needs noting, say plainly what is unrecorded—never pad with *"maintains a low profile."* |
| **M3** | **Sycophantic validation** | *Great question!, You're absolutely right to point that out!, That's a deeply insightful framing!* | RLHF helpfulness/agreeableness conditioning. **Fix:** Delete praise and answer or argue the substance directly. |

### 2.4 Filler, Pacing & Rhetorical Slop (`F1–F10`)

| ID | Pattern | Telltale Surface Markers | Root Pathology & Deterministic Fix |
|----|---------|--------------------------|------------------------------------|
| **F1** | **Bureaucratic wordy filler** | *in order to, due to the fact that, at this point in time, has the ability to, in the event that, with regard to, a wide variety of* | Multi-word prepositional padding where one short word works. **Fix:** *to, because, now, can, if, about, many*. |
| **F2** | **Stacked epistemic hedging** | *could potentially possibly, might arguably tend to suggest, seems to somewhat indicate* | Cowardly double/triple qualification. **Fix:** Pick **one** honest epistemic marker (*may*, *can*, or a concrete probability/condition) or state the bound directly. |
| **F3** | **Generic upbeat / moralizing endings** | *The future looks bright, exciting times lie ahead, Ultimately the key is striking a balance, Only time will tell* | Essay-conclusion reflex that wraps every topic in a warm TED-talk bow. **Fix:** Stop on the final concrete finding, trade-off, or open technical question (see Section 6.2). |
| **F4** | **Meta-signposting & throat-clearing** | *Let's dive in, Here's what you need to know, In this section we will explore, Before we begin it is essential to understand* | Announces that writing is about to happen instead of starting. **Fix:** Delete the warmup sentence and open directly with the claim, problem, or event (see Section 6.1). |
| **F5** | **Fragmented echo headers** | `## Caching strategy` followed immediately by *"This section describes our caching strategy and why caching matters."* | Zero-information repetition between heading and first sentence. **Fix:** Start directly under `## Caching strategy` with *"Redis stores session tokens with a 15-minute TTL."* |
| **F6** | **Diff-anchored documentation** | *This flag was added to replace the legacy timeout behavior; We updated the parser so it now supports…* (inside evergreen docs) | Prompting an LLM with a PR diff causes it to narrate edit history inside reference docs. **Fix:** In evergreen docs/READMEs, describe **current system behavior** timelessly; keep change history solely in `CHANGELOG.md` or commit messages. |
| **F7** | **Staccato drama ("LinkedIn broetry")** | *Most teams fail at this. Every single time. Why? Complexity. Full stop. Let that sink in.* | Overcorrection against stiff prose that produces breathless, manipulative one-line fragments. **Fix:** Merge theatrical fragments into real sentences with concrete subjects and actions; limit deliberate short fragments to rare, earned emphasis. |
| **F8** | **Synthetic aphorism formulas** | *Trust is the currency of leadership; Code is a liability, not an asset; AI isn't a replacement, it's a mirror; Clarity is kindness.* | Fortune-cookie epigrams generated to sound quotable on social feeds. **Fix:** Replace the slogan with the actual operational mechanism or empirical observation. |
| **F9** | **Fake-candor rhetorical openers** | *Honestly?, Look., The truth is,, Here's the thing:, Let's be real for a second:, Spoiler alert:* | Simulated intimacy used by modern LLMs when told to "sound casual/conversational." **Fix:** Cut the performative throat-clear; real candor comes from admitting a concrete mistake or unpopular trade-off, not typing *"Honestly?"* |
| **F10** | **Low-density restatement loops** | *In other words…, Put simply…, That is to say…, Essentially, what this means is…* | The model writes an opaque first sentence and then translates itself instead of writing clearly once. **Fix:** Delete the opaque first sentence and the *"Put simply"* bridge; keep only the clear version. |

---

## 3. Tiered AI Vocabulary Blacklists & Concrete Replacement Matrices

### 3.1 Why Lexical Spikes Betray AI Text (Stylometric Grounding)

Large-scale corpus studies demonstrate that post-2023 LLMs exhibit extreme, non-human lexical concentration:
- **Kobak et al. (*Science Advances*)** analyzed 14+ million PubMed abstracts and found sudden post-ChatGPT frequency explosions in style words—not content terms—led by **`delve`** (surging 10x–25x above historical baselines), **`showcasing`**, **`underscores`**, **`pivotal`**, **`intricate`**, **`realm`**, **`tapestry`**, **`meticulous`**, **`nuanced`**, **`comprehensive`**, and **`notably`**.
- **Liang et al. (Stanford, ICLR/NeurIPS corpus study)** measured peer-review adjective/verb drift and found **`meticulous`** (+34.7x), **`intricate`** (+11.2x), **`commendable`** (+9.8x), **`innovative`**, **`versatile`**, **`noteworthy`**, and **`garner`** dominating AI-modified prose.

Because human readers now encounter these exact words dozens of times a day in unedited chat outputs, even two or three of them in proximity trigger immediate reader distrust.

### 3.2 Tier-1 Blacklist — Kill on Sight

Unless inside a direct quotation or an explicit domain term (e.g., *"network topology"*, *"loss landscape"* in optimization papers where standard—and even there, *"loss surface"* is cleaner), **replace Tier-1 words unconditionally**. Never swap a Tier-1 word for another Tier-1/Tier-2 synonym; replace it with the specific mechanism or plain English.

#### Tier-1 Verbs

| Banned AI Verb | What the Text Actually Means | Concrete Human Replacements |
|----------------|------------------------------|-----------------------------|
| **delve (into)** | examine, inspect, test, explain | *examine, analyze, trace, test, measure, look at, break down* (or cut *"delve into X"* and state X) |
| **underscore** | prove, show, emphasize, expose | *show, confirm, expose, make clear, point to* |
| **leverage** (non-finance) | use | *use, apply, rely on, reuse, call* |
| **spearhead** | lead, start, build | *lead, run, start, build, direct* |
| **embark (on)** | begin, start, launch | *start, begin, launch, switch to* |
| **navigate** (figurative) | handle, solve, work around | *handle, resolve, work through, manage, trade off* |
| **harness / unleash / unlock** | use, capture, enable | *use, capture, enable, open up, speed up* |
| **bolster** | strengthen, support, confirm | *strengthen, back up, support, raise, improve* |
| **garner** | get, earn, attract, collect | *get, earn, draw, collect, win* |
| **elevate** (figurative) | improve, raise | *improve, raise, upgrade, sharpen* |
| **revolutionize / transform** | change, replace, speed up | *replace, cut [metric] by X%, automate, change how [actor] does [task]* |
| **transcend** | go beyond, cross, outlast | *exceed, cross, outlast, work across* |
| **illuminate / elucidate** | explain, clarify, show | *explain, clarify, show, reveal* |
| **resonate (with)** | appeal to, match, convince | *convince, match, matter to, fit* |
| **unpack** (meta-discourse) | explain, separate, analyze | *explain, separate, trace, examine* |

#### Tier-1 Nouns & Figurative Metaphors

| Banned AI Noun | Why It Fails | Concrete Human Replacements |
|----------------|--------------|-----------------------------|
| **tapestry / mosaic / symphony** | Flowery decorative metaphor for "a mix of things" | *mix, set, combination, network, collection* (better: name the actual components) |
| **testament (to)** | Cliché significance inflation (*"serves as a testament to"*) | Delete wrapper; state cause and effect (*"The 99.98% uptime came from..."*) |
| **realm** | Pompous Medievalism for "field" or "area" | *field, area, domain, scope, layer* |
| **landscape** (abstract) | Overused dead metaphor (*"today's AI landscape"*) | *market, field, ecosystem (sparingly), toolset, current tools, industry* |
| **beacon** | Melodramatic puffery (*"a beacon of innovation"*) | Delete metaphor; state specific influence or benchmark rank |
| **interplay** | Vague hand-wave at how two things interact | *interaction, coupling, trade-off, feedback loop between A and B* |
| **catalyst** (figurative cliché) | Overused trigger metaphor | *trigger, cause, driver, what prompted X* |
| **cornerstone / bedrock / linchpin** | Architectural inflation for "main part" | *foundation, core requirement, main dependency, basis* |
| **paradigm / paradigm shift** | Burned-out buzzword for any change | *model, approach, design, shift from A to B* |
| **myriad / plethora** | Pseudo-literary inflation for "many" | *many, dozens of, [exact count]* |
| **double-edged sword** | Cliché binary framing | State the exact upside and exact cost side by side |
| **game-changer** | Pure marketing hype | Delete; state what previously impossible task now works |

#### Tier-1 Adjectives & Adverbs

| Banned AI Modifier | Why It Fails | Concrete Human Replacements |
|--------------------|--------------|-----------------------------|
| **multifaceted** | Vague way to say "has several parts" | Name the 2–4 distinct parts, or use *complex* |
| **indelible** | Almost always paired with *"mark"* or *"impact"* | Delete; state what persisted over time |
| **burgeoning** | Journalistic cliché for "growing" | *growing, expanding, fast-growing, new* (+ growth figure if known) |
| **poised (to)** | Speculative hype (*"poised to disrupt"*) | State current capability or concrete roadmap; drop predictions |
| **paramount** | Pompous intensifier (*"of paramount importance"*) | *essential, required, top-priority*, or state what breaks without it |
| **unparalleled / unmatched** | Unverified superlative puffery | *fastest tested, highest in Table 2*, or cut |
| **groundbreaking** (figurative) | Self-congratulatory hype | State what is first or new (*"the first lock-free implementation of..."*) |
| **nestled** | Travel-brochure tic (*"nestled in the valley"*) | *in, between, at the base of, three miles north of* |
| **seamlessly** | Magic-wand adverb hiding integration mechanics | Explain *how* the handoff works (*"without a restart"*, *"in one click"*, *"via shared memory"*) |
| **meticulously / tirelessly** | Flattering filler adverbs | Delete adverb; show the rigor via sample size, checks, or method |

#### Tier-1 Stock Phrases

- *"In today's fast-paced / ever-evolving / digital world..."* → **Delete entire clause.**
- *"It is worth noting that..." / "It is important to note that..." / "It bears mentioning that..."* → **Delete prefix; keep the main clause.**
- *"At the end of the day..." / "When all is said and done..."* → **Delete.**
- *"Paving the way for..." / "Shaping the future of..."* → **State the concrete downstream use.**
- *"A testament to..." / "Stands at the intersection of X and Y"* → **State what combines X and Y.**

### 3.3 Tier-2 Density Watchlist — Kill in Clusters

A human writer may naturally use **one** Tier-2 word occasionally. An LLM packs **three to seven** of them into a single 120-word block. **Rule:** If a paragraph contains 2+ Tier-2 words (or 1 Tier-2 word alongside any structural tell), replace them.

| Tier-2 Word | Cluster Symptom | Plain Replacement |
|-------------|-----------------|-------------------|
| **pivotal / crucial** | Every design choice is *"crucial"* or *"pivotal"* | *key, central, necessary, main*—or show what fails if omitted |
| **foster / cultivate** | *"fostering collaboration / innovation"* | *encourage, fund, build, train, reward* |
| **showcase / exhibit** | *"Table 3 showcases our model's..."* | *show, report, plot, list, demonstrate* |
| **utilize** | Used everywhere `use` fits | **Always replace with `use`** (save *utilize* only for thermodynamic/resource utilization rates) |
| **facilitate** | *"facilitate communication between..."* | *help, let, allow, route, connect* |
| **nuanced** | Self-praise (*"a nuanced understanding"*) | State the actual distinction or edge case instead of calling it nuanced |
| **holistic / overarching / comprehensive** | Padding before *approach, framework, view* | Delete modifier, or specify coverage (*"covers ingestion, indexing, and search"*) |
| **vibrant / dynamic** | Empty energy adjectives | Describe actual activity, frequency, or variety |
| **intricate / meticulous / commendable** | Classic Liang et al. LLM review/abstract spikes | *detailed, careful, thorough, solid*—or name the exact detail |
| **robust** | Slapped onto every pipeline/system outside formal stats | Outside *robust statistics / adversarial robustness*, specify *fault-tolerant, retry-safe, stable under X* |
| **streamline / optimize** (vague) | Used without saying what was cut or sped up | *cut two approval steps, shrink latency by 40 ms, simplify* |
| **moreover / furthermore / additionally / consequently** | Paragraph-initial transition conveyor belt | Cut 80% of formal conjunctive adverbs; let logical sequence carry transitions, or use *Also, Still, Yet, So* sparingly |
| **notably / importantly / crucially / significantly** | Sentence-initial emphasis crutches (*"Significantly"* outside $p$-values) | Delete sentence-initial booster; reserve *statistically significant ($p < 0.01$)* for actual tests |
| **aligns with / resonates with** | Corporate agreement speak | *matches, agrees with, follows, confirms* |

### 3.4 Tier-3 Safe Everyday Words — Do NOT Over-Purge

Do not turn prose into awkward caveman English by banning ordinary vocabulary. Words like **`key`**, **`important`**, **`main`**, **`clear`**, **`useful`**, **`hard`**, **`fast`**, **`because`**, **`but`**, **`however`** (used once, preferably mid-sentence rather than every paragraph start), **`for example`**, and **`show`** are clean, invisible English. Keep them when they carry real meaning.

### 3.5 Unslop Rules: Killing Abstract Tech Metaphors & Zombie Nouns

Even without *delve* or *tapestry*, technical and business AI drafts drown in **abstract nominalizations** ("zombie nouns," Helen Sword) and **VC/architecture buzz-nouns**:

1. **Purge abstract metaphor nouns:** Replace *substrate, wedge, vector (non-math), modality (when you just mean format/channel), bedrock, surface area (figurative), flywheel, north star, scaffolding (figurative), connective tissue* with the literal component (*database, entry product, input format, API endpoints, feedback loop, goal, glue code*).
2. **Mechanism over vibe:** Never write *"SQL you can actually read"* or *"blazingly fast developer ergonomics."* Show the `.toSQL()` output or state *"compiles 40k lines in 180 ms."*
3. **De-nominalize zombie nouns (Orwell + Williams):** Whenever a verb has been embalmed in `-tion`, `-ment`, `-ance`, `-ity`, or `-ing` and paired with a weak verb (*conduct, perform, achieve, occur, facilitate, provide*), resurrect the verb and put the real actor in the subject slot:
   - ❌ *"The **implementation** of batching **resulted in a reduction** of memory overhead."*
   - ✅ *"Batching **cut** memory overhead by 38%."*
   - ❌ *"We **conducted an investigation** into the **occurrence** of tail-latency spikes."*
   - ✅ *"We **traced** why tail latency spiked."*
4. **Kill `adverb + weak verb` pairs:** Replace *"significantly improves"*, *"dramatically reduces"*, *"greatly enhances"*, *"effectively mitigates"* with either a stronger single verb or the exact measured delta (*"halves"*, *"cuts tail latency from 140 ms to 22 ms"*, *"blocks"*).

---

## 4. The Direct-Statement Law — Hard Ban on Negative Parallelisms (`L3`)

### 4.1 The Core Mandate

> **Say what a thing IS, not what it is NOT.**

Negative parallelism (*antithesis by negation*) is the single loudest structural tic of modern RLHF-tuned models. Asked to explain a database, a poem, or a policy, an LLM reflexively invents a strawman misconception, negates it, and pivots dramatically to its real claim: *"X isn't just a cache—it's a distributed coordination engine."* Used once in a speech by John F. Kennedy, antithesis is memorable; used three times per page by an LLM, it reads like a manipulative copywriter who thinks every sentence is a movie trailer.

**Rule:** Delete the negated strawman half (`not X`). State the affirmative claim (`Y`) directly. If both `X` and `Y` are genuinely true facts that the reader needs, state both affirmatively without the fake dramatic reveal.

### 4.2 Complete 10-Pattern Negation-Pivot Ban Table

| # | Banned Formula | Example Slop | Surgical Affirmative Rewrite |
|---|----------------|--------------|------------------------------|
| 1 | **`not X, but Y`** | *It's not a tool, but a platform.* / *The bottleneck is not compute, but memory bandwidth.* | *It's a platform that hosts and manages your models.* / *Memory bandwidth is the bottleneck.* |
| 2 | **`not just X, it's Y`** (or `;` / `—`) | *It's not just a linter—it's an architectural guardrail.* | *The linter enforces module-boundary rules at build time.* |
| 3 | **`not only X, but (also) Y`** | *Quantization not only shrinks weights, but also speeds up decoding.* | *Quantization shrinks weights by 4x and speeds up decoding by 1.7x.* |
| 4 | **`rather than X, Y`** (rhetorical) | *Rather than relying on heuristics, our scheduler solves an ILP.* | *Our scheduler solves an integer linear program at each epoch.* |
| 5 | **`This isn't about X, it's about Y`** | *This migration isn't about cost; it's about operational ownership.* | *We migrated so product teams could deploy without filing infra tickets.* |
| 6 | **`It's not X. It's Y.`** (2-sentence split) | *That wasn't a network blip. It was a split-brain failover bug.* | *A split-brain failover bug caused the outage.* |
| 7 | **`X, not Y`** (trailing negation) | *Write tests for behavior, not implementation details.* | *Test observable outputs and public contracts so internal refactors stay green.* |
| 8 | **`less about X and more about Y`** | *Success here is less about model size and more about data hygiene.* | *Data deduplication moves accuracy more than doubling parameter count.* |
| 9 | **`not merely / simply X; rather, Y`** | *Attention is not merely a weighting scheme; rather, it routes values.* | *Attention routes token values across positions via learned query-key scores.* |
| 10 | **`Stop thinking of X as A. Start seeing it as B.`** | *Stop viewing logs as exhaust. Start treating them as an event stream.* | *Treat structured logs as a queryable event stream.* |

**Bilingual / Mixed-Text Note:** When editing bilingual English-Chinese drafts or English translated from Chinese AI prose, apply the exact same ban to calques of `不是…而是…`, `并非…而是…`, `与其说…不如说…`, `不仅仅是…更是…`, and `不在于…而在于…`.

### 4.3 Strict Exemptions (Rare — Maximum One per Piece)

Negation is permitted **only** in three narrow cases:
1. **Direct verbatim quotation** from a source, interviewee, or cited paper.
2. **Hard technical/legal scope boundary** where excluding a specific misinterpretation is the entire factual payload—and even then, prefer an affirmative semicolon split when cleaner:
   - *Acceptable:* `"Rate limits apply per API key, not per organization."`
   - *Even cleaner affirmative form:* `"Rate limits apply per API key; organization-wide pooling does not apply."`
3. **Naturalistic spoken dialogue** in fiction or transcripts.

### 4.4 Mandatory Self-Check Grep Patterns

Before delivering any `:english` rewrite, scan your draft against these patterns (mentally or via regex search on files). Any hit outside the three rare exemptions above must be rewritten:

```regex
(?i)\bnot\s+(only|just|merely|simply)\b
(?i)\bnot\s+[^.!?\n]{1,60},\s*but\b
(?i)\brather\s+than\b
(?i)\b(isn't|is\s+not|wasn't|was\s+not|aren't|are\s+not)\s+about\b
(?i)\bless\s+about\b.*\bmore\s+about\b
(?i)\b(it's|it\s+is|this\s+is|that's)\s+not\b[^.!?\n]*[.!?]\s*(it's|it\s+is|this\s+is|that's)\b
```

---

## 5. Deep Syntactic & Punctuation Surgery

Even after stripping every Tier-1 buzzword, unedited LLM prose betrays itself through six recurring syntactic and typographic tics. Fix them structurally rather than playing synonym whack-a-mole.

### 5.1 Participial Tail Clauses (`C3`: `, highlighting...`)

**The Tell:** A factually complete main clause followed by a comma and a present-participial phrase (`-ing`) that tells the reader how impressed to feel:
- *"...cutting P99 latency to 14 ms, **highlighting the effectiveness of our lock-free ring buffer**."*
- *"...adopted by 14 municipal agencies, **underscoring its growing relevance in public-sector modernization**."*
- *"...validates inputs at the edge, **ensuring seamless reliability and fostering developer confidence**."*
- *"...merges token spans dynamically, **paving the way for more scalable sequence modeling**."*

**Why It Sounds Fake:** Two grammatical sins collide here:
1. **False agency:** An inanimate event or whole clause is made the implicit subject of a human rhetorical verb (*highlight, underscore, showcase, reflect, foster*). Facts do not "underscore" things; authors argue things.
2. **Zero-information caboose:** If cutting P99 latency to 14 ms already proves the ring buffer works, appending *", highlighting the effectiveness of our ring buffer"* insults the reader's intelligence.

**Three-Way Surgical Fix:**
1. **The Hard Cut (Default — works 75% of the time):** Put a period right before the comma and delete the entire `-ing` tail.
   - ✅ *"The lock-free ring buffer cut P99 latency from 89 ms to 14 ms."*
2. **Promote to an Independent Evidence Sentence:** If the tail hints at a genuinely distinct downstream consequence, turn it into a second sentence with concrete numbers, actors, or citations.
   - ❌ *"...adopted by 14 municipal agencies, underscoring its growing relevance in public-sector modernization."*
   - ✅ *"Fourteen municipal agencies adopted the schema in 2025. Three state procurement boards now require it for vendor bids."*
3. **Convert `ensuring` into a Literal Causal/Failure Statement:** LLMs abuse `, ensuring X` to promise magic guarantees. State the exact invariant instead.
   - ❌ *"The gateway validates JWT signatures at ingress, ensuring end-to-end security."*
   - ✅ *"The gateway rejects requests with expired or invalid JWT signatures before they reach upstream services."*

### 5.2 Copula Avoidance (`L2`: `serves as`, `stands as`, `boasts`)

**The Tell:** LLMs treat `is`, `are`, `was`, `were`, `has`, and `have` as "boring" and systematically swap them out for pompous linking substitutes or real-estate verbs:
- *serves as / stands as / functions as / acts as* → almost always just **`is`**
- *boasts / features / sports / comes equipped with* → almost always just **`has`** or **`includes`**
- *represents a / marks a / constitutes a* → **`is a`** or state the direct verb

| ❌ AI Copula-Avoidance Slop | ✅ Clean Human Directness |
|-----------------------------|---------------------------|
| *SQLite **serves as** the local metadata store and **boasts** zero external dependencies.* | *SQLite **stores** local metadata and **has** zero external dependencies.* (or *SQLite **is** the local metadata store...*) |
| *The 1924 strike **stands as** a turning point in maritime labor law.* | *The 1924 strike **changed** maritime labor law.* / *The 1924 strike **was** a turning point in maritime labor law.* |
| *The cluster **features** 64 H100 GPUs connected via NVLink.* | *The cluster **has** 64 H100 GPUs on NVLink.* |

**Exception:** Keep *functions as* or *acts as* only when describing an improvised or secondary role (*"During network partitions, the read replica acts as a temporary leader"*—because it is *not* permanently the leader).

### 5.3 Rule-of-Three Tricolons (`L4`)

**The Tell:** Every list of adjectives, verbs, nouns, or clauses arrives in neat, rhythmic triplets:
- **Adjective triads:** *fast, reliable, and scalable; clear, concise, and actionable; robust, flexible, and intuitive*
- **Verb triads:** *ingest, transform, and visualize; analyze, optimize, and deploy*
- **Abstract noun triads:** *efficiency, transparency, and accountability; speed, quality, and cost*
- **Clause triads:** *whether you are a solo founder, a growing startup, or a Fortune 500 enterprise...*

**Why It Betrays AI:** One tricolon in an essay feels classical; four tricolons on one page reveal statistical beam-search symmetry. Worse, the third item in an AI triad is almost always semantic padding (*"clear, concise, and actionable"* where *clear* already implies *concise*).

**Surgical Fixes:**
- **Cut to 1 specific claim:** Replace *"fast, reliable, and scalable"* with the one dimension you actually measured (*"handles 40k writes/sec with zero dropped acks"*).
- **Use 2 asymmetric items:** Pairs feel grounded and uncontrived (*"cheap to run and easy to grep"*).
- **Use 4+ items when enumerating a real spec:** Complete domain enumerations (*"supports `int8`, `fp8`, `bf16`, and `fp32` tensors"*) read as engineering fact rather than rhetorical performance.

### 5.4 False Ranges (`L6`: `from X to Y`)

**The Tell:** Using `from X to Y` (or `ranging from X to Y`) when `X` and `Y` do not lie at opposite ends of any coherent, ordered spectrum:
- ❌ *"The outage disrupted everything **from checkout latency to quarterly board slides**."* (What sits halfway between checkout latency and board slides?)
- ❌ *"Contributors come **from compiler engineers to computational biologists**."* (Professions are unordered categories, not a number line.)
- ❌ *"Our platform handles workflows **ranging from data ingestion to compliance auditing**."*

**The Ordered-Scale Test:** Before keeping `from X to Y`, ask: *Can I name a natural midpoint `M` on the same single axis between `X` and `Y`?*
- **Pass (True range):** *"from 8-bit microcontrollers to 64-socket servers"* (compute scale); *"from 1998 to 2014"* (time); *"from Lisbon to Vladivostok"* (geography); *"from L1 cache to cold object storage"* (memory hierarchy).
- **Fail (False range):** Drop `from... to...` and name the actual list or shared property:
  - ✅ *"The outage slowed checkout and delayed the numbers needed for Tuesday's board deck."*
  - ✅ *"Compiler engineers, database maintainers, and computational biologists contribute to the repo."*

### 5.5 Em-Dash & En-Dash Discipline (`L7`: Zero-Dash Prose Rule)

**The Tell:** Modern LLMs scatter `—` (em dashes), spaced ` – ` (en dashes), or `--` across every third sentence:
- As mid-sentence parenthetical interruptions (*"The scheduler—which we rewrote in Rust last spring—cut tail latency..."*)
- As dramatic end-of-sentence reveals (*"...leaving only one viable option—starting over."*)
- As lazy appositive splices where a comma, colon, or period belongs.

**Hard Rule:** Deliver **zero** `—`, spaced `–`, or `--` in final prose unless the user provided a personal writing sample that deliberately uses em dashes.

**The 5-Way Punctuation Replacement Decision Tree:**

| How the AI Used `—` | Replace With | Example Transformation |
|---------------------|--------------|------------------------|
| Splicing two complete independent clauses | **Period (`.`)** or **Semicolon (`;`)** | ❌ *The cache warmed in four seconds—traffic immediately stabilized.*<br>✅ *The cache warmed in four seconds. Traffic stabilized right away.* |
| Introducing an explanation, list, or punchline | **Colon (`:`)** | ❌ *Only one check failed—certificate revocation.*<br>✅ *Only one check failed: certificate revocation.* |
| Tacking on a low-priority aside | **Parentheses (`(...)`)** or **Delete** | ❌ *Three nodes—all in `us-east-1b`—dropped off the ring.*<br>✅ *Three nodes (all in `us-east-1b`) dropped off the ring.* |
| Light non-restrictive appositive | **Commas (`, ... ,`)** | ❌ *Dwarf, our debug format—originally designed for C—encodes line tables.*<br>✅ *DWARF, originally designed for C, encodes source-line tables.* |
| Double interruption inside an already long sentence | **Split & Restructure** | ❌ *When a worker crashes—which happens roughly twice a week under spot pricing—the coordinator reassigns its shard.*<br>✅ *Spot preemptions kill a worker roughly twice a week. Whenever one dies, the coordinator reassigns its shard.* |

**Protected Non-Prose Tokens (Do NOT Corrupt):**
- Code blocks, inline code, CLI flags (`--max-time 5`, `-O3`), SQL comments (`--`), YAML frontmatter (`---`), Markdown table dividers (`|---|`), URLs, and file paths.
- Mathematical minus signs (`$a - b$`, `-40 °C`) and standard ASCII hyphens in compound pre-modifiers (`lock-free`, `UTF-8`, `pages 12-18` using ASCII `-` if `–` is banned in plain-text pipelines).

### 5.6 Elegant Variation (`L5`), Subjectless Passives (`L11`) & Formatting Hygiene (`L8–L10`, `L12`)

- **Kill Synonym Cycling (`L5`):** Never call a `token` a *lexical unit* in sentence 2 and an *input symbol* in sentence 3 just to avoid repeating *token*. In technical, legal, and analytical English, **same concept = same word**. Repetition of domain nouns creates precision; synonym cycling creates bugs in the reader's mental model.
- **Restore Actors to Subjectless Passives (`L11`):** AI docs love eerie ghost-agency: *"Migrations are applied automatically. Invalid rows are quarantined."* Always answer *Who or what component does this, and when?* → *"On startup, `migrator` applies pending SQL files and moves malformed rows to `quarantine_events`."*
- **Formatting Slop Cleanup (`L8–L10`, `L12`):**
  - Strip decorative emojis (`✨`, `🚀`, `💡`, `🔍`, `✅` in prose essays).
  - Unpack "**Bold Header:** Echo sentence" bullet lists into real paragraphs whenever items have causal or narrative flow; keep bullet lists only for genuine checklists, parameters, or discrete options.
  - Convert `### Every Word Capitalized Like An Ad` (`L9`) to `### Sentence case headings`.
  - Use straight ASCII quotes `"` and `'` (`L10`).
  - Fix predicate hyphenation (`L12`): write *"a well-tested parser"*, *"the parser is well tested"* (no hyphen after the noun).

---

## 6. Macro-Structure Surgery — Throat-Clearing Intros & Moralizing Outros

If you read an AI-generated article and cross out the first paragraph and the last paragraph, the remaining middle almost always improves instantly.

### 6.1 Six Throat-Clearing Opener Archetypes (`F4`, `F9`) — Cut on Sight

| Archetype | Typical Slop Opening | Surgical Fix |
|-----------|----------------------|--------------|
| **1. Cosmic / Historical Zoom-Out** | *"Since the dawn of distributed computing, engineers have grappled with state synchronization..."* | Start in the present at the exact failure boundary: *"Two replicas receiving concurrent writes must pick a winner."* |
| **2. "Today's Landscape" Wallpaper** | *"In today's rapidly evolving AI landscape, inference efficiency has become more critical than ever."* | Delete sentence 1 completely. Start with sentence 2 or the concrete bottleneck (*"KV-cache memory outgrows model weights past 32k context."*). |
| **3. Empty Topical Frame** | *"When it comes to database indexing, few topics generate as much debate as B-trees versus LSM-trees."* | State the actual trade-off directly: *"B-trees win on point reads; LSM-trees win on sustained random writes."* |
| **4. Fake Rhetorical Question** | *"Have you ever wondered why your Docker builds take twelve minutes? You're not alone."* | State the cause: *"Docker rebuilds every layer after `COPY . .` whenever a single README typo invalidates the cache."* |
| **5. Meta-Signposting Announcement** | *"In this comprehensive guide, we will delve into three core strategies for reducing churn."* | Drop the table-of-contents narration; open with the strongest finding or problem. |
| **6. Simulated Intimacy (`F9`)** | *"Honestly? Look. Here's the uncomfortable truth nobody in DevOps talks about:"* | Delete the theatrical drumroll and state the uncomfortable claim cold. |

> **The Sentence-Three Rule:** In 80% of LLM drafts, the real first sentence is sitting at Sentence 3 or Paragraph 2. Delete everything above it and adjust pronouns.

### 6.2 Five Moralizing & Summary-Bow Outro Archetypes (`F3`, `F8`) — Hard Stop Rule

LLMs suffer from compulsive closure: they cannot end an explanation without stepping onto a podium to summarize what you just read and wish humanity well.

| Archetype | Typical Slop Ending | Surgical Fix |
|-----------|---------------------|--------------|
| **1. High-School Summary Recap** | *"In conclusion, by combining caching, batching, and async I/O, teams can build resilient systems..."* | Delete the recap paragraph if the piece is under 1,500 words; readers remember what they read two minutes ago. |
| **2. Golden-Mean Fence-Sitting** | *"Ultimately, there is no silver bullet; the key is striking the right balance for your unique needs."* | Name the concrete decision rule (*"Pick Postgres until write throughput exceeds 30k TPS on a single primary; shard after."*). |
| **3. Horizon / Future Cheerleading** | *"As hardware continues to evolve, the future of local inference looks brighter than ever."* | Delete completely. Stop on the last measured fact. |
| **4. Prescriptive Corporate Sermon** | *"Organizations that embrace this shift today will unlock lasting competitive advantage tomorrow."* | Delete completely. |
| **5. Fortune-Cookie Epigram (`F8`)** | *"Because at the end of the day, observability isn't about dashboards. It's about peace of mind."* | Delete completely, or end on a concrete operational detail (*"The alert hasn't paged anyone at 3 a.m. since October."*). |

> **The Hard-Stop Rule:** End on a concrete number, a specific unresolved edge case, a crisp decision threshold, or a dry observation—then stop typing.

---

## 7. Sentence-Length Burstiness, Rhythm Craft & Adding Soul

### 7.1 Why Clean Grammar Still Sounds Like a Bot

Suppose you remove *delve*, *tapestry*, em dashes, and negative parallelisms, yet every sentence in a paragraph has 19, 21, 18, 22, and 20 words, and every sentence opens with `Subject + Verb` or `Transition, Subject + Verb`. A human ear will still detect machine prose within five seconds.

Autoregressive decoding favors medium-length, medium-entropy clauses that hover safely around a **16–24 word mean** with uniform right-branching tree depth. Humans do not think or breathe at a constant metronome.

### 7.2 Engineering Burstiness (Gary Provost's Rhythm Law)

Gary Provost demonstrated the cure in *100 Ways to Improve Your Writing*: five uniform short sentences in a row drone like a stuck record, whereas mixing short punches, medium workhorses, and an occasional sustained long sentence creates natural cadence.

**Operational Burstiness Targets:**
1. **Never write 3+ consecutive sentences in the same length band** (within ±4 words of each other).
2. **Weave three distinct length bands across paragraphs:**
   - **Short punches (3–8 words):** Deliver verdicts, reversals, or blunt facts (*"It failed under load."* / *"That assumption held for six months."* / *"Memory stayed flat."*).
   - **Medium workhorses (12–22 words):** Carry standard causal steps, definitions, and transitions.
   - **Sustained builds (28–42 words):** Unpack a multi-part mechanism, trace a chain of failure from root trigger to customer symptom, or lay out a concrete comparison—provided every clause earns its keep and doesn't tangle syntax.
3. **Rotate grammatical sentence openings:** Never start three consecutive sentences with `The [noun] [verb]...` or `This [verb]...` or `[Conjunctive adverb], ...`. Mix:
   - Concrete actor + active verb (*"Postgres acquires a row lock..."*)
   - Short temporal/conditional anchor (*"Under 80% disk fill, compaction stalls."*)
   - Prepositional locus (*"Inside `parse_header()`, two bounds checks..."*)
   - Inverted or blunt short verdict (*"Neither fix worked."*)

### 7.3 Joseph Williams's Clarity & Flow Engine

Apply four structural principles from *Style: Lessons in Clarity and Grace* to make prose effortless to read:

1. **Characters as Grammatical Subjects:** Put real people, specific systems, or concrete components (`the client`, `reviewers`, `Linux's CFS scheduler`, `our first prototype`) in the subject slot—not abstractions (`the utilization of`, `resource contention dynamics`).
2. **Actions as Verbs:** Put what those characters *do* (`rejects`, `stalls`, `splits`, `overwrote`, `measured`) in the main verb slot.
3. **Old Information Before New Information (Cohesion):** Start sentences with concepts the reader already met in the previous sentence ("topic"), and place the unfamiliar, complex, or surprising payload at the end ("stress"). AI often dumps a brand-new 10-word noun phrase at the start of a sentence and ends weakly with *"...is important."*
4. **End-Focus (Climactic Weight):** The last three to five words of a sentence hit the ear hardest. Never waste the end of a sentence on filler (*"...in many different scenarios"*, *"...to a certain extent"*, *"...as mentioned previously"*). End on the sharpest noun, verb, or number.

### 7.4 Adding Soul (When Register Permits)

Sterile, scrubbed prose can feel just as lifeless as raw AI slop. When editing essays, blogs, opinion pieces, memos, or newsletters (**not** encyclopedias, contracts, safety specs, or formal proofs):

- **Have an actual take:** React to facts instead of neutrally cataloging both sides forever. Say what surprised you, what annoyed you, or which trade-off you would pick.
- **Replace evaluative labels with sensory/concrete detail:** Instead of calling a legacy codebase *"concerning and difficult to maintain,"* write *"Touching `billing.py` meant scrolling past 4,200 lines of nested `if` blocks written for a tax law that expired in 2019."*
- **Allow human texture:** Keep parenthetical asides, honest uncertainty (*"I still don't know why the third run converged"*), self-corrections, dry understatement, and unresolved tension. Real thinkers leave hard problems messy when they are messy.

### 7.5 Rescuing ESL / Non-Native Drafts from the "Polish My English" Trap

Non-native English researchers and engineers frequently feed a clear, fact-rich rough draft to an LLM with the prompt *"Polish my English to sound native and academic."* Standard LLMs interpret *"native and academic"* as *"maximum Tier-1 GPTese"*—injecting *delve*, *pivotal*, *multifaceted*, *underscores*, *not only... but also*, and participial `-ing` tails into every sentence.

**How to Polish ESL Drafts Properly (`:english` Preservation Mode):**
1. **Keep the author's original verbs and logic** if they are plain and accurate (*examine, test, reduce, compare, build*). Fix only genuine grammar errors: articles (`a/an/the`), prepositions (`in/on/at/for`), subject-verb agreement, tense consistency, and Chinglish/L1 calques (e.g., *"make an optimization to"* → *"optimize"*; *"have a good performance"* → *"perform well"* or state the metric; *"give a detailed introduction of"* → *"describe"* or *"introduce"*).
2. **Unpack L1 topic-comment run-ons** (*"For this hyperparameter, we tested five values, it shows little sensitivity"*) into clean English clause boundaries (*"We tested five values of $\lambda$; accuracy varied by less than 0.2%."*).
3. **Never inflate register upward** beyond the plainest prose accepted at top venues (e.g., Jeff Dean / Sanjay Ghemawat systems papers or Kaiming He vision papers, which use crystal-clear short words: *we use, we test, we observe, simple, fast, drops*).

---

## 8. Annotated Before/After Rewrite Masterclass

Study how multiple pattern fixes (`C1–C6`, `L1–L12`, `F1–F10`), direct statements, em-dash removal, and burstiness work together in full prose.

### Case 0: Canonical Quick Fixes (Core `english.md` Baseline)

**❌ Before:**
> Additionally, this pivotal initiative underscores our commitment to fostering innovation in today's evolving landscape—it's not just about technology, but about culture.

**✅ After:**
> The initiative funds two internal tools and a weekly demo slot. Team culture shapes how those tools get used; the budget line is explicit in Appendix B.

**Direct-statement fix:**
> It's not a tool, but a platform.
> → **It's a platform that hosts and manages your models.**

---

### Case 1: Executive / Product Initiative Memo (Baseline Expansion)

**❌ Before (76 words | Sentence lengths: 31, 24, 21 — flat cadence):**
> Additionally, in today's rapidly evolving AI landscape, this pivotal initiative serves as a testament to our commitment to fostering innovation—it's not just about deploying cutting-edge technology, but about cultivating a resilient, data-driven, and collaborative culture. By leveraging cross-functional synergies, teams can seamlessly navigate complex bottlenecks, ultimately unlocking transformative value across the entire organization. Moving forward, this holistic approach will pave the way for sustainable growth.

*Diagnosis:* `L1` (*Additionally, landscape, pivotal, testament, fostering, cutting-edge, leveraging, seamlessly, navigate, unlocking, transformative, holistic, pave the way*); `C1` (significance inflation); `L2` (*serves as*); `L3` (*not just about X, but about Y*); `L4` (tricolon *resilient, data-driven, and collaborative*); `L7` (em dash); `F3` (*Moving forward... sustainable growth*). Almost zero factual content survives stripping the fluff; where facts exist in surrounding context, anchor to them.

**✅ After (39 words | Sentence lengths: 11, 16, 12 — grounded & factual):**
> The initiative funds two internal prototyping tools and a Friday demo slot. Product and infra engineers share one backlog so teams can ship model updates without waiting on quarterly platform reviews. Full budget lines sit in Appendix B.

---

### Case 2: Open-Source Software README / Systems Architecture

**❌ Before (94 words | Sentence lengths: 29, 34, 31 — uniform drone):**
> When it comes to local vector search, developers often face a daunting choice between blazing speed and operational simplicity. `vec-lite` isn't merely another wrapper—it stands as a lightweight, battle-tested, and production-ready embedded engine that empowers applications to harness approximate nearest-neighbor search without external infrastructure. Rather than requiring a separate daemon, `vec-lite` seamlessly integrates into your host process via mmap, ensuring minimal memory overhead and highlighting the power of zero-copy serialization.

*Diagnosis:* `F4` (*When it comes to...*); `C4` (*daunting, blazing, battle-tested, empowers*); `L3` (*isn't merely X—it stands as Y*, *Rather than requiring X*); `L2` (*stands as*); `L4` (*lightweight, battle-tested, and production-ready*); `L7` (em dash); `L1` (*harness, seamlessly*); `C3` (*ensuring..., highlighting...*).

**✅ After (56 words | Sentence lengths: 14, 6, 23, 13 — bursty `[14, 6, 23, 13]`):**
> `vec-lite` embeds HNSW vector search directly inside your process as a single C library. No separate server runs. It memory-maps index files from disk with zero-copy reads, keeping resident RAM under 45 MB for one million 768-dimensional float16 vectors. Link `libveclite.a` and query an index in six lines of Go or Rust.

---

### Case 3: Computer Science / Empirical Research Paragraph

**❌ Before (103 words | Sentence lengths: 32, 36, 35 — wall of academic GPTese):**
> In this section, we delve into the intricate interplay between quantization granularity and speculative decoding acceptance rates, an area that has garnered significant attention in recent literature. Notably, our meticulous ablation studies showcase that channel-wise scaling not only preserves perplexity on long-context benchmarks, but also bolsters draft-token acceptance—underscoring its pivotal role in latency-sensitive deployments. Furthermore, these commendable findings align with theoretical bounds, paving the way for future explorations into ultra-low-bit inference realms.

*Diagnosis:* `F4` (*In this section, we...*); `L1` (*delve, intricate, interplay, garnered, Notably, meticulous, showcase, bolsters, pivotal, Furthermore, commendable, realms*); `C5` (*in recent literature* without citation); `L3` (*not only... but also*); `L7` (em dash); `C3` (*underscoring..., paving the way for...*).

**✅ After (64 words | Sentence lengths: 15, 29, 20 — crisp empirical style):**
> We next measure how quantization group size affects speculative decoding acceptance rates. Switching weights from per-tensor to 128-channel group scaling holds WikiText-2 perplexity within 0.08 of FP16 while raising draft-token acceptance from 61% to 78% on Llama-3-70B. That jump cuts end-to-end decoding latency by 1.42x on a single A100, matching the variance bound in Proposition 2.

---

### Case 4: Engineering Blog / Postmortem Essay (Adding Soul & Voice)

**❌ Before (91 words | Sentence lengths: 28, 32, 31):**
> In today's distributed microservices environment, retry logic is widely regarded as a vital mechanism for maintaining high availability. However, retries can act as a double-edged sword when downstream dependencies experience degradation. During Tuesday's incident, aggressive client retries amplified load on the primary database—transforming a minor network hiccup into a full-scale cascading outage, underscoring the critical importance of exponential backoff and jitter. Ultimately, resilience requires thoughtful engineering and continuous vigilance.

*Diagnosis:* `F4` (*In today's...*); `C5` (*widely regarded*); `L1` (*vital, double-edged sword, transforming, underscoring, Ultimately*); `L7` (em dash); `C3` (*underscoring...*); `F3` (moralizing sermon ending). Zero human voice despite describing a real outage.

**✅ After (78 words | Sentence lengths: 7, 25, 4, 30, 12 — high burstiness + honest voice):**
> Our own retry loop took us down. At 14:07 UTC on Tuesday, a 400 ms switch flap dropped 3% of packets between `checkout-api` and primary Postgres. That should have hurt nobody. Instead, 180 API pods fired three immediate retries with zero jitter, multiplying query volume by 4x until connection pools locked solid for nineteen minutes. We shipped capped exponential backoff with full jitter before dinner, and ripped unconditional retries out of every write path.

---

### Case 5: Encyclopedic / Biographical Entry (Wikipedia `WP:AISIGNS` Neutrality)

**❌ Before (86 words):**
> Nestled at the intersection of mathematics and textile design, Ada Rivera's groundbreaking career stands as an enduring testament to interdisciplinary creativity. From local community workshops in Oaxaca to prestigious galleries in Zurich, her vibrant woven sculptures have garnered international acclaim, featured in *The Guardian*, *Wired*, and *Artforum*. Despite facing early skepticism from traditional institutions, Rivera continues to push boundaries, leaving an indelible mark on contemporary fiber art.

*Diagnosis:* `C4` (*Nestled, groundbreaking, prestigious, vibrant*); `C1` (*enduring testament, push boundaries, indelible mark*); `L2` (*stands as*); `L6` (false/promotional range); `L1` (*garnered*); `C2` (uncontextualized media name-drop triad); `C6` (*Despite facing early skepticism... continues to*).

**✅ After (58 words | Strictly neutral, verifiable encyclopedic prose):**
> Ada Rivera (born 1978) is a Mexican weaver and mathematician whose sculptures model hyperbolic geometry in hand-dyed wool. She taught weaving cooperatives in Oaxaca from 2006 to 2012 before exhibiting her first non-Euclidean tapestries at Kunsthalle Zürich in 2015. Reviewing her 2021 retrospective, *Artforum* noted her method of encoding cellular automata rules directly into warp thread counts.

---

### Case 6: Curing Overcorrected "Anti-AI" LinkedIn Broetry (`F7`, `F8`, `F9`)

**❌ Before (61 words | 9 fragmented lines):**
> Honestly? Most engineers misunderstand technical debt.
>
> They think it's messy code.
>
> It's not.
>
> Technical debt isn't about bad syntax—it's about outdated assumptions frozen in logic.
>
> Speed isn't the enemy. Rigidity is.
>
> Read that again. Full stop.

*Diagnosis:* When told "don't sound like ChatGPT," LLMs frequently swing to the opposite ditch: `F9` (*Honestly?*), `L3` (*It's not. Technical debt isn't about X—it's about Y*, *Speed isn't the enemy. Rigidity is*), `L7` (em dash), `F8` (fake aphorism), `F7` (staccato broetry + *Read that again. Full stop.*).

**✅ After (49 words | 1 cohesive paragraph, concrete claim):**
> Messy functions rarely sink a codebase; wrong domain assumptions do. You can rename variables and split 300-line methods in an afternoon, whereas baking "one user belongs to one workspace" into forty database tables takes six months to unwind once enterprise customers ask for multi-org logins.

---

### Case 7: Diff-Anchored & Echo-Header Documentation (`F5`, `F6`, `L8`, `L11`)

**❌ Before:**
> ### Configuring Request Timeouts And Retry Policies
> This section explains how request timeouts and retry policies are configured in the SDK.
> - ⚡ **Timeout Configuration:** Timeout configuration was added in v2.4 to replace the legacy `socket_wait` parameter—requests are now terminated automatically if no headers arrive.
> - 🛡️ **Retry Policy:** No manual setup needed! Transient `503` responses are retried seamlessly under the hood.

*Diagnosis:* `L9` (Title Case heading); `F5` (echo sentence); `L8` (emojis + `**Label:**` echoed immediately); `F6` (diff-anchored *was added to replace...* in evergreen docs); `L7` (em dash); `L11` (subjectless passives *are terminated*, *No manual setup needed*); `L1` (*seamlessly*).

**✅ After:**
> ### Request timeouts and retries
>
> `Client` aborts any HTTP request whose response headers do not arrive within `read_timeout_ms` (default: `5000`). When an upstream server returns `502`, `503`, or `504` on an idempotent `GET` or `HEAD` call, `Client` retries up to twice with 200 ms base backoff. Pass `max_retries=0` to disable retries.

---

### Case 8: ESL Draft → Bad "AI Polish" → Clean Native English

- **Original ESL Author Draft:** *"For big graphs, the baseline GNN has out-of-memory problem on 24GB GPU because neighbor explosion. We sample top-8 neighbors by edge weight, it reduces memory 65% and accuracy almost not drop (only 0.3%)."*
- **❌ Bad "AI Polish" (Trading L2 errors for peak GPTese):** *"When dealing with large-scale graph topologies, conventional GNN architectures frequently encounter debilitating memory bottlenecks due to the multifaceted neighbor-explosion phenomenon. Rather than aggregating exhaustive neighborhoods, our framework leverages weight-prioritized top-8 sampling—dramatically slashing GPU memory consumption by 65% while seamlessly preserving model fidelity, underscoring its practical viability on consumer-grade hardware."*
- **✅ Proper `:english` Humanize Polish (Preserving the author's plain voice & exact numbers):** *"On large graphs, neighbor expansion pushes the baseline GNN past 24 GB of VRAM. Sampling only the eight highest-weight neighbors per node cuts peak memory by 65% while holding accuracy within 0.3% of full-neighborhood training."*

---

## 9. False Positives, Human Signals & Anti-Overcorrection Guardrails

Good editing removes synthetic noise without vandalizing clean prose or mutating facts.

### 9.1 False Positives — Do NOT Flag in Isolation

Never accuse or rewrite clean prose solely because of a single isolated feature:
- **Clean, standard grammar and spelling.** Competent human editors write grammatically sound sentences.
- **A single `however`, `therefore`, `crucial`, or `robust` (in statistical/control contexts)** surrounded by concrete, varied prose.
- **Curly quotes (`“ ”`) or an occasional em dash** in text pasted directly from macOS Pages, Microsoft Word, LaTeX (`---`), or Substack where the rest of the voice is unmistakably human—though during an active `:english` rewrite pass, still normalize dashes to zero unless matching a user sample.
- **Formal or Latinate domain terminology** that carries exact technical meaning (*idempotent, monotonic, heteroskedastic, amortized, orthogonal, fiduciary, jurisdiction*). Never dumb down real technical terms into imprecise slang.
- **Standard business/email salutations** (*"Thanks for sending the logs,"*, *"Best,"*).
- **Quoted AI output** inside an article that is explicitly analyzing or critiquing AI writing.

### 9.2 Human Signals — Preserve Untouched

When you encounter any of the following in a draft, **protect them**—they are the exact proof of human authorship that aggressive LLM rewrites accidentally sand off:
- **Hard-to-fabricate specifics:** exact commit hashes, street intersections, weird benchmark anomalies (*"seed 42 diverged at step 11,400"*), dollar amounts down to the cent, named Slack channels, dates of Tuesday outages.
- **Unresolved tension & honest uncertainty:** admitting two goals conflict without a neat resolution, or noting *"we never reproduced this outside staging."*
- **Idiosyncratic humor, dry asides, and era-specific vernacular** that fits the author's persona.
- **Deliberate, solitary sentence fragments** used once for dry comedic or rhythmic timing (distinct from 8-line LinkedIn broetry walls).
- **Verified pre-2022 archival passages, legal clauses, quotations, code blocks, CLI commands, and YAML frontmatter.**

### 9.3 Four Anti-Overcorrection Guardrails

1. **Zero Fact Fabrication:** Never invent metrics (*"cut latency by 43%"*), company names, dates, or anecdotes to make vague AI prose sound "specific." When an AI draft says *"significantly improved performance"* and the user provided no number, either ask for the number, write *"[insert measured delta]"* if drafting a template, or strip the adverb (*"sped up query execution"*) without inventing digits.
2. **Never Overcorrect into Caveman or Slangy Prose:** Removing *utilize* and *delve* does not mean inserting *"kinda"*, *"super cool"*, *"folks"*, or *"stuff"* into an academic paper or RFC. Plain English (`examine`, `measure`, `use`, `reduce`) is dignified in every register from *Nature* to kernel commit messages.
3. **Never Overcorrect into Broetry (`F7`):** Do not chop every paragraph into one-sentence lines or add *"Let that sink in."* Real paragraphs group 3–6 sentences around one cohesive thought.
4. **Respect Compression:** Humanized text is almost always **15%–40% shorter** than the AI draft it replaces. Never pad word count back up after cutting throat-clearing, negative parallelisms, and `-ing` tails.

---

## 10. Quick-Run Regex Audit & Pre-Flight Verification Checklist

Run these two checks before finalizing any `:english` output.

### 10.1 High-Signal Slop Grep Suite

```regex
# 1. Tier-1 AI Vocabulary (case-insensitive)
(?i)\b(delve[sd]?|delving|tapestry|testament|underscore[sd]?|underscoring|multifaceted|realm[s]?|interplay|beacon[s]?|spearhead(ed|ing)?|embark(ed|ing)?|burgeoning|poised|paramount|unparalleled|nestled|seamlessly|meticulously|tirelessly|myriad|plethora)\b

# 2. Negation-Pivot / Direct-Statement Violations (L3)
(?i)(\bnot\s+(only|just|merely|simply)\b|\bnot\s+[^.!?\n]{1,50},\s*but\b|\brather\s+than\b|\b(isn't|is\s+not|wasn't|was\s+not)\s+about\b|\bless\s+about\b.*\bmore\s+about\b)

# 3. Participial Significance Tails (C3)
,\s*(highlighting|underscoring|showcasing|fostering|ensuring|reflecting|paving\s+the\s+way|contributing\s+to)\b

# 4. Copula Avoidance (L2)
(?i)\b(serves\s+as|stands\s+as|functions\s+as|boasts|marks\s+a\s+pivotal)\b

# 5. Prose Em/En Dashes & Double Hyphens (L7 — run outside code blocks)
(—| – |\s--\s)

# 6. Throat-Clearing & Moralizing Wrappers (F1, F3, F4, M1)
(?i)(in\s+today's\s+[^,]{3,35}\s+(landscape|world|era)|it\s+is\s+(worth\s+noting|important\s+to\s+note)\s+that|let's\s+dive\s+in|here's\s+what\s+you\s+need\s+to\s+know|i\s+hope\s+this\s+helps|the\s+future\s+looks\s+bright|exciting\s+times\s+ahead|only\s+time\s+will\s+tell)
```

### 10.2 Final 8-Point Pre-Flight Checklist

- [ ] **Facts intact:** Zero invented numbers, names, dates, quotes, or citations; zero dropped constraints.
- [ ] **Direct statement clean:** Zero `not X, but Y` / `not just X, it's Y` / `rather than X` pivots (unless within the single-exemption factual boundary rule).
- [ ] **Zero prose dashes:** Zero `—`, prose `–`, or ` -- ` (unless matching an explicit user writing sample).
- [ ] **Lexicon clean:** Zero Tier-1 words; Tier-2 words isolated (never clustered 2+ per paragraph); `utilize` → `use`; zombie nominalizations converted to active verbs.
- [ ] **Tails & copulas fixed:** Zero `, highlighting / underscoring / fostering` tails; `serves as / stands as / boasts` restored to `is / has` or concrete verbs; mechanical rule-of-three triads and false `from X to Y` ranges broken.
- [ ] **Macro-edges trimmed:** Throat-clearing intro paragraph and moralizing/summary-bow outro deleted; piece starts with content and stops on its final concrete point.
- [ ] **Burstiness & openings:** No 3+ consecutive sentences of near-identical word count; mixed short (~5w), medium (~18w), and long (~35w) sentences; varied sentence starts; characters in subjects, actions in verbs.
- [ ] **Read-aloud pass:** Sounds like an informed human speaking or writing at natural speed for the target register, with straight quotes and sentence-case headings.

---

## 11. Embedded / Subagent Execution Prompt Template

When invoking `:english` inside an automated pipeline or embedded editing pass, apply this condensed operational contract alongside the full catalog above:

```text
Rewrite the English text so it reads like an attentive domain expert wrote it directly.
1. Preserve 100% of facts, numbers, dates, names, quotes, code blocks, CLI flags, and citations. Never invent metrics or examples.
2. Direct-statement law: zero negation-pivot framing ("not X, but Y", "not just X, it's Y", "not only... but also", "rather than X, Y", "isn't about X"). State what things ARE.
3. Zero prose em dashes (—), spaced en dashes (–), or double-hyphen dashes (--), unless matching a user-supplied writing sample. Use periods, commas, colons, parentheses, or separate sentences.
4. Purge Tier-1 AI vocabulary (delve, tapestry, testament, underscore, leverage, multifaceted, realm, interplay, beacon, spearhead, embark, burgeoning, poised, seamlessly, meticulously, paramount, landscape) and break clusters of Tier-2 words (pivotal, crucial, foster, showcase, holistic, nuanced, robust, moreover, furthermore). Always use "use" instead of "utilize".
5. Cut sentence-final participial significance tails (", highlighting...", ", underscoring...", ", ensuring...", ", fostering..."). Restore plain copulas (is/are/has) over "serves as / stands as / boasts", or use concrete action verbs with real actors in the subject slot.
6. Break mechanical rule-of-three triads and false "from X to Y" ranges. Cut throat-clearing opening warmups and moralizing/summary-bow endings; stop on the last concrete point.
7. Vary sentence length across every paragraph (~5-word punches, ~18-word workhorses, ~35-word sustained clauses; never 3+ uniform sentences in a row). Match register: keep specs/encyclopedic text dry and neutral; give essays/blogs real point of view without staccato LinkedIn broetry.
```
