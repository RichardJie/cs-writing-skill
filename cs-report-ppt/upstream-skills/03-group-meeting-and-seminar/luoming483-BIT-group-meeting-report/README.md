# BIT-PPT-literature

Claude Code 技能：读取学术论文 PDF，自动生成北京理工大学（BIT）学术风格的文献汇报 PPT。

## 功能

- 自动解析论文 PDF，提取文本和图片
- 生成 8 页标准学术汇报 PPT（封面、背景、方法、实验、总结等）
- 使用 BIT 学术答辩 PPT 模板（绿白配色、微软雅黑字体）
- 支持论文原图自动插入（保持原始宽高比）
- 支持 Mermaid 框架图、数据柱状图、公式文本框
- 自动排版：小文本框精确分区、结论色块、关键词标红

## 安装

### 1. 安装 officecli

```bash
# macOS / Linux
curl -fsSL https://d.officecli.ai/install.sh | bash

# Windows (PowerShell)
irm https://d.officecli.ai/install.ps1 | iex
```

### 2. 安装 PyMuPDF（用于提取 PDF 图片）

```bash
pip install pymupdf
```

### 3. 获取技能文件

克隆本仓库后，技能文件已位于 `.claude/skills/BIT-PPT-literature/SKILL.md`，在仓库目录内直接可用。

如需全局使用（任意目录均可调用 `/BIT-PPT-literature`），复制到用户目录：

```bash
# Windows (PowerShell)
copy .claude\skills\BIT-PPT-literature\SKILL.md %USERPROFILE%\.claude\skills\BIT-PPT-literature\SKILL.md

# macOS / Linux
cp .claude/skills/BIT-PPT-literature/SKILL.md ~/.claude/skills/BIT-PPT-literature/SKILL.md
```

### 4. 准备 BIT 模板

仓库已包含预生成的迷你模板 `北理工模板_mini.pptx`（5页，36MB），包含封面、内容、双栏对比、三列卡片、结尾五种页面类型。

如果使用自己的完整模板，可重新生成迷你模板：

```bash
# 从完整模板（580页）提取5个核心页面
officecli create 北理工模板_mini.pptx
# ... 克隆需要的页面 ...
```

将 `北理工模板_mini.pptx` 放到 `D:/BIT_ppt_skills/` 目录下即可。

## 使用

在 Claude Code 对话中调用：

```
/BIT-PPT-literature /path/to/paper.pdf
```

Claude 将自动：
1. 读取论文内容
2. 提取 PDF 中的图片
3. 分析论文结构并规划 PPT 大纲
4. 生成 PPT 文件，保存到 `论文目录/论文文件名_汇报.pptx`

## 生成的 PPT 结构

| 页码 | 内容 | 布局 |
|------|------|------|
| 1 | 封面 | 论文标题、作者、期刊 |
| 2 | 研究背景与动机 | 全宽文字 + 结论色块 |
| 3 | 方法/框架总览 | 左文右图（或中央架构图） |
| 4 | 方法细节 | 文字 + 原图 |
| 5 | 实验设置与结果 | 上文下图 + 结论色块 |
| 6 | 对比分析 | 双栏对比 |
| 7 | 总结与展望 | 全宽文字 / 三列卡片 |
| 8 | 结尾感谢 | Q&A 页 |

## 依赖

- [officecli](https://officecli.ai) - OOXML CLI 工具
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF 图片提取
- Claude Code - AI 助手
