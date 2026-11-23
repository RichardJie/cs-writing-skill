# Open-Source PPT Agent Skills, Slide Generation Engines & Vision-in-the-Loop QA Architecture

> **Module Role**: Foundational engineering reference for [`cs-report-ppt`](../SKILL.md). Synthesizes open-source presentation agent skills, programmatic slide generation stacks, academic document-to-slide research systems, cognitive presentation design principles, deterministic engine routing rules, high-DPI figure harvesting ([`scripts/crop_figures.py`](../scripts/crop_figures.py)), native DrawingML/OMML equation injection ([`omml_syntax_guide.md`](omml_syntax_guide.md) & [`scripts/latex_to_omml.py`](../scripts/latex_to_omml.py)), headless LibreOffice + PyMuPDF visual self-inspection, and a 25-point Visual & Structural Defect Audit Checklist.

---

## 1. Architectural Synthesis: Why Academic Presentations Require a Hybrid Engine

Most generic AI slide generators fail on scientific and technical presentations because they optimize for corporate pitch decks—producing bloated bullet walls, decorative stock imagery, broken mathematical notation, and distorted figures. Conversely, traditional academic workflows (`LaTeX Beamer`) preserve mathematical rigor at the cost of rigid visual layouts and non-editable PDFs that collaborators cannot tweak in PowerPoint or Keynote.

`cs-report-ppt` unifies four historically separate lineages into a single deterministic, agent-executable pipeline:

1. **Code-Driven Editable OOXML Generation** (from `anthropics/skills`, Cursor/Claude Code `PptxGenJS` & `python-pptx` workflows): Generating native `.pptx` DrawingML primitives (`<p:sp>`, `<a:tbl>`, `<p:pic>`) on a strict $13.333'' \times 7.500''$ (16:9) coordinate grid so every text box, vector node, and table cell remains double-click editable.
2. **Native AST-to-OMML Vector Math Injection** (bridging `Pandoc`/`texmath` and OpenXML `<a14:m>`): Bypassing blurry PNG/SVG equation bitmaps by compiling $\LaTeX$ directly into Office Math Markup Language (`<m:oMath>` / `<m:oMathPara>`) injected into slide XML runs.
3. **Multimodal Research-Grade Asset Grounding & Spatial Planning** (from `Paper2Poster`, `PPTAgent`, `AutoPresent`, and `PyMuPDF`/`Docling`/`MinerU`): Harvesting authentic 300+ DPI vector/raster figures and tables from source PDFs, measuring true aspect ratios ($R = W / H$), and dynamically adapting card geometry to the visual evidence rather than cramming graphics into static boxes.
4. **Closed-Loop Painter–Commenter Vision QA** (from `Paper2Poster`, `PPTEval`, and headless `LibreOffice` + `PyMuPDF`): Treating programmatic XML checks as pre-filters while enforcing multimodal pixel inspection of 150–200 DPI rendered slide images as the sole ground truth.

---

## 2. Ecosystem Survey: Open-Source PPT Skills, Engines & Research Systems

### 2.1 Open-Source Coding-Agent PPT Skills (`Claude Code`, `Cursor`, `OpenClaw`, `Codex`)

| Ecosystem / Repository | Core Technical Mechanism | Architectural Strengths to Adopt | Failure Modes in Academic Contexts |
|:---|:---|:---|:---|
| **`anthropics/skills` (`skills/pptx`)** | Dual-track workflow: (1) **Scratch Creation** via Node.js `PptxGenJS` or `html2pptx` DOM coordinate extraction; (2) **Template Surgery** by unzipping `.pptx` OOXML, building a layout inventory (`inventory.py`), cloning/reordering slides (`add_slide.py`, `rearrange.py`), pruning orphan `.rels` (`clean.py`), and rendering contact sheets (`thumbnail.py`) via `soffice` + `pdftoppm`. | • Treating `.pptx` as a transparent ZIP of XML files for surgical edits.<br>• Mandatory visual contact-sheet thumbnail review to catch layout regressions.<br>• Clean separation between greenfield code generation and corporate/university `.potx` template editing. | • Zero native OMML math support (`PptxGenJS` emits plain text runs).<br>• Enforces commercial "dark-light-dark contrast sandwich" palettes that clash with high-key white-background academic figures.<br>• `html2pptx` flattens math and complex CSS grids into brittle absolute boxes. |
| **Cursor / Claude Editorial Skills** (`sharonzhang98/editorial-pptx-deck`, `sunchaokun/PPT-Design-Skill`, `PPT Master`) | Direct coordinate-computed `PptxGenJS` / `python-pptx` scripts enforcing strict typographic grids, thin hairline rules, custom accent bars, and double-click editable native shapes without locked master placeholders. | • High-contrast editorial minimalism (`#FFFFFF` canvas, crisp rules, disciplined whitespace).<br>• Explicit pixel/inch coordinate budgets preventing text-box overlap.<br>• Native PowerPoint object hierarchy preserving user post-editability. | • Tuned for executive strategy/pitch narratives rather than multi-panel ablations, tensor shapes, or regression tables.<br>• No automated PDF figure harvesting or $\LaTeX$ equation pipeline. |
| **OpenClaw & Web-First Deck Skills** (`LeoYeAI/openclaw-slides`, `kaisersong/slide-creator`, `Yuancircle/openclaw-ppt-html-pipeline`) | Blueprint $\rightarrow$ Outline Review $\rightarrow$ Single-file zero-dependency HTML/CSS/JS slide generation or third-party API wrappers (`SlideSpeak`, `Tosea`). | • Explicit **Blueprint Gate** before slide synthesis prevents structural drift.<br>• Rich CSS animations and responsive browser previewing for developer talks. | • HTML decks cannot be double-clicked in PowerPoint/Keynote for advisor edits or conference upload.<br>• Headless browser print-to-PDF/PPTX frequently breaks pagination, fonts, and vector crispness. |
| **`awesome-claude-skills` / `awesome-openclaw-skills`** Community Variants | Markdown-to-PPTX bridges (`pandoc -t pptx`, `marp --pptx`) or lightweight `python-pptx` placeholder fillers. | • Ultra-low token overhead for rapid 5-minute draft outlines. | • `pandoc -t pptx` produces austere, single-column unstyled slides unable to represent asymmetric figure-and-callout layouts (`split_65_35`) or multi-card matrices (`quadrant_2x2`). |

### 2.2 Programmatic `.pptx` & OpenXML Generation Engines

| Technical Dimension | `PptxGenJS` (Node.js) + OpenXML Post-Injector | `python-pptx` (Python) + `lxml` / `ElementTree` | HTML-to-PPTX (`dom-to-pptx` / Browser DOM) | Raw OOXML ZIP Surgery (`slideN.xml` Direct) |
|:---|:---|:---|:---|:---|
| **Coordinate Unit** | Floating-point **Inches** (`x: 0.60, y: 1.65, w: 7.70, h: 5.20`) | **EMU** integers (`Inches(0.60)` = `548640` EMU; $1'' = 914,400\text{ EMU}$) | CSS `px` / `%` / Flexbox / Grid mapped via `getBoundingClientRect()` | Raw **EMU** attributes (`<a:off x="..." y="..."/><a:ext cx="..." cy="..."/>`) |
| **Code Conciseness & Agent Reliability** | **Highest** — Compact declarative JSON options; minimal boilerplate per card/table. | **High** — Explicit Python API, but styling borders, shadows, and cell margins requires verbose XML helper functions. | **Medium** — LLMs write HTML/Tailwind easily, but DOM-to-DrawingML coordinate conversion drifts on line wraps. | **Low for scratch; Highest for template edits** — Writing full `slideN.xml` from scratch is token-expensive and schema-fragile. |
| **Image Aspect-Ratio Control** | Built-in `sizing: { type: 'contain', w, h }` centers and scales isotropically inside target box. | `add_picture(path, left, top, width, height)` stretches if both `width` & `height` are passed unless pre-computed via `PIL.Image.size`. | CSS `object-fit: contain` works in browser, often mishandled or stretched by DOM exporters. | Manual calculation of `<a:xfrm>` extents and `<a:srcRect>` cropping percentages ($1/1000\%$). |
| **Native Table Engine** | Clean 2D cell array with per-cell `fill`, `bold`, `border`, `colW`, `valign`. | Native `add_table(rows, cols, ...)`, requires manual cell iteration for borders (`<a:ln>`) and vertical centering. | HTML `<table>` often exported as disconnected rectangles + text boxes instead of a true `<a:tbl>`. | Verbose `<a:graphicData>` / `<a:tbl>` / `<a:tr>` / `<a:tc>` XML construction. |
| **Vector Diagrams & Connectors** | Clean `ShapeType.roundRect`, `ellipse`, `rightArrow`, `line`, `rectRadius`, soft shadows. | Full `MSO_SHAPE` enum support; drop shadows and custom rounded radii require `oxml` manipulation. | SVG/CSS borders frequently rasterized or dropped during PPTX conversion. | Full access to every DrawingML `<a:prstGeom>` and `<p:cxnSp>` connector routing node. |
| **Native Editable Math (OMML)** | ❌ None natively; **Solved via Two-Phase `<<MATH:...>>` + `latex_to_omml.py` injection**. | ❌ None natively; naive `lxml` append into `<a:r>` causes PowerPoint **Silent Drop** unless wrapped in `<a14:m>` under `<a:p>`. | ❌ KaTeX/MathJax spans flatten to static non-editable SVG/PNG or broken spans. | ✅ Native `<a14:m><m:oMath>...</m:oMath></a14:m>` full schema control. |
| **Institutional `.potx`/`.pptx` Master Preservation** | ❌ Generates fresh master; cannot natively edit an existing university `.pptx` file in place. | ✅ Opens existing `.pptx` (`Presentation("univ_template.pptx")`), preserves masters, logos, and theme fonts. | ❌ Overwrites or ignores existing `.pptx` slide masters. | ✅ 100% fidelity preservation of university masters, animations, `.rels`, and embedded media. |

### 2.3 Declarative Markup & Academic Typesetting Frameworks

When the user explicitly requests a `.pdf` or live-code web deck rather than an editable `.pptx`, four text-first engines dominate technical academia:

| Framework | Core Syntax & Compiler | Compile Speed | Math & Vector Diagram Fidelity | `.pptx` Export Fidelity | Optimal Academic Use Case |
|:---|:---|:---|:---|:---|:---|
| **`Typst + Touying`** | Typst markup (Rust single-binary CLI `typst compile`) | **Instant** ($< 0.1\text{ s}$) | **First-class** native math (`$ sum_(i=1)^n x_i $`) + `CeTZ` / `Fletcher` commutative diagrams & `#pause` / `#meanwhile` subslides. | ❌ Native PDF/SVG/PNG only (requires PDF-to-PPTX conversion if `.pptx` requested). | **Primary recommendation for pure-PDF theoretical CS, math, physics, and optimization talks**; clean syntax yields near-zero LLM compile errors. |
| **`LaTeX Beamer`** | $\LaTeX$ (`xelatex` / `lualatex` for CJK `ctexbeamer`) | **Slow** ($3\text{--}25\text{ s}$, multi-pass) | **Gold standard** (`amsmath`, `tikz`, `pgfplots`, `algorithm2e`, `biblatex`). | ❌ PDF only (tools like `pdf2pptx` rasterize pages into non-editable images). | Mandatory only when a venue, advisor, or department strictly requires an official `.tex` Beamer template. |
| **`Slidev`** | Markdown + Vue 3 + UnoCSS / Vite | **Fast** ($1\text{--}3\text{ s}$ HMR; Playwright export slower) | **High** (KaTeX math, Mermaid, Shiki syntax highlighting with line-by-line morphing `v-click` / Magic Move). | ⚠️ `--format pptx` exports each slide as a **flat raster screenshot** inside `.pptx` (non-editable text!). | Live software engineering demos, PL/compiler code walkthroughs, interactive web visualizations in browser. |
| **`Marp` (`marp-cli`)** | CommonMark Markdown + CSS directives | **Fast** ($< 1\text{ s}$) | **Moderate** (KaTeX / MathJax). Lacks multi-card spatial primitives without custom inline HTML/CSS. | ⚠️ `--pptx` exports static background images unless `--pptx-editable` (experimental LibreOffice conversion) is used. | Rapid 5-minute Markdown-to-PDF seminar notes or lightweight internal reading-group drafts. |

### 2.4 Academic Research Systems & Benchmarks (Paper-to-Slide / Poster Literature)

Modern academic research on automated scientific slide and poster synthesis establishes key architectural patterns integrated into `cs-report-ppt`:

1. **`DOC2PPT` (Fu et al., AAAI)**: Framed scientific document-to-slide generation as hierarchical seq2seq summarization + cross-modal figure retrieval, proving that **figure-text alignment**—not text summarization alone—determines slide utility, while exposing that end-to-end neural layout regression causes chronic bounding-box collisions.
2. **`PPTAgent` & `PPTEval` (Zheng et al., EMNLP / `icip-cas/PPTAgent`)**: Replaced monolithic one-shot generation with a two-stage **Analyze $\rightarrow$ Code-Action Edit $\rightarrow$ Self-Correct** workflow, demonstrating that **ROUGE/BLEU text overlap metrics anti-correlate with slide quality** (rewarding copy-pasted text walls). Introduced **`PPTEval`**, scoring rendered slide images via VLMs across three orthogonal axes:
   - **Content**: Faithfulness to source metrics, conciseness, zero hallucinated numbers.
   - **Design**: Spatial equilibrium, zero overlap/overflow, high visual-to-text ratio, typographic contrast.
   - **Coherence**: Logical progression across sections, contextual headers/trackers, consistent visual grammar.
3. **`Paper2Poster` (Pang et al., NeurIPS / `Paper2Poster/Paper2Poster`)**: Introduced **`PosterAgent`**, combining: (a) a multimodal PDF **Parser** building a grounded figure/table/text asset bank, (b) a binary-tree spatial **Planner** matching asset aspect ratios to panel capacities, and (c) a **Painter–Commenter VLM Loop** that executes layout code, renders panels to images, diagnoses overflow or dead whitespace via vision critiques, and iteratively adjusts coordinates.
4. **`AutoPresent` & `SlidesBench` (Ge et al., CVPR 2025)**: Demonstrated on 7,000+ slide-program pairs that generating executable Python layout programs (`SlidesLib` abstractions over `python-pptx`) paired with **snapshot-based visual self-refinement** dramatically outperforms direct image-diffusion slide generation (which corrupts text and prevents user editing).
5. **`PresentAgent` / `Paper2Slides` (ACL / RAG-Grounded Pipelines)**: Emphasized fine-grained cross-reference grounding—explicitly linking slide claims to exact paper subfigures (`Fig. 3b`, `Table 2, Row 4`) and synchronizing visual callouts with spoken presenter scripts so slides never duplicate the speaker's verbatim monologue.

---

## 3. Cognitive & Visual Design Principles for Academic Slides

Every generated deck must obey the four canonical laws of scientific visual communication, translated below into deterministic agent constraints:

### 3.1 The Four Foundational Authorities

1. **Michael Alley's Assertion–Evidence (AE) Structure**:
   - **Rule**: Replace generic *Topic–Subtopic* titles (`"Experimental Results"`, `"Methodology"`, `"实验结果"`) with **declarative, conclusion-first Assertion Headlines** ($\le 14$ English words or $\le 26$ Chinese characters) stating the slide's core empirical or theoretical takeaway, supported beneath by **Visual Evidence** (authentic paper figure, schematic, equation block, or focal table) rather than bulleted prose paragraphs.
   - **Exception**: Title/Overview slides (Slide 1) and section divider headers use clean title-case paper/section titles paired with a 1-line assertion subtitle.
2. **Jean-luc Doumont's Signal-to-Noise Engineering (*Trees, Maps, and Theorems*)**:
   - **Rule**: Slides are scanned **globally in $< 3\text{ seconds}$**, not read linearly like journal pages. Maximize signal-to-noise ratio by: (a) segregating structural navigation (`Category Badge` + `Slide X / N` tracker above a thin `1pt` hairline rule at $Y = 1.50''$) from content cards ($Y \in [1.65'', 6.85'']$), (b) banning repetitive decorative chrome, clip-art icons, 3D bevels, and heavy drop shadows, and (c) enforcing visual parallelism across multi-column cards (identical header heights, bullet counts, and grammatical lead-ins).
3. **Patrick Winston's Single Language-Processor Constraint (*MIT How to Speak*)**:
   - **Rule**: Humans possess **one verbal language processor**. If a slide contains full-paragraph sentences (> 25 words per bullet), the audience reads the screen and tunes out the speaker.
   - **Operational Mandates**:
     - **Micro-Bullets Only**: Use telegraphic `**Bold Lead-In**: Quantified mechanism/verdict` fragments ($\le 14\text{--}18$ words per bullet, max 3–4 bullets per card).
     - **Eliminate "Laser Pointer Crimes"**: Bake visual attention guides directly onto diagrams and tables (subtle highlight boxes, `✦ PROPOSED` badges, bolded SOTA cells, explicit `Fig. 2b` callout references).
     - **Ban Dead `"Thank You / Q&A"` Final Slides**: Never waste the final frame (which remains projected during the entire 5–15 min Q&A) on `"Thank You! Questions?"`. Always close on a high-density **Contributions Summary + Forward Discussion Prompts / Lab Roadmap** slide.
4. **Edward Tufte's Data-Ink Ratio & Analytical Rigor (*The Cognitive Style of PowerPoint*)**:
   - **Rule**: Never dumb down scientific causality into nested 4-level bullet hierarchies. Preserve high-resolution empirical evidence: show exact sample sizes ($N$), units, error bars / standard deviations ($\pm \sigma$), relative/absolute deltas ($\Delta +4.8\%$, $2.8\times$ speedup), and explicit baseline conditions.

### 3.2 Assertion–Evidence Headline Transformation Rules

| ❌ Topic-Label Anti-Pattern (Banned) | ✅ Assertion–Evidence Slide Title + Subtitle (Required) |
|:---|:---|
| `Background and Motivation` | **Title**: `KV Cache Memory Bottlenecks Long-Context Decoding Before Compute Saturates`<br>*Subtitle*: `Standard MHA scales linearly with sequence length, exhausting 80GB VRAM at 128K tokens (Fig. 1).` |
| `System Architecture` | **Title**: `Low-Rank Joint KV Compression Cuts Cache Footprint by 73% via Decoupled RoPE`<br>*Subtitle*: `Three-stage latent projection preserves positional sensitivity while compressing cached states (Fig. 3).` |
| `Ablation Study` | **Title**: `Decoupled Positional Queries Drive +3.2% MMLU Gain Over Naive Latent Pooling`<br>*Subtitle*: `Component-wise ablations confirm rank d_c = 128 saturates quality across 7B–67B scales (Table 3).` |
| `实验结果与对比分析` (Topic Label) | **Title**: `解耦潜注意力在 6 大推理基准上超越稠密 MHA 且吞吐提升 2.8 倍`<br>*Subtitle*: `Table 1 主实验：仅保留 27% 键值缓存即实现 +1.9% GSM8K 增益` |
| `总结与致谢 / Thank You!` | **Title**: `Core Contributions, Open Scaling Boundaries & 3-Week Lab Verification Roadmap`<br>*Subtitle*: `Summary of validated speedups, unverified FP4 quantization limits, and immediate reproduction milestones.` |

### 3.3 Quantitative Slide Density & Visual Coverage Budgets

| Metric / Element | Hard Operational Bound | Anti-Pattern Triggering Refactor |
|:---|:---|:---|
| **Deck Visual Coverage** | **$\ge 80\%$ of slides** (e.g., $\ge 11/14$) contain an authentic figure, vector diagram, equation block, or data table | $> 20\%$ pure-text card slides $\rightarrow$ harvest missing PDF plots or construct native DrawingML taxonomy/pipeline diagrams. |
| **Slide Headline Length** | **1 line** ($\le 75\text{ EN chars}$ / $\le 14\text{ words}$; $\le 28\text{ CN chars}$) at `22–26pt Bold` | Wrapping onto 2+ lines and colliding with subtitle at $Y = 1.08''$ $\rightarrow$ tighten verb phrase. |
| **Total Prose Words per Slide** | **$35\text{--}85\text{ EN words}$** ($60\text{--}140\text{ CN chars}$), excluding figure/table internal labels | $> 110\text{ EN words}$ (teleprompter wall) or $< 20\text{ words}$ without full-bleed hero visual (vacant slide). |
| **Bullets per Card** | **$2\text{--}4\text{ bullets}$** (strictly **zero** sub-bullets / level-2 nesting) | $\ge 5$ bullets or nested `◦` / `▪` lists $\rightarrow$ split into 2 cards or convert into a structured comparison table. |
| **Length per Bullet** | **$\le 18\text{ EN words}$ / $\le 120\text{ chars}$** ($\le 45\text{ CN chars}$), ideally 1–2 rendered lines | 4-line paragraph bullets $\rightarrow$ rewrite as `**Lead Term**: Concise metric + subfigure anchor`. |
| **Display Equations per Slide** | **$1\text{--}2\text{ master equations}$** in `<m:oMathPara>` + symbol glossary / intuition line | Dumping 6–8 multi-line proof steps (`\begin{align}` wall) $\rightarrow$ show master objective + 1 key update rule; move derivation steps to Backup Slides. |
| **Native Table Dimensions** | **$\le 8\text{ rows} \times \le 7\text{ columns}$** at `>= 10.5pt` font | Copying a 35-row $\times$ 14-column paper leaderboard verbatim $\rightarrow$ curate top 3 baselines + SOTA competitor + Proposed + $\Delta$ row. |
| **Card Occupancy Ratio** | **$70\%\text{--}88\%$** of card interior height filled purposefully | $< 50\%$ occupancy (giant dead white void at bottom of card) or $> 95\%$ (text touching bottom border). |

---

## 4. Deterministic Engine Selection Matrix & Routing Rules

Before writing a single line of slide generation code, the agent must select the execution track using this deterministic decision matrix:

```
User Request & Environment Check
 ├── Does user explicitly demand PDF-only / LaTeX / Typst slides?
 │    ├── User specifies University .tex Beamer template ──► Track D2: LaTeX Beamer (xelatex)
 │    └── Otherwise (fast math/theory PDF deck) ───────────► Track D1: Typst + Touying (<0.1s compile)
 ├── Does user explicitly demand interactive browser / live-code web slides?
 │    └── Yes ─────────────────────────────────────────────► Track E: Slidev / Marp HTML
 ├── Did user supply an existing institutional .pptx / .potx master to populate?
 │    └── Yes ─────────────────────────────────────────────► Track C: OOXML Template Surgery / python-pptx Master Mode
 └── Standard Editable .pptx Deliverable (Default for 95% of academic talks)
      ├── Node.js + pptxgenjs available (or cs-report-ppt accelerator present)?
      │    └── Yes ────────────────────────────────────────► Track A (PRIMARY): PptxGenJS + latex_to_omml.py + PyMuPDF
      └── Node.js unavailable (Pure Python Conda environment only)?
           └── Yes ────────────────────────────────────────► Track B (FALLBACK): python-pptx + <a14:m> OMML Injector + PyMuPDF
```

### Engine Routing Reference Table

| Track | Stack Components | Environment Execution Rule | Primary Strengths & Mandatory Guardrails |
|:---|:---|:---|:---|
| **Track A (Primary Default)** | `PptxGenJS` (`build_deck.js` or custom `.js`) + `latex_to_omml.py` + `crop_figures.py` (`PyMuPDF` + `Pillow`) | Run Node script + Python post-injector inside user's existing Conda environment (**never** create `venv`/`.venv` or stray `requirements.txt`). | Cleanest JSON/JS coordinate control (`13.333'' x 7.500''`), native `sizing: { type: 'contain' }`, crisp vector flowcharts, and full Phase-2 native `<a14:m>` OMML equation injection. |
| **Track B (Pure-Python Fallback)** | `python-pptx` + `latex_to_omml.py` (`inject_omml_into_pptx`) + `PyMuPDF` + `Pillow` | Activate appropriate local Conda environment (`conda run -n <env> python ...`); zero local virtualenvs. | Zero Node.js dependency. **Guardrail**: Always write `<<MATH_DISPLAY:...>>` / `<<MATH_INLINE:...>>` text placeholders first and run `inject_omml_into_pptx()` on the saved `.pptx`—never append raw `<m:oMath>` directly inside `<a:r>` via `python-pptx`. Always compute isotropic image dimensions from `PIL.Image.size` before calling `add_picture()`. |
| **Track C (Template / Master Surgery)** | `python-pptx` (existing `.pptx` load) or Direct ZIP OOXML Unpack + `latex_to_omml.py` | Read-only inspect `ppt/slideLayouts/*.xml` and render template thumbnails before editing. | Preserves university crests, NSFC/defense master headers, and custom theme fonts. **Guardrail**: Strip unused default bullet placeholders (`sp._element.getparent().remove(sp._element)`) so ghost `"Click to add text"` boxes never leak. |
| **Track D1/D2 (Typeset PDF)** | `Typst + Touying` (`typst compile`) or `LaTeX Beamer` (`xelatex -interaction=nonstopmode`) | Verify `typst --version` or `xelatex --version` with explicit command timeouts. | Ideal for pure-math colloquia with commutative diagrams (`Fletcher`/`TikZ`) and step-by-step proof reveals (`#pause`). Still requires **Stage 4 PNG rasterization via `PyMuPDF` + Vision QA**! |
| **Track E (Web / Live Code)** | `Slidev` or `Marp CLI` | Use only when interactive browser execution or live code-runner widgets are explicitly requested. | Never silently deliver flat screenshot-exported `.pptx` from `Slidev`/`Marp` when the user asked for an editable PowerPoint presentation. |

---

## 5. High-DPI Figure & Table Harvesting & True Aspect-Ratio Preservation

Authentic empirical visuals are the backbone of an academic presentation ($\ge 80\%$ slide coverage). Low-resolution screenshots, clipped axis labels, or stretched aspect ratios immediately destroy scholarly credibility.

### 5.1 Three-Tier PDF Visual Harvesting Protocol

#### Tier 1: Automated Caption-Anchored Vector + Raster Clustering (`crop_figures.py --auto`)
1. **Caption Detection**: Scan `page.get_text("blocks")` in `PyMuPDF` (`pymupdf`) for bilingual caption anchors:
   - English: `^(Figure|Fig\.|Table|Algorithm)\s*([0-9]+|[A-Z][0-9]*)\s*[:.]`
   - Chinese: `^(图|表|算法)\s*([0-9]+|[A-Z]?[0-9]+(?:-[0-9]+)?)\s*[:：.\s]`
2. **Header/Footer Rule Filtering**: Discard horizontal page rules and running headers where $y_1 < 45\text{ pt}$ or $y_0 > H_{\text{page}} - 45\text{ pt}$, or hairline dividers ($h < 1.0\text{ pt}, w > 0.7 W_{\text{page}}$ near page extrema).
3. **Column-Aware Spatial Clustering**:
   - Determine whether the caption spans both columns ($W_{\text{cap}} > 0.45 W_{\text{page}}$ or crosses $x \in [0.25 W_{\text{page}}, 0.75 W_{\text{page}}]$) or sits inside a single column.
   - Collect all vector paths (`page.get_drawings()`) and embedded raster xrefs (`page.get_image_rects(xref)`) within the vertical search horizon ($450\text{ pt}$ above caption for figures; both below and above caption for tables since IEEE/ACM/LaTeX place table captions above while some journals place them below).
   - For tables, union internal `page.get_text("blocks")` inside the table envelope so vector rule lines and text cells are captured completely without clipping outer columns.
4. **300–400 DPI Pixmap Rasterization & Margin Trimming**:
   - Native PDF points operate at $72\text{ DPI}$. Always render clipped regions at **`dpi=300` minimum** (`dpi=400` for small single-column plots or dense microscopy/circuit schematics):
     ```python
     pix = page.get_pixmap(dpi=350, clip=bbox_rect, alpha=False)
     ```
   - Strip uneven PDF margins via `Pillow` grayscale inversion (`ImageOps.invert(img.convert("L")).getbbox()`) and restore a uniform **`10–14 px` clean white border** so subfigure labels `(a)`, `(b)` and axis ticks never touch card strokes.
   - Strip the paper's verbose multi-line prose caption (`"Figure 3: Overview of our proposed..."`) from the cropped image itself—captions belong synthesized inside slide bullets and headers, not rendered as tiny `6pt` unreadable text beneath the graphic!

#### Tier 2: VLM-Guided Manual Coordinate Refinement (`crop_figures.py --page P --bbox ...`)
Auto-clustering can miss **captionless teaser figures on Page 1**, **multi-panel figures split by whitespace $> 30\text{ pt}$**, or **algorithm pseudocode boxes**.
1. Render key PDF pages at `150 DPI` full-page previews and inspect them visually with `view_file`.
2. Identify exact normalized `[x0, y0, x1, y1]` $\in [0, 1]^4$ or `72-pt` coordinates and re-extract cleanly:
   ```bash
   python crop_figures.py --pdf paper.pdf --page 1 --bbox "0.08,0.28,0.92,0.64" --dpi 350 --name fig1_teaser
   ```
3. Visually open every extracted `.png` asset **before** building the deck to verify: (a) zero clipped axis titles/legends, (b) zero stray body-paragraph lines leaked at top/bottom, and (c) crisp text legibility.

#### Tier 3: Complex Multi-Column / Scanned PDF Fallback (`MinerU` / `Docling`)
For scanned historical PDFs, double-column borderless economics tables, or complex supplementary PDFs where `page.get_drawings()` lacks vector rules:
- Use layout-detection bounding boxes (`Docling` RT-DETRv2 or `MinerU` `PDF-Extract-Kit`), **snap normalized coordinates back to native 72-pt PDF page dimensions** ($\text{Rect}_{\text{pt}} = [x_0 W_p, y_0 H_p, x_1 W_p, y_1 H_p]$), and still perform the final crop at `300+ DPI` via `PyMuPDF` to avoid neural-resizer aspect distortion.

### 5.2 Aspect-Ratio Classification & Zero-Distortion Adaptive Layout Math

Every harvested asset emits `width_px`, `height_px`, and true aspect ratio $R = W_{\text{px}} / H_{\text{px}}$ into `figures_metadata.json`. **Layout selection must follow $R$, never force-fit $R$ into an incompatible card**:

| Geometry Class | Aspect Ratio $R = W / H$ | Typical Academic Examples | Mandatory Slide Layout Mapping |
|:---|:---|:---|:---|
| **Ultra-Wide Panorama** | $R > 2.20$ | End-to-end multi-stage transformer pipeline, 5-column qualitative frame strip, wide timeline | **`asymmetric_2row`** (Top full-width hero card $12.133'' \times 2.45''\text{--}2.90''$ + Bottom 2–3 analytical takeaway cards) or full `hero_1col` top band. **Never** squeeze into a narrow $4.1''$ or $5.9''$ column! |
| **Standard Landscape** | $1.35 \le R \le 2.20$ | Architecture diagram, Pareto throughput-accuracy plot, multi-line loss curves | **`split_65_35`** (Left $65\%$ visual card $7.700'' \times 5.200''$ + Right $35\%$ mechanism breakdown or Lab Synergy callout $4.133'' \times 5.200''$). |
| **Square / Balanced** | $0.85 \le R < 1.35$ | Confusion matrix, t-SNE/UMAP manifold, 2x2 subfigure ablation grid, radar chart | **`split_equal_2col`** (Left $5.916'' \times 5.200''$ figure card + Right $5.916'' \times 5.200''$ mathematical formulation or empirical dissection card). |
| **Portrait / Tall Vertical** | $R < 0.85$ | Vertical residual block stack, clinical CONSORT flowchart, tall microscopy column | **Asymmetric Left-Tall Split** ($4.60''\text{--}5.20'' \times 5.200''$ left image container paired with 2 vertically stacked right-hand cards $6.633'' \times 2.475''$ each). |

#### Isotropic Containment Scaling Equations (Mandatory in Every Builder)
Given an available interior image zone $(X_{\text{zone}}, Y_{\text{zone}}, W_{\text{zone}}, H_{\text{zone}})$ inside a card (after subtracting card header height and padding $P_x, P_y \ge 0.20''$) and native pixel dimensions $(W_{\text{px}}, H_{\text{px}})$ with $R = W_{\text{px}} / H_{\text{px}}$:

$$W_{\text{render}} = \min\left(W_{\text{zone}},\; H_{\text{zone}} \cdot R\right), \qquad H_{\text{render}} = \frac{W_{\text{render}}}{R}$$

$$X_{\text{render}} = X_{\text{zone}} + \frac{W_{\text{zone}} - W_{\text{render}}}{2}, \qquad Y_{\text{render}} = Y_{\text{zone}} + \frac{H_{\text{zone}} - H_{\text{render}}}{2}$$

- **In `PptxGenJS`**: Either pass the exact pre-computed `{ x: X_render, y: Y_render, w: W_render, h: H_render }` OR use `sizing: { type: 'contain', w: W_zone, h: H_zone }`. **Never** pass arbitrary `w` and `h` without `contain`, and **never** use `sizing: { type: 'cover' }` on scientific figures (which crops off axis ticks and legends).
- **In `python-pptx`**: Always read `(w_px, h_px) = PIL.Image.open(img_path).size`, compute `W_render` and `H_render` in inches via the equations above, and pass `Inches(X_render), Inches(Y_render), width=Inches(W_render), height=Inches(H_render)` (where `W_render / H_render == w_px / h_px` to within $10^{-4}$).
- **Dead-Space Guardrail**: If $W_{\text{render}} \cdot H_{\text{render}} < 0.55 \cdot (W_{\text{zone}} \cdot H_{\text{zone}})$, the card geometry mismatches the figure's aspect ratio—switch layout models immediately rather than leaving $> 45\%$ blank whitespace inside the image card.

### 5.3 Cropped PDF Table vs. Native Redesigned DrawingML Table Rule

| Table Source Scenario | Actionable Engineering Rule |
|:---|:---|
| **Focal SOTA or Ablation Table ($\le 8$ rows $\times \le 7$ cols)** | **Rebuild as a Native Editable PPTX Table** (`slide.addTable` / `add_table`) at `11–12pt` font: dark header fill (`#000000` or theme `primary`), subtle zebra striping (`#F9FAFB`), **bold** best metric, underlined runner-up, and an explicit rightmost or bottom **$\Delta$ Gain** column (`+4.8%`, `2.8x`). |
| **Massive 20–45 Row Paper Leaderboard / Regression Dump** | **Never crop and paste the full wall** (produces unreadable `5pt` micro-text). Extract and curate 5–7 representative rows (classic anchor baseline + top 2–3 prior SOTA methods + Proposed + $\Delta$) into a clean native table, adding a footer note: *`Selected from 18 baselines in Table 1; full suite in Backup Slide B2.`* |
| **Complex Visual-Embedded Table** (inline sparklines, chemical structures, multi-level rotated headers with $\le 10$ rows) | **Harvest at 350–400 DPI** via `crop_figures.py` only if rendered cell text visually exceeds an effective `11pt` equivalent on the $13.333''$ canvas during Stage 4 Vision QA. |

---

## 6. Native Editable OMML Mathematical Formula Architecture

Academic audiences judge rigor through notation precision. Embedding equations as raster PNGs causes blurry pixelation on 4K auditorium projectors, clashes with slide fonts, and prevents collaborators from editing symbols; raw Unicode strings (`L_total = 1/N sum l_i(theta)`) collapse on fractions, matrices, limits, and multi-level subscripts.

### 6.1 OpenXML DrawingML 2010 Math Specification (`<a14:m>`)

In PowerPoint OpenXML (`ppt/slides/slideN.xml`), native editable equations live inside DrawingML paragraphs (`<a:p>`) wrapped in the Office 2010 DrawingML Math extension `<a14:m>`:

1. **Required Namespaces**:
   - `xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"`
   - `xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main"`
   - `xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"`
2. **Critical Structural Rule (Avoiding PowerPoint's "Silent Drop" Bug)**:
   - `<a14:m>` **MUST be a direct child of `<a:p>`** (a sibling of `<a:r>` text runs), **NEVER** nested inside `<a:r>` or `<a:t>`! Nesting `<m:oMath>` inside `<a:r>` causes desktop PowerPoint to silently delete the equation or trigger a file-corruption repair prompt.
   - **Inline Math** (`$x_t \in \mathbb{R}^d$` inside a bullet): `<a:p>` contains preceding `<a:r>`, followed by `<a14:m><m:oMath>...</m:oMath></a14:m>`, followed by trailing `<a:r>`.
   - **Display / Block Math** (standalone centered master objective): `<a:p>` contains `<a:pPr algn="ctr"/>` and `<a14:m><m:oMathPara><m:oMath>...</m:oMath></m:oMathPara></a14:m>`.

### 6.2 Two-Phase Placeholder & AST Injection Pipeline (`latex_to_omml.py`)

Both Track A (`PptxGenJS`) and Track B (`python-pptx`) share the exact same **Two-Phase Math Architecture**:

1. **Phase 1 — Layout Generation with Tagged Math Placeholders & Dynamic Height Budgeting**:
   - Inline expressions inside bullets/text are tagged as `<<MATH_INLINE:\mathbf{x}_t \in \mathbb{R}^{B \times L \times D}>>` (or `$...$`, normalized by the builder).
   - Standalone display equations are written into dedicated equation boxes tagged as `<<MATH_DISPLAY:\mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^N \ell_i(\boldsymbol{\theta}) + \lambda \|\boldsymbol{\theta}\|_2^2>>`.
   - **Dynamic Vertical Height Allocation** (preventing formula-to-caption collisions): Tall 2D operators expand line height far beyond standard `14pt` single-line text. Always reserve vertical box height $H_{\text{eq}}$ (in inches) before advancing `currentY`:
     $$H_{\text{eq}}(\text{latex}) = \min\Big(1.55'',\; 0.58'' + 0.42'' \cdot \mathbb{I}[\text{has }\mathtt{\backslash frac, \backslash sum, \backslash prod, \backslash int}] + 0.28'' \cdot \mathbb{I}[\text{has }\mathtt{\backslash sqrt, \backslash left, \backslash begin\{*matrix\}}] + 0.22'' \cdot \mathbb{I}[\text{len} > 75]\Big)$$
   - Immediately beneath each display equation, allocate a dedicated `0.35''–0.45''` **Physical Intuition / Term Glossary** callout (`💡 Intuition: First term enforces reconstruction fidelity; second term bounds spectral norm`) so equations never float unanchored.

2. **Phase 2 — In-Place ZIP XML AST Replacement (`latex_to_omml.py --inject`)**:
   - Unpack `stage1.pptx` into a temporary directory, parse every `ppt/slides/slide*.xml`, locate `<a:r>` runs matching `<<MATH_(INLINE|DISPLAY):...>>`, split surrounding text into clean `<a:r>` siblings preserving original `<a:rPr>` font properties, compile the $\LaTeX$ string via recursive-descent AST (`Fraction -> <m:f>`, `NaryOp -> <m:nary>`, `SubSuperscript -> <m:sSubSup>`, `Delimiter -> <m:d>`, `Radical -> <m:rad>`, `Accent -> <m:acc>`, `Matrix -> <m:m>`), escape XML entities (`&amp;`, `&lt;`, `&gt;`), insert `<a14:m>`, and repackage into the final `.pptx`.
   - **Alternative Converter Fallback**: For exotic $\LaTeX$ macros not covered by `latex_to_omml.py`, simplify the macro into standard `amsmath` primitives (`\frac`, `\sum`, `\mathbf`, `\mathbb`, `\mathcal`, `\begin{bmatrix}`) rather than falling back to raw unparsed backslash strings.

---

## 7. LibreOffice + PyMuPDF Multimodal Vision-in-the-Loop QA Protocol

> **Core Invariant**: Programmatic XML validation ([`scripts/verify_deck.py`](../scripts/verify_deck.py)) is **necessary but never sufficient**. XML validators cannot see CJK line-wrap widows, overlapping OMML integral bounds, clipped figure legends, low-contrast pastel text, or awkward half-empty cards. **Every generated deck MUST be rendered to PNG images and inspected slide-by-slide with the agent's own multimodal vision tool (`view_file` / `read_file`).**

### 7.1 Two-Stage Headless Rendering Pipeline (`PPTX -> PDF -> 150–200 DPI PNG`)

Direct `soffice --convert-to png` only exports Slide 1 and degrades typography. Always execute the deterministic **two-hop pipeline** (`PPTX -> PDF` via headless LibreOffice Impress, followed by `PDF -> PNG` via `PyMuPDF` `fitz`):

```python
import os, subprocess, tempfile, shutil
import pymupdf  # PyMuPDF

def render_deck_for_vision_qa(pptx_path: str, out_dir: str, dpi: int = 160) -> list[str]:
    """Converts PPTX -> PDF via isolated headless LibreOffice, then renders 160 DPI slide PNGs."""
    os.makedirs(out_dir, exist_ok=True)
    soffice_bin = (
        r"C:\Program Files\LibreOffice\program\soffice.exe"
        if os.name == "nt" and os.path.exists(r"C:\Program Files\LibreOffice\program\soffice.exe")
        else "soffice"
    )
    # Isolated temporary UserInstallation prevents zombie soffice.bin lockups under parallel runs
    profile_dir = tempfile.mkdtemp(prefix="libo_qa_")
    profile_uri = "file:///" + profile_dir.replace("\\", "/").lstrip("/")
    try:
        cmd = [
            soffice_bin,
            "--headless",
            "--norestore",
            "--nolockcheck",
            f"-env:UserInstallation={profile_uri}",
            "--convert-to", "pdf",
            "--outdir", out_dir,
            pptx_path,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if res.returncode != 0:
            raise RuntimeError(f"LibreOffice headless conversion failed: {res.stderr}")

        stem = os.path.splitext(os.path.basename(pptx_path))[0]
        pdf_path = os.path.join(out_dir, f"{stem}.pdf")
        doc = pymupdf.open(pdf_path)
        png_paths = []
        for idx, page in enumerate(doc):
            pix = page.get_pixmap(dpi=dpi, alpha=False)
            img_path = os.path.join(out_dir, f"slide_{idx + 1:02d}.png")
            pix.save(img_path)
            png_paths.append(img_path)
        doc.close()
        return png_paths
    finally:
        shutil.rmtree(profile_dir, ignore_errors=True)
```

### 7.2 Cross-Platform Font, CJK & Math Rendering Safeguards

Headless rendering fidelity depends on font metrics matching between authoring code and `soffice`:
1. **Isolated User Profile & Timeout**: Always pass `-env:UserInstallation=file:///...` and `timeout=60` so concurrent agent tasks never hang on a locked default LibreOffice profile.
2. **CJK Tofu (`□□□`) Prevention**: On Windows, `Microsoft YaHei` (`微软雅黑`), `SimHei`, `Arial`, `Segoe UI`, and `Cambria Math` are present natively. On headless Linux/Docker containers, verify `fc-list :lang=zh` includes `Noto Sans CJK SC` / `Source Han Sans SC` (`fonts-noto-cjk`) and `libreoffice-math` + `Liberation Sans` / `STIX Two Math` so Chinese characters and OMML operators (`∑`, `∫`, `ℝ`, `ℒ`) never render as blank boxes.
3. **Font Metric Expansion Buffer**: Linux fallback fonts (`Liberation Sans` substituting for `Arial`, `Noto Sans CJK` substituting for `Microsoft YaHei`) can run **5–8% wider** horizontally than Windows fonts. Always leave a **`0.15''–0.20''` safety buffer** on right text-box edges and single-line headlines so slides remain wrap-safe across Windows, macOS, and Linux projectors.

### 7.3 Closed-Loop 4-Gate Vision Self-Inspection & Repair Protocol

```
Gate 1: Programmatic XML Audit (verify_deck.py)
  • Valid ZIP/OOXML, exact 16:9 EMU (12192000 x 6858000), expected slide count
  • Zero raw math token leaks (<<MATH_, {{MATH:, [[MATH_, raw $$, \frac, \sum)
  • Zero out-of-canvas shapes (x >= 0, y >= 0, x + w <= 13.333", y + h <= 7.500")
        │
        ▼
Gate 2: High-DPI Rasterization (150–200 DPI PNGs + Optional Contact-Sheet Grid)
  • Export PDF + slide_01.png ... slide_NN.png via LibreOffice + PyMuPDF
  • Sanity check every page: file size > 15 KB, non-empty extracted PDF text
        │
        ▼
Gate 3: Multimodal Pixel Audit (Agent calls view_file on EVERY slide_XX.png)
  • Inspect every individual slide image against the 25-Point Defect Checklist
  • Inspect cross-slide rhythm: >= 80% visual coverage, layout diversity (no 3 identical consecutive layouts)
        │
        ├── Any Defect Found ──► Gate 4: Root-Cause Coordinate/Prose Surgery
        │                          • Text overflow/collision -> cut prose 20-30% or increase box h (never shrink body < 11pt!)
        │                          • Figure letterboxed/tiny -> re-crop margins or switch layout model to match R = W/H
        │                          • Formula overlap -> expand eqH (+0.30" to +0.45") & re-inject OMML
        │                          • Re-run Gate 1 -> Gate 2 -> Gate 3 on modified slides until 0 defects
        ▼
Zero Defects Verified ──► Final Delivery (.pptx + .pdf + Rendered Slide Gallery)
```

---

## 8. The 25-Point Visual & Structural Defect Audit Checklist

Before marking any presentation deliverable complete, the agent must audit the deck against all **25 binary pass/fail criteria** across five structural and visual dimensions:

### Category A: Canvas Geometry, Boundaries & Spatial Collisions (01–05)

| # | Audit Checkpoint | Check Mode | Defect Symptom | Pass Threshold & Exact Remediation |
|:---|:---|:---|:---|:---|
| **01** | **16:9 Widescreen Canvas Conformance** | XML + Vision | 4:3 pillarboxed slides or mismatched master dimensions. | Exact $13.333'' \times 7.500''$ (`12,192,000 x 6,858,000 EMU`) across 100% of slides. Fix `defineLayout` / `slide_width`. |
| **02** | **Canvas Margin & Bleed Containment** | XML + Vision | Cards, footnotes, or arrows clipped at slide edges or violating margins. | All content strictly inside $X \in [0.50'', 12.833'']$, $Y \in [0.20'', 7.38'']$. Recompute `x + w` and `y + h`. |
| **03** | **Header Zone Non-Collision** | Vision (`view_file`) | Multi-line slide title wraps downward onto italic subtitle ($Y = 1.08''$) or divider rule ($Y = 1.50''$); title collides with top-right `XX / NN` tracker. | Clear $\ge 0.06''$ vertical gap between tracker, 1-line title, subtitle, and hairline divider. Shorten headline to $\le 14$ EN words / $\le 28$ CN chars. |
| **04** | **Inter-Element Vertical & Horizontal Clearance** | Vision (`view_file`) | Card body bullets overlap embedded figures, tables, OMML equations, or footer citation ($Y = 7.00''$). | Minimum $0.20''\text{--}0.30''$ gap between adjacent cards and $\ge 0.12''$ internal vertical clearance between card elements. |
| **05** | **Ghost Placeholder & Orphan Shape Hygiene** | XML + Vision | Default template `"Click to add title"` text boxes, empty bordered cards, or stray connector lines visible. | Zero unpopulated shapes or template placeholder leaks. Remove unused layout shapes programmatically. |

### Category B: Typography, Hierarchy, Bilingual CJK-Latin & Readability (06–10)

| # | Audit Checkpoint | Check Mode | Defect Symptom | Pass Threshold & Exact Remediation |
|:---|:---|:---|:---|:---|
| **06** | **Minimum Auditorium Font Floor** | XML + Vision | Auto-shrunk `7–9pt` micro-bullets or unreadable tiny footnotes. | Title `22–28pt`, Subtitle `14–16pt`, Card Header `15–18pt`, Body Bullets `>= 12pt` (`11pt` absolute floor for dense tables), Tracker/Footer `9.5–10.5pt`. Prune text instead of shrinking font! |
| **07** | **Assertion–Evidence Headline Compliance** | Vision + Text | Vague topic headers (`"Introduction"`, `"Results"`, `"方法介绍"`). | Every content slide headline states a concrete, verb-driven claim or empirical verdict (except Slide 1 Title Overview). |
| **08** | **Telegraphic Micro-Bullet Discipline** | Vision + Text | 4–6 line prose paragraphs copied from paper abstract/method, or 3-level nested sub-bullets. | $2\text{--}4$ top-level bullets per card, zero nested sub-bullets, `**Bold Lead-In**: Concise empirical statement` ($\le 2$ lines per bullet). |
| **09** | **CJK–Latin Bilingual Typography & Widow Control** | Vision (`view_file`) | Missing CJK glyphs (`□`), jarring font switches within words, punctuation starting a new line (`，`/`。` at line head), or single-character orphan last lines. | Clean CJK sans-serif (`Microsoft YaHei` / `Source Han Sans SC`) paired with `Arial` / `Segoe UI` for Latin/numbers; tighten phrasing by 2–4 chars to eliminate 1-word/2-char dangling orphan lines. |
| **10** | **WCAG AA Contrast Compliance** | Vision (`view_file`) | Light gray text on white cards, dark text on dark navy headers, or washed-out pastel badges. | Body/header text contrast ratio $\ge 4.5:1$ (prefer $\ge 7:1$, e.g., `#000000` / `#1F2937` on `#FFFFFF`, or `#FFFFFF` on `#0F2042`). |

### Category C: Figure/Table Fidelity, Aspect Ratio & Data-Ink Integrity (11–15)

| # | Audit Checkpoint | Check Mode | Defect Symptom | Pass Threshold & Exact Remediation |
|:---|:---|:---|:---|:---|
| **11** | **$\ge 80\%$ Authentic Visual Asset Coverage** | Deck Thumbnail Scan | Deck looks like a monochrome Word handout of text cards ($\ge 4$ text-only slides in a 14-slide deck). | $\ge 80\%$ of slides ($\ge 11/14$) anchored by harvested high-DPI paper figures, vector diagrams, master equations, or benchmark tables. |
| **12** | **True Aspect-Ratio Preservation (Zero Distortion)** | Vision + Metadata | Circles look oval, text inside paper diagrams looks horizontally squashed or vertically stretched. | $|(W_{\text{render}} / H_{\text{render}}) - (W_{\text{px}} / H_{\text{px}})| < 0.01$. Enforce isotropic `contain` math everywhere. |
| **13** | **300+ DPI Sharpness & Clean Crop Boundaries** | Vision (`view_file`) | Blurry/pixelated upscaled figures, clipped axis titles/legends, leaked paper body text lines, or duplicate tiny `"Figure 3: ..."` captions inside image. | Re-extract via `crop_figures.py` at `300–400 DPI` with tight caption-excluded bounding box and `10–14 px` uniform white margin. |
| **14** | **Semantic Visual–Text Anchoring** | Vision + Text | Generic bullets sitting beside a figure without referencing its panels, axes, or numbers. | Slide bullets explicitly anchor to visual coordinates (`Fig. 3b`, `orange Pareto curve`, `Row 4`, `$\Delta +4.8\%$`) and bake callout cues onto schematics. |
| **15** | **Publication-Grade Focal Table Formatting** | Vision (`view_file`) | Raw 30-row screenshot table with `5pt` text, overflowing numbers wrapping mid-digit (`94.\n2%`), or missing SOTA highlights. | Curated $\le 8 \times 7$ native table (or crisp $\ge 11\text{pt}$-equivalent crop), **bold** best metric, explicit `Δ` gain column, widened numeric columns so numbers never wrap mid-token. |

### Category D: Mathematical OMML Rigor & Notation Hygiene (16–20)

| # | Audit Checkpoint | Check Mode | Defect Symptom | Pass Threshold & Exact Remediation |
|:---|:---|:---|:---|:---|
| **16** | **Zero Unparsed Math Placeholder or $\LaTeX$ Leaks** | XML (`verify_deck.py`) + Vision | Visible `<<MATH_DISPLAY:...>>`, `{{MATH:...}}`, raw `$$`, `\frac`, `\mathcal`, or `\boldsymbol` in rendered slide text. | `0` leaked tokens in XML and PNGs. Run `latex_to_omml.py --inject` and fix any unbalanced braces in source $\LaTeX$. |
| **17** | **Native Vector OMML Editability (`<a14:m>`)** | XML (`verify_deck.py`) | Equations embedded as blurry low-DPI screenshots or flat ASCII `x_i^2` strings. | Equations encoded as `<a14:m><m:oMath>` / `<m:oMathPara>` children of `<a:p>` (or native vector math in Typst/Beamer PDF tracks). |
| **18** | **2D Operator & Matrix Vertical Breathing Room** | Vision (`view_file`) | Summation limits ($\sum_{i=1}^N$), stacked fractions, or matrices clipped at top/bottom or colliding with the `💡 Intuition` caption below. | Reserve dynamic $H_{\text{eq}} \in [0.60'', 1.55'']$ and verify clear whitespace above upper limits and below denominators. |
| **19** | **Symbol Glossary & Physical Intuition Grounding** | Vision + Text | Master loss equation dropped onto a slide without defining variables ($\boldsymbol{\theta}, \lambda, \mathcal{D}$) or explaining what each term optimizes. | Every display equation paired with a variable glossary or 1-line physical/geometric intuition annotation. |
| **20** | **Cross-Slide Notation Consistency** | Text + Vision | Slide 6 writes hidden state as $h_t$, Slide 7 writes $\mathbf{s}_t$, and Slide 8 diagram writes `H_t` without mapping. | Identical symbol, bold/tensor convention ($\mathbf{X}$ matrix, $\mathbf{x}$ vector, $x$ scalar), and subscript indexing across the entire deck. |

### Category E: Narrative Spine, Visual Balance & Anti-AI-Slop Aesthetics (21–25)

| # | Audit Checkpoint | Check Mode | Defect Symptom | Pass Threshold & Exact Remediation |
|:---|:---|:---|:---|:---|
| **21** | **Card Occupancy & Zero Dead-Space Equilibrium** | Vision (`view_file`) | Half-empty cards with 2 short lines floating above a $3.5''$ white void, or lopsided slides with 90% ink on left and 10% on right. | Every card achieves $70\%\text{--}88\%$ purposeful occupancy; switch layout grid (`asymmetric_2row` $\leftrightarrow$ `split_65_35` $\leftrightarrow$ `quadrant_2x2`) to balance visual weight. |
| **22** | **Cross-Slide Layout Rhythm & Variety** | Deck Thumbnail Scan | Monotonous repetition of the exact same 2-column card template across 6+ consecutive slides. | Never repeat the exact same `layout` geometry more than **2 consecutive slides**; alternate hero visuals, asymmetric splits, tables, and 2x2/3-col matrices. |
| **23** | **Zero AI-Slop Decorative Visuals** | Vision (`view_file`) | Neon purple-cyan gradients, glowing sci-fi brains, decorative emoji confetti (`🚀🔥✨🎯`), heavy drop shadows, or generic stock icons. | Scholarly palette discipline (`academic_mono` `#FFFFFF`/`#000000`/`#1F2937` or curated academic palette); max 1 restrained accent hue; zero decorative clip-art. |
| **24** | **Complete Scholarly Provenance & Navigation Chrome** | Vision (`view_file`) | Missing author/venue/arXiv citation on Slide 1, missing `Slide X / N` counter, or inconsistent category badges. | Slide 1 displays full paper title, authors, affiliations, venue/year, and DOI/arXiv ID; all content slides carry consistent category badge, footer citation, and `X / N` pagination. |
| **25** | **Actionable Closing Frame (No Dead `"Thank You"` Slide)** | Vision (`view_file`) | Final slide contains only `"Thank You! Questions?"` or `"感谢聆听，敬请批评指正"` in huge centered font over empty background. | Final slide anchors Q&A with synthesized contributions, honest scope/limitation boundaries, forward seminar discussion prompts, or concrete next-step milestones. |

---

## 9. Engine-to-Spine Mapping & Pure-Python (`Track B`) Reference Implementation

### 9.1 Mapping the 14-Slide Baseline Spine to Optimal Engine Primitives

To prevent agents from defaulting to homogeneous bullet cards or screenshotting everything blindly, each slot of the standard 14-slide academic spine maps to a primary OpenXML object class:

| Slide # | Spine Role | Primary Engine Primitive | Expected Asset Geometry $R = W/H$ | Mandatory Engine & Vision Verification |
|:---|:---|:---|:---|:---|
| **01** | Paper Overview & Citation Hero | Harvested Teaser Figure (`<p:pic>`) + Metadata Grid (`<p:sp>`) | $1.35 \le R \le 2.40$ | Verify full title, authors, venue/year, DOI/arXiv ID, and crisp 350 DPI teaser graphic without title wrap collision. |
| **02** | Motivation & Prior Failure Modes | Harvested Qualitative Failure Samples (`<p:pic>`) + `[State Memory / Adaptivity]` Callout | $1.10 \le R \le 2.00$ | Verify `split_65_35` gap ($0.30''$), left vertical callout bar (`0.08''`), and subfigure callout anchors (`Fig. 1a/b`). |
| **03** | Literature Taxonomy & Positioning | Native DrawingML 3-Col Taxonomy (`<p:sp>`) or Harvested Scaling Plot (`<p:pic>`) | `grid_3col` or $R \approx 1.4$ | Verify identical column heights ($5.200''$), parallel bold headers, and $\ge 75\%$ card occupancy. |
| **04** | Core Objective & Research Gap | Asymmetric Split: Empirical Bottleneck Plot (`<p:pic>`) vs. Hypothesis Card | $0.90 \le R \le 1.60$ | Verify balanced 50/50 or 60/40 weight and explicit target invariant / bound statement. |
| **05** | Historical Lineage & Baselines | Native DrawingML Timeline (`<p:sp>` + `rightArrow`) or Lineage Table (`<a:tbl>`) + `[Own Lab Synergy]` | `split_65_35` | Verify chronological progression (`Origin -> Transition -> Proposed`) and concrete lab codebase link. |
| **06** | Inputs, Spaces & Assumptions | Harvested Latent/Spectral Plot (`<p:pic>`) + Inline `<a14:m>` Tensor Spaces | $0.85 \le R \le 1.50$ | Verify inline OMML tensor dimensions ($\mathbf{x} \in \mathbb{R}^{B \times L \times D}$) render without raw `$` leaks. |
| **07** | Mathematical Formulation | Dedicated Display `<a14:m><m:oMathPara>` Master Equations + Symbol Glossary Table (`<a:tbl>`) | `split_equal_2col` / `asymmetric_2row` | Verify dynamic $H_{\text{eq}}$ clearance, centered `<m:oMathPara>`, physical intuition caption, and complete symbol definitions. |
| **08** | System Architecture & Mechanism | Harvested 350+ DPI Pipeline (`<p:pic>`) or Native Vector Flowchart (`>10 <p:sp>` nodes) + `[Mechanistic Interpretability]` | $R > 2.2$ (`asymmetric_2row`) or $1.4\text{--}2.1$ (`split_65_35`) | Adapt layout strictly to pipeline $R$; never crush a wide architecture panorama into a narrow column! |
| **09** | Experimental Protocol & Compute | Native 3-Col Protocol Cards (`<p:sp>`) or Focal Setup Table (`<a:tbl>`) | `grid_3col` | Verify datasets, baseline families, hardware cluster, and precision (`BF16`/`FP8`) are explicitly itemized. |
| **10** | Primary SOTA Benchmarks | Native Redesigned `<a:tbl>` ($\le 8 \times 7$) or Crisp 350 DPI Table Crop + Takeaway Cards | `asymmetric_2row` | Verify **bold** SOTA cells, underlined runner-up, explicit `Δ` gain column, and zero mid-number line wraps. |
| **11** | Trade-off & Pareto Analysis | Harvested Pareto / Throughput Curve (`<p:pic>`) + `[Computational & Hardware Efficiency]` Callout | $1.20 \le R \le 1.90$ | Verify axis labels/legends are legible at `150 DPI` slide preview and VRAM/latency numbers are anchored in text. |
| **12** | Component Ablations & Scaling | `quadrant_2x2` Native Ablation Table (`<a:tbl>`) + Sensitivity / Scaling Subplots (`<p:pic>`) | `quadrant_2x2` ($4 \times 5.916'' \times 2.475''$) | Verify uniform $G_x = 0.30''$, $G_y = 0.25''$ gutters and quantified component drop deltas ($-\Delta 3.2\%$). |
| **13** | Contributions vs. Independent Critique | Balanced `split_equal_2col` Synthesis Cards (`<p:sp>`) | 50/50 Dual Cards | Verify equal visual weight between validated breakthroughs and honest scope/compute/generalization boundaries. |
| **14** | Seminar Prompts & Lab Roadmap | `split_65_35` Discussion Prompts + 3-Phase `[Own Lab Synergy]` Action Milestones | `split_65_35` | Verify zero dead `"Thank You"` filler; confirm 3 time-bounded actionable milestones (`Week 1 -> Week 2 -> Week 3`). |

### 9.2 Track B (`python-pptx`) Reference Primitives (Zero-Distortion + Two-Phase OMML Safe)

When Node.js/`PptxGenJS` is unavailable and the agent writes a pure-Python generator inside the active Conda environment, use these exact patterns to guarantee isotropic image scaling, clean academic tables, and `latex_to_omml.py` compatibility:

```python
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

def init_widescreen_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(13.333)   # 12,192,000 EMU (16:9)
    prs.slide_height = Inches(7.500)  # 6,858,000 EMU
    return prs

def add_isotropic_picture(slide, img_path: str, zone_x: float, zone_y: float, zone_w: float, zone_h: float):
    """Places a high-DPI image centered inside (zone_x, zone_y, zone_w, zone_h) inches with ZERO aspect distortion."""
    with Image.open(img_path) as im:
        w_px, h_px = im.size
    aspect = w_px / max(1.0, float(h_px))
    render_w = min(zone_w, zone_h * aspect)
    render_h = render_w / aspect
    render_x = zone_x + (zone_w - render_w) / 2.0
    render_y = zone_y + (zone_h - render_h) / 2.0
    return slide.shapes.add_picture(
        img_path,
        Inches(render_x),
        Inches(render_y),
        width=Inches(render_w),
        height=Inches(render_h),
    )

def add_display_math_placeholder(slide, latex_expr: str, x: float, y: float, w: float, h: float):
    """Writes a Phase-1 <<MATH_DISPLAY:...>> placeholder run ready for latex_to_omml.py --inject."""
    tx = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = f"<<MATH_DISPLAY:{latex_expr}>>"
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    return tx
```

---

## 10. Critical Engine Anti-Patterns & Failure Recovery Playbook

| # | Engine / Workflow Anti-Pattern | Concrete Failure Mechanism | Deterministic Prevention & Recovery Rule |
|:---|:---|:---|:---|
| **1** | **Unescaped `&` in `PptxGenJS` Metadata (`pptx.author`, `pptx.company`, `pptx.title`)** | `PptxGenJS` writes metadata properties into `docProps/core.xml` without escaping raw `&` in strings like `"R&D Lab"`, causing PowerPoint to show an *"unreadable content / repair"* warning on open. | Always sanitize deck metadata strings (`.replace(/&/g, 'and')`) while letting `PptxGenJS` / `latex_to_omml.py` properly escape `&amp;` inside slide XML runs. |
| **2** | **Appending `<m:oMath>` Inside `<a:r>` in `python-pptx`** | OpenXML forbids `<m:oMath>` inside `<a:r>`; PowerPoint silently drops the entire equation node and renders an empty gap. | Always insert `<a14:m><m:oMath>...</m:oMath></a14:m>` as a **direct child of `<a:p>`** (sibling to `<a:r>`), using `latex_to_omml.py --inject`. |
| **3** | **Relying Solely on `shrinkText: true` / `MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE` for Overflow** | LibreOffice headless (`soffice`) partially ignores PowerPoint's client-side `normAutofit` scaling factor—or shrinks dense bullets down to unreadable `7pt` micro-text in desktop PowerPoint. | Treat `shrinkText` only as a minor 5% safety cushion. Enforce hard character/bullet budgets upfront and visually verify rendered font legibility in `160 DPI` PNGs. |
| **4** | **Delivering `Slidev --format pptx` or `Marp --pptx` When User Requested `.pptx`** | Both tools rasterize every slide into a full-bleed static PNG background inside a `.pptx` shell—making titles, bullets, and tables 100% uneditable in PowerPoint. | Never use `Slidev` or non-editable `Marp` export for `.pptx` deliverables; always use Track A (`PptxGenJS`), Track B (`python-pptx`), or Track C (OOXML Surgery). |
| **5** | **Concurrent `soffice --headless` Calls Without `-env:UserInstallation` Isolation** | Multiple parallel LibreOffice processes lock the shared default user profile, hanging indefinitely or returning exit code `0` without writing a `.pdf` file. | Always pass a unique temporary `-env:UserInstallation=file:///...` directory, `--norestore`, `--nolockcheck`, and an explicit `timeout=60` on every `soffice` invocation. |
| **6** | **Auto-Cropping Multi-Panel Figures With Wide Internal White Gutters (`> 30 pt`)** | Caption-anchored bottom-up clustering stops early at the bottom row of subfigures `(c)(d)`, slicing off top panels `(a)(b)`! | Visually inspect every extracted figure via `view_file` in Stage 1; if top subfigures are missing, re-extract immediately using manual `--page P --bbox "x0,y0,x1,y1"` coordinates. |
| **7** | **Creating Project-Local `venv` / `.venv` or Leaving Temporary Build Artifacts** | Violates workspace hygiene and pollutes user repositories with gigabytes of duplicate Python/Node packages or `_stage1.pptx` intermediates. | Execute Python helpers strictly via existing local Conda environments, delete `_stage1.pptx` and temporary LibreOffice profiles in `finally` blocks, and verify clean staging output. |
