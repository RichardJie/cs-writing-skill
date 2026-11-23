---
name: sci-figure-workflow
description: |
  AIGC 科研绘图 4 步工作流（GPT-image-2 × Gemini Vision × Nano Banana 2 × draw.io），用于做**生产级、顶会级、可编辑**的论文配图、架构图、graphical abstract、taxonomy 图、机制图。

  核心理念：从"P 图"到"写规格"——顶级科研图的核心不是画，是 prompt。要像写工程设计文档一样把布局/颜色/箭头/字体/分辨率全部定义清楚。

  四步管线：① Gemini/GPT 理解参考图或论文文字 → 输出结构化规格描述；② GPT-image-2 / Nano Banana 2 按规格生成 PNG 参考图（多轮迭代）；③ 三路并行转可编辑格式（drawio / pptx / svg）；④ 在 draw.io / Illustrator / Inkscape 里人工精修，过生产级检查清单。

  触发词（中英双语）：科研绘图、论文配图、顶会架构图、Nature/Cell/NeurIPS 配图、graphical abstract、taxonomy 图、机制图、消融实验图、复刻这张图、帮我画论文里的示意图、scientific figure、publication figure、conference figure、reproduce this figure、make this editable。

  也适用于：把投稿被 reviewer 嫌"图不清晰"的旧图重做、把白板手绘图升级成投稿级矢量图、把别人论文里的图改造成自己的版本。

  **不要**在以下场景触发：
  - 数据可视化（柱状图/折线图/热力图）→ 用 matplotlib/seaborn/data-viz-plots
  - 一键单轮生图（不需要可编辑产出）→ 用 scientific-schematics
  - 普通 PPT 作图、商业流程图 → 用通用工具
---

# 科研绘图 4 步工作流

> **核心咒语**：每个生图 prompt 末尾必须加一句 `Do not simplify, follow every detail exactly.` —— 这是整套方法论的关键技巧，强制 AI 严格执行规格。

## 总览

```
输入（参考图 OR 论文文字）
        ↓
Step 1 — 理解输入（Gemini Vision / GPT）
   ├─ 图片模式（有参考图）→ 输出中文结构描述
   └─ 文字模式（无参考图）→ 设计 flat design 英文规格
        ↓
Step 2 — 生成参考图（多轮迭代）
   ├─ 路径 A：GPT-image-2（推荐，2025 最强）
   └─ 路径 B：Imagen 4.0 / Nano Banana 2
        ↓
Step 3 — 三路并行转可编辑格式
   ├─ figure.drawio（首选，编辑灵活）
   ├─ figure.pptx（快速改文字）
   └─ figure.svg（视觉最保真，投稿级）
        ↓
Step 4 — 人工精修 + 过生产级检查清单
        ↓
最终交付
```

## Step 0：触发后的第一件事——分支选择

被触发后，**先确认用户处于哪种模式**，不要跳过这一步：

- **有参考图（图片模式）**：用户已经提供 / 即将提供一张要复刻或改造的图 → 走 Step 1 图片模式
- **无参考图（文字模式）**：用户只有论文方法描述、模块名称、流程文字 → 走 Step 1 文字模式
- **混合模式**：用户有参考图但要改方向（"仿这张但用我的内容"）→ 先图片模式提取结构，再用文字模式替换内容

如果用户没明说，主动问一句"你有参考图想复刻吗？还是从零设计？"再继续。

## Step 1：理解输入（Gemini Vision / GPT 文字理解）

这一步的输出质量决定后面所有步骤的上限。**不要跳过这一步直接生图。**

### 图片模式（复刻参考图）

把参考图丢给 Gemini Vision 或 GPT，用以下中文 prompt：

```
分析这张科研图，输出用于重绘的完整结构描述：
1. 整体布局（横向/纵向/几列/几层）
2. 每个模块的：形状、填充颜色（十六进制）、文字标签、尺寸比例
3. 连接关系：箭头类型（实线/虚线）、方向、粗细、颜色
4. 特殊元素：图标、数学符号、嵌套关系
5. 整体配色方案（列出所有使用的十六进制色值）
请用中文输出，尽量详细，不遗漏任何细节。
```

得到结构描述后，**让用户检查一遍**：色值对吗？漏了哪个箭头吗？这一步多花 1 分钟，后面省半小时。

### 文字模式（原创设计）

无参考图时，用"黄金模板"让 LLM 替你写英文规格：

```
你是一位深谙国际期刊（Nature / Cell / NeurIPS）出版规范的资深学术图表设计师。

请根据以下研究内容，生成一段用于绘制顶会学术架构图的英文提示词。

要求：
1. 明确布局方式（横向流程 / 纵向分层 / 四列分区）
2. 精确定义每个模块的形状、颜色（十六进制）、文字标签
3. 描述箭头类型（实线/虚线）和数据流方向
4. 配色不超过 4 种，附色彩语义说明
5. 风格：flat design, 白色背景, 无阴影, 无渐变, Times New Roman 字体
6. 分辨率：300DPI, 单栏 ≤ 8.5cm 或双栏 ≤ 17.5cm

【我的研究内容】
（此处粘贴论文摘要 / 方法描述 / 模块名称）
```

完整的 prompt 模板见 `references/prompt_templates.md`。

## Step 2：生成参考图

把 Step 1 的结构描述（中文）转成英文 prompt，喂给生图模型。

### 路径 A：GPT-image-2（推荐）

2025 年最强生图模型，多轮对话迭代能力最好。在英文 prompt 末尾**必须**加：

> **`Do not simplify, follow every detail exactly.`**

迭代原则——**每轮只改一个地方**：
- 第 1 轮：先看整体布局对不对
- 第 2 轮：调配色
- 第 3 轮：调箭头方向
- ...

不要一次改 5 个地方，AI 会顾此失彼。

### 路径 B：Imagen 4.0 / Nano Banana 2

Nano Banana 2 是 flat design 专精，特别适合：
- Graphical abstract（论文摘要图）
- 机制图（mechanism / pipeline）
- 简洁的 taxonomy

Imagen 4.0 风格更稳定，与 Gemini 同 Key，做自动化流程时和 Step 1 串起来更顺。

## Step 3：三路并行转可编辑格式

PNG 不能直接投稿（reviewer 要源文件），也不能改字。满意的 PNG 出来后，让 Gemini Vision 或 GPT 同时输出三种格式：

| 文件 | 工具 | 推荐场景 |
|------|------|---------|
| `figure.drawio` | draw.io | **首选**：内置科研图标库，编辑最灵活，免费 |
| `figure.pptx` | PowerPoint / WPS | 改文字、配色最快，适合规则流程图 |
| `figure.svg` | Inkscape / Illustrator / 浏览器 | 视觉最保真，精修后导出 PDF 投稿用 |

让用户三种都拿到，根据要怎么改、改多少自己挑。

## Step 4：人工精修（不可省）

AI 生成的是初稿，**没过这一步不算你的图**。

打开 draw.io / Illustrator / Inkscape，逐项核查 `references/checklist.md`：

- **数据准确性**：所有数值和正文一致；缩写大小写规范；数学符号、下标、希腊字母对齐
- **视觉规范**：300 DPI；配色 ≤ 4 种且有语义；Times New Roman；flat design（白底/无阴影/无渐变）
- **文件规范**：单栏 ≤ 8.5 cm，双栏 ≤ 17.5 cm；导出 PDF 嵌字体
- **版权合规**：确认目标会议/期刊的 AI 绘图披露政策

完整清单见 `references/checklist.md`。

## 与 `scientific-schematics` skill 的分工

| 维度 | scientific-schematics | sci-figure-workflow（本 skill） |
|------|----------------------|--------------------------------|
| 工具 | Nano Banana Pro 单轮 | GPT-image-2 + Gemini + draw.io 多工具串联 |
| 输出 | PNG 一张 | drawio / pptx / svg 三种可编辑格式 |
| 适用 | 一键出图，无需精修 | 顶会投稿，要反复迭代和精修 |
| 检查 | 自动质量分判定 | 人工过生产级 checklist |

需要"一键生图，质量过得去就行"用前者；需要"投顶会、reviewer 挑刺都不怕"用本 skill。

## 参考资料

- `references/prompt_templates.md` —— 两种模式 prompt 模板、英文咒语全集、迭代话术
- `references/case_examples.md` —— 4 个顶会风格完整案例（主架构图 / 四列分区 / Taxonomy / 消融实验）
- `references/tool_reference.md` —— 工具速查表 + 每个工具的典型用法和坑
- `references/checklist.md` —— Step 4 生产级细节检查清单

## 方法论溯源

本工作流由数字生命阿东（大模型算法工程师，OPC 创业者）总结提出。核心洞察："顶级科研图的核心不是画，是 prompt。要像写工程设计文档一样定义所有规格。"
