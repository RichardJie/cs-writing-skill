# Academic Slide Languages, Micro-Copy & Bilingual Typography Specification

> **Module Role**: Authoritative linguistic, micro-copy, and typographic execution guide for [`cs-report-ppt`](../SKILL.md). Governs Track 1 (**100% Academic English**), Track 2 (**100% Simplified Chinese — 中文学术汇报**), and Track 3 (**CN-EN Bilingual Hybrid — 中英双语混合组会/国际合作汇报**), integrating seamlessly with [`typography_rules.md`](typography_rules.md), [`omml_syntax_guide.md`](omml_syntax_guide.md), and [`palettes-and-layouts.md`](palettes-and-layouts.md).

---

## 0. Track Selection & Language Routing Matrix

Before writing a single slide title or generating presentation code, lock the deck's linguistic track from user intent or scenario defaults:

| Linguistic Track | Config Token | Target Scenarios | Slide Text Language | Paper Asset / Terminology Policy | Dialogue Language |
|:---|:---|:---|:---|:---|:---|
| **Track 1: 100% Academic English** | `en_academic` | International conferences (NeurIPS, CVPR, ACL, Nature/Science seminars), English journal clubs, faculty job talks | **100% Formal Academic English** (zero Chinese glyphs on canvas) | Original paper figures, English labels, standard mathematical notation | Follows user prompt language (default: 简体中文) |
| **Track 2: 100% Academic Chinese** | `zh_academic` | 硕士/博士毕业答辩、开题/中期考核、国自然(NSFC)/重点研发立项与结题、国奖/优博答辩、中文课题组周报 | **规范学术简体中文**（去Word化动宾/结论短句） | 保留高共识专业英文缩写与模型/数据集/指标原名；中西文双字体显式绑定 | 100% 简体中文 |
| **Track 3: CN-EN Bilingual Hybrid** | `zh_en_hybrid` | 国内实验室英文顶会论文精读组会（Paper Reading）、跨国联合课题组技术对齐 | **中文结论主标题 + 中文凝练解读要点**，保留英文原图/原表及核心英文术语锚点 | 原版 PDF 高清英文图表直嵌（严禁机翻重绘原图破坏精度）+ 中文互文批注 | 100% 简体中文 |

> [!IMPORTANT]
> **Track Purity Law**: Never drift tracks mid-deck. In `en_academic`, not a single Chinese character or full-width punctuation mark (`，。：（）`) may appear on any slide. In `zh_academic`, ban "散装外企中英夹杂腔" (e.g., *"我们 base 在 baseline 上做 trade-off 去 boost 性能"*); only canonical domain terms and formal acronyms stay in English.

---

## 1. Track 1: 100% Academic English (`en_academic`)

Academic English slides fail in two opposite ways: **teleprompter walls of text** (copy-pasted paper abstracts) or **content-free corporate slogans** (*"Experimental Results"*, *"Key Insights"*). Track 1 enforces **Assertion-Evidence Headlines + Anchored Micro-Bullets ($\le 12$ words) + Screen-Calibrated Sans/Math Typography**.

### 1.1 Assertion-Evidence Claim Headlines (Alley & Doumont Standard)

Pioneered by Michael Alley and Jean-luc Doumont, the **Assertion-Evidence** model replaces passive topic labels with **falsifiable, empirical claim headlines** backed immediately by visual evidence below.

#### Hard Headline Construction Rules
1. **Complete Empirical Claim, Never a Topic Noun Phrase**:
   - Every content slide (Slides 2–14) must state **what is true, why it happens, or how much it improves**—never merely *what topic is on the slide*.
   - **Formula**: `[Mechanism / Subject] + [Strong Active Verb] + [Target Outcome / Quantified Delta] + [Condition / Bound]`
2. **Word & Character Budget**:
   - **Target**: **8–13 words** ($\le 72$ characters), fitting cleanly on **1 single line** at `24–26pt Bold`.
   - **Hard Ceiling**: **16 words** ($\le 95$ characters), wrapping to **at most 2 lines** (`22–24pt Bold`). If a headline wraps to 3 lines, rewrite or split the slide—never shrink title font below `20pt`.
3. **Alignment & Case Policy**:
   - **Left-aligned** (`align: "left"` at `x = 0.600"`). Centered headlines break the left visual reading axis and waste horizontal span.
   - **Sentence case** for all Assertion-Evidence claim headlines (capitalizing only the first word, proper nouns, and canonical acronyms like `KV`, `LoRA`, `ImageNet`, `AUROC`). Sentence case reads **14–18% faster** in auditoriums than Title Case.
   - **Title Case** is reserved *exclusively* for Slide 1 (the official published paper title) and optional `2–3` word Card Headers.
   - **ALL-CAPS** is **strictly banned** in headlines and body text; permitted *only* inside `9–10pt` section tracker badges (`METHODOLOGY: ARCHITECTURE`).
   - **No terminal period (`.`)** at the end of single-sentence slide headlines.

#### Headline Templates Across the Academic Spine

| Slide Archetype | ❌ Weak Topic Headline (Banned) | ✅ Assertion-Evidence Claim Headline (Required) |
|:---|:---|:---|
| **Motivation / Bottleneck** | `Background and Motivation` | `Dense self-attention scales quadratically, exhausting 80 GB VRAM at 128K context` |
| **Target Research Gap** | `Problem Statement & Limitations` | `Prior KV eviction heuristics drop early sink tokens and collapse multi-hop recall` |
| **Theoretical Guarantee** | `Convergence Analysis` | `Proximal variance reduction achieves linear O(log(1/ε)) convergence without convexity` |
| **System Architecture** | `Proposed Framework Overview` | `Three-stage Dual-Path Router decouples global semantic planning from local token decoding` |
| **Primary SOTA Benchmark** | `Main Experimental Results` | `Ours outperforms FlashAttention-2 by +4.8% EM while cutting end-to-end latency by 37%` |
| **Ablation & Sensitivity** | `Ablation Studies` | `Removing spectral gating degrades OOD robustness by 6.2%, dominating total gain` |
| **Economics / Causal ID** | `DID Regression Table` | `Carbon trading pilot raises firm green patenting by 19.4% with clean pre-trend parallel` |
| **Biomedical / Clinical** | `Survival Analysis` | `Dual PD-1/LAG-3 blockade extends median progression-free survival from 4.7 to 11.3 months` |
| **Critique & Limitations** | `Conclusion and Future Work` | `Gains rely on 8×H100 calibration; INT4 edge quantization remains untested` |

---

### 1.2 `<=12`-Word Micro-Bullets & Semantic Visual-Text Anchoring

When a figure or benchmark table anchors the slide, body text exists **solely to direct the audience's eye** to specific geometric features, inflection points, and table rows.

#### The `<=12`-Word Micro-Bullet Grammar
Every bullet point inside a visual slide card must obey:
$$\underbrace{\textbf{Bold Anchor (1–3 words):}}_{\text{Scannable index}} \; \underbrace{\text{Active Verb + Visual Pointer (Fig./Row) + Quantified Metric}}_{\le 9\text{–}10\text{ words}} \quad (\text{Total } \le 12\text{ words; hard cap } 15)$$

1. **Strip Grammatical Filler**:
   - Drop leading throat-clearers (`It can be observed from Figure 3 that...`, `Notably, our experiments demonstrate that...`, `In order to address this issue, we...`).
   - Drop redundant articles (`the`, `a`, `an`) and auxiliary verbs (`is able to` $\rightarrow$ `can` or active verb) where telegraphic scientific clarity holds.
   - Replace wordy clauses with crisp mathematical/quantitative symbols (`increases by 14.2 percent compared to baseline` $\rightarrow$ `+14.2% vs. baseline`; `from 32 milliseconds down to 9 milliseconds` $\rightarrow$ `32 ms → 9 ms`).
2. **Mandatory Visual Coordinates**:
   - At least **2 bullets per visual slide** must cite explicit visual coordinates inside the embedded asset: `(Fig. 2b, red curve)`, `(Table 1, bottom row)`, `(Stage ②, dashed box)`, `(x > 64K inflection)`.
3. **Parallel Syntactic Cadence**:
   - Within any single card, all bullets must share the **same grammatical lead structure** (all noun-anchor + verb, or all imperative stage verbs). Never mix full conversational sentences, fragments, and questions in one list.

#### Slide & Card Text Density Budgets (`en_academic`)

| Container Type | Max Bullets | Target Words / Bullet | Hard Cap / Bullet | Max Total Body Words on Slide |
|:---|:---|:---|:---|:---|
| **Figure-Dominant Card (`split_65_35` / `62_38`)** | `3` (max `4`) | `8–12 words` | `15 words` | `45–65 words` |
| **Bottom Dissection Card (`panorama_arch` 3-col)** | `2` per card | `7–10 words` | `12 words` | `50–70 words` |
| **Marginal Synergy Callout (`旁注` Sidenote)** | `2–3` | `8–12 words` | `14 words` | `+25–35 words` |
| **Pure Synthesis / Critique Slide (Slide 13–14)** | `3–4` per card | `10–14 words` | `16 words` | `85–110 words` |

#### Before-vs-After Micro-Bullet Surgery

| ❌ Paper-Copy Teleprompter Prose (Banned — 34–42 words) | ✅ `<=12`-Word Anchored Micro-Bullets (Required — 9–12 words) |
|:---|:---|
| *"As illustrated in Figure 4, when the sequence length grows beyond 32K tokens, the baseline Ring-Attention method suffers from severe inter-node AllReduce communication overhead, which causes throughput to drop by more than 54%."* | **32K+ Bottleneck (Fig. 4a):** AllReduce overhead halves Ring-Attention throughput (`-54% tok/s`). |
| *"In Table 2, we perform a comprehensive ablation study by removing each proposed module one by one, and we find that the dynamic anchor selection component contributes the largest improvement of 3.9 F1 points."* | **Dominant Module (Table 2, Row 3):** Dynamic anchor selection drives `+3.9 F1` gain. |
| *"Furthermore, our method requires only 14.2 GB of peak GPU memory during inference, which makes it feasible to deploy directly on a single consumer-grade RTX 4090 graphics card."* | **Single-GPU Fit:** `14.2 GB` peak VRAM enables native RTX 4090 deployment. |

---

### 1.3 Curated English Font Pairings & Typographic Micro-Rules

Never combine decorative serifs, thin hairline weights (`Light 300` below `18pt`), or mismatched math fonts. Choose **one** pairing per deck:

| Pairing ID | Heading Font | Body & Table Font | Math Font (OMML) | Code / Tensor Font | Best Use Case & OS Compatibility |
|:---|:---|:---|:---|:---|:---|
| **`EN-1: Universal Podium Safe` (Default)** | `Arial` (Bold) | `Arial` (Regular) | `Cambria Math` | `Consolas` / `Courier New` | **Zero-substitution guarantee** across Windows, macOS, and Linux `soffice` (`Liberation Sans` metric-identical). |
| **`EN-2: Screen-Engineered Modern`** | `Segoe UI` / `Inter` (Bold/Semibold) | `Segoe UI` / `Inter` (Regular) | `Cambria Math` / `STIX Two Math` | `JetBrains Mono` / `Consolas` | Tall x-height, crisp `Il1` / `0O` disambiguation, native tabular numerals (`tnum`) for dense ML/Systems tables. |
| **`EN-3: Keynote / macOS Stage`** | `SF Pro Display` / `Helvetica Neue` (Bold) | `SF Pro Text` / `Helvetica Neue` | `STIX Two Math` | `SF Mono` / `Menlo` | High-craft Apple Keynote / PDF conference oral presentations. Embed fonts or export PDF if moving to Windows. |
| **`EN-4: Theory & Proof Hybrid`** | `Arial` / `Helvetica Neue` (Bold) | `Arial` / `Segoe UI` (Body); `Georgia` (Formal Theorem Box *only*) | `Cambria Math` / `Latin Modern Math` | `Consolas` | Mathematics, Theoretical CS, Econometrics—distinguishes formal *Theorem 1* statement from sans-serif intuition bullets. |

#### Precision English Micro-Typography Rules
- **True Minus & En-Dash**: Use Unicode minus `−` (`U+2212`) for negative numbers (`−4.2%`, `10⁻⁴`) and en-dash `–` (`U+2013`) for numeric ranges (`Slides 6–9`, `12–15 min`, `pp. 104–118`). Never use ASCII hyphen `-` for minus signs, and ban LLM em-dash (`—`) clause abuse in bullets.
- **SI Unit Non-Breaking Space**: Separate numerals and units with a narrow/non-breaking space (`14.2 GB`, `38 ms`, `300 DPI`), except `%` and `°` (`94.6%`, `45°`).
- **Tabular Numerals in Tables**: Right-align quantitative columns (or decimal-align `±` standard deviations: `84.2 ± 0.4`) so vertical place values align cleanly.
- **No Underlining or All-Italic Paragraphs**: Underline (`<u>`) is reserved exclusively for **runner-up (2nd best) metrics inside SOTA benchmark tables** (where **bold** marks 1st place). Never underline headings or body phrases.

---

## 2. Track 2 & 3: 中文学术汇报与中英双语混排规范 (`zh_academic` & `zh_en_hybrid`)

Chinese academic presentations (博士/硕士毕业答辩、开题与中期考核、国自然 NSFC / 重点研发计划答辩、课题组组会) face unique linguistic and typographic challenges: Word-style paragraph dumping, bureaucratic filler, amateurish CJK built-in Latin glyphs, and smaller optical stroke legibility at low point sizes.

### 2.1 中文学术汇报“去Word化”五步改造手术 (5-Step De-Wordification Surgery)

“Word搬家症”是中文学术 PPT 头号顽疾——直接将学位论文、基金申请书（本子）中的 4–6 行自然段粘贴进文本框，导致评审专家陷入“读字则漏听演讲，听讲则满屏文字干扰”的认知过载。

#### 诊断红线（触发任意一条即强制执行去Word化手术）
1. 任意单个文本框或卡片内出现 **连续 $\ge 3$ 行的完整自然段**（无分点、无粗体锚点）。
2. 句首出现论文式公文套话：`本文针对……问题，`、`为了解决上述挑战，本研究提出了……`、`通过大量的实验验证表明，`、`值得注意的是，`、`综上所述，`。
3. 列表退化为机械序数词堆砌：`首先，……；其次，……；再次，……；最后，……`。
4. 只有定性吹捧形容词（`大幅提升了性能`、`取得了显著的优越性`、`具有极强的鲁棒性`），缺乏具体指标与数值增量。

#### 五步去Word化改造流水线
- **Step 1 — 砍主语与公文套话（Zero Throat-Clearing）**：删除一切“本文/本研究/我们/针对……背景/实验结果表明”等冗余主语和过渡壳子，直奔技术动作或实证结果。
- **Step 2 — 提炼“粗体锚点 + 动宾/主谓结论短句”（Micro-Chunking）**：每条控制在 **14–22 个汉字**（上限 **26 字**），格式统一为 **`核心维度（2–4字）：` + 精炼机制/量化结果**。
- **Step 3 — 逻辑关系结构化（Text-to-Topology）**：
  - 递进/时序关系（“先预处理，再特征提取，最后分类”）$\rightarrow$ 改造成 **横向三阶箭头卡片 (`阶段一 → 阶段二 → 阶段三`)**，禁止竖排纯文字。
  - 优劣对比关系（“传统方法存在A缺点，而本文方法具有B优势”）$\rightarrow$ 改造成 **左右双栏对照卡 (`传统基线瓶颈` vs. `本文方法突破`)**。
- **Step 4 — 量化增益前置与视觉高亮（Metric Front-Loading）**：将藏在段落末尾的数据提炼为粗体或主题强调色（如 `+18.6%`、`延迟降低 3.4×`、`p < 0.001`）。
- **Step 5 — 图表坐标显式互文（Visual Pointer Binding）**：每条文字显式指向旁侧图表的子图编号、曲线颜色或表格行号（如 `见图3b红线`、`表2末行`）。

#### 去Word化实战改造对照表（答辩 / 国自然 / 组会）

| 场景 | ❌ 原版“Word搬家腔”（严禁上屏 — 75~95字段落） | ✅ 去Word化学术精炼版（可直接上屏 — 结构化短条目） |
|:---|:---|:---|
| **博士答辩（研究背景）** | “随着大语言模型上下文长度扩展至百万词元级别，传统全注意力机制的键值缓存（KV Cache）显存占用呈线性激增，在多并发推理场景下极易引发显存溢出瓶颈，严重制约了端侧与单卡部署。” | • **显存线性膨胀（图1a）：** 1M 上下文 KV Cache 高达 `160 GB`，单卡无法承载<br>• **并发吞吐坍塌（图1b）：** 访存带宽受限，Batch>8 时解码延迟激增 `4.6×`<br>• **核心瓶颈定位：** 92% 历史注意力权重集中于不足 `8%` 关键词元 |
| **国自然 NSFC（研究方案）** | “本课题拟首先构建多源异构遥感影像时空对齐数据集，其次设计物理机理约束的扩散生成网络以修复云雾遮挡区域，最后在典型流域洪涝监测业务系统中开展实地验证与示范应用。” | *(改造为三栏横向技术路线卡)*<br>① **构建时空对齐基准库**：融合 SAR 与光学多源影像，覆盖 `12` 个典型流域<br>② **设计物理约束扩散模型**：嵌入辐射传输方程先验，云下重建 PSNR 达 `34.8 dB`<br>③ **开展业务系统实证**：接入流域防汛平台，预警响应缩短至 `15 min` |
| **科研周报（进展与排障）** | “本周我主要阅读了三篇关于对比学习的文献，并且跑了两组在 CIFAR-100 上的预实验，但是发现温度系数调小之后训练后期 Loss 出现了 NaN 震荡，下周打算继续排查梯度爆炸原因。” | • **复现异常定位（图2）：** 温度系数 $\tau < 0.03$ 时，`Epoch 42` 出现 FP16 指数上溢（NaN）<br>• **根因诊断：** 负样本相似度内积超出 `65,504` 半精度上限<br>• **下周闭环动作：** 切换 `BF16` 混合精度 + 引入 LogSumExp 数值稳定项（预计周三验证） |

---

### 2.2 动宾结论式标题规范 (Conclusion Headlines & Symmetric Verb-Object Headers)

中文学术 PPT 的标题分为两级：**页顶主标题（Slide Title）** 与 **卡片/模块小标题（Card / Stage Header）**，二者各司其职、句法严明。

#### 1. 页顶主标题：结论先行句（严禁名词标签）
- **铁律**：严禁使用 `研究背景`、`实验结果与分析`、`第三章 模型设计`、`消融实验` 作为页顶主标题！（章节归属一律放入左上角 `10pt` 胶囊导航栏 Tracker Badge，如 `第三章 · 创新点二：高效推理架构`）。
- **句式模板**：**`[核心方法/研究对象] + [强动词] + [量化实证结论 / 核心机制突破]`**
- **字数与行数硬约束**：**14–22 个汉字**（含英文缩写与数字总宽不超过 24 个全角字符位），`24–28pt 加粗`，**强制单行显示，严禁断行成孤字尾巴**（若超出 24 字，提炼主干并将补充条件移入 `14–15pt` 副标题）。

| ❌ 静态目录式废标题（禁止） | ✅ 结论先行页主标题（强制规范） |
|:---|:---|
| `实验结果分析` | `跨模态对齐机制在五大基准全面超越 SOTA，检索召回率最高提升 9.4%` |
| `模型架构介绍` | `双通道时空解耦架构将复杂度由 O(N²) 降至线性 O(N)` |
| `稳健性检验` | `替换核心解释变量与安慰剂检验均在 1% 水平显著，因果效应稳健` |
| `主要创新点` | `围绕“机理建模—算法加速—系统落地”形成三项递进式原始创新` |

#### 2. 卡片标题与并列模块：严格对称“动宾结构”
当页面包含 2–4 个并列卡片、技术路线阶段、研究内容或创新点摘要时，所有卡片小标题必须采用 **字数相等（如全四字、全六字或全八字）、词性对齐的动宾短语（Verb + Object）**。

- **高能量学术动词词库（按场景选用，同页不重复）**：
  - *理论与机理*：`揭示……机理`、`建立……界限`、`阐明……规律`、`刻画……演化`、`证明……收敛`
  - *方法与架构*：`构建……网络`、`提出……算子`、`引入……先验`、`解耦……表征`、`重构……流水线`
  - *优化与突破*：`攻克……瓶颈`、`压缩……开销`、`消除……偏差`、`抑制……退化`、`突破……极限`
  - *实验与落地*：`验证……泛化`、`消融……贡献`、`部署……平台`、`赋能……决策`
- **对称性正误示范**：
  - ❌ *词性混乱、长短不一*：`1. 数据集是怎么收集的` / `2. 多尺度特征融合模块` / `3. 实验效果非常好`
  - ✅ *六字对称动宾结构*：`构建多源基准` $\rightarrow$ `解耦多尺特征` $\rightarrow$ `验证跨域泛化`
  - ✅ *八字对称动宾结构*：`揭示长程衰减机理` $\rightarrow$ `提出动态稀疏算子` $\rightarrow$ `实现端侧实时推理`

---

### 2.3 思源黑体 / 微软雅黑 + Arial / Segoe UI 混排规范

在中英文混排 PPT 中，**绝对禁止将英文单词、数字和符号直接交由中文字体自带的西文字形渲染**。微软雅黑或思源黑体内置的拉丁字符为了迁就汉字宽度，字怀偏扁、字距松散；更严重的是，若用宋体（SimSun）渲染中文却未绑定西文字体，西文会变成锯齿感极强的点阵窄字。

#### 三套黄金中西文双字体方案 (Dual-Script Font Stacks)

| 方案代号 | 中文字体 (`<a:ea>`) | 西文与数字 (`<a:latin>`) | 数学公式 (OMML) | 代码等宽 (`mono`) | 适用场景与跨平台渲染安全策略 |
|:---|:---|:---|:---|:---|:---|
| **`CN-1: 现代精致思源流`（首选推荐）** | `Source Han Sans SC`（思源黑体 / Linux: `Noto Sans CJK SC`） | `Segoe UI`（或 `Inter` / `Arial`） | `Cambria Math` | `Consolas` | 顶会组会、高水平学术论坛、PDF/PNG 交付物。字重齐全（Regular / Medium / Bold），与 `soffice` Linux 渲染器 `Noto Sans CJK SC` 度量 100% 一致。 |
| **`CN-2: 答辩零风险兼容流`（Windows 现场投影首选）** | `Microsoft YaHei`（微软雅黑） | `Arial`（或 `Segoe UI`） | `Cambria Math` | `Consolas` | **高校答辩室/基金评审现场电脑 100% 预装**，拷入陌生 Windows 电脑绝不乱码、绝不回退成宋体。 |
| **`CN-3: 苹果原生学术流`（macOS Keynote/Office）** | `PingFang SC`（苹方-简） | `SF Pro Text` / `Helvetica Neue` | `STIX Two Math` / `Cambria Math` | `SF Mono` / `Menlo` | Mac 本机演示或导出 PDF 汇报。**严禁不转 PDF 直接将含 PingFang SC 的 PPTX 拷至 Windows 电脑打开**。 |

> [!WARNING]
> **宋体（SimSun / 华文中宋）投影避坑准则**：传统纸质学位论文正文用宋体，但**投影仪屏幕严禁大面积使用细笔画宋体作为 `<20pt` 正文**——低分辨率或高亮泛白投影仪会导致宋体横画断裂、闪烁发虚。除人文历史古籍引文卡片可使用 `20pt+ 华文中宋/方正书宋` 外，现代理工医经管学术 PPT 一律采用无衬线黑体（思源黑体 / 微软雅黑）。

#### 代码级双字体显式绑定规范（`python-pptx` & `PptxGenJS` 强制实现）

PowerPoint 的 OpenXML 底层将同一文本运行（`<a:r>`）的字体拆分为拉丁脚本 `<a:latin>` 与东亚脚本 `<a:ea>`。在 `python-pptx` 中仅设置 `run.font.name = "Arial"` 会导致汉字回退为系统丑陋默认字体；仅设置 `run.font.name = "Microsoft YaHei"` 又会让英文数字失去 `Segoe UI / Arial` 的紧凑造型。生成代码必须显式双绑：

```python
# python-pptx: 显式绑定西文 (<a:latin>) 与中文 (<a:ea>) 双字体，杜绝中英混排崩塌与 Linux 方块乱码
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

def set_bilingual_font(run, latin_font="Segoe UI", ea_font="Microsoft YaHei", size_pt=15, bold=False, color_rgb=None):
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    if color_rgb:
        run.font.color.rgb = color_rgb
    rPr = run._r.get_or_add_rPr()
    rPr.set("lang", "zh-CN")
    rPr.set("altLang", "en-US")
    # 绑定西文与数字字体 (<a:latin>)
    latin = rPr.find(qn("a:latin"))
    if latin is None:
        latin = parse_xml(f'<a:latin xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="{latin_font}"/>')
        rPr.append(latin)
    else:
        latin.set("typeface", latin_font)
    # 绑定东亚汉字字体 (<a:ea>)
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = parse_xml(f'<a:ea xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="{ea_font}"/>')
        rPr.append(ea)
    else:
        ea.set("typeface", ea_font)
```

在 **`PptxGenJS`** 中，由于单次 `fontFace` 属性会同时写入 `<a:latin>` 和 `<a:ea>`，处理中英混排时应通过正则切分中英文 Run 数组，分别赋给 `Segoe UI / Arial` 与 `Microsoft YaHei / Noto Sans CJK SC`：

```javascript
// PptxGenJS: 自动切分中英文/数字 Run，确保西文用 Segoe UI/Arial、中文用思源黑体/微软雅黑
function buildBilingualRuns(text, baseOpts = {}, latinFace = "Segoe UI", cjkFace = "Microsoft YaHei") {
  // 匹配连续 ASCII 西文、数字、常见半角符号（含 %, +, -, ., /, @）
  const tokenRegex = /([A-Za-z0-9_@#%&+\-./:=<>±×÷~]+(?:\s+[A-Za-z0-9_@#%&+\-./:=<>±×÷~]+)*)/g;
  const parts = text.split(tokenRegex).filter(Boolean);
  return parts.map(part => {
    const isLatin = /^[A-Za-z0-9_@#%&+\-./:=<>±×÷~]/.test(part);
    return {
      text: part,
      options: {
        ...baseOpts,
        fontFace: isLatin ? latinFace : cjkFace,
        lang: isLatin ? "en-US" : "zh-CN"
      }
    };
  });
}
```

#### W3C CLReq 盘古之白（Pangu Spacing）与标点全半角铁律
1. **盘古之白（汉字与西文/数字间距）**：
   - 在**汉字与英文字母、汉字与阿拉伯数字**之间，统一插入 **1 个半角空格（`U+0020`）**：
     - ❌ `在ImageNet上Top-1准确率提升3.8%，仅需8张RTX4090训练12小时。`
     - ✅ `在 ImageNet 上 Top-1 准确率提升 3.8%，仅需 8 张 RTX 4090 训练 12 小时。`
   - **唯一例外（不加空格）**：西文/数字紧邻**中文全角标点**（`“”‘’（），。：；、`）时，全角标点自带半宽留白，**严禁再加空格**：
     - ❌ `提出了 “SparseKV” （见图 2a） ，显著降低延迟。`
     - ✅ `提出了“SparseKV”（见图 2a），显著降低延迟。`
   - **度数与百分号**：数字与 `%`、`°C` 之间不加空格，但 `%` 与后续汉字之间加半角空格（`提升 14.2% 的吞吐量`）。
2. **标点全半角严格隔离**：
   - 中文主干句一律使用**全角标点**：`、` `，` `。` `：` `；` `（` `）` `“”`。
   - 括号内纯英文文献引用、数学区间、代码表达式内部使用**半角标点**：`(Vaswani et al., 2017)`、`[0, 1]`、`O(N log N)`。
   - **绝对禁止阴阳括号与半角逗号混穿**：如 `（CNN, 卷积神经网络)` 或 `精度提升 4.2%, 延迟下降 18%`。
3. **行首禁则与防断行保护**：
   - 数值与单位（`128 GB`、`p < 0.01`）、图号引用（`图 3b`、`Table 2`）在临近文本框右边界时，使用不间断空格 `\u00A0` 连接，严禁上一行留 `128`、下一行掉出 `GB`。

---

### 2.4 专业英文术语保留准则 (Domain Terminology Preservation Matrix)

中文学术汇报既反对“生硬汉化导致评委看不懂”（把 `KV Cache` 译成“键值高速缓冲存储器”），也反对“散装外企夹生英语”（把“权衡”说成 `trade-off`、把“基线”说成 `baseline` 满天飞）。严格执行**三级术语分流准则**：

| 分流层级 | 适用词类 | 执行准则 | ✅ 规范示例 | ❌ 错误反例（生硬机翻或散装夹杂） |
|:---|:---|:---|:---|:---|
| **Tier 1：强制保留纯英文原名** | 专有模型/算法名、数据集、评估指标缩写、硬件与精度规格、复杂度、基因/分子式、统计符号 | **直接保留标准英文大小写，不强译中文**（严禁全小写如 `imagenet`、`bert`、`bleu`） | `Transformer`、`FlashAttention-2`、`LoRA`、`KV Cache`、`ImageNet-1K`、`BLEU-4`、`mAP@0.5`、`AUROC`、`FP8`、`RTX 4090`、`CRISPR-Cas9`、`p < 0.001` | ❌ `闪光注意力二号`、`低秩适配器`、`键值缓存`、`图像网数据集`、`transformer`（首字母漏大写） |
| **Tier 2：首现“中文规范名（英文缩写）”锚定** | 学科核心机制、统计因果方法、跨学科评审可能陌生的领域缩略语（尤见于博士答辩与国自然） | **全片首次出现时给出“规范中文名（英文缩写）”**，后续幻灯片统一直接使用英文缩写或简短中文名 | 首次：`检索增强生成（RAG）`、`双重差分法（DID）`、`倾向得分匹配（PSM）`、`稀疏自编码器（SAE）`；后文直接写 `RAG`、`DID` | ❌ 全片十几次重复写冗长的 `检索增强生成（Retrieval-Augmented Generation, RAG）`，挤占宝贵版面 |
| **Tier 3：强制使用纯正学术中文** | 通用科研动作、普通名词、性质形容词、逻辑连接词 | **一律使用精准凝练的学术中文，严禁散装中英混杂** | `基线模型`、`消融实验`、`泛化能力`、`鲁棒性`、`吞吐量`、`收敛速度`、`权衡`、`微调`、`端到端`、`显著优于` | ❌ `我们在 baseline 上 finetune 后做了一个 trade-off，robustness 很 solid，成功 boost 了 performance` |

---

### 2.5 字号与行距配比：中西文光学补偿矩阵 (Optical Font Sizing & Line-Height Calibration)

由于汉字属于高笔画密度的方块表意文字（字面率约 `90%–94%`，无上下延展的升部 ascender / 降部 descender），而拉丁字母小写高度（x-height）仅占字身框约 `52%`：
1. **字号下限补偿（`+1pt ~ +2pt` 法则）**：在 `12pt` 下，英文 `Arial / Segoe UI` 依然锐利易读，但多笔画汉字（如 `囊、簇、骤、鲁棒`）在投影仪上已开始笔画糊连。因此，**中文卡片正文字号必须比同布局英文版上调 `1–2pt`，大礼堂答辩场景上调 `2–4pt`**。
2. **行距呼吸感补偿（`+0.10x ~ +0.15x` 法则）**：英文行距 `1.20x` 即有天然的上下留白，而中文在 `1.15x–1.20x` 下两行方块字几乎上下顶死，极易串行。因此，**中文多行要点行距必须设为 `1.30x–1.40x`**，段后间距（`spaceAfter`）设为 `6–8pt`。

#### 全场景字号、行距与字数预算总表（16:9 画布 `13.333" × 7.500"`）

| 层级角色 (Hierarchy Role) | Track 1: 英文标准 (`en_academic`) | Track 2/3: 中文组会/精读 (`zh_academic` 密排) | Track 2: 学位答辩/国自然大屏 (`zh_defense` 礼堂) | 行距倍数 (`EN` / `CN`) | 字重与样式约束 |
|:---|:---|:---|:---|:---|:---|
| **顶部章节导航胶囊 (`Tracker Badge`)** | `10 pt` (`9–11`) | `10.5 pt` (`10–11`) | `11–12 pt` | `1.00x` / `1.00x` | Bold；英文大写字母字距 `+0.5pt`；中文配间隔号 `·` |
| **页顶结论主标题 (`Slide Title`)** | `25–26 pt` (`22–28`) | `24–26 pt` (`22–28`) | `26–30 pt` (`24–32`) | `1.10x` / `1.18x` | **Bold (700)**；英文 $\le 2$ 行，中文优选 **1 行**（$\le 22$ 字） |
| **页顶副标题 (`Slide Subtitle`)** | `14–15 pt` | `14–15 pt` | `15–16 pt` | `1.20x` / `1.25x` | EN: Medium/Italic；**CN: Regular/Medium（严禁中文斜体！）** |
| **卡片/模块标题 (`Card Header`)** | `16–18 pt` | `16–18 pt` | `18–20 pt` | `1.15x` / `1.20x` | **Bold (700)**；对称动宾短语或名词锚点 |
| **标准卡片正文条目 (`Card Body`)** | `13–14 pt` | `14–15 pt` | `16–18 pt` | `1.22x` / `1.35x` | Regular + **粗体前缀锚点**；段后距 `6pt` |
| **高密度批注/三栏卡正文 (`Body Dense`)** | `12 pt` *(硬下限)* | `13–14 pt` *(13pt 硬下限)* | `14–15 pt` *(14pt 硬下限)* | `1.20x` / `1.30x` | 仅用于三栏/四栏紧凑拆解卡或旁注卡 |
| **数据表格内容 (`Table Header / Cell`)** | `12 pt` / `11–12 pt` | `13 pt` / `12–13 pt` | `14 pt` / `13–14 pt` | `1.15x` / `1.25x` | 表头 Bold；SOTA 最优值 **Bold**，次优值 <u>Underline</u> |
| **独立数学公式 (`OMML Display / Inline`)** | `14–16 pt` / `13 pt` | `15–16 pt` / `14 pt` | `16–18 pt` / `15 pt` | `1.20x` / `1.25x` | 原生矢量 `Cambria Math` OMML，严禁低清截图 |
| **图表引线标注 / 页脚 (`Callout / Footer`)** | `10–11 pt` / `10 pt` | `11–12 pt` / `10.5 pt` | `12 pt` / `11 pt` | `1.10x` / `1.15x` | 页脚统一含文献出处与右下角页码 `XX / YY` |

> [!CAUTION]
> **中文绝对禁止使用斜体（`italic: true`）！** 汉字在排版传统中不存在斜体概念；PowerPoint 对汉字强加 `italic` 只会执行机械几何剪切（电子伪斜体），导致字形倾倒变形、极度业余。在 `zh_academic` 与 `zh_en_hybrid` 轨道中，副标题、旁注、强调词一律使用 **颜色层级（次级灰 `#475569`）或字重（Medium / Bold）** 替代斜体，仅数学变量符号（如 $x_i, \theta, p$）及拉丁语学术词（*et al.*, *in vivo*, *in situ*）保留斜体。

---

## 3. Linux Headless Vision-QA (`soffice`) Font Fallback Protocol

Stage 4 of `cs-report-ppt` converts `.pptx` $\rightarrow$ `.pdf` $\rightarrow$ `150+ DPI PNG` via LibreOffice (`soffice --headless --convert-to pdf`) so the agent visually inspects every slide. When running in Linux/Docker environments where `Microsoft YaHei` or `Segoe UI` is absent, missing Fontconfig rules cause **tofu boxes (`□□□`) or metric overflow** (false text-collision positives).

1. **Pre-Flight Font Verification**:
   - Before rendering Chinese decks on Linux, check `fc-list :lang=zh` for `Noto Sans CJK SC` or `Source Han Sans SC` (`fonts-noto-cjk` package) and `Liberation Sans` / `DejaVu Sans` for Latin metric parity with `Arial`.
2. **Safe Cross-Platform Pairing Rule**:
   - On Windows hosts: `Microsoft YaHei` + `Segoe UI` / `Arial` renders natively in both PowerPoint and LibreOffice.
   - On Linux hosts without Windows fonts: Set `<a:ea typeface="Noto Sans CJK SC"/>` and `<a:latin typeface="Liberation Sans"/>` (or configure Fontconfig `<alias>` mapping `Microsoft YaHei` $\rightarrow$ `Noto Sans CJK SC`), ensuring rendered QA PNGs match desktop PowerPoint line-wrap geometry within `< 2%` width variance.

---

## 4. Agent Pre-Render Linguistic & Typographic Audit Checklist

Before compiling `.pptx` code, verify every slide against these 10 deterministic checks:

- [ ] **Track Lock**: Zero Chinese characters or full-width punctuation in `en_academic`; zero "散装外企中英混杂" in `zh_academic`.
- [ ] **Assertion Headlines**: Slides 2–14 all use empirical claim headlines (EN: 8–13 words, Sentence case, $\le 2$ lines; CN: 14–22 chars, single line, zero static labels like `实验结果`).
- [ ] **Symmetric Subheaders**: Parallel cards use grammatically parallel headers (CN: equal-length 4/6/8-character verb-object phrases; EN: parallel noun/gerund anchors).
- [ ] **Micro-Bullet Length**: Every visual-slide bullet stays $\le 12$ words (EN, hard cap 15) or $\le 22$汉字 (CN, hard cap 26), starting with a **Bold Anchor**.
- [ ] **Visual-Text Pointers**: At least 2 bullets per visual slide explicitly reference `Fig. X`, curve colors, stage numbers, or table rows alongside quantified $\Delta$ metrics.
- [ ] **Dual-Script XML Binding**: Every CJK text run explicitly binds `<a:latin>` (`Segoe UI` / `Arial`) and `<a:ea>` (`Source Han Sans SC` / `Microsoft YaHei` / `Noto Sans CJK SC`).
- [ ] **Zero Chinese Italics**: `italic: false` enforced on all Chinese text runs (subtitles, callouts, annotations).
- [ ] **Pangu Spacing & Punctuation**: Half-width space placed between CJK and Latin/numerals; omitted next to full-width CJK punctuation; zero mismatched brackets `（...)`.
- [ ] **Font Floor Compliance**: Zero body text below `12pt` (EN) or `13pt` (CN seminar) / `16pt` (CN auditorium defense); line spacing set to `1.20–1.25x` (EN) or `1.30–1.40x` (CN).
- [ ] **True Math & Symbols**: Native OMML (`Cambria Math`) used for equations; Unicode `−` (`U+2212`), `×` (`U+00D7`), and `–` (`U+2013`) used instead of raw ASCII hyphens.
