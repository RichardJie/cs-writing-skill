---
name: cs-report-ppt
description: "Create conference-level academic paper presentation PPT decks from paper PDFs with 14-slide figure-dominant spine, native OMML formulas, and pure vision-in-the-loop self-inspection."
---

# CS Report PPT Skill (`cs-report-ppt`)

Transform scientific research papers (PDF) into conference-grade (NeurIPS, ICML, CVPR, ICLR, KDD, ACL), 16:9 widescreen PowerPoint presentation decks combining **dense, informative academic rigor** with **clean, minimalist visual aesthetics**.

---

## 1. Core Philosophy & Quality Standards

A premier academic presentation is **neither a wall of bullet points nor a rigid cookie-cutter template**. It is an adaptive, publication-grade visual narrative governed by five principles:

1. **Figure & Table Dominance ($\ge 80\%$ Visual Asset Coverage)**:
   - **Visuals take center stage**: At least **11 out of 14 slides** must be anchored by authentic high-resolution figures, system architectures, benchmark tables, or qualitative comparisons harvested directly from the paper PDF.
   - Never substitute speculative text where empirical visual evidence exists. Pure-text cards are strictly reserved for synthesis slides (Critical Assessment and Seminar Roadmap).
2. **Vision-Driven Adaptive Layout (量体裁衣，摒弃死板网格)**:
   - Real research figures come in diverse aspect ratios: wide panorama architectures, vertical multi-stage flowcharts, paired ablation subfigures, or dense master benchmark tables.
   - **Do not force-fit figures into rigid, hardcoded layout boxes**. The AI must inspect each harvested asset's visual geometry and tailor the slide layout dynamically (e.g., top-hero banner, asymmetric 60/40 split, side-by-side comparison, or full-width matrix).
3. **Pure Vision-in-the-Loop Feedback (以眼为准，视觉闭环自检)**:
   - **Scripts are blind; vision sees ground truth**. Layout defects, text collisions, awkward line wraps, and unbalanced white space cannot be judged by counting text characters or checking XML tags.
   - Every generated presentation must be rendered to high-DPI images and **visually audited by the AI's own multimodal vision system**. The AI inspects the rendered pixels like an expert designer, catches flaws with its own eyes, and iterates until visual perfection is reached.
4. **Semantic Visual-Text Anchoring (图文深度互文)**:
   - Text must actively dissect and interpret the visual asset rather than sitting passively beside it.
   - Bullet points must explicitly reference subfigures (e.g. `Fig. 2b`), curve inflection points, key matrix rows, and quantified deltas ($\Delta +4.8\%$, $-21\%\text{ Latency}$), delivering crisp empirical verdicts.
5. **Academic Minimalist Monochrome (`academic_mono`)**:
   - **Default Aesthetic**: High-contrast, distraction-free monochrome / grayscale.
   - Pure white background (`#FFFFFF`), pure black headers (`#000000`), deep slate body text (`#1F2937`), subtle light gray borders (`#D1D5DB`), and low-saturation neutral callouts (`#F9FAFB`).
   - Saturated banners and heavy color blocks are banned to maintain serious scholarly authority.

---

## 2. Language & Interaction Policy

- **Interactive Dialogue & Progress Reporting**: **100% 简体中文 (Chinese)**.
  - All communication, extraction summaries, architectural rationale, and visual inspection feedback must be presented in clear, professional Chinese.
- **Generated Slide Deck Content**: **100% Academic English (专业学术英文)**.
  - All slide titles, subtitles, card headers, bullet points, table text, diagram labels, and footnotes must be written in formal, publication-grade academic English.

---

## 3. The 14-Slide Figure-Dominant Academic Spine

The presentation strictly adheres to the **14-slide Session Note Spine**. Over **80% of slides** are organically paired with authentic paper visual assets:

| Slide # | Section | Category Badge | Standard Slide Title | Adaptive Visual Composition | Key Visual Asset & Empirical Focus | Marginal Callout Slot |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Header | `PAPER OVERVIEW` | `[Paper Title in Title Case]` | Dynamic Split / Hero | **Teaser / Core Trade-off Figure**: Full citation, authors, affiliations, venue/year alongside teaser dilemma diagram. | None (Metadata Grid) |
| **2** | Background (1/4) | `BACKGROUND & MOTIVATION` | `Motivation & Problem Context` | Visual Comparison Split | **Qualitative Failure Samples (Fig. 1/2)**: Visual failure modes of prior art paired with challenge breakdown. | `[State Memory Inertia]` / `[Model Adaptivity]` |
| **3** | Background (2/4) | `LITERATURE LANDSCAPE` | `Paper Classification & Taxonomy` | Multi-Column / Chart | **Taxonomy / Capacity Scaling Chart**: Methodological taxonomy, parameter bounds, or capacity trade-off plot. | None (Taxonomy Matrix) |
| **4** | Background (3/4) | `RESEARCH OBJECTIVE` | `Core Objective & Target Gap` | Asymmetric Split | **Empirical Gap Visualization**: Central hypothesis vs. 2–3 unresolved theoretical / computational bottlenecks. | None (Hypothesis Hero) |
| **5** | Background (4/4) | `HISTORICAL LINEAGE` | `Historical Evolution & Baselines` | Timeline / Table Split | **Lineage / Downsampling Comparison Table**: Evolutionary timeline (Origin $\rightarrow$ Transition $\rightarrow$ Current) + author lab background. | `[Own Lab Synergy]` |
| **6** | Methods (1/4) | `METHODOLOGY: FOUNDATIONS` | `Inputs, Assumptions & Prerequisites` | Distribution Split | **Latent Space / Spectral Analysis Plot (Fig. 4)**: Input spaces ($\mathbf{x} \in \mathbb{R}^{B \times L \times D}$), tokenization, stationarity invariants. | None (Foundational Invariants) |
| **7** | Methods (2/4) | `METHODOLOGY: FORMULATION` | `Mathematical Formulation & Objectives` | Dedicated Formula Grid | **Native OMML Master Loss Equations**: Multi-objective formulation ($\mathcal{L}_{\text{total}}$), adaptive gradient weights, parameter glossary. | None (Native OMML Formulation) |
| **8** | Methods (3/4) | `METHODOLOGY: ARCHITECTURE`| `Technical Mechanism & Architecture` | Full Architecture Split | **Main System Architecture Diagram (Fig. 3)**: High-DPI pipeline figure paired with 3-phase execution breakdown. | `[Mechanistic Interpretability]` |
| **9** | Methods (4/4) | `EXPERIMENTAL PROTOCOL` | `Experimental Design & Setup` | Protocol Grid / Table | **Benchmark Configuration Table**: Datasets, evaluation protocols, baseline suites, GPU compute budget. | None (Protocol Specs) |
| **10** | Results (1/3) | `BENCHMARK RESULTS` | `Primary Quantitative Benchmarks` | Full Benchmark Table | **Primary SOTA Benchmark Table (Table 1)**: Authentic benchmark table with bolded best metrics and percentage deltas ($\Delta$). | None (Benchmark SOTA Table) |
| **11** | Results (2/3) | `COMPARATIVE ANALYSIS` | `Comparative Evaluation & Trade-offs`| Curve / Sample Split | **Scaling Curves / Qualitative Visuals (Fig. 5)**: Multi-paradigm breakdown, Pareto throughput/quality frontier. | `[Computational & Hardware Efficiency]` |
| **12** | Results (3/3) | `ABLATION & SENSITIVITY` | `Ablation Studies & Scaling Curves` | Ablation Matrix / Table | **Component Ablation Table (Table 2)**: Stepwise contribution ablations, hyperparameter sensitivity, channel scaling. | None (Ablation Table/Curves) |
| **13** | Conclusion (1/2) | `CRITICAL ASSESSMENT` | `Core Contributions vs. Critique` | Balanced Dual Cards | **Balanced Synthesis Cards**: Author-claimed breakthroughs vs. independent critique (hidden compute, generalization bounds). | None (Balanced Critique) |
| **14** | Conclusion (2/2) | `SEMINAR DISCUSSION` | `Discussion Prompts & Lab Roadmap` | Discussion & Roadmap | **Forward Roadmap Cards**: 3 forward-looking seminar discussion questions paired with actionable 3-phase lab milestones. | `[Own Lab Synergy]` (Action Roadmap) |

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

## 5. End-to-End Vision-First Execution Loop

```
┌────────────────────────────────────────────────────────┐
│ Stage 1: Multi-Modal Harvesting & Geometry Inspection  │
│ • Extract figures, tables & diagrams at 300+ DPI       │
│ • AI visually inspects aspect ratios & visual features │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 2: Adaptive Information Architecture & Anchoring │
│ • Structure into 14-slide figure-dominant spine        │
│ • Craft analytical bullets actively dissecting visuals │
│ • Write display LaTeX math ($...$ / $$...$$)           │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 3: Adaptive Code-Driven Slide Generation         │
│ • AI dynamically codes layout tailored to figure shapes│
│ • Academic Minimalist Monochrome (pure black & white)  │
│ • Inject editable DrawingML OMML vector formulas       │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Stage 4: High-DPI Rendering & Pure Vision Inspection   │
│ • Export deck to 150+ DPI PNG slide images             │
│ • AI calls view_file on EVERY slide to SEE the layout  │
│ • Visually verify: zero collision, balance, sharpness  │
└──────────────────────────┬─────────────────────────────┘
                           │
               ┌───────────┴───────────┐
            Visual Defect Seen     Visually Flawless
               │                       │
               ▼                       ▼
┌─────────────────────────────┐   ┌───────────────────────┐
│ Stage 5: Vision-Guided Fix  │   │ Final Delivery        │
│ • Adjust code coordinates   │   │ • Deliver PPTX + PDF  │
│ • Re-render & visually audit│   │ • Embed image gallery │
└─────────────────────────────┘   └───────────────────────┘
```

### Stage 1: Multi-Modal Harvesting & Geometry Inspection
1. Read the paper PDF to understand theory, contributions, baselines, and findings.
2. **Extract 8–12 authentic figures and tables directly from the PDF at 300+ DPI** (using PyMuPDF, pdfplumber, or custom scripts).
3. **Inspect visual geometry**: Note whether each asset is wide (e.g., $W/H > 2.0$), square, tall ($W/H < 0.8$), or multi-panel. This geometry dictates the slide layout.

### Stage 2: Adaptive Information Architecture & Anchoring
1. Map harvested visual assets to the 14-slide spine.
2. For every visual slide, compose 2–3 concise bullet points that directly explain what the visual demonstrates.
3. Formulate equations in standard LaTeX (`$x_t$` for inline, `$$\mathcal{L}$$` for display).
4. Assign the 5 research connection marginal callouts.

### Stage 3: Adaptive Code-Driven Slide Generation
1. Write clean, direct presentation generation code (e.g., using `python-pptx`, `pptxgenjs`, or helper tools):
   - Canvas: Standard 16:9 widescreen ($13.333'' \times 7.500''$).
   - Colors: Pure white canvas (`#FFFFFF`), pure black headers (`#000000`), deep slate text (`#1F2937`), subtle gray card strokes (`#D1D5DB`).
   - Layout: Dynamically allocate card boundaries based on the figure's physical aspect ratio (never squeeze or distort images).
2. Inject native vector DrawingML OMML math (using `latex_to_omml.py` or native OpenXML tools) to guarantee sharp, editable typography.

### Stage 4: High-DPI Rendering & Pure Vision Self-Inspection (Mandatory)
1. Convert the generated presentation to PDF and rasterize all 14 slides to **150+ DPI PNG images** (using `soffice` and `pdftoppm` or `pymupdf`).
2. **The AI must call `view_file` to visually inspect every slide image with its own multimodal eyes**:
   - [ ] **Spatial Collision**: Look for overlapping text, equations colliding with explanation lines, or slide titles touching tracker badges.
   - [ ] **Visual Balance & Dead Space**: Check for awkward empty patches, unbalanced weight distribution, or text drowning in blank space.
   - [ ] **Aspect Ratio Integrity**: Check that figures and tables look crisp, natural, and unstretched.
   - [ ] **Legibility & Hierarchy**: Confirm that titles (22–26pt), headers (15–17pt), and body bullets (12–14pt) have crisp contrast against the white background.
3. **If any visual flaw is seen**: Modify the code coordinates, font sizes, or card boundaries, re-render, and visually inspect again. Do not stop until all 14 slides pass visual inspection.

### Stage 5: Final Delivery
1. Provide clickable links to the final `.pptx` and `.pdf` files.
2. Present the full 14-slide rendered image gallery in the conversation walkthrough for instant visual review.

---

## 6. Vision-First Inspection Rubric (What the AI's Eyes Check)

| Visual Dimension | How to Judge with AI Vision (`view_file`) | Standard for Passing |
|:---|:---|:---|
| **1. Text & Element Collision** | Scan vertical lines of sight between header, badge, formula, bullets, and footer. | **Zero collision**: Every text block, formula, and visual asset breathes with clear positive white space around it. |
| **2. Figure & Table Dominance** | Glance across the 14 slide thumbnails. | **$\ge 11$ slides feature real graphics**: At a glance, the presentation is visibly visual-first, not a wall of text. |
| **3. Asset Fidelity & Geometry** | Inspect the embedded paper figures and benchmark tables. | **Undistorted**: Circles remain circular, text in tables is crisp, aspect ratios match the original paper exactly. |
| **4. Visual Weight & Balance** | Evaluate the distribution of dark ink and white space across the 16:9 canvas. | **Harmonious density**: No giant vacant voids; cards feel purposefully filled without visual cramping. |
| **5. Scholarly Monochrome** | Check slide color distribution. | **Clean grayscale**: Distraction-free black and white palette; zero loud or neon decorative strips. |

---

## 7. Modular Accelerators & Agent Autonomy

The repository provides low-level utility scripts as accelerators:

- **`scripts/crop_figures.py`**: High-DPI PyMuPDF asset harvesting helper.
- **`scripts/latex_to_omml.py`**: LaTeX to Office Math (OMML) OpenXML vector converter and injector.
- **`scripts/build_deck.js`**: Node.js slide builder reference accelerator.
- **`resources/template_config.json`**: Palette specifications and canvas standard metrics.

> [!IMPORTANT]
> **Full Agent Autonomy**: These scripts are modular accelerators. Capable AI agents have full freedom to adapt, write custom Python/Node scripts, or use any suitable library (`python-pptx`, `pptxgenjs`, `pymupdf`, `PIL`, `matplotlib`, etc.) to achieve the highest visual standard. The sole ground truth is **what the presentation looks like in the rendered images**.
