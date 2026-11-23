# paper2beamer-skills

**English** | [繁體中文](README.zh-TW.md)

A reusable **skills library** for reading, understanding, presenting, and synthesizing academic papers — **field-agnostic**, with an optional per-workspace `domain.md` to tune it to your research area.

It is not a PDF-to-slides converter.
The goal is to help a researcher read, understand, reorganize, explain, critique, and synthesize papers, so the output feels like a careful graduate student prepared a seminar talk or research memo — not like an LLM emitted shallow bullets.

> **Status: experimental — early-stage release.** This is a reusable skill library, not a polished product.
> It has been exercised primarily as an **agent workflow** (an AI agent reading the `SKILL.md` files and following them), not as a conventional CLI tool, and it has limited real-world testing so far.
> **Always inspect the outputs manually** — verify slides compile and read well, and check that every claim, number, and citation matches the source papers before you rely on or present anything.
> Interfaces and wording may change.

## What's in here

```text
.
├── AGENTS.md                 # task routing + global principles for agents
├── README.md                 # this file (English)
├── README.zh-TW.md           # Traditional Chinese
├── LICENSE                   # MIT License
├── CHANGELOG.md              # version/change notes
├── Makefile                  # repo-level test / compile / hygiene checks
├── docs/                     # quickstart, prompt templates, copyright policy
├── skills/
│   ├── paper-beamer-deck/        # ONE paper  → detailed XeLaTeX Beamer deck
│   │   ├── SKILL.md
│   │   ├── templates/            # main.tex, Makefile, notes.md
│   │   ├── scripts/              # log gate, PDF rendering, deterministic figure extraction
│   │   └── examples/
│   └── research-gap-analysis/    # MANY papers → research-gap memo
│       ├── SKILL.md
│       ├── templates/            # research-gap-analysis.md, paper-matrix.md, reading-note.md
│       └── examples/
└── workspace-template/       # copy this to start a new paper-reading workspace
    ├── AGENTS.md
    ├── papers/  slides/  analysis/
    ├── domain.md                 # optional: your field & audience (skills adapt to it)
    ├── theme.tex                 # workspace-wide theme selection: edit to restyle all decks
    └── beamerthemeSimple.sty     # bundled default Simple Beamer theme (no logos)
```

## Available skills

| Skill | Use it when | Produces |
|-------|-------------|----------|
| **[paper-beamer-deck](skills/paper-beamer-deck/SKILL.md)** | the user wants slides / a summary / an explanation of **one** specific paper | a detailed, presentation-ready XeLaTeX Beamer deck (+ speaker notes) under `slides/<name>/` |
| **[research-gap-analysis](skills/research-gap-analysis/SKILL.md)** | the user wants to compare / synthesize / find gaps across **multiple** papers | a structured research-gap memo, comparison matrix, and per-paper reading notes under `analysis/<topic>/`, **plus** a synthesis presentation deck under `slides/<topic>-gap-analysis/` |

Agents: open the matching `SKILL.md` and follow it.
`AGENTS.md` at the repo root routes tasks to the right skill and states the shared principles.

Start here if you are new:
- [`docs/quickstart.md`](docs/quickstart.md) — shortest path from PDF to reviewed deck.
- [`docs/prompts.md`](docs/prompts.md) — prompt templates for common workflows.
- [`docs/copyright.md`](docs/copyright.md) — repository and workspace copyright hygiene.

## Installation & usage

There are two ways to use these skills.
Pick one.

### Option A — self-contained workspace (simplest)

Copy `workspace-template/` to a new folder and drop the `skills/` directory inside it, so the workspace carries its own copy of the skills, theme, and templates.
Everything lives in one place; nothing references this repo afterward.

```bash
cp -r workspace-template ../my-topic-workspace
cp -r skills            ../my-topic-workspace/skills
cd ../my-topic-workspace
# put PDFs in papers/, then invoke a skill (see the two "Using …" sections below)
```

In this layout the helper-script paths are `skills/paper-beamer-deck/scripts/…` from the workspace root (the deck Makefile already finds `check_latex_log.py` via its `../../skills/…` / `../../../skills/…` lookup).
Best when you want a portable, frozen copy per project.

### Option B — external skills repo (shared, updatable)

Keep this repo in one place and reference it from each workspace via a path or a git submodule, so multiple workspaces share one copy you can update centrally.

```bash
# one-time: clone the skills repo somewhere stable
git clone https://github.com/Haouo/paper2beamer-skills ~/tools/paper2beamer-skills

# per project: a workspace that points at it
cp -r ~/tools/paper2beamer-skills/workspace-template ../my-topic-workspace
cd ../my-topic-workspace
ln -s ~/tools/paper2beamer-skills/skills skills      # or a git submodule (below)
```

As a submodule inside a project that is itself a git repo:

```bash
git submodule add https://github.com/Haouo/paper2beamer-skills .skills-src
ln -s .skills-src/skills skills
```

Point the agent at the workspace and tell it where the skills live (e.g. `skills/` via the symlink).
Best when several workspaces should track the same skills and get updates with a `git pull` / `git submodule update`.

> Either way, the agent reads the skills from `SKILL.md` and writes outputs into the workspace's `papers/ slides/ analysis/`.
> The skill files themselves are reference material; you do not "install" them into a runtime.

## Using the paper Beamer deck skill

You don't run the build by hand — the agent does. Your part:

1. In a workspace (see below), put the paper at `papers/<name>.pdf`.
2. Ask the agent (see [Example prompts](#example-prompts)). Optionally pick a **visual-QA cadence** up front — the skill asks once, default **risk-targeted**:
   - **one-shot** — log-gate every batch, then one final full-deck visual pass + aggressive repair. Fastest.
   - **risk-targeted** (default) — log-gate every batch, visually inspect only high-risk slides (TikZ, big/cropped figures, wide tables, result plots), plus one final full-deck pass.
   - **incremental** — visually inspect after every batch. Most thorough, ~10× the visual-QA cost.

The agent then follows [`SKILL.md`](skills/paper-beamer-deck/SKILL.md): it reads the paper, outlines, authors slides **in small batches**, runs the fail-on-warning log gate every batch (cheap, in all modes), does the visual QA for your chosen cadence, and ends with a **mandatory final full-deck visual pass** — fixing broken slides by splitting/redesigning, not by shrinking fonts.
Outputs land in `slides/<paper-short-name>/` (`main.tex`, `notes.md`, `figures/`).
Decks use the bundled Simple theme (`\usetheme{Simple}`) and **require XeLaTeX**; the template `Makefile`/`main.tex` resolve the theme from the workspace root.

When the source paper is a PDF, the agent first runs the deterministic figure
extraction pipeline:

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/<paper>.pdf --out build/figures/<paper-short-name>
```

This writes `figures.json`, high-resolution full-page renders under `pages/`,
figure crops under `figures/`, and a validation page at
`previews/index.html`.
Slide generation consumes `figures.json` and uses only records marked
`status: ok` after preview inspection.
If layout extraction fails, the pipeline renders pages for manual review and
marks figure records as `needs_manual_review` rather than inventing approximate
crops.

<details>
<summary>What the agent runs under the hood</summary>

```bash
# scaffold the deck
mkdir -p slides/<paper-short-name>/figures
cp skills/paper-beamer-deck/templates/{main.tex,Makefile,notes.md} slides/<paper-short-name>/

# after each batch (cheap, every mode): compile + log gate
cd slides/<paper-short-name>
make                 # xelatex ×2 + fail-on-warning log gate

# read rendered pages when the cadence calls for it (the expensive step)
python3 ../../skills/paper-beamer-deck/scripts/render_pdf_pages.py main.pdf --pages 1-10
```
</details>

Helper scripts:
- `scripts/check_latex_log.py` — fails the build on LaTeX/package errors, missing files, overfull h/vbox, and undefined references/citations.
- `scripts/render_pdf_pages.py` — renders pages to PNGs via `pdftoppm`/`pdftocairo`/ ImageMagick (best-effort; prints install hints if none are present).
- `scripts/figure_extraction/extract_figures.py` — extracts PDF figure metadata/crops into `figures.json`, renders full pages, supports `figure_overrides.json`, and writes `previews/index.html`.
- `scripts/figure_extraction/verify_figures.py` — verifies `figures.json`, bbox bounds, crop files, and blank-looking crops before slide generation.
- `scripts/figure_extraction/select_figures.py` — copies selected `status: ok` figures into a deck's `figures/` directory by label or manifest index.
- `scripts/figure_extraction/schema.md` — stable `figures.json` schema.
- `scripts/generate_quality_report.py` — writes a deck `quality_report.md` covering build, visual-QA, figure, and open-risk status.
- `scripts/check_deck_sources.py` — checks source traceability and reused-figure attribution basics.
- `scripts/check_visual_qa.py` — checks rendered-page coverage for final visual inspection.
- `scripts/doctor.py` — diagnoses common workspace dependency/setup problems.
- `scripts/extract_pdf_figures.md` — manual/debug fallback notes.

The helper scripts have a regression suite (no LaTeX/poppler needed; the figure extraction smoke test requires PyMuPDF):

```bash
make check
```

## Using the research gap analysis skill

As above, the agent does the work — your part is to drop in papers and ask. This skill has two output modes — say which up front (default `memo+deck`):

- **`memo+deck`** (default): the written analysis **plus** a presentation deck. Higher cost — it also builds and visually inspects a LaTeX deck (needs XeLaTeX).
- **`memo-only`**: just the Markdown memo, matrix, and reading notes. Lower cost, no LaTeX. Pick this if you only need the written analysis or XeLaTeX is unavailable.

1. Put the papers in `papers/`.
2. Ask the agent (see [Example prompts](#example-prompts)), saying which mode you want.

The agent then follows [`SKILL.md`](skills/research-gap-analysis/SKILL.md): it builds a paper matrix and synthesizes **across** papers (not one-by-one) — explicit / implied / methodology / deployment / opportunity gaps, each rated Strong / Medium / Weak, with claims grounded in the papers and uncertainty marked. In `memo+deck` mode it then builds **one** presentation deck for the whole analysis (landscape → taxonomy → comparison → graded gaps → directions, not one deck per paper), reusing the Beamer build/QA machinery and the same selectable visual-QA cadence as the deck skill.
Outputs land in `analysis/<topic>/` (plus `slides/<topic>-gap-analysis/` for the deck).

<details>
<summary>What the agent runs under the hood</summary>

```bash
# scaffold the analysis
mkdir -p analysis/<topic>/reading-notes analysis/<topic>/figures
cp skills/research-gap-analysis/templates/research-gap-analysis.md analysis/<topic>/
cp skills/research-gap-analysis/templates/paper-matrix.md          analysis/<topic>/
cp skills/research-gap-analysis/templates/reading-note.md          analysis/<topic>/reading-notes/<paper>.md

# memo+deck mode: scaffold the synthesis deck, then build it (same QA cadence as the deck skill)
mkdir -p slides/<topic>-gap-analysis/figures
cp skills/research-gap-analysis/templates/slides-main.tex  slides/<topic>-gap-analysis/main.tex
cp skills/research-gap-analysis/templates/slides-notes.md  slides/<topic>-gap-analysis/notes.md
cp skills/paper-beamer-deck/templates/Makefile             slides/<topic>-gap-analysis/
cd slides/<topic>-gap-analysis && make
```
</details>

See [`workspace-template/AGENTS.md`](workspace-template/AGENTS.md) for how the skills are used from inside a copied workspace, and [Installation & usage](#installation--usage) above for the two ways to wire it up.

## Example prompts

**Single-paper Beamer deck**
- "Read `papers/foo.pdf` and make a detailed Beamer deck."
- "Create a presentation-ready slide deck explaining this paper for a seminar."
- "Summarize and teach paper X with slides and speaker notes."

**Multi-paper research-gap analysis**
- "Analyze these papers and find research gaps."
- "Compare papers A, B, and C and tell me what's missing."
- "What has been done in this area and what remains open?
  Suggest research directions."

## Works for any field

These skills are **field-agnostic** — the workflow (understand → outline → present, and compare → synthesize → find gaps) applies to any empirical or method-driven research, not just computer science.
To tune background depth, terminology, and how evidence is judged to your area, fill in the per-workspace `domain.md` (your field, audience, assumed background, key terms).
Leave it unedited and the skills stay neutral, assuming a general graduate-level audience in each paper's own field.
The worked examples under `skills/*/examples/` use a computer-architecture topic purely for illustration.

## Theming

Decks use the bundled **Simple** theme by default, but the theme is a single workspace-wide choice you can swap.
Each workspace has a `theme.tex` at its root that every deck loads; edit it once to restyle all decks (decks fall back to Simple if it is absent).
Three options:

1. **Any installed Beamer theme** — in `theme.tex`, use e.g. `\usetheme{metropolis}` or `\usetheme{Madrid}` (must be installed in your TeX distribution).
2. **Your own custom theme** — drop `beamerthemeMyTheme.sty` (and any images it needs) at the workspace root and set `\usetheme{MyTheme}` in `theme.tex`.
   The deck `Makefile` already adds the workspace root to `TEXINPUTS`, so the `.sty` is found automatically.
3. **Tweak the bundled theme** — set `\definecolor{simpleAccent}{RGB}{...}` before `\usetheme{Simple}` in `theme.tex` to change the accent color.

To restyle just one deck, replace the `\InputIfFileExists{../../theme.tex}{}{...}` line in that deck's `main.tex` with a direct `\usetheme{...}`.
See [`workspace-template/AGENTS.md`](workspace-template/AGENTS.md#theming) for details.

## Requirements

- **XeLaTeX** (TeX Live or similar) for the Beamer decks.
  The bundled Simple theme is self-contained (no logos/assets) and falls back to default fonts if TeX Gyre Heros / Fira Mono are not installed.
  See [Theming](#theming) to use your own theme.
- **Python 3** for the helper scripts (standard library only).
- **PyMuPDF** (`python3 -m pip install pymupdf`) for deterministic source-PDF figure extraction.
- Optional for PDF page rendering: `poppler-utils` (`pdftoppm`/`pdftocairo`) or ImageMagick + Ghostscript.
- Recommended for layout-aware figure detection: `docling`.
  First use may download Docling model artifacts; scanned PDFs may also require OCR model artifacts if you pass `--docling-ocr`.
  For offline machines, run one warm-cache conversion while online or point Docling to a pre-populated artifacts cache before using the workflow offline.
- Legacy optional fallback for layout-aware figure detection: `pdffigures2`.

Why not just extract embedded images?
Many academic figures are vector drawings, line plots, or composites made from
many PDF objects. Raw embedded-image extraction can miss them, split them into
tiles, or omit vector labels and axes. The figure pipeline therefore uses
layout metadata plus high-resolution rendered-page cropping, which preserves
vector and mixed figures as they appear in the paper.

Manual bbox overrides use `figure_overrides.json`:

```json
[
  {
    "label": "Figure 3",
    "page": 5,
    "bbox": [72, 120, 520, 430],
    "caption": "Manually corrected Figure 3"
  }
]
```

Place it in the current directory or output directory, or pass
`--overrides path/to/figure_overrides.json`, then rerun the extractor.
The extractor also writes `figure_overrides.example.json` with page dimensions
and placeholder bboxes for manual correction.

Useful figure commands:

```bash
# Filter noisy layout detections.
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/foo.pdf --out build/figures/foo --type picture,chart,table --min-area-ratio 0.01

# Verify before using extracted assets in slides.
python3 skills/paper-beamer-deck/scripts/figure_extraction/verify_figures.py \
  build/figures/foo/figures.json

# Copy selected figures into a deck.
python3 skills/paper-beamer-deck/scripts/figure_extraction/select_figures.py \
  build/figures/foo/figures.json --labels "Figure 1,Table 2" --copy-to slides/foo/figures
```

The preview HTML includes each crop plus a red bbox overlay on the rendered page
so incorrect layout detections are easier to catch.
Before accepting a deck, the helper scripts can produce a quality report and
run lightweight checks:

```bash
python3 skills/paper-beamer-deck/scripts/generate_quality_report.py slides/foo \
  --figures-json build/figures/foo/figures.json
python3 skills/paper-beamer-deck/scripts/check_deck_sources.py slides/foo
python3 skills/paper-beamer-deck/scripts/check_visual_qa.py slides/foo
python3 skills/paper-beamer-deck/scripts/doctor.py .
```

## Smoke test

A 60-second check that your environment can build and inspect decks.
Run from the repo root (or a workspace that has the `skills/` directory).

**1.
Is XeLaTeX available?**

```bash
xelatex --version        # should print "XeTeX 3.x …"; if "command not found", install TeX Live
```

**2.
Does the log gate work?** Feed `check_latex_log.py` a tiny log with a known problem and confirm it fails (exit code `1`), then a clean log and confirm it passes (exit `0`):

```bash
printf 'Overfull \\hbox (12.0pt too wide) in paragraph at lines 1--2\n' > /tmp/bad.log
python3 skills/paper-beamer-deck/scripts/check_latex_log.py /tmp/bad.log ; echo "exit=$?"   # FAIL, exit=1

printf 'Output written on main.pdf (3 pages).\n' > /tmp/ok.log
python3 skills/paper-beamer-deck/scripts/check_latex_log.py /tmp/ok.log  ; echo "exit=$?"   # OK,   exit=0
```

**3.
Can you render PDF pages?** Only if you already have a compiled `main.pdf` (e.g. after `make` in a deck directory):

```bash
python3 skills/paper-beamer-deck/scripts/render_pdf_pages.py main.pdf --pages 1-3 --out _preview
# writes _preview/main-page-*.png; open them to eyeball the slides.
# With no PDF tool installed it prints install hints and exits non-zero (no traceback).
```

**4.
Can you run figure extraction fallback mode?** Only if you have PyMuPDF and any valid paper PDF:

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/foo.pdf --out build/figures/foo
# Default backend is --backend auto: Docling first, then pdffigures2.
# If no layout backend succeeds, expect pages/page_*.png, figures.json,
# previews/index.html, and needs_manual_review records/instructions.
```

The regression suite uses generated synthetic PDFs for fixture coverage instead
of committing copied paper content. An optional live Docling smoke test is
available with `PAPER_BEAMER_RUN_DOCLING_SMOKE=1`; keep it off in hermetic CI.
This repository also ships a GitHub Actions workflow for tests/compile checks,
a `CHANGELOG.md`, and a synthetic-only examples gallery under
`skills/paper-beamer-deck/examples/gallery.md`.

Repository hygiene checks reject tracked paper PDFs / binary assets and broken
local Markdown links:

```bash
make hygiene
```

**5.
(Optional) Full template build.** Copy the deck template into a workspace and build:

```bash
cp -r workspace-template /tmp/ws && cp -r skills /tmp/ws/skills
mkdir -p /tmp/ws/slides/demo/figures
cp skills/paper-beamer-deck/templates/{main.tex,Makefile} /tmp/ws/slides/demo/
( cd /tmp/ws/slides/demo && make )   # expect "main.pdf" + a clean log gate
```

## License

MIT License. See [`LICENSE`](LICENSE).
