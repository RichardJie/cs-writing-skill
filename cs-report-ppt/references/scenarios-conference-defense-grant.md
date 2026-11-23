# High-Stakes Academic Presentation Playbooks: Conferences, Degree Defenses, Grants, Awards & Job Talks

> **Module Role**: External-facing high-stakes presentation playbooks for [`cs-report-ppt`](../SKILL.md). Works alongside [`scenarios-group-meeting.md`](scenarios-group-meeting.md), [`languages-and-typography.md`](languages-and-typography.md), and [`palettes-and-layouts.md`](palettes-and-layouts.md).

This reference module extends `cs-report-ppt` from internal paper-reading decks into **formal, high-stakes, external-facing academic presentations** across both **international English venues** (NeurIPS, ICML, CVPR, ACL, CHI, SIGGRAPH, NSF/NIH/DARPA/ERC panels, R1 faculty searches) and **Chinese universities & funding agencies** (开题报告、中期考核、硕博毕业答辩、国自然 NSFC 优青/杰青/海外优青/重点项目、国家重点研发计划验收、企业横向课题、国奖/优博答辩、高校青椒教职应聘).

Every playbook below is **agent-executable** and inherits the four foundational invariants of `cs-report-ppt`:
1. **16:9 Widescreen Coordinate Canvas** (`13.333" × 7.500"`, Header `Y: 0.35"–1.55"`, Content `Y: 1.65"–6.85"`, Footer `Y: 7.00"–7.35"`), dynamically selecting from `hero_1col`, `split_equal_2col`, `split_65_35`, `grid_3col`, `grid_4col`, `quadrant_2x2`, and `asymmetric_2row` based on real visual geometry.
2. **Figure & Table Dominance ($\ge 80\%$ Visual Asset Coverage)**: Authentic 300+ DPI paper/thesis figures (`crop_figures.py` / PyMuPDF) with locked aspect ratios ($s = \min((W_{\text{card}}-2P_x)/W_{\text{orig}}, (H_{\text{card}}-2P_y)/H_{\text{orig}})$), native OpenXML DrawingML vector flowcharts (`roundRect`, `oval`, `rightArrow`), and focal-row cropped benchmark/KPI tables.
3. **Native Vector OMML Mathematics**: All display and inline equations injected as editable OpenXML Math (`latex_to_omml.py`) — zero blurry equation screenshots, zero raw LaTeX leaks, and strict scenario-specific equation ceilings.
4. **Pure Vision-in-the-Loop Self-Inspection (`view_file` at 150+ DPI)**: Every generated slide deck is rasterized via LibreOffice + PyMuPDF and audited pixel-by-pixel for auditorium legibility, spatial collisions, breadcrumb alignment, and visual balance before delivery.

---

## 1. Master Scenario Routing Matrix & Universal High-Stakes Laws

### 1.1 Scenario Selection & Pacing Physics Matrix

When the user requests a presentation, first classify the exact scenario using the table below to lock the **slide count, speaking pace, visual ratio, equation ceiling, and closing slide protocol**:

| Scenario ID | Venue / Milestone | Speaking Time (+ Q&A) | Target Slides | Pace (Sec / Slide) | Speech Budget (EN wpm @130 / CN cpm @205) | Visual Asset Floor | Native OMML Equation Cap | Table Complexity Cap | Recommended Palette | Final Lingering Slide Rule |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **1A. Conference Oral** | NeurIPS, ICML, CVPR, ACL, CHI, OSDI, CCF-A | **12 min** (+3 min Q&A) | **12–15** | 48–60 s | 1,500–1,600 words / 2,400–2,600 字 | $\ge 85\%$ | $\le 3$ slides | $\le 6\text{ rows} \times 5\text{ cols}$ | `academic_mono` / `cvpr_clean_blue` / `keynote_dark_oral` | **Contributions + QR/Code Summary** (No "Thank You" blank slide) |
| **1B. Spotlight / Lightning** | NeurIPS/ICML/ICLR Spotlight, ACL Short | **3–5 min** (0–1 min Q&A) | **4–7** | 40–45 s | 390–650 words / 600–1,025 字 | **100%** | $\le 1$ core eq. | $\le 4\text{ rows} \times 4\text{ cols}$ | `academic_mono` / `cvpr_clean_blue` | **Take-Home + Poster Slot/Board # + QR** |
| **1C. Poster Teaser / Madness** | SIGGRAPH Fast Forward, CHI/CVPR 1-Min | **1–2 min** (Zero Q&A) | **2–3** (or **1** 3-panel) | 20–30 s | 130–240 words / 200–380 字 | **100%** | **0** (Visual intuition only) | $\le 3$ hero bars/metrics | High-contrast light or dark | **Headline Delta + Poster Booth Map & QR** |
| **2A. Thesis Proposal** | 开题报告 (硕/博) / PhD Qualifying Exam | **12–20 min** (CN) / **25–35 min** (Intl) | **16–22** (CN) / **22–28** (Intl) | 45–65 s | 1,600–3,800 words / 2,500–4,100 字 | $\ge 80\%$ | $\le 4$ slides | Gap matrix + Gantt + Pilot table | `oxford_navy` / University VI + `academic_mono` | CN: Brief `致谢` $\rightarrow$ **总体技术路线与预期成果页**; Intl: **Aims Summary & Timeline** |
| **2B. Mid-Term Check** | 中期考核 / Thesis Progress Defense | **10–15 min** (+5–10 min Q&A) | **14–18** | 45–55 s | 1,300–1,950 words / 2,050–3,100 字 | $\ge 85\%$ | $\le 3$ slides | **Plan-vs-Actual Scorecard** + 2 result tables | `oxford_navy` / University VI | **完成度总览 + 后续冲刺里程碑页** |
| **2C. Master / PhD Defense** | 硕士答辩 (15–20m) / 博士答辩 (30–45m) | **18 min** (MS) / **35–45 min** (PhD) | **22–28** (MS) / **36–46** (PhD) | 45–60 s | MS: 3,600 字; PhD: 7,000–9,000 字 (or 5,200 EN words) | $\ge 85\%$ | 1–2 per innovation chapter | Focal tables ($\le 7$ rows) + **成果矩阵** | University Official VI Accent + Clean White Canvas | Brief `致谢` bow (10s) $\rightarrow$ **核心创新闭环与Q&A导航总控页** (+ Backup `B1–B6`) |
| **3A-1. Competitive Grant** | 国自然 NSFC (青基/优青/杰青/海外优青/重点) / NSF / NIH / DARPA | **10–15 min** (+5–10 min Q&A) | **16–22** | 40–50 s | 1,300–1,950 words / 2,050–3,100 字 | $\ge 85\%$ | $\le 2$ key mechanisms | Representative works matrix + Risk/Budget | `oxford_navy` / `nature_slate_teal` | **学术主线—代表作—拟开展研究一页全景图** |
| **3A-2. Project Acceptance** | 国家重点研发计划 / 重大专项 (中期/结题验收) | **15–20 min** (+10–15 min Q&A) | **22–28** | 40–50 s | 3,100–4,100 字 | $\ge 85\%$ | $\le 1$ (Focus on KPIs & systems) | **Verbatim《任务书》KPI对照表** + 经费决算表 | `oxford_navy` / Deep Sovereign Blue | **考核指标100%达成与示范效益总览页** (+ 佐证索引) |
| **3A-3. Industry / Horizontal** | 企业横向课题立项投标 / 结题交付汇报 | **10–15 min** (+10 min Discussion) | **10–15** | 50–60 s | 2,000–3,000 字 | $\ge 85\%$ | $\le 1$ (Business-mapped) | Business ROI table + Online A/B + Handover list | Client Brand Accent or `cvpr_clean_blue` | **业务痛点闭环、ROI收益与交付清单页** |
| **3B. Award / Scholarship** | 研究生国奖 / 校长奖 / 优博优硕 / 宝钢奖 | **3 min** (初审) / **5 min** (终审) | **5** (3m) / **8–10** (5m) | 30–38 s | 3m: 600 字; 5m: 950–1,050 字 | $\ge 90\%$ | $\le 1$ | **Slide 1 Portrait Dashboard** + Output matrix | Crisp `oxford_navy` / `mit_crimson_neutral` | **个人画像与代表性突破汇总页** |
| **3C. Faculty Job Talk** | Tenure-Track CS/STEM Job Talk / 高校教职学术报告 | **45–50 min** (+10–15 min Q&A) | **38–46** | 60–70 s | 5,800–6,400 EN words (CN variant: 20m / 25 slides) | $\ge 85\%$ | $\le 4$ (Intuition-scaffolded) | $\le 6$ rows; heavy system/concept diagrams | `academic_mono` / `oxford_navy` | **Research Ecosystem: Past Pillars $\rightarrow$ 10-Year Lab Vision** |

---

### 1.2 Five Universal High-Stakes Engineering Laws

1. **The 90% Rehearsal Buffer Rule**:
   - High-stakes timers are unforgiving: NeurIPS Spotlight chairs mute microphones at `03:00`; NSFC talent defense systems cut off projection at the exact second (`10:00` or `15:00`).
   - Always budget slide count and spoken script for **90% of the nominal slot** (e.g., design a 15-minute NSFC talk to finish cleanly at `13:30`; design a 3-minute国奖 pitch to land at `02:42`).
2. **Assertion-Evidence & Verb-Object Claim Headlines (结论先行标题铁律)**:
   - Following Michael Alley (*Assertion-Evidence*) and Jean-luc Doumont (*Trees, Maps, and Theorems*), **generic topic nouns (`Background`, `Method`, `Experimental Results`, `实验结果`, `文献综述`) are strictly banned as standalone slide titles** in high-stakes talks.
   - **English Rule**: Write a $\le 14$-word declarative sentence with a concrete verb and quantified outcome (`Decoupled Latent Attention Cuts KV Memory by 73% Without Perplexity Loss`).
   - **Chinese Rule**: Write a $\le 22$-character verb-object or mechanism-outcome claim (`解耦潜在注意力机制：零精度损失下降低73%显存占用`), placing the structural section name (`03 核心创新一 · 方法架构`) inside the `10pt` top tracker badge (`Y = 0.35"`), never wasting the `26pt` headline slot.
3. **Author-Voice Shift (`paper-boundaries` Strengths-First Framing)**:
   - Unlike internal lab Journal Clubs (`SKILL.md` Slide 13, where you critique an external author's blindspots), in **Conferences, Defenses, Grants, Awards, and Job Talks, YOU are the author/PI**.
   - Never include self-sabotaging phrasing (*"Although our method only works on..."*, *"Due to limited GPUs we failed to..."*). Frame scope boundaries positively as **principled design regimes** on main slides, and store honest boundary failure analyses in **hyperlinked Q&A Backup Slides** so you project supreme mastery when asked.
4. **Auditorium Back-Row Typography & Focal-Table Surgery**:
   - Conference halls and defense rooms span 12–25 meters. Enforce strict font floors: **Slide Title `24–28pt` Bold**, **Subtitle `15–16pt`**, **Card Body / Table Cells $\ge 14\text{pt}$** ($\ge 16\text{pt}$ for 1–5 min Spotlights/Awards; `12–13pt` permitted *only* for footnote citations).
   - **Never screenshot a 35-row LaTeX benchmark table**. Re-typeset or crop to **4–6 representative baselines + Ours**, bold top numbers, underline second-best, and add an explicit accent-tinted **`$\Delta$ vs. Best Baseline`** column (`+4.8% mAP`, `2.8× Speedup`).
5. **The Final Lingering Slide Law (黄金留屏页法则)**:
   - The final slide remains on screen for **3 to 15 minutes during Q&A**—longer than any other slide in the deck. Wasting `92 sq. inches` of canvas on giant word art reading *"Thank You! Questions?"* or *"感 谢 聆 听 · 敬请批评指正"* erases your technical evidence right when judges score your ballot.
   - **International Venues (Conferences, PhD Viva, Job Talks, NSF/ERC)**: End directly on a **Synthesis & Take-Home Dashboard** (3 numbered contributions, key headline metric chart, GitHub/Paper QR code, Future Horizon). Thank the audience *verbally*.
   - **Chinese Institutional Venues (开题/中期/毕业答辩、国自然、重点研发、国奖)**: Respect domestic academic etiquette by including a crisp, dignified **`致谢 / 恳请各位专家批评指正`** banner (`10 seconds` spoken bow), either **(Option A — Recommended)** integrated as the top/bottom 20% banner of a **核心贡献与成果总览留屏页**, or **(Option B)** followed immediately (1 click forward as Q&A begins) by a **Q&A 核心结论与预备页导航总控台** containing clickable buttons to Backup Slides `B1–B6`.

---

## 2. Pillar I: Academic Conference Presentations (Oral, Spotlight & Poster Teaser)

### 2.1 Conference Oral Presentation (12–15 Min Talk + 3 Min Q&A)

#### A. Operational Context & Pacing Budget
- **Target Venues**: NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, ACL, EMNLP, KDD, WWW, AAAI, CHI, OSDI, SOSP, SIGCOMM, DAC, ICRA, and domestic flagship conferences (CNCC, CCF-A专委年会, 中国自动化学会大会).
- **Audience Psychology**: 100–800 researchers in a darkened hall, half checking laptops or session schedules. They share broad disciplinary literacy (e.g., ML or Systems) but **have not read your paper**. If they lose the thread at Minute 4 (during notation overload), they never recover.
- **The 30 / 50 / 20 Pacing Allocation (for a 12-Minute Speaking Target in a 15-Min Slot)**:
  - **Act I — Hook, Bottleneck & Core Intuition (`00:00–03:30`, 3.5 min, Slides 1–4)**: Zero outline slide; start with an Empowerment Promise and visual failure of the status quo, culminating in your **single-sentence "Aha!" insight** demonstrated on a 2D/toy example *before* any Greek letters appear.
  - **Act II — Technical Mechanism & Empirical Proof (`03:30–09:45`, 6.25 min, Slides 5–11)**: High-level architecture overview $\rightarrow$ deep dive into 1–2 novel mechanisms (color-annotated OMML) $\rightarrow$ focal SOTA benchmark table $\rightarrow$ diagnostic ablation ("*why* it works") $\rightarrow$ Pareto efficiency / scaling law.
  - **Act III — Qualitative Reality, Impact & Lingering Summary (`09:45–11:45`, 2.0 min, Slides 12–14)**: Qualitative visual comparison / video keyframe strip $\rightarrow$ ecosystem release / broad takeaway $\rightarrow$ Contributions + Artifact QR Dashboard left on screen for Q&A (`11:45–15:00`).

#### B. Complete 14-Slide Conference Oral Spine (Author Perspective)

| Slide # | Time Window | Tracker Badge (`10pt`) | Recommended Grid | Assertion Headline Template (EN / CN) | Mandatory Visual Asset, OMML & Table Spec | Density Budget |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | `00:00–00:35` | `CONFERENCE ORAL • [VENUE YEAR]` | `split_65_35` or `hero_1col` | `[Paper Title]` + Subtitle: `[1-Line Core Value Proposition]` | **Teaser Trade-off / Output Hero Figure** (left 65%) + Author photos/logos, Affiliation, Paper ID, Code/Project QR badge (right 35%). | Title $\le 16$ words; zero body bullets. |
| **2** | `00:35–01:30` | `MOTIVATION & STAKES` | `split_equal_2col` | EN: `[Target Task] Is Blocked by [Concrete Bottleneck] at Scale`<br>CN: `[目标任务]在真实规模下面临严重的[核心瓶颈]` | **Left**: Real-world deployment stakes / application visual.<br>**Right**: Striking qualitative failure or scaling wall plot (e.g., VRAM OOM / collapse curve). | $\le 3$ micro-bullets ($\le 12$ EN words / $\le 20$ CN chars each). |
| **3** | `01:30–02:30` | `WHY PRIOR ART FAILS` | `split_65_35` | EN: `Existing Paradigms Force a False Trade-off Between [X] and [Y]`<br>CN: `现有主流范式难以兼顾[指标X]与[指标Y]的根本矛盾` | **65% Main**: 2D trade-off scatter plot or side-by-side structural comparison of Paradigm A vs. Paradigm B (fencing your gap without listing 15 citations). **35% Side**: Root-cause diagnosis box. | Max 2 baseline families + root-cause summary. |
| **4** | `02:30–03:30` | `KEY INSIGHT ("AHA!" MOMENT)` | `hero_1col` (Visual Split) | EN: `Core Insight: [Mechanism] Eliminates [Bottleneck] via [Property]`<br>CN: `核心洞察：利用[关键性质]实现[机制突破]` | **Toy Numerical / Geometric Walkthrough**: Before-vs-After schematic on a 3-token / 2D manifold toy example so every listener grasps the intuition *with zero equations*. | 1 bold bottom-line callout strip (`16pt Bold`). |
| **5** | `03:30–04:30` | `SYSTEM / METHOD OVERVIEW` | `hero_1col` | EN: `[Method Name]: End-to-End Pipeline in Three Stages`<br>CN: `[方法名称]：三阶段端到端协同架构总览` | **Full-Width Vector Pipeline Diagram**: Standard modules in neutral slate (`#F1F5F9`); **Proposed Novel Modules** highlighted in accent tint with `✦ OUR CONTRIBUTION` pills; numbered stages `① → ② → ③`. | Diagram labels $\ge 13\text{pt}$; 3 bottom stage captions. |
| **6** | `04:30–05:45` | `MECHANISM I: [MODULE NAME]` | `split_65_35` | EN: `Stage ①: [Module 1] Compresses [Input] While Preserving [Invariant]`<br>CN: `机制一：[模块名称]在保持[不变量]前提下实现高效表征` | **65% Main**: Zoomed sub-architecture diagram (dimming Stages ②–③) + tensor shape transformations ($\mathbf{X} \in \mathbb{R}^{B \times L \times D} \to \mathbf{Z} \in \mathbb{R}^{B \times L \times r}$). **35% Side**: **1 Color-Annotated Native OMML Equation**. | 1 OMML display eq. + 3 color-matched term tags. |
| **7** | `05:45–07:00` | `MECHANISM II / THEORY` | `split_equal_2col` | EN: `Stage ②: [Theorem / Objective] Guarantees [Property / Bound]`<br>CN: `机制二与理论保障：[定理/目标函数]确保[收敛性/误差上界]` | **Left**: Clean **Theorem / Optimization Box** in native OMML (high-level bound only; full proof deferred to Backup `B1`). **Right**: Empirical verification plot showing theoretical bound tracking actual error. | 1 Theorem box ($\le 4$ lines) + 1 empirical validation plot. |
| **8** | `07:00–08:00` | `PRIMARY BENCHMARK RESULTS` | `asymmetric_2row` | EN: `[Method] Achieves SOTA Across [N] Benchmarks (+[X]% Over [Best Baseline])`<br>CN: `[方法]在[N]项权威基准全面领先，核心指标提升[X]%` | **Top Wide Card**: **Focal Benchmark Table** ($\le 6$ rows $\times 5$ cols; bold SOTA, accent-shaded `Ours` row, explicit `$\Delta$` column). **Bottom Dual Cards**: Evaluation protocol fairness badge + Statistical significance ($p < 0.01$ / 5 seeds). | Max 30 table cells total; cell font $\ge 14\text{pt}$. |
| **9** | `08:00–09:00` | `DIAGNOSTIC ABLATIONS` | `split_65_35` | EN: `Both [Component A] and [Component B] Are Essential for Peak Gain`<br>CN: `消融归因验证：[模块A]与[模块B]贡献呈显著正交互补` | **65% Main**: Progressive waterfall bar chart or 4-row incremental ablation (`Baseline → +Mod A → +Mod B → Full Ours`). **35% Side**: Mechanistic explanation of *why* removing Mod A triggers collapse. | 4-bar waterfall or 4-row table; $\le 3$ bullets. |
| **10** | `09:00–09:45` | `PARETO EFFICIENCY & SCALING` | `split_equal_2col` | EN: `[Method] Shifts the Accuracy–Latency Pareto Frontier by [K]×`<br>CN: `效率帕累托前沿：推理吞吐提升[K]倍且随规模稳健扩展` | **Left**: Pareto curve (Throughput / VRAM / Cost vs. Quality; upper-left / upper-right star marker for `Ours`). **Right**: Compute or sequence-length scaling law plot ($L = 4\text{K} \to 128\text{K}$). | 2 high-DPI vector plots with direct data callouts. |
| **11** | `09:45–10:30` | `QUALITATIVE / DEMO EVIDENCE` | `grid_3col` or `hero_1col` | EN: `Qualitative Comparison: Crisp Fidelity Under Extreme [Stress Regime]`<br>CN: `定性对比与实机演示：极端复杂场景下保持高保真输出` | **Side-by-Side Visual Grid** (`Input | Best Baseline [Artifact Callout] | Ours [Clean Callout]`) OR **Live Video with 3-Frame Static Fallback Strip** ($t_0, t_1, t_2$). | Zero long bullets; use red/green bounding-box callouts on images. |
| **12** | `10:30–11:05` | `STRESS-TEST & SCOPE REGIME` | `split_equal_2col` | EN: `Principled Operating Regime & Robustness Under Distribution Shift`<br>CN: `分布外泛化稳健性与适用边界定量刻画` | **Left**: OOD / noise corruption robustness curve. **Right**: Principled operating envelope (when to set rank $r=64$ vs. $r=128$) + future extension hook (pre-empting Reviewer #2's obvious Q&A question!). | 1 plot + 2 crisp design-guideline cards. |
| **13** | `11:05–11:30` | `OPEN SCIENCE & ECOSYSTEM` | `grid_3col` | EN: `Plug-and-Play Open-Source Release & Drop-In Integration`<br>CN: `开源生态与即插即用部署：3行代码无缝接入现有框架` | **Card 1**: 4-line syntax-highlighted Python/CLI snippet (`pip install ...`). **Card 2**: Pretrained checkpoints / dataset hub table. **Card 3**: Real-world downstream adoption scenarios. | Optional slide (merge into Slide 14 if slot is 10 min). |
| **14** | `11:30–12:00` *(Lingers in Q&A)* | `SUMMARY & ARTIFACTS` | `split_65_35` | EN: `Summary: [1-Sentence Memorable Bottom Line of the Paper]`<br>CN: `总结：[一句话凝练全文核心突破与范式价值]` | **65% Main**: **3 Numbered Take-Home Pillars** (each paired with a mini icon/thumbnail of Fig. 2, Fig. 3, Table 1 + headline delta). **35% Side**: Large scannable **QR Codes** (Paper PDF / GitHub / Project Page), Poster Session Slot, Contact Email. | Leaves 100% of core evidence visible throughout Q&A! |

#### C. Video & Live Demo Resilience Protocol
- Never rely on live SSH terminals or browser tabs during a 12-minute conference oral.
- **Dual-Layer Asset Rule**: Embed pre-recorded `1080p MP4` (muted, auto-play, `60fps`) for PowerPoint live playback, **AND** place a 3-panel static high-DPI keyframe strip (`t = 0.0s`, `t = 1.5s`, `t = 3.0s` with motion arrows) directly on the slide layer underneath (or on the PDF export version) so PDF handouts and LibreOffice Vision QA remain 100% self-explanatory.

---

### 2.2 Spotlight / Lightning Talk (3–5 Min Rapid Pitch)

#### A. Operational Context & Ruthless Compression Surgery
- **Target Venues**: NeurIPS / ICML / ICLR Spotlight (`3–5 min`), CVPR Highlight, KDD / ACL Short Oral, Workshop Lightning Talks.
- **Audience Psychology**: Attendees watch **10–15 Spotlights back-to-back** in a single block to decide **which 3 posters to visit tonight**. Your goal is *not* to teach every proof detail—it is to plant **one unforgettable insight + one undeniable result** that compels them to walk to your poster board.
- **What Must Be Surgically Excised from a 14-Slide Oral**:

| Oral Component | Fate in 3–5 Min Spotlight | Surgical Replacement Rule |
|:---|:---|:---|
| Outline / Roadmap Slide | **100% Deleted** | Zero agenda slides in a $\le 5$-minute talk. |
| Related Work / Lineage (2 slides) | **Compressed into 15 sec on Slide 2** | One visual contrast diagram showing why *all* existing methods hit the same wall. |
| Multi-Stage Architecture + 3 Equations | **1 Intuitive Diagram + Max 1 Equation** | Show only the *single novel module* (`✦`) against a grayed-out standard backbone. |
| 10-Model Benchmark Table + 4 Ablations | **1 Hero Bar/Pareto Chart (4 bars max)** | Plot `Prior SOTA vs. Ours` on 2 primary metrics + 1 inline callout badge (`2.8× faster`). |
| Verbose Acknowledgements Slide | **Merged into Slide 5 Footer** | Put co-author thumbnails & funding logo strip along the bottom of the Final Takeaway + Poster CTA slide. |

#### B. Complete 5-Slide Spotlight Spine (`3:00` Target = `02:45` Rehearsed)

| Slide # | Time Window | Tracker Badge | Grid Model | Assertion Headline Template (EN / CN) | Visual & Content Specification |
|:---|:---|:---|:---|:---|:---|
| **1** | `00:00–00:25` | `SPOTLIGHT • [POSTER #B-42]` | `split_65_35` | `[Short Punchy Title]: [Quantified Value Hook]` | **65%**: Eye-catching teaser visual comparing Baseline Failure vs. Ours. **35%**: Authors, affiliations, **Giant Poster Session Time & Board Badge** (`Thu Dec 10 • 18:30 • Hall B #42` — show it on Slide 1 *and* Slide 5!). |
| **2** | `00:25–01:05` | `THE BOTTLENECK` | `split_equal_2col` | EN: `Why Current [Models] Break Under [Condition]`<br>CN: `痛点直击：为何现有[模型]在[场景]下全面失效？` | **Left**: Visual failure mode / memory explosion curve. **Right**: 2 crisp root-cause bullets (`16pt`) isolating the exact false assumption in prior work. |
| **3** | `01:05–01:55` | `CORE INSIGHT & MECHANISM` | `hero_1col` | EN: `Key Idea: Replace [Costly Step] with [Our Mechanism]`<br>CN: `核心突破：以[新机制]重构[高开销模块]` | **Before-vs-After Mechanism Schematic**: Top row = Conventional $O(L^2)$ bottleneck; Bottom row = Proposed $O(Lr)$ mechanism (`✦`) + at most **1 ultra-clean native OMML formula** ($\le 5$ symbols). |
| **4** | `01:55–02:30` | `HEADLINE EMPIRICAL PROOF` | `split_65_35` | EN: `[+X%] Higher Accuracy at [K]× Lower Compute Across [Benchmarks]`<br>CN: `核心实证：[N]大基准提升[X]%，推理成本降低[K]倍` | **65%**: Clean grouped bar chart or Pareto frontier (`3 baselines + Ours`, `16pt` direct value labels above bars). **35%**: 1 qualitative visual win or 1 killer ablation takeaway pill. |
| **5** | `02:30–02:50` | `VISIT POSTER #B-42` | `split_65_35` | EN: `Takeaway: [1-Sentence Bottom Line] — See Full Proofs at Poster #B-42`<br>CN: `总结：[一句话核心结论] · 欢迎莅临海报 #B-42 深入交流` | **65%**: 3 ultra-crisp takeaway bullets ($\le 10$ words each) + hook of what awaits at the poster (*"At our poster: theoretical bounds, 70B scaling & live demo"*). **35%**: High-contrast **QR Code** (`w = 2.2"`) + **Poster Floor-Plan Pin / Booth ID** + Co-author photo strip. |

> **5-Minute Extension (`6–7 Slides`)**: Add **Slide 3b** (Toy example walkthrough before mechanism) and **Slide 4b** (Qualitative visual comparison / secondary ablation plot).

---

### 2.3 Poster Teaser / 1-Minute Madness / Fast Forward (1–2 Min Pitch)

#### A. The Inverted Paper Law (`Result First, Secret Sauce Second`)
In a `30–90 second` Fast Forward (SIGGRAPH, CHI Madness, CVPR/ICCV Poster Preview), starting with background and math guarantees getting cut off before showing a single result. Execute the **Inverted 4-Beat Arc**:
1. **Beat 1 — Visceral Pain Hook (`00:00–00:12`)**: 1 relatable frustration or catastrophic baseline failure visual.
2. **Beat 2 — Show the Magic Immediately (`00:12–00:35`)**: Flash your most jaw-dropping visual output, real-time robot clip, or headline SOTA leap *first*.
3. **Beat 3 — One-Sentence Secret Sauce (`00:35–00:48`)**: 1 conceptual graphic explaining *what trick made it possible* (zero equations, zero Greek symbols).
4. **Beat 4 — Poster Call-to-Action (`00:48–00:58`)**: Memorable paper nickname + Poster Board ID + QR code.

#### B. Complete 3-Slide Teaser Spine (`60 Seconds`)
- **Slide 1 (`00:00–00:15`, `split_equal_2col`)**: Headline: `Current [Systems] Fail Catastrophically When [Condition]` — Left: Baseline failure image/frame; Right: 1-line problem statement (`20pt Bold`).
- **Slide 2 (`00:15–00:40`, `hero_1col`)**: Headline: `Meet [Method]: Real-Time [Capability] with [+X%] Higher Fidelity` — Full-bleed hero comparison (`Baseline` vs. `Ours`) + 2 giant metric callout badges (`28pt Bold`: `73% Less VRAM`, `3.1× Faster`).
- **Slide 3 (`00:40–00:58`, `split_65_35`)**: Headline: `Secret Sauce: [1-Phrase Intuition] — Come Try It Live at Poster #A-19!` — Left 65%: 3-box conceptual diagram (`Input → [✦ Magic Step] → Output`); Right 35%: Giant Poster Badge (`#A-19 • Tue PM`) + QR code (`w = 2.4"`).

#### C. Single-Slide Madness Canvas Recipe (When Venue Enforces a Strict `1-Slide PDF` Limit)
Many workshops and conferences require uploading **exactly 1 static 16:9 PDF slide** for a 60-second teaser. Use `grid_3col` (`Y: 1.65"–6.85"`, `w = 3.877"` per column) with high-impact `18pt+` typography:
- **Header (`Y: 0.35"–1.50"`)**: Paper Short Name + Full Title (`24pt Bold`) + Right-aligned Pill Badge `[POSTER #A-19 • SESSION 2]` (`X = 9.50", W = 3.23", H = 0.45"`, solid accent fill, white bold text).
- **Col 1 (`X = 0.600"`, Problem)**: Header `1. The Bottleneck` + Failure visual + 1 caption (`15pt`).
- **Col 2 (`X = 4.727"`, Core Idea)**: Header `2. Our Key Insight` + Simplified 2-block schematic (`✦`) + 1 caption (`15pt`).
- **Col 3 (`X = 8.854"`, Magic Result & QR)**: Header `3. SOTA Leap` + Compact 3-bar chart (`+6.4%`) + Bottom QR Code (`1.5" × 1.5"`) beside GitHub URL.

---

## 3. Pillar II: Degree Milestone Defenses (开题报告 · 中期考核 · 硕博毕业答辩)

University degree defenses follow an institutional accountability contract across three sequential gates: **Proposal (`开题报告` — Can this succeed and is it worth a degree?)**, **Mid-Term (`中期考核` — Is execution on schedule with real empirical traction?)**, and **Final Defense (`毕业答辩` — Do the completed innovations form a coherent, degree-worthy scholarly contribution?)**.

---

### 3.1 Thesis Proposal / PhD Qualifying Exam (开题报告 / Doctoral Proposal Defense)

#### A. Evaluator Psychology & Bilingual Institutional Calibration
- **Chinese University Committee (`开题专家组`, 3–5 Professors, `12–15 min` Master / `15–25 min` PhD)**: Audits four fatal failure modes: (1)选题陈旧或工程堆砌无科学深度, (2)文献综述写成编年史流水账且未导出本文切入点, (3)**把“研究内容（干什么活）”错写成“关键科学问题（底层机理瓶颈）”**, and (4)技术路线空泛、毫无前期预实验支撑。
- **International PhD Qualifying / Proposal Committee (`25–35 min` Talk + `30–45 min` Closed/Open Interrogation)**: Acts as a "Rescue & Redirect" advisory board checking whether **Specific Aims 1–3** are decoupled enough that **if Aim 1 hits a negative result, Aim 2 does not collapse** (mandatory **Contingency / Go-No-Go Fallback Plan** per Aim).

#### B. Surgical Distinction: `研究内容` vs. `拟解决的关键科学问题`
Agents generating Proposal slides must strictly separate *tasks* from *scientific bottlenecks*:

| Dimension | ❌ Common Defect (Task Disguised as Science) | ✅ High-Scoring Formulation (Mechanistic Bottleneck) |
|:---|:---|:---|
| **CN 开题表述** | “关键科学问题1：研究多模态特征融合网络的搭建与参数调优；问题2：开发边缘端量化部署系统。” *(这是工程任务清单，会被评委直接批驳！)* | “**关键科学问题1（跨模态异构表征失配机理）**：在强噪声非对齐采样下，揭示高频视觉局部特征与稀疏语义空间的流形坍缩规律，建立保拓扑的低秩耦合映射边界。” |
| **EN Proposal** | *"Research Question 1: Build a Transformer pipeline for medical segmentation and test it on 3 datasets."* | *"Scientific Question 1 (Non-Stationary Calibration Bound): Under hospital-level covariate shift, what minimal spectral invariant guarantees calibrated uncertainty without target labels?"* |
| **Sentence Formula** | `[动词: 搭建/实现/采集] + [系统/模块名称]` *(Keep ONLY in 研究内容)* | `针对[特定场景]下因[底层矛盾A与B冲突]导致的[失效现象]，拟揭示[演化规律/数学机理]，突破[理论或算法瓶颈]。` *(Limit to **2–3** crisp items)* |

#### C. Literature Review Anti-Laundry-List Rule (`批判性范式对比矩阵`)
Never generate bullet slides listing `[1] Wang et al. (2022) proposed X... [2] Liu et al. (2023) used Y...`. Always construct a **Paradigm × Limitation Gap Matrix** (`asymmetric_2row` or `hero_1col`):
- **Columns**: `方法流派 (Paradigm) | 代表性工作 (Key Works) | 核心机理优势 (Strengths) | 未解决的共性局限 (Unresolved Bottleneck) | 本文拟突破切入点 (Our Thesis Hook)`
- **Bottom Highlighted Row**: `✦ 本课题拟提出方案 (Proposed Thesis)` showing `✓` across the exact columns where prior paradigms show `✗`.

#### D. Complete 18-Slide Thesis Proposal Spine (CN `开题报告` & Intl `Qualifying Exam` Dual-Mapped)

| Slide # | Time (15m / 30m) | Section Badge | Grid Model | Assertion Headline Template (CN / EN) | Mandatory Visual, Table & Proof Assets |
|:---|:---|:---|:---|:---|:---|
| **1** | `00:00–00:30` | `THESIS PROPOSAL • 开题报告` | `hero_1col` | `[学位论文题目]` (明确标注：博士/硕士学位论文开题报告) | University official VI badge, Student Name/ID, Major, Advisor, Lab, Date. Zero clutter. |
| **2** | `00:30–01:30` | `1. 选题背景与战略需求` | `split_equal_2col` | CN: `国家重大需求与[领域]规模化落地亟需突破[核心痛点]`<br>EN: `[Domain] Demands Scalable [Capability] Beyond Current Limits` | **Left**: Industry/scientific macro-demand chart (authoritative whitepaper/policy/benchmark trend). **Right**: Concrete failure case in real deployment. |
| **3** | `01:30–02:30` | `1. 问题抽象与理论意义` | `split_65_35` | CN: `从工程表象到科学本质：[现实痛点]映射为[核心数学/机理矛盾]`<br>EN: `Formalizing the Practical Bottleneck as a Fundamental [X–Y] Trade-off` | **65%**: Conceptual abstraction diagram mapping domain phenomenon $\to$ formal mathematical problem space. **35%**: Theoretical + practical value cards. |
| **4** | `02:30–03:45` | `2. 国内外研究现状 (1/2)` | `grid_3col` | CN: `主流技术路线演进脉络：三大流派的范式演替与边界`<br>EN: `Taxonomic Lineage: Three Dominant Paradigms in Literature` | 3 evolutionary paradigm cards (`早期机理驱动` $\to$ `纯数据驱动深度学习` $\to$ `知识-数据协同前沿`) with key milestone citations (`Author, Venue'YY`). |
| **5** | `03:45–05:00` | `2. 文献批判与切入点 (2/2)` | `hero_1col` | CN: `现有研究共性盲区：缺乏兼顾[维度A]、[维度B]与[维度C]的统一机制`<br>EN: `Critical Gap Matrix: No Existing Method Satisfies [A, B, C] Jointly` | **5-Column Paradigm Gap Matrix Table** ($\le 5$ rows) culminating in the accent-highlighted `✦ 本课题切入点` row. |
| **6** | `05:00–06:00` | `3. 总体目标与研究内容概览` | `split_65_35` | CN: `总体研究目标与“三层递进式”核心研究内容体系`<br>EN: `Overarching Thesis Goal & Three Coupled Specific Aims` | **65%**: Coupling diagram of **研究内容一 (基础表征) $\to$ 研究内容二 (核心优化) $\to$ 研究内容三 (系统验证)**. **35%**: Quantified target metrics. |
| **7** | `06:00–07:15` | `3. 拟解决的关键科学问题` | `split_equal_2col` | CN: `聚焦两大底层科学瓶颈：[科学问题一]与[科学问题二]`<br>EN: `Two Core Scientific Questions & Testable Hypotheses` | **2 High-Contrast Scientific Bottleneck Cards** using the mechanistic conflict formula + native OMML mathematical problem statement. |
| **8** | `07:15–08:45` | `4. 总体技术路线图 ★` | `hero_1col` | CN: `总体技术路线图：问题驱动、章节咬合与实验闭环全景`<br>EN: `Master Technical Roadmap: Input → Aims 1–3 → Validation` | **Full-Canvas Native Vector Master Flowchart** (`输入数据/场景层 → 核心研究内容1/2/3算法模块 → 评测基准与原型系统 → 预期学术/应用指标`). |
| **9** | `08:45–09:45` | `4. 拟开展工作一 (Aim 1)` | `split_65_35` | CN: `研究内容一：[方法名称]——拟采用的技术方案与理论建模`<br>EN: `Aim 1: [Method] Formulation, Architecture & Evaluation Plan` | **65%**: Proposed module architecture + 1 native OMML objective. **35%**: Target datasets, baselines & **Contingency Plan (`备选预案`)**. |
| **10** | `09:45–10:45` | `4. 拟开展工作二 (Aim 2)` | `split_65_35` | CN: `研究内容二：[方法名称]——承接内容一并突破[动态/规模瓶颈]`<br>EN: `Aim 2: Scaling to [Regime] with Theoretical Guarantees` | **65%**: Algorithmic workflow + interface from Aim 1. **35%**: Evaluation metrics & **Risk Mitigation / Fallback Route** if primary assumption relaxes. |
| **11** | `10:45–11:30` | `4. 拟开展工作三 (Aim 3)` | `split_equal_2col` | CN: `研究内容三：面向[真实场景]的软硬件协同集成与实证验证`<br>EN: `Aim 3: End-to-End System Integration & Real-World Benchmark` | **Left**: System testbed / clinical / industrial validation architecture. **Right**: Target end-to-end latency/accuracy thresholds. |
| **12** | `11:30–12:15` | `5. 特色与预期创新点` | `grid_3col` | CN: `本课题拟形成的三项递进式学术创新点凝练`<br>EN: `Three Anticipated Theoretical & Methodological Innovations` | 3 crisp cards: `创新点一 (新机理/表征)`、`创新点二 (新算法/理论界)`、`创新点三 (新系统/范式)` — verb-object phrasing, zero exaggerated buzzwords (`填补国际空白` banned!). |
| **13** | `12:15–13:15` | `6. 前期研究基础与预实验 ★` | `split_65_35` | CN: `前期预实验验证：已完成[模块一]原型开发并取得初步正收益`<br>EN: `Preliminary Pilot Results De-Risk Aim 1 Feasibility` | **65%**: Authentic **Pilot Experiment Table / Convergence Curve** already obtained by the student (`Baseline 74.2% → Pilot Ours 78.9%`). **35%**: Completed codebase/data prep status. |
| **14** | `13:15–13:50` | `6. 四维可行性论证` | `quadrant_2x2` | CN: `理论、技术、数据与实验平台四维可行性闭环支撑`<br>EN: `Feasibility Guarantee: Theory, Infrastructure, Data & Lab Track Record` | **4 Quadrants**: `① 理论可行性` (prior theorems), `② 技术积累` (lab repos), `③ 数据与硬件算力` (e.g., `8× H100 / 实验台架已就位`), `④ 导师团队前期项目支撑`. |
| **15** | `13:50–14:20` | `7. 学位论文结构与进度计划` | `asymmetric_2row` | CN: `学位论文拟定章节大纲与季度里程碑甘特图`<br>EN: `Dissertation Chapter Blueprint & Quarterly Execution Gantt` | **Top**: 6-Chapter dissertation outline (`第1章 绪论 ... 第6章 总结`). **Bottom**: **Quarterly Gantt Chart** (`2026 Q4 – 2028 Q2`) with clear mid-term & submission gates. |
| **16** | `14:20–14:45` | `7. 预期成果与考核指标` | `split_equal_2col` | CN: `预期学术论文、发明专利与开源系统产出计划`<br>EN: `Expected Publications, Open-Source Artifacts & Graduation Criteria` | Concrete mapping: Aim 1 $\to$ `CCF-A/SCI Q1 ×1 (在研/拟投)`; Aim 2 $\to$ `顶会/顶刊 ×1`; Aim 3 $\to$ `发明专利 ×1 + 原型系统`. |
| **17–18** | `14:45–15:00` | `致谢与恳请指导 / Q&A` | `split_65_35` | CN: `恳请各位专家批评指正 · 总体路线与关键科学问题留屏`<br>EN: `Summary of Specific Aims, Pilot Evidence & Timeline` | Dignified `恳请专家指导` header + miniature **Master Technical Roadmap + 3 Aims Summary** kept visible on screen for committee steering questions! |

---

### 3.2 Mid-Term Check / Progress Defense (中期考核 / Thesis Progress Review)

#### A. Evaluator Psychology & The Anti-Effort-Diary Rule
Mid-term committees care about **two hard facts**: (1) *Did you fulfill your Proposal contract on schedule with authentic quantitative results?* and (2) *Are the remaining 6–12 months de-risked enough for on-time blind thesis review (`盲审`)?*
- **Strictly Banned**: Effort diaries (`读了50篇文献、学习了PyTorch源码、调了三个月参`). Every slide must present **deliverables, curves, tables, or diagnosed root causes**.

#### B. Mandatory Core Visual: `开题计划对照完成度矩阵` (Plan-vs-Actual Scorecard)
Slide 3 of every Mid-Term deck must be a full-width `hero_1col` scorecard table:

| 开题预定研究板块 | 开题设定指标 | 当前完成进度 | 核心实证产出与论文/专利状态 | 偏差诊断与方案微调说明 |
|:---|:---|:---|:---|:---|
| **研究内容一（第3章）** | 提出XX表征模型，精度超SOTA $\ge 3\%$ | **`[██████████] 100%`** | 基准提升 **+4.6%**；一作论文已录用 **CVPR 2026** | 按期超额完成，无偏差 |
| **研究内容二（第4章）** | 建立动态自适应算法，时延降低 $40\%$ | **`[███████░░░] 75%`** | 核心算法跑通（时延 **-43%**）；论文在投 **IEEE TPAMI (Under Review)** | 极端长序列下收敛震荡，已引入谱归一化约束解决 |
| **研究内容三（第5章）** | 端到端原型系统与真实产线验证 | **`[███░░░░░░░] 30%`** | 完成硬件接口联调与数据集清洗；拟于下季度完成消融 | 原定公开集存在标注噪声，新增自采校准集补充 |

#### C. Complete 15-Slide Mid-Term Check Spine (`12 Min` Target)
1. **Slide 1 (`封面`)**: Thesis Title + `博士/硕士学位论文中期考核汇报` + Student/Advisor/Date.
2. **Slide 2 (`开题回顾`, `00:25–01:10`)**: 1-slide compact recap of Research Background, Core Scientific Questions & Master Technical Roadmap (never re-spend 4 minutes on Proposal background!).
3. **Slide 3 (`计划对照总览 ★`, `01:10–02:15`)**: **Plan-vs-Actual Completion Scorecard Table** (exact schema above).
4. **Slides 4–6 (`已完成工作一详解`, `02:15–05:15`)**: Closed-loop presentation of **Chapter 3 (100% Done)** — Mechanism architecture $\to$ Native OMML formulation $\to$ SOTA benchmark & ablation tables.
5. **Slides 7–9 (`阶段性工作二详解`, `05:15–08:00`)**: Progress on **Chapter 4 (70–80% Done)** — Current architecture $\to$ Preliminary benchmark gains $\to$ Remaining ablation checklist.
6. **Slide 10 (`推进中工作三进展`, `08:00–08:50`)**: Initial prototype / dataset / experimental setup for **Chapter 5 (25–40% Done)**.
7. **Slide 11 (`难点剖析与方案微调 ★`, `08:50–09:50`)**: Honest engineering/theoretical blocker encountered since Proposal $\to$ Diagnostic root cause $\to$ **Validated Adjustment (`原方案 vs. 修正方案对比`)** proving scientific maturity.
8. **Slide 12 (`大论文撰写与盲审倒计时甘特图`, `09:50–10:40`)**: Month-by-month countdown (`M1–M8`) to thesis draft completion, internal pre-defense (`预答辩`), similarity check, and external blind review (`双盲送审`).
9. **Slide 13 (`已取得学术成果矩阵`, `10:40–11:15`)**: Published / Accepted / Under-Review papers, patents, and coursework credit completion (`学分达标情况`).
10. **Slides 14–15 (`总结与恳请专家把关`, `11:15–11:45`)**: Dignified bow + lingering dashboard of **Completion Scorecard + Countdown Milestones**.

---

### 3.3 Master & PhD Thesis / Dissertation Defense (硕士/博士毕业答辩)

A graduation defense is the crowning academic performance of a degree. The #1 reason strong candidates receive harsh committee critiques is **"三篇小论文机械拼凑感" (Three Stitched Papers Syndrome)**—presenting Chapters 3, 4, and 5 as disconnected conference papers with inconsistent notation and no causal thread.

#### A. Master vs. PhD Structural Calibration

| Calibration Axis | Master Thesis Defense (`硕士毕业答辩`) | PhD Dissertation Defense (`博士毕业答辩 / Viva`) |
|:---|:---|:---|
| **Speaking Window** | **15–20 min** (+ 10–15 min Q&A) | **30–40 min** in CN (+ 20–30 min Q&A); **40–50 min** in US/EU |
| **Slide Budget** | **22–28 main slides** (+ 5–8 Backup slides) | **36–46 main slides** (+ 10–15 Backup slides) |
| **Core Chapters** | **2–3 Chapters** (e.g., Method Innovation + System/Application Verification) | **3–4 Progressive Innovation Chapters** (Chapters 3, 4, 5, [6]) |
| **Committee Bar** | Solid mastery of domain methods, **full engineering/experimental workload (`工作量饱满`)**, complete closed-loop system or empirical validation. | **Systematic originality (`系统性创造性成果`)**, deep theoretical modeling, progressive causal coupling across chapters, independent scholarly authority. |
| **Notation Rule** | Unified symbol table across all chapters ($\mathbf{X}, \mathcal{L}$). | **Mandatory global mathematical notation unification** across all 3–4 chapters (never copy-paste conflicting symbols $\mathbf{h}_t$ vs. $\mathbf{z}_i$ from separate published papers!). |

---

#### B. Architectural Signature 1: `总体技术路线图贯穿导航条` (Master Roadmap & Persistent Breadcrumb Bar)

To visually prove your thesis is an organic whole, enforce **two synchronized structural devices**:

##### 1. Persistent Top Breadcrumb Navigation Strip (`Y: 0.00" → 0.32"`)
On every content slide (`Slides 3` through `Conclusion`), reserve a sleek `0.32"` top navigation bar across the `13.333"` canvas (shifting `Header Zone` slightly to `Y: 0.38"–1.55"` while keeping `Content Zone` intact at `Y: 1.65"–6.85"`):

```
0.00" ┌──────────────────────────────────────────────────────────────────────────────┐
      │  01 绪论与痛点   ▸   02 总体路线   ▸  [★ 03 创新点一：低秩表征]  ▸   04 创新点二   ▸   05 创新点三   ▸   06 总结与成果 │
0.32" └──────────────────────────────────────────────────────────────────────────────┘
```
- **Inactive Pills**: Fill `#F8FAFC`, text `#64748B` (`9.5pt Bold`), border `none`.
- **Completed Pills**: Fill `#F1F5F9`, text `#334155` with subtle `✓` prefix.
- **Active Chapter Pill (`★`)**: Solid University VI / Theme `primary` fill (e.g., `#0F2042` Navy or `#5C068C` Tsinghua Purple or `#8C1515` Cardinal), white bold text `#FFFFFF` (`10pt Bold`), `roundRect` radius `0.04"`.

##### 2. Full-Canvas Master Technical Roadmap & Chapter Opener Spotlight Dimming
- **Master Roadmap Slide (`Slide 6`, `hero_1col`)**: Construct a 4-tier native DrawingML diagram showing **explicit inter-chapter causal dependency arrows**:
  - `Tier 1 (问题与机理层)`: Overarching domain challenge decomposed into 3 coupled sub-bottlenecks (`静态失配` / `动态漂移` / `端侧算力受限`).
  - `Tier 2 (核心创新章节层)`:
    - **第3章（创新点一）** solves Sub-Bottleneck 1 $\xrightarrow{\text{输出紧凑特征表示 } \mathbf{Z} \text{，暴露动态演化失稳问题}}$ **第4章（创新点二）** solves Sub-Bottleneck 2 $\xrightarrow{\text{联合第3/4章模型，面临高并发低时延部署约束}}$ **第5章（创新点三）** completes end-to-end hardware-aware system optimization.
  - `Tier 3 (实证与系统验证层)`: Public benchmarks + Self-built dataset + Real-world prototype deployment.
  - `Tier 4 (成果支撑映射栏)`: Inline tags (`[CVPR'25 一作]`, `[TPAMI'26 一作]`, `[授权发明专利×2]`) anchored directly beneath Chapters 3, 4, and 5!
- **Chapter Transition Opener (`第3章/第4章/第5章 过渡页`)**: Never use an empty colored divider slide that just says *"第三章：基于XX的方法"*. Instead, **re-render the Master Technical Roadmap**, dimming inactive chapters to `30% opacity` (`#E2E8F0` muted outline) while highlighting the **Active Chapter in `100%` crisp contrast** alongside a right-side `35%` card stating:
  - `承接上章输入 (Input from Ch. k-1)`
  - `本章核心突破 (Core Breakthrough of Ch. k)`
  - `向下章输出接口 (Output Handoff to Ch. k+1)`

---

#### C. Architectural Signature 2: `各创新点闭环章节` (6-Slide Closed-Loop Innovation Micro-Spine)

Every core innovation chapter in a PhD/Master defense must execute this **self-contained 6-slide closed loop** (`~6–8 minutes` per chapter for PhD; compress `S2+S3` and `S4+S5` into **4–5 slides** per chapter for Master):

1. **Slide `C.1` — Chapter Spotlight & Sub-Problem Anchor (`split_65_35`)**:
   - Dimmed Master Roadmap spotlighting `Chapter k` + specific sub-bottleneck left unresolved by prior art (or by `Chapter k-1`).
2. **Slide `C.2` — Core Theoretical Insight & Native OMML Formulation (`split_equal_2col`)**:
   - Left: Geometric/intuitive contrast (`传统建模失真 vs. 本文机理建模`). Right: Unified-notation native OMML objective / Theorem box ($\le 2$ equations, color-coded terms).
3. **Slide `C.3` — Proposed Algorithmic / System Architecture (`hero_1col` or `split_65_35`)**:
   - High-DPI vector pipeline diagram with `✦ 本章核心创新模块` badge, tensor dimensions, and 3-step algorithmic walkthrough.
4. **Slide `C.4` — Primary Quantitative Benchmarks (`asymmetric_2row`)**:
   - Focal SOTA comparison table ($\le 7$ rows, bold SOTA, `$\Delta$` gain column, $p$-value / std dev) + 2 empirical takeaway cards.
5. **Slide `C.5` — Diagnostic Ablation, Complexity & Visual Case Study (`split_equal_2col` or `quadrant_2x2`)**:
   - Left: Module ablation waterfall + hyperparameter sensitivity curve. Right: Qualitative visual comparison (`Baseline Failure vs. Ours`) + compute/latency overhead check.
6. **Slide `C.6` — Chapter Closed-Loop Summary Strip (`split_65_35`, `本章小结与递进引线`)**:
   - **65% Card (`第k章小结 — 闭环验证`)**: 3 quantified bullets answering `针对什么子问题 → 提出什么新方法 → 取得什么硬指标突破（支撑成果：[Venue'YY]）`.
   - **35% Card (`🔗 章节递进引线 → 引出第k+1章`)**: Explicitly states what new boundary arises once `Chapter k` succeeds, seamlessly launching `Chapter k+1`!

---

#### D. Architectural Signature 3: `成果矩阵` (Chapter-Mapped Academic Output Matrix)

Committee members flip between your thesis achievement sheet and your slides to verify graduation eligibility (`学位授予标准`). Design a dedicated `hero_1col` **Chapter-Mapped Output Matrix** (`攻博/攻硕期间科研成果与章节支撑矩阵`):

| 成果类别 | 代表性学术成果完整规范引用（高亮本人位次与通讯关系） | 期刊/会议级别 | 状态标识 | 量化影响力 / 应用佐证 | 支撑论文章节 |
|:---|:---|:---|:---|:---|:---|
| **代表作 1** | **[本人姓名 (1st)]**, Advisor*. *"Title..."*, **CVPR 2025 (Oral, Top 3.3%)** | **CCF-A 顶会** | `[✓ 已发表]` | Google Scholar 他引 48 次；GitHub **1.4k Stars** | **第 3 章** |
| **代表作 2** | **[本人姓名 (1st)]**, Co-author, Advisor*. *"Title..."*, **IEEE TPAMI 2026** | **中科院 SCI 一区 Top (IF: 20.8)** | `[✓ 已录用 / Early Access]` | 刷新 4 项公开基准 SOTA | **第 4 章** |
| **代表作 3** | Advisor, **[本人姓名 (导师一作·本人二作)]**. *"Title..."*, **NeurIPS 2025** | **CCF-A 顶会** | `[✓ 已发表]` | 获领域综述论文正面专节评述 | **第 5 章** |
| **在审工作** | **[本人姓名 (1st)]**, Advisor*. *"Title..."*, 投递 **ICML 2026** | **CCF-A 在投** | `[⏳ Under Review (Rebuttal阶段)]` | *注：不计入最低毕业硬指标，作为体系延伸* | **第 5 章延伸** |
| **知识产权/转化** | 国家发明专利：《一种面向XX的低时延推理方法及系统》（ZL20241XXXX.X） | **已授权发明专利 ×2 / 软著 ×1** | `[✓ 已授权]` | 在 **[合作企业/医院]** 原型验证稳定运行 6 个月 | **第 5 章系统** |

> **Academic Integrity Guardrail**: **NEVER blur `在审 (Submitted / Under Review)` with `已录用 (Accepted)`**! Explicitly badging status in distinct pills (`#DCFCE7` emerald for Published/Accepted; `#FEF3C7` amber for Revision/Under Review) wins massive trust from senior examiners. Also separate **"学位论文直接支撑成果"** (top table) from **"攻读学位期间参与的其他合作成果"** (compact bottom footnote bar).

---

#### E. Architectural Signature 4: `Q&A Backup Slides` (答辩委员会高频追问预备页工程)

##### 1. Two-Step Closing Choreography (`致谢` $\rightarrow$ `Q&A 总控留屏页`)
- **Slide `N-1` (`致谢 / Acknowledgements`, spoken for `10–15 seconds`)**: Sincere, structured 4-tier gratitude (`导师悉心指导` $\to$ `答辩委员会与盲审评阅专家宝贵意见` $\to$ `课题组同门与合作单位支持` $\to$ `家人默默付出`), ending with **`恳请各位专家批评指正！`** and a respectful bow.
- **Slide `N` (`Q&A 核心结论留屏与预备页导航台` — Projected Throughout All 20–30 Minutes of Q&A!)**: Immediately advance 1 click after bowing so examiners stare at:
  - **Left `70%`**: Miniaturized **Master Technical Roadmap + 3 Chapters' Headline Metrics + 3 Future Directions**.
  - **Right `30%` (`🔍 专家提问快速索引 / Backup Index`)**: 6 clean clickable DrawingML action buttons (`action: hyperlink to Slide B1..B6`) so when an examiner asks *"第4章定理2的Lipschitz常数假设在真实数据上成立吗？"*, one click jumps straight to `Backup B1`!
  - **Return Button on Every Backup Slide (`B1–B12`)**: Place a persistent button `[↩ 返回总结总览]` at `(X = 11.35", Y = 0.36", W = 1.38", H = 0.30")` hyperlinked back to `Slide N`.

##### 2. The 6 Mandatory Defense Backup Slide Categories (`B1–B6`)
- **`B1` — Full Mathematical Proofs & Regularity Verification**: Complete proof steps omitted from main slides + empirical plot verifying assumptions (e.g., singular value decay / Lipschitz constant histogram on real datasets).
- **`B2` — Blind-Review (`盲审评阅意见`) Point-by-Point Revision Matrix**: *Crucial in Chinese defenses!* A 2-column table (`外审专家核心意见摘要` vs. `学位论文修改位置(第X页第Y节)与补充实验结果`) — committees almost always ask *"盲审专家提了什么问题，你怎么改的？"*!
- **`B3` — Uncropped Master Tables & Statistical Significance**: Full 20-baseline tables, multi-seed error bars, and cross-dataset generalization breakdowns.
- **`B4` — Training/Inference Cost, Hardware Specs & Hyperparameter Sensitivity**: Exact GPU hours, peak VRAM, wall-clock latency breakdown, and full grid-search surfaces.
- **`B5` — Honest Failure Cases & Theoretical Boundary Conditions**: Concrete visual examples where the method degrades (e.g., extreme >80% occlusion) + mechanistic root cause + mitigation path.
- **`B6` — Engineering Deployment, Dataset Curation Ethics & Reproducibility**: Data cleaning pipeline, human-subject IRB / desensitization compliance, hardware testbed photos.

---

#### F. Complete 38-Slide PhD Dissertation Defense Master Spine *(with 24-Slide Master Compression Notes)*

| Slide Range | Time (35m PhD) | Breadcrumb Section | Slide-by-Slide Structural Assignment | Master (`18m / 24 Slides`) Compression |
|:---|:---|:---|:---|:---|
| **1** | `00:00–00:30` | *(Cover)* | Official University VI Cover: Dissertation Title, Candidate, Advisor, Specialty, Date | Keep (1 slide) |
| **2** | `00:30–01:00` | *(Outline)* | 5-Part Structural Directory (`01 绪论 · 02 总体路线 · 03-05 核心创新章节 · 06 总结与成果`) | Keep (1 slide) |
| **3–5** | `01:00–04:00` | `01 绪论与痛点` | **S3**: National/Scientific Urgency & Application Pain Point; **S4**: Paradigm Gap Matrix (`文献综述矩阵`); **S5**: Core Scientific Problems (`2–3个科学问题`) | Compress into **2 slides** (`背景痛点` + `现状矩阵与研究目标`) |
| **6** | `04:00–05:30` | `02 总体技术路线` | **S6**: **Full-Canvas Master Technical Roadmap (`总体技术路线图`)** with Ch. 3 $\to$ 4 $\to$ 5 causal coupling & mapped papers | Keep (1 slide — Chapters 3 & 4 coupling) |
| **7–13** | `05:30–12:30` | `03 创新点一 (第3章)` | **S7**: Roadmap Spotlight Opener; **S8**: Sub-problem & Intuition; **S9**: Native OMML Model; **S10**: Architecture Diagram; **S11**: SOTA Benchmark Table; **S12**: Ablation + Case Visuals; **S13**: `本章小结 + 引出第4章` | **5 slides** (`过渡痛点` + `模型与架构` + `主实验` + `消融可视化` + `小结`) |
| **14–20** | `12:30–19:30` | `04 创新点二 (第4章)` | **S14**: Roadmap Spotlight Opener (`承接第3章`); **S15**: Dynamic/Theoretical Bottleneck; **S16**: Theorem/Formulation; **S17**: Mechanism Pipeline; **S18**: Primary Results; **S19**: Pareto/Sensitivity; **S20**: `本章小结 + 引出第5章` | **5 slides** (Second core innovation chapter) |
| **21–27** | `19:30–26:30` | `05 创新点三 (第5章)` | **S21**: Roadmap Spotlight Opener (`承接第3-4章`); **S22**: System/Scale Challenge; **S23**: Co-Design Architecture; **S24**: End-to-End Benchmarks; **S25**: Real-World Testbed / Deployment; **S26**: Ablations; **S27**: `本章小结` | **5 slides** (System integration / application verification chapter; optional if 2-chapter MS) |
| **28–33** | `26:30–31:30` | *(Optional Ch. 6)* | *(If 4-innovation PhD: 6-slide closed loop for Chapter 6; otherwise allocate extra 1–2 deep-dive theory/demo slides to Chapters 3–5)* | Omit in MS |
| **34–35** | `31:30–33:15` | `06 总结与展望` | **S34**: **Thesis Conclusion Synthesis** (`3–4条核心创新点闭环对照科学问题`); **S35**: Honest Limitations & 3 Concrete Future Research Extensions | **2 slides** (`全文工作总结` + `不足与未来展望`) |
| **36** | `33:15–34:15` | `06 攻博科研成果` | **S36**: **Chapter-Mapped Academic Output Matrix (`成果矩阵`)** (Papers, Patents, Systems, Awards) | **1 slide** (`攻硕期间科研成果列表`) |
| **37** | `34:15–34:35` | `致谢` | **S37**: Dignified 4-tier `致谢` + `恳请各位专家批评指正` (`15s` bow) | **1 slide** (`致谢`) |
| **38** | *(Lingers in Q&A)* | `Q&A 总控导航台` | **S38**: **Master Roadmap + Key Deltas + Hyperlinked Backup Index (`[B1 理论证明] [B2 盲审修改] [B3 完整实验] [B4 算力开销] [B5 边界案例] [B6 系统细节]`)** | **1 Lingering Q&A Hub** + `5–8` Backup Slides |

---

## 4. Pillar III: Research Grants, Academic Awards & 50-Minute Faculty Job Talks

### 4.1 Grant Proposal & Concluding Defense (国自然NSFC · 国家重点研发 · 横向课题 · International Panels)

Grant presentations invert conference storytelling: conference talks prove *what you already discovered*; funding pitches prove **why an agency or enterprise should entrust scarce capital to your vision, de-risked methodology, and execution track record**.

---

#### 4.1A Competitive Talent & Fundamental Science Pitch (国自然 NSFC 优青/杰青/海外优青/青托/重点项目 & NSF CAREER / ERC / NIH / DARPA, `10–15 Min`)

##### 1. Dual Theoretical Frameworks: NSFC Reform Mandates $\leftrightarrow$ Heilmeier Catechism
Every competitive grant deck must satisfy both domestic NSFC review rubrics and the international **8-Question Heilmeier Catechism**:

| Strategic Dimension | Chinese NSFC / Talent Panel Standard (`国自然/人才会评`) | International Panel Standard (`NSF / DARPA / ERC / NIH`) |
|:---|:---|:---|
| **Identity Anchor** | **精准学术标签 (`Academic Label`, Slide 1–2)**: `[研究载体] + [核心机制] + [标志性突破]` (例：`面向高维非平稳系统的流形解耦建模与可信预测`) — 让大同行评委10秒记住你的生态位。 | **PI Research Identity & Vision Tagline**: Single jargon-free sentence defining the fundamental capability gap your career/project unlocks (*Heilmeier Q1*). |
| **Problem Framing** | **四大科学问题属性精准锚定**:<br>① `鼓励探索，突出原创` (0到1新概念)<br>② `聚焦前沿，独辟蹊径` (国际热点新路径)<br>③ `需求牵引，突破瓶颈` (卡脖子底层科学机理 — 重点/杰青高频)<br>④ `共性导向，交叉融通` (多学科方法论融合) | **Status Quo Wall & Payoff (*Heilmeier Q2, Q3, Q4*)**: Why today's best practice hits a hard physical/computational wall, what is fundamentally new in your premise, and *who cares* if you succeed (*Broader Impacts / Clinical Significance*). |
| **Track Record Proof** | **代表作故事化与独立贡献边界 (`3–4项代表作`)**: 严禁罗列论文清单；每项代表作按 **`领域痛点 → 本人原创机理 → 权威正面他引`** 展开，明确标注 **`独立通讯 / 第一作者`**，严防“把大团队平台成果算作个人功劳”。 | **Preliminary Data & De-Risking Proof**: Pilot prototypes, theoretical feasibility bounds, and prior foundational bricks proving the premise is not speculative. |
| **Future & Risk** | **延续性与深水区跃迁 (`拟开展研究`)**: 与前期成果一脉相承但绝不重复吃老本；包含清晰的技术路线与备选预案；海外优青必须专设 **`依托单位平台、算力、招生与配套经费硬支撑`** 页。 | **Specific Aims, Milestones & Risk Mitigation Matrix (*Heilmeier Q5–Q8*)**: Mandatory **Risk $\to$ Fallback Strategy** table, quantitative Year 1/3/5 "exams", and transparent budget alignment. |

##### 2. Signature Layout: `代表性成果一页解构卡` (1-Slide-Per-Breakthrough Anatomy)
When presenting `代表作一 / 二 / 三` (Slides 6–11 in NSFC Talent talks), enforce `split_65_35` with a top attribution bar:
- **Top Ribbon (`H = 0.42"`)**: `[代表性成果一]` **IEEE TPAMI 2025 / Nature Mach. Intell.** | **`本人角色：独立通讯作者`** | `支撑核心科学问题一`
- **Left `65%` Card (`科学突破闭环`)**:
  - *Top-left mini-box*: Prior bottleneck (`传统方法在XX下误差发散`).
  - *Center hero graphic*: Clean vector mechanism diagram (`✦ 本人提出XX新原理/新算子`) + headline metric comparison (`精度 +8.4%，计算复杂度由 O(N³) 降至 O(N log N)`).
- **Right `35%` Card (`独立贡献与国际学术反响`)**:
  - **`👤 个人独立贡献界定`**: *“本人独立提出核心流形解耦假说，推导收敛性上下界并主导开源框架研发。”*
  - **`🌍 权威同行正面评价`**: Verbatim highlighted excerpt from Fellow / Academician / Review article (*“Smith et al. (MIT, IEEE Fellow) 在综述中评价该工作 ‘pioneered a tractable paradigm for...’”*, ESI Top 1% 高被引，他引 `186` 次).
  - **`⚙️ 实际应用/辐射`**: Adopted by `[国家重大工程 / 开源社区 3.2k Stars / 行业龙头产线]`.

##### 3. Complete 18-Slide NSFC Talent / Key Grant & International Panel Spine (`12–15 Min`)

| Slide # | Time (12m Talk) | Section Badge | Grid Model | Assertion Headline Template (CN / EN) | Mandatory Visual & Review Evidence |
|:---|:---|:---|:---|:---|:---|
| **1** | `00:00–00:25` | `GRANT DEFENSE • 项目答辩` | `hero_1col` | `[项目名称 / 学术方向总题]` + **核心学术标签副标题** | Applicant Name, ID, Host Institution, Grant Category (`优青/杰青/海外优青/重点项目/NSF CAREER`), Date. |
| **2** | `00:25–01:10` | `1. 个人画像与学术定位` | `split_65_35` | CN: `学术定位：深耕[方向]，形成“[标签关键词]”鲜明特色`<br>EN: `PI Trajectory & Cohesive Research Identity` | **65%**: Education/Postdoc/PI timeline + **1-Line Core Identity Banner**. **35%**: Quantitative snapshot (Representative papers, independent citations, editorial/committee roles). |
| **3** | `01:10–02:00` | `2. 战略需求与立项依据` | `split_equal_2col` | CN: `面向[国家重大需求/前沿]，[卡脖子痛点]亟待底层机理突破`<br>EN: `Grand Challenge & Limits of Current Practice (Heilmeier Q1–Q2)` | **Left**: Strategic bottleneck in national industry/science. **Right**: Hard physical/computational wall blocking existing approaches. |
| **4** | `02:00–03:00` | `2. 科学问题属性与总体主线 ★` | `hero_1col` | CN: `属性锚定“[需求牵引，突破瓶颈]”：一条主线串联三大科学问题`<br>EN: `Overarching Research Spine: Past Foundations → Proposed Leap` | **Panoramic Research Architecture Map**: Shows how **Past Achievements 1–3** built the exact foundation for **Proposed Thrusts 1–3** (*proving continuity + upward leap*). |
| **5–6** | `03:00–04:40` | `3. 代表性成果一 (发现/表征)` | `split_65_35` | CN: `成果一：揭示[新机理]，突破[瓶颈1]（独立一作/通讯，[Venue]）`<br>EN: `Foundation 1: Discovering [Mechanism] to Resolve [Limit 1]` | **S5**: Mechanism diagram + core theorem/curve; **S6**: **1-Slide Breakthrough Card** (Independent role + international Fellow positive citations + impact). |
| **7–8** | `04:40–06:20` | `3. 代表性成果二 (核心方法)` | `split_65_35` | CN: `成果二：提出[原创算法/理论]，实现[指标跨越]（独立通讯）`<br>EN: `Foundation 2: Scalable [Algorithm] Achieving [K]× Gain` | **S7**: Algorithmic innovation + benchmark SOTA leap; **S8**: Independent contribution boundary + peer adoption / ESI citation highlights. |
| **9–10** | `06:20–07:45` | `3. 代表性成果三 (系统/落地)` | `split_65_35` | CN: `成果三：研制[原型系统/平台]，在[重大场景]完成实证闭环`<br>EN: `Foundation 3: Real-World Validation & Ecosystem Impact` | **S9**: Hardware/clinical/industrial deployment architecture; **S10**: Third-party application certificate (`应用证明`) / open-source ecosystem metrics. |
| **11** | `07:45–08:20` | `3. 学术影响力与独立性综述` | `grid_3col` | CN: `同行认可与学术独立性：从跟随探索到开辟独立子方向`<br>EN: `Scholarly Independence & International Standing` | 3 crisp cards: `代表作矩阵总览 (5篇精选)`、`国际同行正面评价地图`、`回国/独立建组以来独立成果占比高亮`. |
| **12** | `08:20–09:10` | `4. 拟开展研究总体方案 ★` | `hero_1col` | CN: `拟开展研究：向[深水区问题]跃迁的总体技术路线与三大课题`<br>EN: `Proposed 5-Year Research Architecture & Specific Aims 1–3` | **Vector Technical Roadmap** of Proposed Thrusts 1, 2, 3 showing novel hypotheses, interfaces, and quantitative Year 1–5 gates (*Heilmeier Q3, Q7, Q8*). |
| **13–14** | `09:10–10:30` | `4. 拟开展核心内容与预实验` | `split_equal_2col` | CN: `拟攻克难点一/二：技术路径与已取得的预实验可行性支撑`<br>EN: `Proposed Thrusts Deep Dive & De-Risking Pilot Data` | Proposed mathematical/system design paired directly with **fresh unpublished pilot curves** proving immediate traction. |
| **15** | `10:30–11:05` | `4. 潜在风险与备选预案 ★` | `hero_1col` | CN: `高风险科学探索的难点预判与双轨备选技术预案`<br>EN: `Risk Management & Contingency Matrix (Heilmeier Q5)` | **3-Row Risk Matrix Table**: `潜在技术风险点 | 触发判据 (Go/No-Go Gate) | 备选降级/替代方案 (Fallback Plan)`. |
| **16** | `11:05–11:35` | `5. 依托单位支撑与预算匹配` | `split_equal_2col` | CN: `依托单位硬核保障：国重平台、算力场地、招生指标与配套经费`<br>EN: `Institutional Environment, Team Synergy & Budget / Education Plan` | **Left**: National Key Lab facilities, committed startup funds, PhD quotas (`已落实X名博士指标/XX㎡空间`). **Right**: Budget pie/timeline (*or NSF CAREER Education Integration*). |
| **17–18** | `11:35–12:00` | `总结与全景留屏` | `split_65_35` | CN: `总结：立足原创积累，攻克[重大瓶颈] · 恳请专家批评指正`<br>EN: `Summary: Investing in [Vision] with Proven Execution Capacity` | Brief respectful bow + **1-Slide Panoramic Summary (`学术标签 + 3大代表作贡献 + 3项拟开展任务`)** lingering throughout panel Q&A! |

---

#### 4.1B National Key R&D & Major Project Acceptance / Mid-Term (国家重点研发计划 · 科技重大专项 中期检查与结题验收, `15–20 Min`)

##### 1. Evaluator Mindset: Technical Academician Panel + CPA Financial Auditors
In Ministry of Science and Technology (`科技部` / 专业机构) evaluations, creativity comes second to **100% contractual fidelity (`交总账、逐字对标《任务书》`)** and **audit-proof evidence chains (`第三方CMA/CNAS检测报告 + 无保留意见审计报告`)**.

##### 2. Mandatory Slide Template 1: `《任务书》考核指标完成情况逐项对照表`
Never paraphrase or reorder KPI wording from the signed Task Book. Render across 2–3 sequential `hero_1col` tables:

| 指标序号 | 《任务书》规定考核指标原文（逐字一致） | 任务书目标值 | 实际完成值 | 完成度判定 | 权威佐证材料与附件索引编号 |
|:---|:---|:---|:---|:---|:---|
| **指标 1.1** | 突破XX多源异构协同感知算法，核心识别准确率 | $\ge 92.0\%$ | **95.4%** | **`[✓ 超额完成]`** | 第三方CMA检测报告（附件3，第18–24页） |
| **指标 1.2** | 研制边缘端智能推理样机，单帧端到端处理时延 | $\le 25\text{ ms}$ | **16.8 ms** | **`[✓ 超额完成]`** | 中国赛宝实验室测试报告（附件4，第41页） |
| **指标 2.1** | 在不少于3个典型行业现场开展示范应用，连续无故障运行 | $\ge 1000\text{ h}$ | **4个现场 / 2400 h** | **`[✓ 超额完成]`** | 用户使用报告与经济效益证明（附件7，第88页） |
| **指标 3.1** | 发表高水平论文 $\ge 15$ 篇（标注专项编号），申请发明专利 $\ge 10$ 项 | 15篇 / 10项 | **21篇 / 授权8项·受理6项** | **`[✓ 全面达成]`** | 检索证明与第一标注核验表（附件9，第112页） |

##### 3. Mandatory Slide Template 2: `专项经费到位、执行率与财务审计合规页`
Use `split_65_35`:
- **Left `65%`**: Grouped horizontal execution bar chart + summary table (`中央财政专项资金：预算 XXX 万 / 到位 100% / 支出 XXX 万 [执行率 97.6%]`；`单位自筹配套资金：预算 XXX 万 / 落实到位 100% / 支出 XXX 万 [执行率 96.2%]`), itemized by `设备费 / 业务费 / 劳务费 / 间接经费`.
- **Right `35%` (`合规性红线核验卡`)**: Explicit bullets confirming: (1) 严格执行国务院办公厅最新科研经费“放管服”及包干/调剂备案制度；(2) 无违规外拨、无突击花钱、自筹资金真实入账；(3) 会计师事务所出具 **`标准无保留意见结题财务审计报告（文号：XX审字[2026]第XX号），账表一致`**。

##### 4. Complete 22-Slide National Key R&D Acceptance Spine (`18 Min` Target)
- **Slide 1**: Project/Sub-project Official Title, Grant Code (`项目编号 202YXXXXXX`), Lead Unit, PI, Participating Units, Date.
- **Slides 2–3 (`立项任务回顾与子课题分解`)**: Task Book overall objective + **课题—子任务—承担单位协同矩阵图** showing how sub-tasks integrate into the flagship system *(not isolated unit silos!)*.
- **Slides 4–7 (`核心考核指标逐项对照总表 ★`)**: Complete verbatim `《任务书》` KPI completion tables (Technical KPIs, Prototypes, Demonstrations, IP/Papers, Talent Training) — **100% coverage, zero omitted clauses**.
- **Slides 8–15 (`代表性关键技术突破与标志性成果 1–3`)**: 2–3 slides per major innovation (`攻克难点 → 创新架构 → 权威对比曲线 → 实物样机高清照片与测试证书截屏角标`).
- **Slides 16–17 (`集成示范应用与经济社会效益`)**: Field deployment photos, architecture in real national infrastructure, quantified economic/social benefit table backed by stamped user certificates (`盖章应用证明`).
- **Slide 18 (`知识产权、标准制定与人才培养矩阵`)**: Strictly filtered to outputs **within the execution period and carrying 1st/valid grant acknowledgment (`第一标注合规核验`)**.
- **Slides 19–20 (`经费到位、预算执行与财务审计合规 ★`)**: Fiscal execution table + CPA audit verdict + asset/data archiving (`科技报告与汇交凭证编号`).
- **Slide 21 (`组织协同管理机制与后续推广计划`)**: Consortium joint-debugging milestones & industrialization roadmap.
- **Slide 22 (`验收总结留屏页`)**: **KPI 100% Completion Summary Badge + 3 Flagship Deliverables + Supporting Evidence Volume Index (`附件册第1–6卷速查导航`)** for instant panel verification!

---

#### 4.1C Industry / Horizontal Project Pitch & Delivery (企业横向课题立项投标与结题验收汇报, `10–15 Min`)

##### 1. The Dual-Metric ROI Translation Rule (`算法指标 ⇄ 业务价值映射`)
Corporate executives and chief engineers tune out pure academic metrics (`F1 = 0.91`, `CRPS = 0.042`). Every technical slide in a horizontal project deck must display a **Dual-Metric Translation Strip**:
- **Kickoff / Bid Pitch (`立项汇报`)**: `业务痛点 (如：零售仓储大促期爆仓与滞销并存 / 电网峰谷负荷预测偏差) → 数学建模定义 → 轻量化可落地技术架构 (兼容企业现有CPU/国产信创/私有云环境) → 保底合同KPI与里程碑交付物`.
- **Final Acceptance (`结题汇报`)**: `合同技术条款逐条达标核验 → 离线回测 + 线上灰度A/B实测收益 (算法RMSE降低16.4% ➔ 业务端缺货率下降4.1%、年化节约成本XX万元) → 工程交付物移交清单`.

##### 2. Complete 12-Slide Horizontal Grant Spine *(Dual-Mode: Bid vs. Acceptance)*
1. **Slide 1**: Project Title, Client Name & University Lab, Contract ID, PI, Date.
2. **Slide 2 (`业务痛点与目标对齐`)**: Client production bottleneck $\to$ Quantified contract KPIs (`合同约定核心技术指标`).
3. **Slide 3 (`端到端系统集成架构`)**: How our algorithm/module plugs cleanly into the client's existing data warehouse / ERP / edge hardware (`蓝色框：企业既有底座` vs. `金色框：本课题交付核心引擎`).
4. **Slides 4–6 (`核心算法与工程攻关 1–2`)**: Domain-tailored innovation (handling dirty real-world enterprise data, cold-start, interpretability, and strict latency/VRAM budgets — maximum 1 clean OMML equation!).
5. **Slides 7–8 (`实证效果 / 线上A/B灰度验证 ★`)**: *Bid*: Pilot PoC benchmark on client sample data; *Acceptance*: **Contract KPI Target vs. Actual Production Score Table** + Online shadow/A/B curve across peak business cycles.
6. **Slide 9 (`典型业务Bad-Case闭环与可解释性`)**: Real operational case walkthrough showing *why* the model made a decision and how edge cases are safely guarded by fallback rules.
7. **Slide 10 (`交付物清单与知识产权归属 ★`)**: Clean checklist table (`容器化推理源码与SDK | 接口与运维文档 | 模型权重与训练流水线 | 联名专利/软著 ×N | 现场技术培训 ×N场`).
8. **Slide 11 (`项目进度里程碑 / 后续二期升级路线`)**: Gantt milestones (*Bid*) or Phase-II scale-up roadmap (*Acceptance*).
9. **Slide 12 (`总结留屏页`)**: **Contract 100% Fulfillment Scorecard + Business ROI Headline + Handover Sign-Off Readiness**.

---

### 4.2 Academic Award & Scholarship Pitch (研究生国奖 · 校长奖学金 · 优博优硕答辩, `3–5 Min`)

#### A. Evaluator Psychology: Beating 40-Candidate Jury Fatigue in 30 Seconds
Scholarship and Outstanding Thesis (`国奖/特奖/优博优硕`) panels comprise **10–15 professors from across the entire school/university** sitting through 30–50 rapid pitches in half a day.
- **Fatal Mistake**: Spending 90 seconds on generic self-introduction (`思想端正、热爱祖国、团结同学、选修了XX课`) and then dumping an unstructured laundry list of 8 disconnected papers/competitions (`报菜名式拼盘`).
- **Winning Formula**: **Slide 1 Instant Quantitative Portrait (`30s`)** $\to$ **One Coherent Research Storyline (`围绕一个硬问题做深做透`)** $\to$ **Quantified Independent Impact & Peer Recognition**.

#### B. Signature Slide 1 Recipe: `一页立体个人画像仪表盘` (Personal Academic Portrait Hero Card)
Design Slide 2 (or Slide 1 combined cover-portrait in a `3-min` sprint) using asymmetric modular cards (`Y: 1.65"–6.85"`):
- **Left Column (`X = 0.60", W = 3.60", H = 5.20"`) — Identity & Hard Numbers Card**:
  - Crisp academic portrait photo + Name / Grade / Advisor + **1-Line Research Tag** (`聚焦大模型高效推理系统`).
  - **4 High-Contrast Metric Tiles (`22pt Bold` numbers + `11pt` labels)**:
    - `GPA 3.96 / 排名 1/72 (Top 1.4%)`
    - `CCF-A / SCI 一区一作 × 4 篇`
    - `Google Scholar 引用 240+ (ESI高被引 ×1)`
    - `授权发明专利 × 2 / GitHub 2.6k ★`
- **Right Zone (`X = 4.45", W = 8.28", H = 5.20"`) — Coherent Research Spine & Top Honors**:
  - **Top Half (`H = 3.10"`)**: **3-Stage Research Storyline Flow (`发现瓶颈 [NeurIPS'25 一作] → 理论突破 [ICML'26 Oral] → 系统落地 [华为昇腾算子合入]`)** proving systematic depth rather than paper-farming!
  - **Bottom Half (`H = 1.85"`)**: Structured highlight strip of top national competitions (`挑战杯/互联网+国赛金奖`) and community service (Area/Journal Reviewer, Open-Source Maintainer).

#### C. Attribution Calibration (`不卑不亢的贡献界定`)
Integrate `paper-boundaries` strengths-first clarity with academic humility:
- ❌ **Arrogant / Overclaiming**: *“我颠覆了传统注意力架构，带领实验室拿下了重点项目。”* *(Triggers instant backlash from professors!)*
- ❌ **Self-Effacing / Vague**: *“参与了实验室的几篇论文实验工作。”* *(Sounds like a helper, not a 国奖 leader!)*
- ✅ **Calibrated Gold Standard**: *“在导师XX教授指导下，本人作为**第一作者**独立完成核心低秩算子理论推导、CUDA内核实现与全部主实验验证，相关代码已合入主流开源框架。”*

#### D. Complete Dual Spines: `3-Min Express (5 Slides)` vs. `5-Min Standard / 优博答辩 (9 Slides)`

| 3-Min 国奖极速版 (5 Slides, `02:45`) | 5-Min 校级终审 / 优博优硕版 (9 Slides, `04:40`) | Layout & Mandatory Visual Content |
|:---|:---|:---|
| **S1 (`00:00–00:35`)**: **封面 + 一页立体个人画像仪表盘** | **S1 (`00:00–00:20`)**: 庄重学术封面（题目 + 个人一句话学术标签）<br>**S2 (`00:20–00:55`)**: **一页立体个人画像与学业硬指标仪表盘** | Hero Portrait Dashboard (exact recipe above; zero prose paragraphs). |
| **S2 (`00:35–01:15`)**: **科研主线与代表作一（核心理论/方法突破）** | **S3 (`00:55–01:35`)**: **科研主线全景图**（围绕1个核心科学问题的三阶递进闭环）<br>**S4 (`01:35–02:20`)**: **代表性突破一**（痛点 $\to$ 原创方法图 $\to$ Oral/一区指标跃升） | High-DPI architecture + bold metric delta badge + `[本人一作 · Oral Top 2%]` pill. |
| **S3 (`01:15–01:55`)**: **代表作二与系统/产业落地实效** | **S5 (`02:20–03:05`)**: **代表性突破二**（承接突破一的深层拓展与SOTA对比）<br>**S6 (`03:05–03:45`)**: **代表性突破三 / 成果转化与开源影响力** | Benchmark chart + GitHub stars / industry application proof / peer review praise quote (`审稿人评价 "Strong Accept"`). |
| **S4 (`01:55–02:25`)**: **完整科研成果矩阵与科创竞赛亮点** | **S7 (`03:45–04:15`)**: **参评周期内完整学术成果矩阵**（严格标注评选年度有效成果！）<br>**S8 (`04:15–04:30`)**: **学术服务、学科竞赛与团队传帮带贡献** | Clean table separating `参评学年新增成果 (高亮)` vs. `历史累计成果` (respecting strict高校国奖学年清零规则!). |
| **S5 (`02:25–02:45`)**: **未来规划、感恩致谢与个人画像留屏** | **S9 (`04:30–04:45`)**: **未来学术规划与致谢留屏页**（保留核心成果摘要供评委打分参考） | 3-point future goal + sincere thanks to advisor/school + **Compact Achievement Scorecard** lingering on screen! |

---

### 4.3 50-Minute Faculty Job Talk (海内外高校教职应聘学术报告, `45–50 Min` + Q&A)

A tenure-track Faculty Job Talk (MIT, Stanford, CMU, UC Berkeley, ETH, Oxbridge, 清华/北大/华五/C9准聘教职应聘报告) is the highest-difficulty presentation in academia because **every faculty member in the room gets a vote, yet 80% of them work outside your subfield**.

#### A. The Hourglass / Audience-Cone Comprehension Law
Structure the 46-minute speaking arc as a deliberate **Comprehension Hourglass**:

```
Comprehension by Full Department (Theory + Systems + AI + HCI + Bio/EE Faculty)
100% ──▶ [00–12 min: Act I — Grand Vision, Status Quo Fallacy & Unified Portfolio Map]
  │         ╲
 80%         ╲──▶ [12–26 min: Act II-A — Flagship Deep Dive 1 (Intuition → Hard Rigor → SOTA)]
  │                │  (100% Specialist Authority + 80% Generalist Accessibility via Visual Scaffolding)
 85%              [26–34 min: Act II-B — Complementary Pillar 2 + Real-World Ecosystem Impact]
  │         ╱
100% ──▶ [34–46 min: Act III — 3-Yr & 10-Yr Fundable Lab Vision + Dept Bridges, Teaching & Funding]
```
- **The Fatal Trap**: Stitching three NeurIPS/OSDI conference talks end-to-end (`"First I'll present Paper A, then Paper B, then Paper C"`). That signals **"productive senior grad student," NOT "visionary future colleague who will define a field and win tenure."**

#### B. Section-by-Section Operational Rules
1. **Act I — Defining Your Subfield (`00:00–12:00`, Slides 1–9)**:
   - Open with a **10-Year Grand Computing/Scientific Challenge** that makes a Systems professor, a Theory professor, and an HCI/Bio professor all lean forward.
   - Expose the **Status Quo Fallacy** (the hidden assumption all existing approaches share).
   - Present your **Unified Research Thesis & 2D Portfolio Map** (`Slide 8`): Plot your entire PhD/Postdoc body of work along two conceptual axes (e.g., *Algorithmic Expressivity* vs. *Hardware-Guaranteed Safety*), showing 6–8 published papers organized into **3 coherent pillars**, then announce: *"Today I will dive deeply into Pillar 1 and Pillar 2, which form the launchpad for my future lab."*
2. **Act II — Proving World-Class Depth & Intellectual Ownership (`12:00–34:00`, Slides 10–30)**:
   - **Flagship Deep Dive 1 (`12:00–26:00`, 12–14 slides)**: Choose your single most technically profound, *personally driven* breakthrough. Walk from **Toy Visual Intuition $\to$ Formal Mathematical/Systems Abstraction (native OMML / clean hardware diagram) $\to$ Hard Algorithmic Resolution $\to$ Empirical & Real-System Proof**. Explicitly surface *why the problem was non-trivial* and *what failed along the way*—senior faculty judge how you think under friction.
   - **Complementary Pillar 2 (`26:00–32:00`, 5–6 slides)**: A brisker second technical arc demonstrating you are not a one-trick pony (e.g., if Dive 1 was theoretical/algorithmic, Dive 2 demonstrates real-systems scaling or cross-disciplinary deployment).
   - **Ecosystem & Mentorship Vignette (`32:00–34:00`, 1–2 slides)**: Open-source adoption, industry/clinical deployment, and **undergraduate/junior PhD co-authors you mentored** (subtle proof you can already advise students!).
3. **Act III — The Independent PI Vision, Department Fit & Teaching (`34:00–46:00`, Slides 31–42)**:
   - **Never rush Future Work in 90 seconds!** Dedicate a full **10–12 minutes** (`25%` of the talk) to your future lab:
     - **Horizon 1 (`Years 1–3`, De-Risked & Grant-Ready)**: 2 concrete PhD-dissertation-sized thrusts ready for **NSF CAREER / DARPA Young Faculty Award / ERC Starting / NSFC 海外优青·青基** proposals on Day 1.
     - **Horizon 2 (`Years 5–10`, Tenure-Defining Moonshot)**: Bold paradigm shift answering *"What chapter of the 2035 textbook will be named after your lab?"*
   - **Tactful Collaboration & Teaching Slide (`Slide 40`)**:
     - Map your research thrusts to **3–4 complementary domains/centers in the host department** (keep it authentic and structural—never name-drop 15 professors superficially).
     - Name **2 specific existing undergraduate/core courses** you are excited to teach (using the host department's actual course level/style, e.g., *Foundations of Machine Learning*, *Operating Systems*) + **1 brand-new graduate seminar** in your specialty.
     - Name concrete target funding programs (`NSF IIS/CNS CAREER, NIH R01, DARPA, Industry Consortia`).

#### C. Handling Mid-Talk Faculty Interruptions & Chinese University Variant
- **Mid-Talk Interruption Protocol**: In US/EU CS departments, faculty interrupt on Slide 5. Design slides with **clean modular visual anchors** so you can answer a 45-second question concisely, bridge back (*"And that exact tension is what motivates Stage 2 on the next slide"*), and keep **slides 27–29 (secondary ablations)** modularly skippable if interactive Q&A consumes 5 minutes mid-talk—**never speak past Minute 48**.
- **Chinese University Faculty Recruitment Variant (`高校准聘/长聘教职应聘学术报告`, `15–25 Min` Talk)**: Domestic search committees (`学术委员会/人才引进评审会`) typically allot `15–20 min` academic talk + `5–10 min` Q&A (sometimes paired with a `10-min` course teaching demo `试讲`). Compress Act II into **3 Representative Works (`代表作一/二/三` highlighting independent 1st/corresponding authorship + JCR/CCF tier)** and expand Act III's **学科建设契合度、平台依托需求（启动经费/博导指标/算力空间）与本研课程承担计划**.

#### D. Complete 42-Slide Faculty Job Talk Master Spine (`46 Min` Speaking Target)

| Slide Range | Time Window | Hourglass Zone | Structural Role & Assertion Headline Strategy | Visual & Content Specification |
|:---|:---|:---|:---|:---|
| **1** | `00:00–00:45` | `Act I (100%)` | **Visionary Title Slide**: `[Field-Defining Noun Phrase]: [Action Subtitle]` | Candidate Name, Affiliation, Clean Visual Motif of Research Agenda. |
| **2–4** | `00:45–04:30` | `Act I (100%)` | **The Grand Challenge**: Why `[Computing / Science Domain]` stands at an inflection point | High-impact real-world stakes, scaling curves, cross-disciplinary hook appealing to the whole department. |
| **5–6** | `04:30–07:30` | `Act I (100%)` | **The Status Quo Fallacy**: Why existing paradigms hit a fundamental wall | Conceptual contrast diagram exposing the shared blindspot across prior approaches. |
| **7–8** | `07:30–11:00` | `Act I (100%)` | **My Core Research Thesis & Portfolio Map ★** | **2D Research Space Map** organizing your 6–10 papers into **3 Coherent Pillars** + highlighting mentored student co-authors. |
| **9** | `11:00–12:00` | `Act I → II` | **Talk Roadmap**: Pillar I (Deep Dive) $\to$ Pillar II (Breadth) $\to$ 10-Year Lab Vision | Visual 3-stop architectural signpost (repeated at transitions). |
| **10–12** | `12:00–15:30` | `Act II-A (90%)` | **Pillar I Setup & Core Intuition**: Concrete failure + 2D toy walkthrough | Visual before/after toy example before introducing formalisms. |
| **13–17** | `15:30–21:30` | `Act II-A (80%)` | **Pillar I Technical Core**: Formal abstraction, theorem/system architecture | Native OMML key theorem/objective + layered system diagram (`✦ Novel Contribution` highlighted). |
| **18–21** | `21:30–25:30` | `Act II-A (90%)` | **Pillar I Empirical & Diagnostic Proof**: SOTA leaps, ablations, Pareto frontier | Cropped focal benchmark table + diagnostic waterfall + scaling curve. |
| **22** | `25:30–26:15` | `Act II-A Close` | **Pillar I Synthesis & New Question Unlocked**: Bridge to Pillar II | Summary strip + causal arrow launching Pillar II (`"Solving X revealed bottleneck Y..."`). |
| **23–28** | `26:15–32:00` | `Act II-B (85%)` | **Pillar II Complementary Breakthrough**: Problem $\to$ Key Idea $\to$ System/Empirical Win | Brisker 6-slide closed loop proving methodological versatility & scale. |
| **29–30** | `32:00–34:00` | `Act II Impact` | **Real-World Deployment, Open-Source Ecosystem & Mentorship** | Production adoption (industry/clinical/standards), GitHub stars/downloads, photo/badges of mentored students. |
| **31–32** | `34:00–36:30` | `Act III (100%)` | **Future Lab Vision Overview**: From `[Current Regime]` to `[Next-Decade Paradigm]` | **5-to-10-Year Lab Blueprint Diagram** connecting Past Pillars to Future Thrusts A, B, C. |
| **33–36** | `36:30–40:30` | `Act III (100%)` | **Horizon 1 (`Years 1–3`)**: Two concrete, grant-ready PhD student thrusts | Preliminary pilot plot + crisp formulation + clear first-PhD-thesis scope. |
| **37–38** | `40:30–42:30` | `Act III (100%)` | **Horizon 2 (`Years 5–10`)**: High-risk, high-reward moonshot agenda | Bold cross-disciplinary frontier defining your long-term scholarly identity. |
| **39–40** | `42:30–44:45` | `Act III Fit` | **Synergy with `[Host Dept]`, Teaching Portfolio & Funding Strategy ★** | **3-Column Card**: `Collaborative Bridges in Dept/Campus` | `Undergrad Core + New Grad Seminar` | `Target Grants (NSF/NIH/DARPA/NSFC)`. |
| **41** | `44:45–45:15` | `Acknowledgements` | **Collaborators, Mentors, Students & Funding Agencies** | Structured photo grid highlighting PhD/Postdoc mentors, student mentees & grant logos. |
| **42** | `45:15–46:00` *(Lingers in Q&A)* | `Synthesis Landing` | **Summary Ecosystem Slide**: Past Pillars $\to$ Future Lab Vision $\to$ Key Takeaways | **Full Research Vision Panorama** kept projected for the entire 15-minute faculty Q&A (+ `10–15` hyperlinked Backup Slides `B1–B12`). |

---

## 5. High-Stakes Vision-in-the-Loop QA Rubric & Anti-Pattern Surgery Catalog

### 5.1 High-Stakes Multimodal Inspection Checklist (`view_file` at 150+ DPI)

In addition to the 5 baseline `cs-report-ppt` visual checks, every deck generated from this playbook must pass **8 scenario-specific visual gates** during Stage 4 (`view_file` pixel inspection):

| # | High-Stakes Inspection Gate | What the Agent's Eyes Must Verify in Rendered PNGs | Pass Threshold |
|:---|:---|:---|:---|
| **1** | **Auditorium Distance Legibility** | Zoom slide preview to `50%` scale (simulating row 15 of a conference hall). Check axis ticks, architecture node labels, and table cells. | Body/table font $\ge 14\text{pt}$ ($\ge 16\text{pt}$ on Teasers/Spotlights); zero unreadable `7pt` matplotlib tick labels. |
| **2** | **Assertion Headline Integrity** | Read every top headline (`Y = 0.60"`). Check for generic topic nouns (`Results`, `实验分析`) or awkward 2-line wraps colliding with subtitles. | **100% declarative claim headlines**; single-line fit (`22–28pt`) with $\ge 0.12''$ vertical clearance above subtitle. |
| **3** | **Breadcrumb & Tracker Monotonicity** | Scan top navigation bars (`Y: 0.00"–0.32"`) across all Thesis Defense / Grant slides. | Active pill (`★`) highlights the exact current chapter, never overlaps the header badge, and progresses monotonically. |
| **4** | **Focal Table Contrast & Cropping** | Inspect benchmark, Plan-vs-Actual, and `《任务书》` KPI tables. | $\le 7$ rows on screen; `Ours` / `实际完成值` row distinctly shaded; best metrics bolded; explicit `$\Delta$` or `[✓ 超额完成]` badge visible. |
| **5** | **Native OMML & Unified Notation** | Inspect mathematical blocks across multi-chapter decks (especially PhD Defense & Job Talk). | Crisp vector Cambria Math OMML; zero raw `\mathcal` strings; identical symbol definitions across Chapters 3, 4, and 5. |
| **6** | **Attribution & Status Honesty Badges** | Inspect `成果矩阵`, NSFC `代表作`, and `国奖` slides. | Distinct visual pills separating `本人一作 / 独立通讯` vs. `合作作者`, and `已发表 / 已录用` vs. `Under Review`. |
| **7** | **Final Lingering Slide Value** | Inspect the final main slide (`Slide N`) before the Backup divider. | **Zero blank "Thank You / 感谢聆听" canvas**; $\ge 75\%$ of final slide displays core takeaways, roadmap, QR codes, or Backup navigation buttons. |
| **8** | **QR Code & Hyperlink Quiet Zones** | Inspect Poster Teaser/Spotlight QR codes and Defense `[↩ 返回总览]` backup buttons. | Square `1:1` aspect ratio (never stretched!), $\ge 0.20''$ pure white quiet border around QR codes, zero collision with card borders. |

---

### 5.2 Twelve High-Stakes Anti-Patterns & Concrete Surgical Rewrites

| # | Scenario | ❌ Fatal High-Stakes Anti-Pattern | ✅ Agent-Executable Surgical Fix |
|:---|:---|:---|:---|
| **1** | **Conference Oral** | Spending `7 minutes` on background & related work (`15` cited papers), then rushing through own method & tables in `90 seconds`. | Enforce the **30/50/20 Pacing Law**: reach your **Core Insight ("Aha!" Slide 4)** by `02:30` and **System Overview (Slide 5)** by `03:30`. |
| **2** | **Spotlight (3m)** | Shrinking all 14 Oral slides and speaking at `220 wpm` like an auctioneer until cut off by the session chair. | Execute **5-Slide Spotlight Surgery**: delete Outline & Related Work, keep **1 bottleneck visual + 1 core mechanism diagram + 1 hero 4-bar chart + Poster Board CTA**. |
| **3** | **Poster Teaser (1m)** | Explaining mathematical notation for 45 seconds before showing what the system actually produces. | Apply the **Inverted Paper Arc**: show the jaw-dropping **visual/empirical result at Second 15**, then give a 1-sentence intuition and Poster `#ID`. |
| **4** | **Thesis Proposal (`开题`)** | Listing engineering chores (`搭建数据集、编写前端界面、调参对比`) under **`拟解决的关键科学问题`**. | Rewrite into **2–3 Mechanistic Bottlenecks** (`针对XX场景下因[矛盾]导致的[失真]，揭示[规律]，建立[理论/模型边界]`); keep engineering modules strictly under `研究内容`. |
| **5** | **Literature Review** | Chronological laundry list (`2021年张三提出A；2022年李四提出B；2023年王五提出C...`). | Replace with a **5-Column Paradigm × Limitation Matrix** ending with an accent-highlighted `✦ 本文切入点` row showing joint satisfaction of all criteria. |
| **6** | **Mid-Term (`中期`)** | Effort-diary narration (`阅读文献60篇，熟悉了服务器环境，正在跑实验`) with zero quantitative tables. | Open Slide 3 with the **Plan-vs-Actual Completion Scorecard (`开题计划对照完成度矩阵`)**, backed by hard benchmark curves and diagnosed adjustment plans. |
| **7** | **PhD Defense (`博答`)** | **Three Stitched Papers Syndrome (`三篇小论文机械拼凑`)**: Chapters 3, 4, 5 use conflicting math notation ($\mathbf{x}_i$ vs. $s_t$) and lack inter-chapter logic. | Unify notation globally; insert **Persistent Top Breadcrumb Bar (`Y: 0.00"–0.32"`)**, **Master Roadmap Causal Arrows**, and **`本章小结 → 引出下章` handoff cards**. |
| **8** | **Output Matrix (`成果页`)** | Mixing `Under Review / 在投` manuscripts unmarked alongside published CCF-A papers, or obscuring advisor-first authorship. | Use explicit status pills (`[✓ 已发表]` vs. `[⏳ 在审]`), bold exact author rank (`本人一作` / `导师一作·本人二作`), and map every item to `支撑第X章`. |
| **9** | **NSFC Talent (`优青/杰青`)** | Claiming group-wide mega-grant achievements as personal credit (`我们团队研制了...`) without isolating independent PI contributions. | Use the **1-Slide-Per-Representative-Work Card** with an explicit **`👤 本人独立贡献界定` (`独立通讯/原创假说提出者`)** box and verbatim international Fellow citations. |
| **10** | **Key R&D Acceptance (`重点研发验收`)** | Paraphrasing Task Book KPIs or writing vague claims (`性能达到国际先进水平`) without report indices. | Quote **`《任务书》` KPI text verbatim** in a 6-column scorecard and bind every number to a **stamped CMA/CNAS report or user certificate page index**. |
| **11** | **Scholarship (`国奖`)** | Generic prose self-praise (`思想积极向上...`) + ungrouped list of 10 minor certificates (`报菜名`). | Open with the **Slide 1 Quantitative Portrait Hero Dashboard** (`GPA/Rank + Top Tier Badges + 3-Stage Coherent Research Storyline`), strictly filtering to eligible academic-year outputs. |
| **12** | **50-Min Job Talk** | Diving into hyper-specialized notation at Minute 3 (losing 80% of voting faculty) and cramming Future Work into 1 rushed slide at Minute 47. | Follow the **Hourglass Comprehension Curve**: `12 min` department-wide framing + Portfolio Map $\to$ `22 min` scaffolded technical depth $\to$ **`12 min` 3-yr/10-yr Lab Vision, Teaching & Dept Fit**. |
