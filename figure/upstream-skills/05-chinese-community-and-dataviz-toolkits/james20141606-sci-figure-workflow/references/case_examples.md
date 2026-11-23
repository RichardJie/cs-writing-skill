# 4 个顶会风格完整案例

每个案例包含：图类型 / 适用场景 / 完整英文 prompt / 关键 trick。

---

## 案例 1：主架构图（三层横向堆叠）

**适用**：方法论 paper 的"系统总览图"——把 pipeline 拆成上中下三层。Memory 系统、Agent 系统、RAG 系统都常用。

**典型代表**：阿东帖子里那张 Memory Taxonomy 图。

### 完整 prompt

```
A publication-quality scientific architecture diagram for a NeurIPS-style paper, depicting an enhanced memory management workflow.

LAYOUT: 5-panel grid, dashed-bordered sub-boxes. Three rows on the left, two rows on the right.

PANELS (left column, top to bottom):
- Panel ①: "Connecting Related Experiences" — graph nodes A-E connected by colored edges; below: 4 small icons labeled "semantic similarity / temporal proximity / contextual relevance / confidence score"
- Panel ②: "Integrating Fragmented Memories" — three document icons → "integrate" arrow → split into "compress→summarization" and "distill→abstraction" → "multimodal fusion" cluster
- Panel ③: "Transforming Across Memory Levels" — "Low memory level" (left) ↔ "transform" (gear icons) ↔ "High memory level" with three sub-items: long-term storage, synthesized structure, retrieval index

PANELS (right column, top to bottom):
- Panel ④: "Updating Existing Memories" — "Existing Memories" database in the center, with arrows from: "specific prompts (summarize/merge) — LLMs", "specific rules", "Agents — revise? prune? resolve conflicts?", "versioning + provenance"
- Panel ⑤: "Filtering Obsolete Information" — two sub-categories: "Usage-based" (access frequency, time-based decay) + "Content-based" (outdated, duplicated, contradictory) → filtering funnel → "Filtered Information" (right) with badges: removing, lower score, invalid tags, privacy-safe pruning

COLOR PALETTE (semantic, max 4):
- #E3EBF5 light blue: structural / data
- #E5F3E0 light green: positive / valid
- #FCE4E4 light pink: alerts / obsolete
- #F5E9D6 cream: neutral background

ARROWS: solid black 1.5px for primary flow; dashed gray for optional/conditional. All arrowheads classic style.

TYPOGRAPHY: Times New Roman. Panel titles bold 12pt with circled numbers (①②③④⑤). Body labels 10pt. Italic 9pt for examples.

STYLE: flat design, white background, no shadows, no gradients, thin black strokes (1px). Iconography: minimalistic line icons (database, gear, document, funnel, lock).

CAPTION (bottom, centered, 11pt): "Figure 5: Enhanced workflow of the memory management process."

Do not simplify, follow every detail exactly.
```

### 关键 trick

- 用 ①②③④⑤ 圈数字而不是 (1)(2)(3) — 视觉重量更够，符合 NeurIPS 风格
- 5 panel 不规则布局（左 3 右 2），比规整的 2x3 更有"研究图"的感觉
- 颜色严格 4 色封顶，每色一个语义

---

## 案例 2：四列分区架构图（仿 GAN / Transformer 风格）

**适用**：方法对比、消融模块拆解、模型组件并列。

### 完整 prompt

```
A clean 4-column architecture diagram for a NeurIPS/ICML paper, comparing four method variants side by side.

LAYOUT: 4 vertical columns of equal width, separated by thin vertical dividers. Each column is a complete pipeline from top (input) to bottom (output).

PER-COLUMN STRUCTURE (top to bottom):
1. Header bar with method name (bold, white text on colored fill)
2. Input block (rectangle, light gray)
3. 3-4 processing modules stacked vertically with downward arrows
4. Output block (rounded rectangle, colored fill)

COLUMN CONTENT:
- Column A: "Baseline" — header #999999 — modules: Encoder → Linear → Decoder
- Column B: "+ Module X" — header #4A90E2 — modules: Encoder → [Module X] → Linear → Decoder
- Column C: "+ Module Y" — header #50C878 — modules: Encoder → Linear → [Module Y] → Decoder
- Column D: "Ours (Full)" — header #E94B3C, with star icon — modules: Encoder → [Module X] → Linear → [Module Y] → Decoder

NEW MODULES highlighted with thicker stroke (2px) and matching column color fill at 30% opacity.

ARROWS: solid black 1.5px down arrows between modules. No cross-column arrows.

ANNOTATIONS: small text labels right of each new module: "Δ params: +2M" or "+contrastive loss".

COLOR PALETTE (semantic, max 4):
- #999999 gray: baseline / no addition
- #4A90E2 blue: structural addition
- #50C878 green: loss/objective addition
- #E94B3C red: full method (ours)

TYPOGRAPHY: Times New Roman. Method name bold white 12pt on colored bar. Module labels 10pt black. Annotations italic 9pt.

DIMENSIONS: 16:9, white background, 300 DPI.

STYLE: flat design, no shadows, no gradients, thin strokes.

CAPTION: "Figure 2: Architecture comparison of baseline and three ablation variants."

Do not simplify, follow every detail exactly.
```

### 关键 trick

- 每列的 header bar 用纯色填白字，是顶会图的标志性视觉
- 新增模块用对应列颜色 30% opacity 填充，立刻能看出"这一列加了啥"
- 第 4 列加 ⭐ 图标暗示"ours"，比写大字"Best!"更专业

---

## 案例 3：Taxonomy 分类图（三段式）

**适用**：综述 paper 的分类总览、概念体系图。

**典型代表**：阿东第二张图里那张 "Memory Forms / Memory Structures / Memory Operations" 三栏图。

### 完整 prompt

```
A taxonomy diagram for a survey paper, classifying a research area into three orthogonal dimensions, presented as three rounded rectangles side by side.

LAYOUT: 3 large rounded rectangles (radius 12px) horizontally arranged with equal spacing. Each rectangle is a self-contained taxonomy panel.

PANEL (a) — "Memory Forms" (left, soft green tint #E8F4E2):
- 4 stacked sub-boxes with dashed borders:
  · "Episodic" with 5 document icons + "..." → caption: "e.g., raw interactions, trajectories"
  · "Semantic" with 5 hexagon icons + "..." → caption: "e.g., facts, entity relations"
  · "Procedural" with 5 gear icons + "..." → caption: "e.g., skill schemas, action templates"
  · "Working" with 5 clipboard icons + "..." → caption: "e.g., in-context task state"

PANEL (b) — "Memory Structures" (center, soft blue tint #E2ECF7):
- Top sub-box: "Graph" — 8 circle nodes (n1..n8) connected by edges in a heterogeneous graph layout → caption: "e.g., Semantic Graph, Causal Graph, KG"
- Bottom sub-box: "Hierarchy" — 3D layered pyramid with circles at each level, up/down arrows → caption: "e.g., Episode→Concept→Schema"

PANEL (c) — "Memory Operations" (right, soft pink tint #F7E2EC):
- 3 stacked sub-boxes:
  · "Write & Encode" — wave icon → "encode" box → graph icon; formula: f_enc: x_t → m_t
  · "Retrieve & Rank" — query q → triangle filter → ranked list 1/2/3; formula: m̂ = argmax_m score(q,m)
  · "Consolidate & Forget" — two circles → merge node → faded X; formula: θ_forget, Δt decay

PANEL LABELS (bold, bottom-center each panel):
"(a) Memory Forms"  "(b) Memory Structures"  "(c) Memory Operations"

NODE STYLE: outlined circles 12px, thin black stroke, white fill.
MATH: italic serif, inline with diagrams. Emoji icons ~18px.
DASHED BORDERS on all sub-boxes, 1px black.

CAPTION below: "Figure 1: Taxonomy of the proposed memory system organized by forms, structures, and operations."

Do not simplify, follow every detail exactly.
```

### 关键 trick

- 三个 panel 用三种极淡的 tint（绿/蓝/粉）暗示并列关系，但不喧宾夺主
- 每个 sub-box 都用 dashed border，避免视觉过重
- 数学公式用 italic serif inline，模拟 LaTeX 排版
- 5 个 icon + `...` 是 Taxonomy 图经典的"举例"语法

---

## 案例 4：消融实验图（矩阵 + 柱状）

**适用**：实验 section 的可视化对比。

### 完整 prompt

```
An ablation study figure combining a configuration matrix with a results bar chart, in NeurIPS publication style.

LAYOUT: 2-column figure, 60/40 split.

LEFT (60%) — Configuration matrix:
- 5 rows × 4 columns table
- Rows: "Baseline", "+ A", "+ B", "+ A+B", "+ A+B+C (Ours)"
- Columns: "Module A", "Module B", "Module C", "Inference Cost"
- Cells: ✓ filled green circle / ✗ empty circle / numeric value (italic) for cost
- Last row highlighted with light yellow background #FFF9D9

RIGHT (40%) — Vertical bar chart:
- X-axis: 5 method names (matching matrix rows, rotated 30°)
- Y-axis: "Accuracy (%)" with range 70-90
- Bars colored:
  · gray #BBBBBB for Baseline
  · light blue #88B0E0 for + A and + B
  · medium blue #4A90E2 for + A+B
  · red #E94B3C for + A+B+C (Ours), with star marker ⭐ above
- Numeric value labels above each bar (bold)
- Thin error bars on top (±std)

LEGEND: small, top-right of bar chart, with color squares and "✓ included / ✗ excluded".

TYPOGRAPHY: Times New Roman. Headers bold 11pt. Body 10pt. Numerics italic. Method names 9pt rotated.

GRID: light gray dashed horizontal grid on bar chart only. No grid on matrix.

STYLE: flat design, white background, thin strokes, no shadows.

DIMENSIONS: double-column width 17.5cm, 300 DPI.

CAPTION: "Figure 3: Ablation study. Left: configuration matrix. Right: accuracy on test set; error bars indicate standard deviation across 5 seeds. ⭐ denotes our final method."

Do not simplify, follow every detail exactly.
```

### 关键 trick

- 矩阵用 ✓/✗ 圆点而不是文字 yes/no，密度更紧凑
- 最佳行用 #FFF9D9 浅黄高亮，比加粗或描边更优雅
- 柱状图按"加了几个模块"梯度配色（gray→light blue→medium blue→red），让"加得越多效果越好"的视觉趋势自动浮现
- ⭐ 标记 ours，不需要再写大字

---

## 通用模板填空表

写新 prompt 时按这张表填，不会漏：

| 字段 | 必填 | 例 |
|------|------|---|
| LAYOUT | ✅ | "5-panel grid", "4 vertical columns", "horizontal flow with 3 stages" |
| PANELS | ✅ | 每个 panel 的位置 + 内容 |
| MODULES | ✅ | 形状 + hex 颜色 + label + 位置 |
| ARROWS | ✅ | from/to + style + 颜色 + 粗细 |
| ICONS / MATH | 选填 | 描述 emoji 或公式 |
| TYPOGRAPHY | ✅ | 字体 + 字号层级 |
| COLOR PALETTE | ✅ | hex + 语义 + ≤4 种 |
| STYLE | ✅ | flat / 白底 / 无阴影 / 无渐变 |
| PANEL LABELS | 选填 | (a)(b)(c) 或 ①②③ |
| CAPTION | ✅ | "Figure N: ..." |
| 末尾咒语 | ✅ | `Do not simplify, follow every detail exactly.` |
