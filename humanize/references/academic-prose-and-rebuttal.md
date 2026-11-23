# Academic Prose, Rebuttals & Grant Proposals — De-AI Reference Guide

Peer-reviewed manuscripts, conference rebuttals, and grant proposals suffer from a distinct strain of AI slop. Corpus-scale stylometry across more than one million arXiv, PubMed, and Nature-portfolio papers (Liang et al., *Nature Human Behaviour* 2024; Kobak et al., 2024) shows that Computer Science papers exhibit the highest concentration of LLM-polished text—exceeding 20% of arXiv CS submissions—and that reviewers recognize these lexical and structural fingerprints within seconds.

Unlike blogs or essays, **academic humanization never adds slang, contractions, or casual banter.** Humanizing scholarly prose means replacing RLHF inflation, textbook throat-clearing, laundry-list citations, and sycophantic rebuttal boilerplate with **mechanistic precision, falsifiable claims, comparative synthesis, and clean mathematical contracts.**

> **Execution Order ([../SKILL.md](../SKILL.md)):** Always enforce [../paper-boundaries.md](../paper-boundaries.md) (Press-Conference Principle / 发布会原则) **before** polishing sentence-level prose so you never humanize a self-undermining narrative or an uncurated experiment dump. Then pair this guide with [../english.md](../english.md), [../chinese.md](../chinese.md), or [bilingual-tech-writing.md](bilingual-tech-writing.md) for prose hygiene, and [scientific-figures-and-ui-de-ai.md](scientific-figures-and-ui-de-ai.md) for Figure 1 / plot standards.

---

## 1. Empirical Academic AI Fingerprint Catalog (EN & CN)

Corpus frequency-shift studies prove that LLMs inflate *decorative style words* while leaving domain-specific nouns untouched. When two or more markers below cluster in one paragraph, rewrite immediately.

### 1.1 English Scholarly Excess-Vocabulary Blacklist

| High-Spike AI Marker | Why Reviewers Flag It | Concrete Scholarly Replacement |
|:---|:---|:---|
| *delve into / delve deeper* | #1 post-2023 LLM statistical outlier in PubMed/arXiv | *analyze, derive, measure, isolate, examine* |
| *intricate / intricate interplay* | Hand-waves away actual functional form | Specify the coupling (*"bilinear interaction between $Q$ and $K$"*, *"feedback loop between..."*) |
| *meticulous / meticulously designed* | Self-congratulatory adverbial fluff | Delete adverb; state the exact design constraint |
| *pivotal / crucial / paramount* | Inflation crutch used when causal weight is unclear | State what breaks without it (*"governs convergence"*, *"bounds worst-case regret"*) |
| *realm (`in the realm of`)* | Zero-content noun padding | Delete (*"in distributed consensus"*, not *"in the realm of distributed consensus"*) |
| *underscores / highlights / showcases* | Participial tail tacked onto data sentences | State the causal takeaway in a finite clause (*", which confirms Equation (5)"*) |
| *leverage / utilize / harness* | Corporate-academic verb inflation | *use, apply, exploit (for structure/sparsity)* |
| *comprehensive / extensive / thorough* | Unverified self-praise on experiments | Give exact counts (*"across 6 datasets, 3 model scales, and 4 corruption types"*) |
| *novel* (used >1x per paper) | Reviewers decide novelty; repeating the word cheapens it | Name *what* is new (*"first single-pass estimator"*, *"exact $O(N)$ formulation"*) |
| *commendable / notable / remarkable* | LLM peer-review & related-work flattery | State the exact quantitative milestone |
| *shed light on / pave the way for* | Vague closing cliché in abstracts | Name the enabled capability or proven bound |
| *paradigm shift / groundbreaking* | Triggers immediate reviewer skepticism | Delete; let Table 1 carry the weight |

### 1.2 Chinese Academic & Journal Slop Blacklist (`中文学术论文高频 AI 套话`)

| AI 套话类别 | 典型高危表达（见则必改） | 严谨学术替换方案 |
|:---|:---|:---|
| **宏大叙事开场** | 在当今数字化/智能化飞速发展的时代背景下；随着深度学习的蓬勃兴起 | 直接删去背景空话，首句直指具体任务场景与失效边界 |
| **空洞价值拔高** | 具有极其重要的理论意义与广阔的实际应用前景 | 写明具体失效代价或理论缺口（如「现有上界在非独立同分布下发散」） |
| **互联网黑话跨界污染** | 痛点、抓手、赋能、闭环、底座、组合拳、赛道、颗粒度、打通最后一公里 | 换回规范学科术语：`瓶颈/退化机理`、`正则约束`、`反馈控制回路`、`基础算子` |
| **对称句式强迫症** | 不仅…而且…；既实现了…又兼顾了…同时还构建了…；不是…而是… | 拆分为因果或递进短句，给出定量权衡指标 |
| **模糊性能吹嘘** | 显著提升了模型的鲁棒性、泛化性与有效性；取得了令人满意的效果 | 给出精确工况与增量（如「在高斯噪声 $\sigma=0.25$ 下将 mAP 提升 3.7 个百分点」） |
| **车轱辘过渡词** | 值得一提的是、不可否认的是、显而易见、综上所述、总而言之 | 能用逻辑关系衔接就不加连接词；确需转折仅用 `然而`、`但`、`为此` |

---

## 2. Section-by-Section Manuscript De-AI Surgery

### 2.1 Abstract: Killing Throat-Clearing & Hype Tails

**AI Failure Mode:** Sentence 1 narrates 10 years of field history; Sentence 2 says prior work *"faces significant challenges in balancing efficiency and accuracy"*; Sentence 3 introduces an acronym-heavy *"novel synergistic framework"*; Sentence 5 promises *"promising results that pave the way for future research."*

**The 5-Move High-Density Abstract Blueprint:**
1. **Target & Concrete Bottleneck (1 sentence):** Name the exact task and physical/algorithmic failure condition—skip generic praise of the field.
2. **Mechanistic Diagnosis (1 sentence):** State *why* existing formulations fail (e.g., quadratic memory, variance explosion, distribution shift).
3. **Core Technical Insight (1 sentence):** State what your method does differently at the mathematical or systems level.
4. **Operational Realization (1 sentence):** Explain how the key component works cleanly without black-box buzzwords.
5. **Hard Numbers + Cost Envelope (1–2 sentences):** Report exact deltas on named benchmarks, compute/latency savings, and code/artifact availability if applicable.

**Before (EN — Typical LLM-Polished CS Abstract):**
> Large Language Models (LLMs) have recently revolutionized natural language processing, demonstrating remarkable capabilities across a wide realm of tasks. However, deploying these massive models in real-world scenarios remains a pivotal challenge due to intricate memory bottlenecks during long-context inference. Existing KV-cache compression methods struggle to balance memory efficiency and generation fidelity, often suffering from severe performance degradation. To address this crucial issue, we propose AdaKV, a novel and comprehensive framework that meticulously leverages attention sparsity to dynamically prune redundant tokens. Extensive experiments across multiple benchmarks showcase that AdaKV significantly outperforms state-of-the-art baselines, underscoring its effectiveness and paving the way for efficient LLM deployment.

**After (EN — Crisp, Mechanistic, Zero-Slop Abstract):**
> Long-context LLM inference beyond 64K tokens is bottlenecked by KV-cache memory growth, which scales linearly with sequence length and exceeds single-GPU capacity before compute saturates. Existing eviction policies assign uniform token budgets across attention heads, discarding retrieval-critical tokens in sparse induction heads while retaining redundant context in local-window heads. We introduce AdaKV, an online head-wise budget allocator that bounds layer-level eviction error via $L_1$ attention-mass concentration measured during prefill. AdaKV requires zero model retraining and adds less than 0.8% latency overhead via a fused Triton kernel. Across LongBench, Needle-in-a-Haystack (up to 128K), and RULER, AdaKV retains 99.3% of full-cache accuracy at 20% KV budget, outperforming uniform H2O and SnapKV eviction by 6.4 points on multi-needle retrieval.

**Before (CN — 典型 AI 味中文摘要):**
> 近年来，随着自动驾驶技术的迅猛发展，三维点云目标检测已成为计算机视觉领域的研究热点，具有重要的理论意义和应用价值。然而，激光雷达点云在远距离场景下存在严重稀疏性，现有方法往往面临精度与速度难以兼顾的痛点。针对上述挑战，本文提出了一种新颖的多尺度上下文赋能网络（MSCENet），通过精心设计的特征融合模块深入挖掘局部与全局之间的内在联系。大量详实的实验结果表明，本文方法在多个主流数据集上均取得了显著优于现有最先进方法的卓越性能，充分彰显了该框架的优越性与鲁棒性。

**After (CN — 紧凑机制驱动中文摘要):**
> 车载激光雷达在 50 米以外区域的点云密度急剧衰减，导致基于固定体素感受野的三维检测器在远距离小目标（行人、骑行者）上出现大量漏检；而直接扩大三维卷积核会使显存与推理延迟呈立方级膨胀。本文提出距离感知动态体素扩散网络（DVD-Net），根据目标径向距离自适应分配径向-方位角非对称稀疏卷积核，在不增加近场计算负担的前提下聚合远场跨体素几何上下文。在 Waymo Open Dataset 与 nuScenes 验证集上，DVD-Net 将 50 米外行人 Level-2 mAPH 提升 4.2 个百分点，在单张 Orin 芯片上保持 28.5 FPS 实时推理速度。

---

### 2.2 Introduction & Contribution Bullets: Falsifiable Contracts

Following Simon Peyton Jones and Michael Ernst, the Introduction establishes tension rapidly and closes with **Contribution Bullets** that serve as an explicit, falsifiable contract with the reviewer.

**Rules for De-AI-ing Introductions & Contributions:**
- **Ban the "History of Computing" Opener:** Never start Paragraph 1 further back than the immediate problem domain. If your paper is on FlashAttention backward-pass register spilling, Paragraph 1 starts at GPU SRAM/HBM bandwidth asymmetry, not *"Deep learning has transformed human society."*
- **Ban Vague Gap Strawmen:** Never write *"Existing works fail to consider efficiency."* Cite the exact competing class and state the exact complexity or approximation bound where they break.
- **Kill the Padding Contribution Bullet:** Delete standalone bullets reading *"We conduct extensive experiments on four benchmarks to demonstrate the superiority of our method."* Fold experimental validation into the substantive algorithmic/empirical contribution bullets, or turn the experimental bullet into a **specific empirical discovery** (e.g., *"We uncover a phase transition at rank $r=16$ across 8 vision-language benchmarks..."*).
- **Zero Self-Awarded Hype Adjectives in Bullets:** Strip *novel, pioneering, elegant, comprehensive, meticulous* from every bullet. Start each bullet with an active verb or artifact noun: **Formulation, Algorithm, Theoretical Guarantee, System Kernel, Empirical Scaling Law.**

**Before (EN — AI Slop Contribution List):**
> Our main contributions can be summarized in threefold as follows:
> - We delve into the intricate problem of multi-agent reward shaping and propose a novel, plug-and-play framework named MARS that seamlessly integrates credit assignment with exploration.
> - We meticulously design an innovative dual-critic module that fosters stable gradient updates and alleviates variance.
> - We conduct comprehensive and extensive experiments on multiple challenging benchmarks, showcasing that MARS achieves state-of-the-art performance and underscoring its broad applicability.

**After (EN — Falsifiable Contract Contribution List):**
> This paper makes three contributions:
> - **Counterfactual Credit Decomposition:** We formulate per-agent advantage estimation via a marginalized Shapley projection (Section 3.2) that reduces critic variance from $O(N^2)$ to $O(N)$ in $N$-agent cooperative games while preserving Nash policy invariance (Theorem 1).
> - **Single-Pass Dual-Critic Estimator:** We design a shared-trunk target network that computes exact marginalized baselines in one forward pass, cutting wall-clock step time by 3.1x compared to counterfactual rollouts (COMA).
> - **Scaling to 64-Agent Benchmarks:** Across SMACv2, Multi-Agent MuJoCo, and Google Research Football (up to 64 agents), our estimator solves three super-hard scenarios where prior credit-assignment methods plateau at 0% win rate.

---

### 2.3 Related Work: Taxonomic Synthesis vs. Laundry Lists (`文献综述去流水账化`)

The #1 sign of junior or AI-generated academic prose is the **Annotated Bibliography Laundry List**: `[1] proposed A. [2] introduced B. Furthermore, [3] developed C. However, none of them address X.`

**The 3-Move Synthesis Protocol:**
1. **Cluster by Technical Axis (Topic Sentence):** Open every paragraph with a **taxonomic claim** grouping 3–8 papers by their core mathematical assumption, representation, or system bottleneck—never by author name or publication year.
2. **Compare Trade-offs Across Clusters (Body):** Contrast Sub-family A against Sub-family B along a shared dimension (e.g., *exactness vs. memory*, *offline supervision vs. test-time latency*). Cite papers inside parentheses or concisely in-line to substantiate mechanisms, never summarizing abstracts one by one.
3. **Position Structural Separation (Closing Sentence):** Close the paragraph by stating the exact assumption your work removes or reframes—without insulting prior authors (*"fails completely"*, *"naive"*).

**Before (EN — Classic Laundry List):**
> Many researchers have studied graph condensation. Jin et al. [1] proposed GCond, which matches gradients between the original graph and synthetic graph. Dosovitskiy et al. [2] further improved efficiency by matching only single-step gradients in DosCond. Additionally, Liu et al. [3] introduced GCDM, which utilizes distribution matching in receptive field space. Moreover, Zheng et al. [4] proposed SFGC to synthesize structure-free node sets using trajectory matching. Despite these commendable efforts, existing methods still suffer from high computational overhead and struggle to generalize across different GNN architectures.

**After (EN — Comparative Taxonomic Synthesis):**
> Graph condensation methods trade bi-level optimization fidelity against synthesis cost along two primary axes: **optimization-aligned matching** and **distribution-aligned matching**. Optimization-aligned approaches match training gradients [1, 2] or multi-epoch parameter trajectories [4] between full and condensed graphs; while trajectory matching [4] captures long-horizon curvature, unrolling inner GNN training loops incurs $O(T \cdot |E|)$ memory and overfits the synthetic graph to the specific relay backbone's spectral filter. Distribution-aligned methods bypass inner loops by matching layer-wise receptive-field embeddings [3], cutting synthesis time by an order of magnitude at the cost of discarding label-boundary discriminative high-frequency components. Our spectral eigen-basis matching bridges both regimes: it avoids inner-loop unrolling entirely while preserving high-frequency class boundaries independent of any fixed GNN propagation operator.

**Before (CN — 中文文献堆砌流水账):**
> 在时间序列异常检测领域，国内外学者开展了大量研究。王明等人[1]提出了一种基于 LSTM 自编码器的重构方法，在工业传感器数据上取得了不错的效果。随后，李华等人[2]引入了图注意力机制以捕捉多变量之间的关联性。此外，Zhang 等人[3]提出了 Anomaly Transformer，利用关联差异来放大正常点与异常点的区分度。值得一提的是，Chen 等人[4]最近将扩散模型引入异常检测中。尽管上述方法做出了一定贡献，但它们在面对非平稳分布漂移时仍然存在诸多不足。

**After (CN — 机理分类与边界对比综述):**
> 多变量时间序列异常检测主要沿**重构残差判别**与**关联结构偏离**两条技术路径演进。重构类方法通过循环自编码器[1]或条件扩散先验[4]拟合正常工况流形，对幅值突变型异常敏感，但在季节性均值缓慢漂移的非平稳工况下，重构误差会被正常趋势放大而触发大量误报。结构偏离类方法显式建模跨传感器图拓扑[2]或自注意力关联差异[3]，提升了子序列上下文异常的检出率，但其均假设正常模式的协方差结构在测试期保持静态不变。本文方法显式解耦局部非平稳趋势项与时变条件独立图，使异常判据在工况均值与方差同步漂移时仍保持恒定虚警率。

---

### 2.4 Method / Approach: Intuition -> Contract -> Mechanism -> Justification

**AI Failure Modes in Method Sections:**
- **Ceremonial Module Naming:** Inventing 4 grandiose acronyms (`Synergistic Cross-Modal Holistic Aggregator, SCMHA`) when `cross-attention gate` suffices.
- **Prose-Equation Echo:** Writing *"We compute $z = \sigma(Wx + b)$, where $W$ is a weight matrix, $x$ is the input, $b$ is a bias, and $\sigma$ is an activation function."* Readers know basic linear algebra; tell them *what $z$ represents geometrically* and *what tensor shapes enter and exit*.
- **Unmotivated Design Choices:** Dropping a temperature $\tau$, an $L_2$ penalty, and a stop-gradient operator with zero explanation of what collapses if you remove them.

**4-Rule Method Rewrite Standard:**
1. **Intuition Before Symbols:** Start every subsection with 1–2 plain sentences stating the sub-problem and geometric/algorithmic idea before introducing notation.
2. **Explicit Input/Output Contract:** Specify domain/tensor dimensions once cleanly (e.g., *"Given token representations $X \in \mathbb{R}^{B \times L \times d}$..."*).
3. **Interpret Terms, Don't Read Symbols Aloud:** After displaying an equation, explain the competing forces or limiting cases (e.g., *"As $\lambda \to 0$, Eq. (4) reduces to hard top-$k$ routing; for $\lambda > 0$, the entropic barrier prevents router collapse during early warmup"*).
4. **State "Why This Over X":** Briefly justify non-obvious choices (*"We apply `stop_grad` on the anchor branch because joint backpropagation admits a trivial constant solution $f(x) \equiv c$"*).

---

### 2.5 Experiments: Killing the "Table-Reader Voice"

**AI Failure Mode:** Converting rows of Table 1 into monotonous prose (*"On Dataset A, our method gets 78.2%, beating Method X (75.1%) by 3.1%. On Dataset B, our method gets 84.0%, beating Method X (81.9%) by 2.1%. This clearly demonstrates..."*).

**Rewrite Rules:**
- **Never transcribe >2 raw baselines in a row** when the reader is already looking at the table. Quote only **deltas, ratios, or extreme regimes** that prove an analytical point.
- **Organize Paragraphs by Takeaway Claim (Bold Lead-Ins Allowed):** Instead of `Results on Dataset A / Results on Dataset B`, group observations by **phenomenon** (*"**Gains widen as context length exceeds 32K.** While dense retrievers degrade by 19 points from 4K to 64K..."*).
- **Explain Anomalies Mechanistically:** If your gain is +8.1% on Dataset A and +0.9% on Dataset B, explain *why* via dataset statistics (e.g., label homophily, sequence length distribution, SNR) rather than glossing over it with *"overall superior performance."*

---

### 2.6 Limitations Without Self-Sabotage (`不递刀子的局限性写法`)

Conferences such as NeurIPS, ICLR, ICML, and ACL ARR mandate an explicit `Limitations` section. AI writers oscillate between two fatal extremes: **Fake-Humble Suicide** (*"Our method suffers from poor scalability and lacks theoretical guarantees"*) or **Dishonest Non-Limitations** (*"A limitation is that we plan to test on more datasets in the future"*).

**The 3-Step Safe Boundary Formula (Aligned with `paper-boundaries`):**
1. **Specify the Exact Boundary Condition (`客观界定适用边界`):** Name the precise mathematical assumption, hardware constraint, or input regime where performance shifts—never use global negative adjectives.
2. **Quantify the Threshold / Existing Mitigation (`量化交叉点或对冲依据`):** Show you already measured *where* the boundary sits and explain why core conclusions inside the target regime remain rock-solid.
3. **Point to Concrete Technical Extension (`指明可落地的技术演进路径`):** Frame the boundary as a crisp engineering or theoretical formulation for follow-up work.

**Before (EN — Self-Sabotaging AI Limitations):**
> Despite achieving strong performance, our method has several notable limitations. First, our diffusion sampler is still relatively slow on edge devices and struggles with real-time generation. Second, our method relies heavily on accurate camera pose annotations, and performance degrades severely when poses are noisy, limiting its practical applicability in the wild.

**After (EN — Rigorous, Trust-Building Boundary Specification):**
> **Operating Boundaries.** First, our 4-step consistency solver targets interactive desktop GPUs (18 FPS on RTX 4070 at $512^2$); deploying below 8W mobile power envelopes requires pairing our trajectory distillation with INT4 weight-activation quantization, which orthogonal post-training quantizers support directly. Second, our epipolar cross-attention assumes camera extrinsics accurate to within $\pm 3^\circ$ rotation (standard COLMAP convergence); under severe pose noise ($>10^\circ$, Appendix Fig. 9), softly annealing the epipolar mask weight $\gamma \to 0.2$ preserves generation coherence while gracefully relaxing multi-view geometric lock.

---

## 3. Conference Rebuttals & Author Responses (OpenReview / ARR / Journal Replies)

OpenReview rebuttals operate under brutal character limits (often 5,000–8,000 characters) and severe Area Chair (AC) time pressure. Unedited LLM rebuttals destroy acceptance chances via **RLHF sycophancy** and **low-density fluff**.

### 3.1 The 5 Fatal Rebuttal Anti-Patterns

| Anti-Pattern | Typical LLM Slop | Why ACs & Reviewers Hate It | Exact Fix |
|:---|:---|:---|:---|
| **1. Sycophantic Groveling** | *"We sincerely thank the reviewer for this extraordinarily insightful, brilliant, and profound comment! You are completely right!"* | Sounds fake; worse, if the reviewer misread a theorem, agreeing validates a false flaw on the permanent record. | Thank the reviewer **once** in 1 line at the top of the reply; open individual answers directly with substance. |
| **2. Character-Budget Bloat** | Restating the reviewer's entire 8-line paragraph + 3 lines of throat-clearing before answering. | Wastes 35% of your character limit; hides new numbers below the fold. | Use compact 4–6 word bold tags: `**[W1: Latency on 70B]**` followed immediately by the answer and table. |
| **3. Camera-Ready IOU** | *"Thank you for the suggestion; we will definitely run this baseline in the camera-ready version."* | Zero evidentiary weight during AC discussion; ACs discount unexecuted promises to zero. | Run the experiment (or a well-scoped compute-matched proxy) *during* the rebuttal window and paste the Markdown table right there. |
| **4. Passive-Aggressive Snark** | *"As we already clearly explained in Section 3.2 (which the reviewer may have overlooked)..."* | Triggers ego defense; turns a persuadable `5: Marginally below` into a dug-in `3: Reject`. | Own exposition clarity without conceding technical validity: *"We apologize that our notation in Sec. 3.2 obscured this: Eq. (6) explicitly handles..."* |
| **5. Hallucinated Explanations** | Letting an LLM invent speculative intuition for an ablation number without checking logs. | Reviewers verify code/PDF diffs; caught speculation kills trust across all scores. | Every number and claim in a rebuttal must trace to a verified run or exact theorem line. |

### 3.2 High-Conversion OpenReview Response Architecture

1. **Global Author Response (`General Response to AC & All Reviewers`, <= 500 words):**
   - Bullet 1: 2-sentence reminder of core consensus strengths acknowledged across reviewers (`R1, R3, R4`).
   - Bullet 2: Summary of **new experiments added during rebuttal** (e.g., *New 70B scaling table, 2 requested baselines, wall-clock breakdown*) in one scannable Markdown table.
   - Bullet 3: Pointer to exact blue-highlighted sections in the revised PDF.
2. **Individual Reviewer Reply (`Direct-Evidence-Diff` Micro-Structure):**
   - **Header (1 sentence max):** *"We thank Reviewer X for constructive feedback on baseline coverage and wall-clock profiling. Below we provide new Llama-3-70B results and pinpoint every PDF update."*
   - **Per-Item Block:**
     - **Direct Answer (Sentence 1):** Answer `Yes / No / Measured result` immediately.
     - **Hard Evidence (Body):** Compact Markdown table or 2-line derivation.
     - **Manuscript Diff Tag (Final Line):** `-> Added to Table 4 & Sec. 4.4 (p. 8, highlighted in blue).`

### 3.3 Rebuttal Surgery Examples

**Scenario A: Correcting a Factual Misreading Politely Without Groveling**
- **Before (AI Sycophancy + Self-Goal):**
  > Thank you so much for this insightful observation! You raise a crucial point regarding data leakage between our retrieval corpus and MMLU test questions. We deeply apologize for not discussing this pivotal aspect thoroughly enough, and we completely agree that contamination is a major concern in modern LLM evaluation.
- **After (Peer-to-Peer Precision + Hard Evidence):**
  > **[W2: Retrieval Corpus Contamination Check]** Our datastore explicitly strips all evaluation benchmarks prior to indexing, and we regret not highlighting this step more prominently in the main text. Specifically, Section 4.1 (and Appendix A.3) applies 13-gram exact and MinHash ($J \ge 0.8$) deduplication against MMLU, GSM8K, and HumanEval test splits, removing 14,820 overlapping passages. Re-running evaluation after an even stricter 8-gram filter changes MMLU accuracy by less than $0.1\%$ ($74.6\% \to 74.5\%$). `-> Promoted decontamination statistics from Appendix A.3 to Sec. 4.1 (p. 5, blue).`

**Scenario B: Handling "Novelty Is Just A + B" With a Decisive Ablation**
- **Before (Defensive AI Rhetoric):**
  > While our method builds upon A and B, we respectfully disagree that it is a simple combination. Rather than merely concatenating A and B, our framework represents a holistic synergy where A and B mutually reinforce each other in a non-trivial manner to unlock emergent performance gains.
- **After (Mechanistic Proof + Naive-Combination Failure Table):**
  > **[W1: Why Naive `A + B` Collapses Without Our Coupling Operator]** Combining A (sparse top-$k$ routing) directly with B (quantized KV eviction) causes severe gradient starvation because evicted tokens zero out router normalization denominators, dropping accuracy *below* A alone ($68.1\% \to 61.4\%$). Our Jacobian-rescaled gate (Eq. 7) resolves this exact variance mismatch:
  >
  > | Variant | LongBench Avg | Peak VRAM |
  > |---|---|---|
  > | A alone (Sparse Routing) | 68.1 | 22.4 GB |
  > | Naive `A + B` (Sequential composition) | 61.4 (-6.7) | 11.2 GB |
  > | **Ours (Jacobian-rescaled `A ∘ B`, Eq. 7)** | **71.9 (+3.8)** | **11.3 GB** |
  >
  > `-> Added naive composition row and gradient-norm trace to Sec. 4.3, Fig. 5 (p. 7, blue).`

### 3.4 中文顶刊审稿意见回复信（《计算机学报》《软件学报》《自动化学报》）

中文期刊修回说明（Response Letter）常见的 AI 灾难是「每条意见前写五十个字的感恩戴德套话」加「修改说明里只写“已补充相关分析”却不贴修改正文」。
- **去套话三段式规范：**
  1. **致谢总起仅限首段一次：** 「感谢审稿专家对本文理论推导与对比实验提出的宝贵建设性意见。我们已逐条补充实验并修订正文（修订处以蓝色字体标出），逐项汇报如下。」单条回复内**严禁**再写「非常感谢您极其敏锐且高屋建瓴的指正！您说得完全正确！」。
  2. **直答核心机制/数据：** 第一句直接回答审稿人疑问（给机理原因或新增实验数值）。
  3. **原位粘贴修改快照：** 精确注明 `【修订位置：第 4.2 节第 9 页第 2 段，表 3】`，并将修改后的关键段落与新增表格直接嵌在回复信中，免去审稿专家来回翻找正文的负担。

---

## 4. NSFC 国自然本子 & 中文基金/学位论文去 AI 味专项

国家自然科学基金委（NSFC）已明确规范生成式 AI 使用边界，函评专家对“大模型生成的宏大套话、空洞排比与工程/科学概念混淆”高度敏感。一旦被判定存在明显模板化 AI 痕迹，极易直接落入 C 类评分。

### 4.1 立项依据：砍掉科普前戏，执行「倒三角四段切入法」
- **严禁写法：** 前一页半从“国家十四五战略、新质生产力、人工智能浪潮”写起，向领域顶尖函评专家科普本学科常识。
- **倒三角切入法：**
  1. **第一段（真实工程/临床硬约束）：** 3~5 句话直接锚定具体场景下的失稳、漏检、能耗或收敛失效现象及量化损失。
  2. **第二段（现有主流范式的机理天花板）：** 按学术机理分类评述国内外代表性工作，精准指出“前人方法在什么数学假设或物理条件下失效，根源是什么”。
  3. **第三段（核心科学假说与突破口）：** 亮出本项目的**科学假说（Hypothesis）**——即引入什么新映射/新守恒量/新耦合机制可打破上述死结。
  4. **第四段（前期预实验锚点）：** 用课题组已验证的初步现象或预实验曲线证明假说并非空想，顺势导出研究目标。

### 4.2 拟解决的关键科学问题：严防「把工程活写成科学问题」
AI 生成本子最致命的硬伤是将**技术实现难点（How to build）**包装成**关键科学问题（Why / What mechanism governs）**。

| ❌ 典型 AI 伪科学问题（实为工程任务或空话） | ✅ 去 AI 味后的真科学问题（机理、耦合规律与数学边界） |
|:---|:---|
| 如何构建一个多模态深度融合的高精度智能诊断平台？ | **异构模态特征在非对齐采样率与缺失退化条件下的互信息守恒边界与自适应校准机理。** |
| 如何收集大规模高质量工业缺陷数据并解决样本不均衡痛点？ | **极小样本长尾分布下生成先验向判别流形迁移时的模式坍缩动力学规律与偏差抑制机制。** |
| 如何实现大模型在边缘端设备上的全方位降本增效与闭环赋能？ | **混合精度低比特量化噪声在深层自注意力传播中的误差累积上界与高曲率通道补偿机制。** |

**结构黄金律：** 全书聚焦 **1 个统领性核心科学问题**，拆解为 **2~3 个层层递进的关键科学问题**，且与后续「研究内容（3~4 项）」严格形成多对一或一对一闭环映射。

### 4.3 研究方案与可行性分析：消灭「形容词支票」
- **AI 假方案：** 「搭建系统化的多维测试验证环境，采用先进的优化策略对模型进行全方位调优，确保系统具备高鲁棒性。」
- **人工真方案：** 「构建基于双机械臂（Franka Research 3）与事件相机（Prophesee EVK4）的硬件在环测试台；固定光照照度（5 lux ~ 10,000 lux 四档）与运动模糊速度（0.5~3.0 m/s），对比本文方法与三类基线在闭环抓取成功率及 2 ms 控制周期抖动率上的定量差异；若单步凸松弛在极端遮挡下不收敛，启用备选李雅普诺夫屏障函数投影保底。」

---

## 5. LaTeX-Safe Prose & Source Hygiene (`LaTeX 源码无损改写规范`)

When humanizing `.tex` manuscripts directly, prose edits that break compilation or corrupt citations are unacceptable. Enforce these 8 hard invariants:

1. **Citation & Cross-Reference Integrity:** Never drop, rename, merge, or invent keys inside `\cite{...}`, `\citet{...}`, `\citep{...}`, `\ref{...}`, `\eqref{...}`, `\autoref{...}`, or `\label{...}`. Keep `\citet{vaswani2017attention}` (textual subject) distinct from `\citep{vaswani2017attention}` (parenthetical).
2. **Non-Breaking Ties (`~`):** Preserve and enforce non-breaking spaces before numbers and references (`Section~\ref{sec:method}`, `Table~\ref{tab:main}`, `Fig.~\ref{fig:overview}`, `Theorem~\ref{thm:bound}`, `32~GB`) to prevent ugly line-start orphan numbers.
3. **Zero Raw Unicode Punctuation Corruption:**
   - Never inject Unicode curly quotes (`“ ” ‘ ’`), Unicode em dashes (`—`), or invisible non-breaking Unicode spaces (`U+00A0`, `U+200B`) into `.tex` source—they break `pdflatex` or render as black boxes/garbled glyphs.
   - Follow our prose em-dash ban: replace `---` / `—` sentence pivots with periods, commas, colons, or parentheses rather than leaving `---` crutches scattered across paragraphs.
   - For intentional quotation marks in LaTeX, use `` ``...'' `` and `` `...' ``.
4. **Percent & Special Character Escaping:** Whenever converting *"24 percent"* to numerals during tightening, write `24\%`—never unescaped `24%`, which silently comments out the rest of the LaTeX line and eats closing braces `}`! Escape `\&` and `\_` outside math/verbatim blocks.
5. **Math Environment Immunity:** Never rewrite variable names, indices, or operators inside `$...$`, `\[...\]`, `equation`, `align`, or custom theorem macros unless explicitly asked to fix math notation. Keep prose variables wrapped in math mode (`$N$ layers`, `$k$-nearest neighbors`, `$L_2$ norm`, never raw `L2` or plain `N`).
6. **Comment Preservation:** Leave `% TODO` author notes and commented-out `\iffalse ... \fi` blocks untouched unless asked to clean camera-ready source for arXiv upload.

---

## 6. Anti-Overcorrection Guardrails for Academic Writing

Do **not** blindly apply blog/social-media humanization rules to peer-reviewed manuscripts:

- **No Contractions in Formal Papers:** Keep *do not, cannot, does not, is not* in IEEE/ACM/Springer/NeurIPS manuscripts (unless writing an invited informal Communications of the ACM viewpoint).
- **No Fake Conversational Openers:** Never insert *"Honestly,"*, *"Look,"*, *"You might wonder,"*, or dramatic 2-word sentence fragments (*"Big mistake."*) into a scientific paper.
- **Keep Technical Term Repetition Exact:** Never cycle synonyms for defined mathematical objects (`node` / `vertex` / `entity`, or `loss` / `objective` / `criterion` / `penalty`) just for variety—pick one canonical term and keep 100% consistency from Section 1 to Appendix Z.
- **Respect Neutral Hedging Where Epistemically Required:** When interpreting observational correlations or empirical conjectures without proof, a single precise epistemic verb (*"suggests"*, *"is consistent with"*, *"empirically tracks"*) is good science—only *stacked* AI hedging (*"could potentially seem to somewhat suggest"*) is slop.
