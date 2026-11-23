<p align="center">
  <img src=".github/assets/banner.svg" alt="slopbuster — before and after AI text humanization" width="100%">
</p>

# slopbuster

Strips the AI tells out of prose, code, and academic writing.

I built this because every "humanizer" I found did the same thing: swap "delve" for "explore" and call it a day. That's find-and-replace with a marketing page.

152 patterns, built from analyzing 1,000+ AI vs human samples and peer-reviewed LLM detection research. Two passes — because removing AI patterns without adding voice produces sterile text that's equally detectable, just by a different classifier.

---

## What it does

A real run. The "before" is AI-generated marketing copy written for this demo; the "after" is slopbuster's actual output, scored with the tool's own three-tier system.

**Before — 0/10** (49 pattern points across 230 words = 213 per 1,000):

> In today's rapidly evolving e-commerce landscape, sustainable packaging has emerged as a pivotal consideration for brands seeking to remain competitive. As consumer expectations continue to shift, it's important to note that packaging **serves as** far more than a protective layer — it **represents** a brand's values, its commitment to the planet, and its understanding of the modern shopper.
>
> Let's **delve** into why this matters. Industry **experts argue** that the environmental footprint of fulfillment operations **underscores the importance** of rethinking materials from the ground up […]
>
> Ultimately, sustainable packaging isn't just a trend — it's a **testament** to where the industry is heading. Brands that embrace this shift today will be **well-positioned to thrive in the years to come**.

**After — 8.5/10** (zero Tier 1, 2, or 3 hits):

> Packaging is the first physical thing your customer touches. That's the whole argument, and most sustainability decks bury it somewhere around slide forty.
>
> Fulfillment waste has gotten expensive enough that materials are worth rethinking — not because it photographs well for the annual report, but because shipping air costs money. Consumers do say they prefer brands with credible environmental practices. They also keep buying the cheap thing. Take the survey data with salt.
>
> The obstacles are the boring ones. Compostable mailers cost more per unit. Suppliers with real certification are scarce and get booked out. A material that works fine for apparel will not survive a pallet of ceramics.
>
> Start with the SKUs you ship most. You will learn more from re-boxing your top ten products than from a year of vendor presentations.

| Measured | Before | After |
|---|---|---|
| Tier 1 hits (3 pts) | 7 | 0 |
| Tier 2 hits (2 pts) | 8 | 0 |
| Tier 3 hits (1 pt) | 12 | 0 |
| Words | 230 | 173 |

**One honest caveat:** sentence-length variance — one of the three readability
metrics — did *not* discriminate here. The slop sample scored 0.59 CV, well
inside the "good" band, while being obviously machine-written. Pattern
detection did all the work. Reproduce it yourself with `--score-only`.

---

## Install

```bash
npx skills add gabelul/slopbuster
```

One command. Auto-detects your agent, symlinks the skill. Update later with `npx skills update`.

<details>
<summary>Manual install</summary>

```bash
# Claude Code
cp -r slopbuster ~/.claude/skills/

# Codex CLI
cp -r slopbuster ~/.codex/skills/

# Any other agent — copy into your agent's skill directory
cp -r slopbuster /path/to/agent/skills/
```
</details>

## Usage

```bash
/slopbuster blog-post.md                              # auto-detect mode, standard depth
/slopbuster src/ --mode code                           # scan source files for AI patterns
/slopbuster paper.md --mode academic --field biomedical # academic with section awareness
/slopbuster doc.md --depth deep --voice-sample me.md   # calibrate to a specific voice
/slopbuster draft.md --score-only                       # just score, don't rewrite
```

**No API key, no second bill, nothing to install.** slopbuster is pure markdown
— a rule set your agent reads and applies, running on the model you're already
paying for. There's no separate service to sign up for and no runtime.

Want your agent to follow slopbuster's rules on *everything* it writes, not just when you invoke the skill? See the **[setup guide](docs/setup-guide.md)** for CLAUDE.md, Cursor, Codex, Windsurf, and other agent configs.

---

## Why two passes

Most humanizers do one: find patterns, replace them, done. That gets you text
with no AI tells and no voice either — sterile, and just as detectable, only by
a different classifier.

So the first pass subtracts and the second adds. Take the packaging example
above. After one pass it reads like this:

> Sustainable materials can reduce waste and improve brand perception. Some
> companies also find operational efficiencies. The obstacles include cost,
> supply chain complexity, and material availability.

Clean. Every flagged pattern gone. Also completely dead — no opinion, no
rhythm, nothing a person would actually say. The second pass is what turns it
into the version at the top of this page: a stated view ("anyone quoting you a
precise number is guessing"), sentences of wildly different lengths, and
concrete nouns instead of categories.

**A warning about the second pass.** "Add specifics" is not "invent specifics."
If a rewrite hands you statistics or company names that weren't in the source,
it has fabricated them, and you have traded a detectable problem for a false
one. slopbuster flags gaps where evidence belongs instead of filling them —
those show up under FLAGS FOR MANUAL REVIEW. Fill them yourself, with real
numbers.

---

## What it catches

### Text (24 patterns)

| Category | Count | Examples |
|----------|-------|---------|
| Content | 6 | Significance inflation ("pivotal moment"), promotional language ("nestled in the heart of"), vague attributions ("experts argue") |
| Language | 6 | AI vocabulary (delve, tapestry, landscape), copula avoidance ("serves as" → "is"), synonym cycling, rule-of-three forcing |
| Style | 6 | Em dash clusters, boldface overuse, emoji as structure, curly quotes, title case headings |
| Communication | 6 | Chatbot artifacts ("I hope this helps!"), sycophancy ("Great question!"), filler phrases, hedging stacks, generic conclusions |
| Structure | — | Opening/ending anti-patterns, rhythm tests, paragraph structure checks |

### Code (79 patterns)

This is what nobody else has. AI-generated code has its own tells — different from prose, but just as detectable:

| Domain | Count | Examples |
|--------|-------|---------|
| Comments | 18 | Tautological (`// Increment counter`), "we" language, philosophical prose, section banners |
| Naming | 14 | Verbose compounds (`userDataObject`), Manager/Handler suffix abuse, acronym avoidance |
| Commits | 10 | Vague verbs ("improve"), passive voice, past tense, "various" bundling |
| Docstrings | 8 | Type redundancy, tautological summaries, happy-path-only docs |
| Quality | 15+ | Broad exception catches, god functions, mock-heavy tests, boolean params |
| LLM tells | 14 | Commented-out alternatives, perfectly symmetrical code, canonical placeholder values |

### Academic (49 rules, 10 groups)

Section-specific guidance that knows Methods sections use passive voice (and should keep it), Discussion sections should open with interpretation (not restatement), and Abstracts can't afford a single filler word:

- **Group A:** Meaning & accuracy (hard boundaries — never break these)
- **Group B:** Generic filler (kill "moreover," "plays a crucial role," meta-language)
- **Group C-D:** Punctuation habits and sentence patterns
- **Group E-F:** Voice, reasoning, deep AI syntax (abstract noun subjects, nominalization chains)
- **Group G-J:** Creative grammar, metaphor architecture, logical closure, subject variety

---

## Scoring

Three-tier weighted system. Not all AI patterns are equal — "delve" is a dead giveaway, "Additionally" is just suspicious.

| Tier | Weight | What it catches |
|------|--------|----------------|
| **Tier 1** | 3 pts | Dead giveaways: "delve," "tapestry," "navigate the landscape," sycophancy, chatbot artifacts |
| **Tier 2** | 2 pts | Corporate tells: "synergy," "leverage," copula avoidance, significance inflation, rule-of-three |
| **Tier 3** | 1 pt | Weak signals: "Additionally," "Furthermore," em dash clusters, mild hedging |

**Human-ness scale (0-10):**
- 0-3: Obviously AI (multiple cliches, robotic structure)
- 4-5: AI-heavy (some human touches, needs work)
- 6-7: Mixed (could go either way)
- 8-9: Human-like (natural voice, minimal patterns)
- 10: Indistinguishable from skilled human writer

**Target: 8+ for anything going public.**

---

## Depth levels

| Depth | What happens | Best for |
|-------|-------------|----------|
| `quick` | Single pass, obvious patterns only, no scoring | Fast edits, social copy, Slack messages |
| `standard` | Full pattern scan + two-pass audit + score + changelog | Anything going public |
| `deep` | Full scan + voice calibration against a writer's sample | Ghostwriting, brand voice matching |

---

## File structure

```
slopbuster/
├── SKILL.md                    # Master orchestrator — routes, modes, process
├── rules/
│   ├── text-content.md         # 6 content patterns
│   ├── text-language.md        # 6 language patterns
│   ├── text-style.md           # 6 style patterns
│   ├── text-communication.md   # 6 communication/filler/hedging patterns
│   ├── text-structure.md       # Structural anti-patterns + restructuring frameworks
│   ├── code-comments.md        # 18 comment anti-patterns
│   ├── code-naming.md          # 14 naming anti-patterns
│   ├── code-commits.md         # 10 commit message anti-patterns
│   ├── code-docstrings.md      # 8 docstring anti-patterns
│   ├── code-quality.md         # Error handling + API design + test patterns
│   ├── code-llm-tells.md       # 14 structural code tells
│   └── academic.md             # 49 rules, 10 groups, section-specific
├── guides/
│   ├── voice-and-soul.md       # Soul injection — not just pattern removal
│   └── style-template.md       # Build-your-own voice profile for deep mode
└── scoring.md                  # Three-tier weighted scoring system
```

---

## Supported tools

slopbuster is markdown, so it works anywhere an agent can read a skill file.
What differs is how it gets triggered.

| Agent | Install | Invoke as | Notes |
|-------|---------|-----------|-------|
| Claude Code | `npx skills add` | `/slopbuster` | Primary target — developed and tested here |
| Codex CLI | `npx skills add` | `/slopbuster` | Reads the same `SKILL.md` |
| OpenClaw | manual | skill trigger | Uses `SKILL-OC.md`, a token-optimized variant |
| Cursor · Windsurf · Cline · Copilot | `npx skills add` | rules file | No slash commands — see the [setup guide](docs/setup-guide.md) to apply the rules to everything the agent writes |
| Gemini CLI · Kiro · Pi | `npx skills add` | varies | Installs cleanly; trigger mechanism depends on the host |

Anything the [Skills CLI](https://github.com/vercel-labs/skills) supports
(40+ agents) can install it. Hosts without slash commands still get the rules —
they just apply them through config rather than on demand.

---

## Related

- **[pixelslop](https://github.com/gabelul/pixelslop)** — the visual counterpart. Catches AI-generated image slop.
- **[pixeltamer](https://github.com/gabelul/pixeltamer-gpt-image-skill)** — the image-generation counterpart. gpt-image-2 prompting doctrine, two backends, three modes, and recipes that actually work.
- **[stitch-kit](https://github.com/gabelul/stitch-kit)** — design superpowers for coding agents via Google Stitch MCP.

## Sources

Built from analyzing 1,000+ AI vs human content samples, cross-referenced against peer-reviewed LLM detection research (Kobak et al. 2025, Liang et al. 2024, Juzek & Ward COLING 2025), and Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (CC BY-SA 4.0).

## Contributing

Found a new AI pattern? Have a rule that catches something we miss? See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — use freely. See [LICENSE](LICENSE).

---

Built by Gabi @ [Booplex.com](https://booplex.com) — because I got tired of reading my own AI-assisted output and cringing.
