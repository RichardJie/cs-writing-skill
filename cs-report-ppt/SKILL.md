---
name: cs-report-ppt
description: "Create conference-level academic paper presentation PPT decks from paper PDFs with 14-slide figure-dominant spine, native paper figures/tables, OMML formulas, and rigorous visual self-inspection."
---

# CS Report PPT Skill (`cs-report-ppt`)

Transform scientific research papers (PDF) into conference-grade (NeurIPS, ICML, CVPR, ICLR, KDD, ACL), 16:9 widescreen PowerPoint presentation decks that combine **dense, informative academic rigor** with **clean, minimalist visual aesthetics**.

---

## 1. Core Philosophy & Quality Standards

A premier academic conference presentation is **not a wall of abstract text**, nor is it a sparse generic template. Every generated deck must embody four core principles:

1. **Figure & Table Dominance ($\ge 80\%$ Visual Asset Coverage)**:
   - **Visuals are first-class citizens**: At least **11 out of 14 slides** must feature authentic high-resolution figures, system architecture diagrams, qualitative visual comparisons, or benchmark tables extracted directly from the paper PDF.
   - Slides should never be filled with purely speculative text when authentic visual evidence exists in the paper. Pure-text cards are strictly reserved for synthesis slides (e.g., Critical Assessment and Discussion Roadmap).
2. **Semantic Visual-Text Anchoring (图文深度互文)**:
   - Do not merely embed an image beside generic text. Card bullet points must **actively dissect the visual asset**:
     - *Point to the evidence*: Call out specific curves, sub-figures (`Fig. 2b`), columns, or inflection points.
     - *Quantify the delta*: Highlight key performance jumps ($\Delta +4.8\%$, $-21\%\text{ Latency}$).
     - *Deliver the verdict*: State the precise empirical takeaway derived from the visual.
3. **Academic Minimalist Black & White Palette (极简学术黑白灰)**:
   - **Default Aesthetic**: Clean, distraction-free monochrome / grayscale (`academic_mono`).
   - Pure white background (`#FFFFFF`), pure black headers (`#000000`), deep slate body text (`#1F2937`), subtle light gray borders (`#D1D5DB`), and low-saturation neutral callout boxes (`#F9FAFB`).
   - Eliminates loud colored banners, heavy blue blocks, and decorative clutter that detract from academic credibility.
4. **Flawless Spatial & Formula Execution (零排版瑕疵，原生数学表达)**:
   - **Zero Collision / Overlap**: Headers, subtitles, equations, card boundaries, and bullet runs must maintain strictly non-zero positive vertical margins ($\ge 0.15''$).
   - **Dynamic Math Sizing**: Multi-line display formulas ($\mathcal{L}_{\text{total}}$, complex fractions, summations) must receive dynamic vertical bounding boxes ($\ge 0.65''\text{--}1.20''$) with separate vertical offsets for physical intuition commentary.
   - **Native DrawingML OMML**: Formulas are rendered as editable, vector Office Math (OMML)—never rasterized screen captures or raw LaTeX placeholders.
   - **Aspect-Ratio Locking**: All cropped figures and tables maintain their true physical proportions (`contain` scaling) with zero geometric stretching.

---

## 2. Language & Interaction Policy

- **Interactive Dialogue & Progress Reporting**: **100% 简体中文 (Chinese)**.
  - All communication, extraction summaries, architectural rationale, and quality check reports must be presented in clear, professional Chinese.
- **Generated Slide Deck Content**: **100% Academic English (专业学术英文)**.
  - All slide titles, subtitles, card headers, bullet points, table text, diagram labels, and footnotes must be written in formal, publication-grade academic English.

---

## 3. The 14-Slide Figure-Dominant Academic Spine

The presentation strictly adheres to the **14-slide Session Note Spine**. Over **80% of slides** are organically paired with authentic paper visual assets:

| Slide # | Section | Category Badge | Standard Slide Title | Recommended Layout | Key Visual Asset & Empirical Focus | Marginal Callout Slot |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Header | `PAPER OVERVIEW` | `[Paper Title in Title Case]` | `split_equal_2col` / `hero_1col` | **Teaser / Core Trade-off Figure**: Full citation, authors, affiliations, venue/year, alongside teaser tradeoff curve or dilemma diagram. | None (Metadata Grid) |
| **2** | Background (1/4) | `BACKGROUND & MOTIVATION` | `Motivation & Problem Context` | `split_65_35` | **Qualitative Failure Samples (Fig. 1/2)**: Real-world failure modes of prior art paired with challenge breakdown. | `[State Memory Inertia]` / `[Model Adaptivity]` |
| **3** | Background (2/4) | `LITERATURE LANDSCAPE` | `Paper Classification & Taxonomy` | `split_65_35` / `grid_3col` | **Taxonomy / Capacity Scaling Chart**: Methodological taxonomy, parameter bounds, or capacity trade-off plot. | None (Taxonomy Matrix) |
| **4** | Background (3/4) | `RESEARCH OBJECTIVE` | `Core Objective & Target Gap` | `split_equal_2col` | **Empirical Gap Visualization**: Central hypothesis vs. 2–3 unresolved theoretical / computational bottlenecks. | None (Hypothesis Hero) |
| **5** | Background (4/4) | `HISTORICAL LINEAGE` | `Historical Evolution & Baselines` | `split_65_35` | **Lineage / Downsampling Comparison Table**: Evolutionary timeline (Origin $\rightarrow$ Transition $\rightarrow$ Current) + author lab background. | `[Own Lab Synergy]` |
| **6** | Methods (1/4) | `METHODOLOGY: FOUNDATIONS` | `Inputs, Assumptions & Prerequisites` | `split_65_35` / `split_equal_2col` | **Latent Space / Spectral Analysis Plot (Fig. 4)**: Input spaces ($\mathbf{x} \in \mathbb{R}^{B \times L \times D}$), tokenization, stationarity invariants. | None (Foundational Invariants) |
| **7** | Methods (2/4) | `METHODOLOGY: FORMULATION` | `Mathematical Formulation & Objectives` | `split_equal_2col` / `asymmetric_2row` | **Native OMML Master Loss Equations**: Multi-objective formulation ($\mathcal{L}_{\text{total}}$), adaptive gradient weights, parameter glossary. | None (Native OMML Formulation) |
| **8** | Methods (3/4) | `METHODOLOGY: ARCHITECTURE`| `Technical Mechanism & Architecture` | `split_65_35` | **Main System Architecture Diagram (Fig. 3)**: High-DPI pipeline figure paired with 3-phase execution breakdown. | `[Mechanistic Interpretability]` |
| **9** | Methods (4/4) | `EXPERIMENTAL PROTOCOL` | `Experimental Design & Setup` | `split_65_35` / `grid_3col` | **Benchmark Configuration Table**: Datasets, evaluation protocols, baseline suites, GPU compute budget. | None (Protocol Specs) |
| **10** | Results (1/3) | `BENCHMARK RESULTS` | `Primary Quantitative Benchmarks` | `split_65_35` / `split_equal_2col` | **Primary SOTA Benchmark Table (Table 1)**: Authentic benchmark table with bolded best metrics and percentage deltas ($\Delta$). | None (Benchmark SOTA Table) |
| **11** | Results (2/3) | `COMPARATIVE ANALYSIS` | `Comparative Evaluation & Trade-offs`| `split_65_35` | **Scaling Curves / Qualitative Visuals (Fig. 5)**: Multi-paradigm breakdown, Pareto throughput/quality frontier. | `[Computational & Hardware Efficiency]` |
| **12** | Results (3/3) | `ABLATION & SENSITIVITY` | `Ablation Studies & Scaling Curves` | `split_65_35` / `quadrant_2x2` | **Component Ablation Table (Table 2)**: Stepwise contribution ablations, hyperparameter sensitivity, channel scaling. | None (Ablation Table/Curves) |
| **13** | Conclusion (1/2) | `CRITICAL ASSESSMENT` | `Core Contributions vs. Critique` | `split_equal_2col` | **Balanced Synthesis Cards**: Author-claimed breakthroughs vs. independent critique (hidden compute, generalization bounds). | None (Balanced Critique) |
| **14** | Conclusion (2/2) | `SEMINAR DISCUSSION` | `Discussion Prompts & Lab Roadmap` | `split_65_35` | **Forward Roadmap Cards**: 3 forward-looking seminar discussion questions paired with actionable 3-phase lab milestones. | `[Own Lab Synergy]` (Action Roadmap) |

---

## 4. 5-Class Laboratory Research Synergy Taxonomy ("旁注")

Academic paper presentations must actively bridge to internal laboratory research agendas via dedicated marginal callouts:

1. **`[State Memory Inertia]`** (Slide 2 or 6):
   - *Focus*: Recurrent state retention, KV cache dynamics, context compression, historical activation decay.
   - *Lab Link*: Connects long-context caching bottlenecks to in-house agent memory scaling.
2. **`[Model Adaptivity / Generalization]`** (Slide 2 or 4):
   - *Focus*: Distribution shift resilience, OOD generalization, test-time compute, continual adaptation.
   - *Lab Link*: Maps paper robust training mechanisms to our perturbed sensor benchmarks.
3. **`[Mechanistic Interpretability]`** (Slide 8):
   - *Focus*: Representation geometry, circuit discovery, attention head routing, sparse autoencoders (SAE).
   - *Lab Link*: Dissects whether internal feature activations match our circuit hypotheses.
4. **`[Computational & Hardware Efficiency]`** (Slide 11):
   - *Focus*: FLOP reduction, memory bandwidth optimization, FP8/INT4 quantization, kernel fusion, GPU VRAM bounds.
   - *Lab Link*: Assesses deployment feasibility within our laboratory compute cluster (e.g. RTX 4090 / H100 testbeds).
5. **`[Own Lab Synergy]`** (Slide 5 or 14):
   - *Focus*: Direct codebase migration, baseline replacement, 3-stage actionable roadmap (Week 1 Reproduction $\rightarrow$ Week 2 Integration $\rightarrow$ Week 3 Hypothesis Test).
   - *Lab Link*: Translates passive presentation consumption into active laboratory research execution.

---

## 5. End-to-End 5-Stage Execution Methodology

```
┌────────────────────────────────────────────────────────┐
│ Stage 1: Paper Deep Reading & Visual Asset Harvesting  │
│ • Extract core theory, equations, baselines & findings │
│ • Harvest 8-12 high-DPI figures & tables directly      │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 2: Semantic Visual-Text Information Architecture │
│ • Structure into 14-slide figure-dominant spine        │
│ • Anchor analytical bullet points to visual evidence   │
│ • Formulate LaTeX math ($...$ / $$...$$) & lab callouts│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 3: Deck Layout & Spatial Assembly                │
│ • Assemble 16:9 widescreen presentation (.pptx)        │
│ • Apply Academic Minimalist Black & White palette      │
│ • Enforce dynamic math vertical sizing & aspect ratio  │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 4: Visual Self-Inspection & Iterative Tuning     │
│ • Render deck to 150+ DPI PNG slide previews           │
│ • Perform multi-modal audit (overlap, overflow, voids) │
│ • Auto-correct coordinates/spacing on any defect       │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 5: Structural Verification & Final Delivery      │
│ • Programmatic OpenXML and OMML math validation        │
│ • Deliver clean .pptx, rendered .pdf, and PNG gallery  │
└────────────────────────────────────────────────────────┘
```

### Stage 1: Paper Deep Reading & Visual Asset Harvesting
1. Read the paper PDF thoroughly to extract metadata, core claims, theoretical formulation, architecture, baseline deltas, and open questions.
2. **Harvest authentic visual assets at 300+ DPI**:
   - Extract **at least 6–10 figures and tables** from the PDF: Teaser diagrams, Failure sample comparisons, System architecture diagrams, Master benchmark tables, Ablation tables, Scaling law plots.
   - Record exact bounding boxes, pixel dimensions, and physical aspect ratios ($W/H$).
   - The AI agent has full autonomy over extraction techniques: PyMuPDF (`fitz`), pdfplumber, pdftoppm, or custom Python scripts.

### Stage 2: Semantic Visual-Text Information Architecture
1. Organize the presentation into the 14-slide spine JSON or structured data model.
2. **Anchor every visual asset with semantic dissection**:
   - Pair each visual with 2–3 structured bullet points that directly interpret its visual data.
   - Formulate mathematical expressions using standard LaTeX (`$x_t$` for inline, `$$\mathcal{L}$$` for display).
   - Inject the 5 laboratory research synergy callouts into their designated slots.

### Stage 3: Deck Layout & Spatial Assembly
1. Construct the 16:9 widescreen presentation ($13.333'' \times 7.500''$ canvas, $12,192,000 \times 6,858,000\text{ EMU}$).
2. Apply the **Academic Minimalist Black & White (`academic_mono`)** palette:
   - Primary: `#000000` | Body: `#1F2937` | Background: `#FFFFFF`
   - Card Borders: `#D1D5DB` | Side-notes: `#F9FAFB` | Accents: `#111827`
3. Enforce dynamic math bounding boxes:
   - Formula box height: dynamically allocated from $0.65''$ to $1.20''$ based on operator density (`\frac`, `\sum`, `\int`, `\matrix`).
   - Maintain vertical clearance $\ge 0.12''$ between formula and explanatory text.
4. Embed figures and tables with `contain` aspect-ratio scaling to preserve true physical geometry.

### Stage 4: Visual Self-Inspection & Iterative Refinement (Mandatory Loop)
1. Convert the generated `.pptx` to PDF and rasterize all 14 slides to **150+ DPI PNG images**.
2. **Execute visual multi-modal self-inspection across every slide**:
   - [ ] **Zero Overlap**: Slide title, tracker badge, formulas, and body text never collide.
   - [ ] **Zero Overflow**: Content remains strictly within cards; cards terminate comfortably above footer ($Y < 6.85''$).
   - [ ] **Figure & Table Dominance**: Confirm $\ge 80\%$ of slides embed authentic visual figures/tables.
   - [ ] **Aspect Ratio**: Visual assets are crisp, sharp, and physically undistorted.
   - [ ] **Math Quality**: Formulas render cleanly as native OMML without unparsed `<<MATH_` leaks or broken symbols.
3. If any defect is detected, immediately tune the layout offsets, font sizes, or card dimensions and re-render.

### Stage 5: Structural Verification & Delivery
1. Verify OpenXML integrity: exactly 14 slides, native DrawingML OMML math nodes, and valid XML schema.
2. Deliver the final presentation `.pptx`, rendered `.pdf`, and slide gallery previews.

---

## 6. Objective Quality Gate Rubric

| Pillar | Criterion | Pass Threshold |
|:---|:---|:---|
| **1. Visual Coverage** | Presentation is figure and table-dominant. | $\ge 11$ of 14 slides feature authentic paper figures, diagrams, or tables. |
| **2. Zero Collision** | No overlapping text boxes, equations, or borders. | Vertical gap $\ge 0.15''$ between headers, formulas, and body bullets. |
| **3. Zero Overflow** | Content stays inside card boundaries. | Card content terminates at $Y < 6.85''$; footer clear at $Y = 7.00''$; `shrinkText` enabled. |
| **4. Minimalist Aesthetics** | Clean academic monochrome / grayscale. | Default `academic_mono`; zero bright neon blocks or heavy saturated color strips. |
| **5. Math Integrity** | Native vector DrawingML OMML math. | OMML math nodes $\ge 4$; zero raw LaTeX leaks (`<<MATH_` or `{{MATH:`); no missing glyphs. |

---

## 7. Modular Tooling Accelerators & Agent Autonomy

The skill package provides modular scripts as optional accelerators:

- **`scripts/crop_figures.py`**: High-DPI PyMuPDF extractor with automatic whitespace snapping and aspect-ratio preservation.
- **`scripts/latex_to_omml.py`**: LaTeX-to-OMML DrawingML converter and in-place PPTX OpenXML injector.
- **`scripts/build_deck.js`**: Node.js + PptxGenJS 16:9 layout generator supporting responsive grids, vector diagrams, and native tables.
- **`scripts/verify_deck.py`**: Programmatic OpenXML validator for slide count, OMML math, and figure metadata.
- **`resources/template_config.json`**: Canvas coordinates, font ladders, and `academic_mono` palette definitions.

> [!IMPORTANT]
> **Full Implementation Autonomy**: The scripts in `scripts/` are **modular accelerators**, not rigid constraints. Capable AI agents have complete autonomy to adapt, write custom Python/Node scripts, or use any suitable library (`python-pptx`, `pptxgenjs`, `pymupdf`, `PIL`, `matplotlib`, etc.) to achieve the highest quality outcome.

---

## 8. Progressive Disclosure References

For deep structural and typographic specifications, consult:
- **[references/spine_template.md](references/spine_template.md)**: Slide-by-slide 14-section specifications with Figure/Table pairing guidelines.
- **[references/typography_rules.md](references/typography_rules.md)**: 16:9 canvas coordinates, grid formulas, and font scale ladders.
- **[references/marginal_annotations.md](references/marginal_annotations.md)**: 5 taxonomy classes for laboratory research synergy side-notes.
- **[references/omml_syntax_guide.md](references/omml_syntax_guide.md)**: DrawingML 2010 OpenXML math structure and element mappings.
- **[references/architecture_diagrams.md](references/architecture_diagrams.md)**: Vector flowchart nodes, connectors, and multi-branch layout primitives.
