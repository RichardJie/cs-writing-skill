# sci-figure-workflow

> Claude Code Skill: AIGC 科研绘图 4 步工作流（GPT-image-2 × Gemini Vision × Nano Banana 2 × draw.io）

把"画一张顶会论文配图"从半天的 PPT 拖框工作，压缩成 10 分钟的多模型协作管线，产出**可编辑**的 `.drawio` / `.pptx` / `.svg` 三种格式。

## 核心理念

**从"P 图"到"写规格"** —— 顶级科研图的核心不是画，是 prompt。要像写工程设计文档一样，把布局、颜色语义、箭头类型、字体大小、分辨率全部定义清楚，AI 才能按规格出图。堆砌"漂亮、高清、专业"这种形容词只会得到"看起来不错但不符合期刊标准"的图。

**关键英文咒语**：每个生图 prompt 末尾必须加 `Do not simplify, follow every detail exactly.`

## 4 步工作流

```
输入（参考图 OR 论文文字）
        ↓
Step 1 — 理解输入（Gemini Vision / GPT）
   ├─ 图片模式（有参考图）→ 输出中文结构描述
   └─ 文字模式（无参考图）→ 设计 flat design 英文规格
        ↓
Step 2 — 生成参考图（多轮迭代，每轮只改一处）
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

## 文件结构

```
sci-figure-workflow/
├── SKILL.md                          # 主入口
├── README.md                         # 本文件
└── references/
    ├── prompt_templates.md           # Step 1 两种模式 prompt + 英文咒语 + 迭代话术
    ├── case_examples.md              # 4 个顶会风格完整案例
    ├── tool_reference.md             # 9 个工具速查 + 典型用法 + 坑
    └── checklist.md                  # Step 4 生产级细节检查清单
```

## 4 个完整案例

`references/case_examples.md` 里有 4 个可直接抄的英文 prompt：

1. **主架构图**（三层横向堆叠，仿 Memory Taxonomy 综述）
2. **四列分区架构图**（仿 GAN / Transformer 风格的方法对比）
3. **Taxonomy 分类图**（survey paper 三段式）
4. **消融实验图**（配置矩阵 + 柱状图）

## 安装到 Claude Code

```bash
git clone https://github.com/james20141606/sci-figure-workflow.git \
  ~/.claude/skills/sci-figure-workflow
```

下次 Claude 看到"科研绘图""帮我复刻这张图""顶会架构图""graphical abstract"等触发词时会自动激活。

## 与其他 skill 的分工

| 对比 | scientific-schematics | sci-figure-workflow（本 skill） |
|------|----------------------|--------------------------------|
| 工具 | Nano Banana Pro 单轮 | GPT-image-2 + Gemini + draw.io 多工具串联 |
| 输出 | PNG 一张 | drawio / pptx / svg 三种可编辑格式 |
| 适用 | 一键出图，无需精修 | 顶会投稿，要反复迭代和精修 |

## 方法论溯源

本工作流由数字生命阿东（大模型算法工程师，OPC 创业者）总结提出。本仓库做的是把这套散落在帖子和飞书文档里的方法论，沉淀成可被 Claude Code 自动触发、机器可执行的 Skill。

## License

MIT
