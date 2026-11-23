---
name: cs-report-ppt
description: "Create conference-grade, multi-scenario, multi-disciplinary academic presentation decks (.pptx/.pdf) across group meetings, conference talks, thesis defenses, grants, and job talks in English, Chinese, or bilingual tracks with figure-dominant spines, native OMML math, 6 scholarly palettes, and pure vision-in-the-loop QA."
---

# Academic Presentation Master Skill (`cs-report-ppt`)

Transform research papers (PDFs), multi-paper reading lists, weekly experiment logs, thesis manuscripts, and grant proposals into publication-grade **16:9 widescreen (`13.333" × 7.500"`)** presentation decks combining **dense empirical rigor** with **clean scholarly visual craft**.

---

## 1. Core Philosophy & Quality Standards

A premier academic presentation is **neither a wall of bullet points nor a rigid cookie-cutter template**. It is an adaptive, publication-grade visual narrative governed by five non-negotiable principles:

1. **Figure & Table Dominance ($\ge 80\%$ Visual Asset Coverage)**:
   - **Visuals take center stage**: At least **80% of slides** (e.g., $\ge 11$ out of 14 slides in the canonical spine) must be anchored by authentic high-resolution figures (300+ DPI), native vector system architectures, curated `booktabs` benchmark tables, or empirical plots harvested directly from source artifacts.
   - Never substitute speculative prose walls where empirical visual evidence exists. Pure-text synthesis cards are strictly reserved for critical assessment, blocker decisions, or roadmap slides.
2. **Vision-Driven Adaptive Layout (量体裁衣，摒弃死板网格)**:
   - Real research visuals span diverse aspect ratios ($R = W / H$): ultra-wide panorama pipelines ($R > 2.0$), standard landscape plots ($1.15 \le R \le 2.0$), square matrices ($0.85 \le R < 1.15$), or tall portrait flowcharts ($R < 0.85$).
   - **Never force-fit figures into incompatible hardcoded boxes**. Measure each harvested asset's pixel geometry first and route dynamically to the matching coordinate layout recipe (e.g., top-hero panorama, 62/38 or 65/35 asymmetric split, tall left-portrait split, or full-width focal matrix) with isotropic `fitContain` scaling.
3. **Pure Vision-in-the-Loop Feedback (以眼为准，视觉闭环自检)**:
   - **Scripts are blind; vision sees ground truth**. Text collisions, CJK orphan line wraps, OMML integral clipping, stretched circles, and awkward dead whitespace cannot be caught by counting characters or checking XML tags alone.
   - Every generated deck must be rendered to **150+ DPI PNG slide images** (`LibreOffice` + `PyMuPDF`) and **visually audited slide-by-slide via `view_file`**. The AI inspects rendered pixels with its own multimodal eyes and iterates coordinates/copy until zero defects remain.
4. **Semantic Visual-Text Anchoring (图文深度互文)**:
   - Slide titles use **Assertion-Evidence claim headlines** (stating *what is true and by how much*, never passive topic labels like `"Experimental Results"` or `"实验分析"`).
   - Micro-bullets actively dissect the visual asset beside them, pointing explicitly to subfigures (`Fig. 2b`), curve inflections, focal table rows, and quantified deltas ($\Delta +4.8\%$, $2.8\times\text{ Speedup}$, $p < 0.001$).
5. **Academic Minimalist Monochrome (`academic_mono` Default) & Anti-AI-Slop Craft**:
   - **Default Aesthetic (`academic_mono`)**: Pure white canvas (`#FFFFFF`), crisp black headers (`#000000`), deep slate body text (`#1F2937`), subtle `1pt` gray borders (`#D1D5DB`), and neutral callouts (`#F9FAFB`)—keeping 100% chromatic focus on authentic paper figures.
   - **Zero AI Visual Slop**: Strictly ban purple-indigo SaaS gradients, emoji bullet soup (`🚀🔥💡`), DALL-E sci-fi brain clipart, nested box-in-box clutter, 1990s heavy colored title banners, vertical table gridlines, and dead `"Thank You / 感谢聆听"` final slides.

---

## 2. Multi-Axis Skill Router (`Scenario × Discipline × Language × Palette/Engine`)

Before generating a deck, lock coordinates along **four orthogonal axes** from explicit user tags (combinable in any order, e.g., `$cs-report-ppt :journal-club :cs :bilingual`, `$cs-report-ppt :phd-defense :biomed :zh :oxford_navy`, `$cs-report-ppt :oral :econ :en`) or **automatic artifact/prompt detection** when tags are omitted, then load **only** the required progressive-disclosure modules from `references/`.

### Axis 1: Presentation Scenario Router (`Scenario` $\rightarrow$ Spine & Pacing)

| Tag(s) | Scenario (CN / EN) | Target Slides & Slot | Signature Structural Modules | Load Reference Playbook(s) |
|:---|:---|:---|:---|:---|
| `:journal-club` `:paper` *(Default for 1 PDF)* | **论文精读组会** / Single-Paper Deep-Dive | **14–18 slides** (20–45 min) | Canonical 14-slide figure-dominant spine + `plain`-style **Toy Numerical Walkthrough** + **5-Axis Reproduction Audit** + **5 Lab Synergy Callouts (`旁注`)** | [spine_template.md](references/spine_template.md), [scenarios-group-meeting.md](references/scenarios-group-meeting.md), [marginal_annotations.md](references/marginal_annotations.md) |
| `:survey` `:lit-sweep` | **文献泛读 / 专题综述组会** / Multi-Paper Literature Sweep | **12–16 slides** (20–35 min) | Unified Notation + **3-Level MECE Taxonomy Tree** + Causal Bottleneck Lineage + **6-Col Cross-Paper Matrix** (`★ Target Gap` row) + 2-Week MVP (*bans sequential paper laundry lists*) | [scenarios-group-meeting.md](references/scenarios-group-meeting.md) |
| `:weekly` `:progress` | **科研周报 / 进展汇报** / Weekly Lab Progress Report | **6–10 slides** + backup (8–15 min) | **BLUF Continuity Scorecard** + Hypothesis $H_1/H_0$ + **4-Branch MECE Failure Diagnosis Tree** (`Ruled Out` vs `Confirmed`) + **Option A/B Blocker Decisions** + SMART Gates (*bans `苦劳流水账`*) | [scenarios-group-meeting.md](references/scenarios-group-meeting.md) |
| `:oral` | **顶会 Oral 报告** / Conference Oral Talk | **12–15 slides** (12–15 min) | Author-voice 30/50/20 arc, Toy "Aha!" Insight by Min 3, Dual-layer video + 3-keyframe static fallback, **Contributions + QR Lingering Q&A Slide** | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |
| `:spotlight` `:poster-teaser` | **Spotlight (3–5m) & Poster Teaser / Madness (1–2m)** | **4–7** or **1–3 slides** | Surgical 5-slide Spotlight cut or 1-min **Inverted Paper Arc** (show jaw-dropping result at 15s) + Giant **Poster Board `#ID` & QR CTA** | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |
| `:proposal` `:midterm` | **开题报告 / Qualifying** & **中期考核 / Mid-Term** | **16–22** (开题) / **14–18** (中期) | **开题**: `研究内容` vs `拟解决关键科学问题` separation, 5-Col Paradigm Gap Matrix, Pilot proof, Aim fallbacks.<br>**中期**: `开题计划对照完成度矩阵` (Plan-vs-Actual Scorecard) + blocker adjustment | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |
| `:master-defense` `:phd-defense` | **硕士 / 博士毕业答辩** / Thesis & Dissertation Defense | **22–28** (MS) / **36–46** (PhD) + `B1–B6` | Persistent `Y: 0.00"–0.32"` Breadcrumb Bar + **4-Tier Master Technical Roadmap (`总体技术路线图`)** spotlighting (`消除三篇小论文拼凑感`), 6-slide closed-loop chapters, chapter-mapped **`成果矩阵`**, `致谢` $\rightarrow$ hyperlinked **Q&A Backup Hub (`B1–B6` incl. `盲审修改对照`)** | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |
| `:nsfc` `:grant` `:key-rd` `:industry` | **国自然 NSFC / 重点研发验收 / 企业横向课题 / NSF·ERC** | **16–22** (NSFC) / **22–28** (重点研发) / **10–15** (横向) | **NSFC**: Academic Label + `四大科学问题属性` + **1-Slide Representative Work Cards** (`独立贡献界定` + Fellow citations).<br>**重点研发**: Verbatim `《任务书》` KPI scorecard + CPA fiscal audit.<br>**横向**: `算法指标 ⇄ 业务ROI` dual-metric translation | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |
| `:award` `:job-talk` | **国奖 / 优博答辩 (3–5m)** & **50-Min Faculty Job Talk** | **5–10** (国奖) / **38–46** (Job Talk) | **国奖**: Slide 1 **Quantitative Portrait Hero Dashboard** + 3-stage coherent storyline.<br>**Job Talk**: **Hourglass Comprehension Curve** (Past 2D Portfolio Map $\rightarrow$ Flagship Deep Dives $\rightarrow$ 3-Yr/10-Yr Fundable Lab Vision, Teaching & Dept Fit) | [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) |

### Axis 2: Academic Discipline Visual Grammar Router (`Discipline` $\rightarrow$ Evidentiary Standards)

| Tag(s) | Discipline Cluster | Core Domain Visual, Table & Formula Grammar | Load Discipline Module(s) |
|:---|:---|:---|:---|
| `:cs` `:ai` `:systems` `:security` | **Computer Science, AI/ML, Systems & Security** *(NeurIPS, CVPR, ACL, OSDI, S&P)* | Clean L-to-R architecture (`❄️ FROZEN` vs `✦ NOVEL`), floating tensor dimension pills + progressive tensor lifecycle tables, explicit `[TCB]` + `In/Out-of-Scope` security maps, pruned `≤8×7` `booktabs` SOTA tables (**bold** 1st, <u>underline</u> 2nd, `Δ` col), cumulative ablation ladders, Pareto/CDF/Roofline plots | [disciplines-stem.md](references/disciplines-stem.md), [architecture_diagrams.md](references/architecture_diagrams.md) |
| `:math` `:stats` `:theory` | **Mathematics, Statistics, Optimization & TCS** *(STOC, COLT, AoS, SIOPT)* | **Halmos–Tao Intuition-First 4-Stage Pipeline**: `2D/Small-n Toy Example` $\rightarrow$ `Semantic Color-Annotated OMML Equation + Leader Pills` $\rightarrow$ `Clean Õ(·) Hero Theorem Card w/ Assumption Pills` $\rightarrow$ `Vector Proof Dependency DAG + Single Magic Lemma` (**bans `>3`-line proof walls**) | [disciplines-stem.md](references/disciplines-stem.md), [omml_syntax_guide.md](references/omml_syntax_guide.md) |
| `:physics` `:ee` `:ic` `:robotics` | **Physics, EE, Semiconductors/IC, Control & Robotics** *(ISSCC, CDC, ICRA, PRL)* | Hierarchical L-to-R signal-flow + bottom feedback blocks (*bans raw Cadence/Simulink dumps*), ISSCC paired **Die Micrograph + Floorplan** haloed callouts & transposed Schreier/Walden FoM tables, stacked Bode (`GM/PM`) & Lyapunov + `y(t)/e(t)/u(t)` stacks, `≥2pt` physics error bars + residuals, real-robot timestamped filmstrips + `ms` latency budget bars | [disciplines-stem.md](references/disciplines-stem.md) |
| `:biomed` `:clinical` `:chem` | **Biomedical, Clinical Medicine, Neuro, Bioinfo & Chemistry** (*Cell*, *Nature*, *NEJM*, *JACS*) | Multi-panel *Cell*/*Nature* sub-panel crop/mask surgery (*zero 10-panel raw dumps*), mandatory `µm` scale bars, Western blot `kDa` + loading controls + SuperPlots, 4-stage vector CONSORT, **Kaplan-Meier curves keeping aligned `No. at Risk` table**, fMRI MNI coords, curated $2\times 4$ substrate scope grids + unsuccessful substrate box | [disciplines-biomed-econ-humanities.md](references/disciplines-biomed-econ-humanities.md) |
| `:econ` `:finance` `:mgmt` | **Economics, Finance, Management & CSS** (*AER*, *QJE*, *JF*, *AMJ*, 《经济研究》) | Magnitude preview by Slide 2, vector **Causal DAGs**, DID dynamic event-study (`k = -1` pinned) / IV `binscatter` (`KP F`) / RDD `rdplot` (`McCrary p`), **6-Step Stata-to-5-Row Focal Regression Surgery** (`FE: ✓`, `(Clustered SE)`, **`Dep. Var. Mean`**), `±1 SD` moderation slopes, de-cluttered SEM paths | [disciplines-biomed-econ-humanities.md](references/disciplines-biomed-econ-humanities.md) |
| `:humanities` `:law` `:qual` | **Humanities, Law, History, Education & Qualitative** (*AHR*, *HLR*, *AERA*, 《历史研究》) | Primary text as visual artifact: high-DPI **Archival Facsimile + `≤45`-word Bilingual Close-Reading Card** (serif original + sans translation + 4-item provenance), statutory operative-clause highlight boxes, native **3-Col Gioia / 扎根理论三级编码** chevron flows, orthogonal $2\times 2$ conceptual matrices, `Cohen's d` OMML cards | [disciplines-biomed-econ-humanities.md](references/disciplines-biomed-econ-humanities.md) |

### Axis 3: Language & Bilingual Typography Policy (`Language Track`)

- **Interactive User Dialogue & Reporting**: Default **100% 简体中文** (or match user's prompt language) for extraction summaries, architecture rationale, and Stage 4 visual inspection reports.
- **Generated Slide Deck Language Track** — lock **one** pure track per deck (see full micro-copy & XML font rules in [languages-and-typography.md](references/languages-and-typography.md) and [typography_rules.md](references/typography_rules.md)):
  1. **`:en` (`en_academic` — 100% Academic English)**: Default for international conferences, English journal clubs, and global job talks. Left-aligned Sentence-case Assertion-Evidence headlines (`8–13 words`), `≤12`-word bold-anchored micro-bullets, `Arial` / `Segoe UI` + `Cambria Math`, **zero CJK characters or full-width punctuation on canvas**.
  2. **`:zh` (`zh_academic` — 100% 规范学术中文)**: Default for 开题/中期/硕博答辩、国自然/重点研发/横向/国奖、中文课题组周报. Enforces **5-Step De-Wordification Surgery (`去Word化五步手术`)**, single-line conclusion titles (`14–22字`) + symmetric 4/6/8-char verb-object headers, explicit OpenXML `<a:ea>` (`Source Han Sans SC` / `Microsoft YaHei`) + `<a:latin>` (`Segoe UI` / `Arial`) dual-script binding, W3C Pangu spacing, 3-tier English domain-term preservation, **strict zero Chinese italics (`italic: false`)**, and `+1~2pt` / `1.30–1.40x` optical CJK compensation.
  3. **`:bilingual` (`zh_en_hybrid` — 中英双语混合组会)**: Ideal for domestic lab reading groups dissecting English top-tier papers. Uses crisp Chinese conclusion headlines and analytical micro-bullets alongside **un-translated 300+ DPI original English paper figures/tables** and canonical English technical anchors.

### Axis 4: Curated Palettes, Coordinate Layouts & Generation Engines

1. **6 Curated Scholarly HEX Palettes** (full WCAG tokens & chart series in [palettes-and-layouts.md](references/palettes-and-layouts.md) and [resources/template_config.json](resources/template_config.json); 5 light palettes enforce a pure `#FFFFFF` canvas so white-background PDF crops blend seamlessly under the **70/25/5 Ink Budget**):
   - `:academic_mono` *(Default)*: Publication Monochrome (`#000000` / `#111827` on `#FFFFFF`) — universal for figure-rich CS/Math/Theory decks.
   - `:oxford_navy`: Institutional Deep Navy & Crimson Point (`#002147` / `#1D4ED8`, `#B91C1C` focal delta) — Thesis Defenses, NSFC Grants, Economics, NeurIPS/ACL.
   - `:nature_slate_teal`: Journal Slate & NPG Teal (`#0F3D3E` / `#0F766E`, `#C2410C` delta) — Biomedical, Clinical, Chemistry, ICML, AI4Science.
   - `:mit_crimson_neutral`: Engineering Crimson & Warm Stone (`#18181B` / `#A31F34`, `#0369A1` counter) — Systems, Hardware/IC, Robotics, Physics, Job Talks.
   - `:cvpr_clean_blue`: Crisp IEEE/CVF Cobalt (`#0F172A` / `#0284C7`, `#B45309` delta) — Computer Vision, Graphics, Medical Imaging, Industry Grants.
   - `:keynote_dark_oral`: Dark Slate Stage (`#F8FAFC` / `#38BDF8` on `#0F1117`) — Auditorium Keynotes/Spotlights (*mandatory rounded `#FFFFFF` matte plates behind white-bg PDF figures*).
   - *(Legacy conference theme IDs `neurips`, `icml`, `cvpr`, `iclr`, `kdd` remain 100% supported in `build_deck.js` and `template_config.json`.)*
2. **5 Deterministic Generation Engine Tracks** (full routing & code patterns in [open-source-skills-and-engines.md](references/open-source-skills-and-engines.md)):
   - **Track A (Primary `.pptx`)**: Node.js `PptxGenJS` ([scripts/build_deck.js](scripts/build_deck.js) or custom `.js`) + [scripts/latex_to_omml.py](scripts/latex_to_omml.py) + [scripts/crop_figures.py](scripts/crop_figures.py).
   - **Track B (Pure-Python `.pptx` Fallback)**: `python-pptx` + `latex_to_omml.py --inject` + `PyMuPDF` inside the user's existing Conda environment (*never create `venv`/`.venv`*).
   - **Track C (University/Agency `.pptx`/`.potx` Master Surgery)**: `python-pptx` template load / OOXML ZIP surgery preserving official crests & masters while pruning unused ghost placeholders.
   - **Track D (`Typst + Touying` / `LaTeX Beamer`) & Track E (`Slidev` / `Marp`)**: Activate **only** when pure-PDF typesetting or live-code browser slides are explicitly requested (never export flat rasterized screenshots when editable `.pptx` is expected).

### Complete 12-Module Reference Index (`references/`)

| Reference File | Core Scope & When to Read |
|:---|:---|
| [references/open-source-skills-and-engines.md](references/open-source-skills-and-engines.md) | 5-track engine selector (`PptxGenJS` vs `python-pptx` vs OOXML vs Typst/Beamer), 300+ DPI figure harvesting, OMML pipeline, LibreOffice+PyMuPDF Vision QA, and **25-Point Defect Audit Checklist**. |
| [references/scenarios-group-meeting.md](references/scenarios-group-meeting.md) | Internal lab playbooks: **Single-Paper Deep-Dive** (14–18 slides + Toy Walkthrough + Repro Audit), **Literature Survey** (MECE Tree + Master Matrix), and **Weekly Progress Report** (BLUF + Fault Tree + A/B Decisions). |
| [references/scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md) | External high-stakes playbooks: **Oral / Spotlight / Poster Teaser**, **开题 / 中期 / 硕博毕业答辩** (Master Roadmap + Breadcrumb + `成果矩阵` + Backup `B1–B6`), **NSFC / 重点研发 / 横向 / 国奖**, and **50-Min Faculty Job Talk**. |
| [references/disciplines-stem.md](references/disciplines-stem.md) | STEM visual grammar: **CS/AI/Systems/Security** (pipelines, tensor pills, TCB, SOTA/ablation tables), **Math/Stats/Opt/TCS** (Halmos–Tao 4-stage theorem & Proof DAGs), and **Physics/EE/IC/Control/Robotics** (FoM, die photos, Bode, robot strips). |
| [references/disciplines-biomed-econ-humanities.md](references/disciplines-biomed-econ-humanities.md) | Non-CS/EE visual grammar: **BioMed/Clinical/Chem** (panel surgery, blots, CONSORT, KM `No. at Risk`, ChemDraw scope), **Econ/Finance/Mgmt** (DAGs, event studies, 5-row Stata surgery), and **Humanities/Law/Qual** (archival cards, Gioia flows). |
| [references/languages-and-typography.md](references/languages-and-typography.md) | Track 1 (`en_academic` Assertion headlines & `≤12`-word micro-bullets) and Tracks 2/3 (`zh_academic` & `zh_en_hybrid` 去Word化五步手术, `<a:latin>`+`<a:ea>` dual-font binding, Pangu spacing, zero-CN-italic rule). |
| [references/palettes-and-layouts.md](references/palettes-and-layouts.md) | **6 curated scholarly HEX palettes**, **10 Anti-AI-Slop visual laws**, aspect-ratio `fitContain` math, and **12 collision-free `(x, y, w, h)` coordinate layout recipes** on `13.333" × 7.500"`. |
| [references/spine_template.md](references/spine_template.md) | Per-slide blueprint (Slides 1–14), narrative roles, visual inspection gates, and character/occupancy budgets for the canonical 14-slide `Session Note` spine. |
| [references/typography_rules.md](references/typography_rules.md) | Foundational 16:9 EMU/inch coordinate math, 3 non-overlapping vertical zones (`Header` / `Content` / `Footer`), 7 core deterministic card grid models, and 9-level typography hierarchy. |
| [references/omml_syntax_guide.md](references/omml_syntax_guide.md) | Office Math Markup Language (`<a14:m><m:oMath>` / `<m:oMathPara>`) OpenXML specification, 22-construct LaTeX-to-OMML mapping matrix, Unicode symbol maps, and two-phase injection protocol. |
| [references/architecture_diagrams.md](references/architecture_diagrams.md) | Native DrawingML vector flowchart & diagram specification (`Novel` vs `Baseline` vs `Terminal` vs `Data Tensor` primitives, JSON IR `diagram` schema, and `>10 <p:sp>` verification invariants). |
| [references/marginal_annotations.md](references/marginal_annotations.md) | Canonical specification, `split_65_35` right-card geometry (`x=8.600", w=4.133", h=5.200"`), and JSON IR templates for the 5-Class Laboratory Research Synergy callouts (`旁注`). |

---

## 3. The Canonical 14-Slide Figure-Dominant Academic Spine

For single-paper presentations (`:journal-club` / baseline mode), the deck adheres to the **14-slide Session Note Spine** (expandable to 16–18 slides with Toy Numerical Walkthrough & Reproduction Audit per [scenarios-group-meeting.md](references/scenarios-group-meeting.md)). Over **80% of slides ($\ge 11/14$)** are organically paired with authentic visual assets:

| Slide # | Section | Category Badge | Standard Slide Title (or Assertion Claim) | Adaptive Visual Composition | Key Visual Asset & Empirical Focus | Marginal Callout Slot |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Header | `PAPER OVERVIEW` | `[Paper Title in Title Case]` | `title_hero_split` / `hero_1col` | **Teaser / Core Trade-off Figure**: Full citation, authors, affiliations, venue/year alongside teaser dilemma diagram. | None (Metadata Grid) |
| **2** | Background (1/4) | `BACKGROUND & MOTIVATION` | `Motivation & Problem Context` | `split_65_35` / `62_38` | **Qualitative Failure Samples (Fig. 1/2)**: Visual failure modes of prior art paired with challenge breakdown. | `[State Memory Inertia]` / `[Model Adaptivity]` |
| **3** | Background (2/4) | `LITERATURE LANDSCAPE` | `Paper Classification & Taxonomy` | `grid_3col` / Chart | **Taxonomy / Capacity Scaling Chart**: Methodological taxonomy, parameter bounds, or capacity trade-off plot. | None (Taxonomy Matrix) |
| **4** | Background (3/4) | `RESEARCH OBJECTIVE` | `Core Objective & Target Gap` | `split_equal_2col` | **Empirical Gap Visualization**: Central hypothesis vs. 2–3 unresolved theoretical / computational bottlenecks. | None (Hypothesis Hero) |
| **5** | Background (4/4) | `HISTORICAL LINEAGE` | `Historical Evolution & Baselines` | `split_65_35` / Panorama | **Lineage / Comparison Timeline**: Evolutionary progression (`Origin → Transition → Current`) + author lab continuity. | `[Own Lab Synergy]` |
| **6** | Methods (1/4) | `METHODOLOGY: FOUNDATIONS` | `Inputs, Assumptions & Prerequisites` | `split_65_35` / `50_50` | **Latent / Spectral / Setup Plot**: Input spaces ($\mathbf{x} \in \mathbb{R}^{B \times L \times D}$), preconditions, regularity invariants. | None (Foundational Invariants) |
| **7** | Methods (2/4) | `METHODOLOGY: FORMULATION` | `Mathematical Formulation & Objectives` | `formula_omml_workbench` | **Native OMML Master Equations**: Multi-objective formulation ($\mathcal{L}_{\text{total}}$), term roles, symbol glossary. | None (Native OMML Formulation) |
| **8** | Methods (3/4) | `METHODOLOGY: ARCHITECTURE` | `Technical Mechanism & Architecture` | `panorama_arch` / `split_65_35` | **Main System Architecture Diagram (Fig. 3)**: High-DPI pipeline figure paired with 3-phase execution breakdown. | `[Mechanistic Interpretability]` |
| **9** | Methods (4/4) | `EXPERIMENTAL PROTOCOL` | `Experimental Design & Setup` | `grid_3col` / Table | **Benchmark Configuration Table**: Datasets, evaluation protocols, baseline suites, compute/cohort budget. | None (Protocol Specs) |
| **10** | Results (1/3) | `BENCHMARK RESULTS` | `Primary Quantitative Benchmarks` | `benchmark_table_kpi_strip` | **Primary SOTA Benchmark Table (Table 1)**: Curated focal table with bolded best metrics, underlined 2nd, and deltas ($\Delta$). | None (Benchmark SOTA Table) |
| **11** | Results (2/3) | `COMPARATIVE ANALYSIS` | `Comparative Evaluation & Trade-offs` | `split_65_35` / `62_38` | **Scaling Curves / Pareto Frontier (Fig. 5)**: Multi-paradigm breakdown, throughput/cost vs. quality frontier. | `[Computational & Hardware Efficiency]` |
| **12** | Results (3/3) | `ABLATION & SENSITIVITY` | `Ablation Studies & Scaling Curves` | `quadrant_2x2` / Ladder | **Component Ablation Matrix (Table 2)**: Stepwise contribution ablations, hyperparameter sensitivity, failure edge cases. | None (Ablation Table/Curves) |
| **13** | Conclusion (1/2) | `CRITICAL ASSESSMENT` | `Core Contributions vs. Critique` | `split_equal_2col` | **Balanced Synthesis Cards**: Author-claimed breakthroughs vs. independent critique (hidden costs, validity bounds). | None (Balanced Critique) |
| **14** | Conclusion (2/2) | `SEMINAR DISCUSSION` | `Discussion Prompts & Lab Roadmap` | `split_65_35` | **Forward Roadmap Cards**: 3 forward-looking seminar discussion questions paired with actionable 3-phase lab milestones. | `[Own Lab Synergy]` (Action Roadmap) |

---

## 4. 5-Class Laboratory Research Synergy Taxonomy ("旁注")

Internal seminar presentations actively connect external papers to laboratory research agendas via right-hand `split_65_35` marginal callouts (`x = 8.600", y = 1.650", w = 4.133", h = 5.200"`, `0.08"` left accent bar; full spec in [marginal_annotations.md](references/marginal_annotations.md)):

1. **`[State Memory Inertia]`** *(Slide 2 or 6 — STEM/Bio/Econ equivalent: `[State / Pathway Dynamics]`)*:
   - *Focus*: Recurrent state retention, KV cache dynamics, context compression, Markov/signaling persistence.
   - *Lab Link*: Connects state bottlenecks directly to in-house long-horizon modeling or experimental dynamics.
2. **`[Model Adaptivity / Generalization]`** *(Slide 2 or 4 — equivalent: `[Adaptivity & External Validity]`)*:
   - *Focus*: Distribution shift resilience, OOD generalization, test-time adaptation, PVT/cross-cohort robustness.
   - *Lab Link*: Maps robustness mechanisms to internal perturbed benchmarks or target populations.
3. **`[Mechanistic Interpretability]`** *(Slide 8 — equivalent: `[Mechanistic / Causal Lens]`)*:
   - *Focus*: Representation geometry, attention circuit routing, physical field coupling, biological rescue, or IV/DID identification validity.
   - *Lab Link*: Audits *why* the mechanism works beyond leaderboard correlation.
4. **`[Computational & Hardware Efficiency]`** *(Slide 11 — equivalent: `[Compute & Resource Cost]`)*:
   - *Focus*: FLOP/VRAM reduction, quantization, kernel fusion, silicon FoM, robot loop latency, or wet-lab reagent/cohort cost.
   - *Lab Link*: Evaluates concrete deployment or replication feasibility within our laboratory budget.
5. **`[Own Lab Synergy]`** *(Slide 5 or 14)*:
   - *Focus*: Direct codebase module migration, baseline upgrade, assay/identification transfer, and a time-bounded 3-stage roadmap (`Week 1 Reproduction → Week 2 Integration → Week 3 Hypothesis Test`).

*(Note: In external author-voice scenarios such as `:oral`, `:phd-defense`, `:nsfc`, or `:job-talk`, replace external reader `旁注` cards with author evidence callouts, attribution badges, or take-home KPI strips per [scenarios-conference-defense-grant.md](references/scenarios-conference-defense-grant.md).)*

---

## 5. End-to-End 5-Stage Vision-in-the-Loop Execution Loop

```
┌─────────────────────────────────────────────────────────────┐
│ Stage 1: Multi-Modal Harvesting & Geometry Inspection       │
│ • Lock 4-Axis Route (Scenario × Discipline × Lang × Theme)  │
│ • Extract figures/tables at 300+ DPI & inspect R = W / H    │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 2: Adaptive Information Architecture & Anchoring      │
│ • Structure into scenario spine & aspect-matched layouts    │
│ • Craft Assertion-Evidence headlines & anchored micro-copy  │
│ • Formulate LaTeX math ($...$ / <<MATH_DISPLAY:...>>)       │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 3: Adaptive Code-Driven Slide Generation              │
│ • Generate native 16:9 PPTX (Track A/B/C) or PDF (Track D)  │
│ • Enforce dual-script fonts (<a:latin> + <a:ea>) & palette  │
│ • Inject editable OpenXML <a14:m> OMML vector equations     │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 4: High-DPI Rendering & Pure Vision Inspection        │
│ • Run verify_deck.py XML pre-check (zero leaked math tags)  │
│ • Render PPTX -> PDF -> 150+ DPI PNGs (soffice + PyMuPDF)   │
│ • Call view_file on EVERY slide PNG to inspect pixels       │
└─────────────────────────────┬───────────────────────────────┘
                              │
                  ┌───────────┴───────────┐
               Visual Defect Seen     Visually Flawless
                  │                       │
                  ▼                       ▼
┌───────────────────────────────┐   ┌─────────────────────────┐
│ Stage 5A: Vision-Guided Fix   │   │ Stage 5B: Final Delivery│
│ • Adjust coordinates/copy/eqH │   │ • Deliver PPTX + PDF    │
│ • Re-render & re-audit PNGs   │   │ • Present slide gallery │
└───────────────────────────────┘   └─────────────────────────┘
```

### Stage 1: Multi-Modal Harvesting & Geometry Inspection
1. Classify the request across the **4-Axis Router** and read the corresponding `references/*.md` modules.
2. Parse the source PDF(s) or research artifacts; **extract 8–12 authentic figures/tables at 300+ DPI** using [scripts/crop_figures.py](scripts/crop_figures.py) (`--auto` followed by `--page P --bbox` refinement if multi-panel subfigures need clean slicing).
3. **Inspect every extracted `.png` with `view_file`** and compute $R = W_{\text{px}} / H_{\text{px}}$ to drive layout selection (never leave clipped axis labels or tiny prose captions attached to cropped images).

### Stage 2: Adaptive Information Architecture & Anchoring
1. Map visual assets onto the selected scenario spine (ensuring no 3 consecutive slides repeat an identical 3-column Bento grid).
2. Write declarative **Assertion-Evidence claim headlines** and `≤12`-word (EN) / `≤22`-char (CN) anchored micro-bullets referencing explicit subfigures, rows, and $\Delta$ metrics.
3. Author display and inline equations in standard LaTeX (`{{MATH_DISPLAY:...}}` / `$...$`) paired with symbol glossaries or physical intuition lines.

### Stage 3: Adaptive Code-Driven Slide Generation
1. Build the 16:9 deck (`13.333" × 7.500"`) via `PptxGenJS` ([scripts/build_deck.js](scripts/build_deck.js) or custom builder) or `python-pptx`, enforcing isotropic `fitContain` image scaling and explicit `<a:latin>` + `<a:ea>` font binding for Chinese/bilingual decks.
2. Inject native vector DrawingML OMML math via [scripts/latex_to_omml.py](scripts/latex_to_omml.py) (`--inject`) with dynamic vertical equation height budgeting ($H_{\text{eq}} \in [0.60'', 1.55'']$).

### Stage 4: High-DPI Rendering & Pure Vision Self-Inspection (Mandatory)
1. Run [scripts/verify_deck.py](scripts/verify_deck.py) as an OpenXML pre-filter (`0` leaked `<<MATH_` / `{{MATH:` tokens, valid `<a14:m>` nodes).
2. Convert `.pptx` $\rightarrow$ `.pdf` via isolated headless LibreOffice (`soffice --headless -env:UserInstallation=... --convert-to pdf` with explicit timeout) and rasterize **all slides to 150+ DPI PNGs** via `PyMuPDF` (`fitz`) or `pdftoppm`.
3. **Call `view_file` on EVERY rendered slide PNG** to inspect pixels directly:
   - [ ] **Spatial Collision**: Zero overlap between tracker, headline, subtitle, divider (`y = 1.50"`), cards (`y ∈ [1.65", 6.85"]`), OMML bounds, and footer (`y = 7.00"`).
   - [ ] **Visual Balance & Dead Space**: Harmonious `70%–88%` card occupancy; zero half-empty voids from mismatched figure aspect ratios.
   - [ ] **Aspect Ratio & Crop Fidelity**: Circles remain circular, embedded table fonts are crisp and unstretched, scale bars and `No. at Risk` tables are intact.
   - [ ] **Typography & Bilingual Hygiene**: Auditorium-safe font floors (`≥12pt` EN / `≥13–16pt` CN), zero CJK tofu (`□`), zero Chinese italics, clean Pangu spacing.
   - [ ] **Anti-Slop & Palette Discipline**: Pure `#FFFFFF` seamless figure blending (or rounded white matte plates on `keynote_dark_oral`), zero gradients/emojis, and an actionable lingering final slide.
4. **Iterate until flawless**: If any visual defect appears, adjust coordinates, layout recipe, or bullet length, re-render, and re-inspect via `view_file`.

### Stage 5: Final Delivery
1. Clean up intermediate build files (`*_stage1.pptx`, temporary LibreOffice profiles, `__pycache__`).
2. Provide clickable links to the final `.pptx` and `.pdf` deliverables alongside a concise visual walkthrough summary.

---

## 6. Vision-First Inspection Rubric (What the AI's Eyes Check)

*(For the exhaustive 25-checkpoint engineering audit, see §8 of [open-source-skills-and-engines.md](references/open-source-skills-and-engines.md).)*

| Visual Dimension | How to Judge with AI Vision (`view_file`) | Standard for Passing |
|:---|:---|:---|
| **1. Text & Element Collision** | Scan vertical and horizontal clearances across header, badges, OMML math, bullets, tables, and footer. | **Zero collision**: Every text block, equation limit, and visual asset breathes with clean positive whitespace. |
| **2. Figure & Evidence Dominance** | Scan all rendered slide thumbnails side-by-side. | **$\ge 80\%$ visual coverage**: Visibly anchored by authentic figures, diagrams, equations, or `booktabs` tables—never a Word-doc bullet wall. |
| **3. Asset Fidelity & Geometry** | Inspect embedded PDF crops, microscopy panels, die photos, and tables at 100% scale. | **Zero distortion (`s_x == s_y`)**: Crisp 300+ DPI resolution, circular geometry preserved, zero leaked paper body text or duplicate tiny captions. |
| **4. Visual Weight & Cadence** | Evaluate dark-ink distribution within each slide and layout variety across consecutive slides. | **Balanced density & rhythm**: `70%–88%` card fill; no 3 consecutive slides repeat an identical 3-column Bento layout. |
| **5. Scholarly Aesthetic Purity** | Audit canvas background, accent budget ($\le 5\%$ chromatic ink), and final Q&A slide. | **Publication-grade craft**: Distraction-free `academic_mono` or curated scholarly palette; zero gradients/emojis; high-value lingering closing slide. |

---

## 7. Modular Accelerators, Environment Hygiene & Agent Autonomy

The skill bundles battle-tested CLI accelerators and declarative schemas:

- **[scripts/crop_figures.py](scripts/crop_figures.py)**: 300+ DPI `PyMuPDF` + `Pillow` PDF figure/table harvester (`--auto` caption clustering & `--page P --bbox` manual precision cropping + `figures_metadata.json` aspect-ratio export).
- **[scripts/latex_to_omml.py](scripts/latex_to_omml.py)**: Zero-dependency pure-stdlib recursive-descent LaTeX-to-OMML (`<a14:m><m:oMath>`) XML compiler and in-place `.pptx` ZIP injector (`--inject`).
- **[scripts/build_deck.js](scripts/build_deck.js)**: `PptxGenJS` 16:9 slide generator supporting all 6 curated scholarly palettes + conference themes, responsive card grids, `booktabs`/zebra tables, vector diagrams, and automatic Phase-2 OMML injection (`--config`, `--theme`, `--figures`).
- **[scripts/verify_deck.py](scripts/verify_deck.py)**: OpenXML structural & math validator checking slide count, `<m:oMath>` / `<a14:m>` injection, and zero leaked math placeholders.
- **[resources/template_config.json](resources/template_config.json)**: Canonical 16:9 coordinate zones, 7 core `gridModels` + 12 extended `layoutRecipes`, bilingual typography scales, and `themes` HEX definitions (paired with sample IR decks [resources/sample_deck_input.json](resources/sample_deck_input.json) and [resources/taming_deck_input.json](resources/taming_deck_input.json)).

> [!IMPORTANT]
> **Full Agent Autonomy & Workspace Hygiene**: These scripts are modular accelerators, not rigid handcuffs. Capable agents have full freedom to write custom `PptxGenJS` or `python-pptx` layout code tailored to bespoke scenarios (such as PhD defense breadcrumb bars, 5-row econometric tables, or multi-panel bio crops) while reusing `crop_figures.py` and `latex_to_omml.py`. Always execute Python commands inside existing system/Conda environments (`python -B` to prevent `__pycache__`; never create project-local `venv` or `.venv` folders). **The sole ground truth is what the presentation looks like in the rendered slide images.**
