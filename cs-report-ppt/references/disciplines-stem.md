# STEM Discipline-Specific Presentation Visual Grammar (`disciplines-stem.md`)

> **Module Role**: STEM discipline-specific visual grammar and operational playbook (`CS, AI/ML, Systems, Security, Math, Statistics, Optimization, TCS, Physics, EE, Semiconductors/Hardware, Control, Robotics`) for [`cs-report-ppt`](../SKILL.md). Works alongside [`architecture_diagrams.md`](architecture_diagrams.md), [`omml_syntax_guide.md`](omml_syntax_guide.md), [`marginal_annotations.md`](marginal_annotations.md), and [`palettes-and-layouts.md`](palettes-and-layouts.md).

Academic presentations across STEM share a demand for quantitative precision, yet **what counts as decisive visual proof differs fundamentally by discipline**. Showing a raw 30-line LaTeX proof in Theoretical CS causes immediate audience cognitive shutdown; showing an unpruned 18-column benchmark screenshot in AI/ML obscures the breakthrough; pasting an unannotated Cadence schematic or cluttered lab bench photo in EE/Physics buries the physical mechanism.

This specification defines **agent-executable visual grammar, slide-by-slide spine adaptations, coordinate layout rules, table/formula/diagram construction standards, bilingual (EN/CN) headline templates, density budgets, and anti-pattern surgeries** across three core STEM clusters:

1. **`STEM-CS` — Computer Science, AI/ML, Computer Systems & Cybersecurity**
2. **`STEM-MATH` — Mathematics, Statistics, Optimization & Theoretical CS**
3. **`STEM-PHYS-ENG` — Physics, Electrical Engineering, Semiconductors/Hardware, Control & Robotics**

---

## 0. STEM Routing Dispatcher & Core Engine Integration Invariants

### 0.1 Sub-Discipline Profile Dispatcher

Before generating slide IR or layout code, classify the source paper/topic into one of the three STEM profiles below:

| Profile ID | Target Sub-Disciplines | Representative Venues | Visual Coverage Floor | Primary Visual Proof Artifacts | Default Palette Recommendation |
|:---|:---|:---|:---|:---|:---|
| **`STEM-CS`** | AI/ML, CV, NLP, Data Mining, OS/Distributed Systems, Databases, Networking, Security & Privacy | NeurIPS, ICML, ICLR, CVPR, ACL, KDD, OSDI, SOSP, NSDI, SIGMOD, IEEE S&P, USENIX Security, CCS | **$\ge 80\%$** ($\ge 11/14$ slides) | Pipeline architecture diagrams, tensor shape callouts, pruned SOTA/ablation tables, Pareto curves, Roofline/CDF plots, threat model TCB maps, qualitative + failure grids | `academic_mono` (default) or `cvpr_clean_blue` / `oxford_navy` |
| **`STEM-MATH`** | Pure & Applied Math, Mathematical Statistics, Convex/Non-Convex Optimization, Theoretical CS, Information Theory | STOC, FOCS, SODA, COLT, ITCS, ISIT, *Annals of Statistics*, *JASA*, *JRSSB*, *Math. Programming*, *SIOPT* | **$\ge 70\%$** ($\ge 10/14$ slides: geometric plots, DAGs, structured OMML theorem/rate cards) | 2D geometric toy examples, color-coded OMML equations with spatial pills, de-cluttered Hero Theorem boxes, Proof Dependency DAGs, rate/tightness tables, statistical-computational phase diagrams | `academic_mono` or `oxford_navy` |
| **`STEM-PHYS-ENG`** | Solid-State Circuits, Computer Architecture, EDA, Control Theory, Robotics & Embodied AI, Experimental/Applied Physics, Optics | ISSCC, VLSI, JSSC, ISCA, MICRO, DAC, IEEE CDC, ACC, *Automatica*, ICRA, RSS, CoRL, APS March Meeting, *PRL*, *Nature Physics* | **$\ge 85\%$** ($\ge 12/14$ slides) | Signal-flow block diagrams, paired die micrograph + floorplan callouts, FoM tables, cleaned oscilloscope waveforms, stacked Bode/Lyapunov plots, physics error-bar fits, real-robot filmstrips + latency budgets | `academic_mono`, `mit_crimson_neutral`, or `nature_slate_teal` |

### 0.2 Universal Core Engine Invariants (Inherited from `SKILL.md`)

Every STEM profile strictly obeys four architectural invariants of `cs-report-ppt`:

1. **16:9 Coordinate Grid Discipline ($13.333'' \times 7.500''$)**:
   - **Header Zone**: $X = 0.600'', Y = 0.350'' \rightarrow 1.550'', W = 12.133'', H = 1.200''$ (Tracker badge `10pt Bold Caps`, Claim Title `24–28pt Bold`, Takeaway Subtitle `14–16pt`, `0.01"` divider rule at $Y = 1.500''$).
   - **Content Zone**: $X = 0.600'', Y = 1.650'' \rightarrow 6.850'', W = 12.133'', H = 5.200''$, partitioned via deterministic layouts (`hero_1col`, `split_equal_2col`, `split_65_35`, `grid_3col`, `grid_4col`, `quadrant_2x2`, `asymmetric_2row`).
   - **Footer Zone**: $X = 0.600'', Y = 7.000'' \rightarrow 7.350'', W = 12.133'', H = 0.350''$.
2. **300+ DPI Asset Harvesting & Aspect-Ratio Locking**:
   - Crop authentic figures/micrographs/plots from source PDFs at $\ge 300\text{ DPI}$ via PyMuPDF (`scripts/crop_figures.py`). Never stretch or squash images; compute uniform scale factor $s = \min((W_{\text{card}} - 2P_x)/W_{\text{orig}}, (H_{\text{card}} - 2P_y)/H_{\text{orig}})$ and center inside the target zone.
3. **Native Vector OMML Math (`<a14:m><m:oMath>`)**:
   - All inline symbols ($\mathbf{x}_t \in \mathbb{R}^{B \times L \times D}$, $\mathcal{O}(1/\sqrt{T})$, $\omega_{\text{BW}}$) and display equations must be injected as native OpenXML math via `scripts/latex_to_omml.py` (`{{MATH:...}}` / `{{MATH_DISPLAY:...}}`) or native PowerPoint equation nodes. **Never paste low-DPI raster screenshots of equations from PDFs, and never leak raw LaTeX strings (`\frac`, `\mathbb`, `$$`) onto rendered slides.**
4. **Cross-STEM Adaptation of Marginal Research Synergy Callouts ("旁注")**:
   - When generating lab seminar or journal-club decks (`split_65_35`: Main Card $W = 7.700''$, Side-Note Card $X = 8.600'', W = 4.133''$), map the 5 baseline synergy classes to discipline-native terminology:

| Baseline Synergy Class | `STEM-CS` (AI / Systems / Security) | `STEM-MATH` (Math / Stats / Opt / TCS) | `STEM-PHYS-ENG` (Physics / EE / Control / Robotics) |
|:---|:---|:---|:---|
| **`[State Memory Inertia]`** | KV-cache compression, recurrent state decay, LSM-tree compaction state | Markov mixing time, martingale filtration memory, momentum history $\beta_t$ | Capacitor charge retention, thermal hysteresis, actuator/observer state lag |
| **`[Model Adaptivity]`** | OOD robustness, test-time compute, workload skew / adversarial drift resilience | Distribution-free / Huber contamination bounds, non-stationary regret | PVT (Process-Voltage-Temperature) variation tolerance, adaptive disturbance rejection, sim-to-real transfer |
| **`[Mechanistic Interpretability]`** | Attention head routing, SAE circuit probing, kernel flame-graph bottleneck root cause | Geometric tight-example construction, dual variable / KKT shadow-price meaning | Physical field coupling, parasitic pole/zero origin, phase-margin erosion mechanism |
| **`[Computational & Hardware Efficiency]`** | FLOPs, VRAM footprint, FP8/INT4 kernels, tail p99 latency, TCB size | Oracle complexity ($\nabla f$ calls), SDP vs first-order runtime, sample complexity $n$ | Walden/Schreier FoM, mW power/mm² area, onboard Orin/MCU control-loop latency budget |
| **`[Own Lab Synergy]`** | Repo baseline drop-in, benchmark suite port, cluster deployment | Proof technique transfer to open lab conjectures, tighter bound plug-in | PCB/FPGA/tape-out block reuse, testbed calibration upgrade, real-robot controller integration |

---

## 1. Cluster 1: Computer Science, AI/ML, Systems & Security (`STEM-CS`)

### 1.1 Sub-Discipline 14-Slide Spine Adaptation Matrix

While AI/ML, Systems, and Security share the 14-slide session backbone, **Slides 2, 6, 7, 8, 10, 11, and 12** swap domain-specific visual proof artifacts:

| Slide # | Category Badge | AI / ML / CV / NLP Focus | Systems / DB / Networking (OSDI/SOSP) | Security & Privacy (USENIX/S&P/CCS) | Recommended Grid |
|:---|:---|:---|:---|:---|:---|
| **1** | `PAPER OVERVIEW` | Title + Teaser Quality/Speed Dilemma Fig + Metadata | Title + Throughput/Latency Breakthrough Fig + Artifact URL | Title + Attack Impact / Defense Overhead Fig + CVE/Artifact | `split_equal_2col` / `hero_1col` |
| **2** | `MOTIVATION` | Qualitative Failure of Prior SOTA (hallucination, blur, OOM) | Production Trace Bottleneck (CPU stall, I/O amplification, tail spike) | Real-World Vulnerability / Exploit Demo & Why Prior Defenses Fail | `split_65_35` |
| **3** | `LANDSCAPE` | Methodological Taxonomy Tree (Dense vs Sparse vs SSM) | Design Space Trade-off Matrix (Consistency vs Latency vs Cost) | Defense Design Space (Hardware TEE vs Crypto vs Static Analysis) | `grid_3col` / `split_65_35` |
| **4** | `CORE OBJECTIVE` | Central Scaling/Generalization Hypothesis vs 3 Bottlenecks | Core Systems Insight (e.g., decoupling control/data planes) | Security Goal: Closing Attack Surface X at $<5\%$ Overhead | `split_equal_2col` |
| **5** | `LINEAGE` | Architectural Evolution Timeline (`2017 → 2023 → Ours`) | Systems Lineage (POSIX/RDMA/eBPF/CXL generation shift) | Attack-Defense Arms Race Timeline (`Exploit A → Patch B → Bypass C`) | `split_65_35` |
| **6** | `FOUNDATIONS` | **Input Modalities & Tensor Spaces** ($\mathbf{X} \in \mathbb{R}^{B \times L \times D}$) | **System Model, Workload Characteristics & Hardware Invariants** | **Threat Model, TCB Boundary & Explicit In/Out-of-Scope Table** | `split_equal_2col` |
| **7** | `FORMULATION` | **Native OMML Master Loss**, Regularizers & Tensor Lifecycle | **Invariants, Consistency/Scheduling Model & Complexity Bounds** | **Formal Security Game / Cryptographic Reduction / Policy Invariant** | `asymmetric_2row` / `split_equal_2col` |
| **8** | `ARCHITECTURE` | **End-to-End Pipeline Diagram** (Frozen vs Novel + Tensor Shapes) | **Control/Data Plane & Kernel/User/NIC Architecture Diagram** | **Defense Architecture + Attack-Mitigation Sequence Ladder** | `split_65_35` / `hero_1col` |
| **9** | `PROTOCOL` | Datasets, Strong Baselines, GPU Cluster & Precision Specs | Testbed Hardware, Standard Benchmarks (YCSB/TPC-C) & Real Traces | Evaluation Targets, Exploit Corpus, Fuzzing/Benchmark Budget | `grid_3col` |
| **10** | `PRIMARY RESULTS` | **Pruned SOTA Benchmark Table** (Bold/Underline/$\Delta$ Pills) | **End-to-End Throughput (ops/s) & Tail Latency (p99) Plots** | **Detection/Prevention Efficacy Table** (FPR, FNR, Exploit Block %) | `asymmetric_2row` |
| **11** | `TRADE-OFFS` | **Pareto Latency–VRAM–Accuracy Curve** + Ideal Corner Arrow | **Roofline Plot / Concurrency Scaling / Resource Breakdown** | **Runtime & Memory Overhead Breakdown** vs Baseline Execution | `split_65_35` |
| **12** | `ABLATIONS` | **Progressive Component Ladder Table** + Hyperparameter Sensitivity | **Micro-Benchmarks** (isolating RPC, cache, lock, or I/O path) | **Adaptive Adversary Stress-Test** & Parameter Sensitivity | `quadrant_2x2` / `split_equal_2col` |
| **13** | `CRITIQUE` | Claimed Gains vs Hidden Pretraining Cost / OOD Ceiling | Claimed Speedup vs Hardware Lock-in / Operational Complexity | Security Guarantees vs Residual Side-Channels / TCB Bloat | `split_equal_2col` |
| **14** | `LAB ROADMAP` | 3 Seminar Prompts + 3-Week PyTorch Reproduction Plan | 3 Systems Questions + Cluster Prototype Milestone Plan | 3 Security Questions + Audit/Integration Milestone Plan | `split_65_35` |

### 1.2 Assertion-Evidence Headline Templates (Bilingual EN & CN)

Ban vague topic nouns (`"Architecture"`, `"Experiments"`, `"Ablation Study"`). Every `STEM-CS` slide title (`24–26pt Bold`, single line $\le 80\text{ EN chars}$ or $\le 32\text{ CN chars}$) must state a falsifiable mechanism or quantitative verdict:

- **Architecture / Pipeline (`Slide 8`)**:
  - *EN*: `Decoupled Latent KV Projection Cuts Cache Memory by 73% Without RoPE Drift`
  - *CN*: `解耦潜在 KV 投影在保持旋转位置编码精度的同时削减 73% 显存占用`
- **Systems Design (`Slide 8`)**:
  - *EN*: `Bypassing Kernel TCP via User-Space eBPF Eliminates 68% Serialization Overhead`
  - *CN*: `基于用户态 eBPF 旁路内核协议栈消除 68% 序列化开销`
- **Security Threat Model (`Slide 6`)**:
  - *EN*: `Threat Model Isolates Untrusted Host OS While Minimizing Enclave TCB to 4.2 KLoC`
  - *CN*: `威胁模型隔离非受信宿主机操作系统并将可信计算基压缩至 4.2 KLoC`
- **Primary SOTA Benchmark (`Slide 10`)**:
  - *EN*: `Outperforms Strongest Prior SOTA by +4.8% on MMLU at 1.9× Higher Token Throughput`
  - *CN*: `MMLU 准确率超越最优基线 +4.8%，端到端吞吐率提升 1.9 倍`
- **Progressive Ablation (`Slide 12`)**:
  - *EN*: `Adaptive Gate Contributes +2.9% Gain; Removing Spectral Loss Degrades OOD by 5.1%`
  - *CN*: `自适应门控贡献 +2.9% 核心增益，移除频域损失导致分布外性能下降 5.1%`

### 1.3 Architecture Pipeline Dissection & Tensor Shape Callout Grammar

#### A. Clean Left-to-Right Pipeline & Novelty Highlighting
1. **Strict Directional Flow**: Primary tensor or packet execution flows **Left $\rightarrow$ Right** (`Input` at $X \approx 0.85''$ $\rightarrow$ `Backbone / Processing` $\rightarrow$ `Output / Loss` at $X \approx 11.80''$). Residual skip-connections route cleanly above (`arc/elbow` top corridor) and gradient/feedback paths route below (`dashed` bottom corridor) — **never cross solid data arrows at arbitrary diagonal angles**.
2. **Three-Tier Visual Component Taxonomy**:
   - **Frozen / Pretrained / Standard Modules**: Cool neutral slate (`#F1F5F9` fill, `#94A3B8` `1.25pt` border, `#334155` text) with top-left micro-tag `❄️ FROZEN` or `◼ STANDARD`.
   - **Proposed / Novel Modules (Maximum 1–2 Accent Colors)**: Warm amber (`#FEF3C7` fill, `#D97706` `2.2pt` border, `#92400E` bold text) in color themes, or crisp high-contrast double-frame (`#F9FAFB` fill, `#111827` `2.2pt` solid border + `✦ NOVEL` black pill badge) in `academic_mono`.
   - **Objective / Loss / Terminal Sink**: Native `oval` or pill container (`#FEE2E2` fill, `#DC2626` `1.5pt` border) labeled with OMML symbol ($\mathcal{L}_{\text{CE}} + \lambda \mathcal{L}_{\text{align}}$).

#### B. Tensor Shape Callouts & Progressive Tensor Lifecycle Builds
Unlabeled boxes turn an ML architecture slide into hand-waving; raw PyTorch autograd graphs turn it into spaghetti. Enforce two complementary standards:

1. **Floating Tensor Dimension Pills on Connectors**:
   - Place a compact `roundRect` pill ($H = 0.24''$, `#FFFFFF` fill, `0.75pt` `#CBD5E1` border, `10.5pt` OMML or monospace) **0.06" above** critical inter-module arrows.
   - **Semantic Variable Persistence**: Keep dimension letters consistent across every slide in the deck:
     - Vision: $\mathbb{R}^{B \times C \times H \times W}$ (e.g., `[B, 256, H/8, W/8]`)
     - Sequence / LLM: $\mathbb{R}^{B \times L \times D}$ or multi-head $\mathbb{R}^{B \times H_q \times L \times d_h}$
     - Graph / Point Cloud: $\mathbf{X} \in \mathbb{R}^{N \times d}, \mathbf{A} \in \{0,1\}^{N \times N}$
   - Only annotate transitions where **dimensionality, rank, or sparsity changes** (e.g., downsampling, latent bottleneck $D \rightarrow d_c \ll D$, attention matrix $L \times L$ vs linear state $d_h \times d_v$). Omit redundant shape tags when $B \times L \times D$ passes unchanged through standard residual layers.

2. **Kayvon Fatahalian Progressive Tensor Lifecycle Table** (For Dense Novel Operators on Slide 7 or 8):
   When a paper's core contribution is a tensor reorganization (e.g., FlashAttention tiling, Multi-Head Latent Attention, Ring Attention, State-Space scan), pair the diagram with a 4-row lifecycle table:

```
┌────────────────────────┬───────────────────┬──────────────────────────────┬───────────────────┬────────────────────┐
│ Stage / Operator       │ Input Shape       │ Active Math Transformation   │ Output Shape      │ SRAM / VRAM Impact │
├────────────────────────┼───────────────────┼──────────────────────────────┼───────────────────┼────────────────────┤
│ 1. Token Embedding     │ [B, L, D]         │ h_t = Embed(x_t)             │ [B, L, D]         │ Baseline O(BLD)    │
│ 2. Latent Down-Proj ✦  │ [B, L, D]         │ c_t^{KV} = W^{DKV} h_t       │ [B, L, d_c]       │ Cache ↓ 9.1×       │
│ 3. Decoupled RoPE   ✦  │ [B, L, d_c]       │ k_t^R = RoPE(W^{KR} h_t)     │ [B, L, d_r]       │ +d_r << H·d_h      │
│ 4. Attention Up-Proj   │ [B, L, d_c + d_r] │ Absorb W^{UK} into W^Q       │ [B, H, L, d_h]    │ Compute-fused      │
└────────────────────────┴───────────────────┴──────────────────────────────┴───────────────────┴────────────────────┘
```

#### C. Systems Swimlanes & Security Threat-Model / TCB Diagrams
- **Systems Architecture (`OSDI/SOSP`)**: Partition the primary card horizontally or vertically into explicit privilege/hardware domains separated by `1.25pt` dashed lines (`#64748B`):
  - **Control Plane** (top, muted `#F8FAFC`, dashed `1.2pt` slow-path configuration arrows) vs **Data Plane** (bottom, crisp `#FFFFFF`, bold `2.5pt` `#1D4ED8` / `#111827` fast-path zero-copy arrows).
  - Explicitly mark crossing costs at boundary lines (`"PCIe Gen5 x16: 64 GB/s"`, `"Zero-Copy Shared Ring"`, `"Avoided Syscall + Copy"`).
- **Security Threat Model & TCB Map (`USENIX/S&P/CCS`, Mandatory on Slide 6)**:
  - Left Card (`w = 5.916"`): **System Trust Boundary Diagram** — render **Trusted Computing Base (`[TCB]`)** inside a solid double-bordered emerald/slate shield box (`#ECFDF5` fill, `#059669` `2.0pt` border, annotated with exact TCB size e.g. `TCB: Hardware CPU + 3.8 KLoC Monitor`) and **Untrusted Adversary Domain** (Host OS, Hypervisor, Network, Malicious Tenant) in soft rose/gray (`#FEF2F2`, dashed `#DC2626` border) with lightning-bolt arrows (`⚡ Compromised Syscall Interface`, `⚡ DMA Replay`) pointing at defended interfaces.
  - Right Card (`w = 5.916"`): **Explicit In-Scope vs Out-of-Scope Matrix** — prevents reviewer ambushes during Q&A:
    - `✔ IN-SCOPE ADVERSARY`: Root OS compromise, page-table tampering, network packet injection, cold-boot DRAM snooping.
    - `✖ OUT-OF-SCOPE (EXPLICIT)`: Physical silicon decapping, denial-of-service (DoS) availability attacks, speculative execution side-channels inside enclave code.

### 1.4 SOTA Benchmark Tables: Ruthless Pruning & Visual Hierarchy

**Hard Rule**: Never paste a raw screenshot of a 25-row $\times$ 12-column paper table where font size drops below `10pt`. Reconstruct primary benchmarks as native PowerPoint/HTML-to-PPTX vector tables (or crop only a clean $\le 8$-row subset at 300+ DPI if typography renders $\ge 11.5\text{pt}$ equivalent).

#### Quantitative Table Formatting Specification (`Slide 10`, `asymmetric_2row` Top Card $W=12.133'', H=2.60''\text{–}3.10''$):
1. **Dimensional Ceiling**: **5 to 8 rows maximum** $\times$ **5 to 7 columns maximum**:
   - Row 1: Foundational/Classic Baseline (e.g., `Llama-3-8B` or `ResNet-50` or `RocksDB`)
   - Rows 2–5: Strongest 3–4 recent/concurrent SOTA competitors (grouped by paradigm or parameter scale)
   - Bottom Row: **`Ours [Method Name]`** shaded across the entire row (`#F3F4F6` in `academic_mono`, `#EFF6FF` in navy/blue themes) with a `1.5pt` top separator rule.
2. **Directional Metric Headers**: Every metric column header **must** include unit + explicit direction arrow:
   - `MMLU (%) ↑` | `GSM8K (%) ↑` | `FID ↓` | `p99 Lat (ms) ↓` | `Peak VRAM (GB) ↓`
3. **Three-Level Winner Encoding**:
   - **Best (1st Place)**: **Bold `700`** in primary/accent ink (`#000000` or `#1E40AF`).
   - **Second Best (Runner-Up)**: <u>Underlined</u> regular `400` weight (`#334155`).
   - **Quantified Gain Column (`Δ vs. Prior SOTA`)**: Dedicated rightmost column displaying explicit absolute or relative gains in bold (`+4.8%`, `-38.2%`, `2.14×`), so the audience never performs mental subtraction live!
4. **Booktabs Border Discipline**: Zero vertical gridlines (`borderLeft: none, borderRight: none`). Use only three clean horizontal rules: `1.5pt` top header rule, `1.0pt` mid-header rule, `1.5pt` bottom rule, plus `0.5pt` subtle `#E2E8F0` group dividers. Right-align or decimal-align all numeric columns; left-align method names.
5. **Mandatory Table Caption Strip (`10pt`, `#64748B`)**:
   - `Bold: best; Underlined: second best. Mean ± std over 5 seeds on 8× H100 (BF16). Δ computed against strongest published baseline.`

### 1.5 Progressive Ablation Tables & Waterfall Decomposition (`Slide 12`)

Dense grids of 24 checkmarks ($\checkmark / \times / \checkmark / \checkmark$) force the audience to play Sudoku across columns. Transform paper ablations into a **Progressive Cumulative Ladder** (`split_65_35` or `quadrant_2x2`):

| Variant ID | Architectural Configuration | ImageNet Top-1 (%) ↑ | Throughput (img/s) ↑ | Incremental $\Delta$ |
|:---|:---|---:|---:|---:|
| **(0) Baseline** | Standard ViT-B/16 Backbone | `81.8` | `1,420` | `—` |
| **(1) + Latent Gate** | Add rank-64 state compression gate | `83.1` | `1,890` | **`+1.3%` / `1.33×`** |
| **(2) + RoPE Decouple** | Separate positional & semantic heads | `84.4` | `1,860` | **`+1.3%`** |
| **(3) Full Model (Ours)** | + Spectral alignment auxiliary loss $\mathcal{L}_{\text{spec}}$ | **`85.2`** | **`1,860`** | **`+0.8%` (`+3.4%` net)** |

- **Training-Time Zero-Cost Note**: Notice how Row (2) $\rightarrow$ Row (3) keeps inference throughput identical (`1,860 img/s`) because $\mathcal{L}_{\text{spec}}$ is training-only — call this out explicitly with a side arrow (`"Training-only loss: +0.8% acc at 0 ms inference cost"`).
- **Leave-One-Out (`w/o`) Alternative**: When components cannot be stacked sequentially, present `Full Model` at the top row followed by `w/o Module A (-2.9%)`, `w/o Module B (-1.7%)`, paired on the right with horizontal red degradation bars.

### 1.6 Pareto Latency–VRAM Curves & Systems Performance Trio (`Slide 11`)

1. **Pareto Trade-Off Curves (AI/ML & Systems)**:
   - **Explicit Ideal-Corner Banner**: Draw a bold diagonal arrow (`1.75pt`) in the optimal corner labeled **`↖ Better (Higher Accuracy, Lower Latency)`** or **`↙ Better (Lower Perplexity, Lower VRAM)`**. Never force viewers to decode inverted axes unassisted.
   - **Outlier Marker Contrast**: Plot `Ours` across scales (e.g., `Ours-Small`, `Ours-Base`, `Ours-Large`) connected by a `2.5pt` solid frontier curve with `12–14pt` filled star/diamond markers; plot all baseline families in muted slate/gray (`#94A3B8`, `7–8pt` circles/triangles, `1.2pt` dashed curves).
   - **Hardware Feasibility Threshold Lines**: Overlay vertical or horizontal dashed constraint lines (`#DC2626` or `#475569`) grounding abstract numbers in real deployment boundaries (e.g., `24 GB Single RTX 4090 Limit`, `Interactive SLA = 50 ms/token`).
2. **Systems Evaluation Visual Trio (`OSDI/SOSP/NSDI`)**:
   - **Tail-Latency CDF**: Plot Cumulative Distribution Function with compressed/log top percentiles (`0.50, 0.90, 0.99, 0.999`) highlighting horizontal gap at `p99` (`"3.8× lower p99 tail latency"`).
   - **Roofline Model Plot**: Log-log plot of `Operational Intensity (FLOPs/Byte)` vs `Attainable Compute (TFLOP/s)`, marking hardware memory-bandwidth slope + Tensor Core ceiling, showing how kernel fusion shifts the operator right/up toward the ridge point.
   - **Normalized Breakdown Stacked Bars**: Decompose end-to-end execution into 3–4 clean phases (`Serialization`, `Network RTT`, `Compute`, `Disk Sync`) comparing `Baseline` vs `Ours`.

### 1.7 Qualitative Comparison Matrices & Proactive Failure Grids (`Slide 2 & Slide 11/12`)

- **Synchronized Qualitative Matrix**:
  - Columns: `Input / Context` $\rightarrow$ `Baseline A` $\rightarrow$ `Baseline B` $\rightarrow$ **`Ours`** $\rightarrow$ `Ground Truth`.
  - **Mandatory Zoom-In Crop Callouts**: Full-frame images hide high-frequency artifacts on auditorium screens. Place a `1.5pt` crisp bounding box (`#EF4444` for baseline failure, `#10B981` or `#111827` for `Ours` recovery) with a `2.5×–4×` magnified inset strip directly beneath each column.
- **Honest Failure Mode Grid (Builds Scientific Credibility)**:
  - Include a dedicated 2-case or 3-case failure strip (`quadrant_2x2` Q4 or Slide 13 right card) showing **exact failure input + failure output + 1-line mechanistic diagnosis** (e.g., *"Fails on >4 overlapping transparent specular objects due to depth-buffer aliasing"*). Preempting limitations disarms Q&A attacks.

### 1.8 `STEM-CS` Anti-Patterns & Concrete Surgeries

| Anti-Pattern Observed | Why It Fails Live | Mandatory Agent Surgery |
|:---|:---|:---|
| Full-page LaTeX `Table 1` screenshot (`18 cols × 28 rows`, `6pt` font) | Unreadable beyond Row 2; zero visual hierarchy | Extract `1 anchor + 4 SOTA baselines + Ours` across `4–5 core metrics`; bold 1st, underline 2nd, add `Δ` column |
| Unedited PyTorch / ONNX / TensorBoard node dump | Zero distinction between standard layers and novel contribution | Redraw as 5–8 macro DrawingML blocks; tint standard blocks slate, highlight novel 1–2 blocks with `✦ NOVEL` + tensor pills |
| Checkmark matrix (`✓ / ✗`) across 9 ablation rows | Forces slow 2D cross-referencing under a 60-second slide clock | Reorder into a 4–5 row cumulative ladder (`Baseline → +A → +B → Full`) with rightmost `+Δ` column |
| Security talk omitting explicit Out-of-Scope threats | Reviewers immediately derail Q&A with side-channel or DoS hypotheticals | Add mandatory Slide 6 TCB diagram + `✔ In-Scope` vs `✖ Out-of-Scope` split table |
| Systems bar chart reporting only mean latency | Hides catastrophic p99/p99.9 stalls caused by GC, locks, or compaction | Pair mean throughput with p50/p99/p99.9 tail bars or CDF + error bars |

---

## 2. Cluster 2: Mathematics, Statistics, Optimization & Theoretical CS (`STEM-MATH`)

### 2.1 Core Expository Philosophy: The Halmos–Tao Inversion

As Paul Halmos (*"How to Talk Mathematics"*) and Terence Tao emphasize: **A talk is not a paper.** A paper progresses deductively for archival verification (`General Definitions → Technical Lemmas 1–7 → Master Theorem → 6-Page Proof → Special Cases`). Replicating that deductive order on slides guarantees losing 90% of the room by Slide 4.

`STEM-MATH` enforces the **Intuition-First Pedagogical Inversion**:
1. **Concrete Puzzle / Degenerate Toy Case ($d=2, n=4, \sigma=0$)** $\rightarrow$
2. **Color-Annotated Equation Dissection (Semantic Term Mapping)** $\rightarrow$
3. **De-Cluttered Hero Theorem Box ($\tilde{\mathcal{O}}$ Clean Form + Assumption Pills)** $\rightarrow$
4. **Proof Dependency DAG + The Single Novel Technical Gadget (Zero Raw Proof Walls)** $\rightarrow$
5. **Tightness, Lower-Bound Match & Phase Transition Geometry**.

### 2.2 `STEM-MATH` 14-Slide Spine Adaptation Matrix

| Slide # | Category Badge | Standard Slide Role (`STEM-MATH`) | Primary Visual / Mathematical Asset | Recommended Grid |
|:---|:---|:---|:---|:---|
| **1** | `PAPER OVERVIEW` | Title, Venue (STOC/COLT/AoS/SIOPT) & **1-Figure Central Phenomenon / Rate Leap** | Visual rate gap diagram (e.g., closing $O(1/\sqrt{T}) \rightarrow O(1/T^2)$ or phase boundary) | `split_equal_2col` |
| **2** | `CENTRAL QUESTION` | **Informal Problem Statement & Concrete Puzzle** | Simple visual counterexample showing why naive estimator/algorithm fails | `split_65_35` |
| **3** | `PRIOR BOUNDS` | **Landscape of Known Upper & Lower Bounds** | **Rate / Complexity Comparison Table** (`Assumptions | Prior Rate | Lower Bound | Gap`) | `hero_1col` / `asymmetric_2row` |
| **4** | `MAIN CONTRIBUTION` | **Preview of Main Result & Barrier Broken** | Timeline or number-line of exponents (e.g., Matrix Multiplication / Regret / Minimax exponent) | `split_equal_2col` |
| **5** | `TOY EXAMPLE` | **2D Geometric / Small-$n$ Toy Walkthrough (`Stage A`)** | **2D Phase/Contour/Graph Sketch** ($d=2$ or 4-vertex gadget) building exact geometric intuition | `split_65_35` |
| **6** | `MODEL & NOTATION` | **Minimal Notation Dictionary & Regularity Setup** | Persistent **Notation Reference Card** + Geometric illustration of assumptions (e.g., $\mu$-convexity vs $L$-smoothness) | `split_equal_2col` |
| **7** | `KEY FORMULATION` | **Color-Annotated Master Equation / Estimator / Algorithm (`Stage B`)** | **16–20pt Display OMML Equation** with semantic color-coding + spatial callout pills | `asymmetric_2row` |
| **8** | `MAIN THEOREM` | **Formal Hero Theorem Box (`Stage C`)** | **Structured 3-Zone Theorem Card** (Assumption pills + Clean OMML bound + Tightness verdict) | `split_65_35` |
| **9** | `PROOF ARCHITECTURE` | **Proof Dependency DAG (`Stage D` — Roadmap)** | **Vector DAG** mapping `[Assumptions] + [Classical Tools] → [Key Lemmas] → [Theorem 1]` | `hero_1col` / `split_65_35` |
| **10** | `CORE PROOF IDEA` | **Deep-Dive into the SINGLE Novel Technical Ingredient** | Geometric/probabilistic diagram of **1 magic step** (novel potential $\Phi_t$, coupling, Fano packing) | `split_equal_2col` |
| **11** | `LOWER BOUND / TIGHTNESS` | **Minimax Lower Bound / Hardness Reduction & Phase Transition** | **2D Phase Transition Regime Map** (`Impossible` vs `Hard Gap` vs `Tractable`) | `split_65_35` |
| **12** | `NUMERICAL / COROLLARY` | **Synthetic Slope Verification or Concrete Application Corollary** | Log-log empirical convergence plot confirming theoretical slope $-1/2$ or $-2$, or key special case | `split_equal_2col` |
| **13** | `SHARPNESS & LIMITS` | **Necessity of Assumptions & Counterexamples When Relaxed** | Table mapping *Dropped Assumption $A_i$* $\rightarrow$ *Explicit Counterexample / Rate Collapse* | `split_equal_2col` |
| **14** | `OPEN PROBLEMS` | **Conjectures, Barrier Extensions & Lab Synergy** | 2–3 Crisp Open Conjectures (stated with exact target rates) + Lab Proof-Technique Transfer | `split_65_35` |

### 2.3 Bilingual Assertion-Evidence Headline Templates (`STEM-MATH`)

- **Toy Example (`Slide 5`)**:
  - *EN*: `In 2D Anisotropic Quadratics, Vanilla SGD Oscillates Across Steep Valley Walls`
  - *CN*: `二维病态二次曲面上，标准随机梯度下降在峡谷陡壁间发生高频震荡`
- **Hero Theorem (`Slide 8`)**:
  - *EN*: `Theorem 1: Proximal Momentum Achieves Optimal O(1/T²) Rate Without Knowing μ`
  - *CN*: `定理 1：自适应近端动量法在未知强凸系数 μ 下达到最优 O(1/T²) 收敛率`
- **Proof DAG / Core Lemma (`Slide 9–10`)**:
  - *EN*: `Proof Hinges on an Asymmetric Lyapunov Potential Canceling Positive Drift`
  - *CN*: `证明核心在于构造非对称 Lyapunov 势函数以精确抵消随机正漂移项`
- **Phase Transition (`Slide 11`)**:
  - *EN*: `Fano Packing Reveals a Sharp k²-vs-k⁴ Statistical-Computational Gap Below SNR Threshold`
  - *CN*: `Fano 装填下界揭示信噪比阈值下方存在显著的 k² 与 k⁴ 统计-计算相变鸿沟`

### 2.4 The 4-Stage Intuition-First Theorem Presentation Pipeline

#### Stage A: 2D Geometric / Degenerate Toy Example (`Slide 5`, `split_65_35`)
Never introduce a general Hilbert space $\mathcal{H}$, measure-theoretic filtration $\{\mathcal{F}_t\}_{t \ge 0}$, or $k$-uniform hypergraph without first anchoring on a low-dimensional projection:
- **Dimensional Reduction Recipes**:
  - *Optimization*: 2D level-set contours ($x \in \mathbb{R}^2$) illustrating saddle escape, Polyak–Łojasiewicz (PL) valley geometry, or projection onto a non-convex cone.
  - *High-Dimensional Statistics*: 2D $\ell_1$ diamond vs $\ell_2$ ball intersection with the affine data subspace $y = X\beta$, showing why sparsity induces corner contact vs bias shrinkage.
  - *TCS / Graph Algorithms / Complexity*: A 4-to-6 vertex toy graph or 2-clause gadget demonstrating where greedy/LP relaxation produces a fractional integrality gap of $2 - \epsilon$.
- **Sanity-Check Anchor**: Explicitly include a 1-line **Extreme Regime Check** pill at the bottom of the card: `"Sanity Check: Set noise σ = 0 ⇒ recovers classical Nesterov O(1/T²) bound; set d = 1 ⇒ matches scalar median."`

#### Stage B: Color-Annotated Master Equation Dissection (`Slide 7`, `asymmetric_2row`)
Equations on slides must be **visually parsed, never read aloud symbol-by-symbol**.

1. **Deck-Wide Semantic Color Dictionary (Max 4 Colors)**:
   Lock variable colors across every equation, DAG node, and plot in the presentation:
   - **Primary Estimand / Target Objective**: Deep Navy/Blue (`#1D4ED8`)
   - **Approximation / Deterministic Bias Term**: Crimson (`#B91C1C`)
   - **Stochastic Variance / Martingale Noise Term**: Deep Teal (`#0F766E`)
   - **Regularization / Algorithmic Penalty / Step-Size**: Warm Amber (`#B45309`)
   - **Universal Constants / Higher-Order Remainder $o(1)$**: Muted Gray (`#64748B`)

2. **Spatial Callout Architecture (Coordinate Recipe for `hero_top` $X=0.600'', Y=1.650'', W=12.133'', H=2.600''$)**:
   Instead of nested LaTeX `\underbrace{\overbrace{...}}` (which shrinks subscript fonts to illegible `7pt`), render the master equation in clean `18pt` Display OMML centered at $Y = 2.450''$, and anchor 3–4 native DrawingML callout pills above/below via thin `0.75pt` leader lines:

```
     ┌─────────────────────────┐                  ┌─────────────────────────────┐
     │ Deterministic Bias O(h²)│                  │ Martingale Variance O(σ²h/n)│
     └────────────┬────────────┘                  └──────────────┬──────────────┘
                  │                                              │
                  ▼                                              ▼
      𝔼[‖θ̂_T − θ*‖²]  ≤   exp(−μhT)‖θ_0 − θ*‖²  +  C₁ h² L²   +   C₂ (σ² h / μ n)
                          ──────────┬──────────
                                    │
                     ┌──────────────┴──────────────┐
                     │ Geometric Initialization Decay│
                     └─────────────────────────────┘
```

- **Persistent Mini-Notation Sidebar**: Whenever specialized symbols ($\Pi_{\mathcal{K}}$, $\mathcal{W}_2(\mu, \nu)$, $d_{\text{eff}}(\lambda)$) persist across Slides 6–11, pin a compact **Notation Reminder Strip** (`x = 8.600", y = 1.650", w = 4.133", h = 1.350"`, `#F8FAFC` fill) so listeners who blink for 10 seconds never lose variable definitions.

#### Stage C: De-Cluttered Formal Hero Theorem Box (`Slide 8`, `split_65_35` or `hero_1col`)
1. **Halmos's "One Hero Theorem" Rule**: Present **at most ONE primary formal theorem box** in a 15-minute talk (at most two in a 45-minute seminar). Convert auxiliary lemmas into visual nodes inside the Slide 9 Proof DAG.
2. **Clean $\tilde{\mathcal{O}}$ / $\lesssim$ Hygiene**: Strip ugly universal constants ($c_1 = 144\sqrt{2}, \log(4d/\delta)$) out of the display box using $\lesssim$ or $\tilde{\mathcal{O}}(\cdot)$, and place exact logarithmic/constant dependencies in a `10.5pt` muted footer line inside the card (`"Here Õ(·) hides polylog(d, T, 1/δ) factors; exact constant C = 8 in Paper Theorem 3.1."`).
3. **3-Zone Hero Theorem Card Anatomy**:
   - **Zone 1 — Header Bar (`h = 0.42"`, `#0F172A` or `#111827` fill, `#FFFFFF` `13pt Bold`)**:
     `THEOREM 1 (MINIMAX-OPTIMAL CONVERGENCE RATE — MAIN RESULT)`
   - **Zone 2 — Explicit Assumption Pills (`h = 0.55"`)**:
     Render each required hypothesis as a rounded pill badge (`[A1: L-Smooth]`, `[A2: PL Condition μ]`, `[A3: Heavy-Tailed p-th Moment, p ∈ (1,2]]`). *Highlight the weakened/novel assumption in accent amber/bold!*
   - **Zone 3 — Centered Display OMML Inequality (`16–18pt`) + Plain-Language Implication Strip**:
     State the clean mathematical bound, followed immediately by a `12.5pt Bold` 1-sentence operational translation:
     `⇒ First polynomial-time estimator achieving information-theoretic O(k log(d/k) / n) rate under heavy-tailed noise.`

#### Stage D: Proof Dependency DAG & Single Magic Ingredient (`Slides 9–10`, Zero Proof Walls)
**Absolute Prohibition**: **Never place more than 3 lines of chained algebraic equalities/inequalities (`= ... ≤ ... ≤ ...`) on a single slide.** Full proofs belong strictly in the paper PDF or Q&A Appendix slides.

1. **Slide 9 — Proof Architecture as a Vector DAG**:
   Construct a left-to-right or top-to-bottom DrawingML Directed Acyclic Graph (`6–8` nodes max) showing logical implication structure:
   - **Column 1 (Inputs / Assumptions, Slate `#F1F5F9`)**: `[A1: Smoothness]` + `[A3: Clipped Gradient]` + `[Classical Tool: Freedman's Inequality]`
   - **Column 2 (Intermediate Lemmas)**:
     - `[Lemma 1: Bounded Bias Under Clipping τ]` (Standard blue/slate box)
     - **`[★ Lemma 2 (Key Novelty): Decoupled Potential Φ_t Contraction]`** (Bold `2.2pt` amber/black highlight box with `✦ CORE TRICK` badge!)
   - **Column 3 (Destination, Oval/Double-Box)**: `[Main Theorem 1: High-Probability Bound]`
   - Label directed edges with 2–3 word proof actions (`"Telescoping sum"`, `"Optimize τ = σ√n"`, `"Union bound"`).

2. **Slide 10 — Unpacking ONLY the `★ Key Novelty` Node**:
   Dedicate Slide 10 exclusively to explaining *why* Lemma 2 works:
   - Left Card (`50%`): The single key identity, potential function $\Phi_t$, dual certificate, or probabilistic coupling equation (`1–2` OMML blocks max), highlighting the exact cross-term that cancels (`− ⟨∇f(x_t), x_t − x*⟩` shaded green/slate).
   - Right Card (`50%`): Geometric vector diagram or 2-step intuition explaining why prior proofs got stuck here (`"Prior L2 analysis blows up when variance is infinite; clipping + Huber potential caps increments at τ"`).

### 2.5 Specialized Visual Artifacts for Optimization, Statistics & TCS

1. **Asymptotic Rate & Complexity Comparison Tables (`Slide 3`)**:
   Structure columns to prevent unfair apples-to-oranges comparisons:
   `Reference | Core Assumptions | Convergence / Minimax Rate | Per-Iter / Oracle Cost | Matches Lower Bound?`
   - Highlight relaxed assumptions (e.g., `Non-Convex` vs `Strongly Convex`, `No Bounded-Gradient Assumption`) just as prominently as faster rates!
2. **Statistical–Computational Phase Transition Diagrams (`Slide 11`)**:
   For high-dimensional statistics, coding theory, and average-case TCS, render a 2D parameter plane (X-axis: Sparsity / Dimension ratio $\alpha = k / n$; Y-axis: Signal-to-Noise Ratio $\text{SNR}$):
   - **Region I (Bottom/Right, Muted Gray `#E2E8F0`)**: *Information-Theoretically Impossible* ($\forall \hat{\theta}, \mathcal{R}(\hat{\theta}) \ge c$ via Fano/Le Cam).
   - **Region II (Middle Band, Hatched Amber `#FEF3C7`)**: *Statistical-Computational Gap* (MLE succeeds in $\exp(k)$ time; Low-Degree / SQ / Planted-Clique lower bounds rule out poly-time).
   - **Region III (Top/Left, Crisp White/Blue Tint)**: *Polynomial-Time Achievable* — plot prior poly-time threshold as dashed line and **`Ours` new frontier** pushing down into the gap!

### 2.6 `STEM-MATH` Anti-Patterns & Concrete Surgeries

| Anti-Pattern Observed | Why It Fails Live | Mandatory Agent Surgery |
|:---|:---|:---|
| Classic Beamer "Wall of Lemmas" (`Definition 1 → Definition 2 → Lemma 1 → Proof` on 1 slide) | Cognitive overload in `<45 seconds`; zero intuition before abstraction | Split across Slides 5–9: 2D Toy Example first $\rightarrow$ Notation Card $\rightarrow$ Single Hero Theorem $\rightarrow$ Proof DAG |
| Screenshot of 12-line `\begin{align*}` inequality chain | Audience stops listening and fails to track line 4 $\rightarrow$ line 5 | Delete intermediate algebra; show `[Goal Bound] → [★ Key Inequality Trick] → [Final Rate]` in 3 clean blocks |
| Theorem statement cluttered with $C_1 = 32 \log(8d/\delta)/\mu^2$ | Visual noise buries the asymptotic scaling in $n, d, T$ | Replace with $\tilde{\mathcal{O}}(d / (\mu^2 n))$ in main display OMML; move exact log/constant factors to `10pt` card footnote |
| Unannotated 6-term objective equation | Listeners cannot tell which term is novel vs standard textbook penalty | Apply 3-color semantic coding + DrawingML leader-line pills (`"Empirical Loss"`, `"✦ Novel Curvature Penalty"`) |
| Stating regularity assumptions (`A1–A5`) without explaining necessity | Sounds arbitrary or overly restrictive to theory reviewers | Pair assumptions on Slide 6/13 with 1-line sharpness notes (`"Without A2, lower bound degrades to Ω(1/√T)"`) |

---

## 3. Cluster 3: Physics, EE, Semiconductors/Hardware, Control & Robotics (`STEM-PHYS-ENG`)

### 3.1 Sub-Discipline 14-Slide Spine Adaptation Matrix

Hardware, physical sciences, control, and robotics audiences evaluate validity through **physical realizability, conservation/stability laws, calibrated instrumentation, silicon/bench measurements, and closed-loop real-world execution**:

| Slide # | Category Badge | IC / Semiconductors / Arch (ISSCC/VLSI/ISCA) | Control & Robotics (CDC/ICRA/RSS/CoRL) | Experimental & Applied Physics (APS/PRL/Optica) | Recommended Grid |
|:---|:---|:---|:---|:---|:---|
| **1** | `PAPER OVERVIEW` | Title + **Die Photo / Peak FoM Teaser** + Process Node Badge | Title + **Real-Robot Deployment Hero Strip** + Task Success Badge | Title + **Core Physical Phenomenon / Phase Diagram Teaser** | `split_equal_2col` / `hero_1col` |
| **2** | `MOTIVATION` | Power/Bandwidth/Area Wall in Prior Silicon Generations | Sim-to-Real Breakdown, Unmodeled Contact, or Instability Mode | Unresolved Physical Anomaly, Quantum/Optical Decoherence Bottleneck | `split_65_35` |
| **3** | `LANDSCAPE` | Prior Topology Trade-offs (SAR vs $\Delta\Sigma$, SRAM vs RRAM) | Classical Model-Based Control vs RL/VLA Trade-off Matrix | Competing Theoretical Regimes / Material Platform Comparison | `grid_3col` / `split_65_35` |
| **4** | `CORE OBJECTIVE` | Target FoM Leap (e.g., $10\times$ Energy Efficiency at 1 GS/s) | Closed-Loop Bandwidth, Stability Guarantee & Agile Task Goal | Target Measurement Sensitivity / New Quantum Phase Observation | `split_equal_2col` |
| **5** | `LINEAGE` | Silicon Node & Circuit Topology Evolution (`65nm → 28nm → N5`) | Control Stack Evolution (`PID/MPC → Domain-Rand RL → Ours`) | Experimental Precision Progression Across Prior Measurements | `split_65_35` |
| **6** | `SYSTEM MODEL` | **Signal/Power Specifications, PVT Bounds & Channel Model** | **Plant Dynamics $\dot{x}=f(x,u,d)$, Sensor/Actuator Constraints** | **Hamiltonian / Field Equations, Symmetry & Boundary Conditions** | `split_equal_2col` |
| **7** | `FORMULATION` | **Transfer Function $H(s)$, Noise/Power Budget & FoM Equation** | **Control Law, Lyapunov Candidate $V(x)$ / MPC Objective (OMML)** | **Analytical Dispersion / Scaling Law & Perturbation Prediction** | `asymmetric_2row` |
| **8** | `ARCHITECTURE` | **Clean Top-Level Block Diagram + Novel Sub-Circuit Schematic** | **Multi-Rate Control Loop Block Diagram + Latency Budget Bar** | **Cleaned Block-Level Optical / Cryogenic / RF Apparatus Schematic** | `split_65_35` / `hero_1col` |
| **9** | `TESTBED & FAB` | **Paired Die Micrograph + Floorplan** & Measurement PCB Setup | **Robot Hardware Platform, Onboard Compute & Sensor Suite** | **Dual-View Calibrated Testbed** (Schematic + Cleaned Device Crop) | `split_equal_2col` |
| **10** | `PRIMARY RESULTS` | **Measured Oscilloscope / Spectrum Plots** (SFDR, SNDR, Droop) | **Real-Robot Deployment Filmstrip** + Success Rate Benchmark Table | **Theory-vs-Experiment Master Plot** (`≥2pt` Error Bars + Residuals) | `asymmetric_2row` |
| **11** | `FREQUENCY / FOM` | **ISSCC Performance Summary & FoM Table + Walden/Schreier Plot** | **Stacked Bode Plot (GM/PM/$\omega_{\text{BW}}$) + Trajectory/Error/$u(t)$** | **Phase Diagram / Parameter Sweep** Across Temperature, Field, or Pump | `split_65_35` |
| **12** | `ROBUSTNESS` | **PVT Corner Sweep** (Voltage/Temp/Chip-to-Chip Histogram) | **External Push/Slip Disturbance Recovery & Ablation Ladder** | **Systematic Uncertainty Budget Table** & Control Null Experiments | `quadrant_2x2` |
| **13** | `CRITIQUE` | Silicon Gains vs Area Overhead / Calibration Complexity | Real-World Agility vs Compute Power / Failure Edge Regimes | Regime of Validity vs Unmodeled Higher-Order Coupling | `split_equal_2col` |
| **14** | `LAB ROADMAP` | Next Tape-Out Node / Packaging & Lab Testbench Reuse | Hardware Deployment Milestones & Sim-to-Real Pipeline Transfer | Next-Gen Detector Upgrade & Theoretical Extension Prompts | `split_65_35` |

### 3.2 Bilingual Assertion-Evidence Headline Templates (`STEM-PHYS-ENG`)

- **IC / Semiconductors (`ISSCC / VLSI`, `Slides 9–11`)**:
  - *EN*: `28nm Pipelined-SAR ADC Achieves 74.2 dB SNDR and 182.4 dB Schreier FoM at 500 MS/s`
  - *CN*: `28nm 流水线 SAR ADC 在 500 MS/s 采样率下实现 74.2 dB SNDR 与 182.4 dB FoM`
- **Control Systems (`CDC / ACC`, `Slide 11`)**:
  - *EN*: `Delay-Compensated Observer Restores 48° Phase Margin and Eliminates Actuator Saturation`
  - *CN*: `时延补偿观测器恢复 48° 相位裕度并彻底消除执行器饱和震荡`
- **Robotics (`ICRA / RSS / CoRL`, `Slides 8 & 10`)**:
  - *EN*: `28.2 ms End-to-End Policy Loop Sustains 500 Hz Torque Tracking Under 18 N Impulse Push`
  - *CN*: `28.2 ms 端到端策略闭环在 18 N 瞬态外力冲击下保持 500 Hz 力矩稳定跟踪`
- **Experimental Physics (`APS / PRL`, `Slide 10`)**:
  - *EN*: `Measured Hall Conductance Quantizes Within 0.4σ of Analytical Chern-Insulator Fit`
  - *CN*: `实测霍尔电导在 0.4σ 统计误差内与陈绝缘体解析理论曲线高度吻合`

### 3.3 Hierarchical System, Circuit & Control Block Diagrams (`Slide 8`)

**Hard Prohibition**: **Never paste raw, unedited exports from Cadence Virtuoso, Synopsys Verdi, MATLAB Simulink, Vivado RTL netlists, or Altium Designer.** Those screenshots contain `5pt` net labels, thin `0.25pt` wires, and 40+ low-level transistors/gates that turn into gray mush on projectors.

1. **Strict Signal-Flow Orientation Grammar**:
   - **Forward Signal / Reference Path**: **Left $\rightarrow$ Right** (`r(t) / Vin` at left $\rightarrow$ `Controller / Analog Frontend` $\rightarrow$ `Plant / Core` $\rightarrow$ `y(t) / Dout` at right).
   - **Power, Clock & Bias Hierarchy**: **Top $\rightarrow$ Bottom** (`VDD / Bias / Master CLK` entering top borders).
   - **Closed-Loop Feedback & Observer Path**: **Right $\rightarrow$ Bottom $\rightarrow$ Left** returning cleanly to a native circular summing junction (`⊕ / ⊖`).
   - **External Disturbances & Noise Injection**: Dashed vertical entry arrow (`d(t)` or $v_n^2$) entering between Controller and Plant (`#DC2626` or `#64748B`).

2. **Three-Domain Maximum Color Discipline**:
   Cap block fills at **3 functional domains** across the entire diagram:
   - *IC / Hardware*: **Analog / RF Front-End** (`#FEF3C7` soft amber) | **Digital / DSP Calibration** (`#E0F2FE` soft blue) | **Clock / Power Management** (`#DCFCE7` soft green) — or high-contrast hatching/stroke weights in `academic_mono`, with a `2.2pt` bold frame + `✦ PROPOSED` badge on the novel circuit block.
   - *Control / Robotics*: **Reference & High-Level Planner (30 Hz)** (`#E0F2FE`) | **✦ Proposed Low-Level Controller / Observer (500 Hz)** (`#FEF3C7`, `2.2pt` border) | **Physical Plant / Robot Dynamics** (`#F1F5F9`).

3. **1:1 Equation–Diagram Symbol Lock**:
   Every symbol drawn inside a block or summing node ($K_p, G_p(s), \hat{d}_k, \Phi_{\text{CLK}}, C_{\text{DAC}}$) **must match character-for-character** the OMML equations on Slide 7. Never label a block `"Filter"` on Slide 8 if Slide 7 calls it $F_{\text{LP}}(z)$.

### 3.4 Die Micrographs, FoM Tables & Cleaned Physics Testbed Callouts (`Slide 9 & 11`)

#### A. Paired Silicon Die Micrograph + Layout Floorplan (`ISSCC / VLSI Standard`, `split_equal_2col`)
Unannotated die photos look like abstract metallic rectangles to everyone except the chip layout engineer. Enforce the **ISSCC Paired Callout Protocol**:
1. **Side-by-Side Pairing**: Place the **High-DPI Die Micrograph** in `Card 0` ($X=0.600'', W=5.916''$) and the **Matching Color-Coded Layout Floorplan / Area Pie** (or Zoomed Core Sub-Block) in `Card 1` ($X=6.816'', W=5.916''$).
2. **Haloed Bounding Boxes & Leader Lines**:
   - Overlay `1.75pt` dashed yellow/white/amber bounding boxes directly over silicon macro regions (`SRAM 64KB`, `PLL`, `✦ Proposed Hybrid ADC Core: 0.14 mm²`).
   - Because die micrographs contain dark silicon/metal backgrounds, surround callout leader lines with a `2.5pt` white/dark halo (`#FFFFFF` outer / `#111827` inner) and anchor labels in high-contrast opaque pills (`#111827` fill with `#FFFFFF` `11pt Bold` text).
3. **Mandatory Silicon Metadata Strip & Scale Bar**:
   - Bottom-right corner of die photo: crisp white **Scale Bar** (`500 μm` or `1 mm`, `2.5pt` bar thickness).
   - Bottom metadata pill strip: `Process: TSMC 28nm HPC+ | Active Area: 0.84 mm² | Supply: 0.9 V | Power: 4.6 mW`.

#### B. ISSCC / JSSC Figure-of-Merit (FoM) Comparison Table (`Slide 11`)
Unlike AI/ML tables (where methods are rows), **solid-state circuits and hardware venues conventionally orient Parameters as Rows and Prior Papers + `[This Work]` as Columns**:

| Metric / Specification | ISSCC '23 [1] | JSSC '24 [2] | VLSI '25 [3] | **This Work** |
|:---|:---:|:---:|:---:|:---:|
| **Technology Node** | `28 nm CMOS` | `16 nm FinFET` | `28 nm CMOS` | **`28 nm CMOS`** |
| **Supply Voltage ($V_{\text{DD}}$)** | `1.0 V` | `0.85 V` | `0.9 V` | **`0.9 V`** |
| **Sampling Rate ($f_s$)** | `400 MS/s` | `500 MS/s` | `500 MS/s` | **`500 MS/s`** |
| **SNDR @ Nyquist (dB) ↑** | `68.4` | `71.1` | <u>`72.0`</u> | **`74.2 (+2.2 dB)`** |
| **Power Consumption (mW) ↓** | `8.9` | `6.4` | <u>`5.8`</u> | **`4.6 (-20.7%)`** |
| **Active Core Area ($\text{mm}^2$) ↓** | `0.31` | `0.19` | <u>`0.18`</u> | **`0.14`** |
| **Schreier $\text{FoM}_S$ (dB) ↑** | `175.9` | `179.9` | <u>`180.4`</u> | **`182.4 (+2.0 dB)`** |

- **Explicit OMML FoM Definition**: Immediately below the table, render the exact Figure of Merit formula in native OMML so reviewers can audit normalization fairness:
  $$\text{FoM}_S = \text{SNDR} + 10 \log_{10}\!\left(\frac{\text{BW}}{P}\right) \quad [\text{dB}], \qquad \text{FoM}_W = \frac{P}{2 \cdot \text{BW} \cdot 2^{\text{ENOB}}} \quad [\text{fJ/conv-step}]$$

#### C. Cleaned Experimental Physics / RF / Optical Benchtop Testbeds (`APS / Optica`, `Slide 9`)
**Ban Raw Cluttered Lab Photos**: Never drop an uncropped smartphone photo of an optical table or electronics bench filled with tangled BNC/SMA cables, aluminum foil, oscilloscopes, and room clutter.
- **Dual-View Apparatus Recipe (`split_65_35` or `split_equal_2col`)**:
  - **Left (`55–65%`) — Clean Vector Block Schematic**: Abstract the setup into functional physics stages (`Pump Laser 780 nm` $\rightarrow$ `AOM Pulse Shaper` $\rightarrow$ **`✦ Cryogenic Cavity Sample (4.2 K)`** $\rightarrow$ `Homodyne Detector`), graying out standard commercial conditioning optics so the eye locks onto the active interaction region.
  - **Right (`35–45%`) — Background-Isolated Device / Chamber Crop**: High-DPI close-up of **only** the custom vacuum cell, photonic chip, metamaterial sample, or custom PCB on a clean neutral background, annotated with numbered badges (`①`, `②`, `③`) cross-referenced directly to nodes in the left schematic, plus a physical scale bar (`10 mm` or `20 μm`).

### 3.5 Waveforms, Bode/Lyapunov Plots & Physics Error-Bar Grammar (`Slides 10–11`)

#### A. Oscilloscope & Logic Analyzer Waveform Hygiene
1. **UI Chrome Stripping & Contrast Re-Plotting**:
   - Crop away dark plastic oscilloscope bezels, softkey menus, and tiny `7pt` channel readouts from Keysight/Tektronix captures.
   - Whenever raw `.csv`/`.wfm` data is available, re-plot onto a **pure white (`#FFFFFF`) vector canvas** with subtle `#E2E8F0` gridlines, `2.0–2.5pt` trace strokes, and `14pt+` axis labels (`Time [ns]`, `V_out [V]`). If only a dark-screen bitmap exists inside the source PDF, frame it cleanly, boost contrast, and overlay crisp native PowerPoint callout pills for axis units and trigger events.
2. **Zoomed Transient Callout Insets**:
   - Highlight dynamic performance directly on the waveform using shaded vertical intervals (`#FEF3C7` at 35% opacity) and double-headed arrows: `"Load Step: 0.1 A → 2.0 A"`, `"Recovery Time: 14 ns"`, `"Undershoot: 38 mV (4.2%)"`.

#### B. Frequency-Domain Bode Plots & Lyapunov Stability Visuals (`CDC / ACC`)
1. **Vertically Stacked Bode Plots**:
   - Stack **Magnitude (dB)** on top and **Phase (deg)** directly underneath with **100% aligned horizontal log-frequency axes** ($\omega \in [10^{-1}, 10^4]\text{ rad/s}$).
   - Draw explicit `1.25pt` dashed reference lines at `0 dB` (gain crossover $\omega_{gc}$) and `-180°` (phase crossover $\omega_{pc}$), with vertical double-arrows calling out **Gain Margin ($\text{GM} = 11.4\text{ dB}$)**, **Phase Margin ($\text{PM} = 52^\circ$)**, and **Closed-Loop Bandwidth ($\omega_{\text{BW}}$)**.
   - Combine color + line style (`Solid Bold` = Proposed Controller, `Dashed Slate` = Uncompensated / PID Baseline, `Dotted Red` = Delayed Plant) so plots remain unambiguous even on low-contrast projectors.
2. **Lyapunov Phase Portraits & 3-Panel Trajectory Tracking**:
   - **Never present $V(x) > 0, \dot{V}(x) \le -\alpha V(x)$ as naked algebra.** Pair the OMML Lyapunov inequality on `Card 0` with a **2D State-Space Phase Portrait** ($x_1$ vs $x_2$) on `Card 1` showing elliptical/non-convex level sets $V(x) = c$, inward vector-field arrows, state convergence trajectories, and the certified **Region of Attraction (ROA)** boundary.
   - **Mandatory 3-Row Time-Domain Tracking Stack** (sharing time axis $t$):
     1. *Top*: Reference $y_{\text{ref}}(t)$ (dashed) vs Measured $y(t)$ (solid).
     2. *Middle*: Tracking Error $e(t)$ bounded inside shaded $\pm \epsilon$ convergence tube.
     3. *Bottom*: **Control Effort / Actuator Input $u(t)$** with horizontal dashed saturation limits ($\pm u_{\max}$) — **essential to prove to CDC/ICRA reviewers that tracking precision does not rely on unrealistic torque spikes or high-frequency sliding-mode chattering!**

#### C. Experimental Physics Theory-vs-Experiment & Error-Bar Standards (`APS / PRL`)
1. **Sacred Marker-vs-Line Convention**:
   - **Experimental Measurements**: Plot as **discrete solid markers (`5–7pt` circles/squares) with explicit error bars (`stroke >= 2.0pt`, visible end-caps)** — never connect noisy discrete experimental points with deceptive spline curves.
   - **Theoretical Prediction / Analytical Model**: Plot as a **continuous smooth curve (`2.2pt` solid line, zero markers)**.
2. **Mandatory Uncertainty Definition & Residual Sub-Panel**:
   - Every physics plot caption or corner legend must explicitly define error bars: `"Error bars: ±1σ statistical uncertainty (N = 500 shots); shaded gray band: ±3% systematic calibration uncertainty."`
   - Attach a thin (`h = 0.85"`) **Normalized Residual Strip** ($(y_{\text{exp}} - y_{\text{th}})/\sigma$ within $\pm 2\sigma$) along the bottom of the main fit plot to visually prove goodness-of-fit (or spotlight new-physics deviations!).

### 3.6 Real-Robot Deployment Frame Strips & Control Latency Budgets (`ICRA / RSS / CoRL`)

#### A. Real-Robot Deployment Filmstrip (`Slide 10`, `asymmetric_2row` Top Card or `grid_4col`)
Static single-frame robot photos cannot prove closed-loop dynamic behavior, and embedded `.mp4` videos frequently fail on conference room PCs. Always include a **Self-Contained High-DPI Deployment Filmstrip**:
1. **4-to-6 Chronological Keyframes** ($W_{\text{total}} = 12.133'', H = 2.45''$, uniform crop aspect ratio, separated by `0.08"` white gutters + `→` chevrons):
   - Stamp every frame at top-left with a dark semi-transparent **Monotonic Timestamp Pill**: `t = 0.0 s` $\rightarrow$ `t = 0.4 s` $\rightarrow$ `t = 0.9 s` $\rightarrow$ `t = 1.6 s` $\rightarrow$ `t = 2.3 s`.
   - Stamp top-right of the strip with an explicit **Playback Honesty Badge**: `▶ 1× Real-Time (Uncut Hardware Rollout)` (if sped up in video, state actual wall-clock seconds clearly).
   - Annotate physical interaction events directly on keyframes: red force arrow at `t = 0.4 s` (`"External Stick Push: 18 N"`), contact/slip inset at `t = 0.9 s` (`"Tactile Slip Detected → Gripper Re-Grasp"`), green check badge at `t = 2.3 s` (`"Sub-mm Peg Insertion Complete"`).

```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ [t = 0.0s]       │  │ [t = 0.4s] ⚡18N │  │ [t = 0.9s]       │  │ [t = 1.6s]       │  │ [t = 2.3s] ✔     │
│  Visual Pre-Grasp│→ │ External Impulse │→ │ Tactile Slip     │→ │ Pose Recovery &  │→ │ 0.4mm Tolerance  │
│  Pose Alignment  │  │ Disturbance Hit  │  │ Compensation     │  │ Impedance Align  │  │ Insertion Success│
└──────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────┘
```

#### B. End-to-End Sim-to-Real Latency Budget Bar (`Slide 8`, Mandatory for Deployed Robotics)
Phase lag from unbudgeted sensor/inference delay is the #1 killer of sim-to-real transfer. Pair the robot control block diagram with a **Horizontal Stacked Latency Budget Bar** (`w = 7.20"`, `h = 0.65"`):

| Pipeline Stage | Hardware / Bus | Measured Latency (ms) | Share of 33.3 ms (30 Hz) Deadline |
|:---|:---|---:|---:|
| **1. RGB-D + Tactile Capture** | Global-Shutter GMSL2 + DMA | `6.4 ms` | `19.2%` |
| **2. Vision-Language Backbone** | Jetson AGX Orin (TensorRT FP16) | `12.8 ms` | `38.4%` |
| **3. Diffusion / Flow Action Chunk** | 4-Step Consistency Distillation ✦ | `5.1 ms` | `15.3%` |
| **4. DDS / EtherCAT + Torque Rise** | 1 kHz Low-Level Impedance PD | `2.9 ms` | `8.7%` |
| **Total End-to-End Loop Delay** | **6.1 ms Safety Headroom Remaining** | **`27.2 ms`** | **`81.7% < 33.3 ms Deadline ✔`** |

### 3.7 `STEM-PHYS-ENG` Anti-Patterns & Concrete Surgeries

| Anti-Pattern Observed | Why It Fails Live | Mandatory Agent Surgery |
|:---|:---|:---|
| Raw Cadence Virtuoso / Simulink / Vivado screenshot | `5pt` net names & hairline wires vanish; zero hierarchy | Abstract into 5–8 clean vector functional blocks (`Left→Right` signal, max 3 domain tints, `✦` on novel block) |
| Bare die micrograph with zero overlays or scale bar | Looks like an indecipherable metallic texture | Pair side-by-side with floorplan; add haloed macro boxes, `500 μm` scale bar, and `Node / Area / VDD / Power` pill |
| Cluttered lab bench photo (oscilloscopes, tangled BNC wires, coffee mug) | Looks amateurish; hides actual physical signal chain | Split slide: clean vector optical/RF schematic on left + background-isolated sample/PCB crop with `①②③` pins on right |
| Physics data points connected by jagged lines without error bars | Violates experimental physics standards; obscures statistical vs systematic noise | Plot discrete markers with `≥2.0pt` error bars + smooth markerless theory curve + explicit `1σ` definition + residual strip |
| Robotics trajectory tracking plot omitting control input $u(t)$ | Reviewers suspect infinite-torque simulation tricks or hardware chattering | Add aligned bottom $u(t)$ subplot showing smooth commands strictly inside $\pm u_{\max}$ actuator limits |

---

## 4. Cross-STEM Synthesis: Density Ceilings, IR Recipes & Vision QA Audit

### 4.1 Quantitative Slide Density & Typography Ceiling Matrix

Enforce these numeric guardrails during Stage 2 (Information Architecture) and Stage 3 (Code Generation):

| Parameter / Budget | `STEM-CS` (AI / Systems / Security) | `STEM-MATH` (Math / Stats / Opt / TCS) | `STEM-PHYS-ENG` (Physics / EE / Robotics) |
|:---|:---|:---|:---|
| **Visual Asset Coverage** | $\ge 11 / 14$ slides ($\ge 80\%$) | $\ge 10 / 14$ slides ($\ge 70\%$ plots/DAGs/OMML cards) | $\ge 12 / 14$ slides ($\ge 85\%$) |
| **Max Display Equations / Slide** | `1–2` OMML display blocks | `2` OMML display blocks (`≤ 3` chained `=/≤` steps max!) | `1–2` OMML display blocks (paired with diagram/plot) |
| **Max Table Dimensions** | `8 rows × 7 cols` (SOTA) / `5 × 5` (Ablation) | `6 rows × 5 cols` (Asymptotic Rate / Tightness table) | `8 rows × 6 cols` (Transposed ISSCC/FoM summary table) |
| **Max Vector Diagram Nodes** | `8–10` macro blocks + `≤ 6` tensor pills | `6–8` Proof DAG nodes + labeled implication edges | `7–10` functional subsystem blocks + feedback loop |
| **Min Body / Table Font Size** | `13 pt` body / `11.5 pt` table cell | `14 pt` body / `16–20 pt` display OMML math | `13 pt` body / `12 pt` FoM cell / `11 pt` diagram callout |
| **Min Plot Line & Error-Bar Width** | `2.0 pt` Pareto/CDF curves | `2.0 pt` geometric contours / phase boundaries | `2.0–2.5 pt` waveforms, Bode curves & `≥ 2.0 pt` error bars |
| **Max Accent Colors / Slide** | `1` primary novelty accent + muted slate | `3–4` persistent semantic math term colors | `3` physical domain tints (e.g., Analog / Digital / Power) |

### 4.2 Agent-Executable Slide IR Recipe (Color-Annotated OMML + Callout Pills)

When generating slide definitions for `build_deck.js` / `python-pptx` + `latex_to_omml.py`, structure STEM slides with explicit coordinate geometry on the $13.333'' \times 7.500''$ canvas:

```json
{
  "slide_index": 7,
  "profile": "STEM-MATH",
  "grid_model": "asymmetric_2row",
  "tracker": "KEY FORMULATION • SLIDE 07 OF 14",
  "title": "Clipped Proximal Risk Decomposes Into Exponential Decay, Bias, and Tail Noise",
  "subtitle": "Separating deterministic curvature contraction from heavy-tailed martingale variance via threshold τ.",
  "cards": [
    {
      "id": "hero_top",
      "x": 0.600, "y": 1.650, "w": 12.133, "h": 2.450,
      "header": "Color-Annotated Excess Risk Upper Bound (Theorem 1 Decomposition)",
      "math_display": "{{MATH_DISPLAY:\\mathbb{E}[\\|\\hat{\\boldsymbol{\\theta}}_T - \\boldsymbol{\\theta}^*\\|_2^2] \\le \\exp(-\\mu \\eta T)\\|\\boldsymbol{\\theta}_0 - \\boldsymbol{\\theta}^*\\|_2^2 + C_1 \\eta^2 \\tau^{2-2p} + C_2 \\frac{\\eta \\sigma_p^p \\tau^{2-p}}{\\mu n}}}",
      "callout_pills": [
        { "label": "Geometric Init Contraction", "color": "1D4ED8", "x": 3.45, "y": 3.45 },
        { "label": "Clipping Bias ( vanishes as τ → ∞ )", "color": "B91C1C", "x": 6.85, "y": 3.45 },
        { "label": "✦ Bounded Tail Variance ( p ∈ (1,2] )", "color": "0F766E", "x": 9.80, "y": 3.45 }
      ]
    },
    {
      "id": "bottom_left",
      "x": 0.600, "y": 4.300, "w": 5.916, "h": 2.550,
      "header": "Optimal Clipping Schedule & Sanity Checks",
      "bullets": [
        "Setting {{MATH:\\tau \\asymp (n / \\eta)^{1/p}}} balances bias and heavy-tailed variance.",
        "Gaussian limit ({{MATH:p = 2}}): recovers exact minimax {{MATH:\\mathcal{O}(d / (\\mu^2 n))}} parametric rate.",
        "Zero-noise limit ({{MATH:\\sigma_p = 0}}): collapses cleanly to deterministic linear convergence."
      ]
    },
    {
      "id": "bottom_right",
      "x": 6.816, "y": 4.300, "w": 5.916, "h": 2.550,
      "header": "Persistent Symbol & Regularity Glossary",
      "bullets": [
        "{{MATH:\\mu, L}}: Strong convexity & Lipschitz gradient constants ({{MATH:\\kappa = L/\\mu}}).",
        "{{MATH:p \\in (1, 2]}}: Bounded {{MATH:p}}-th central moment of stochastic gradient noise.",
        "{{MATH:\\tau > 0}}: Adaptive norm-clipping radius requiring zero prior knowledge of {{MATH:\\mu}}."
      ]
    }
  ]
}
```

### 4.3 15-Point STEM Vision-in-the-Loop Pixel Audit (`Stage 4 QA`)

After rendering all slides via LibreOffice + `pdftoppm`/PyMuPDF at **150+ DPI PNG**, call `view_file` on **every slide** and verify these 15 STEM-specific visual checks before completion:

- [ ] **1. Assertion-Evidence Headline Check**: Every slide title states a concrete technical mechanism, theorem bound, or quantified delta — zero generic labels (`"Method"`, `"Results"`, `"Proof"`).
- [ ] **2. Zero Raw LaTeX Leakage**: Zero literal `$$`, `\frac`, `\mathcal`, `\mathbb`, or `{{MATH:...}}` tokens visible anywhere on rendered slides; all math is sharp vector Cambria Math OMML.
- [ ] **3. Aspect-Ratio Integrity**: Harvested architecture diagrams, die micrographs, oscilloscope captures, and qualitative crops have natural proportions (circular summing junctions `(⊕)` and wafer dies are true circles, never ovals).
- [ ] **4. Novelty Pop Test (`STEM-CS` / `STEM-PHYS-ENG`)**: Within 3 seconds of viewing Slide 8, the proposed module/circuit/controller (`✦ NOVEL`) is visually unmistakable from frozen/standard baseline blocks.
- [ ] **5. Tensor Pill Clearance (`STEM-CS`)**: Tensor shape badges (`[B, L, d_c]`) float cleanly above/below connector shafts with zero line-through-text collisions.
- [ ] **6. SOTA Table Readability & Winner Hierarchy (`STEM-CS`)**: Benchmark tables have $\le 8$ rows, zero vertical gridlines, directional arrows (`↑ / ↓`) on every metric header, bold 1st-place, underlined 2nd-place, and an explicit `Δ` column.
- [ ] **7. Pareto Ideal-Corner Orientation (`STEM-CS`)**: Trade-off scatter/line plots display a clear diagonal arrow pointing to the optimal corner (`↖ Better`) and highlight `Ours` above muted baselines.
- [ ] **8. Security Trust Boundary Explicitness (`STEM-CS`)**: Security decks visibly separate `[TCB]` from untrusted components and explicitly list both `In-Scope` and `Out-of-Scope` threats.
- [ ] **9. Zero Proof Walls (`STEM-MATH`)**: No slide contains $>3$ chained lines of algebraic derivation; theorem proofs are represented via a Proof Dependency DAG + single novel lemma deep-dive.
- [ ] **10. Semantic Formula Color & Callout Alignment (`STEM-MATH`)**: Leader lines from semantic callout pills point accurately to their target OMML equation terms without overlapping subscripts/superscripts.
- [ ] **11. Clean $\tilde{\mathcal{O}}$ Theorem Box (`STEM-MATH`)**: Formal theorem card uses assumption pills, clean asymptotic notation, and relegates messy universal constants to a `10pt` card footer.
- [ ] **12. Haloed Die & Cleaned Testbed Callouts (`STEM-PHYS-ENG`)**: Die micrographs include a physical scale bar, process node pill, and legible haloed callouts; benchtop setups use vector schematics + isolated crops rather than messy lab photos.
- [ ] **13. Aligned Bode & Complete Control Stack (`STEM-PHYS-ENG`)**: Bode Magnitude and Phase share an aligned log-$\omega$ axis with labeled `GM / PM`; time-domain tracking plots include control effort $u(t)$ within saturation bounds.
- [ ] **14. Physics Error-Bar & Fit Convention (`STEM-PHYS-ENG`)**: Experimental points use discrete markers with thick (`≥2pt`) error bars (`1σ` defined); theoretical predictions use smooth markerless curves.
- [ ] **15. Real-Robot Filmstrip & Latency Deadline (`STEM-PHYS-ENG`)**: Robot deployment strips have monotonic `t = ... s` badges + `1× Real-Time` tag, and the stacked latency budget bar sums strictly below the control period deadline.
