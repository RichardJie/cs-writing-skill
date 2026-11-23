# 🧪 Awesome Scientific Figures — Skills, MCPs & Plugins for AI Coding Agents

> 科研绘图武器库：面向 **Claude Code** 和 **OpenAI Codex** 的 Skills、MCP Server、插件、Python 库精选列表。

论文级精美图表 + 架构图 + 示意图 —— 告别裸 matplotlib，让 AI 编程助手帮你画图。

---

## 📋 目录

- [Skills（技能文件）](#skills技能文件)
  - [Codex 专属](#codex-专属-skills)
  - [Claude Code 专属](#claude-code-专属-skills)
  - [跨平台通用](#跨平台通用-skills)
- [MCP Server（模型上下文协议服务器）](#mcp-server模型上下文协议服务器)
  - [Draw.io 系列](#drawio-系列)
  - [Excalidraw 系列](#excalidraw-系列)
  - [TikZ / LaTeX 系列](#tikz--latex-系列)
  - [通用图表](#通用图表)
- [Codex 官方插件（openai/plugins）](#codex-官方插件-openaiplugins)
- [Python 库（程序化精美绘图）](#python-库程序化精美绘图)
- [推荐组合方案](#推荐组合方案)

---

## Skills（技能文件）

### Codex 专属 Skills

| Skill | Stars | 描述 |
|---|---|---|
| [**engineering-figure-agent**](https://github.com/heyu-233/engineering-figure-agent) | ⭐245 | 双模式：**Image Mode**（系统架构图、算法流程图、示意图、图形摘要，用 Gemini/GPT 图像模型生成） + **Plot Mode**（精确数值的 benchmark 柱状图、消融实验图、趋势曲线、热图、散点图）；支持中英双语标注 |
| [**abstract-fig**](https://github.com/keros68/abstract-fig) | 新 | Codex 专用——生成**可编辑的 draw.io 图形摘要和手稿概念图**：Image2 生成元素→透明分离 PNG→嵌入 draw.io 独立对象→文字框/箭头/标签全可编辑，输出 `.drawio` |
| [**paper-framework-figure-studio-pro**](https://www.sourcepulse.org/projects/29689594) | 新 | 论文框架图工作室——专门生成论文 Method 部分的 pipeline 架构图和框架示意图 |
| [**archify**](https://github.com/tt-a1i/archify) | v2.5 | 5 种图表类型（Architecture/Workflow/Sequence/Data Flow/Lifecycle）；暗/亮双主题 SVG 自动切换；PNG/JPEG/WebP/SVG 导出最高 4× 分辨率；单 HTML 零依赖 |
| [**codex-skill-academic-slides**](https://github.com/FA-T-T/codex-skill-academic-slides) | 新 | Codex 学术幻灯片/海报/校样图/架构图生成，基于 GPT Image 2 |

### Claude Code 专属 Skills

| Skill | Stars | 描述 |
|---|---|---|
| [**scipilot-figure-skill**](https://github.com/Haojae/scipilot-figure-skill) | ⭐ 推荐 | **"先想再画"哲学**：先分析数据→确定论证目标→推荐图表类型；15 条拦截规则阻止坏实践（双Y轴→分面、饼图→水平条、彩虹色谱→viridis）；v2.1 视觉自检；Okabe-Ito 色盲安全配色 |
| [**academic-figure-skill**](https://github.com/TingxiYu/academic-figure-skill) | ⭐ 推荐 | **29 种图表类型**（火山图、热图、UMAP、小提琴、雷达图、桑基图、森林图等）；目标 Nature/Cell/Science 标准；4 轮 QA 协议（反模式扫描→代码合规→视觉逻辑→渲染验证） |
| [**paper-figure**](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/skills-codex-claude-review/paper-figure/SKILL.md) | ⭐ 推荐 | 8 步工作流：读论文方案→环境搭建→自动选图→生成→批跑→LaTeX 嵌入→评审质量→视觉检查清单；300 DPI、衬线字体、矢量 PDF、无标题（标题用 LaTeX caption） |
| [**paper-illustration**](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/paper-illustration/SKILL.md) | ⭐ 推荐 | **架构图/方法插图专用**——Claude 规划→Gemini 布局优化→风格验证→渲染→Claude 严格审核（1-10 分，迭代到 ≥9）；CVPR/ICLR/NeurIPS 风格；绿输入→蓝编码器→紫融合→橙输出配色 |
| [**bioinformatics-plotting-standards**](https://github.com/Rooneyxu/bioinformatics-plotting-standards) | 新 | 生信出版级单图/多 panel 组合（火山图、热图、UMAP/t-SNE、小提琴、点图、曼哈顿图、空间转录组图）；内置 QC 脚本 |

### 跨平台通用 Skills

| Skill | Stars | 描述 |
|---|---|---|
| [**drawio-diagram-builder-skill**](https://github.com/Will-hxw/drawio-diagram-builder-skill) | ⭐ 推荐 | 研究风格可编辑 draw.io 图——**截图驱动自纠循环**（生成→预览→截图→自检缺陷→修复→重复）；含 MIT 许可的 Tabler SVG 图标库；支持参考图复刻 |
| [**paper-illustrate**](https://skillsmp.com/zh/creators/shiien/self-evolved-research-framework/skills-paper-illustrate) | 新 | 生成**严格学术标准 TikZ/SVG 图**：架构图、pipeline 图、概念图、流程图、对比图；约束调色板、一致间距、色盲安全 |
| [**archify**](https://github.com/tt-a1i/archify) | v2.5 | Claude / Codex CLI / opencode 通用；Mermaid 方言输入；CJK 字体降级；golden-file CI 测试 |
| [**AgentFigureGallery**](https://github.com/Dsadd4/AgentFigureGallery) | 16k+ 样本 | 10 种科学图表类型的 16,341 个视觉参考；浏览器端点赞/筛选；导出参考包用于绘图代码生成 |
| [**NaturePanelForge**](https://github.com/littlepeachs/NaturePanelForge) | 新 | 将科学论文图片和 Nature 系列开放获取论文转化为 panel 级可执行绘图代码重建任务 |
| [**diagram-to-image**](https://github.com/zju-zhanglu/diagram-to-image) | 新 | 将 Markdown 中的 ASCII/Unicode 文本图转换为 draw.io PNG 图片 |

---

## MCP Server（模型上下文协议服务器）

### Draw.io 系列

| MCP Server | 安装命令 | 亮点 |
|---|---|---|
| [**drawio-mcp (Python版)**](https://github.com/yohasacura/drawio-mcp) 🏆 | `uvx drawio-mcp` | **310+ 形状、44 种边样式、21 种颜色主题**；C4/BPMN/K8s/网络拓扑/ER/UML；Sugiyama DAG 自动布局；**一键美化(polish)**；支持多页/多图层 |
| [**drawio-mcp (JS版)**](https://github.com/Sujimoshi/drawio-mcp) | `npx drawio-mcp` | `.drawio.svg` 格式 VSCode 无缝兼容；hierarchical/circle/organic/radial-tree/partition/stack 多种自动布局 |
| [**drawio-mcp-server (lgazo)**](https://github.com/lgazo/drawio-mcp-server) 🏆 | `npx -y drawio-mcp-server --editor` | **内建 draw.io 编辑器** (localhost:3000)；自动发现 AWS/GCP/Azure/Cisco 图标库；Mermaid 导入；多 Tab/多页面；TLS/HTTPS |
| [**@drawio/mcp (官方)**](https://www.npmjs.com/package/@drawio/mcp) | `npx -y @drawio/mcp` | Draw.io 官方 MCP；支持原生 XML、CSV、Mermaid 语法输入 |
| [**AWS sample-drawio-mcp**](https://github.com/aws-samples/sample-drawio-mcp) | `npx -y https://...` | AWS 官方架构图（CloudFront/API Gateway/Lambda/Aurora/S3/Bedrock 等）；100% 本地运行 |

### Excalidraw 系列

| MCP Server | 安装命令 | 亮点 |
|---|---|---|
| [**codex-excalidraw**](https://www.npmjs.com/package/codex-excalidraw) 🏆 | `npx codex-excalidraw` | Codex/Claude **直接在可编辑 Excalidraw 画布上画图**；Mermaid→Excalidraw 转换；双向编辑（AI 画→人编辑→AI 读取画布→改进）；本地工作台 `http://127.0.0.1:3000/` |
| [**drawmode**](https://github.com/teamchong/drawmode) | `npx drawmode --stdio` | LLM 只需写 ~10 行 TypeScript（代替 500 行 JSON）；Graphviz 自动布局；输出 `.excalidraw`、PNG、SVG |
| [**@kamiazya/whiteboard**](https://github.com/kamiazya/whiteboard) | `npx -y @kamiazya/whiteboard-mcp@latest` | **实时协作白板**——WebSocket 同步；Claude Code / Codex / Gemini CLI 通用；捆绑 3 个 Skill |
| [**@airmix/mcp-excalidraw-server**](https://www.npmjs.com/package/@airmix/mcp-excalidraw-server) | npm install | **26 个 MCP 工具**——元素级 CRUD 控制；`describe_scene` + `get_canvas_screenshot` 让 AI "看到"画布；快照/回滚；可分享 URL；Docker 支持 |

### TikZ / LaTeX 系列

| MCP Server | 安装命令 | 亮点 |
|---|---|---|
| [**tikz-mcp**](https://github.com/FlorianHuo/tikz-mcp) 🏆 | `pip install tikz-mcp` | 本地 `pdflatex` 编译 TikZ → **1000 DPI PNG**（透明背景）；内建风格指南 + **AI 自检流程**（AI 自动检查并修复输出后再呈现）；v0.2.0 (2026.3) |
| [**upmath-mcp**](https://github.com/danielsimonjr/upmath-mcp) | `npm install` | 通过 i.upmath.me API 渲染 TikZ，**无需本地安装 TeX**；支持 tikz-3dplot、pgfplots、circuitikz、bussproofs、mhchem |
| [**texra-scientific-skills**](https://github.com/texra-ai/texra-scientific-skills) | GitHub clone | 9 个科研 Skill 包，含 `tikz-figure-builder`（迭代编译+查看工作流）、`math-ocr`、`manuscript-review` 等 |
| [**Overleaf Claude MCP**](https://github.com/junfei-z/overleaf-claude-mcp) | GitHub clone | Claude Code ↔ Overleaf 直连——读/写/推送 LaTeX 文件；Smart Diff 模式省 Token；v1.1.0 (2026.4) |
| [**TeXFlow MCP**](https://glama.ai/mcp/servers/aaronsb/texflow-mcp) | `uvx texflow-mcp` | 结构化文档模型——LaTeX 是输出产物非直接编辑对象；Markdown 导入 |

### 通用图表

| MCP Server | 安装命令 | 亮点 |
|---|---|---|
| [**diagrams-mcp**](https://github.com/ByteOverDev/diagrams-mcp) | `uvx diagrams-mcp-server` | 基于 mingrammer/diagrams；15+ 云厂商、500+ 节点类型；Mermaid + PlantUML 双引擎；输出 PNG/PDF/JPG/DOT |
| [**graphviz-mcp**](https://www.npmjs.com/package/graphviz-mcp) | `npx -y graphviz-mcp` | 任意描述→Graphviz 渲染；交互式查看器 pan/zoom；**无需单独安装 Graphviz** |
| [**CC_SysML**](https://github.com/atk-pulsar/CC_SysML) | GitHub clone | 代码库→SysML v2.0 模型→Gemini 生成专业 PNG；15 个 MCP 工具；支持 BDD/IBD/PKG/ACT/SEQ 图 |
| [**@usetessera/mcp**](https://www.npmjs.com/package/@usetessera/mcp) | npm install | C4 模型架构文档（Context/Container/Component/Module）；34 个工具；git 新鲜度验证 |

---

## Codex 官方插件（openai/plugins）

以下插件来自 [openai/plugins](https://github.com/openai/plugins) 仓库，是 Codex 生态中最成熟的扩展：

| 插件 | 分类 | 绘图/可视化能力 |
|---|---|---|
| [**figma**](https://github.com/openai/plugins) | 设计 | 🏆 **最完整参考实现**——`use_figma` 读取设计→生成代码、Code to Canvas 反向同步、Code Connect、设计系统规则；含 skills + commands + hooks + UI HTML |
| [**canva**](https://github.com/openai/plugins) | 设计 | 搜索模板、创建设计、编辑现有资产；社交媒图/海报/封面图；支持一键导出 PowerPoint→Canva 精修 |
| [**remotion**](https://github.com/openai/plugins) | 视频 | **代码即视频**——React 控制字幕/转场/图表动画/进度条；localhost:3031 时间线编辑器 |
| [**google-slides**](https://github.com/openai/plugins) | 演示 | 演示文稿自动化——程序化创建/编辑 Google Slides |
| [**build-web-apps**](https://github.com/openai/plugins) | 开发 | 含 UI 组件、图表、仪表盘等 Web 可视化相关的完整工作流 |
| [**vercel**](https://github.com/openai/plugins) | DevOps | 最大插件（47 skills + 3 agents + 5 commands）；含前端部署后的可视化仪表盘 |
| [**render**](https://github.com/openai/plugins) | DevOps | 20+ skills；含架构和基础设施图相关的部署流程 |

---

## Python 库（程序化精美绘图）

从 Python 端升级 matplotlib 默认输出的利器：

| 库 | 安装 | 亮点 |
|---|---|---|
| [**dartwork-mpl**](https://pypi.org/project/dartwork-mpl/) 🏆 | `pip install dartwork-mpl` | **AI 原生**——自带 MCP Server + Prompt 语料库；物理宽度 API（`figsize("13cm", "col1")`）；确定性布局（算术非启发式）；OKLCH 色彩系统；`validate_figure()` 自动质检 |
| [**figrecipe**](https://pypi.org/project/figrecipe/) 🏆 | `pip install figrecipe` | 毫米级精确布局；**内置示意图 DSL**（boxes/cylinders/stadiums/documents/code blocks/folders）可直接画架构图；SCIEX/SCIEX_DARK/MATPLOTLIB 预设；GUI 编辑器 |
| [**Swizz**](https://github.com/) (ICML 2025) | `pip install swizz` | 一行代码绘图；DataFrame→LaTeX 表格；Flutter 式 block 布局（PlotBlock/Row/Col/LegendBlock）拼合多 panel |
| [**AutoFigure**](https://github.com/ResearAI/AutoFigure) (ICLR 2026) | GitHub | **文本→图形 / 论文 PDF→图形**；双代理 Review-Refine 循环；输出 SVG 或 draw.io mxGraph XML |
| [**Tesserax**](https://blog.apiad.net/p/introducing-tesserax) | `pip install tesserax` | 零依赖纯 Python；原生 SVG；**锚点系统**（相对定位，无手动坐标）；参数化可复用 |
| [**Netgraph**](https://github.com/paulbrodersen/netgraph) | `pip install netgraph` | 发表级网络/图可视化；节点重叠消解、边交叉最小化、边解捆；交互式编辑 |
| [**CACHAI**](https://pypi.org/project/cachai/) | `pip install cachai` | 弦图/相关性图专用——逐元素样式、对数缩放线宽、Bezier 平滑 |

---

## 推荐组合方案

### 🏆 全能选手（科研全场景覆盖）

```
┌─────────────────────────────────────────────┐
│  架构图/示意图/pipeline 图                     │
│  → drawio-mcp (Python版) + abstract-fig      │
│  → 备选: paper-illustration Skill            │
├─────────────────────────────────────────────┤
│  数据图（柱/线/散/热/火山/UMAP...）            │
│  → dartwork-mpl + Swizz                      │
│  → 备选: scipilot-figure-skill               │
├─────────────────────────────────────────────┤
│  TikZ / LaTeX 论文图                          │
│  → tikz-mcp + texra-scientific-skills        │
│  → 备选: upmath-mcp (免装 TeX)               │
├─────────────────────────────────────────────┤
│  快速白板/手绘风格                             │
│  → codex-excalidraw + drawmode               │
│  → 备选: @airmix/mcp-excalidraw-server       │
└─────────────────────────────────────────────┘
```

### 🥇 Claude Code 用户最小可行套装

```bash
# Skills
git clone https://github.com/Haojae/scipilot-figure-skill.git ~/.claude/skills/scipilot-figure
git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git
# 复制 paper-figure 和 paper-illustration 到 ~/.claude/skills/

# MCP
claude mcp add drawio -- uvx drawio-mcp
claude mcp add tikz -- pip install tikz-mcp

# Python
pip install dartwork-mpl swizz
```

### 🥇 Codex 用户最小可行套装

```bash
# Skills
git clone https://github.com/heyu-233/engineering-figure-agent.git
git clone https://github.com/keros68/abstract-fig.git

# MCP & Plugins
codex mcp add drawio -- npx -y @drawio/mcp
codex plugin marketplace add kamiazya/whiteboard

# Python
pip install dartwork-mpl figrecipe
```

---

## 📊 能力矩阵速查

| 需求 | 首选工具 | 安装/获取 |
|---|---|---|
| 论文数据图（matplotlib 替代） | dartwork-mpl + Swizz | `pip install dartwork-mpl swizz` |
| 架构图 / System Diagram | drawio-mcp (Python版) | `uvx drawio-mcp` |
| Pipeline / Framework 图 | paper-illustration Skill | GitHub clone |
| 手绘风格流程图 | codex-excalidraw / drawmode | `npx codex-excalidraw` |
| TikZ 论文图 | tikz-mcp | `pip install tikz-mcp` |
| 云架构图 (AWS/GCP/Azure) | AWS sample-drawio-mcp | `npx` |
| 图形摘要 / Graphical Abstract | abstract-fig (Codex) | GitHub clone |
| 网络图 / 图论可视化 | Netgraph | `pip install netgraph` |
| 可编辑 draw.io 图 | drawio-mcp-server (lgazo) | `npx -y drawio-mcp-server --editor` |
| 科研幻灯片 | codex-skill-academic-slides | GitHub clone |
| 弦图 / 相关性图 | CACHAI | `pip install cachai` |

---

## 🔗 相关资源

- [openai/plugins](https://github.com/openai/plugins) — Codex 官方插件合集 (170+)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Claude Skills 精选 (64k+ Stars)
- [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) — Codex Skills 精选 (14k+ Stars)
- [anthropics/skills](https://github.com/anthropics/skills) — Anthropic 官方 Skills (127k+ Stars)
- [SkillsMP](https://skillsmp.com) — Agent Skills 市场和发现平台

---

## ⚖️ 许可

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — 本列表为公共领域，欢迎自由使用、修改和分享。

---

> **维护提示**: 科研绘图 AI 工具生态在 2025-2026 年爆发式增长。如果你发现新的优秀工具，欢迎提 Issue 或 PR！
