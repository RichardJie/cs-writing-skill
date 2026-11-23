# Internal Lab Group Meeting & Seminar Playbooks (`scenarios-group-meeting.md`)

> **Module Role**: Operational scenario playbooks for internal academic laboratory meetings in [`cs-report-ppt`](../SKILL.md). Integrates directly with [`spine_template.md`](spine_template.md), [`marginal_annotations.md`](marginal_annotations.md), [`languages-and-typography.md`](languages-and-typography.md), and [`palettes-and-layouts.md`](palettes-and-layouts.md).

This reference defines **agent-executable operational playbooks, slide-by-slide spines, density budgets, layout geometry, and visual audit rules** for the three core internal academic laboratory presentation scenarios:

1. **Scenario 1 — Single-Paper Deep-Dive Journal Club (`论文精读组会` / Reading Group Deep-Dive)**: **14–18 slides** (25–45 min interactive slot). Anchored by an $\ge 80\%$ figure-dominant spine, a domain-native **Toy Numerical Walkthrough**, a 5-axis **Reproduction & Artifact Audit**, and **Lab Synergy Marginal Callouts (`旁注`)**.
2. **Scenario 2 — Multi-Paper Literature Sweep / Topic Survey (`文献泛读 / 专题综述组会`)**: **12–16 slides** (20–35 min synthesis slot). Driven by a **MECE Taxonomy Tree**, a **Generational Lineage Timeline**, a **Cross-Paper Master Comparison Matrix**, and **Structural Open Research Gaps** (strictly banning paper-by-paper laundry lists).
3. **Scenario 3 — Weekly / Bi-Weekly Lab Progress Report (`科研周报 / 课题进展汇报`)**: **6–10 slides** (+ unnumbered raw-data backup appendix; 8–15 min working slot). Governed by **Conclusion-First (BLUF) Framing**, **Hypothesis–Experiment–Root-Cause Failure Diagnosis**, **Structured A/B Blocker Decision Options**, and **Falsifiable Next-Period Milestones** (strictly banning chronological effort diaries / `苦劳流水账`).

All three scenarios inherit the core `cs-report-ppt` invariants: **16:9 widescreen canvas (`13.333" × 7.500"`)**, **300+ DPI authentic visual asset harvesting** with aspect-ratio lock, **native Office OpenXML Math (`OMML`)** vector equations, **Semantic Visual-Text Anchoring**, and **150+ DPI Pure Vision-in-the-Loop QA**.

---

## 0. Scenario Routing & Operational Selection Matrix

When generating a group-meeting deck, the agent first classifies the user's source artifacts and communicative goal using this routing matrix:

| Routing Dimension | Scenario 1: Journal Club Deep-Dive (`论文精读组会`) | Scenario 2: Literature Sweep / Survey (`文献泛读/专题综述`) | Scenario 3: Lab Progress Report (`科研周报/进展汇报`) |
|:---|:---|:---|:---|
| **Primary Input Artifacts** | 1 target paper PDF (+ optional official GitHub repo / appendix PDF) | 3–15 related paper PDFs, reading list, or survey topic prompt | Experiment logs, tables/plots, git commits, failure notes, last week's slides |
| **Core Communicative Goal** | Demystify mechanics, audit validity/reproducibility, extract lab transfer | Synthesize field structure, expose paradigm trade-offs, pitch research gap | Align with PI/peers, diagnose anomalies/failures, resolve blockers via A/B choices |
| **Slide Count Budget** | **14–18 slides** (14 core + up to 4 deep-dive modules) | **12–16 slides** (+ optional bibliography appendix) | **6–10 main slides** (+ 2–5 unnumbered raw-data backup slides) |
| **Speaking vs. Discussion Split** | 20–25 min presentation + 15–20 min active interruption/debate | 20–25 min thematic synthesis + 10 min entry-point debate | 8–12 min crisp readout + 10–20 min collaborative troubleshooting |
| **Visual Asset Coverage Floor** | **$\ge 80\%$** ($\ge 12/15$ slides anchored by harvested figures/tables/diagrams) | **$\ge 75\%$** ($\ge 10/13$ slides anchored by trees, timelines, matrices, paired crops) | **$\ge 75\%$** ($\ge 6/8$ slides anchored by empirical plots, fault trees, scorecards) |
| **Signature Structural Modules** | Toy Numerical Walkthrough + Reproduction Audit + 5 Lab Synergy Callouts | MECE Taxonomy Tree + Lineage Timeline + Cross-Paper Matrix + Gap Funnel | BLUF Continuity Scorecard + MECE Failure Diagnosis Tree + A/B Blocker Matrix |
| **Primary Anti-Pattern Banned** | Passive abstract/section translation (`逐段翻译复述论文`) | Sequential single-paper summaries (`第一篇…第二篇…串烧流水账`) | Chronological effort diary (`周一配环境、周二调参…苦劳流水账`) |

### Shared Canvas & Coordinate System Invariants (`13.333" × 7.500"`)
Every slide across all three playbooks respects the non-overlapping three-zone vertical partition from `resources/template_config.json`:
- **Header Zone (`x = 0.600", y = 0.350", w = 12.133", h = 1.200"`)**:
  - Category Tracker Badge (`y = 0.350", h = 0.250"`, `10pt Bold Uppercase`)
  - Assertion-Evidence Headline (`y = 0.600", h = 0.480"`, `22–26pt Bold`, single-line or tight 2-line claim—never generic labels like `"Results"` or `"实验结果"`)
  - Subtitle / Empirical Takeaway (`y = 1.080", h = 0.350"`, `14–15pt Medium/Italic`)
  - Divider Rule (`y = 1.500", h = 0.015"`)
- **Content Zone (`x = 0.600", y = 1.650", w = 12.133", h = 5.200"`)**: Populated via deterministic grid recipes (`hero_1col`, `split_equal_2col`, `split_65_35`, `grid_3col`, `grid_4col`, `quadrant_2x2`, `asymmetric_2row`) adapted dynamically to harvested asset aspect ratios ($W_{\text{orig}} / H_{\text{orig}}$).
- **Footer Zone (`x = 0.600", y = 7.000", w = 12.133", h = 0.350"`, `10pt Regular`)**: Left = Citation / Project Tag / Repo Commit; Right = Slide Index (`XX / NN`).

### Bilingual Track Switching Rules
- **100% Academic English Track** (International labs, English-medium seminars): All headlines, micro-bullets ($\le 12$ words/bullet), diagram callouts, and axis labels in crisp academic English.
- **100% Chinese / CN-EN Hybrid Lab Track** (Chinese university & institute seminars — 清华/北大/上交/浙大/中科院/AI Lab norm): Headlines use compact verb-object assertion clauses ($\le 22$ Chinese chars); body bullets use concise Chinese prose while **preserving canonical English technical identifiers verbatim** (`KV Cache`, `LoRA`, `Pareto Frontier`, `DID`, `Western Blot`, `p < 0.01`, `OOM`) with proper CJK-Latin spacing. Never invent awkward Chinese calques for standard domain terms.

---

## 1. Scenario 1: Single-Paper Deep-Dive Journal Club (`论文精读组会`)

### 1.1 Pedagogical & Critical Philosophy
In top international reading groups (MIT CSAIL, Stanford SAIL, Berkeley BAIR, Toronto Role-Playing Seminars) and premier Chinese research labs, **a journal club presenter is an independent scientific auditor and translator, not the paper's PR spokesperson**:
1. **Separate Author Claims from Presenter Verdict**: Explicitly tag what the authors claim (`[Author Claim / 原文主张]`) versus what the empirical evidence actually proves (`[Empirical Audit / 实证核验]`).
2. **Demystify via Concrete Numbers, Not Jargon Loops**: Dense notation walls put half the room to sleep. Following the `plain` skill methodology, insert a **Toy Numerical Walkthrough** using tiny, domain-native numbers ($2 \times 2$ matrices, 3 tokens, 2 assay dilutions, or a 4-cell cohort table) computed step-by-step on identical inputs for Baseline vs. Proposed.
3. **Audit Reproducibility Like an Engineer ("The Hacker & Detective Lens")**: Before the lab invests weeks building on a paper, audit its open-source repo, hidden compute cost, data availability, hyperparameter fragility, and appendix negative results.
4. **Anchor Externally to Lab Trajectory (`旁注`)**: Use `split_65_35` marginal callouts (`w = 4.133"`) on 5 strategic slides so every attendee knows *why our lab cares* and *what module we might steal, benchmark, or refute*.

---

### 1.2 The 16-Slide Deep-Dive Spine (14 Core + 2 Mandatory Audit/Walkthrough Modules, Expandable to 18)

When upgrading from a standard 14-slide conference summary to an internal **Deep-Dive Journal Club (14–18 slides)**, the spine preserves all 14 canonical analytical beats while inserting **Slide 8 (Toy Numerical Walkthrough)** and **Slide 11 (Reproduction & Artifact Audit)** as first-class operational slides (with optional **Slide 15 Appendix Detective** and **Slide 17–18 Q&A Backup** for 45-minute slots):

| Slide | Section | Tracker Badge (EN / CN) | Assertion-Evidence Headline Template | Grid Recipe | Mandatory Visual Asset & Focus | Density Budget | Marginal Callout (`旁注`) |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **1** | Header | `PAPER OVERVIEW` / `论文概览与速览` | `[Exact Paper Title]` + **3-Line TL;DR Pitch Strip** (Pain $\rightarrow$ Core Trick $\rightarrow$ Headline $\Delta$) | `split_equal_2col` or `asymmetric_2row` | **Cropped Teaser / Core Trade-off Figure (Fig. 1, 300 DPI)** + Metadata Grid (Venue, Year, Affiliations, Code URL, Artifact Badge) | Metadata + $\le 45$ words TL;DR | None (Metadata & TL;DR Strip) |
| **2** | Background (1/4) | `MOTIVATION & FAILURE MODES` / `研究动机与现有痛点` | `[Prior Paradigm] Fails Under [Stress Condition] Due to [Root Bottleneck]` | `split_65_35` | **Qualitative Failure / Bottleneck Plot (Fig. 1/2)**: Real error case, scaling wall, or confounding artifact | Main: 3 bullets ($\le 14$ EN words / $\le 26$ CN chars each) | `[State / Pathway Mechanism]` or `[Adaptivity]` |
| **3** | Background (2/4) | `LITERATURE TAXONOMY` / `方法谱系与定位` | `[Paper] Occupies the [Unexplored Quadrant] Between [Branch A] and [Branch B]` | `grid_3col` or `split_65_35` | **2D Design-Space Quadrant or Capacity Trade-off Chart** situating the paper against 2–3 dominant families | $\le 3$ items/card; $\le 75$ words total | None (Positioning Map) |
| **4** | Background (3/4) | `CORE HYPOTHESIS & GAP` / `核心科学假设与缺口` | `Core Thesis: [Mechanism Y] Resolves [Bottleneck X] Without Sacrificing [Constraint Z]` | `split_equal_2col` | **Empirical Gap Diagram / Counter-Example** contrasting prior unverified assumption vs. paper's central hypothesis | Left: 1 Thesis + 2 Bounds; Right: 3 Concrete Gaps | None (Hypothesis Hero) |
| **5** | Background (4/4) | `HISTORICAL LINEAGE` / `技术演进与作者脉络` | `From [2020 Origin] to [Paper]: Tracing the [3-Step Architectural Lineage]` | `split_65_35` | **3-Epoch Lineage Timeline + Author Lab Prior Work Continuity** (what prior paper from the same group led here) | 3 timeline nodes ($\le 20$ words/node) | `[Own Lab Synergy]` (Baseline intersection) |
| **6** | Methods (1/5) | `INPUTS & ASSUMPTIONS` / `形式化输入与前提假设` | `Method Assumes [Key Invariant] Over Input Space [Formal Tensor / Cohort Domain]` | `split_equal_2col` | **Input Representation / Spectral / Distribution Plot** + Native OMML domain definitions ($\mathbf{x} \in \mathbb{R}^{B \times L \times D}$) | Left: 3 domain specs; Right: 3 explicit assumptions | None (Foundational Invariants) |
| **7** | Methods (2/5) | `ARCHITECTURE PIPELINE` / `系统架构与数据流` | `[System Name] Routes [Input] Through [3 Stages], Isolating Novelty in [Module X]` | `split_65_35` | **Main System Architecture / Experimental Workflow (Fig. 2/3, 300 DPI)** with `✦ NOVEL` amber callout box | Figure = 65% canvas; Right = 3-step tensor/process trace | `[Mechanistic / Causal Lens]` |
| **8** | Methods (3/5) | `MATHEMATICAL FORMULATION` / `核心公式与目标函数` | `[Objective / Estimator] Balances [Fidelity Term] Against [Regularizer / Control Term]` | `asymmetric_2row` | **Color-Coded Native OMML Master Equation** (`<m:oMathPara>`) + Symbol-to-Meaning Glossary Table | Max 2 display equations + 4-row symbol glossary | None (Native OMML Formulation) |
| **9** | Methods (4/5) | `TOY NUMERICAL WALKTHROUGH` / `极简算例逐步推演` | `Step-by-Step Toy Example: How [Proposed Step] Shifts Output from [Baseline Val] to [New Val]` | `split_equal_2col` | **Side-by-Side Concrete Number Trace** ($2\times 2$ or $3$-item input $\rightarrow$ intermediate $\rightarrow$ output) labeled `[Toy Mechanism Example]` | Zero prose paragraphs; 3–4 aligned arithmetic steps/side | None (`plain` Skill Integration) |
| **10** | Methods (5/5) | `EXPERIMENTAL SETUP` / `实验设置与基线公平性` | `Evaluated Across [N Datasets] Against [M Baselines] Under [Compute / Control Protocol]` | `grid_3col` | **Protocol & Baseline Fairness Matrix** flagging whether baselines were re-tuned fairly or copied from older splits | 3 cards: Datasets/Metrics, Baseline Audit, Compute/Controls | None (Protocol Audit) |
| **11** | Audit (1/1) | `REPRODUCTION & ARTIFACT AUDIT` / `代码复现与开销审计` | `Reproduction Verdict: [Status] — Requires [VRAM/Time], With [Key Missing Detail / Trap]` | `split_65_35` | **5-Axis Reproducibility Scorecard Table** (`[VERIFIED]` / `[PARTIAL]` / `[GATED]`) + Repo File/Config Inspection | 5-row scorecard + 3 concrete lab replication estimates | `[Compute / Resource Efficiency]` |
| **12** | Results (1/3) | `PRIMARY BENCHMARKS` / `主实验结果与核心增益` | `[Proposed] Outperforms [Strongest Baseline] by [Δ +X%] on [Primary Metric] (Table 1)` | `asymmetric_2row` | **Cropped Primary Benchmark Table / Plot (300 DPI)** with bounding-box zoom on focal rows + explicit $\Delta$ badges | Top: Master Table; Bottom: 2 takeaway cards ($\le 35$ words each) | None (SOTA Verification) |
| **13** | Results (2/3) | `PARETO & SCALING TRADE-OFFS` / `效率帕累托与扩展曲线` | `Gains Hold Above [Scale Threshold], Yielding [X×] Speedup at Iso-Quality (Fig. 5)` | `split_65_35` | **Pareto Frontier / Scaling Law / Dose-Response Curve** highlighting operating regime where method dominates vs. degrades | Plot = 65%; Right = 2 regime bullets + hardware callout | `[Compute / Resource Efficiency]` |
| **14** | Results (3/3) | `ABLATIONS & FAILURE CASES` / `消融实验与失效边界` | `Component [A] Drives [75%] of Gain, While Method Breaks Under [Edge Case Z]` | `quadrant_2x2` | **Stepwise Ablation Table + Qualitative Failure Case Crop** (including hidden failure cases harvested from Appendix!) | 4 quadrants, max 2 micro-bullets ($\le 14$ words) per quadrant | None (Ablation & Blindspots) |
| **15** | Critique (1/2) | `CRITICAL ASSESSMENT` / `核心贡献与独立批判` | `Verdict: Strong [Strength X], But Vulnerable to [Unverified Assumption Y & Cost Z]` | `split_equal_2col` | **Balanced 50/50 Synthesis Cards**: Left = Validated Breakthroughs; Right = Methodological Blindspots & Reviewer Knives | 3 sharp points per card ($\le 18$ EN words / $\le 32$ CN chars) | None (Peer-Review Lens) |
| **16** | Critique (2/2) | `SEMINAR DISCUSSION & LAB ROADMAP` / `讨论议题与本组落地路线` | `3 Provocative Questions for the Room & A 3-Week Lab Transfer Plan` | `split_65_35` | **Left: 3 Debate Prompts** (Theory / Scale / Transfer); **Right: 3-Stage Lab Action Card** (Wk 1–3) | 3 debate prompts + 3 time-boxed lab milestones | `[Own Lab Synergy]` (Action Roadmap) |

> **Adaptive Length Compression / Expansion Rules**:
> - **14-Slide Compact Slot (20–25 min)**: Merge Slide 10 (Experimental Setup) & Slide 11 (Reproduction Audit) into one `split_65_35` Protocol & Reproducibility slide, and fold Slide 9 (Toy Numerical Walkthrough) into the bottom half of Slide 8 (`asymmetric_2row`) when the mathematical formulation is a single compact equation.
> - **17–18 Slide Extended Seminar (45–60 min)**: Add **Slide 15B (`APPENDIX DETECTIVE / 附录深挖与反常数据`)** spotlighting supplementary proofs, hyperparameter sensitivity cliffs, or negative controls buried in Appendix C–F, plus **Slides 17–18 (`BACKUP PROOFS & HYPERPARAMETER LEDGER`)** after Slide 16 for live Q&A grilling.

---

### 1.3 Mandatory Deep-Dive Sub-Protocols

#### A. Toy Numerical Walkthrough Protocol (Slide 9 — `plain` Skill Integration)
Abstract equations (`$\mathbf{c}_t = W^{DKV}\mathbf{h}_t$`) hide dimensionality bugs, normalization tricks, and causal routing. Slide 9 forces mechanical clarity by walking **one tiny, domain-native numerical input** from start to finish:

1. **Mandatory Visual Badge**: Top-right of the card MUST carry a pill badge:
   - EN: `[TOY MECHANISM EXAMPLE — ILLUSTRATIVE NUMBERS, NOT BENCHMARK DATA]`
   - CN: `[机制演算小例 — 仅用于逐步验算机制，非论文实测指标]`
2. **Domain-Native Objects Only (Zero Cross-Domain Metaphors)**:
   - *CS / AI*: Use 3 tokens, $d=4 \rightarrow d_c=2$ projection matrices with small integers (`[1, 0, -1, 2]`), attention masks, or cache byte counts. Never use metaphors like "postal sorting" or "water pipes."
   - *Mathematics / Optimization*: Use a 2D quadratic $f(x_1, x_2) = 2x_1^2 + \frac{1}{2}x_2^2$ from $(x_1^{(0)}, x_2^{(0)}) = (1, 2)$ for 1 gradient step vs. 1 preconditioned step.
   - *Biomedical / Wet Lab*: Use concrete assay counts (e.g., `1000 cells`, `MOI = 0.3`, vehicle control `OD = 0.20` vs. rescue `OD = 0.80`) showing raw readout $\rightarrow$ background subtraction $\rightarrow$ fold-change normalization.
   - *Economics / Social Science*: Use a $2 \times 2$ Treated/Control $\times$ Pre/Post cohort cell table (`Pre: 50 vs 40; Post: 75 vs 50`) computing first differences (`+25` vs `+10`) and final DID estimate (`+15`) alongside how a confounder breaks parallel trends.
3. **Zero Skipped Steps & Side-by-Side Comparison (`split_equal_2col`)**:
   - **Left Card (`Baseline Execution`)** and **Right Card (`Proposed Execution`)** MUST process the **exact same toy input**.
   - Every row states `Input` $\rightarrow$ `Operation` (in native OMML `<m:oMath>`) $\rightarrow$ `Exact Numerical Output`. Never write `"..."`, `"similarly for remaining terms"`, or `"after normalization"` without showing the arithmetic.

```
0.60" ┌───────────────────────────────────┐  6.82" ┌───────────────────────────────────┐ 12.73"
1.65" │ ◼ BASELINE: Standard KV Cache     │        │ ✦ PROPOSED: Low-Rank MLA Cache    │
      │ [Toy Mechanism Example]           │        │ [Toy Mechanism Example]           │
      │ Input h_t (d=4): [2, 0, 1, -1]    │        │ Input h_t (d=4): [2, 0, 1, -1]    │
      │ Step 1 (Project K, V in R^4):     │        │ Step 1 (Compress c_t = W_DKV h_t):│
      │   k_t = [2, 1, 0, -1] (4 floats)  │        │   W_DKV=[[1,0,1,0],[0,1,0,-1]]    │
      │   v_t = [0, 2, 1,  1] (4 floats)  │        │   c_t = [3, 1]  (ONLY 2 floats!)  │
      │ Step 2 (Cache Stored in VRAM):    │        │ Step 2 (Cache Stored in VRAM):    │
      │   Store (k_t, v_t) = 8 floats/tok │        │   Store c_t = 2 floats/tok (-75%) │
      │ Step 3 (Attention Score w/ q_t):  │        │ Step 3 (Absorb W_UK into q_t):    │
      │   q_t · k_t = [1,0,1,0]·k_t = 2   │        │   (W_UK^T q_t) · c_t = [1,-1]·[3,1]=2│
6.85" └───────────────────────────────────┘        └───────────────────────────────────┘
```

#### B. 5-Axis Reproduction & Artifact Audit Protocol (Slide 11 — "The Hacker Lens")
Top labs never take benchmark tables at face value. Slide 11 audits whether a graduate student in the room can actually reproduce and build upon the paper within realistic lab constraints:

| Audit Axis | Traffic-Light Tags | Concrete Evidence Agent Must Extract & Display on Slide 11 |
|:---|:---|:---|
| **1. Code & Weights** | `🟢 VERIFIED` / `🟡 PARTIAL` / `🔴 MISSING` | Official GitHub URL, license, whether repo includes **training + data prep scripts** vs. inference-only wrapper or empty `"Coming Soon"` README. |
| **2. Data & Splits** | `🟢 PUBLIC` / `🟡 MIXED` / `🔴 PROPRIETARY` | Exact dataset download availability, filtering/deduplication scripts, train/val/test split hashes, or undisclosed synthetic teacher data. |
| **3. Compute & VRAM Wall** | `🟢 LAB-FEASIBLE` / `🟡 STRETCH` / `🔴 GATED` | Total GPU hours & peak VRAM (`e.g., 64× H100 × 72h = 4,608 GPU-hrs` vs. `4× RTX 4090 × 6h`). Translate into **our lab cluster wall-clock cost**. |
| **4. Hyperparameter Fragility** | `🟢 ROBUST` / `🟡 SENSITIVE` / `🔴 BRITTLE` | Hidden tricks in Appendix/code: dataset-specific learning rates, gradient clipping thresholds, EMA decay, warmup schedules, seed variance ($\pm \sigma$). |
| **5. Baseline & Eval Integrity** | `🟢 FAIR` / `🟡 ASYMMETRIC` / `🔴 STRAWMAN` | Did authors re-tune baselines at equal compute/parameters, or copy stale numbers from older papers under weaker backbones/prompts? |

#### C. Universalized 5-Class Lab Synergy Marginal Callouts (`旁注` — `split_65_35` Right Card `w = 4.133"`)
To support universal multi-disciplinary seminars while preserving the 5-class architecture in `references/marginal_annotations.md`, map each class badge to the target discipline:

| Slot | Canonical Badge ID | CS / AI / Systems Focus | Math / Physics / EE Focus | Biomed / Wet-Lab / Econ Focus |
|:---|:---|:---|:---|:---|
| **Slide 2** | `[State / Pathway Dynamics]` | KV cache, recurrent state decay, memory bottleneck | Non-Markovian drift, phase-space dissipation, sensor noise | Signaling feedback loop, metabolic compensation, dynamic panel persistence |
| **Slide 4** | `[Adaptivity & Validity]` | OOD shift, test-time adaptation, continual learning | Perturbation stability, boundary condition breakdown | Cross-cohort/clinical generalizability, external validity across regimes |
| **Slide 7** | `[Mechanistic / Causal Lens]` | Circuit routing, SAE probing, representation geometry | Conservation laws, symmetry group invariance, Bode phase margin | Genetic rescue / off-target control, IV/DID/RDD causal identification check |
| **Slide 11/13**| `[Compute & Resource Cost]` | FLOPs, VRAM bandwidth, quantization, latency SLA | Die area, power envelope (mW), FPGA LUT utilization | Reagent cost/sample, bench turnaround weeks, cohort recruitment sample size $N$ |
| **Slide 5/16** | `[Own Lab Synergy]` | Module drop-in to in-house repo, Week 1–3 test plan | Lemma reuse in active proof, testbed calibration upgrade | Assay protocol adoption, new control arm, dataset linkage to ongoing grant |

---

### 1.4 Headline Templates, Table/Formula Rules & Anti-Patterns (Scenario 1)

#### Bilingual Assertion-Evidence Headline Templates
- **Motivation (Slide 2)**:
  - EN: `Standard Softmax Attention Wastes 78% Memory Bandwidth on Redundant KV States (Fig. 1b)`
  - CN: `传统全量 KV Cache 占用 78% 显存带宽，成为长上下文推理核心瓶颈（图 1b）`
- **Main Benchmark (Slide 12)**:
  - EN: `Decoupled Latent Compression Cuts VRAM by 4.2x While Improving MMLU by +1.9% (Table 2)`
  - CN: `解耦潜空间压缩降低 4.2 倍显存开销，且 MMLU 准确率反升 1.9%（表 2）`
- **Critique (Slide 15)**:
  - EN: `Elegant Low-Rank Formulation, But Speedup Vanishes Below Batch Size 8 Without Custom Kernels`
  - CN: `低秩解耦设计优雅，但缺乏定制算子时小批量（Batch < 8）加速比完全消失`

#### Table & Formula Formatting Rules
1. **Never Dump Full 25-Row Paper Tables Uncropped**: Either crop the focal sub-table at 300+ DPI and overlay a crisp vector highlight border (`2.0pt #E11D48` or `#111827`) around the `Baseline vs. Ours` rows, OR reconstruct a clean 5-to-7 row slide table showing `Method | Backbone/Scale | Metric 1 | Metric 2 | Cost/Latency | Δ vs. Strongest Baseline`.
2. **Color-Anchored OMML Equations**: Never paste screenshots of PDF equations (font aliasing and gray backgrounds fail Vision QA). Inject native `<m:oMathPara>` (`14–16pt Cambria Math`), limit to **$\le 2$ display equations per slide**, and map every key term (`Data Fidelity`, `KL Penalty`, `Jacobian Bound`) to a 1-line physical/algorithmic explanation immediately below or beside it.

#### Scenario 1 Anti-Patterns & Corrections

| Anti-Pattern (`组会精读大忌`) | Observable Symptom on Slide | Mandatory Agent Correction |
|:---|:---|:---|
| **Paper Translator (`逐段翻译机器`)** | Slide sequence mirrors paper section titles (`1. Intro`, `2. Related Work`, `3.1 Preliminaries`...) with walls of copied sentences | Rewrite every slide title as an empirical Assertion-Evidence claim; replace prose blocks with harvested figures + 3 analytical micro-bullets. |
| **Cheerleader Mode (`沦为作者夸夸群`)** | Slides repeat `"novel"`, `"state-of-the-art"`, `"seamlessly solves"` without questioning baselines or hidden costs | Strip promotional adjectives; enforce Slide 11 (5-Axis Reproduction Audit) and Slide 15 (50/50 Strengths vs. Blindspots). |
| **Notation Snowstorm (`符号雪崩`)** | 6 equations on one slide with undefined $\alpha, \beta, \tilde{\mathcal{Z}}_k^{(l)}$ | Cap at 2 native OMML equations on Slide 8 + mandatory Symbol Glossary + concrete integer Toy Walkthrough on Slide 9. |
| **Awkward Silence Ending (`结尾冷场：Thank You!`)** | Final slide only says `"Thanks / Q&A"` | Never end with a `"Thank You"` slide. End on **Slide 16** left open on screen: 3 sharp debate questions + 3-week Lab Synergy roadmap. |

---

## 2. Scenario 2: Multi-Paper Literature Sweep / Topic Survey (`文献泛读 / 专题综述组会`)

### 2.1 Synthesis-First Philosophy (Zero Laundry Lists)
When a graduate student or researcher surveys 5–15 papers for an exploratory topic seminar or literature sweep, the #1 failure mode across labs worldwide is the **Sequential Paper Laundry List (`串烧式流水账`: Slides 2–4 = Paper A, Slides 5–7 = Paper B, Slides 8–10 = Paper C)**. By Slide 6, the PI and lab mates suffer cognitive overload because notation changes every three slides and nobody sees the structural trade-offs.

**Mandatory Architectural Rule**: **Organize by Mechanism & Design Axes, NEVER by Paper Index.**
- Individual papers appear only as **evidence nodes** inside a unified **Taxonomy Tree**, causal **Lineage Timeline**, **Cross-Paper Master Matrix**, or **Branch Archetype Comparisons** using **normalized notation** across the entire deck.

---

### 2.2 The 14-Slide Literature Sweep / Topic Survey Spine (Adaptable 12–16 Slides)

| Slide | Section | Tracker Badge (EN / CN) | Assertion-Evidence Headline Template | Grid Recipe | Mandatory Visual Asset & Synthesis Focus | Density Budget |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Header | `TOPIC SURVEY` / `专题文献综述` | `[Topic Domain]: Synthesizing [N] Core Papers ([Year Range]) Toward [Lab Goal]` | `hero_1col` or `asymmetric_2row` | **Topic Scope Visual + Corpus Snapshot Strip** (Venues covered, e.g., `NeurIPS/ICLR/CVPR 2023–2026` or `Nature/Cell/AER`, Presenter, Lab Project Link) | Title + 3-stat corpus pill bar ($\le 40$ words) |
| **2** | Framing (1/2) | `PROBLEM & UNIFIED NOTATION` / `核心问题与符号统一` | `All [N] Works Target [Core Bottleneck], Formalized Under One Unified Objective` | `split_equal_2col` | **Unified Problem Schematic + Normalized Notation Box (Native OMML)**: Standardize $\mathbf{x}, \mathbf{y}, \mathcal{L}, \text{Cost}$ across all surveyed papers | Left: schematic + 2 bullets; Right: 4-row unified symbol table |
| **3** | Framing (2/2) | `CORPUS SELECTION FUNNEL` / `文献检索与筛选漏斗` | `Filtered [M] Candidate Papers Down to [N] Anchor Works Across [3] Paradigms` | `split_65_35` | **PRISMA-Lite Selection Funnel / Venue-Year Distribution Chart** + Explicit Inclusion/Exclusion Criteria (`e.g., open-source + >7B scale`) | Funnel diagram + 3 selection rules ($\le 55$ words) |
| **4** | Synthesis (1/3)| `METHODOLOGICAL TAXONOMY` / `方法论分类树 (MECE)` | `Existing Literature Splits Along [Primary Axis] Into [3] Distinct Paradigm Branches` | `hero_1col` | **Native DrawingML MECE Taxonomy Tree** (`Root Problem` $\rightarrow$ `3 Level-1 Paradigms` $\rightarrow$ `6 Sub-Mechanisms` $\rightarrow$ `[Author'YY]` leaf tags) | Vector tree ($\le 14$ nodes) + 1-line axis definition strip |
| **5** | Synthesis (2/3)| `EVOLUTIONARY LINEAGE` / `技术演进脉络与代际跃迁` | `Three Generational Shifts Driven by [Bottleneck 1 → Bottleneck 2 → Current Wall]` | `asymmetric_2row` | **Horizontal 3-to-4 Epoch Lineage Timeline** with causal transition callouts (`Why Gen 1 Broke` $\rightarrow$ `Gen 2 Fix` $\rightarrow$ `New Side-Effect`) | Top: vector timeline; Bottom: 2 causal shift callouts |
| **6** | Synthesis (3/3)| `MASTER COMPARISON MATRIX` / `跨文献核心维度对比矩阵` | `No Existing Paradigm Simultaneously Achieves [Property A], [Property B], and [Low Cost C]` | `hero_1col` | **Cross-Paper Master Comparison Matrix** (6–8 anchor papers $\times$ 6 orthogonal structural/empirical columns + shaded bottom `[Target Gap]` row) | Table only ($\le 6$ EN words / $\le 12$ CN chars per cell) |
| **7** | Paradigms (1/3)| `BRANCH 1 ARCHETYPE` / `范式一代表作深度拆解` | `Branch 1 ([Paradigm A]): High [Strength], Capped by [Structural Ceiling] ([Paper 1, Paper 2])` | `split_65_35` | **Paired High-DPI Architecture Crop** of Branch 1's flagship paper + mechanistic trade-off dissection | Left: cropped Fig. + flow tags; Right: `Mechanism / Win / Ceiling` |
| **8** | Paradigms (2/3)| `BRANCH 2 ARCHETYPE` / `范式二代表作深度拆解` | `Branch 2 ([Paradigm B]): Eliminates [Bottleneck X] via [Mechanism], Introducing [Cost Y]` | `split_65_35` | **Paired High-DPI Architecture / Assay / Identification Diagram** of Branch 2's flagship paper | Left: cropped Fig.; Right: `Mechanism / Win / Ceiling` |
| **9** | Paradigms (3/3)| `BRANCH 3 ARCHETYPE` / `范式三代表作深度拆解` | `Branch 3 ([Paradigm C]): Emerging [2025–2026] Frontier Trading [Assumption] for [Gain]` | `split_65_35` | **Paired High-DPI Architecture / Mechanism Diagram** of Branch 3's flagship paper + Lab Synergy callout | Left: cropped Fig.; Right: `Mechanism / Win / Lab Link` |
| **10** | Evidence (1/2) | `CROSS-PAPER EMPIRICAL FRONTIER` / `跨论文实证帕累托对比` | `Normalized Across [Shared Benchmark], [Branch C] Leads Quality While [Branch B] Wins Latency` | `split_65_35` | **Synthesized Quality-vs-Cost Pareto Scatter Plot or Harmonized Benchmark Table** (explicitly flagging backbone/split discrepancies!) | Plot/Table = 65%; Right = 3 fairness & scaling caveats |
| **11** | Evidence (2/2) | `SHARED ASSUMPTIONS & BLINDSPOTS` / `共性隐含假设与集体盲区` | `All Three Paradigms Quietly Rely on [Fragile Assumption X] That Fails in [Real Regime]` | `grid_3col` | **3-Column Blindspot Audit**: `Data / Environment Assumption`, `Evaluation Metric Distortion`, `Deployment / Sample-Size Wall` | 3 equal columns, 2 concrete paper citations + 2 bullets/col |
| **12** | Gaps (1/2) | `OPEN RESEARCH GAPS` / `结构性研究空白图谱` | `Three Unresolved Structural Gaps Where Prior Methods Collide` | `quadrant_2x2` or `grid_3col` | **Gap Map Visual** highlighting exact empty cells from the Taxonomy (Slide 4) and Master Matrix (Slide 6) | 3 structural gaps: `Why Unsolved` + `Why Solvable Now` |
| **13** | Gaps (2/2) | `LAB ENTRY POINT & HYPOTHESIS` / `本组切入点与拟验证思路` | `Proposed Lab Entry: Combine [Branch B Representation] With [Branch C Control] on [Our Task]` | `split_65_35` | **Draft Architecture / Identification Sketch (`✦ OUR IDEA`)** + Risk/Reward Feasibility Card | Left: vector concept diagram; Right: hypothesis + risk check |
| **14** | Action (1/1) | `MVP EXPERIMENT & READING QUEUE` / `两周最小可行实验与讨论` | `Next 2 Weeks: Reproduce [Anchor Baseline X] & Run [Falsifiable Toy Test Y]` | `split_equal_2col` | **Left: 2-Week MVP Verification Plan** (codebase to fork + pass/fail metric); **Right: 3 Seminar Decision Questions** | Left: 3 concrete steps; Right: 3 room decision questions |

> **12-Slide Fast Sweep vs. 16-Slide Comprehensive Survey**:
> - **12-Slide Fast Sweep (15–20 min, 3–5 papers)**: Merge Slide 2 & Slide 3 into a single `Scope & Unified Formulation` slide, and combine two thinner paradigm branches onto a `split_equal_2col` side-by-side comparison slide.
> - **16-Slide Deep Survey (35–45 min, 10–15 papers)**: Add **Slide 10B (`BENCHMARK & DATASET ECOSYSTEM AUDIT / 评测基准与数据集盘点`)** comparing datasets, evaluation metrics, and contamination/saturation issues, plus **Slide 15–16 (`ANNOTATED CITATION DIRECTORY`)** grouping all surveyed papers with GitHub links.

---

### 2.3 Mandatory Multi-Paper Synthesis Sub-Protocols

#### A. MECE Methodological Taxonomy Tree Protocol (Slide 4)
1. **Valid Splitting Axes Only**: Partition literature by **core algorithmic mechanism, mathematical objective, causal identification strategy, or biological intervention locus**—NEVER by publication year (`2023 Papers vs. 2025 Papers`), venue (`CVPR vs. NeurIPS`), or vague adjectives (`Simple vs. Complex`).
2. **Tree Geometry Constraints (`hero_1col`: `x = 0.600", y = 1.650", w = 12.133", h = 5.200"`)**:
   - **Depth**: Exactly **3 levels** (`Root Problem` $\rightarrow$ `2–4 Primary Paradigms` $\rightarrow$ `4–8 Concrete Sub-Families with [Author'YY] Badges`).
   - **Visual Highlighting**: Shade the specific branch or cross-branch intersection that directly touches our lab's active project in warm amber (`#FEF3C7` fill, `2.0pt #F59E0B` border) with a `✦ LAB TARGET ZONE` tag.

```
0.60" ┌────────────────────────────────────────────────────────────────────────┐ 12.73"
1.65" │                  [ Root: Long-Context LLM Memory Bottleneck ]          │
      │                     (Splitting Axis: When & How State Is Compressed)   │
      │                 ┌───────────────────────┼───────────────────────┐      │
      │                 ▼                       ▼                       ▼      │
      │    ┌────────────────────────┐ ┌────────────────────┐ ┌───────────────┐ │
      │    │ 1. Token Eviction/Drop │ │ 2. Latent KV Proj. │ │ 3. Linear/SSM │ │
      │    │  (Zero train cost)     │ │ (✦ LAB TARGET ZONE)│ │ (O(1) state)  │ │
      │    └─────┬────────────┬─────┘ └─────────┬──────────┘ └───────┬───────┘ │
      │          ▼            ▼                 ▼                    ▼         │
      │     [H2O '23]   [SnapKV '24]     [DeepSeek-MLA '24]    [Mamba-2 '24]   │
      │     [Streaming] [PyramidKV]      [Palu '24, EigenKV]   [GatedDelta '25]│
6.85" └────────────────────────────────────────────────────────────────────────┘
```

#### B. Generational Lineage & Causal Bottleneck Timeline Protocol (Slide 5)
A timeline without causality is just a calendar. Every arrow connecting `Epoch k` $\rightarrow$ `Epoch k+1` MUST carry an explicit **Causal Bottleneck Trigger** explaining *what specific failure mode in Epoch k forced researchers to invent Epoch k+1*:
- **Node Structure**: `[Years] Epoch Name` + `Anchor Papers (1–2)` + `Core Capability Unlocked`.
- **Transition Arrow Badge**: `⚠️ Broke on: [Exact Bottleneck]` (e.g., `⚠️ Quadratic O(L²) VRAM at 32K` $\rightarrow$ `⚠️ Loss of Needle-in-a-Haystack Recall` $\rightarrow$ `Current Frontier`).

#### C. Cross-Paper Master Comparison Matrix Protocol (Slide 6)
Slide 6 is the single highest-value slide in any survey seminar. Design it so a viewer can photograph this one slide and grasp the entire sub-field:

1. **Row Selection**: Include **5–8 representative anchor papers** ordered by Taxonomy Branch (NOT alphabetically!), followed by a shaded final row: **`★ Ideal / Our Target Gap`**.
2. **Column Schema (6 Orthogonal Columns)**:
   - Col 1: `Paper & Venue` (`[Author, Venue'YY]` + `🟢 Code` / `🔴 Closed` icon)
   - Col 2: `Taxonomy Branch` (matching Slide 4 labels)
   - Col 3: `Core Mechanism / Estimator` ($\le 6$ words or compact inline OMML)
   - Col 4: `Key Requirement / Assumption` (e.g., `Retraining?`, `Paired Data?`, `Parallel Trends?`, `CRISPR Line?`)
   - Col 5: `Normalized Gain / Complexity` (e.g., `O(L) / -68% VRAM`, `AUC +3.4% vs. ResNet`)
   - Col 6: `Primary Failure Mode / Catch` ($\le 7$ words exposing the exact trade-off penalty)
3. **Cell Scannability Rules**:
   - Strict cell word cap: **$\le 6$ English words** or **$\le 12$ Chinese characters** per cell.
   - Use high-contrast typographic symbols (`✓` Supported / Low-Cost, `◐` Partial / Conditional, `✗` Unsupported / Prohibitive) rather than full sentences.
   - **Cross-Paper Metric Harmonization**: Never compare raw benchmark numbers across papers evaluated on different backbones or splits without an explicit normalization tag (`e.g., +2.1% over LLaMA-3-8B` vs. `+4.5% over GPT-2`).

#### D. Structural Open Research Gaps vs. Fake Gaps (Slide 12)
Train the agent to reject **Fake Combinatorial Gaps** (`"Paper A used Transformer on Dataset X, nobody ran Mamba on Dataset Y yet"`) and formulate **Structural Scientific Gaps**:

| Structural Gap Archetype | Diagnostic Formula | Example Seminar Pitch |
|:---|:---|:---|
| **1. Impossible Triangle / Pareto Cliff** | Branch A achieves `X+Y` but fails `Z`; Branch B achieves `Z` but destroys `X` | *Exact recall (`✓`) + Zero retraining (`✓`) + Sub-linear VRAM (`✓`) remains simultaneously unachieved.* |
| **2. Violated Shared Invariant** | All surveyed works assume `Condition C`, which fails in real deployment | *Every surveyed estimator assumes stationary noise; real sensor/clinical streams exhibit burst drift.* |
| **3. Confounded Evaluation Artifact** | Reported gains stem from benchmark leakage or asymmetric compute | *80% of surveyed gains disappear when baselines are given equal test-time token budgets.* |
| **4. Scale / Regime Discontinuity** | Mechanism works at toy scale ($N < 10^3$) but collapses at target scale ($N > 10^6$) | *Second-order Jacobian regularization OOMs above 7B parameters without block-diagonal approximation.* |

---

### 2.4 Scenario 2 Anti-Patterns & Before/After Rewrites

| Anti-Pattern (`文献泛读大忌`) | ❌ Bad Slide Design (Before) | ✅ Synthesis-First Slide Design (After) |
|:---|:---|:---|
| **Sequential Book Report (`串烧读书报告`)** | Slide 3: *Paper 1 Summary*; Slide 4: *Paper 2 Summary*; Slide 5: *Paper 3 Summary*... | Slide 4: *3-Branch MECE Taxonomy*; Slide 6: *7-Paper Master Trade-off Matrix*; Slides 7–9: *Paradigm Archetypes*. |
| **Notation Babel (`符号巴别塔`)** | Slide 7 copies Paper A's $z_t = f_\theta(x_t)$; Slide 8 copies Paper B's $s_i = \phi_w(u_i)$ for the exact same state | Slide 2 defines one unified symbol table ($\mathbf{h}_t, \mathbf{c}_t$); all downstream slides rewrite equations into unified native OMML. |
| **Prose-Stuffed Matrix (`表格塞满小作文`)** | 8×6 table where every cell has a 30-word paragraph in `8pt` unreadable font | `11–12pt` crisp cells capped at $\le 6$ words + `✓ / ◐ / ✗` glyphs + shaded bottom `★ Target Gap` row. |
| **No Lab Landing (`只综述不落地`)** | Ends with vague clichés: *"Future work: improve accuracy and efficiency on more datasets."* | Ends with Slide 13–14: *Concrete cross-branch hypothesis + exact GitHub baseline to fork + 2-week MVP pass/fail gate*. |

---

## 3. Scenario 3: Weekly / Bi-Weekly Lab Progress Report (`科研周报 / 课题组进展汇报`)

### 3.1 Working-Session Philosophy & Hard Ban on Effort Diaries (`严禁苦劳流水账`)
A weekly or bi-weekly lab progress update is **NOT an attendance timecard or chronological diary (`周一到周五干活流水账`)**; it is a **high-bandwidth scientific & engineering decision session** with the PI and peers. Faculty and senior researchers care about three things only:
1. **Bottom-Line Delta**: What falsifiable claim did we prove, refute, or de-risk since the last meeting?
2. **Rigorous Diagnosis of Negative Data**: Failed experiments are normal in research; **unexplained, un-isolated failures** are not. Showing systematic variable elimination builds higher PI trust than cherry-picked happy numbers.
3. **Structured Decision Leverage**: Never ask the room *"It didn't work—what should I do next?"* empty-handed. Present concrete **Option A (Recommended)** vs. **Option B (Fallback)** with resource costs and stop-loss criteria.

#### Diagnostic Ban List: Effort Diary (`苦劳流水账`) vs. Scientific Progress Framing

| Reporting Dimension | ❌ Banned Effort-Diary (`流水账 / 情绪化汇报` — NEVER GENERATE) | ✅ Mandatory Conclusion-First Framing (`结论与归因导向` — ALWAYS GENERATE) |
|:---|:---|:---|
| **Opening / TL;DR** | *"This week I configured CUDA, read 3 papers, cleaned datasets, and ran 5 experiments..."*<br>*“本周主要配了环境、跑了五组参数、精读了两篇文献…”* | **`BLUF:`** *"Reproduced Baseline X within 0.3% of paper claim, but custom loss diverges at step 4k due to FP16 norm overflow."*<br>*“本周核心结论：打通 Baseline 复现（误差 <0.3%），锁定新损失函数在 4k 步梯度爆炸源于 FP16 下溢。”* |
| **Process vs. Logic** | *"Monday: data script; Tuesday: server crashed; Wednesday–Friday: tuned lr..."*<br>*“周一写脚本，周二服务器崩了，周三到周五一直在调参…”* | *"Controlled 3-factor sweep (`lr × warmup × norm`) isolated pre-norm scaling—not learning rate—as the stability bottleneck (Fig. 2)."*<br>*“通过三因子控制变量实验排除学习率干扰，确认瓶颈位于 Pre-Norm 缩放尺度（图 2）。”* |
| **Negative Results** | *"Tried Method A many times, very hard, metrics didn't go up at all."*<br>*“试了好多次都不涨点，实验太难做了，不知道为啥没效果。”* | **`[Root-Cause Diagnosis]`** *"Ruled out data bug via overfit-1-batch test (loss → 0.002); zero val gain stems from label noise in split B (18% mislabeled)."*<br>*“【失败归因】单 Batch 过拟合测试通过（排除代码 Bug），定位验证集不涨点源于 B 子集存在 18% 标签噪声。”* |
| **Blocker Escalation** | *"Model OOMs / Assay failed. Teacher, what should I do next?"*<br>*“显存一直爆 / 反应不出产物，老师我接下来该怎么办？”* | **`[Decision Ask]`** *"Propose **Option A** (Gradient Checkpointing + rank-64, 2 days, 0 accuracy loss) over **Option B** (truncate context to 4k). Confirm Option A?"*<br>*“【决策诉求】拟优先执行方案 A（重计算+秩64压缩，耗时2天），备选方案 B（截断至4k）；请老师拍板是否按 A 推进。”* |
| **Next-Week Plan** | *"Next week: continue tuning hyperparameters and read more papers."*<br>*“下周计划：继续调参优化模型，把没做完的实验做完，多读文献。”* | *"1. Run 3-seed sweep on cleaned split by Wed (**Pass Gate: F1 ≥ 78.5%**); 2. If <76%, trigger Plan B contrastive pre-filtering on Thu."*<br>*“① 周三前完成清洗集 3 随机种子复测（达标线：F1 ≥ 78.5%）；② 若低于 76%，周四启动备选对比过滤方案。”* |

---

### 3.2 The 8-Slide Lab Progress Report Spine (Adaptable 6–10 Main Slides + Raw Backup Shield)

| Slide | Section | Tracker Badge (EN / CN) | Assertion-Evidence Headline Template | Grid Recipe | Mandatory Visual Asset & Working Focus | Density Budget |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Executive | `EXECUTIVE BLUF & CONTINUITY` / `核心结论先行与本周兑现表` | **`BLUF:`** `[1-Sentence Bottom-Line Verdict + Key Quantitative Delta]` | `asymmetric_2row` | **Top: 3-Row Continuity Scorecard** (`Last-Period Promise` $\rightarrow$ `🟢/🟡/🔴 Status` $\rightarrow$ `Key Metric`); **Bottom: Hero Metric Snapshot + Today's Explicit Decision Ask** | Scorecard ($\le 35$ words) + 1 bold Meeting Ask box |
| **2** | Context | `PROJECT MAP & ACTIVE HYPOTHESIS` / `课题全局坐标与本周待验假设` | `Testing Hypothesis H1: [Intervention X] Resolves [Bottleneck Y] by [Observable Signature Z]` | `split_65_35` | **30-Second Project Mini-Pipeline** with `[📍 THIS WEEK]` highlight node + Formal `H1 (Hypothesis)` vs. `H0 (Null)` & Falsification Metric | Mini-diagram + `H1 / H0 / Success Gate` card ($\le 60$ words) |
| **3** | Setup | `PROTOCOL DIFF & CONTROLS` / `实验改动增量与对照设计` | `Isolated [Target Variable] Against [Positive / Negative / Baseline Controls] (Commit #a1b2c)` | `split_equal_2col` | **Left: Architecture / Assay / Specification Diff** (highlighting ONLY what changed since last report); **Right: Sanity-Check & Control Matrix** | Diff diagram + 4-row control table ($\le 65$ words) |
| **4** | Results (1/2) | `QUANTITATIVE READOUT` / `核心量化实验结果对比` | `[New Variant] Shifts [Primary Metric] by [Δ +X% / -Y%] vs. Last Week's Baseline` | `split_65_35` | **Delta Comparison Table or Training/Dose Curve** with explicit `Last Week Baseline` $\rightarrow$ `This Week` $\rightarrow$ `Target Gate` reference line | Plot/Table = 65%; Right = 3 empirical observations |
| **5** | Results (2/2) | `RAW SIGNAL & ERROR CASES` / `原始数据表征与典型样本剖析` | `Raw Readout Reveals [Specific Pattern / Sub-Group Divergence], Not Uniform Gain` | `split_equal_2col` | **Primary Unprocessed Evidence** (raw loss/grad-norm curves, confusion matrix, failure case pairs, uncropped blot/spectrum) + **Strict `Observation` vs. `Interpretation` Split** | Raw visual + 2 `Observed Facts` + 1 `Working Inference` |
| **6** | Diagnosis | `ROOT-CAUSE FAILURE DIAGNOSIS` / `异常现象与失败归因排查树` | `Root-Cause Isolation: Ruled Out [A & B]; Pinpointed [Suspect C] via [Diagnostic Test]` | `hero_1col` or `split_65_35` | **MECE 4-Branch Fault-Isolation Tree** (`🟢 Ruled Out w/ Evidence` vs. `🔴 Confirmed Culprit` vs. `🟡 Pending Test`) | Fault tree ($\le 8$ nodes) + 2 verification data points |
| **7** | Pivot / Lit | `LITERATURE / THEORY CROSS-CHECK` / `文献对标与机理解释支撑` *(Include when debugging bottlenecks or pivoting)* | `Recent Work ([Author'YY]) Confirms [Phenomenon] Stems from [Mechanism], Suggesting [Fix]` | `split_65_35` | **Cropped Reference Curve/Equation from Anchor Paper** mapped directly onto our Slide 5/6 anomaly | Cropped external evidence + 3-bullet transfer mapping |
| **8** | Decisions | `BLOCKER & A/B DECISION OPTIONS` / `核心卡点与 A/B 决策方案请求` | `Decision Needed: Approve [Option A: Recommended] Over [Option B] to Unblock [Milestone]` | `split_equal_2col` | **Structured Option A vs. Option B Trade-Off Matrix** (`Mechanism`, `Time/GPU/Reagent Cost`, `Expected Gain`, `Risk`, `Kill Criterion`) + **Explicit PI Ask Banner** | 2 option cards + bottom `Explicit Ask` strip ($\le 80$ words) |
| **9** | Next Steps | `NEXT-PERIOD SMART MILESTONES` / `下周可考核计划与止损线` | `Next Period: [2–3 Quantified Tasks] Gated by [Pass/Fail Threshold] Before [Date]` | `hero_1col` | **Priority-Ordered Milestone Execution Table** (`Priority | Concrete Action | Compute/Assay Budget | Quantitative Pass Gate | Fallback Trigger | ETA`) | 3-to-4 row table; zero vague verbs (`"continue"`, `"study"`) |
| **A1–A3** | Appendix | `BACKUP: RAW LOGS & LEDGER` / `附录备份：原始曲线与超参账本` *(Unnumbered, after Slide 9)* | `Backup Verification: Full Seed Variance, Hyperparameter Diff & Negative Controls` | `quadrant_2x2` | **Full TensorBoard/W&B curves, exact hyperparameter/reagent config table, outlier slices** ready for live PI deep-dive questions | High-precision archival tables/plots |

---

### 3.3 Mandatory Progress-Report Sub-Protocols

#### A. Slide 1 Continuity Scorecard & Meeting Goal Protocol
PIs track 5–20 concurrent sub-projects and cannot recall what a student promised 14 days ago. Slide 1 MUST open with three instant-alignment blocks:
1. **Top Strip — Meeting Goal (`本次汇报核心诉求`, 1 line)**: e.g., `Goal Today: Validate root-cause diagnosis on OOD drop and choose between data re-weighting (Option A) vs. adapter rank expansion (Option B).`
2. **Middle Card — Last-Period Continuity Ledger (`承诺兑现核对表`, 3 rows max)**:
   - `[🟢 DELIVERED]` `Reproduce baseline on Split-v2` $\rightarrow$ `Achieved 81.4% (Paper: 81.6%)`
   - `[🟡 PARTIAL]` `Full 32k context ablation` $\rightarrow$ `Completed 16k (+2.1%); 32k hit OOM at step 1,800`
   - `[🔴 PIVOTED]` `Synthetic distill v1` $\rightarrow$ `Halted after 500-sample audit showed 22% hallucinated labels`
3. **Bottom Card — Headline Empirical Snapshot**: Mini sparkline/bar delta or single hero figure thumbnail proving the week's central finding.

#### B. MECE Failure Mode & Anomaly Diagnosis Tree Protocol (Slide 6)
Whenever an experiment yields negative results, stalls, diverges, or contradicts expectations, Slide 6 MUST render a structured **MECE Fault-Isolation Tree** separating **what has already been experimentally ruled out** from **the active root cause**:

| Diagnostic Branch | CS / AI / Systems Checks | Wet-Lab Biomed / Chemistry Checks | Economics / Empirical Social Checks |
|:---|:---|:---|:---|
| **1. Implementation / Assay Integrity (`工程/操作故障`)** | Tensor shape broadcast bug, train/eval mode mismatch, tokenizer padding leak, 1-batch overfit check | Reagent degradation, pH/temperature drift, primer contamination, positive control failure | Merge key duplication, sample attrition coding bug, weight scaling error |
| **2. Data / Sample Distribution (`数据/样本伪影`)** | Train-val distribution shift, noisy/corrupted labels, class imbalance, sequence truncation | Clonal selection artifact, batch effect, cell viability drop, low MOI transduction | Pre-trend violation, compositional shift in panel, survivorship bias, weak first-stage $F < 10$ |
| **3. Optimization / Regime Tuning (`优化/条件失配`)** | LR/warmup mismatch, BF16/FP16 gradient underflow, regularizer dominating main loss | Incubation time too short/long, dose outside linear dynamic range, off-target toxicity | Over-controlling bad controls (collider bias), clustered SE misspecification, outlier leverage |
| **4. Core Hypothesis Falsification (`核心科学假设证伪`)** | Clean toy test also fails $\rightarrow$ hypothesized representation lacks mutual information with target | Rescue + orthogonal assay both null $\rightarrow$ pathway A does not regulate phenotype B | Placebo + clean sub-sample both null ($p > 0.50$) $\rightarrow$ treatment has zero causal effect |

```
0.60" ┌────────────────────────────────────────────────────────────────────────┐ 12.73"
1.65" │ Symptom: Val Accuracy Stalled at 64.2% (vs. 74.0% Target) After 10 Epochs │
      ├───────────────────────┬────────────────────────┬───────────────────────┤
      │ 1. Code / Grad Bug?   │ 2. Optimization Stall? │ 3. Data / Split Leak? │
      │ [🟢 RULED OUT]        │ [🟢 RULED OUT]         │ [🔴 CONFIRMED CULPRIT]│
      │ • 64-sample overfit   │ • Cosine vs. Constant  │ • Audited 100 val errs│
      │   hits 99.8% in 80    │   LR & FP32 master     │ • 31% of val queries  │
      │   steps; grad norm    │   weights gave <0.2%   │   truncated at 512    │
      │   healthy (0.4–1.1).  │   difference.          │   tokens, losing cues.│
6.85" └───────────────────────┴────────────────────────┴───────────────────────┘
```

#### C. Structured Blocker & A/B Decision Options Protocol (Slide 8)
Transform passive blockers into executive engineering choices using `split_equal_2col`:
- **Card 1: `★ Option A (Recommended): [Concrete Fix]`** — Mechanism, exact cost (`e.g., 16 GPU-hrs / 2 days / ¥1,200 reagent`), expected observable outcome, and **Stop-Loss / Kill Criterion** (`"If metric < X after 500 steps, abort immediately"`).
- **Card 2: `Option B (Fallback / Conservative): [Alternative Path]`** — Mechanism, cost, trade-off penalty (`e.g., caps ceiling at 8k tokens`), and when it triggers.
- **Bottom Strip (`y = 6.35", h = 0.50"`)**: **`Explicit Ask for PI / Lab:`** Specifying whether you need (a) directional sign-off on Option A, (b) temporary GPU/instrument quota, or (c) peer code/assay review from a named lab mate.

#### D. Adaptive Sub-Variants for Real Weekly Lab Scenarios
Not every week has positive metrics. The agent dynamically adapts the 6–10 slide budget across three real-world modes:
1. **Variant 3A — Breakthrough / Positive-Signal Week (`正向突破周`, 6–7 Slides)**:
   - Compress Slide 6 (Failure Diagnosis) into a **Confounder & Sanity-Check Verification Slide (`排除虚假涨点自检`)**: prove the gain is NOT caused by data leakage, unfair extra parameters, lucky random seed, or metric hacking before celebrating.
2. **Variant 3B — Negative-Result / Bug-Hunt Week (`负结果与排障周`, 7–8 Slides)**:
   - Dedicate Slides 4–6 to **Raw Anomaly Visualization + 4-Branch MECE Elimination Tree + Minimal Toy Verification**, followed by Slide 7–8 **Pivot Decision Matrix**. Frame eliminated dead-ends as permanent information gain for the lab.
3. **Variant 3C — Cold-Start / First-Month Exploration Week (`新课题冷启动周`, 6–7 Slides)**:
   - Replace delta results with: Slide 1 `Problem Scoping BLUF` $\rightarrow$ Slide 2 `Anchor Baseline Selection` $\rightarrow$ Slide 3 `Environment & Dataset Verification Ledger` $\rightarrow$ Slide 4 `Baseline Reproduction vs. Paper Claim Table` $\rightarrow$ Slide 5 `First Error-Case Dissection` $\rightarrow$ Slide 6 `Week-2 First Hypothesis & Milestones`.

---

## 4. End-to-End Agent Execution & Group-Meeting Vision QA Protocol

### 4.1 Structured Pre-Generation Extraction Workflow
Before writing slide generation code (`python-pptx` / `pptxgenjs` + `latex_to_omml.py`), the agent executes a scenario-specific extraction pass:

1. **Scenario 1 (`论文精读`)**:
   - Harvest 8–12 PDF figures/tables at **300+ DPI** (`scripts/crop_figures.py`), recording exact $(W_{\text{orig}}, H_{\text{orig}})$ aspect ratios.
   - Construct 1 concrete domain-native **Toy Numerical Example** (verifying every arithmetic step in Python before rendering).
   - Inspect paper appendix + code link to populate all 5 rows of the **Reproduction & Artifact Audit Scorecard**.
   - Draft the 5 **Lab Synergy Marginal Callouts (`旁注`)** anchored to user's lab profile (or general domain frontier if unspecified).
2. **Scenario 2 (`文献泛读/综述`)**:
   - Normalize core mathematical symbols across all surveyed papers into a single **Unified Symbol Glossary**.
   - Partition papers along one strict **MECE Splitting Axis** (zero `"Misc / Others"` bucket) and extract 1 flagship architecture/result crop per paradigm branch at 300+ DPI.
   - Build the **6-Column Master Comparison Matrix** with cell lengths strictly $\le 6$ EN words / $\le 12$ CN chars, appending the `★ Target Gap` row.
3. **Scenario 3 (`科研周报`)**:
   - Refactor raw chronological user notes/logs into **BLUF Verdict + Continuity Scorecard + Hypothesis $H_1/H_0$**.
   - Generate clean vector plots or structured delta tables with explicit `Baseline | Last Period | This Period | Target Gate` columns.
   - Map any failed run or stalled metric into a **MECE Fault-Isolation Tree** (`Ruled Out` vs. `Confirmed`) and synthesize **Option A vs. Option B** decision cards + SMART milestones with numerical pass/fail gates.

---

### 4.2 Group-Meeting Vision-in-the-Loop Inspection Rubric (`150+ DPI PNG` via `view_file`)

After rendering the `.pptx` to PDF (`soffice --headless --convert-to pdf`) and rasterizing every slide at **150+ DPI** (`pdftoppm -png -r 150` or `pymupdf`), the agent MUST visually inspect **every single slide image** against both the core `cs-report-ppt` geometric rules and these scenario-specific visual gates:

| # | Visual Audit Check | Target Scenario(s) | Pass Criterion Verified by Multimodal Vision (`view_file`) | Immediate Code Fix if Defective |
|:---|:---|:---|:---|:---|
| **1** | **Assertion-Evidence Headline Integrity** | All (1, 2, 3) | Zero generic titles (`"Methodology"`, `"Results"`, `"本周工作"`). Every headline states a crisp empirical verdict in 1–2 lines without colliding with the top tracker badge (`y = 0.35"`). | Rewrite headline to verb-driven claim; tighten font from `26pt` to `22–24pt` if wrapping to 3 lines. |
| **2** | **High-DPI Figure Aspect Lock** | All (1, 2, 3) | Harvested architectures, blots, and plots appear razor-sharp with undistorted circles/fonts, centered cleanly with $\ge 0.15"$ breathing padding inside cards. | Recompute scale $s = \min((W_c-2P_x)/W_0, (H_c-2P_y)/H_0)$ and re-crop PDF at 300 DPI. |
| **3** | **Native OMML Vector Math Cleanliness** | All (1, 2, 3) | Zero raw LaTeX tokens (`\frac`, `$$`, `{{MATH:...}}`), zero blurry gray-background equation screenshots, and zero overlap between `<m:oMathPara>` blocks and bullet lines. | Run `latex_to_omml.py` injection check; expand equation box height by `+0.35"`. |
| **4** | **Toy Walkthrough Alignment & Badge** | Scenario 1 (Slide 9) | Baseline (Left) and Proposed (Right) arithmetic steps align horizontally row-by-row; `[Toy Mechanism Example / 机制演算小例]` badge is visibly distinct. | Align step $Y$-coordinates across `split_equal_2col` cards; shrink step font to `12pt` monospace/OMML. |
| **5** | **Reproduction Audit Traffic Lights** | Scenario 1 (Slide 11) | All 5 audit rows (`Code`, `Data`, `Compute`, `Hyperparams`, `Baselines`) show high-contrast status pills and concrete lab hardware estimates without row clipping. | Convert overflowing prose cells into `Status Pill + <=10-word evidence phrase`. |
| **6** | **Marginal Callout (`旁注`) Separation** | Scenario 1 & 2 | `split_65_35` right callout card (`x = 8.600", w = 4.133"`) preserves a clean `0.300"` gap from the main card and renders a crisp `0.08"` left vertical accent bar. | Lock `main_card.w = 7.700"` and `side_note.x = 8.600"`; cap side-note to 3 short bullets. |
| **7** | **Taxonomy Tree Node Legibility** | Scenario 2 (Slide 4) | Connector lines never slice through text boxes; leaf `[Author'YY]` tags are legible at `>= 11pt`; `✦ LAB TARGET ZONE` branch stands out immediately. | Limit tree depth to 3 levels and $\le 4$ branches; widen node boxes or switch to left-to-right horizontal tree. |
| **8** | **Master Comparison Matrix Scannability** | Scenario 2 (Slide 6) | Table text is `>= 11pt` with zero vertical cell overflow; `✓ / ◐ / ✗` symbols align cleanly; bottom `★ Target Gap` row is subtly shaded. | Trim cell text to $\le 6$ EN words / $\le 12$ CN chars; cap rows at 8 anchor papers + 1 gap row. |
| **9** | **Zero Effort-Diary (`流水账`) Leakage** | Scenario 3 (All) | Zero weekday chronological lists (`Mon/Tue/Wed` or `周一/周二`) and zero vague plans (`"continue tuning"`). Slide 1 visibly leads with BLUF + Continuity Scorecard. | Refactor timeline text into variable-isolation cards and quantified SMART milestone rows. |
| **10** | **Fault-Tree Visual Polarity** | Scenario 3 (Slide 6) | Ruled-out branches (`🟢 RULED OUT`) vs. confirmed root causes (`🔴 CONFIRMED`) are visually unmistakable at a 3-second glance, each backed by a concrete test number. | Replace bulleted excuses with a 3-to-4 column DrawingML fault-tree diagram. |
| **11** | **Decision & Discussion Ending Screen** | All (Final Slide) | Final main slide is **never** a blank `"Thank You / Q&A"` page—it stays anchored on Seminar Debate Prompts + Lab Roadmap (Scenarios 1–2) or SMART Milestones (Scenario 3). | Delete standalone `"Thank You"` slide; merge acknowledgements into Footer or Backup Appendix. |
| **12** | **CJK-Latin Hybrid Typography** | Bilingual / CN Decks | Chinese characters (`思源黑体` / `Microsoft YaHei`) and Latin/numeric tokens (`Arial` / `Segoe UI` / `Cambria Math`) have clean visual spacing without cramped glyphs or orphan punctuation wrap. | Enforce explicit `eastAsia` and `latin` OpenXML font slots and insert clean spacing around English/numeric tokens. |

---

### 4.3 Canonical JSON Slide IR Schemas for Signature Group-Meeting Modules

To ensure deterministic code generation across `build_deck.js` (`PptxGenJS`) and `python-pptx` builders with `latex_to_omml.py` two-phase math injection (`{{MATH:...}}` / `{{MATH_DISPLAY:...}}`), agents use these standardized slide IR payloads for the signature modules introduced in Scenarios 1–3:

#### 1. `toy_walkthrough` Slide IR (Scenario 1, Slide 9 — `split_equal_2col`)
```json
{
  "slide_index": 9,
  "scenario": "journal_club",
  "tracker": "TOY NUMERICAL WALKTHROUGH • SLIDE 09 OF 16",
  "title": "Step-by-Step Toy Example: Low-Rank KV Projection Cuts State Cache by 75% at Zero Dot-Product Error",
  "subtitle": "Evaluating identical 4D input token h_t across standard KV cache vs. absorbed MLA projection",
  "layout": "split_equal_2col",
  "disclaimer_badge": "TOY MECHANISM EXAMPLE — ILLUSTRATIVE NUMBERS, NOT BENCHMARK DATA",
  "left_card": {
    "header": "◼ Baseline: Standard Multi-Head KV Cache",
    "steps": [
      { "step": "Input", "expr": "{{MATH:\\mathbf{h}_t = [2, 0, 1, -1]^\\top \\in \\mathbb{R}^4}}" },
      { "step": "Project K, V", "expr": "{{MATH:\\mathbf{k}_t = [2, 1, 0, -1]^\\top, \\; \\mathbf{v}_t = [0, 2, 1, 1]^\\top}}" },
      { "step": "VRAM Stored", "expr": "8 floats / token (scales with n_heads × d_head)" },
      { "step": "Query Score", "expr": "{{MATH:\\mathbf{q}_t^\\top \\mathbf{k}_t = [1, 0, 1, 0] \\cdot [2, 1, 0, -1]^\\top = 2}}" }
    ]
  },
  "right_card": {
    "header": "✦ Proposed: Compressed Latent Vector + Absorbed Query",
    "steps": [
      { "step": "Input", "expr": "{{MATH:\\mathbf{h}_t = [2, 0, 1, -1]^\\top \\in \\mathbb{R}^4}}" },
      { "step": "Compress Latent", "expr": "{{MATH:\\mathbf{c}_t = W^{DKV}\\mathbf{h}_t = [3, 1]^\\top \\in \\mathbb{R}^2}}" },
      { "step": "VRAM Stored", "expr": "2 floats / token (Δ -75% cache footprint)" },
      { "step": "Absorbed Score", "expr": "{{MATH:((W^{UK})^\\top \\mathbf{q}_t)^\\top \\mathbf{c}_t = [1, -1] \\cdot [3, 1]^\\top = 2}}" }
    ]
  }
}
```

#### 2. `repro_audit_scorecard` Slide IR (Scenario 1, Slide 11 — `split_65_35`)
```json
{
  "slide_index": 11,
  "scenario": "journal_club",
  "tracker": "REPRODUCTION & ARTIFACT AUDIT • SLIDE 11 OF 16",
  "title": "Reproduction Verdict: Partial — Inference Weights Public, Pre-Training Kernel Gated at 64× H100",
  "layout": "split_65_35",
  "scorecard_rows": [
    { "axis": "Code & Checkpoints", "status": "PARTIAL", "evidence": "Inference + LoRA scripts on MIT license; pre-training fused Triton kernel omitted" },
    { "axis": "Data & Splits", "status": "VERIFIED", "evidence": "Exact HuggingFace dataset hashes & deduplication scripts provided" },
    { "axis": "Compute Wall", "status": "STRETCH", "evidence": "Full run = 3,200 H100-hrs; 1.3B proxy reproducible on 4× RTX 4090 in 14h" },
    { "axis": "Hyperparameter Stability", "status": "SENSITIVE", "evidence": "Appendix C2 notes divergence if RoPE decoupling lr > 1.5e-4 without 2k warmup" },
    { "axis": "Baseline Fairness", "status": "FAIR", "evidence": "GQA and MQA baselines re-trained on identical token budget and tokenizer" }
  ],
  "side_note": {
    "badge": "🔬 OUR RESEARCH CONNECTION",
    "categoryClass": "[Compute & Resource Cost]",
    "title": "Lab Cluster Replication Plan",
    "bullets": [
      "Skip full pre-training; mount authors' 7B checkpoint on our 2× A800 node (38GB VRAM).",
      "Validate rank-64 SVD initialization trick on our domain corpus in <8 GPU-hours."
    ]
  }
}
```

#### 3. `mece_fault_tree` & `ab_blocker_decision` Slide IR (Scenario 3, Slides 6 & 8)
```json
{
  "progress_diagnostics": {
    "slide_6_fault_tree": {
      "symptom": "Validation F1 stalled at 64.2% (Target Gate: >= 74.0%) at Epoch 10",
      "branches": [
        { "bucket": "Implementation Bug", "verdict": "RULED_OUT", "proof": "64-sample overfit reaches 99.8% in 80 steps; grad norm stable (0.5–1.1)" },
        { "bucket": "Optimization / Precision", "verdict": "RULED_OUT", "proof": "FP32 master weights + cosine/constant LR sweep changed Val F1 by <0.2%" },
        { "bucket": "Data / Truncation Artifact", "verdict": "CONFIRMED", "proof": "Manual audit of 100 errors: 31% had evidence clipped past 512-token cap" },
        { "bucket": "Core Hypothesis Null", "verdict": "PENDING", "proof": "Re-test after raising window to 2,048 tokens with FlashAttention-2" }
      ]
    },
    "slide_8_ab_decision": {
      "option_a_recommended": {
        "title": "Option A (Recommended): Extend Context to 2,048 + Sliding Chunk Pool",
        "cost": "12 GPU-hrs on 4× RTX 4090 (1.5 days)",
        "expected_signal": "Recover >= 7.5% F1 on truncated long-document subset",
        "kill_criterion": "Abort if Val F1 < 70.0% at Epoch 3"
      },
      "option_b_fallback": {
        "title": "Option B (Fallback): BM25 Sentence Pre-Extractor Before 512 Encoder",
        "cost": "4 hrs CPU indexing + 6 GPU-hrs",
        "tradeoff": "Zero VRAM increase, but introduces two-stage retrieval recall ceiling"
      },
      "explicit_pi_ask": "Confirm Option A priority and approve 4× 4090 queue reservation through Wednesday."
    }
  }
}
```
