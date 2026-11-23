# cs-writing-skill

Cross-harness Agent Skill pack for research narrative framing, multi-dimensional AI-voice removal (`humanize`), crystal-clear concept explanation (`plain`), and publication-grade academic presentation generation (`cs-report-ppt`). Each installable skill lives in its own top-level directory with a `SKILL.md` router, progressive-disclosure `references/`, and optional `agents/openai.yaml` UI metadata.

```text
cs-writing-skill/
├── README.md
├── plain/                                           # Pedagogical explanation: make hard ideas click
│   ├── SKILL.md
│   └── agents/openai.yaml
├── humanize/                                        # Multi-dimensional de-AI & narrative surgery suite
│   ├── SKILL.md                                     # 5-axis master router + guardrails + chaining recipes
│   ├── chinese.md                                   # :chinese — 7-step surgery, 28 CN patterns, anti-translationese
│   ├── english.md                                   # :english — C1-F10 catalog, direct-statement law, zero-dash rule
│   ├── paper-boundaries.md                          # :paper-boundaries — 发布会原则 (Press-Conference Principle)
│   ├── references/
│   │   ├── methodology-and-audit.md                 # :audit / :rubric — 3-Pass Engine, 100-pt rubric & voice calibration
│   │   ├── bilingual-tech-writing.md                # :bilingual — CN-EN CS prose, Pangu spacing, 32 anti-calques
│   │   ├── model-fingerprints.md                    # :model — GPT, Claude, Gemini, DeepSeek, Qwen, Kimi, Doubao, Llama
│   │   ├── academic-prose-and-rebuttal.md           # :academic / :rebuttal / :nsfc — papers, OpenReview, NSFC & LaTeX
│   │   ├── genres-playbook.md                       # :blog / :readme / :social / :email / :sop / :script / :fiction
│   │   ├── visual-image-de-ai.md                    # :image / :photo / :mj / :flux — optical physics & film halation/grain
│   │   └── scientific-figures-and-ui-de-ai.md       # :figure / :diagram / :ui — Nature/NeurIPS vectors & anti-slop UI
│   └── agents/openai.yaml
└── cs-report-ppt/                                   # Multi-scenario, multi-disciplinary academic deck generator
    ├── SKILL.md                                     # 4-axis master router, 14-slide spine & vision-in-the-loop QA
    ├── references/
    │   ├── open-source-skills-and-engines.md        # 5-track engine selector, 300+ DPI harvesting & 25-pt QA checklist
    │   ├── scenarios-group-meeting.md               # Journal club deep-dive, literature survey & weekly lab progress
    │   ├── scenarios-conference-defense-grant.md    # Oral/Spotlight/Poster, 开题/中期/硕博答辩, NSFC/grants & Job Talk
    │   ├── disciplines-stem.md                      # CS/AI/Systems/Security, Math/Stats/TCS & Physics/EE/IC/Robotics
    │   ├── disciplines-biomed-econ-humanities.md    # BioMed/Clinical/Chem, Econ/Finance/Mgmt & Humanities/Law/Qual
    │   ├── languages-and-typography.md              # Academic English, 中文学术汇报 (去Word化) & CN-EN bilingual tracks
    │   ├── palettes-and-layouts.md                  # 6 scholarly HEX palettes, anti-AI-slop laws & 12 16:9 layouts
    │   ├── spine_template.md                        # Canonical 14-slide Session Note per-slide blueprint
    │   ├── typography_rules.md                      # 16:9 EMU/inch geometry, 3 vertical zones & 7 core grid models
    │   ├── omml_syntax_guide.md                     # Native OpenXML <a14:m><m:oMath> LaTeX-to-OMML guide
    │   ├── architecture_diagrams.md                 # Native DrawingML vector diagram specification
    │   └── marginal_annotations.md                  # 5-class Lab Research Synergy callouts (旁注)
    ├── scripts/                                     # build_deck.js, crop_figures.py, latex_to_omml.py, verify_deck.py
    ├── resources/                                   # Declarative themes/palettes JSON & sample figure-backed decks
    └── agents/openai.yaml
```

---

## Skills Overview

| Skill | Entrypoint | Role | Typical Use |
|:---|:---|:---|:---|
| **`plain`** | [plain/SKILL.md](plain/SKILL.md) | Explain difficult concepts clearly without hand-waving | Diagnose where understanding breaks, then walk one small domain-native numerical example step by step |
| **`humanize`** | [humanize/SKILL.md](humanize/SKILL.md) | Remove AI voice, enforce `paper-boundaries` academic framing, and strip visual/UI slop | Rewrite CN/EN/bilingual prose, frame non-defensive papers & rebuttals (`:paper-boundaries` / `:academic`), scrub generator fingerprints, humanize image prompts & UI |
| **`cs-report-ppt`** | [cs-report-ppt/SKILL.md](cs-report-ppt/SKILL.md) | Multi-scenario, multi-disciplinary academic slide deck generator | Build figure-dominant 16:9 `.pptx`/`.pdf` decks with native OMML math across journal clubs, conference talks, thesis defenses, grants, and job talks |

> **`paper-boundaries` Integration Note:** Standalone `paper-boundaries` (Press-Conference Principle / `发布会原则`) is now built directly into `humanize` at [humanize/paper-boundaries.md](humanize/paper-boundaries.md). Invoke `/humanize :paper-boundaries` for pure narrative/experiment restructuring, or `/humanize :academic` to chain narrative surgery *before* section-by-section scholarly prose de-slopping.

The three skills remain cleanly orthogonal:
- **`plain`** governs *how to repair mental models and explain hard mechanisms with concrete domain-native numbers*;
- **`humanize`** governs *how to structure non-defensive arguments (`:paper-boundaries`) and strip synthetic AI tells across text, academic writing, imagery, and UI*;
- **`cs-report-ppt`** governs *how to turn papers, surveys, experiment logs, theses, and grants into publication-grade slide decks*.

---

## `/humanize` Multi-Axis Tag Matrix

Tags compose freely across axes (e.g., `/humanize :academic :english :claude`, `/humanize :bilingual :readme`, `/humanize :chinese :wechat :deepseek`). When no tag is supplied, `humanize` auto-detects modality, genre, language, and model family.

| Axis | Tags | Loaded Module(s) | What It Fixes |
|:---|:---|:---|:---|
| **1. Language Tracks** | `:chinese` (`:zh`, `:cn`) | [humanize/chinese.md](humanize/chinese.md) | 7-step surgery (`七步手术法`), 28 CN patterns, 3-tier corporate jargon blacklist, 余光中 12-symptom anti-translationese, parataxis & burstiness |
| | `:english` (`:en`) | [humanize/english.md](humanize/english.md) | 31-pattern catalog (`C1–F10`), Direct-Statement Law (`not X, but Y` ban), zero prose em/en-dash ban, Tier-1/2 lexical matrices, burstiness & ESL rescue |
| | `:bilingual` (`:zh-en`) | [humanize/references/bilingual-tech-writing.md](humanize/references/bilingual-tech-writing.md) | CN-EN CS prose: Pangu spacing + 8 exceptions, brand casing (`PyTorch`, `vLLM`), `` `code` `` boundaries, 32 anti-calques (`vanilla`, `oracle`), 10 AST syntax surgeries |
| **2. Academic & `paper-boundaries`** | `:paper-boundaries` | [humanize/paper-boundaries.md](humanize/paper-boundaries.md) | **发布会原则 (Press-Conference Principle):** 12 mandates, 7-tier unfavorable-result waterfall, CN/EN self-sabotage lexicons, Pareto reframing, reviewer-knife prevention |
| | `:academic` (`:paper`), `:rebuttal`, `:nsfc` (`:grant`) | [humanize/paper-boundaries.md](humanize/paper-boundaries.md) + [humanize/references/academic-prose-and-rebuttal.md](humanize/references/academic-prose-and-rebuttal.md) | Pairs `paper-boundaries` narrative lock with section-by-section paper surgery, taxonomic Related Work synthesis, `Direct-Evidence-Diff` OpenReview/journal rebuttals, NSFC (`国自然`) framing & LaTeX-safe `.tex` rules |
| **3. AI Model Fingerprints** | `:model`, `:gpt`, `:claude`, `:gemini`, `:deepseek`, `:qwen`, `:kimi`, `:doubao`, `:llama`, `:mistral` | [humanize/references/model-fingerprints.md](humanize/references/model-fingerprints.md) | Rapid Model-ID Triage + generator counter-surgeries (GPT-4o/o3/5 contrasts & scope blocks, Claude *"Here's the thing"* / *sit with* / 1-liners, Gemini bold-colon echo lists, DeepSeek `<think>` & 金句对仗, Qwen 黑话, Kimi 连接词, Doubao Emoji 捧场, Llama/Mistral) |
| **4. Genres & Formats** | `:blog`, `:readme`, `:postmortem`, `:social`, `:wechat`, `:xhs`, `:zhihu`, `:x`, `:linkedin`, `:substack`, `:email`, `:sop`, `:resume`, `:prd`, `:script`, `:fiction` | [humanize/references/genres-playbook.md](humanize/references/genres-playbook.md) | 15-genre calibration matrix: utilitarian READMEs, blameless RCAs, 公众号/小红书/知乎/X/LinkedIn (anti-broetry)/Substack, `<=120w` BLUF & PhD cold emails, Grad SOPs, XYZ Resumes, PRDs, ear-first video/podcast scripts (`气口切分`) & subtextual fiction |
| **5. Visuals, Figures & UI** | `:image`, `:photo`, `:mj`, `:flux` (`:sdxl`, `:gpt-image`, `:imagen`, `:ideogram`, `:recraft`) | [humanize/references/visual-image-de-ai.md](humanize/references/visual-image-de-ai.md) | Diagnose `V1–V12` visual tells, purge poison quality tokens (`8k`, `masterpiece`), camera/lens/film/entropy prompts, `--style raw` / Flux Raw / GPT `5600K` overrides, Lightroom/PS/Resolve + Python halation & grain |
| | `:figure`, `:diagram`, `:ui` | [humanize/references/scientific-figures-and-ui-de-ai.md](humanize/references/scientific-figures-and-ui-de-ai.md) | **Part I (`:figure`):** *Nature*/*Science*/*NeurIPS* 1:1 mm vectors, Okabe-Ito & Two-Tone HEX, `matplotlib` Type-42 & `TikZ` templates.<br>**Part II (`:ui`):** Purge purple-gradient/3-card SaaS slop (`UI1–UI12`), 5 human UI archetypes, `tabular-nums` CSS & 5-state audit |
| **6. Engine & Audit** | `:audit`, `:rubric` | [humanize/references/methodology-and-audit.md](humanize/references/methodology-and-audit.md) | Step 0 Information-Epistemic Ledger, 3-Pass Engine, 5 Hard-Fail Gates (`G1–G5`), 100-Point 6D Rubric (`D1–D6`), 8-Axis Voice DNA Calibration & 12 Anti-Overcorrection Guardrails |

---

## `/cs-report-ppt` Multi-Axis Tag Matrix

Combine tags across Scenario, Discipline, Language Track, and Palette (e.g., `/cs-report-ppt :journal-club :cs :bilingual`, `/cs-report-ppt :phd-defense :biomed :zh :oxford_navy`, `/cs-report-ppt :oral :econ :en`).

| Axis | Tags | Loaded Reference Module(s) | Core Capabilities |
|:---|:---|:---|:---|
| **1. Scenarios** | `:journal-club` (`:paper`), `:survey` (`:lit-sweep`), `:weekly` (`:progress`) | [scenarios-group-meeting.md](cs-report-ppt/references/scenarios-group-meeting.md), [spine_template.md](cs-report-ppt/references/spine_template.md), [marginal_annotations.md](cs-report-ppt/references/marginal_annotations.md) | 14–18 slide single-paper deep dive (+ Toy Walkthrough & Repro Audit), 12–16 slide MECE taxonomy survey, 6–10 slide BLUF weekly progress + MECE fault tree |
| | `:oral`, `:spotlight`, `:poster-teaser`, `:proposal`, `:midterm`, `:master-defense`, `:phd-defense`, `:nsfc`, `:grant`, `:key-rd`, `:industry`, `:award`, `:job-talk` | [scenarios-conference-defense-grant.md](cs-report-ppt/references/scenarios-conference-defense-grant.md) | Conference Oral (12–15m) / Spotlight / Poster Teaser, 开题 / 中期 / 硕博毕业答辩 (Master Roadmap + Breadcrumb + `成果矩阵` + Q&A Backup `B1–B6`), NSFC / 重点研发 / 横向 / 国奖, and 50-min Faculty Job Talk |
| **2. Disciplines** | `:cs`, `:ai`, `:systems`, `:security`, `:math`, `:stats`, `:theory`, `:physics`, `:ee`, `:ic`, `:robotics` | [disciplines-stem.md](cs-report-ppt/references/disciplines-stem.md), [architecture_diagrams.md](cs-report-ppt/references/architecture_diagrams.md), [omml_syntax_guide.md](cs-report-ppt/references/omml_syntax_guide.md) | STEM visual grammar: frozen-vs-novel pipelines, tensor pills, TCB maps, `booktabs` SOTA/ablation tables, Halmos–Tao 4-stage theorem & Proof DAGs, ISSCC die/FoM layouts, Bode & robot filmstrips |
| | `:biomed`, `:clinical`, `:chem`, `:econ`, `:finance`, `:mgmt`, `:humanities`, `:law`, `:qual` | [disciplines-biomed-econ-humanities.md](cs-report-ppt/references/disciplines-biomed-econ-humanities.md) | *Cell*/*Nature* panel surgery, blots, CONSORT, KM `No. at Risk`, ChemDraw grids; Causal DAGs, DID/IV/RDD & 5-row Stata regression surgery; archival facsimiles & Gioia coding flows |
| **3. Languages** | `:en`, `:zh`, `:bilingual` | [languages-and-typography.md](cs-report-ppt/references/languages-and-typography.md), [typography_rules.md](cs-report-ppt/references/typography_rules.md) | 100% Academic English Assertion-Evidence, 100% 规范学术中文 (`去Word化五步手术`, `<a:ea>`+`<a:latin>` dual-font binding, zero CN italic), or CN-EN hybrid group meeting |
| **4. Palettes & Engines** | `:academic_mono` *(default)*, `:oxford_navy`, `:nature_slate_teal`, `:mit_crimson_neutral`, `:cvpr_clean_blue`, `:keynote_dark_oral` | [palettes-and-layouts.md](cs-report-ppt/references/palettes-and-layouts.md), [open-source-skills-and-engines.md](cs-report-ppt/references/open-source-skills-and-engines.md) | 6 WCAG-verified scholarly palettes, 12 collision-free 16:9 layout recipes, 5 generation tracks (`PptxGenJS`, `python-pptx`, OOXML master surgery, `Typst/Beamer`, `Slidev/Marp`) + 150+ DPI Vision QA |

---

## MIRASIM

### Install

1. Open **Plugins → Skill Pack → Install from GitHub**
2. Enter the repo URL: `https://github.com/RichardJie/cs-writing-skill`
3. MIRASIM discovers every top-level subdirectory containing a `SKILL.md` (`plain`, `humanize`, `cs-report-ppt`) and installs each as an independent skill in `~/.mirasim/skills/<skill-name>/`.

*(Upgrading from an earlier version? Remove the retired `~/.mirasim/skills/paper-boundaries` card if present; `paper-boundaries` now runs via `/humanize :paper-boundaries`.)*

### Update

Click **Update** on a skill card, or run **Install from GitHub** again (overwrites the local copy).

### Usage

Use **slash commands** in the MIRASIM chat input:

| Command | What it does |
|:---|:---|
| `/plain` | Explain a hard concept with one small, domain-native numerical walkthrough |
| `/humanize :paper-boundaries` | Restructure paper narrative & experiments under the Press-Conference Principle (`发布会原则`) |
| `/humanize :academic :english` | Run `paper-boundaries` + section-by-section English scholarly prose de-slopping |
| `/humanize :chinese` | Chinese de-AI-ing — 7-step surgery, corporate jargon purge & anti-translationese |
| `/humanize :bilingual :readme` | Clean CN-EN mixed CS documentation (Pangu spacing, anti-calquing, maintainer README craft) |
| `/humanize :claude` / `:deepseek` | Scrub generator-specific rhetorical tells with adversarial cross-family guardrails |
| `/humanize :image :mj` / `:ui` | Engineer optical photorealistic image prompts or refactor vibe-coded SaaS UI slop |
| `/cs-report-ppt` | Build a 14-slide figure-dominant academic deck from a paper PDF (supports scenario/discipline/language tags) |

Natural-language triggers also work directly:
- *"Use plain to explain what grouped-query attention is actually computing"*
- *"humanize :paper-boundaries — reframe our mixed latency/accuracy table and abstract"*
- *"humanize :chinese :wechat :deepseek — 去掉这篇公众号草稿的 DeepSeek 金句味和大厂黑话"*
- *"cs-report-ppt :phd-defense :cs :zh :oxford_navy — generate my PhD defense deck"*

### Note on `SKILL.md` Descriptions

MIRASIM reads the `description` field from each top-level `SKILL.md` frontmatter using a **single-line** parser. Never use YAML folded or block scalars (`>-` or `|`); always use a single-line double-quoted string (`description: "..."`), and never place extra `SKILL.md` files inside nested reference folders.

---

## Claude Code

### Install

```bash
git clone https://github.com/RichardJie/cs-writing-skill.git /tmp/cs-writing-skill
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/paper-boundaries
cp -R /tmp/cs-writing-skill/plain ~/.claude/skills/
cp -R /tmp/cs-writing-skill/humanize ~/.claude/skills/
cp -R /tmp/cs-writing-skill/cs-report-ppt ~/.claude/skills/
```

Project-scoped install: copy skill directories into `<project>/.claude/skills/`.

### Usage

Mention the skill by name or invoke explicitly with tags:
- `$plain`
- `$humanize :paper-boundaries`
- `$humanize :academic :english`
- `$humanize :chinese` / `$humanize :bilingual`
- `$humanize :image :flux` / `$humanize :ui`
- `$cs-report-ppt :journal-club :cs :bilingual`

---

## Adding a New Skill

1. Create `<skill-name>/SKILL.md` at the repo root (required)
2. Place deep domain playbooks in `<skill-name>/references/*.md` (never name sub-files `SKILL.md`)
3. Optionally add `<skill-name>/agents/openai.yaml` for harness UI strings
4. Frontmatter format:

```yaml
---
name: my-skill
description: "Single-line double-quoted description; parses cleanly in MIRASIM and other harnesses."
---
```

5. Commit, push, then reinstall or click **Update** in your harness.

## Conventions

- One installable skill = one top-level directory + `SKILL.md`
- Always use a single-line double-quoted `description: "..."` (MIRASIM-compatible; no `>-` or `|`)
- `agents/openai.yaml` is optional harness UI metadata
- Keep skills cleanly scoped; organize large domain catalogs via progressive-disclosure files referenced from the hub `SKILL.md`
