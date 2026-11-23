<div align="center">

# Humanise Text — AI Writing De-Slopper for Claude Code

**Strip every detectable sign of AI from your writing. One command.**

<br />

[![Star this repo](https://img.shields.io/github/stars/199-biotechnologies/humanise-text-skill?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/199-biotechnologies/humanise-text-skill/stargazers)
&nbsp;&nbsp;
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

<br />

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
&nbsp;
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-blueviolet?style=for-the-badge)](https://github.com/199-biotechnologies/humanise-text-skill)
&nbsp;
[![Python 3](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
&nbsp;
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](https://github.com/199-biotechnologies/humanise-text-skill/pulls)

---

AI-generated text has tells. "Leverage", "delve", "it's important to note", ascending tricolons, uniform sentence length, synonym cycling. Readers spot it. Editors reject it. Detection tools flag it. This skill finds every AI pattern in your text and rewrites it so it reads like a person wrote it — with the same meaning, in a fraction of the time manual editing takes.

[Install](#install) | [How It Works](#how-it-works) | [Before vs After](#before-vs-after) | [Features](#features) | [What's Inside](#whats-inside) | [Contributing](#contributing)

</div>

## The Problem

AI writing has a fingerprint. Not one tell — dozens. "Delve" appears 28x more in AI text than human text. "Showcase" is 10.7x over-represented. Negative parallelism ("It's not just X, it's Y") barely exists in human prose but saturates AI output. The sentence length barely varies — every sentence lands at 15-20 words like a metronome.

Manual de-slopping is slow and inconsistent. You catch "leverage" but miss the tricolon. You vary sentence length but leave "Furthermore" at the start of every third paragraph. The patterns are too numerous and too subtle for spot-checking.

## Before vs After

From the included blog example (Oaxaca travel piece):

| | Before (AI) | After (Human) |
|---|---|---|
| **Opening** | "In the tapestry of Mexican culture, few regions boast the breathtaking diversity..." | "I spent eleven days in Oaxaca City last March and I've been annoyed at restaurants ever since." |
| **Detail level** | "a rich array of traditional flavours" | "32 ingredients. She roasts the chillies over charcoal until they blacken but don't burn." |
| **Voice** | "This remarkable state serves as a vibrant testament to centuries of indigenous tradition" | "I bought a piece of black pottery for 300 pesos — about 15 dollars — and I'm still not sure she charged me enough." |
| **Sentence rhythm** | SD ~2-3 words (monotone) | SD >6 words (varied) |
| **Banned words** | 14 red-flag words | 0 |
| **Conclusion** | "Whether you're drawn to its culinary traditions, its artistic heritage, or its natural wonders..." | "Go in March." |

## Install

```bash
git clone https://github.com/199-biotechnologies/humanise-text-skill.git \
  ~/.claude/skills/humanise-text
```

Requires Python 3.x (no external dependencies — the scripts use only stdlib).

Then tell Claude Code: "humanise this text" or paste any text and ask to "de-slop it" or "make it sound human."

## How It Works

The skill runs a 6-step pipeline with automated detection, rewriting, critique, and validation:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  1. DETECT     Run detect_ai_patterns.py → JSON report      │
│       ↓        (scores AI density 0-100, flags every tell)   │
│                                                              │
│  2. REWRITE    Address every flag from the report            │
│       ↓        (words, phrases, structure, rhythm, tone)     │
│                                                              │
│  3. CRITIQUE   Blind LLM self-critique via subagent          │
│       ↓        (spots tells the regex missed)                │
│                                                              │
│  4. FIX        Apply critique fixes                          │
│       ↓                                                      │
│  5. VALIDATE   Run validate_humanised.py                     │
│       ↓        (12 automated checks, must all pass)          │
│                                                              │
│  6. COMPARE    Run compare_texts.py → change summary         │
│                (AI density before/after, words replaced)      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

For texts over 2,000 words, the skill splits into parallel agents — each rewrites a section with overlapping context at the seams, then a coordinator stitches and validates.

## Features

| Feature | What It Does |
|---|---|
| **AI pattern detection** | Scores text 0-100 on AI density. Flags every red/yellow word, phrase, structural pattern, and rhythm issue with positions and severity |
| **507-entry banned word list** | Every AI-overused word catalogued with human alternatives and statistical excess ratios (e.g., "delve" = 28x, "showcase" = 10.7x) |
| **Structural pattern matching** | Catches negative parallelism, ascending tricolons, trailing -ing clauses, synonym cycling, uniform paragraph openings |
| **Rhythm analysis** | Measures sentence/paragraph length standard deviation. Targets SD >6 (human range) vs SD ~2-3 (AI monotone) |
| **Blind LLM self-critique** | After rewriting, a separate agent reads the output cold and flags remaining tells the regex missed |
| **12-check validation** | Automated pass/fail on: AI density, red words, rhythm SD, paragraph SD, word count drift, formulaic openings/closings, tricolons, and more |
| **Before/after comparison** | Shows exactly what changed: density score, words replaced, patterns removed, rhythm shift |
| **3 reference guides** | Banned patterns (507 entries), structural tells (with detection heuristics), and rewrite principles (with before/after examples) |
| **3 worked examples** | Academic, business, and blog/travel — full before/after with annotated changes |

## What's Inside

```
humanise-text-skill/
├── SKILL.md                              # Skill definition (Claude Code reads this)
├── scripts/
│   ├── detect_ai_patterns.py             # AI pattern detection → JSON report (1,336 lines)
│   ├── validate_humanised.py             # 12-check validation suite (583 lines)
│   └── compare_texts.py                  # Before/after diff and metrics (859 lines)
├── reference/
│   ├── banned_patterns.md                # 507 banned words/phrases with alternatives
│   ├── structural_tells.md               # Structural AI patterns with detection heuristics
│   └── rewrite_principles.md             # Positive writing guidance with examples
├── examples/
│   ├── academic_before_after.md          # Scientific writing transformation
│   ├── business_before_after.md          # Marketing copy transformation
│   └── blog_before_after.md             # Travel/cultural writing transformation
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## The Banned Patterns Catalogue

The reference directory contains 507 flagged words and phrases across these categories:

| Category | Examples | Severity |
|---|---|---|
| **Red-flag verbs** | delve, harness, leverage, showcase, underscore, illuminate | Zero tolerance |
| **Red-flag adjectives** | robust, comprehensive, cutting-edge, myriad, multifaceted | Zero tolerance |
| **Red-flag adverbs** | seamlessly, meticulously, notably, furthermore, moreover | Zero tolerance |
| **Red-flag phrases** | "it's important to note", "no discussion would be complete without", "in today's ever-evolving" | Zero tolerance |
| **Yellow-flag words** | optimize, framework, paradigm, nuance | Max 1 per document |
| **Structural tells** | Negative parallelism, ascending tricolons, trailing -ing clauses, synonym cycling | Must break pattern |

## Standalone Script Usage

The Python scripts work independently of Claude Code:

```bash
# Detect AI patterns (outputs JSON)
python3 scripts/detect_ai_patterns.py your_text.txt --format json

# Validate humanised output against original
python3 scripts/validate_humanised.py original.txt rewritten.txt

# Compare before/after with metrics
python3 scripts/compare_texts.py original.txt rewritten.txt
```

No pip install needed. Pure Python 3 stdlib.

## Contributing

If you've spotted an AI pattern the detector misses, or found a banned word that should be on the list, PRs are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the process.

## License

[MIT](LICENSE)

---

<div align="center">

Built by [Boris Djordjevic](https://github.com/longevityboris) at [199 Biotechnologies](https://github.com/199-biotechnologies) | [Paperfoot AI](https://paperfoot.ai)

<br />

**If this is useful to you:**

[![Star this repo](https://img.shields.io/github/stars/199-biotechnologies/humanise-text-skill?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/199-biotechnologies/humanise-text-skill/stargazers)
&nbsp;&nbsp;
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

</div>
