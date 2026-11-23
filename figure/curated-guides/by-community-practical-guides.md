# 科研绘图与顶会架构图网友及学者实战经验汇编 (`by-community-practical-guides.md`)

> **数据来源与零自创声明（Zero AI Self-Invention Notice）**
> 本文档收录的每一条工作流、软件选型对比、参数配置、报错排查方案、色值组合与 AI 辅助绘图原版 Prompt，均经实抓核验（Live-Scraped & Verified），严格摘录或忠实归纳自 **知乎（Zhihu）**、**GitHub 中文与学者开源社区**、**少数派（sspai）**、**科学网（ScienceNet）**、**研之成理（公众号归档）**、**Reddit（`r/MachineLearning`、`r/AskAcademia`、`r/LaTeX`、`r/datavisualization`）**、**Hacker News** 以及 **一线科研人员独立博客** 的真实公开贴文，**零 AI 自创规则、零虚构示例、零自造评分表**。所有条目均逐一标注真实作者/账号、平台、发布/编辑日期与精确原始 URL。

---

## 目录

1. [第一部分：顶会（CVPR / NeurIPS / ICML / ACL）Teaser 图与模型架构图绘制工作流](#第一部分顶会cvpr--neurips--icml--aclteaser-图与模型架构图绘制工作流)
   - 1.1 顶会论文 Teaser 图与 Methodology 框架图分工与自查清单（知乎 / GitHub 中文社区）
   - 1.2 PowerPoint / Keynote / Google Slides + ML Visuals / Illustrator 搭积木工作流（知乎 / 少数派 / Reddit / HN / GitHub）
   - 1.3 Draw.io（`diagrams.net`）与 Figma / Visio 科研架构图实战流（知乎 / 少数派 / Reddit / GitHub）
   - 1.4 Inkscape + LaTeX / Matplotlib 矢量科研插图实战工作流（Researcher Blogs / HN / Reddit）
   - 1.5 TikZ 代码流与手绘转 TikZ / 可视化编辑器讨论（Researcher Blog / Reddit `r/LaTeX` & `r/MachineLearning` / Hacker News）
   - 1.6 AI 辅助科研架构图与机理图**原版 Prompt** 与多轮精修实测贴（少数派 / 知乎 / 科学网 / Reddit / GitHub 中文仓库）
2. [第二部分：Nature / Science / Cell 多面板拼图、字体嵌入（`pdf.fonttype=42`）、矢量导出与审稿人拒稿配图问题实测](#第二部分nature--science--cell-多面板拼图字体嵌入pdffonttype42矢量导出与审稿人拒稿配图问题实测)
   - 2.1 Nature 子刊级多面板拼图（Multi-panel Layout）Adobe Illustrator 与 Inkscape 实操贴（知乎 / Reddit `r/AskAcademia`）
   - 2.2 Matplotlib `pdf.fonttype = 42`、Type 3 字体报错（IEEE PDF eXpress / EDAS / VLDB / ScholarOne）与 Linux HPC 缺字体实测贴（Researcher Blogs / 知乎 / GitHub Issue）
   - 2.3 期刊投稿矢量格式、DPI 分辨率红线与审稿人常见返修/拒稿配图痛点（科学网 / GitHub 中文社区 / Reddit）
3. [第三部分：科研配色与图表美化真实网友及学者经验贴](#第三部分科研配色与图表美化真实网友及学者经验贴)
   - 3.1 研之成理与知乎高赞科研配色方法论（互补色、HSL 调色、蓝-橙-灰三色公式、Illustrator 重新着色）
   - 3.2 *Nature* / *Science* 顶刊取色实测贴与中文开源配色库（知乎 / 科学网 / 少数派 / GitHub）
   - 3.3 色盲友好（Colorblind-Safe）与多类别色板实战讨论（Reddit `r/datavisualization` / GitHub 中文 Skill）

---

## 第一部分：顶会（CVPR / NeurIPS / ICML / ACL）Teaser 图与模型架构图绘制工作流

### 1.1 顶会论文 Teaser 图与 Methodology 框架图分工与自查清单

#### [1] 邹镇洪（知乎专栏，2021-10-16）—《科研分享4——从顶会BestPaper学习图表优化》
- **作者 / 平台**：邹镇洪（`zhihu.com/people/zou-zhen-hong-70`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/422236215
- **核心实战经验整理（源自近年 CVPR / AI 顶会 Best Paper 图表拆解）**：
  - **核心目标**：「如何让读者在最短时间内（只看图表）掌握本文的关键信息——3 性能、1 方法、2 论证过程。不会影响论文的实际贡献，但会影响论文的可读性/录用。」
  - **位置 1（Abstract / Introduction 立论区的 Teaser / Image Abstract 效果展示图）**：一般位于双栏右上方或摘要正下方作为 `image abstract`，要求高度概括本文最大贡献（究竟突出**性能**、**新发现**还是**新方法**，例如 CVPR *DeepCap* 与 *BSP-Net* 的首页展示图）。
  - **位置 2（Method / Experiment / Ablation 辩论区图表矩阵）**：拆分为「模型总览图（展示算法逻辑） + 模块细节图 + 视觉效果图（自我对比与横向对比） + 统计分析图 + 性能对比图」。

#### [2] 大学青椒（知乎专栏，2026-07-24）—《计算机视觉方向工科生，论文写作全指南（第四篇：Methodology部分的写法与分段策略）》
- **作者 / 平台**：大学青椒（`zhihu.com/people/cai-wo-shi-shui-44`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/2063961383830659919
- **核心实战经验整理（CV 方向 Overall Architecture 框架图标准与四步画法）**：
  - **好框架图的四项硬标准**：
    1. **数据流向清晰**：箭头一目了然，「输入 → 处理 → 输出」，读者能直接追踪张量怎么走；
    2. **模块边界明确**：不同功能模块用不同颜色的虚线框或背景框区分；
    3. **关键维度标注**：特征图尺寸（$H \times W \times C$）在关键位置明确标出；
    4. **图上文字精简**：图上文字不要过多，解释留给正文。
  - **工具学习成本与场景选型（原文对照表）**：`Visio`（通用架构图最稳妥，学习成本低）、`PowerPoint/Keynote`（快速出图，极低）、`draw.io`（免费在线，极低）、`Adobe Illustrator`（顶会级精美图，高）、`TikZ (LaTeX)`（直接嵌入论文最专业，高）。
  - **实操四步法与投稿检查项**：
    1. 先在白纸上手画一遍草稿，确定每个模块位置与连线；
    2. 从输入开始按数据流向逐个画模块；
    3. 添加箭头并标注特征图维度；
    4. 加上图例和标题，导出矢量图（`PDF` / `EMF`）直接插入 LaTeX。
  - **符号与正文对齐自查**：「字体与正文字体一致（通常 `Arial` 或 `Times New Roman`，字号不小于 `8pt`）；图上的关键符号（如 $\mathbf{F}_{att}$）必须与正文公式符号完全一致；框架图上的模块名称必须与正文 Key Components 小节标题一一对应。」

#### [3] MLNLP-World 社区（GitHub 中文开源仓库）— `MLNLP-World/Paper-Writing-Tips` & `MLNLP-World/Paper-Picture-Writing-Code`
- **作者 / 平台**：MLNLP 社区组织者与贡献者｜GitHub 中文仓库
- **原始 URL**：
  - https://github.com/MLNLP-World/Paper-Writing-Tips （Commit `50712564062249b28b8493ebdc35f8b3a3b88512`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/MLNLP-World-Paper-Writing-Tips/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/MLNLP-World-Paper-Writing-Tips/)）
  - https://github.com/MLNLP-World/Paper-Picture-Writing-Code （Commit `4092efa7b630afccb22f1c27370e945b464a556c`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/MLNLP-World-Paper-Picture-Writing-Code/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/MLNLP-World-Paper-Picture-Writing-Code/)）
- **核心实战经验整理（原文条目 #34, #37–#40）**：
  - **Caption 与正文不复述（#34）**：「Caption 写『这个图表是什么』；正文写『这个图表说明了什么』，不要把 Caption 在正文中复述。」
  - **矢量图硬要求（#37）**：使用 Adobe Illustrator、OmniGraffle 存为 PDF 矢量图，或 Matplotlib `plt.savefig('draw.pdf')`，或在 LaTeX 中用 `pgfplots` 直接绘制。
  - **图片字号准则（#38）**：「图片字体大小应**介于正文字体与 caption 之间**，且图中字体大小保持一致。」
  - **黑白打印兼容（#39）**：「不要以颜色作为指代图示中线条的唯一特征，可使用实线/虚线、亮/暗、不同线形等。」
  - **简洁规范（#40）**：「颜色种类不超过六种；避免过亮的颜色；尽量少用文字描述；同样功能模块使用统一格式；**箭头走向应趋于同一个方向**。」
  - **配套开源代码**：`Paper-Picture-Writing-Code` 提供 AI 顶会常用五类图（折线图、带误差条折线图、柱状图、散点图、Attention 注意力热力图与序列可视化、Transformer 结构图、Taxonomy 分类树、Timeline 时间线）的 LaTeX TikZ/PGFPlots 与 Matplotlib 对照源码。

#### [4] 陈冠英 Guanying Chen（GitHub 学者仓库）— `guanyingc/latex_paper_writing_tips` & `guanyingc/python_plot_utils`
- **作者 / 平台**：Guanying Chen（SYSU / HKU）｜GitHub
- **原始 URL**：
  - https://github.com/guanyingc/latex_paper_writing_tips （Commit `62d649a9fc05e6b7c99cb42657d2d61815b8efb3`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/guanyingc-latex-paper-writing-tips/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/guanyingc-latex-paper-writing-tips/)）
  - https://github.com/guanyingc/python_plot_utils （Commit `d73b62ba7185db0c86b8ecb0c13fe23a7714cab5`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/guanyingc-python-plot-utils/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/guanyingc-python-plot-utils/)）
- **核心实战经验整理**：
  - 收录 15 套 CVPR / ICCV / ECCV / NeurIPS 真实发表论文的 LaTeX 子图排版模板（`figures/figure1.tex`–`figure15.tex`），解决跨栏首页 Teaser（`figure*`）、多列视觉定性对比图无白边对齐、旋转行标签与局部放大框（Crop Patches for Zoom-in Comparison）等 CV 顶会高频刚需。

---

### 1.2 PowerPoint / Keynote / Google Slides + ML Visuals / Illustrator 搭积木工作流

#### [5] 机器学习社区（知乎专栏，2022-01-20）—《拯救手残党！如何画出漂亮的深度学习模型图？》
- **作者 / 平台**：机器学习社区（`zhihu.com/people/chen-xi-63-33-5`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/450978352
- **核心实战经验整理**：
  - 介绍 Elvis Saravia（DAIR.AI）发起的开源项目 **ML Visuals**（https://github.com/dair-ai/ml-visuals ）在深度学习架构图中的复用方法：直接在 Google Slides / PowerPoint 模板中复用预置的 Transformer 编码器块、多头注意力连接、特征图张量块、残差连接箭头等可拆分矢量图形组件，改字与重组后导出矢量 PDF 插入论文。

#### [6] 投必得论文编译（知乎专栏，2021-03-19）—《科研论文作图系列-从PPT到AI (一)》
- **作者 / 平台**：投必得论文编译（`zhihu.com/people/tou-bi-de`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/114831367
- **核心实战经验整理**：
  - 对比位图与矢量图差异后，拆解「统计软件（Origin / GraphPad Prism）或 PPT 初稿 → 直接复制粘贴导入 Adobe Illustrator（AI）精修」的经典科研联合工作流：统计图粘贴进 AI 后会自动解构为独立可编辑矢量图元，可用文字工具直接选中坐标轴标签统一替换字体、增删标注，再与原理示意图拼合输出。

#### [7] `huashu996/PPT-Framework-Skill`（GitHub 中文开源仓库）— PowerPoint 原生可编辑学术框图重构规范
- **作者 / 平台**：`huashu996`｜GitHub 中文仓库
- **原始 URL**：https://github.com/huashu996/PPT-Framework-Skill （Commit `01f51d69c93975771074dc563cade221151b90f6`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/huashu996-PPT-Framework-Skill/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/huashu996-PPT-Framework-Skill/)）
- **核心实战经验整理（摘自 `SKILL.md` 与 `references/ppt-construction-layout-unified-principles.md`）**：
  - **Hybrid Reconstruction 原生可编辑三铁律**：
    1. 所有可读文字与公式严禁与框线、箭头、形状或其他文字发生可见边界碰撞，含「标题 + 公式」的模块必须先划分互不重叠的标题带与公式槽；
    2. 每条折线或折线箭头必须是**单个 PowerPoint 原生可编辑连接器对象**，严禁用多条碎直线拼接冒充折线，且连接直箭头前先对齐框体中心轴以保证严格水平或垂直；
    3. 横排文本严禁出现单个汉字、孤立英文 token 或孤立标点独占一行。

#### [8] Reddit `r/MachineLearning` 网友热议贴 — 顶会神经网络架构图究竟用什么画？
- **平台与原始 URL（4 篇高讨论度实测贴）**：
  1. `u/KarmaCut132` et al., *"[D] Which software do you guys use for illustrating research frameworks/ideas ?"* (`r/MachineLearning`) — https://www.reddit.com/r/MachineLearning/comments/18qzdnj/d_which_software_do_you_guys_use_for_illustrating/
  2. `u/SimpleObvious4048` et al., *"[D] Which software tools do researchers use to make neural net architectures like this?"* (`r/MachineLearning`) — https://www.reddit.com/r/MachineLearning/comments/1ig6k3l/d_which_software_tools_do_researchers_use_to_make/
  3. `u/Pedimus` et al., *"[D] Best tool for drawing U-Net style diagrams?"* (`r/MachineLearning`) — https://www.reddit.com/r/MachineLearning/comments/rin63t/d_best_tool_for_drawing_unet_style_diagrams/
  4. `u/insider_7` et al., *"[D] resources to make journal-level artwork in ML"* (`r/MachineLearning`) — https://www.reddit.com/r/MachineLearning/comments/8s0uu1/d_resources_to_make_journallevel_artwork_in_ml/
- **真实研究人员高赞回复摘录**：
  - **Google Slides / PowerPoint 实用派**：
    - `u/SirBlobfish`（`18qzdnj`）：*"Google slides for basic shapes (for easy collaboration), matplotlib for plots, occasional tikz for graphs/mathy things, and latex for putting things together. Looking at other comments, I'll probably switch to inkscape for putting stuff together. Pro tip: chatgpt is a godsend for tikz and matplotlib formatting."*
    - `u/dp3471`（`1ig6k3l`）：*"Powerpoint. The more time I spend automating, the more time I end up spending redoing stuff in powerpoint."*
  - **OmniGraffle / Mathcha / Draw.io 派**：
    - `u/hendriksc`（`18qzdnj`）：Mac 端使用 **OmniGraffle**，支持直接嵌入 LaTeX 公式；
    - `u/sir_ipad_newton`（`18qzdnj`）与 `u/SulszBachFramed`（`rin63t`）：使用 **[Mathcha](https://www.mathcha.io/)** 可视化手绘框图与数学公式，并可直接导出为原生 `TikZ` 代码；
    - `u/sanjuromack` & `u/Grove_street_home`（`rin63t`）：推荐 `draw.io` 离线桌面客户端（`jgraph/drawio-desktop`），以及 `PlotNeuralNet` 中的 `examples/Unet_Ushape`（`u/dojoteef`）。
  - **纯 TikZ 独立编译派**：
    - `u/PatWie_`（`8s0uu1`）：使用 `pdflatex` 下的 `\PreviewEnvironment{tikzpicture}` 将每张网络图单独编译为独立 PDF，配合 `tikz spy` 宏包做局部放大框（zoom-ins），优势在于字号与正文字体天然一致、单双栏与海报复用无损、`.tex` 图源码与论文同库 Git 版本管理。

---

### 1.3 Draw.io（`diagrams.net`）与 Figma / Visio 科研架构图实战流

#### [9] 知乎专栏《论文流程图用什么软件画？10款常用流程图工具盘点》（2026-03-12）
- **作者 / 平台**：知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/2015525043938018372
- **核心实战技巧整理**：
  - **Draw.io 自带 XML 源码的 PNG/SVG 保存技巧**：「draw.io 可以存成自带 XML 数据的 PNG 图片。万一原工程文件找不到了，直接把这张 PNG 图片拖进 draw.io 网页，照样能修改里面的文字和框线；同时支持在节点中开启 LaTeX 数学公式渲染。」
  - **Figma / Pixso / Sketch 设计类矢量流定位**：当论文需要视觉表现力强的封面图、Graphical Abstract 或现代扁平风研究框架图时，Figma 的矢量布尔运算、组件对齐与色彩样式管理比传统流程图软件更顺滑。
  - **Microsoft Visio 与 Office 联动**：工程与系统类论文将 Visio 图嵌入 Word 后可直接双击原位唤起编辑，或导出矢量 PDF 插入 LaTeX。

#### [10] 飘雷（少数派 sspai，2026-07-12）—《动动嘴就能画架构图？NAS一键部署Next-AI-Draw.io，让AI替你打工》
- **作者 / 平台**：飘雷（`sspai.com/u/sfidwjl6`）｜少数派（sspai）
- **原始 URL**：https://sspai.com/post/112208
- **核心实战经验整理**：
  - 实测开源项目 `DayuanJiang/next-ai-draw-io`（https://github.com/DayuanJiang/next-ai-draw-io ）：底层为标准 `draw.io` 画布，右侧接入 Claude / OpenAI / Gemini / DeepSeek API；先用自然语言让大模型自动生成 `.drawio` 节点排布与连线，再直接在左侧 `draw.io` 面板手动拖拽微调文字、对齐与箭头锚点，支持历史版本回退与矢量导出。

#### [11] `icebird1998/drawio-scientific-illustrator` & `ywq177995212697-droid/visio-scientific-figures`（GitHub 开源实战仓库）
- **作者 / 平台**：`icebird1998` & `ywq177995212697-droid`｜GitHub
- **原始 URL**：
  - https://github.com/icebird1998/drawio-scientific-illustrator （MIT，Commit `9bbeca93ffd134a29bfc90023f22c65359efe584`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/drawio-sci-illustrator/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/drawio-sci-illustrator/)）
  - https://github.com/ywq177995212697-droid/visio-scientific-figures （MIT，Commit `d9e5191d56640af4c7b28f30eb90f11d8cbaf2fc`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/ywq177995212697-visio-scientific-figures/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/ywq177995212697-visio-scientific-figures/)）
- **核心实战经验整理**：分别针对 `draw.io` 实时画布与 `Microsoft Visio` 提供从论文结构化 YAML 规范生成原生可编辑科研框架图的分步构建与质量门禁规则。

---

### 1.4 Inkscape + LaTeX / Matplotlib 矢量科研插图实战工作流

#### [12] Gilles Castel（Researcher Blog，2019-04-26）& Hacker News 312 赞热议贴 — *How I draw figures for my mathematical lecture notes using Inkscape*
- **作者 / 平台**：Gilles Castel（KU Leuven 数学物理研究者，`castel.dev`）& Hacker News 社区讨论
- **原始 URL**：
  - 博客原文：https://castel.dev/post/lecture-notes-2/
  - Hacker News 讨论贴（312 points，`marcodiego` 提交，2022-05-01）：https://news.ycombinator.com/item?id=31227940
- **核心实战经验整理**：
  - **Inkscape `--export-latex` 双文件分离渲染法**：Gilles Castel 详述了为什么复杂曲线和几何示意图在 Inkscape 中远快于手写 TikZ，同时又完美保留 LaTeX 原生数学排版——导出时启用 Inkscape 的 `PDF+LaTeX`（`--export-latex`）选项，自动拆分为纯图形 `.pdf`（剥离文字）与定位文字的 `.pdf_tex` 文件，在 LaTeX 中 `\incfig` 引入后，图中所有公式和字号随主文档字体自动同步。
  - **HN 学者与工程师补充实测**：
    - `jofer`（HN `31227940`）：区分科研中的概念示意图（"scientific cartoons"）与观测数据图（"data figures"），指出 *"A cartoon is the highest form of scientific communication"*，Illustrator 功能虽强，但快速绘制极简科学概念图是 Inkscape 的甜点区；
    - `baby`（*Real-World Cryptography* 作者 David Wong，HN `31227940`）：早期写论文执迷于毫米级精度的 TikZ，但耗时极其夸张，最终整本密码学专著的所有矢量插图全部改用 **Keynote** 高效完成。

#### [13] Oxford Protein Informatics Group (BLOPIG，2026-02) — *Creating scientific figures in Inkscape*
- **作者 / 平台**：Oxford Protein Informatics Group（牛津大学蛋白信息学课题组博客 `blopig.com`）
- **原始 URL**：https://www.blopig.com/blog/2026/02/creating-scientific-figures-in-inkscape/
- **核心实战经验整理**：
  - **Matplotlib SVG + Inkscape `TexText` 插件工作流**：
    1. Python 端先调 `plt.tight_layout()`，再用 `plt.savefig("filename.svg", dpi=300)` 保存为矢量 SVG；
    2. 在 Inkscape 中安装 **[TexText](https://github.com/textext/textext)** 插件并配置 `amsmath` 导言区，实现在矢量画布内随时二次编辑重编译 LaTeX 公式；
    3. **嵌入（Insert）vs 链接引用（Reference）两种模式的取舍**：直接嵌入 SVG 后按 `Cmd+Shift+G` 解组（或右键 `Enter Group`）、按 `N` 键进入节点工具可自由改任意坐标轴与数据点样式，但更新实验数据后需重调；以文件引用方式链入则修改数据重跑 Python 脚本后 Inkscape 拼图会自动同步更新。

---

### 1.5 TikZ 代码流与手绘转 TikZ / 可视化编辑器讨论

#### [14] Chaoqi Liu（Researcher Blog）—《AI 时代如何制作科研图表和 PPT》
- **作者 / 平台**：Chaoqi Liu（研究者独立博客 `chaoqi-liu.com`）
- **原始 URL**：https://chaoqi-liu.com/blog/ai-era-figures-slides/zh/
- **核心实战经验整理**：
  - **核心主张**：「用 Python（Matplotlib）做数据探索与快速诊断；当论文论点稳定进入定稿层时，将折线图、分组柱状图、热力图与示意图迁移为原生 **TikZ** 源码。」
  - **痛点复盘**：外部导入的 Matplotlib PDF 在 LaTeX 双栏/单栏切换时经常出现「字体像从另一个世界来的、有的标签在单栏太小换位置又太大」的割裂感；过去不写 TikZ 是因为人类手写几百行坐标成本太高，AI 编程助手改变了成本曲线。
  - **防 AI 篡改实验数据的六步可检查工作流（原文 01–06）**：
    1. **锁定论点**：先写清图注必须支撑的那句话；
    2. **锁定唯一数据源**：把数值放在独立 JSON / CSV / 表格宏里，绝不让图源码成为数据唯一存在处；
    3. **生成 TikZ 框架**：明确告知 AI 论文栏宽、字体环境、面板结构、图例与视觉主次；
    4. **把依赖数据的部分机械化**：用 Python 脚本从 JSON 计算/生成坐标、柱高和单元格数字；
    5. **编译、检查、小步修改**：每次给出具体指令（如「左侧标签和刻度撞了」「两列共用一个图例」），严禁为好看手动挪动科学数值；
    6. **把数值校验脚本放在图旁边**：每次 AI 改图必须同步跑通校验脚本。

#### [15] Hacker News 热门讨论 — TikZ 生态、自动布局边界与可视化编辑器
- **平台与原始 URL（3 篇 HN 讨论贴）**：
  1. `JohnHammersley` et al. (199 points, 2021-08-21), *"Tikz.net – Graphics with TikZ in LaTeX"* — https://news.ycombinator.com/item?id=28260875
  2. `potamides` et al. (132 points, 2024-06-06), *"Show HN: Synthesize TikZ Graphics Programs for Scientific Figures and Sketches (`DeTikZify`)"* — https://news.ycombinator.com/item?id=40596711
  3. `DominikPeters` et al. (451 points, 2026-06-23), *"Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX (`tikz.dev/editor`)"* — https://news.ycombinator.com/item?id=48645437
- **真实网友高赞经验摘录**：
  - **TikZ vs Graphviz 选型边界**（`JoshTriplett`，HN `28260875`）：如果你在乎节点精确位置、角度锚点（如“从节点 A 轴上方 30° 平滑连到节点 B 的 150°”）与宏复用，选 **TikZ**；如果只想声明拓扑连接关系而不关心节点具体摆在哪，选 **Graphviz**。
  - **Overleaf 编译超时坑点**（`63`，HN `28260875`）：论文中包含大量 TikZ/PGF 图时极易触发 Overleaf 免费版编译超时，务必本地编译或预编译为独立 PDF。
  - **可视化微调旧 TikZ 源码**（`Littice` & `j2kun`，HN `48645437`）：`tikz.dev/editor/` 最大的实用价值是直接可视化微调旧 TikZ 代码而不把源码污染成不可读的机器乱码；交换图表（commutative diagrams）则推荐专用可视化转 TikZ 工具 **[quiver (`q.uiver.app`)](https://q.uiver.app/)**。

---

### 1.6 AI 辅助科研架构图与机理图**原版 Prompt** 与多轮精修实测贴

#### [16] 胡拉图说（少数派 Matrix 首页推荐，2026-11-13）—《研究生如何用 AI 辅助完成一篇综述：我的科研写作工具与实践经验》
- **作者 / 平台**：胡拉图说（`sspai.com/u/hulatu`）｜少数派（sspai）
- **原始 URL**：https://sspai.com/post/118153
- **实战工作流**：「已核对综述正文段落 → ChatGPT 生成视觉分区与高分辨率科研机理草图 → 人工排查 4 类 AI 幻觉错误（箭头方向反、凭空捏造反应物、过程混杂、术语不准） → 导入 **Keynote / PowerPoint** 从局部到整体逐块矢量临摹（搭配 Bioicons、SciDraw、Reactome、Smart Servier 开源科学图标库） → Keynote 导出『最佳质量 PDF』再用 macOS『预览（Preview）』指定 `300` 或 `600 DPI` 无损转出 TIFF/PNG 投稿。」
- **作者公开的科研机理图 / Graphical Abstract 原版完整 Prompt**：
  ```text
  # 角色设定
  你现在是一位专业的科研绘图设计师，擅长为高水平学术期刊绘制清晰、规范的机理示意图（Mechanism Diagram / Graphical Abstract）。

  # 任务目标
  请根据我提供的综述正文段落，先为我梳理出机理图的「视觉排版方案」，再调用绘图工具生成一张高分辨率的科研机理草图，作为我后续使用 Keynote 临摹和排版的视觉参考框架。

  # 待可视化的综述正文内容
  【在此处粘贴你已经核对好的综述正文段落，如：原料前处理、固态发酵过程或产物转化机制】

  # 作图具体要求
  1. 逻辑与分区：请先用文字简要说明你打算如何分区（例如：采用「从左到右」的工艺流程布局，或「上下分层」的宏观-微观机制布局），提取出 3～4 个核心阶段，并用清晰的箭头指示物质转化或作用方向。
  2. 视觉风格：采用扁平化、现代的 2D 科研矢量插画风格（参考 BioRender 或主流 SCI 期刊配图风格）。纯白色背景，配色简洁克制（主色调不超过 3 种，建议采用清新、柔和的学术配色），严禁出现杂乱的 3D 渲染、科幻光效或过度写实的复杂背景。
  3. 元素与标注：尽量使用直观的科学图标、简化的分子/细胞结构或实验器材示意图形，减少大段文字堆砌，仅在关键节点保留简短的英文核心词汇作为占位标签（方便我后续在 Keynote 中替换为准确的中文或规范术语）。
  4. 严谨性约束：画面中出现的所有反应步骤、物质元素和箭头指向，必须严格基于我提供的正文内容，不得凭空捏造未提及的反应路径或实验设备。
  ```

#### [17] Reddit `r/LaTeX`（`u/max_confused`）— iPad GoodNotes 网格手绘批量转 TikZ 原版 Prompt
- **作者 / 平台**：`u/max_confused`（回复 `u/nnenneplex`）｜Reddit `r/LaTeX`
- **原始 URL**：https://www.reddit.com/r/LaTeX/comments/1egfaqf/how_do_you_use_tikz/
- **实战工作流与原版英文 Prompt**：
  1. 在 iPad GoodNotes 中开启网格辅助线整齐手绘框图（每个图外画边界框并在下方手写图注），导出 PDF 时关闭网格背景保留纯白底；
  2. 将 PDF 附件上传至 ChatGPT 并附上以下原版 Prompt：
  ```text
  I have attached a PDF which contain 13 figures. Please convert them into Tikz codes and provide me the code for each figure in a separate code block. Keep the figure width to 45% of the textwidth. Scale height maintaining aspect ratio of the original hand drawn figure. Use the text below each figure to assign captions to each figure. Name the figure labels as "fig:diagX" where X stands for the position of the figure in the PDF document.
  ```

#### [18] CoderJia（知乎专栏，2025-03-28）—《解锁 Claude 的 SVG 绘图能力》
- **作者 / 平台**：CoderJia（`zhihu.com/people/CoderJia`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/1889232628172948597
- **实战工作流与原版 SVG 知识图解 Prompt**：横向对比 Claude 3.7 Sonnet、Gemini 2.0 Pro、DeepSeek V3、GPT-4o 直接生成可缩放矢量 SVG 示意图的效果，指出生成后若局部有多余黑色箭头等瑕疵，可直接拖入在线 SVG 编辑器或 Illustrator 删改节点。文中收录的原版三阶段 SVG 生成 Prompt：
  ```text
  请仔细阅读下面的文章，并按照以下步骤创建一个引人入胜且信息丰富的SVG知识图解：
  1. 分析阶段：
  • 识别并提取文章中的核心概念、关键观点和它们之间的逻辑关系
  • 确定最适合表达这些内容的图解类型（思维导图、流程图、概念图、比较图等）
  • 考虑目标受众和他们的认知需求
  2. 设计阶段：
  • 创建清晰的视觉层次结构，突出最重要的信息
  • 使用适当的视觉隐喻和符号，使抽象概念更容易理解
  • 应用一致的配色方案（3-5种互补色），增强可读性和美感
  • 平衡文字与视觉元素，确保简洁性和完整性
  • 使用视觉分组、对比和空间关系传达概念间的联系
  3. 优化阶段：
  • 简化复杂信息，去除不必要的细节
  • 确保图解自成一体，无需原文也能传达完整信息
  • 验证图解是否准确反映了原文的核心思想
  请使用SVG格式创建这个知识图解，确保它既能独立传达核心信息，又能以视觉上吸引人的方式呈现。图解应该是概念性的，而不仅是文本内容的重新排列。
  ```

#### [19] 京东云技术团队（知乎专栏，2026-08-03）—《实测 9 款 AI 架构图工具：从 Mermaid 美化到 GPT-Image2，一份选型清单》
- **作者 / 平台**：京东云（`zhihu.com/org/jing-dong-yun-32`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/2067617350732535450
- **核心实测选型结论**：「DSL 让架构图从『图形资产』变成了『代码资产』。想要 Mermaid 美化选 `beautiful-mermaid`（输出 SVG + Unicode + Mermaid 源码）；想要 14 类工程与 Agent 架构图选 `fireworks-tech-graph`；想要可长期手动维护的 `.drawio` 源文件选 `drawio-skill` 或 `next-ai-draw-io`。」

#### [20] AJE学术交流（科学网博客，2025-12-05）—《实用指南！用Nano Banana Pro制作论文插图，附Prompt》
- **作者 / 平台**：AJE学术交流（`blog.sciencenet.cn/u/AJE2017`）｜科学网博客
- **原始 URL**：https://blog.sciencenet.cn/home.php?mod=space&uid=3344631&do=blog&id=1513096
- **核心实战经验与避坑提醒**：
  - 使用 Thinking 推理模式组织五要素 Prompt：**主题/主体**（如 `"a signaling pathway diagram of MAPK cascade"`）+ **风格**（`"technical blueprint-style"`, `"clean infographic"`, `"isometric view"`）+ **注释**（明确需标注的分子/模块名与箭头激活方向）+ **布局/颜色**（`"white background, minimalistic"`, `"muted pastel colors"`）+ **参考图引导**（`"use the uploaded diagram for layout guidance"`）；迭代时使用单点局部指令（`"make the arrow thicker"`, `"add a box around protein name"`）。
  - **关键局限警示**：复杂机制图中模型仍可能因追求“视觉对称合理”而把**抑制箭头画反**或擅自重排实验步骤顺序，定稿前必须导入 Illustrator / PowerPoint / Inkscape 人工逐项核验科学逻辑。

#### [21] `james20141606/sci-figure-workflow` & `LigphiDonk/academic-figure-generator`（GitHub 中文开源原版 Prompt 仓库）
- **作者 / 平台**：`james20141606` & `LigphiDonk`｜GitHub 中文仓库
- **原始 URL**：
  - https://github.com/james20141606/sci-figure-workflow （Commit `5c70a24be780338a77ed3a2071f7d0aa0026d39d`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/james20141606-sci-figure-workflow/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/james20141606-sci-figure-workflow/)）
  - https://github.com/LigphiDonk/academic-figure-generator （MIT，Commit `0a2bec6bb56d6b47143a81909f8d818716bdcbab`，已归档于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/LigphiDonk-academic-figure-prompts/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/LigphiDonk-academic-figure-prompts/)）
- **核心实战经验整理**：
  - `sci-figure-workflow` 提出四步管线（① Gemini Vision / GPT 提取 JSON/中文结构规格 → ② GPT-image-2 / Nano Banana 2 按规格生图，末尾必加硬约束咒语 `Do not simplify, follow every detail exactly.`，且**多轮迭代每轮只改一处** → ③ 并行转 `.drawio` / `.pptx` / `.svg` 可编辑格式 → ④ 人工精修并过生产级细节清单）。
  - `LigphiDonk/academic-figure-generator` 在 `academic-figure-prompt/SKILL.md` 中定义四层高密度英文架构图 Prompt 模板（Global Description → `=== SECTION NAME ===` 分区框体与子组件细节 → Global Annotations 张量维度如 `"X ∈ R^(120×6)"` 与跳接虚线 → Style Specifications 精确 HEX 色板），强调「每个模块框内部都必须有子内容，不允许出现空白占位框」。

---

## 第二部分：Nature / Science / Cell 多面板拼图、字体嵌入（`pdf.fonttype=42`）、矢量导出与审稿人拒稿配图问题实测

### 2.1 Nature 子刊级多面板拼图（Multi-panel Layout）Adobe Illustrator 与 Inkscape 实操贴

#### [22] 开心重要（知乎专栏，2024-05-28）—《导师：你还在用PPT组图排版？试试AI吧！》（复现 *Nature Microbiology* 多面板组图全流程）
- **作者 / 平台**：开心重要（`zhihu.com/people/wen-ming-xing-79`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/700363938
- **核心实操参数与技巧整理（以复现 *Nature Microbiology* Fig. 3 为例）**：
  1. **新建标准画板**：按 *Nature* 双栏竖版建立画板，**宽度 `183 mm`**，最大高度 **`247 mm`**，颜色模式选 **RGB**，打开标尺并从标尺拖出水平/垂直参考线对齐各面板标签。
  2. **字号与字体层级**：全局统一使用英文无衬线体 **`Arial`**；子图编号标签（小写 **`a`、`b`、`c`**）设为 **`12pt` 加粗（Bold）**；子图内部坐标轴与标注文字统一设为 **`8pt`**；坐标轴与框线粗细统一设为 **`0.75pt`**。
  3. **置入 R / Python 导出的矢量 PDF 子图与去白板坑点**：
     - 缩放子图时**必须按住 `Shift` 等比例缩放**，严禁非等比拉伸导致文字和散点变形；
     - **清除底层白板与剪切蒙版**：R / Python 导出的 PDF 置入 AI 后自带白色底板，会遮挡相邻子图并阻碍点选内部元素，需选中白板按 `Delete` 删除（露出底层网格线）。
  4. **批量统一全图字体与线宽快捷键**：
     - 全图改字：`菜单栏 → 选择 → 对象 → 所有文本对象`，一键将所有子图字体统一改为 `Arial 8pt`；
     - 批量改同色箱体或 `0.75pt` 坐标轴线宽：使用左侧**魔棒工具（Magic Wand）**或 `选择 → 相同 → 填色颜色 / 描边粗细` 批量修改。
  5. **双格式归档与导出**：同时保存可编辑 `.ai` 与矢量 `.pdf` 用于投稿；若需导出位图用于汇报，选择 `文件 → 导出 → 600 ppi`（最低不小于 `300 ppi`）。

#### [23] Reddit `r/AskAcademia` 网友高赞经验贴 — 多面板大图为什么不能在 Overleaf / LaTeX 里强行缩放？
- **平台与原始 URL（2 篇实测贴）**：
  1. `u/coronary-service` et al., *"How do people make nice figures for their papers?"* (`r/AskAcademia`) — https://www.reddit.com/r/AskAcademia/comments/19bs8q1/how_do_people_make_nice_figures_for_their_papers/
  2. `u/kidsweekend` et al., *"STEM scholars: how do you produce tables, graphs, charts for publication?"* (`r/AskAcademia`) — https://www.reddit.com/r/AskAcademia/comments/4zo73s/stem_scholars_how_do_you_produce_tables_graphs/
- **核心实战避坑经验摘录**：
  - **禁止画完再在 Overleaf 缩放导致字号崩坏**（`u/confusedpsycopath`，`19bs8q1`）：期刊通常全栏宽 `7 inch`、半栏宽 `3.5 inch`。画子图前**必须先根据最终拼图版面固定每个子图的物理 `figsize` 与字号**（半栏图 `6–7pt`，全栏图 `8–10pt`）；如果在 Matplotlib 里用 6pt 画了一张大图再在 Overleaf 里缩放到半栏，实际字号会缩成不可读的 `3pt`！
  - **Inkscape 零缩放描边失真技巧**（`u/gregysuper`，`19bs8q1`）：
    1. Inkscape 默认画布直接设为论文版心宽度，杜绝导入 Overleaf 时二次缩放；
    2. 导入仿真软件/Matlab/Python 导出的 `.pdf` 后，全选按 `T` 键统一字体；
    3. **在 Inkscape 内缩放子图时，务必取消勾选工具栏的「缩放对象时同步缩放描边宽度（When scaling objects, scale the stroke width by the same proportion）」按钮并锁定纵横比**，否则坐标轴线宽会变得粗细不一；
    4. 选中全部内容导出 `.pdf`（自动零白边裁剪）。
  - **位图切忌用有损 JPEG 伪装成 TIFF**（`u/OrbitalPete`，`4zo73s`）：连续色调照片/显微图位图标准不低于 `300 ppi` 并保存为无损 `TIFF`；一旦先存成有损压缩的 `JPEG` 出现伪影，后续再另存为 `TIFF` 也无法恢复画质。

---

### 2.2 Matplotlib `pdf.fonttype = 42`、Type 3 字体报错与 Linux HPC 缺字体实测贴

#### [24] Jamie Oaks（Researcher Blog `phyletica.org`，2014-03-01）— *Avoiding Type 3 fonts in matplotlib plots*
- **作者 / 平台**：Jamie Oaks（Auburn University 进化生物学家）｜个人学术博客 `phyletica`
- **原始 URL**：http://phyletica.org/matplotlib-fonts/
- **核心实测结论**：
  - 投稿上传 **ScholarOne Manuscript Central** 时因 PDF 插图含 Type 3 PostScript 字体被系统拒收，定位根因是 Python `matplotlib` 默认将 `pdf.fonttype` 与 `ps.fonttype` 设为 `3`（Type 3 位图化字体）。
  - **标准修复代码（写入脚本开头或 `matplotlibrc`）**：
    ```python
    import matplotlib
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    ```
  - **为什么不推荐盲目开启 `text.usetex = True`**：作者实测指出，虽然 `matplotlib.rcParams['text.usetex'] = True` 也能强制生成 Type 1 字体，但它会显著改变图内字体外观，且当坐标轴字符串包含下划线或特殊字符时会与 TeX 语法冲突导致乱码或报错；改为 `42`（TrueType）可在完全不改变图像外观的前提下一次重跑通过投稿系统检测。

#### [25] Jonathan Soma（Columbia Journalism School 教程）— *Exporting from matplotlib to open in Adobe Illustrator*
- **作者 / 平台**：Jonathan Soma｜`jonathansoma.com`
- **原始 URL**：https://jonathansoma.com/lede/data-studio/matplotlib/exporting-from-matplotlib-to-open-in-adobe-illustrator/
- **核心实测技巧**：
  - **解决 Illustrator 打开 Matplotlib PDF 文字变碎片形状无法编辑的问题**：默认 Type 3 字体导入 Adobe Illustrator 后每个字母都会变成不可编辑的轮廓碎片；执行以下命令永久写入全局配置后，导出的 `.pdf` 在 Illustrator 中即为完整可编辑文本：
    ```bash
    mkdir -p ~/.matplotlib
    echo 'pdf.fonttype: 42' >> ~/.matplotlib/matplotlibrc
    echo 'ps.fonttype: 42' >> ~/.matplotlib/matplotlibrc
    ```
  - **Illustrator 友好的导出参数**：导出时加 `plt.savefig("output.pdf", transparent=True)` 去除白色背景层；画柱状图加 `linewidth=0`、画散点图加 `markeredgewidth=0`，避免在 Illustrator 里多出一圈难以清理的隐形描边圆环。

#### [26] 佐记妙妙屋 / 别玩了该学了 / 田源（知乎专栏 3 篇投稿系统字体报错实录）& Matplotlib Issue #11303
- **作者 / 平台 / 原始 URL**：
  1. **佐记妙妙屋**（2023-04-02）《VLDB论文发表之神秘的字体》— https://zhuanlan.zhihu.com/p/609500904
  2. **别玩了该学了**（2021-01-30）《Matplotlib中使用Type 1/TrueType字体、嵌入子集、中文、使用Latex的总结》— https://zhuanlan.zhihu.com/p/348169013
  3. **田源**（2025-04-28）《IEEE PDF Express/EDAS 上传失败，请检查字体设置》— https://zhuanlan.zhihu.com/p/694986593
  4. **Matplotlib 官方仓库讨论** Issue #11303 (*"Using fonttype 42 will make the produced PDF size considerably larger"*) — https://github.com/matplotlib/matplotlib/issues/11303
- **核心实测数据与应急排障汇总**：
  - **IEEE EDAS / PDF eXpress / PVLDB 典型报错原文**：
    ```text
    fonttype: Upload failed: Font DejaVuSans-Bold is of type Type 3.
    Errors: Font Helvetica-BoldOblique, Helvetica-Oblique is not embedded
    ```
  - **本地自检命令**（佐记妙妙屋 `p/609500904`）：提交 Camera-ready 前用 Poppler 工具链执行 `pdffonts <your_paper.pdf>` 检查是否存在任何 `Type 3` 或 `emb=no` 字体。
  - **`pdf.fonttype=42` 文件体积暴涨痛点与 `pgf` 子集嵌入解法**（别玩了该学了 `p/348169013` & Matplotlib `#11303`）：
    - 同一张 Helvetica 图实测对比：`pdf.use14corefonts = True` 仅 **`4 KB`**（但仅限 14 种 PostScript 核心英文字体，注意 `Times Roman` 与 `Times New Roman` 不同）；`pdf.fonttype = 42` 在部分版本中会将整套 TrueType 字库全量嵌入，导致单图暴涨至 **`973 KB`**（多张图合并后易超会议投稿体积上限）；
    - **兼顾任意 TrueType/中文字体与极小体积的方案**：切换 `plt.switch_backend('pgf')`，自动执行 **TrueType Embedded Subset（子集嵌入）**，同一张图体积仅 **`14 KB`**！
  - **丢失作图源码时的 Inkscape 救急转曲法**（田源 `p/694986593`）：若旧 PDF 插图源码已不可重跑，用 Inkscape 打开该 PDF → `Ctrl + A` 全选 → `Path -> Object to Path` → 另存为 PDF 时勾选 `Convert text to paths`，将文字彻底转为矢量几何路径即可绕过 EDAS Type 3 检测。

#### [27] Harriet Alexander（Alexander Lab @ WHOI，2021-03-30）— *Fixing my matplotlib font woes*
- **作者 / 平台**：Harriet Alexander（Woods Hole Oceanographic Institution 海洋生物学家）｜课题组博客 `alexanderlabwhoi.github.io`
- **原始 URL**：https://alexanderlabwhoi.github.io/post/2021-03-missingfont/
- **核心实测排障方案（远程 Linux 服务器画图找不到 Arial / Times New Roman 退回 DejaVu Sans）**：
  - **现象**：在远程 Linux HPC / SSH Jupyter 上设了 `Arial` 仍不断报 `findfont: Font family ['sans-serif'] not found. Falling back to DejaVu Sans.`，根因是 Linux 服务器未装微软核心字库且 Matplotlib 缓存了旧字体索引。
  - **三行命令根治方案（无需管理员 root 权限）**：
    ```bash
    conda activate <your_plotting_env>
    conda install -c conda-forge mscorefonts
    rm ~/.cache/matplotlib -rf
    ```

---

### 2.3 期刊投稿矢量格式、DPI 分辨率红线与审稿人常见返修/拒稿配图痛点

#### [28] 科学网编辑部（科学网精选博文，2025-09-17 & 2026-03-25）— 顶刊图片格式硬指标与「插图 AI 感太重」审稿新雷区
- **作者 / 平台**：科学网编辑部（`blog.sciencenet.cn/u/科学网编辑部`）｜科学网博客
- **原始 URL**：
  1. 《收藏转发！论文投稿需要注意这些图片要求……》（2025-09-17）— https://blog.sciencenet.cn/blog-45-1502355.html
  2. 《论文投稿新问题！审稿人说插图AI感太重……》（2026-03-25）— https://blog.sciencenet.cn/blog-45-1527261.html
- **核心实测红线整理**：
  - **不同图像类型的硬性物理指标**（`blog-45-1502355`）：
    - **矢量图**：首选 `EPS` / `PDF`，且包含字体的矢量图**必须将字体嵌入文件中**；
    - **纯黑白线条图（Line art）**：所有线条宽度**至少为 `0.1 mm`（`0.3 pt`）**；若为扫描或位图格式，分辨率**不低于 `1200 dpi`**；
    - **组合图（图文混合 / 照片+曲线组合）**：分辨率**不低于 `600 dpi`**；
    - **半色调图（连续灰度照片/电镜/染色图）**：分辨率**不低于 `300 dpi`**，存在放大效果的显微照片**必须在图内标明比例尺（Scale bar）**；
    - **色彩模式与栏宽**：彩色插图以 **RGB** 模式提交；常见期刊标准栏宽为 `39 mm`、`84 mm`（单栏）、`129 mm`（1.5 栏）或 `174 mm`（双栏），高度不超过 `234 mm`（*Nature* 单栏 `89 mm` / 双栏 `183 mm`）。
  - **审稿人拒稿新槽点——「插图 AI 感太重」**（`blog-45-1527261`）：
    1. *Nature*、*Science* 等顶刊明令禁止直接使用生成式 AI 图像作为正式科研插图；
    2. 文生图直出的模式化发光质感、塑料3D渲染、解剖/分子结构失真与错乱细节极易被审稿人一眼识破，甚至触发学术不端核查；AI 仅能作为前期构图草稿参考，正式投稿插图必须重绘为严谨可控的矢量元素。

#### [29] Taylor & Francis 学术服务（科学网精选博文，2026-06-02）—《英文论文总返修？收好这篇国际期刊图表和表格规范，论文更易过审！》
- **作者 / 平台**：Taylor & Francis 学术服务（`blog.sciencenet.cn/u/tandfmarketing`）｜科学网博客
- **原始 URL**：https://blog.sciencenet.cn/blog-3574014-1537519.html
- **审稿人高频要求大修的三大图表通病**：
  1. **图文高度重复、丧失独立可读性（Self-contained）**：正文逐条罗列数据后又在图表中原样复刻；正确规范是「读者仅凭图题、图例和注释无需翻阅正文即可完整读懂实验维度与结论，正文只提炼趋势与关键差异」。
  2. **单张图表强塞过多维度、无视目标期刊栏宽**：字迹拥挤、缩印后无法辨认；复杂数据集应拆分为多张主次分明的图表或移入 Supplementary Material。
  3. **误解无格式投稿（Format-free Submission）**：无格式投稿仅放宽初审版式模板，但审稿人对图表独立可读性、误差棒/统计显著性标注及表图分工（表格管精准量化数值对比，图表管趋势与规律）的审核标准从未降低。

---

## 第三部分：科研配色与图表美化真实网友及学者经验贴

### 3.1 研之成理与知乎高赞科研配色方法论

#### [30] 研之成理 · 钟老师科学可视化工作室（微信公众号 `rationalscience` / 知乎专栏归档，2017-03-14）—《推荐：如何选取论文图以及/PPT中的配色？》
- **作者 / 平台**：研之成理（`zhihu.com/people/yan-zhi-cheng-li-41`，微信公众号 ID：`rationalscience`；另见谷战军课题组归档页 `http://m.guzjlab.org/nd.jsp?id=123`）｜知乎专栏 / 公众号归档
- **原始 URL**：https://zhuanlan.zhihu.com/p/25512856
- **核心六条科研配色实战法则（原文归纳）**：
  1. **单图主色上限**：「颜色过于鲜艳、每个元素都太明亮，会导致图中作者要表达的科学信息不明确。**每张图最多选取 2–3 种主要颜色**，然后通过改变明暗程度（加白/加黑）以及饱和度来衍生更多色彩组合。」
  2. **色轮互补色与相似色**：色轮呈 180° 的互补色（如**蓝+橙**）具有高对比度，适合制造强区分；相邻的三个相似色（如蓝绿、蓝、蓝紫）适合在同一色调内营造质感与层次。
  3. **冷暖色视觉进退分工**：「暖色调（红、黄、橙）在视觉上给人以『前进』的感觉，用于突出想强调的核心部分；冷色调（蓝、紫、灰）作为背景、陪衬色或次级重要元素。」
  4. **全文跨图语义一致**：同一篇论文或报告中，相同的实验组/物质/模块在所有子图和幻灯片中必须锁定同一种颜色。
  5. **焦点色（Focal Color）+ 灰度降噪**：对唯一核心结论选用一个明亮主色，其余次要对照全部压暗为中性灰色。
  6. **调色面板优先用 HSL 而非 RGB 或软件默认标准十色**：PPT / 绘图软件预置的标准十色饱和度过高且跨度生硬；切到自定义颜色的 **HSL（色调-饱和度-亮度）** 模式压低饱和度、拉开亮度梯度，远比直接拉 RGB 滑块更容易调出协调学术色。

#### [31] 墨水叛逃事件（知乎专栏，2025-06-28）—《科研绘图颜色搭配万能公式：记住这3个色号就够了》
- **作者 / 平台**：墨水叛逃事件（`zhihu.com/people/43-38-8-6-49`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/1922264380688560782
- **核心实测三色公式与比例**：
  - 统计数百篇 *Nature* / *Science* 论文图表后提炼的稳妥**「蓝-橙-灰」三色 RGB/HEX 组合**（兼具互补高对比度、低饱和学术感与红绿色盲安全）：
    1. **重点蓝（主数据 / 核心变量）**：`RGB(43, 85, 125)`（即 `#2B557D`）
    2. **对比橙（强调组 / 次要关键变量）**：`RGB(247, 144, 61)`（即 `#F7903D`）
    3. **中性灰（对照组 / 基线参考线）**：`RGB(127, 127, 127)`（即 `#7F7F7F`）
  - **60-30-10 面积比例法则**：60% 主色调（如蓝色系）、30% 辅助色（如橙色系）、10% 强调或参考点缀色。

#### [32] 麦德辑学术（知乎专栏，2023-09-20）—《科研绘图教程｜如何利用illustrator自带的着色功能来给你的科研绘图配色》
- **作者 / 平台**：武汉麦德辑科技有限公司 / 麦德辑学术（`zhihu.com/org/wu-yi-mai-de-ji-ke-ji-you-xian-gong-si`）｜知乎专栏
- **原始 URL**：https://zhuanlan.zhihu.com/p/657495403
- **核心实操技巧**：针对和弦图、复杂多组柱状图等难以逐块手调颜色的图形，在 Adobe Illustrator 中先对黑白线稿随机填上区分色，全选后点击顶部色轮图标打开**「重新着色图稿（Recolor Artwork）」** → 点击「颜色库 → **科学（Scientific）→ 分裂互补色 / 互补色 / 类似色**」，即可一键联动旋转色轮或单独解锁微调某一元素饱和度与明度。

---

### 3.2 *Nature* / *Science* 顶刊取色实测贴与中文开源配色库

#### [33] `lcpmgh/colors`（GitHub 中文开源仓库）& 千屈菜 / 模术狮（知乎顶刊取色系列）& AJE学术交流（科学网）& Openbiox Hiplot（少数派）
- **作者 / 平台 / 原始 URL**：
  1. **`lcpmgh`**（GitHub 中文 MIT 开源仓库）— *科研绘图配色推荐器 (`lcpmgh/colors`)*：https://github.com/lcpmgh/colors （Commit `3d744402b1c00b4341a08652c3377941b6aeb639`，已归档纯文本色板 `@palettes.csv` 与 `app.R` 于 [`../upstream-skills/05-chinese-community-and-dataviz-toolkits/lcpmgh-colors/`](../upstream-skills/05-chinese-community-and-dataviz-toolkits/lcpmgh-colors/)）
  2. **千屈菜**（知乎专栏，2024-06-19）—《论文配色：跟着顶刊学配色（Nature篇）》：https://zhuanlan.zhihu.com/p/704390338
  3. **模术狮论文指导与发表**（知乎专栏，2024-06-25）—《跟着【Science】学习科研配色！（持续更新）》：https://zhuanlan.zhihu.com/p/704260077
  4. **AJE学术交流**（科学网博客，2025-06-30）—《顶级期刊配色方案大公开！让你的论文图表更具高级感》：https://blog.sciencenet.cn/blog-3344631-1491791.html
  5. **Openbiox 社区**（少数派 sspai，2020-09-24）—《Hiplot 科研绘图平台免邀请码注册正式开启》：https://sspai.com/post/62875
- **真实开源色值与社区工具链精要**：
  - `lcpmgh/colors` 将知乎顶刊取色贴与 `ggsci` 清洗去重（剔除早期 OCR 取色无效码）整理为 229 组结构化离散色板表 `@palettes.csv`（涵盖 2 色至多色组合，例如双色冷暖对比 `#ACD6EC, #F5A889`、`#91CAE8, #F48892`；三色学术组合 `#1C3C63, #93C8C0, #D3D5D4`、`#2472A3, #A5B55D, #F4F3EE`、`#2C91E0, #3ABF99, #F0A73A`；四色对比组合 `#383838, #5CA7C7, #D4352D, #FBCE6A` 等），并提供双栏实时柱状/散点/箱线图对比预览与透明度滑杆，同时索引了 [Python Color Palette Finder](https://python-graph-gallery.com/color-palette-finder/)、`scico`（科学连续色表）与 `colorspace::hclwizard()`。
  - 千屈菜（`p/704390338`）从 589 篇 *Nature* Article 中提取实刊色卡并同时给出 **HEX、RGB、HSB、CMYK、LAB** 五种色彩空间参数，提醒作者注意屏幕 RGB 显示与印刷 CMYK 油墨色域差异；AJE 学术交流（`blog-3344631-1491791`）则从 *Nature Communications* 归纳出「低饱和莫兰迪系（多组对比耐看）」「高饱和重点突出系（强化单一核心结论）」「自然冷绿系」三类实刊套路。

---

### 3.3 色盲友好（Colorblind-Safe）与多类别色板实战讨论

#### [34] Reddit `r/datavisualization` 网友讨论贴 — 当分类超过 12 类时如何兼顾色盲安全与认知负荷？
- **平台与原始 URL（2 篇讨论贴）**：
  1. `u/Odd-Establishment604` & `u/X28`, *"Color Palette for Colorblindness"* (`r/datavisualization`) — https://www.reddit.com/r/datavisualization/comments/1dkkszj/color_palette_for_colorblindness/
  2. *"The Colorblind Nightmare"* (`r/datavisualization`) — https://www.reddit.com/r/datavisualization/comments/1qxdlwh/the_colorblind_nightmare/
- **核心实战结论**：
  - 约 8% 男性存在色觉缺陷（最常见为红绿色盲），严禁将纯红配纯绿作为图表唯一区分通道。
  - 即便对正常色觉读者，离散分类色板的认知负荷上限通常也在 **8–12 种颜色**以内；当遇到如 19 个病毒门类等超多分类绘图需求时，任何单一色板都无法同时保证三类色盲完全可分（经 R `colorBlindness` 包模拟验证），实战中可参考 **Martin Krzywinski（BC Cancer Genome Sciences Centre）专门设计的 12/15/24 色色盲友好调色板**（https://mk.bcgsc.ca/brewer/ ）与 **Viridis 感知均匀色表**（https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html ），并叠加形状（marker shape）、分面（small multiples）或直接尾部标签替代纯靠颜色硬凑的巨型图例。

#### [35] `LigphiDonk/academic-figure-generator`（GitHub 中文仓库）— 顶会架构图语义化预设色板表
- **作者 / 平台**：`LigphiDonk`｜GitHub 中文仓库（MIT）
- **原始 URL**：https://github.com/LigphiDonk/academic-figure-generator/blob/main/academic-figure-prompt/SKILL.md （Commit `0a2bec6bb56d6b47143a81909f8d818716bdcbab`）
- **原版架构图框体/背景/箭头全链路语义色值表（摘自 `SKILL.md`）**：
  - **方案 A（Okabe-Ito 学术标准，CVPR / Nature / Science 推荐色盲友好）**：主色 Steel Blue `#0072B2`（核心模块边框、节标签、主箭头）、辅色 Warm Orange `#E69F00`（次要模块边框）、点缀色 Bluish Green `#009E73`（输出/结果模块）、警告高亮 Vermillion `#D55E00`、模块填充 Pure White `#FFFFFF`、大区域分组底板 Faint Grey `#F7F7F7`、普通框体边框 Light Grey `#CCCCCC`、正文字色 Charcoal `#333333`、连接箭头 Dark Grey `#4D4D4D`。
  - **方案 C（Teal + Amber，ICLR / NeurIPS 现代风）**：Deep Teal `#00897B` + Amber `#FFB300` + Soft Grey `#ECEFF1`。
  - **方案 D（Navy + Coral，IEEE 沉稳期刊风）**：Deep Navy `#1A3A5C` + Coral `#E05A47` + Warm Sand `#F5ECD7`。
  - **配套在线配色与色盲模拟工具链**：[Coolors](https://coolors.co)、[ColorBrewer 2.0](https://colorbrewer2.org)、Susie Lu 的数据可视化色盲实时模拟器 **[Viz Palette](https://projects.susielu.com/viz-palette)**。
