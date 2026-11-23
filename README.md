# cs-writing-skill

Cross-harness Agent Skill pack for crystal-clear concept explanation (`plain`), AI-voice removal & non-defensive research framing (`humanize`), conference-grade academic presentation generation (`cs-report-ppt`), and extensible scientific figure production (`figure`). Each installable skill lives in its own top-level directory with a `SKILL.md` router and optional `agents/openai.yaml` UI metadata.

```text
cs-writing-skill/
├── README.md
├── plain/                                              # Explanation technique: make hard ideas click
│   ├── SKILL.md
│   └── agents/openai.yaml
├── humanize/                                           # Remove AI voice + paper-boundaries + open-source de-AI library
│   ├── SKILL.md                                        # Hub router (:chinese / :english / :paper-boundaries) + taxonomic index
│   ├── chinese.md                                      # :chinese track — 7-step surgery + Chinese AI patterns
│   ├── english.md                                      # :english track — pattern catalog + direct-statement & em-dash rules
│   ├── paper-boundaries.md                             # :paper-boundaries — 发布会原则 (Press-Conference Principle)
│   ├── upstream-skills/                                # 74 deduplicated verbatim open-source de-AI & writing GitHub skills/datasets
│   │   ├── 01-english-and-universal/                   # 16 English & universal anti-slop skills, Vale/.mdc rules & linters
│   │   ├── 02-chinese-and-bilingual/                   # 20 Simplified/Traditional Chinese de-AI & CJK style skills
│   │   ├── 03-models-and-stylometry-data/              # 8 cross-model corpus studies, excess-vocab CSV/JSONs & counter-prompts
│   │   ├── 04-genres-academic-tech-social/             # 18 academic, rebuttal, tech-doc/README, social, email & official-doc skills
│   │   └── 05-visual-image-figure-and-ui/              # 12 photorealism, scientific figure QA & UI anti-slop skills
│   ├── curated-guides/                                 # Source-attributed literature, official docs & community archives
│   │   ├── SOURCES_CATALOG.md                          # Master provenance catalog (GitHub URLs, Commit SHAs, Licenses, DOIs)
│   │   ├── wikipedia-signs-of-ai-writing.md            # Verbatim Wikipedia:Signs of AI writing (+ /Style & /Markup) archive
│   │   ├── published-stylometry-and-classics.md        # Peer-reviewed LLM excess-vocabulary studies + Orwell & Paul Graham
│   │   ├── by-language-chinese-community.md            # Chinese anti-translationese classics + community de-AI prompts
│   │   ├── by-model-tells-and-prompts.md               # GPT / Claude / Gemini / DeepSeek / Qwen / Kimi / Doubao tells & prompts
│   │   ├── by-genre-academic-tech-social.md            # Academic, rebuttal, tech blog/README, social media & email guides
│   │   └── by-visual-image-figure-ui.md                # Midjourney/FLUX/SD realism docs, journal AI figure policy & UI anti-slop
│   └── agents/openai.yaml
├── cs-report-ppt/                                      # Conference presentation PPT generator + open-source presentation library
│   ├── SKILL.md                                        # 14-slide figure-dominant spine, vision-in-the-loop QA & taxonomic index
│   ├── references/                                     # Spine template, typography rules, OMML syntax, diagrams & annotations
│   ├── scripts/                                        # build_deck.js, crop_figures.py, latex_to_omml.py, verify_deck.py
│   ├── resources/                                      # Academic theme configuration & sample figure-backed templates
│   ├── upstream-skills/                                # Verbatim open-source academic presentation & slide skills
│   │   ├── 01-general-engines/                         # PPTX, Slidev, Marp & HTML slide engines
│   │   ├── 02-paper-to-slides-and-posters/             # Paper-to-slides, LaTeX Beamer, Typst Touying & scientific posters
│   │   ├── 03-group-meeting-and-seminar/               # Journal club, literature seminar & group meeting templates
│   │   ├── 04-defense-grant-and-speaking/              # Conference talks, thesis proposals/defenses, grants & speaking skills
│   │   └── 05-disciplines-and-palettes/                # Discipline-specific slide templates & scientific color palettes
│   ├── curated-guides/                                 # Source-attributed scholar, university & practitioner presentation guides
│   └── agents/openai.yaml
└── figure/                                             # Scientific figure & diagram curation directory + nature-figure-skill
    ├── SKILL.md                                        # Pure classification & routing index across all figure skills & guides
    ├── nature-figure-skill/                            # jing1312/nature-figure-skill — Python/R journal workflow + FigureForge studio
    │   ├── README.md / README.zh-CN.md                 # Bilingual documentation, 83-panel chart atlases & quick start
    │   ├── LICENSE / DERIVATIVE_NOTICE.md              # MIT license & upstream attribution
    │   ├── figureforge/                                # Browser-based WYSIWYG SVG studio (22 templates, 16 palettes)
    │   ├── assets/                                     # 9 showcase SVG atlases (83 panels) + workflow diagrams
    │   ├── skills/nature-figure/                       # Contract-first Python/R plotting skill, 14 references & figures4papers demos
    │   ├── skills/nature-*/                            # 8 companion nature-* workflow modules
    │   └── scripts/                                    # Template, SVG & link/schema verification scripts
    ├── upstream-skills/                                # 124 deduplicated verbatim open-source plotting, diagram & dataviz GitHub repos
    │   ├── 01-scientific-figure-agent-skills/          # 30 scientific plotting, biomedical schematic & Origin/MATLAB/PyGMT skills
    │   ├── 02-architecture-diagrams-and-autofigure/    # 20 PaperBanana, AutoFigure, FigGenie, FigCraft & ML architecture toolkits
    │   ├── 03-tikz-drawio-mermaid-and-vector-dsl/      # 20 LaTeX TikZ/PGFPlots, Typst CeTZ, Draw.io, Mermaid, Excalidraw & D2 skills
    │   ├── 04-matplotlib-seaborn-and-ggplot2-styles/   # 30 SciencePlots, tueplots, mplstyle sheets, colormaps & R ggplot2 packages
    │   └── 05-chinese-community-and-dataviz-toolkits/  # 24 Chinese research community plotting/layout repos & Data-to-Viz toolkits
    ├── curated-guides/                                 # Source-attributed journal specs, scholar classics & community figure guides
    │   ├── SOURCES_CATALOG.md                          # Master provenance catalog (125 GitHub repos, Commit SHAs, Licenses, DOIs, URLs)
    │   ├── by-journal-and-scholar-guides.md            # Nature/Science/Cell/PLOS/IEEE/ACM/CVPR/NeurIPS specs + Wilke, Holtz, Wong, Rougier
    │   └── by-community-practical-guides.md            # Zhihu, sspai, ScienceNet, Reddit, HN & researcher blog figure workflows & prompts
    └── agents/openai.yaml
```

---

## Skills Overview

| Skill | Entrypoint | Role | Typical Use |
|:---|:---|:---|:---|
| **`plain`** | [plain/SKILL.md](plain/SKILL.md) | Explain difficult concepts clearly | Diagnose where understanding breaks, then walk one small domain-native numerical example step by step |
| **`humanize`** | [humanize/SKILL.md](humanize/SKILL.md) | Remove AI tone from prose, apply `paper-boundaries` narrative framing, and index verified open-source de-AI skills & empirical guides | `:chinese` ([chinese.md](humanize/chinese.md)) for Chinese de-AI-ing; `:english` ([english.md](humanize/english.md)) for English de-slopping; `:paper-boundaries` ([paper-boundaries.md](humanize/paper-boundaries.md)) for press-conference principle paper framing; plus 74 vendored upstream skills & 6 source-linked guides |
| **`cs-report-ppt`** | [cs-report-ppt/SKILL.md](cs-report-ppt/SKILL.md) | Conference paper presentation deck generator & curated academic presentation skill library | Transform paper PDFs into 14-slide figure-dominant 16:9 widescreen PPT decks with native OMML math, plus categorized upstream PPT/Beamer/Touying/Slidev/Marp skills and scholar guides |
| **`figure`** | [figure/SKILL.md](figure/SKILL.md) | Scientific figure, academic architecture diagram & data visualization curation directory | Index [`jing1312/nature-figure-skill`](figure/nature-figure-skill/README.md) ([`nature-figure`](figure/nature-figure-skill/skills/nature-figure/SKILL.md) Python/R workflow + **FigureForge** 83-panel SVG studio), 124 vendored open-source plotting/TikZ/Draw.io/AutoFigure skills, and source-linked journal, scholar & community guides |

> **`paper-boundaries` Integration Note:** Standalone `paper-boundaries` (`发布会原则` / Press-Conference Principle) is integrated directly into `humanize` at [humanize/paper-boundaries.md](humanize/paper-boundaries.md) and invoked via `/humanize :paper-boundaries`.

The four skills are independent and orthogonal:
- **`plain`** governs *how to explain and repair understanding with concrete domain-native examples*;
- **`humanize`** governs *how to strip AI voice from prose (`:chinese` / `:english`), enforce non-defensive paper framing (`:paper-boundaries`), and route to verified open-source de-AI skills and primary literature*;
- **`cs-report-ppt`** governs *how to transform papers into figure-dominant academic slide decks with vision-in-the-loop self-inspection and route to open-source presentation engines/guides*;
- **`figure`** governs *how to locate and apply verified open-source scientific plotting skills, architecture diagram toolkits, and official journal/scholar figure specifications*.

---

## `humanize/` Tracks & Open-Source Curation Taxonomy

### Core Tracks

| Invocation | Loaded File | Best For |
|:---|:---|:---|
| `:chinese` | [humanize/chinese.md](humanize/chinese.md) | Chinese prose, WeChat posts, CN blogs, CN academic polish (7-step surgery + Chinese AI pattern scan) |
| `:english` | [humanize/english.md](humanize/english.md) | English essays, READMEs, LinkedIn, technical docs (pattern catalog, direct-statement rules, em-dash ban) |
| `:paper-boundaries` | [humanize/paper-boundaries.md](humanize/paper-boundaries.md) | CS paper narrative boundaries (`发布会原则`: strengths-only framing, no self-undermining phrasing) |

### Verbatim Open-Source Skills & Curated Literature (`humanize/upstream-skills/` & `humanize/curated-guides/`)

Full commit-pinned provenance (GitHub URLs, 40-char Commit SHAs, Licenses, DOIs, and live web URLs) is cataloged in [humanize/curated-guides/SOURCES_CATALOG.md](humanize/curated-guides/SOURCES_CATALOG.md) and indexed in [humanize/SKILL.md](humanize/SKILL.md):

| Classification Axis | Upstream Skill Directory (`humanize/upstream-skills/`) | Source-Attributed Curated Guide(s) (`humanize/curated-guides/`) |
|:---|:---|:---|
| **1. English, Chinese & Bilingual** | `01-english-and-universal/` (16 repos) · `02-chinese-and-bilingual/` (20 repos) | [wikipedia-signs-of-ai-writing.md](humanize/curated-guides/wikipedia-signs-of-ai-writing.md) · [published-stylometry-and-classics.md](humanize/curated-guides/published-stylometry-and-classics.md) · [by-language-chinese-community.md](humanize/curated-guides/by-language-chinese-community.md) |
| **2. AI Models & Stylometry Data** (`GPT` / `Claude` / `Gemini` / `DeepSeek` / `Qwen` / `Kimi` / `Doubao`) | `03-models-and-stylometry-data/` (8 repos) | [by-model-tells-and-prompts.md](humanize/curated-guides/by-model-tells-and-prompts.md) · [published-stylometry-and-classics.md](humanize/curated-guides/published-stylometry-and-classics.md) |
| **3. Genres** (Academic + `paper-boundaries` / Rebuttal / Tech Docs & `README` / Social / Email & Official Docs) | `04-genres-academic-tech-social/` (18 repos) | [by-genre-academic-tech-social.md](humanize/curated-guides/by-genre-academic-tech-social.md) · [paper-boundaries.md](humanize/paper-boundaries.md) |
| **4. Visuals, Scientific Figures & UI** (`Midjourney` / `FLUX` / `SD` / Figure QA / Frontend Anti-Slop) | `05-visual-image-figure-and-ui/` (12 repos) | [by-visual-image-figure-ui.md](humanize/curated-guides/by-visual-image-figure-ui.md) |

---

## `cs-report-ppt/` Core Workflow & Open-Source Curation Taxonomy

[cs-report-ppt/SKILL.md](cs-report-ppt/SKILL.md) combines its baseline 14-slide figure-dominant conference presentation workflow with a categorized library of real open-source presentation skills and scholar/university guides:

- **Core Baseline References & Scripts:** [spine_template.md](cs-report-ppt/references/spine_template.md), [typography_rules.md](cs-report-ppt/references/typography_rules.md), [omml_syntax_guide.md](cs-report-ppt/references/omml_syntax_guide.md), [architecture_diagrams.md](cs-report-ppt/references/architecture_diagrams.md), [marginal_annotations.md](cs-report-ppt/references/marginal_annotations.md), plus modular scripts in `cs-report-ppt/scripts/` (`build_deck.js`, `crop_figures.py`, `latex_to_omml.py`, `verify_deck.py`).
- **Categorized Upstream Presentation Skills (`cs-report-ppt/upstream-skills/`):** `01-general-engines/`, `02-paper-to-slides-and-posters/`, `03-group-meeting-and-seminar/`, `04-defense-grant-and-speaking/`, and `05-disciplines-and-palettes/`.
- **Source-Attributed Presentation Guides (`cs-report-ppt/curated-guides/`):** Master provenance catalog (`SOURCES_CATALOG.md`) and scenario/discipline/language/palette guides indexed from [cs-report-ppt/SKILL.md](cs-report-ppt/SKILL.md).

---

## `figure/` Integrated Suite & Open-Source Curation Taxonomy

`figure` ([figure/SKILL.md](figure/SKILL.md)) indexes the verbatim upstream [`jing1312/nature-figure-skill`](https://github.com/jing1312/nature-figure-skill) suite ([README.md](figure/nature-figure-skill/README.md), [LICENSE](figure/nature-figure-skill/LICENSE)), **124** deduplicated open-source scientific plotting, diagramming, and visualization repositories under `figure/upstream-skills/`, and source-attributed journal/scholar/community guides cataloged in [figure/curated-guides/SOURCES_CATALOG.md](figure/curated-guides/SOURCES_CATALOG.md):

| Classification Axis | Local Upstream Directory / Entrypoint | Source-Attributed Curated Guide(s) (`figure/curated-guides/`) |
|:---|:---|:---|
| **0. Flagship Nature Figure & FigureForge Suite** | [nature-figure-skill/README.md](figure/nature-figure-skill/README.md) · [skills/nature-figure/SKILL.md](figure/nature-figure-skill/skills/nature-figure/SKILL.md) · [figureforge/README.md](figure/nature-figure-skill/figureforge/README.md) · [figure-contract.md](figure/nature-figure-skill/skills/nature-figure/references/figure-contract.md) · [atlas-gallery.md](figure/nature-figure-skill/skills/nature-figure/references/atlas-gallery.md) · [qa-contract.md](figure/nature-figure-skill/skills/nature-figure/references/qa-contract.md) | [SOURCES_CATALOG.md](figure/curated-guides/SOURCES_CATALOG.md) · [by-journal-and-scholar-guides.md](figure/curated-guides/by-journal-and-scholar-guides.md) |
| **1. Scientific Figure Agent Skills** | `figure/upstream-skills/01-scientific-figure-agent-skills/` (30 repos) | [by-journal-and-scholar-guides.md](figure/curated-guides/by-journal-and-scholar-guides.md) · [by-community-practical-guides.md](figure/curated-guides/by-community-practical-guides.md) |
| **2. Architecture Diagrams & AutoFigure** (`PaperBanana` / `AutoFigure` / `FigGenie` / `FigCraft` / `PlotNeuralNet`) | `figure/upstream-skills/02-architecture-diagrams-and-autofigure/` (20 repos) | [by-community-practical-guides.md](figure/curated-guides/by-community-practical-guides.md) |
| **3. TikZ, Draw.io, Mermaid & Vector DSLs** (`TikZ` / `PGFPlots` / `CeTZ` / `Draw.io` / `Mermaid` / `Excalidraw` / `D2`) | `figure/upstream-skills/03-tikz-drawio-mermaid-and-vector-dsl/` (20 repos) | [by-community-practical-guides.md](figure/curated-guides/by-community-practical-guides.md) |
| **4. Matplotlib, Seaborn & ggplot2 Styles** (`SciencePlots` / `tueplots` / `cmcrameri` / `ggsci` / `cowplot` / `patchwork`) | `figure/upstream-skills/04-matplotlib-seaborn-and-ggplot2-styles/` (30 repos) | [by-journal-and-scholar-guides.md](figure/curated-guides/by-journal-and-scholar-guides.md) |
| **5. Chinese Community & Dataviz Toolkits** (`MLNLP-World` / `guanyingc` / `lcpmgh/colors` / `From Data to Viz` / `AntV`) | `figure/upstream-skills/05-chinese-community-and-dataviz-toolkits/` (24 repos) | [by-community-practical-guides.md](figure/curated-guides/by-community-practical-guides.md) · [by-journal-and-scholar-guides.md](figure/curated-guides/by-journal-and-scholar-guides.md) |

---

## MIRASIM

### Install

1. Open **Plugins → Skill Pack → Install from GitHub**
2. Enter the repo URL: `https://github.com/RichardJie/cs-writing-skill`
3. MIRASIM discovers every top-level subdirectory that contains a `SKILL.md` (`plain`, `humanize`, `cs-report-ppt`, `figure`) and installs each as a separate skill in `~/.mirasim/skills/<skill-name>/`.

*(Upgrading from an earlier version? Remove `~/.mirasim/skills/paper-boundaries` if present; `paper-boundaries` now runs via `/humanize :paper-boundaries`.)*

### Update

Click **Update** on a skill card, or run **Install from GitHub** again (overwrites the local copy).

### Usage

Use **slash commands** in the MIRASIM chat input:

| Command | What it does |
|:---|:---|
| `/plain` | Explain a concept with a small, domain-native numerical walkthrough |
| `/humanize :chinese` | Chinese de-AI-ing — 7-step surgery, Chinese pattern scan |
| `/humanize :english` | Humanize English — pattern catalog, em-dash ban, direct-statement rules |
| `/humanize :paper-boundaries` | Revise, compress, or restructure paper narrative under the press-conference principle (`发布会原则`) |
| `/cs-report-ppt` | Create a 14-slide figure-dominant academic presentation deck from a paper PDF |
| `/figure` | Route to `nature-figure-skill` (`Python`/`R` workflow & **FigureForge** studio), 124 upstream plotting/diagram skills, and journal/scholar/community figure guides |

Natural-language triggers also work, for example:
- *"Use plain to explain what attention is actually computing"*
- *"humanize :chinese — remove AI voice from this Chinese paragraph"*
- *"humanize :english — remove AI tells from this README"*
- *"humanize :paper-boundaries — revise this abstract and experiment discussion"*
- *"Use figure to turn this ablation CSV into a 183mm two-column Nature multi-panel figure"*

### Note on `SKILL.md` Descriptions

MIRASIM reads the `description` field from each top-level `SKILL.md` frontmatter using a **single-line** parser. Do not use YAML folded or block scalars (`>-` or `|`); always use a single-line double-quoted string (`description: "..."`).

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
cp -R /tmp/cs-writing-skill/figure ~/.claude/skills/
```

Project-scoped install: copy skill directories to `<project>/.claude/skills/`.

### Usage

Mention the skill by name or invoke explicitly:
- `$plain`
- `$humanize :english` / `$humanize :chinese` / `$humanize :paper-boundaries`
- `$cs-report-ppt`
- `$figure`

---

## Adding a New Skill

1. Create `<skill-name>/SKILL.md` at the repo root (required)
2. Optionally add `<skill-name>/agents/openai.yaml` for harness UI strings
3. Frontmatter example:

```yaml
---
name: my-skill
description: "Single-line description; parses correctly in MIRASIM and other harnesses"
---
```

4. Commit, push, then reinstall or click **Update** in your harness.

## Conventions

- One skill = one top-level directory + `SKILL.md`
- Always use a single-line double-quoted `description: "..."` (MIRASIM-compatible; no `>-` or `|`)
- `agents/openai.yaml` is optional metadata; MIRASIM skill cards do not read it
- Keep each skill focused; use progressive disclosure referenced from the hub `SKILL.md`
