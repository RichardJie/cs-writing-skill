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

---

## 8. 全网开源 PPT Skill 与学术汇报资料分类索引

本节为纯资料分类与路由导航索引（零 AI 自创规则），收录全网 63 个已固定 Commit SHA 与开源协议的真实 GitHub 仓库（归档于 [`upstream-skills/`](upstream-skills/)）及 120+ 份实名学者、高校通信实验室、顶会官方、资助机构与中文学术社区指南（归档于 [`curated-guides/`](curated-guides/)）。完整来源清单、Commit SHA 与外部链接总表见 [`curated-guides/SOURCES_CATALOG.md`](curated-guides/SOURCES_CATALOG.md)。

### 8.1 核心分类资料库总览

| 目录 / 索引文档 | 收录内容与来源范围 |
|:---|:---|
| [`curated-guides/SOURCES_CATALOG.md`](curated-guides/SOURCES_CATALOG.md) | 63 个开源仓库（GitHub URL、40 位 Commit SHA、License）与 4 份实名指南总目录 |
| [`curated-guides/by-scenario-group-meeting.md`](curated-guides/by-scenario-group-meeting.md) | 论文精读组会、Journal Club、文献泛读对比、科研周报与导师 1v1 进展同步（36 个实名来源） |
| [`curated-guides/by-scenario-conference-defense-grant.md`](curated-guides/by-scenario-conference-defense-grant.md) | 顶会 Oral/Spotlight/Poster、开题·中期·硕博毕业答辩、DARPA/ERC/国自然项目与人才答辩、Job Talk |
| [`curated-guides/by-discipline-guides.md`](curated-guides/by-discipline-guides.md) | CS·工程、数学·统计·理论、生医·化学、经济·金融·管理、人文·历史·社科五大学科实名学者指南 |
| [`curated-guides/by-language-typography-and-palettes.md`](curated-guides/by-language-typography-and-palettes.md) | Nature/Science/NEJM/Lancet 等期刊官方色板、Okabe–Ito/Paul Tol 无障碍色板、W3C 中英混排与中文学术排版规范 |
| [`upstream-skills/01-general-engines/`](upstream-skills/01-general-engines/) | 18 个通用演示生成引擎与可编辑重构 Skill（PPTX / Beamer / Typst Touying / Slidev / Marp / HTML） |
| [`upstream-skills/02-paper-to-slides-and-posters/`](upstream-skills/02-paper-to-slides-and-posters/) | 12 个论文转幻灯片（Paper-to-Slides）框架、科学演示 Skill 与顶会海报（Poster）模板 |
| [`upstream-skills/03-group-meeting-and-seminar/`](upstream-skills/03-group-meeting-and-seminar/) | 12 个课题组组会、Journal Club、科研周报开源 Skill 与顶尖学者实验室手册仓库 |
| [`upstream-skills/04-defense-grant-and-speaking/`](upstream-skills/04-defense-grant-and-speaking/) | 10 个开题·中期·硕博毕业答辩、Heilmeier 立项问答与 Winston/Alley 经典学术演讲 Skill 及模板 |
| [`upstream-skills/05-disciplines-and-palettes/`](upstream-skills/05-disciplines-and-palettes/) | 11 个学科专属汇报模板、期刊/色盲友好科学色板源码与中英文排版规范仓库 |

---

### 8.2 按汇报场景分类索引（汇报场景路由）

| 汇报场景 | 实名学者 / 高校 / 社区资料汇编 | 对应本地开源 Skill 与模板仓库 |
|:---|:---|:---|
| **论文精读组会 / Journal Club** | [`by-scenario-group-meeting.md`](curated-guides/by-scenario-group-meeting.md)（Part I–II：Keshav 三遍读论文法、Fatahalian Stanford CS、Celia Elliott UIUC、Schwartz 10 分钟 Journal Club、Jacobson & Raffel 角色研讨、Harvard SEAS、Stanford CS224U、李沐论文精读、科学网博导博文） | [`smallSheep123-paper-skills`](upstream-skills/03-group-meeting-and-seminar/smallSheep123-paper-skills/)、[`Zero-stargazer-group-meeting-ppt-skill`](upstream-skills/03-group-meeting-and-seminar/Zero-stargazer-group-meeting-ppt-skill/)、[`JohnJiahao-group-meeting-presentation-ppt`](upstream-skills/03-group-meeting-and-seminar/JohnJiahao-group-meeting-presentation-ppt/)、[`mlxbc12138-academic-Group-meeting-skills`](upstream-skills/03-group-meeting-and-seminar/mlxbc12138-academic-Group-meeting-skills/)、[`luoming483-BIT-group-meeting-report`](upstream-skills/03-group-meeting-and-seminar/luoming483-BIT-group-meeting-report/)、[`xiao634zhang-paper-ppt-skill`](upstream-skills/03-group-meeting-and-seminar/xiao634zhang-paper-ppt-skill/)、[`paper2ppt`](upstream-skills/02-paper-to-slides-and-posters/paper2ppt/)、[`Paper2Slides`](upstream-skills/02-paper-to-slides-and-posters/Paper2Slides/)、[`mli-paper-reading`](upstream-skills/03-group-meeting-and-seminar/mli-paper-reading/) |
| **文献泛读 / 多篇对比与综述** | [`by-scenario-group-meeting.md`](curated-guides/by-scenario-group-meeting.md)（Part III：Brown CSCI 2952-F 多文献对比骨架、Pautasso *PLOS Comp Biol* 文献综述十律、Jia-Bin Huang 相关工作分类法） | [`paper2beamer-skills`](upstream-skills/02-paper-to-slides-and-posters/paper2beamer-skills/)（含 `research-gap-analysis` 多论文对比矩阵）、[`jbhuang0604-awesome-tips`](upstream-skills/03-group-meeting-and-seminar/jbhuang0604-awesome-tips/)、[`wycmochi-cn-academic-spark`](upstream-skills/04-defense-grant-and-speaking/wycmochi-cn-academic-spark/)（Route D 文献综述） |
| **科研周报 / 导师 1v1 同步** | [`by-scenario-group-meeting.md`](curated-guides/by-scenario-group-meeting.md)（Part IV–V：中科院大连化物所李灿院士组官方 7 页周报规范、Bill Freeman MIT、高鸣宇清华交叉信息院、Mariam Aly 实验室手册、南京大学 LAMDA、浙大彭思达） | [`HughYau-zuhui-skill`](upstream-skills/03-group-meeting-and-seminar/HughYau-zuhui-skill/)、[`jbhuang0604-awesome-tips`](upstream-skills/03-group-meeting-and-seminar/jbhuang0604-awesome-tips/)、[`LAMDA-NeSy-Research-Starter-Kit`](upstream-skills/03-group-meeting-and-seminar/LAMDA-NeSy-Research-Starter-Kit/)、[`pengsida-learning-research`](upstream-skills/03-group-meeting-and-seminar/pengsida-learning-research/)、[`samuelmehr-labhandbooks`](upstream-skills/03-group-meeting-and-seminar/samuelmehr-labhandbooks/) |
| **顶会 Oral · Spotlight · Poster** | [`by-scenario-conference-defense-grant.md`](curated-guides/by-scenario-conference-defense-grant.md)（Part I–II：Winston MIT *How to Speak*、Alley *Assertion-Evidence*、Peyton Jones MSR、Doumont、Mark Hill & Patterson、ICML/CVPR/NeurIPS/ACL 官方指南、Lortie 短报告十律、Erren & Bourne / Purrington / `#betterposter` 海报规范） | [`PPTAgent`](upstream-skills/02-paper-to-slides-and-posters/PPTAgent/)、[`PPTAgent-v2-prompts`](upstream-skills/02-paper-to-slides-and-posters/PPTAgent-v2-prompts/)、[`AutoPresent`](upstream-skills/02-paper-to-slides-and-posters/AutoPresent/)、[`SlideTailor`](upstream-skills/02-paper-to-slides-and-posters/SlideTailor/)、[`scientific-agent-skills`](upstream-skills/02-paper-to-slides-and-posters/scientific-agent-skills/)、[`Paper2Poster`](upstream-skills/02-paper-to-slides-and-posters/Paper2Poster/)、[`gemini-beamerposter`](upstream-skills/02-paper-to-slides-and-posters/gemini-beamerposter/)、[`typst-poster`](upstream-skills/02-paper-to-slides-and-posters/typst-poster/)、[`rafaelbailo-betterposter-latex-template`](upstream-skills/02-paper-to-slides-and-posters/rafaelbailo-betterposter-latex-template/)、[`Gabberflast-academic-pptx-skill`](upstream-skills/01-general-engines/Gabberflast-academic-pptx-skill/) |
| **开题 · 中期 · 硕博毕业答辩** | [`by-scenario-conference-defense-grant.md`](curated-guides/by-scenario-conference-defense-grant.md)（Part III：MIT EECS 开题与资格考、MIT CEE 答辩问答、Alley & Thole 硕博答辩教程、上海交大/北京交大/华南理工/上海科大/浙大软院官方答辩细则、科学网刘进平/张忆文/马臻/唐常杰答辩指南） | [`zouchenzhen-thesis-defense-pptx-skill`](upstream-skills/04-defense-grant-and-speaking/zouchenzhen-thesis-defense-pptx-skill/)、[`Faust-Donf-beamer-academic`](upstream-skills/04-defense-grant-and-speaking/Faust-Donf-beamer-academic/)、[`wycmochi-cn-academic-spark`](upstream-skills/04-defense-grant-and-speaking/wycmochi-cn-academic-spark/)、[`w1ndys-html-ppt-academic-skill`](upstream-skills/04-defense-grant-and-speaking/w1ndys-html-ppt-academic-skill/)、[`1321dad-das-research-ppt-design-skill`](upstream-skills/04-defense-grant-and-speaking/1321dad-das-research-ppt-design-skill/)、[`Falldio-Kokura-Beamer`](upstream-skills/04-defense-grant-and-speaking/Falldio-Kokura-Beamer/) |
| **国自然 · 项目/人才答辩 · Job Talk** | [`by-scenario-conference-defense-grant.md`](curated-guides/by-scenario-conference-defense-grant.md)（Part IV–V：DARPA 官方 *Heilmeier Catechism*、ERC 面试指南、Bourne & Chalupa 基金十律、NSFC 官方四类科学问题属性、中科院秦四清职称答辩博文、MIT EECS 与 Sura et al. *Job Talk* 指南） | [`RealZYZhang-paper-reader-heilmeier`](upstream-skills/04-defense-grant-and-speaking/RealZYZhang-paper-reader-heilmeier/)、[`keyuchen21-how-to-speak-skill`](upstream-skills/04-defense-grant-and-speaking/keyuchen21-how-to-speak-skill/)、[`Arahmane1007-winston-presentations-skill`](upstream-skills/04-defense-grant-and-speaking/Arahmane1007-winston-presentations-skill/)、[`hplgit-MAlley-slide-templates`](upstream-skills/04-defense-grant-and-speaking/hplgit-MAlley-slide-templates/) |

---

### 8.3 按学科领域分类索引（学科规范路由）

| 学科领域 | 学科实名学者与学会指南章节 | 对应学科开源 Skill 与代码仓库 |
|:---|:---|:---|
| **CS · 系统 · 工程** | [`by-discipline-guides.md`](curated-guides/by-discipline-guides.md)（§4：David Patterson 反面十诫、Mark D. Hill、Jonathan Shewchuk UC Berkeley、Kayvon Fatahalian Stanford、Simon Peyton Jones MSR、Patrick Winston MIT） | [`PPTAgent`](upstream-skills/02-paper-to-slides-and-posters/PPTAgent/)、[`AutoPresent`](upstream-skills/02-paper-to-slides-and-posters/AutoPresent/)、[`SlideTailor`](upstream-skills/02-paper-to-slides-and-posters/SlideTailor/)、[`Paper2Slides`](upstream-skills/02-paper-to-slides-and-posters/Paper2Slides/)、[`Paper2Poster`](upstream-skills/02-paper-to-slides-and-posters/Paper2Poster/)、[`slidevjs-slidev-skill`](upstream-skills/01-general-engines/slidevjs-slidev-skill/)、[`hplgit-MAlley-slide-templates`](upstream-skills/04-defense-grant-and-speaking/hplgit-MAlley-slide-templates/)、[`ten-rules`](upstream-skills/05-disciplines-and-palettes/ten-rules/) |
| **数学 · 统计 · 理论科学** | [`by-discipline-guides.md`](curated-guides/by-discipline-guides.md)（§3：Paul Halmos *How to Talk Mathematics*、Terence Tao 陶哲轩博客、John E. McCarthy AMS 报告指南、Gian-Carlo Rota 十训、Karl Broman 统计图表准则） | [`beamer-skill`](upstream-skills/01-general-engines/beamer-skill/)、[`academic-beamer-skill`](upstream-skills/01-general-engines/academic-beamer-skill/)、[`touying`](upstream-skills/01-general-engines/touying/)、[`seaslides`](upstream-skills/01-general-engines/seaslides/)、[`kbroman-Talk_Graphs`](upstream-skills/05-disciplines-and-palettes/kbroman-Talk_Graphs/) |
| **生医 · 生命科学 · 化学** | [`by-discipline-guides.md`](curated-guides/by-discipline-guides.md)（§2：Philip Bourne 口头与海报双十律、Susan McConnell Stanford/iBiology、Uri Alon *Molecular Cell*、Jean-luc Doumont *Nature Scitable*、Jeffrey Leek、Prashant Kamat *ACS Energy Lett.*） | [`scientific-agent-skills`](upstream-skills/02-paper-to-slides-and-posters/scientific-agent-skills/)、[`mlxbc12138-academic-Group-meeting-skills`](upstream-skills/03-group-meeting-and-seminar/mlxbc12138-academic-Group-meeting-skills/)、[`jtleek-talkguide`](upstream-skills/05-disciplines-and-palettes/jtleek-talkguide/)、[`ggsci`](upstream-skills/05-disciplines-and-palettes/ggsci/)、[`khroma`](upstream-skills/05-disciplines-and-palettes/khroma/) |
| **经济 · 金融 · 管理 · 定量社科** | [`by-discipline-guides.md`](curated-guides/by-discipline-guides.md)（§1：Paul Goldsmith-Pinkham Yale、Jesse Shapiro Harvard 实证微观报告笔记、John Cochrane 博士生指南、Monika Piazzesi Stanford / AEA CSWEP、Marc Bellemare 22 条建议、Jonathan Schwabish *JEP*） | [`hanlulong-econ-slides-skill`](upstream-skills/05-disciplines-and-palettes/hanlulong-econ-slides-skill/)、[`paulgp-beamer-tips`](upstream-skills/05-disciplines-and-palettes/paulgp-beamer-tips/) |
| **人文 · 历史 · 文学 · 定性社科** | [`by-discipline-guides.md`](curated-guides/by-discipline-guides.md)（§5：Linda Kerber 美国历史学会 AHA 宣读规范、AHA 年会指南、现代语言学会 MLA 无障碍展示与 Access Copies 规范、Paul N. Edwards 学术报告指南） | [`Gabberflast-academic-pptx-skill`](upstream-skills/01-general-engines/Gabberflast-academic-pptx-skill/)、[`hunkim-slide-skill`](upstream-skills/01-general-engines/hunkim-slide-skill/) |

---

### 8.4 按语言、字体排版与期刊官方色板分类索引

| 语言与视觉维度 | 权威规范与社区指南章节 | 对应本地开源仓库与规范文件 |
|:---|:---|:---|
| **中文学术排版与“去 Word 化”** | [`by-language-typography-and-palettes.md`](curated-guides/by-language-typography-and-palettes.md)（§4–§5：阮一峰技术文档规范、中国科大《简约学术组会》字号与色彩体系、连享会×知乎学术 PPT 热议合集、少数派诺灰/钟多少玲排版教程、`GordenPPTSkill` 原创设计原则） | [`liano3-ustc-ppt-theme`](upstream-skills/05-disciplines-and-palettes/liano3-ustc-ppt-theme/)、[`atomiechen-THU-PPT-Theme`](upstream-skills/05-disciplines-and-palettes/atomiechen-THU-PPT-Theme/)、[`ruanyf-document-style-guide`](upstream-skills/05-disciplines-and-palettes/ruanyf-document-style-guide/)、[`wycmochi-cn-academic-spark`](upstream-skills/04-defense-grant-and-speaking/wycmochi-cn-academic-spark/)、[`w1ndys-html-ppt-academic-skill`](upstream-skills/04-defense-grant-and-speaking/w1ndys-html-ppt-academic-skill/)、[`1321dad-das-research-ppt-design-skill`](upstream-skills/04-defense-grant-and-speaking/1321dad-das-research-ppt-design-skill/) |
| **英文学术版式与图表重绘** | [`by-language-typography-and-palettes.md`](curated-guides/by-language-typography-and-palettes.md)（§3：Matthew Butterick *Practical Typography: Presentations*、Rougier et al. *PLOS Comp Biol* 2014 演讲图适配准则、Edward Tufte *Cognitive Style of PowerPoint*） | [`ten-rules`](upstream-skills/05-disciplines-and-palettes/ten-rules/)、[`kbroman-Talk_Graphs`](upstream-skills/05-disciplines-and-palettes/kbroman-Talk_Graphs/)、[`hplgit-MAlley-slide-templates`](upstream-skills/04-defense-grant-and-speaking/hplgit-MAlley-slide-templates/)、[`Gabberflast-academic-pptx-skill`](upstream-skills/01-general-engines/Gabberflast-academic-pptx-skill/) |
| **中英双语混排规范** | [`by-language-typography-and-palettes.md`](curated-guides/by-language-typography-and-palettes.md)（§4.1–§4.2：W3C `clreq`《中文排版需求》中西文间距/标点/行距条款、《中文文案排版指北》） | [`chinese-copywriting-guidelines`](upstream-skills/05-disciplines-and-palettes/chinese-copywriting-guidelines/)、[`paper2ppt`](upstream-skills/02-paper-to-slides-and-posters/paper2ppt/)、[`academic-beamer-skill`](upstream-skills/01-general-engines/academic-beamer-skill/)、[`Faust-Donf-beamer-academic`](upstream-skills/04-defense-grant-and-speaking/Faust-Donf-beamer-academic/)、[`Falldio-Kokura-Beamer`](upstream-skills/04-defense-grant-and-speaking/Falldio-Kokura-Beamer/) |
| **期刊官方色板与色觉无障碍色板** | [`by-language-typography-and-palettes.md`](curated-guides/by-language-typography-and-palettes.md)（§1–§2：NPG *Nature*、AAAS *Science*、*NEJM*、*Lancet*、*JAMA*、*JCO*、*BMJ* 精确 HEX 色值表；Okabe & Ito CUD、Bang Wong *Nature Methods* 2011、Paul Tol 无障碍色板） | [`ggsci`](upstream-skills/05-disciplines-and-palettes/ggsci/)（`R/palettes.R` 原始 HEX 定义）、[`khroma`](upstream-skills/05-disciplines-and-palettes/khroma/)（`data-raw/schemes_OkabeIto.R` 与 `schemes_PaulTol.R`） |

---

### 8.5 按技术引擎分类索引（全量 63 个本地归档开源仓库）

#### 1. PPTX / OOXML / PptxGenJS / SVG-to-DrawingML（23 个仓库）
- **通用引擎与图像重构**：[`anthropics-skills-pptx`](upstream-skills/01-general-engines/anthropics-skills-pptx/)、[`JetBrains-skills-slides`](upstream-skills/01-general-engines/JetBrains-skills-slides/)、[`hugohe3-ppt-master`](upstream-skills/01-general-engines/hugohe3-ppt-master/)、[`Gabberflast-academic-pptx-skill`](upstream-skills/01-general-engines/Gabberflast-academic-pptx-skill/)、[`ningzimu-image-to-editable-ppt-skill`](upstream-skills/01-general-engines/ningzimu-image-to-editable-ppt-skill/)、[`proyecto26-slides-ai-plugin`](upstream-skills/01-general-engines/proyecto26-slides-ai-plugin/)
- **论文转 PPTX 与海报**：[`PPTAgent`](upstream-skills/02-paper-to-slides-and-posters/PPTAgent/)、[`PPTAgent-v2-prompts`](upstream-skills/02-paper-to-slides-and-posters/PPTAgent-v2-prompts/)、[`Paper2Slides`](upstream-skills/02-paper-to-slides-and-posters/Paper2Slides/)、[`AutoPresent`](upstream-skills/02-paper-to-slides-and-posters/AutoPresent/)、[`SlideTailor`](upstream-skills/02-paper-to-slides-and-posters/SlideTailor/)、[`paper2ppt`](upstream-skills/02-paper-to-slides-and-posters/paper2ppt/)、[`scientific-agent-skills`](upstream-skills/02-paper-to-slides-and-posters/scientific-agent-skills/)、[`Paper2Poster`](upstream-skills/02-paper-to-slides-and-posters/Paper2Poster/)
- **组会与学位答辩 PPTX**：[`Zero-stargazer-group-meeting-ppt-skill`](upstream-skills/03-group-meeting-and-seminar/Zero-stargazer-group-meeting-ppt-skill/)、[`smallSheep123-paper-skills`](upstream-skills/03-group-meeting-and-seminar/smallSheep123-paper-skills/)、[`JohnJiahao-group-meeting-presentation-ppt`](upstream-skills/03-group-meeting-and-seminar/JohnJiahao-group-meeting-presentation-ppt/)、[`mlxbc12138-academic-Group-meeting-skills`](upstream-skills/03-group-meeting-and-seminar/mlxbc12138-academic-Group-meeting-skills/)、[`luoming483-BIT-group-meeting-report`](upstream-skills/03-group-meeting-and-seminar/luoming483-BIT-group-meeting-report/)、[`xiao634zhang-paper-ppt-skill`](upstream-skills/03-group-meeting-and-seminar/xiao634zhang-paper-ppt-skill/)、[`zouchenzhen-thesis-defense-pptx-skill`](upstream-skills/04-defense-grant-and-speaking/zouchenzhen-thesis-defense-pptx-skill/)、[`wycmochi-cn-academic-spark`](upstream-skills/04-defense-grant-and-speaking/wycmochi-cn-academic-spark/)、[`1321dad-das-research-ppt-design-skill`](upstream-skills/04-defense-grant-and-speaking/1321dad-das-research-ppt-design-skill/)

#### 2. LaTeX Beamer / `beamerposter` / `betterposter`（12 个仓库）
- **通用与论文转 Beamer**：[`beamer-skill`](upstream-skills/01-general-engines/beamer-skill/)、[`academic-beamer-skill`](upstream-skills/01-general-engines/academic-beamer-skill/)、[`paper2beamer-skills`](upstream-skills/02-paper-to-slides-and-posters/paper2beamer-skills/)
- **会议海报 LaTeX 模板**：[`gemini-beamerposter`](upstream-skills/02-paper-to-slides-and-posters/gemini-beamerposter/)、[`rafaelbailo-betterposter-latex-template`](upstream-skills/02-paper-to-slides-and-posters/rafaelbailo-betterposter-latex-template/)
- **答辩、周报与学科 Beamer**：[`Faust-Donf-beamer-academic`](upstream-skills/04-defense-grant-and-speaking/Faust-Donf-beamer-academic/)、[`Falldio-Kokura-Beamer`](upstream-skills/04-defense-grant-and-speaking/Falldio-Kokura-Beamer/)、[`hplgit-MAlley-slide-templates`](upstream-skills/04-defense-grant-and-speaking/hplgit-MAlley-slide-templates/)、[`HughYau-zuhui-skill`](upstream-skills/03-group-meeting-and-seminar/HughYau-zuhui-skill/)、[`hanlulong-econ-slides-skill`](upstream-skills/05-disciplines-and-palettes/hanlulong-econ-slides-skill/)、[`paulgp-beamer-tips`](upstream-skills/05-disciplines-and-palettes/paulgp-beamer-tips/)、[`kbroman-Talk_Graphs`](upstream-skills/05-disciplines-and-palettes/kbroman-Talk_Graphs/)

#### 3. Typst Touying / Typst Poster（3 个仓库）
- [`touying`](upstream-skills/01-general-engines/touying/)（官方核心引擎与内置主题）、[`seaslides`](upstream-skills/01-general-engines/seaslides/)（官方 AI 幻灯片 Skill 与高校主题库）、[`typst-poster`](upstream-skills/02-paper-to-slides-and-posters/typst-poster/)（Typst 会议海报模板）

#### 4. Slidev（Markdown + Vue，2 个仓库）
- [`slidevjs-slidev-skill`](upstream-skills/01-general-engines/slidevjs-slidev-skill/)（Slidev 官方 Skill）、[`yoanbernabeu-slidev-skills`](upstream-skills/01-general-engines/yoanbernabeu-slidev-skills/)（20 个模块化子技能）

#### 5. Marp（Markdown -> PPTX / PDF / HTML，2 个仓库）
- [`minorun365-minorun-marp-skill`](upstream-skills/01-general-engines/minorun365-minorun-marp-skill/)（Marp 叙事/版式/SVG 检查器）、[`softaworks-agent-toolkit-marp-slide`](upstream-skills/01-general-engines/softaworks-agent-toolkit-marp-slide/)（7 套 Marp CSS 主题）

#### 6. HTML / Web 幻灯片（4 个仓库）
- [`zarazhangrui-frontend-slides`](upstream-skills/01-general-engines/zarazhangrui-frontend-slides/)、[`archlizheng-frontend-slides-editable`](upstream-skills/01-general-engines/archlizheng-frontend-slides-editable/)、[`LeoYeAI-openclaw-slides`](upstream-skills/01-general-engines/LeoYeAI-openclaw-slides/)、[`w1ndys-html-ppt-academic-skill`](upstream-skills/04-defense-grant-and-speaking/w1ndys-html-ppt-academic-skill/)

#### 7. 跨引擎通用演讲法则、实验室手册、科学色板与中英排版规范仓库（17 个仓库）
- **通用设计、演讲与立项框架**：[`hunkim-slide-skill`](upstream-skills/01-general-engines/hunkim-slide-skill/)、[`keyuchen21-how-to-speak-skill`](upstream-skills/04-defense-grant-and-speaking/keyuchen21-how-to-speak-skill/)、[`Arahmane1007-winston-presentations-skill`](upstream-skills/04-defense-grant-and-speaking/Arahmane1007-winston-presentations-skill/)、[`RealZYZhang-paper-reader-heilmeier`](upstream-skills/04-defense-grant-and-speaking/RealZYZhang-paper-reader-heilmeier/)
- **顶尖学者指南与实验室手册**：[`jbhuang0604-awesome-tips`](upstream-skills/03-group-meeting-and-seminar/jbhuang0604-awesome-tips/)、[`LAMDA-NeSy-Research-Starter-Kit`](upstream-skills/03-group-meeting-and-seminar/LAMDA-NeSy-Research-Starter-Kit/)、[`pengsida-learning-research`](upstream-skills/03-group-meeting-and-seminar/pengsida-learning-research/)、[`samuelmehr-labhandbooks`](upstream-skills/03-group-meeting-and-seminar/samuelmehr-labhandbooks/)、[`mli-paper-reading`](upstream-skills/03-group-meeting-and-seminar/mli-paper-reading/)、[`jtleek-talkguide`](upstream-skills/05-disciplines-and-palettes/jtleek-talkguide/)
- **科学色板、演讲图表与中英排版规范**：[`ggsci`](upstream-skills/05-disciplines-and-palettes/ggsci/)、[`khroma`](upstream-skills/05-disciplines-and-palettes/khroma/)、[`ten-rules`](upstream-skills/05-disciplines-and-palettes/ten-rules/)、[`chinese-copywriting-guidelines`](upstream-skills/05-disciplines-and-palettes/chinese-copywriting-guidelines/)、[`ruanyf-document-style-guide`](upstream-skills/05-disciplines-and-palettes/ruanyf-document-style-guide/)、[`liano3-ustc-ppt-theme`](upstream-skills/05-disciplines-and-palettes/liano3-ustc-ppt-theme/)、[`atomiechen-THU-PPT-Theme`](upstream-skills/05-disciplines-and-palettes/atomiechen-THU-PPT-Theme/)
