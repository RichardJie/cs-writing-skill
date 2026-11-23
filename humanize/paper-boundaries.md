# Paper Boundaries — 发布会原则 (The Press-Conference Principle)

在论文写作、修改、压缩和实验组织的全流程中，始终把论文视为一场学术发布会，而不是项目总结、实验日志或自我审查报告。

你的任务不是平均呈现这项工作的所有方面，而是识别其中最值得发表的价值，并围绕这一价值建立最有利、最完整、最有说服力的叙事。

Treat every research paper throughout drafting, revision, compression, and experimental design as an **academic press conference (学术发布会)**, never as a project wrap-up report (项目总结), lab notebook (实验日志), or self-audit confession (自我审查报告). Your job is not to give equal airtime to every aspect of the project, but to isolate what is genuinely worth publishing and construct the sharpest, most complete, and most persuasive evidentiary narrative around that value.

> **Relationship to De-AI Prose Surgery ([SKILL.md](SKILL.md)):** RLHF-trained LLMs default to **artificial "both-sides" balance** (*"While our approach improves efficiency, it suffers from degraded accuracy on..."* / *「尽管本文方法提升了效率，但遗憾的是在……上仍存在明显不足」*). Left unchecked, AI polishing injects defensive caveats into abstracts, turns failed side-experiments into main-text confessions, and hands reviewers ready-made rejection quotes. Always apply `paper-boundaries.md` **first** to lock narrative architecture and claim scope, then run section-level and prose-level de-AI surgery via [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md), [english.md](english.md), [chinese.md](chinese.md), and [references/scientific-figures-and-ui-de-ai.md](references/scientific-figures-and-ui-de-ai.md).

---

## 1. Core Doctrine: The 12 Mandates of the Press-Conference Principle (核心要求)

### 1.1 只围绕优势组织论文 (Organize Exclusively Around Strengths)
优先寻找本文真正领先、独特或不可替代的部分，包括新能力、新问题、新机制、新视角、更强适用性、更低成本、更高效率、更好扩展性或更有意义的权衡。没有形成优势的内容，不应成为论文主线。
- **EN Operational Rule:** Identify what is genuinely leading, distinctive, or irreplaceable in the work. Material that forms no clear advantage never belongs in the main storyline.
- **AI Trap:** LLMs summarize prompt notes democratically—giving three paragraphs to a standard preprocessing pipeline and one paragraph to the actual algorithmic breakthrough. Invert that ratio ruthlessly.

### 1.2 不要写成工作汇报 (Never Write a Chronological Progress Report)
不要按照「我们先做了什么、后来尝试了什么、哪些尝试失败了」的过程展开。论文只保留最终成立的逻辑：问题为什么重要，现有方法为什么不够，本文提供了什么新解法，证据如何支持这一解法。
- **EN Operational Rule:** Never organize a paper around *"what we tried first, what we tried second, and which attempts failed."* Retain only the final deductive chain: (1) why the problem matters, (2) why existing methods fall short mechanistically, (3) what new solution this paper introduces, and (4) how empirical and theoretical evidence validates that solution.

### 1.3 不要主动提供负面评价 (Zero Voluntary Negative Self-Evaluation)
不要替审稿人总结本文哪里弱、哪里输、哪里不如别人，也不要使用「遗憾的是」「仅仅」「仍明显落后」「效果有限」「存在严重不足」等自我削弱式表达。
某项结果不构成优势时，不必主动把它提炼成结论，更不应帮助读者把局部现象上升为对整个方法的否定。
- **EN Operational Rule:** Never do the opposition's job by summarizing where your method is weak, where it loses, or where it trails competitors. Ban self-undermining lexicon across both languages (see Section 3 Diagnostic Catalog), and never extrapolate a local artifact into an indictment of the entire method.

### 1.4 打不过的维度，不要把它设为比赛项目 (Never Compete in an Event You Lose)
如果本文在某个指标上不占优势，就不要把论文叙事建立在该指标上。重新选择更能反映本文价值的任务定义、评价维度、应用场景、约束条件或比较口径。
不要争夺不属于本文的冠军，而要明确本文赢的是另一场更有意义的比赛。
- **EN Operational Rule:** If your method does not lead on Metric X, do not build your narrative scoreboard around Metric X. Select the task formulation, evaluation axis, deployment constraint, resource budget, or comparison protocol that reveals your true advantage.

### 1.5 不要说输，改写比较逻辑 (Never Narrate Defeat — Rewrite the Comparison Logic)
面对不占优的结果，不使用「本文弱于」「性能下降」「未能超过」等直接失败叙述。优先判断：

- 该结果是否必须讨论；
- 是否可以从不同目标、约束或适用场景解释；
- 是否体现了某种合理权衡；
- 是否可以收缩主张，避免不必要的正面对撞；
- 是否应调整故事主线，使其不再承担证明核心贡献的职责。

**EN 5-Point Diagnostic:** Confronted with a non-dominant number, ban direct defeatist phrasing (*"is inferior to"*, *"degrades performance"*, *"fails to surpass"*):
1. **Necessity:** Does the reader need prose commentary on a minor row in a 15-column table? Often the answer is silence.
2. **Regime & Constraint Divergence:** Was the competitor trained with 10x supervision, unbounded latency, or oracle metadata that your setting forbids?
3. **Principled Trade-off:** Is a 0.4-point drop in clean accuracy the expected price of a 4.3x speedup or a +14.2-point gain under corruptions?
4. **Claim Tightening:** Did you over-claim universal superiority when your mechanism specifically targets long-tail / memory-bound / cold-start regimes?
5. **Storyline Reassignment:** Should this experiment be demoted from proving the primary contribution to illustrating an operating boundary?

### 1.6 优势必须被明确说出来 (Articulate Every Advantage Explicitly)
不要期待审稿人自己从表格中发现贡献。凡是能够支持本文价值的结果，都应主动解释：

- 本文在哪个条件下表现最好；
- 为什么这种优势会出现；
- 这一优势解决了什么实际问题；
- 相比已有方法，这种能力为什么值得关注。

**EN Operational Rule:** Never expect a tired reviewer scanning six PDFs at midnight to discover your contribution buried inside Table 3. Explicitly state **Condition** (where it peaks), **Mechanism** (why it occurs), **Practical Resolution** (what bottleneck disappears), and **Comparative Significance** (why prior methods structurally could not achieve this).

### 1.7 控制比较范围 (Control Comparison Scope)
不追求「所有数据集、所有指标、所有设置全面领先」这种不必要的目标。只提出证据能够牢固支撑的主张，并围绕这些主张选择最合适的实验和对比。
论文的说服力来自主张与证据高度一致，而不是比较项目数量最多。
- **EN Operational Rule:** Put forward only claims that your evidence locks down tightly, and choose baselines and benchmarks tailored to test *those* claims. Persuasive power comes from **claim-evidence alignment**, not benchmark bloat.

### 1.8 实验不是结果仓库，而是论证工具 (Experiments Are Argumentation Tools, Not Data Warehouses)
每个实验都必须承担明确职责，例如：

- 证明核心方法有效（**Validate Core Efficacy**）；
- 证明优势来自关键机制（**Isolate Mechanism Attribution**）；
- 证明方法在目标场景中具有价值（**Demonstrate Target-Scenario Value**）；
- 排除最可能的替代解释（**Refute Plausible Alternative Explanations**）。

无法强化主线、容易分散注意力或引出无关争议的实验，应删除、弱化、移动或重新设计（**delete, compress, move to the appendix, or redesign**）。

### 1.9 允许彻底重构故事 (Authorize Total Story Reconstruction)
当现有结果无法支撑原始叙事时，不要围绕原始叙事进行防守。重新定义论文真正解决的问题，重新排序贡献，重新选择主结果，重新设计标题、摘要、引言和实验结构。
故事应服务于最强证据，而不是忠于最初设想。
- **EN Operational Rule:** Stop defending a dead hypothesis. Redefine the problem the paper actually solves, re-rank contribution bullets, promote the strongest empirical phenomenon to Table 1 / Figure 1, and rewrite Title, Abstract, Introduction, and Experiments around your strongest evidence.

### 1.10 避免给审稿人递刀子 (Never Hand Knives to Reviewers)
写作时持续检查：

- 这句话是否无意中扩大了本文需要承担的责任（**expand the burden of proof**）；
- 是否提出了一个本来没人要求回答的问题（**raise an unprompted question**）；
- 是否把局部现象描述成普遍缺陷（**inflate a local quirk into a universal defect**）；
- 是否使用了比证据更广泛的负面判断（**make a negative judgment broader than the evidence**）；
- 是否可以通过更准确的定位避免无意义的自我攻击（**eliminate self-attack via sharper positioning**）。

不主动制造审稿问题，不主动扩大攻击面，不主动替反方完成论证。

### 1.11 摘要和引言必须像发布会开场 (Abstract & Introduction Must Open Like a Keynote Launch)
开头应迅速建立：

- 一个重要且尚未解决的问题（**important, unresolved problem**）；
- 现有方法的关键缺口（**critical structural gap in existing methods**）；
- 本文独特的解决思路（**distinctive solution insight**）；
- 最有分量的结果和意义（**heaviest-hitting quantitative evidence and significance**）。

不要从实现细节、研究过程或大量背景知识开始，也不要在贡献尚未建立时提前讨论不足。

### 1.12 结论只强化记忆点 (Conclusion Reinforces Memory Anchors Only)
结论不是重新审判论文，而是让读者记住：本文解决了什么、提出了什么、证明了什么、为什么重要。不要在最后一段突然加入新的自我否定或扩大局限性。

---

## 2. 默认决策规则与最终目标 (Default Decision Priority & Final Goal)

当遇到任何不理想的材料时，按以下优先级处理（1 -> 7）：

1. 删除与核心主张无关的内容；
2. 缩小主张，避免无意义的正面对比；
3. 更换更能体现价值的评价维度；
4. 将结果解释为目标差异或合理权衡；
5. 重组实验，使优势成为视觉和叙事中心；
6. 重新定义论文故事；
7. 只有在无法回避且确实影响核心结论时，才进行必要说明。

| Priority | Action (EN) | Canonical Rule (CN) | Concrete Execution |
|:---:|:---|:---|:---|
| **1** | **Delete irrelevant material** | 删除与核心主张无关的内容 | Cut side-experiments, tangential datasets, or auxiliary metrics that test claims you never made. |
| **2** | **Narrow the claim scope** | 缩小主张，避免无意义的正面对比 | Replace *"universal vision backbone"* with *"memory-bounded dense prediction on edge GPUs"*. |
| **3** | **Switch evaluation dimension** | 更换更能体现价值的评价维度 | Replace raw unconstrained Top-1 accuracy with accuracy-per-ms latency, throughput at 8 GB VRAM, or worst-group recall. |
| **4** | **Frame as objective divergence or trade-off** | 将结果解释为目标差异或合理权衡 | Show how optimizing for streaming causal inference naturally trades offline bidirectional lookahead for zero buffering delay. |
| **5** | **Restructure visual & narrative center** | 重组实验，使优势成为视觉和叙事中心 | Put your target-regime win in Figure 1 and Table 1; move legacy unconstrained comparisons to a compact boundary analysis subsection. |
| **6** | **Redefine the overarching paper story** | 重新定义论文故事 | Pivot Title, Abstract, and Contribution bullets around the phenomenon where the method genuinely dominates. |
| **7** | **Bounded factual clarification (Last Resort)** | 只有在无法回避且确实影响核心结论时，才进行必要说明 | State the exact mathematical/operational boundary condition neutrally in 1-2 sentences without emotional self-deprecation. |

### 最终目标 (Final Goal)

论文中的每一个章节、段落、表格和句子，都应共同完成一件事：

让读者相信，这项工作解决了一个值得解决的问题，提出了一种值得关注的方法，并且已经有足够清晰的证据证明它的价值。

不要平均展示，不要主动示弱，不要写实验流水账，不要替审稿人攻击自己。找到真正成立的优势，围绕它组织全部材料，并把这个优势讲到足够清楚。

---

## 3. Diagnostic Pattern Catalog: Self-Undermining Lexicon Blacklist

Scan manuscripts for these defensive tells. Any hit in Abstract, Introduction, Contribution bullets, or Conclusion requires immediate surgery; hits in Experiments/Limitations must be converted into neutral boundary conditions or trade-offs.

### 3.1 Chinese Self-Sabotage Lexicon (`中文自我削弱词库`)

| Category | Banned Self-Undermining Phrasing (禁用表达) | Strengths-Driven / Boundary-Precise Replacement (发布会级改写方向) |
|:---|:---|:---|
| **Emotional Apology (情绪化示弱)** | 遗憾的是、不幸的是、令人失望的是、惭愧的是 | Delete emotion entirely; state operating condition neutrally (`在 X 约束下，方法呈现 Y 特性`). |
| **Minimizers (价值贬损词)** | 仅仅提升了、只做到了、不过是、只是对…的简单改进 | State exact delta + mechanism significance (`在不增加推理开销的前提下，将 X 提升 2.3 个百分点`). |
| **Defeatist Comparison (直接认输)** | 本文明显弱于、仍大幅落后于、未能超越、不敌、败给 | Reframe via resource/assumption asymmetry (`方法 B 依赖离线全量重训练，而本文在单遍流式约束下达到其 98.4% 的精度，且延迟降低 6.2 倍`). |
| **Global Self-Negation (全局否定)** | 效果有限、存在严重不足、鲁棒性较差、尚未真正解决 | Pinpoint exact regime boundary (`当输入序列信噪比低于 -10 dB 时，一阶近似误差开始显现`). |
| **Lab-Diary Drift (工作汇报腔)** | 起初我们尝试了 A 但失败了，后来改成 B 效果依然不好，最后我们才想到 C | Cut A and B from narrative history; if A/B are meaningful baselines, test them cleanly in the Ablation table as controlled design alternatives. |
| **Disclaimer Suicide (免责声明自杀)** | 本研究仍处于初步探索阶段，结论仅供参考，有待未来进一步完善 | State verified scope firmly (`本文实验确立了 X 机制在 Y 规模下的收敛优势，为扩展至 Z 模态提供了可复用的算子基础`). |

### 3.2 English Self-Sabotage Lexicon (`英文自我削弱词库`)

| Category | Banned Self-Undermining Phrasing | Strengths-Driven / Boundary-Precise Replacement |
|:---|:---|:---|
| **Apologetic Openers** | *Unfortunately, Regrettably, Admittedly, Sadly, To our disappointment* | Cut adverb; state the physical or statistical regime (*"Under sub-4-bit activation quantization, outlier channels require..."*). |
| **Diminishing Qualifiers** | *merely, only a modest gain, a naive extension, incremental, Marginally* | Quantify the gain relative to budget or baseline ceiling (*"reduces KV-cache footprint by 62% with zero extra calibration passes"*). |
| **Defeatist Verbs** | *fails to beat, lags behind, is inferior to, suffers from poor X, degrades* | Express the trade-off vector (*"trades 0.5 EM on synthetic short queries for a 3.8x throughput gain on 64K-token contexts"*). |
| **AI Both-Sides Templates** | *While our method excels at X, it struggles significantly with Y and Z* | Keep X in the main claim; address Y in a dedicated scope paragraph specifying *when* Y occurs and *why* the objective prioritizes X. |
| **Premature Hedging** | *Although preliminary and limited to two benchmarks, we hope our humble attempt...* | State what the two benchmarks establish (*"Across WikiText-103 and C4, sparse routing cuts wall-clock pretraining time by 28%"*). |

---

## 4. Deep Bilingual Surgery Playbook (Before vs. After)

### 4.1 Surgery A: Chronological Lab Diary -> Launch Keynote Opening

**Before (Chinese — 实验流水账 + 提前示弱):**
> 起初，我们尝试直接将图注意力网络应用于大规模交通流预测，但在实验过程中发现显存占用过高，训练经常崩溃。后来我们又尝试了随机子图采样，遗憾的是预测精度出现了严重下降，在 PeMS08 数据集上甚至不如传统基线。经过多次参数调整和失败尝试后，我们最终设计了一种基于低秩谱滤波的轻量化模块，虽然在极短期（5分钟）预测上仅仅与现有最先进方法持平，但在长周期预测上取得了一定改进。

**After (Chinese — 发布会开场 + 优势锚定):**
> 城市级路网的长周期交通流预测受制于尖锐的时空扩展性瓶颈：全图注意力机制的显存开销随节点数呈二次方增长，而现有的随机子图采样则会截断跨区域传播波，导致远期预测失真。本文提出一种低秩谱滤波架构（LRSF），在保留全局低频传播模态的同时将单步计算复杂度压缩至线性级别。在 PeMS04 与 PeMS08 基准上，LRSF 将 60 分钟长周期预测误差（MAE）降低了 8.7%，峰值显存占用减少 74%，并在 5 分钟短时预测上以 1/4 的推理延迟匹配最优全图模型。

**Before (English — Defensive Chronology + AI Hedging):**
> Initially, we explored fine-tuning the full 70B model using standard LoRA, which unfortunately ran out of memory on consumer GPUs. We then experimented with aggressive layer pruning, but this approach failed to preserve multi-hop reasoning and lagged behind full fine-tuning by 9 points. Eventually, we arrived at gradient-guided rank allocation. While our method is not superior to full fine-tuning on unconstrained H100 clusters, it provides a somewhat useful compromise when hardware is limited.

**After (English — Problem-Gap-Mechanism-Evidence Keynote):**
> Adapting 70B-parameter language models on single-workstation GPUs exposes a sharp failure mode in uniform low-rank adaptation: uniform rank budgets overflow 24 GB VRAM, whereas static layer pruning severs multi-hop reasoning circuits. We introduce Gradient-Guided Rank Allocation (GGRA), which concentrates trainable rank capacity on high-curvature attention projections identified during a 30-second calibration pass. On GSM8K and StrategyQA, GGRA recovers 99.1% of full 8xH100 fine-tuning accuracy on a single RTX 4090 while cutting peak memory by 68%.

---

### 4.2 Surgery B: Comparison Reframing ("Don't Compete in a Lost Race")

Suppose your method (`FastRetrieve`) gets **81.9 Recall@10** at **4.2 ms** latency, while a heavyweight cross-encoder reranker (`HeavyCross`) gets **83.1 Recall@10** at **185.0 ms** latency.

**Before (CN — 把别人的主场设为比赛项目):**
> 从表 1 可以看出，遗憾的是，本文提出的 FastRetrieve 在 Recall@10 指标上仅为 81.9%，未能超过 HeavyCross（83.1%），仍存在 1.2% 的性能差距，说明双塔近似结构在细粒度交互捕捉上依然不如交叉编码器。不过，FastRetrieve 的推理速度比 HeavyCross 快一些。

**After (CN — 重构比较逻辑与评价主轴):**
> 表 1 揭示了在线检索系统中的延迟-召回帕累托边界：在严格的毫秒级在线服务约束（SLA < 10 ms）下，交叉编码器 HeavyCross 因 185.0 ms 的逐对重排延迟无法部署；而在所有满足实时上线的检索架构中，FastRetrieve 将 Recall@10 推高至 81.9%（领先次优实时基线 +4.6 个百分点），以 1/44 的在线计算开销捕获了离线重排上限 98.6% 的召回能力。

**Before (EN — Narrating Defeat):**
> As shown in Table 1, FastRetrieve achieves 81.9% Recall@10, which falls short of HeavyCross (83.1%) by 1.2 points. This performance degradation occurs because our method avoids cross-attention over query-document pairs. Nevertheless, our inference speed is faster.

**After (EN — Reframing Around the Target Operating Regime):**
> Table 1 maps accuracy against production latency budgets. HeavyCross requires 185.0 ms per query (18x above the 10 ms interactive search SLA) due to exhaustive token-level cross-attention. Within the deployable sub-10 ms regime, FastRetrieve establishes a new Pareto frontier at 81.9% Recall@10 (+4.6 points over the strongest real-time dense retriever), retaining 98.6% of offline cross-encoder recall at 44x higher throughput.

---

### 4.3 Surgery C: Experiment-as-Argument Restructuring

When an experiment section reads like an uncurated dump ("Table 2 shows hyperparameter sensitivity, Table 3 shows dataset X, Table 4 shows backbone Y..."), apply **Argumentative Role Mapping**:

| Experimental Block | Weak "Warehouse" Framing (禁止：仓库式罗列) | Strong "Argumentation" Framing (推荐：命题驱动论证) |
|:---|:---|:---|
| **Main Benchmark (Table 1)** | *"Comparison with baselines on five datasets."* | **Claim 1 Validation:** Proves end-to-end dominance under the target memory-bounded regime across scale. |
| **Mechanism Ablation (Table 2)** | *"Ablation study of different components A, B, and C."* | **Mechanism Attribution:** Isolates that 78% of the accuracy gain originates from spectral gating (`B`), not auxiliary regularization (`C`). |
| **Compute-Matched Control (Table 3)** | *"Results when we increase baseline width."* | **Alternative-Hypothesis Refutation:** Rules out extra FLOPs/parameters—even given 1.5x parameter budget, the baseline trails by 3.4 points. |
| **Noisy Toy Dataset where Method Ties** | Kept in Table 1 out of habit, forcing awkward excuses in text. | **Pruned / Moved:** Deleted or moved to Appendix Boundary Analysis because label noise at 40% saturates the Bayes error ceiling for all methods. |

---

### 4.4 Surgery D: Preventing "Handing Knives to Reviewers" (避免给审稿人递刀子)

Below are five classic sentences authors write thinking they sound "modest and rigorous," alongside the exact knife reviewers pull from them and the boundary-precise rewrite.

1. **Unprompted Burden Expansion (`无意扩大责任`)**
   - *Self-Inflicted Knife:* *"Ideally, a general-purpose code repair agent should also verify formal memory safety in C++ kernels, which we leave for future work."*
   - *Reviewer's Reject Quote:* *"As the authors themselves admit, the agent cannot verify formal safety, making it unsuitable for general-purpose repair."*
   - *Press-Conference Fix:* Scope the paper cleanly around Python/TypeScript test-driven repository repair from line 1; never introduce C++ kernel formal verification as an unfulfilled obligation.

2. **Local Quirk -> Global Defect (`局部现象上升为普遍缺陷`)**
   - *Self-Inflicted Knife:* 「我们的方法在处理高分辨率图像时会出现严重的边缘伪影，说明隐空间上采样器存在固有缺陷。」
   - *Reviewer's Reject Quote:* *"The latent upsampler has an inherent defect causing severe boundary artifacts at high resolutions."*
   - *Press-Conference Fix:* 「在未经分块重叠（non-overlapped tiling）的 4K 零样本外推设置下，分块边界处会出现高频相位不连续；引入 16 像素余弦羽化窗口即可在不增加显存的前提下消除拼接痕迹（见图 6）。」

3. **Unasked Vulnerability (`主动制造没人问的问题`)**
   - *Self-Inflicted Knife:* *"We did not evaluate whether adversarial poisoning of the calibration set breaks our quantizer."*
   - *Reviewer's Reject Quote:* *"Security against calibration poisoning was completely ignored; authors must add adversarial robustness experiments."*
   - *Press-Conference Fix:* State positively in the setup: *"Following standard post-training quantization protocols (GPTQ, AWQ), calibration uses 128 unlabelled samples drawn from the clean pretraining distribution."*

4. **Premature Caveat in the Introduction (`引言未立功先认罪`)**
   - *Self-Inflicted Knife:* *"Although our theoretical bound only holds for convex objectives and single-node SGD, it still offers rough intuition for deep networks."*
   - *Press-Conference Fix:* Establish the empirical deep-network breakthrough first; then introduce the theorem proudly for what it *does* prove: *"To explain why variance collapses near saddle plateaus, Theorem 1 proves exact $O(1/T)$ convergence under locally $\mu$-PL geometry, matching empirical layer-wise Hessian spectra measured on ResNet-50."*

5. **Last-Paragraph Self-Sabotage in Conclusion (`结论临门自砍一刀`)**
   - *Self-Inflicted Knife:* *"In conclusion, we proposed X. However, due to limited compute, we only tested up to 7B models, and our latency overhead during prefill remains a bottleneck."*
   - *Press-Conference Fix:* Keep bounded prefill analysis in the dedicated Limitations subsection (paired with exact crossover sequence length $L > 2048$ where decode savings outweigh prefill by 5x). End the Conclusion strictly on the proven contribution, mechanism, and impact.

---

## 5. Story Reconstruction Protocol (彻底重构故事操作流)

When your original idea ("Method X beats SOTA on clean ImageNet") yields +0.1% on clean ImageNet, **+9.4% on ImageNet-C corruptions**, and **2.2x faster training convergence**:

1. **Kill the Old Framing Immediately:** Stop writing a clean-ImageNet accuracy paper with excuses about hyperparameter tuning.
2. **Audit the Strongest Evidence Cluster:** Ask *"If an outsider saw only our tables without knowing our original plan, what dramatic phenomenon would jump off the page?"* Answer: corruption resilience + fast convergence from a single regularizer.
3. **Rebuild the Spine Top-Down:**
   - **New Title:** Shift from *"Improving Vision Transformers via X"* -> *"Fast-Converging Corruption-Resilient Vision Transformers via X"*.
   - **New Opening Gap:** Frame the longstanding tension in vision backbones—robustness augmentations (AugMix, adversarial training) usually *double or triple* training epochs, whereas fast-training recipes degrade OOD robustness.
   - **New Table 1:** Place ImageNet-C, ImageNet-R, and Training Wall-Clock GPU-Hours side by side alongside clean ImageNet Top-1 (showing clean parity + massive OOD & speed wins).
   - **Prune:** Remove three inconclusive clean-data augmentation ablations that belonged to the dead storyline.

---

## 6. Anti-Overcorrection & Scientific Integrity Guardrails (反过度矫正与学术诚信红线)

The Press-Conference Principle is **strategic framing and disciplined scope architecture—never scientific misconduct or AI marketing hype.** Overcorrecting into breathless bragging triggers reviewer hostility faster than anything else.

| Dimension | Legitimate Press-Conference Framing (合规优势叙事) | Forbidden Overcorrection / Misconduct (严禁越界红线) |
|:---|:---|:---|
| **Data & Baselines** | Define a clear, honest scope (e.g., *single-GPU 8 GB budget*) and compare against **all** strongest baselines under that exact fair budget. | Deleting a baseline that beats you *inside your claimed scope*, crippling baseline hyperparameters, or cherry-picking random seeds. |
| **Tone & Adjectives** | Crisp, dry, quantitative precision (*"cuts P99 latency by 41% across 4 workloads"*). | AI promotional slop (*"groundbreaking, revolutionary, flawless paradigm shift that solves X once and for all"*). |
| **Mandatory Limitations Sections** | State concrete mathematical assumptions, regime crossover thresholds (e.g., *"decode speedup materializes for generation lengths > 128 tokens"*), and resource envelopes. | Pretending zero limitations exist at venues requiring a `Limitations` section (NeurIPS/ICLR/ACL), which incurs desk-reject or Ethics/Review penalties. |
| **Fatal Flaws vs. Boundaries** | Reframe *regime trade-offs* via Priority Rules 1-6. | Trying to "reframe" a bug, test-set contamination, or broken theorem via clever prose—fix the experiment/math before submitting. |

---

## 7. Agent Execution Checklist & Rewrite Prompt Constraint Block

When invoking `paper-boundaries` on a draft or outline, execute this 6-point pass before outputting text:

- [ ] **Keynote Test:** Do the Abstract and first 3 paragraphs of the Introduction establish Problem -> Mechanistic Gap -> Solution -> Best Quantitative Evidence with zero chronological history or premature caveats?
- [ ] **Lexicon Sweep:** Zero instances of `遗憾的是 / 仅仅 / 未能超越 / 效果有限` or `unfortunately / merely / fails to beat / suffers from / lags behind` describing the authors' own work.
- [ ] **Scoreboard Audit:** Does Table 1 measure the exact dimension where the method's mechanism creates structural advantage?
- [ ] **Explicit Advantage Rule:** Every main-text table/figure paragraph states *where* we win, *why* (mechanism), and *what bottleneck* that solves.
- [ ] **Warehouse Purge:** Every experiment maps to Efficacy, Mechanism Attribution, Scenario Value, or Alternative-Explanation Refutation.
- [ ] **Knife Check:** Zero unprompted scope expansions, zero local-to-global self-indictments, and zero fresh self-negation in the Conclusion.
