---
name: figure
description: "Modular academic and scientific figure generation hub. Routes publication-grade multi-panel plots, chart-family selection, Python/R vector pipelines, and no-code SVG layout editing (:nature, :figureforge, :python, :r, :atlas, :qa) to nature-figure-skill, with an extensible sub-skill registry for future diagram and illustration engines."
---

# Academic & Scientific Figure Generation Hub (`figure`)

Unified, extensible top-level skill hub for **submission-grade scientific plotting, multi-panel composite figures, visual SVG layout prototyping, and academic diagram engineering**. Read the matched sub-skill entrypoint and reference modules before generating layouts or plotting code.

```text
figure/
├── SKILL.md                                           # Master figure router, shared guardrails & extension spec
├── agents/openai.yaml                                 # Harness UI metadata
├── nature-figure-skill/                               # :nature (default) — Nature-grade Python/R workflow + FigureForge
│   ├── SKILL.md                                       # Standardized sub-skill entrypoint & route dispatcher
│   ├── README.md / README.zh-CN.md                    # Bilingual overview, templates showcase & quick start
│   ├── LICENSE / DERIVATIVE_NOTICE.md                 # MIT license & upstream attribution
│   ├── figureforge/                                   # :figureforge — No-code browser SVG studio (22 templates, 16 palettes)
│   │   ├── index.html / README.md
│   │   ├── css/                                       # style.css, workspace.css
│   │   └── js/                                        # 20 modular canvas/editor/palette/showcase scripts
│   ├── assets/                                        # 9 rendered SVG atlases (83 panels) + workflow diagrams
│   ├── skills/
│   │   ├── nature-figure/                             # Core contract-first Python/R publication figure engine
│   │   │   ├── SKILL.md                               # Backend gate, 3 hard rules, Python & R scaffolds
│   │   │   ├── references/                            # 14 playbooks: contract, selection, api, R, 83-panel atlas, QA
│   │   │   ├── assets/                                # gallery/, chart-atlas/, figures4papers/ demo scripts
│   │   │   ├── evals/                                 # evals.json + visual-baseline/render.py
│   │   │   └── agents/openai.yaml
│   │   └── nature-{polishing,writing,citation,data,reader,response,paper2ppt,academic-search}/
│   ├── scripts/                                       # Zero-dependency template, SVG & link/schema self-checks
│   └── tools/make_mockup.py                           # Product card mockup utility
└── <future-sub-skill>/                                # Plug-in slot for future diagram / schematic / 3D / bio figure skills
    └── SKILL.md
```

---

## 1. Sub-Skill Registry (`已接入与预留画图子技能注册表`)

`figure` operates as an open **dispatcher + guardrail layer**. Each specialized figure engine lives in an isolated subdirectory `figure/<sub-skill-dir>/` with its own `SKILL.md` and assets:

| Sub-Skill Directory | Primary Tag(s) | Status | Entrypoint | Core Domain & Output Deliverables |
|:---|:---|:---|:---|:---|
| [`nature-figure-skill/`](nature-figure-skill/SKILL.md) | `:nature` *(default)*, `:plot`, `:figureforge`, `:python`, `:r`, `:atlas`, `:qa` | **Active** | [nature-figure-skill/SKILL.md](nature-figure-skill/SKILL.md) → [skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md) & [figureforge/README.md](nature-figure-skill/figureforge/README.md) | *Nature* / *Science* / *Cell* / *NeurIPS* quantitative & multi-panel composite figures: contract-first `matplotlib`/`seaborn` & `ggplot2`/`patchwork`/`ComplexHeatmap` pipelines (`SVG` + `PDF` + `600 DPI TIFF`), 9 atlases (83 panels), `figures4papers` demos, and the no-code **FigureForge** SVG studio |
| `figure/<arch-diagram-skill>/` | `:arch`, `:tikz`, `:schematic` *(reserved)* | *Plug-in Slot* | `figure/<arch-diagram-skill>/SKILL.md` | Method/system architecture diagrams, LaTeX `TikZ` / DrawingML / SVG tensor pipelines, Figure 1 conceptual schematics |
| `figure/<bio-illustration-skill>/` | `:bio`, `:pathway`, `:clinical` *(reserved)* | *Plug-in Slot* | `figure/<bio-illustration-skill>/SKILL.md` | Wet-lab experimental workflows, signaling pathways, CONSORT / clinical trial schematics, organ/cell vector icons |
| `figure/<3d-scientific-skill>/` | `:3d`, `:manifold`, `:teaser` *(reserved)* | *Plug-in Slot* | `figure/<3d-scientific-skill>/SKILL.md` | Geometric/physics ray-cast illustrations, point-cloud / mesh / robotics filmstrips, CV/graphics teaser plates |
| `figure/<interactive-vis-skill>/` | `:interactive`, `:web-vis` *(reserved)* | *Plug-in Slot* | `figure/<interactive-vis-skill>/SKILL.md` | Interactive HTML/SVG/Vega/Plotly exploratory & supplementary web figures |

---

## 2. Tag-Based & Intent-Based Routing Protocol (`标签与意图双模路由`)

Explicit tags compose freely (e.g., `/figure :nature :python`, `/figure :nature :r :qa`, `/figure :figureforge`, `/figure :select`). When no tag is supplied, auto-detect from user intent using §2.2.

### 2.1 Active Tag Router (`nature-figure-skill`)

| Tag(s) | Load Module(s) (In Order) | Action & Execution Rules |
|:---|:---|:---|
| `:nature` *(default)* / `:plot` | 1. [nature-figure-skill/SKILL.md](nature-figure-skill/SKILL.md)<br>2. [nature-figure-skill/skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md) | Full *Nature*-standard figure pipeline: triage FigureForge vs. code → lock **Figure Contract** → enforce **Backend Gate (`Python or R?`)** if unspecified → single-backend render → QA → `save_pub_set()` / `save_pub_r()` export |
| `:figureforge` (`:editor`, `:nocode`, `:canvas`) | 1. [nature-figure-skill/figureforge/README.md](nature-figure-skill/figureforge/README.md)<br>2. [nature-figure-skill/README.md](nature-figure-skill/README.md) | **No-code / layout-first route**: launch or guide the **FigureForge** infinite canvas & WYSIWYG SVG editor (`figureforge/index.html` locally or <https://jing1312.github.io/nature-figure-skill/figureforge/>) with 22 templates, 16 palettes, and 83 remixable panels. **Never ask `"Python or R?"` on this route.** |
| `:select` (`:chart-type`) | 1. [figure-selection.md](nature-figure-skill/skills/nature-figure/references/figure-selection.md)<br>2. [atlas-gallery.md](nature-figure-skill/skills/nature-figure/references/atlas-gallery.md) | Recommend 1–3 optimal chart families from the scientific claim (group comparison, distribution, trend, matrix, hierarchy, network, survival/clinical) plus explicit anti-recommendations |
| `:contract` (`:layout`) | 1. [figure-contract.md](nature-figure-skill/skills/nature-figure/references/figure-contract.md)<br>2. [nature-2026-observations.md](nature-figure-skill/skills/nature-figure/references/nature-2026-observations.md)<br>3. [common-patterns.md](nature-figure-skill/skills/nature-figure/references/common-patterns.md) | Convert a raw claim or table list into a one-sentence conclusion, 4-archetype classification (`quantitative grid`, `schematic-led composite`, `image plate + quant`, `asymmetric mixed-modality`), non-redundant panel map, and hero-panel hierarchy |
| `:python` (`:matplotlib`, `:seaborn`) | 1. [nature-figure-skill/skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md)<br>2. [api.md](nature-figure-skill/skills/nature-figure/references/api.md)<br>3. [common-patterns.md](nature-figure-skill/skills/nature-figure/references/common-patterns.md)<br>4. [demos.md](nature-figure-skill/skills/nature-figure/references/demos.md) *(when adapting `figures4papers`)* | **Pre-satisfies the Python backend gate**: execute exclusively in Python (`apply_publication_style()`, `svg.fonttype='none'`, `pdf.fonttype=42`, `PALETTE` / `PALETTE_NMI_PASTEL`, `add_stat_strip()`, `save_pub_set()`) |
| `:r` (`:ggplot2`, `:patchwork`, `:complexheatmap`) | 1. [nature-figure-skill/skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md)<br>2. [r-workflow.md](nature-figure-skill/skills/nature-figure/references/r-workflow.md)<br>3. [r-template-index.md](nature-figure-skill/skills/nature-figure/references/r-template-index.md) | **Pre-satisfies the R backend gate**: execute exclusively in R (`ggplot2` + `patchwork` + `ComplexHeatmap` + `ggrepel`, exported via `svglite` + `cairo_pdf` + `ragg::agg_tiff` in `save_pub_r()`) |
| `:atlas` (`:templates`, `:demos`) | 1. [atlas-gallery.md](nature-figure-skill/skills/nature-figure/references/atlas-gallery.md)<br>2. [chart-types.md](nature-figure-skill/skills/nature-figure/references/chart-types.md)<br>3. [tutorials.md](nature-figure-skill/skills/nature-figure/references/tutorials.md) | Reuse geometry (`W=1080, COLW=352`), jewel-pastel / NPG / NMI palettes, and patterns from the 9 showcase atlases (83 panels) and 9 bundled `figures4papers` projects |
| `:qa` (`:audit`, `:check`) | 1. [qa-contract.md](nature-figure-skill/skills/nature-figure/references/qa-contract.md)<br>2. [design-theory.md](nature-figure-skill/skills/nature-figure/references/design-theory.md) | Pre-submission audit: final print point size (`5–7 pt` at `89/183 mm`), zero legend/stat occlusion, editable vector text, error-bar/`n`/test disclosure, blot/microscopy integrity, and cross-panel color consistency |

### 2.2 Automatic Intent Routing (When No Tag Is Given)

1. **Match registered sub-skill domain first**: If future specialized sub-skills are installed under `figure/<sub-skill-dir>/` and the prompt matches their registered domain (e.g., pure LaTeX `TikZ` circuit/architecture drawing), route to that sub-skill's `SKILL.md`.
2. **Triage No-Code vs. Scripted Pipeline**:
   - Requests mentioning *"no code"*, *"drag and drop"*, *"browser editor"*, *"show me layout skeletons first"*, or *"FigureForge"* → route directly to **FigureForge** ([nature-figure-skill/figureforge/README.md](nature-figure-skill/figureforge/README.md)).
   - Requests asking *"which chart type fits my data?"* before plotting → open [figure-selection.md](nature-figure-skill/skills/nature-figure/references/figure-selection.md) first.
   - All quantitative, statistical, bioinformatics, clinical, or ML manuscript plotting / revision / QA tasks → route to **[nature-figure-skill/skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md)**.
3. **Respect the Backend Gate in Scripted Mode**:
   - If the user already specified `:python` / `.py` / `matplotlib` or `:r` / `.R` / `ggplot2`, lock that backend immediately and never cross-render with the other language.
   - If the user asks *"Python or R — which do you recommend?"*, consult [backend-selection.md](nature-figure-skill/skills/nature-figure/references/backend-selection.md), state the rationale, and proceed.
   - Otherwise, ask one concise question (**"Python or R?"**) and wait before writing plotting scripts, per [skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md).

---

## 3. Core Capabilities of `nature-figure-skill`

Integrated from [`jing1312/nature-figure-skill`](https://github.com/jing1312/nature-figure-skill) (MIT; see [LICENSE](nature-figure-skill/LICENSE) and [DERIVATIVE_NOTICE.md](nature-figure-skill/DERIVATIVE_NOTICE.md)):

- **Dual-Route Workflow (FigureForge ↔ Code Handoff)**:
  - **FigureForge Visual Studio** ([figureforge/](nature-figure-skill/figureforge/)): VibePaper-style infinite canvas, 22 publication-grade templates (superplot bars, clustered heatmaps with dendrograms, volcano, forest, Kaplan–Meier + risk table, violin/box, multi-panel hero composites), 16 series-linked palettes, smart alignment guides, SVG element splitting, and 1-click `SVG` / `PDF` / `600 DPI TIFF` / `PNG` / `PPTX` export.
  - **Contract-First Python & R Engine** ([skills/nature-figure/SKILL.md](nature-figure-skill/skills/nature-figure/SKILL.md)): Enforces `Figure Contract → Backend Gate → Single-Backend Render → Layout & QA → Unified Export Bundle`.
- **9 Programmatic Showcase Atlases (83 Panels)**:
  - `showcase.svg` (12 base statistical charts), `showcase-pro.svg` (radar, polar, quadrant, volcano, z-score heatmap), `showcase-bio.svg` (12 bioinformatics/single-cell panels: Mantel, GSEA, PCA ellipses, dot-dendrogram), `showcase-extra.svg` (OncoPrint, waterfall, alluvial, ridgeline, Bland–Altman, forest, Manhattan), `showcase-plus.svg` (chord, UpSet, network, ternary, treemap, sunburst, hexbin, parallel coords), `showcase-ultra.svg` (Circos, QQ, KM+risk, raincloud, GO lollipop, Venn, Gantt, radial tree, coverage tracks), `showcase-max.svg` (SPLOM, MA, pathway dot, circle packing, bump, 2D contour, dumbbell, diverging bar, calendar), `showcase-nova.svg` (Sankey, correlogram, mosaic, biplot, pyramid, ring heatmap, dual-axis, response surface, ECDF+KS), and `showcase-apex.svg` (funnel, Taylor, arc, icicle, beeswarm, cycle, horizon, bullet, waffle).
- **Production `figures4papers` Demo Library**:
  - 9 real *Nature Machine Intelligence* / ML / bioinformatics figure codebases under `nature-figure-skill/skills/nature-figure/assets/figures4papers/` indexed in [demos.md](nature-figure-skill/skills/nature-figure/references/demos.md).
- **Bundled Companion `nature-*` Reference Skills**:
  - `nature-figure-skill/skills/` preserves upstream's companion modules (`nature-polishing`, `nature-writing`, `nature-citation`, `nature-data`, `nature-reader`, `nature-response`, `nature-paper2ppt`, `nature-academic-search`) for *Nature*-specific data-availability statements, CNS citation verification, or bilingual reading when explicitly needed alongside figure production.

---

## 4. Shared Publication Figure Guardrails (`全局出版级配图硬性准则`)

Every sub-skill under `figure/` (both `nature-figure-skill` and all future drawing skills) MUST uphold these six publication invariants:

1. **`G1` Exact 1:1 Column Geometry & Final Print Point Sizes**:
   - Set canvas dimensions to real journal column widths **before** drawing (`89 mm` single-column, `120–136 mm` 1.5-column, `183 mm` double-column for *Nature*; `139.7 mm` NeurIPS; `174–178 mm` IEEE/CVPR).
   - Size typography in **final print points**: `5.5–7 pt` axis/tick labels, `7–8 pt` bold lowercase panel letters (`a`, `b`, `c`), `0.6–0.8 pt` strokes. Never author `16–24 pt` slide text and shrink the canvas down.
2. **`G2` Editable Vector Primary + High-DPI Print Companions**:
   - Export editable vector text (`svg.fonttype = 'none'`, `pdf.fonttype = 42`, `svglite`, `cairo_pdf`, or native `TikZ`/SVG `<text>`) paired with `600 DPI` `.tiff` and `300+ DPI` `.png` previews via a single canonical export helper (`save_pub_set` / `save_pub_r`).
   - Never deliver rasterized diffusion gibberish text, JPEG-compressed line art, or silently merged collages when independent figures were requested.
3. **`G3` Zero Data Occlusion & Frameless Visual Hierarchy**:
   - Remove top/right plot spines (`despine`) unless framing a bounded matrix/image plate; keep plot backgrounds pure `#FFFFFF` (use dark plates solely for fluorescence/microscopy channels).
   - Never place legends, correlation boxes, or `p`-value callouts over data points; use direct curve labels, external frameless legends, or frameless top stat strips (`add_stat_strip`).
4. **`G4` Semantic Role Color & Colorblind/Grayscale Safety**:
   - Assign color by **scientific role** (proposed hero method vs. baseline family vs. neutral control vs. signed $\Delta$ accent)—never cycle arbitrary rainbow palettes or `jet`.
   - Keep the exact same hue family for the same method across every panel (`a` through `f`), and ensure curves/bars remain distinguishable under deuteranopia/protanopia and monochrome print.
5. **`G5` Evidence Non-Redundancy & Statistical Honesty**:
   - Every panel in a composite figure must carry a unique link in the manuscript's claim chain (never pair a pie chart and stacked bar of the same percentages).
   - Explicitly state sample size `n`, error-bar definition (`mean ± s.d.`, `median ± IQR`, `95% CI`), and statistical test in the figure strip or companion caption notes; tighten axes to honest ranges without distorting zero-baseline bars.
6. **`G6` Privacy & Repository Hygiene**:
   - Never expose private local user paths, chat-attachment filenames, or unpublished template provenance in figure text, code comments, or replies.
   - Never create `venv`, `.venv`, `node_modules`, or `__pycache__` inside skill directories.

---

## 5. Extensible Architecture for Future Drawing Skills (`后续画图 Skill 扩展接入规范`)

`figure/` is architected to grow into a comprehensive multi-engine scientific visual suite (adding architecture diagrammers, `TikZ`/LaTeX schematic builders, biomedical pathway illustrators, 3D/teaser renderers, etc.) **without changing the top-level skill count or breaking MIRASIM / Claude Code installation**.

### 3-Step Plug-In Guide (`三步标准接入流程`)

#### Step 1 — Vendor Cleanly into `figure/<new-skill-dir>/` (Zero Git Submodule Trap)
1. Clone or stage the upstream skill into a temporary folder outside the repo (always pass explicit network timeouts such as `git -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=15`).
2. **CRITICAL — Strip `.git` Before Copying**: Remove `.git/` (plus repo-root-only `.github/` workflows, `.DS_Store`, `__pycache__`, `node_modules`) **before** copying into `figure/<new-skill-dir>/` so Git tracks every file as a normal `100644`/`100755` blob and **never** creates a `160000` submodule gitlink.
3. Preserve upstream `LICENSE`, `README.md`, attribution notices, scripts, templates, and references intact; scrub any hardcoded personal home-directory or machine-local absolute paths.
4. Ensure `figure/<new-skill-dir>/SKILL.md` exists and uses a **single-line double-quoted `description: "..."`** in its YAML frontmatter (strictly zero `>-` or `|` multiline YAML scalars).

#### Step 2 — Register in `figure/SKILL.md` Sub-Skill Router
1. Update the directory tree at the top of `figure/SKILL.md` and promote or add the sub-skill row in **§1 Sub-Skill Registry** with its `[<new-skill-dir>/SKILL.md](<new-skill-dir>/SKILL.md)` entrypoint.
2. Assign clean, non-overlapping `:tag` triggers (e.g., `:arch` / `:tikz` for architecture schematics, `:bio` for pathway illustrations, `:3d` for ray-cast/mesh figures) in **§2.1** and add an intent rule in **§2.2** so natural-language requests dispatch deterministically while `:nature` remains the default quantitative publication-plotting engine.
3. Confirm the new sub-skill adheres to **§4 Shared Publication Figure Guardrails (`G1–G6`)**.

#### Step 3 — Sync Root `README.md` & Pass Verification Gates
1. Add `<new-skill-dir>/` under `figure/` in root `README.md` (repo tree + `/figure` tag matrix). No extra `cp -R` line is needed for Claude Code or MIRASIM because installing `figure/` automatically bundles every `figure/<sub-skill-dir>/`!
2. Run read-only verification (`python -B` so zero `__pycache__` is emitted):
   - `git ls-files --stage figure/` → confirm `0` `160000` gitlinks and `0` nested `.git` directories.
   - YAML frontmatter check → `figure/SKILL.md` and all nested `SKILL.md` / `openai.yaml` files parse cleanly with single-line quoted descriptions.
   - Script & link check → all `.py` (`ast.parse`) and `.js` (`node --check`) scripts pass syntax checks, `0` hardcoded local user paths remain, and `100%` of relative Markdown links resolve.

---

## Related Skills in Pack

- **`humanize`** (`../humanize/SKILL.md` when installed in pack) — Pair with `:paper-boundaries` (`../humanize/paper-boundaries.md`) to lock the non-defensive claim hierarchy *before* designing Figure 1 or ablation plots, or `:figure` (`../humanize/references/scientific-figures-and-ui-de-ai.md`) to diagnose and purge `SF1–SF10` AI-generated diagram slop.
- **`plain`** (`../plain/SKILL.md` when installed in pack) — Walk through one small domain-native numerical example step by step—ideal for designing toy walkthrough insets in method figures.
- **`cs-report-ppt`** (`../cs-report-ppt/SKILL.md` when installed in pack) — Assemble exported high-DPI / vector figures into 16:9 conference, group-meeting, thesis-defense, or grant slide decks with Vision-in-the-Loop QA.
