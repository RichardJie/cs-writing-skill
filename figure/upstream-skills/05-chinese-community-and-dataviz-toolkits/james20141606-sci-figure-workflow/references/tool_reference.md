# 工具速查 + 典型用法

## 速查表

| 工具 | 类型 | 定位 | 推荐场景 | 价格/Key |
|------|------|------|---------|---------|
| **GPT-image-2** | 生图 | 2025 最强生图，多轮迭代 | Step 2 首选；结构复杂、需要精确控制细节的图 | OpenAI API / ChatGPT Plus |
| **Gemini Vision (Gemini 3 Pro)** | 识图 + 文字 | 看图最准、能输出代码 | Step 1 图片分析；Step 3 转 SVG/drawio | Google AI Studio / OpenRouter |
| **Nano Banana 2** | 生图 | flat design 专精 | Mechanism diagram、graphical abstract、简洁 taxonomy | Gemini API（同 Key） |
| **Imagen 4.0** | 生图 | Google 系，风格稳定 | 跟 Gemini 串自动化流时一体化 | Gemini API（同 Key） |
| **PaperBanana** | 生图 + 代码 | 谷歌+北大学术专用 | 直接读论文 → 生成 Matplotlib 代码 | 学术工具 |
| **draw.io / diagrams.net** | 编辑 | 免费矢量编辑器，内置科研图标库 | Step 4 精修首选，能直接打开 .drawio | 免费，桌面+网页 |
| **Adobe Illustrator** | 编辑 | 专业矢量编辑 | 期刊投稿前最终精修，导出 PDF/EPS | 订阅制 |
| **Inkscape** | 编辑 | 免费 AI 替代 | SVG 精修，预算受限时选它 | 免费 |
| **Figma** | 编辑 | 协作设计 | Poster、graphical abstract（团队协作） | 免费 + 付费 |
| **PowerPoint / WPS** | 编辑 | 大众工具 | 改文字、改颜色最快 | 微软/金山 |

## 每个工具的典型用法和坑

### GPT-image-2（Step 2 首选）

**怎么调**：
- ChatGPT Plus 网页版直接用 → 最快上手
- API：`gpt-image-2` 模型，参数 `size: "1792x1024"` (16:9), `quality: "high"`

**常见坑**：
- ❌ 一次想改 5 处 → 它会忘了一半。**每轮只改一处**
- ❌ 中文字符多的 prompt 它会画错 → **prompt 写英文**，原始素材可以中文
- ❌ 不加 `Do not simplify, follow every detail exactly.` → 它会自动"美化"，删掉你写的细节
- ❌ 直接说"美观/专业/清晰" → 它按它的审美来，不符合期刊。**所有诉求翻译成具体规格**（DPI、字号、配色数）

**搭配**：和 Gemini Vision 串—— Gemini 看参考图出结构描述 → 转英文 prompt → GPT-image-2 生图。

### Gemini Vision（Step 1 + Step 3）

**Step 1 用法**：丢参考图 + 用 `prompt_templates.md` 里的"图片模式"模板。Gemini 3 Pro 看图比 GPT-4V 准，特别是颜色和布局。

**Step 3 用法**：满意的 PNG 丢回去，让它输出 SVG / drawio XML / python-pptx 代码。**指定输出格式 + 列出每个元素的 hex 色值**，否则它会瞎猜。

**坑**：
- 转 SVG 时它有时会把 text 转成 outline path → **明确要求 "all text must be real `<text>` elements"**
- 转 drawio 时它可能用错的 mxCell style → 拿到后用 draw.io 打开看一眼，错的话发回去让它修

### Nano Banana 2（Step 2 备选 / 平替）

**适合**：flat design 极简风格、graphical abstract、单图。

**不适合**：5 个以上 panel 的复杂架构图（容易丢细节）。

**坑**：相比 GPT-image-2，多轮迭代能力弱。**第一轮 prompt 一定要写全**。

### draw.io（Step 4 精修首选）

**为什么是首选**：
- 免费 + 离线
- 内置科研图标库（数据库、神经元、 server、CPU、GPU、DNA helix...）
- `.drawio` 文件本质是 XML，diff 友好，团队协作好
- 能直接导出 PNG / SVG / PDF

**精修流程**：
1. 用 Gemini 转好的 `.drawio` 在 https://app.diagrams.net 打开（或下载桌面版）
2. 选中元素 → 右侧面板调 `Style`（颜色、边框、字体）
3. 用左侧 `Search Shapes` 搜科研图标（如 `database`、`neuron`、`gear`）
4. 文件 → 导出为 → SVG / PDF（投稿用 PDF）

**坑**：默认字体不是 Times New Roman → 全选文字 → 字体下拉选 Times New Roman。

### Adobe Illustrator（最后精修）

**何时用**：投顶会/Nature 级期刊，需要逐像素调位置 + 调字距。

**典型操作**：
- 打开 Gemini 转的 SVG
- `Object → Path → Outline Stroke`（防止打印时线条变形）
- `Type → Find Font` 全局替换字体为 Times New Roman
- 导出 → PDF（嵌入字体，subset 100%）

**坑**：Illustrator 打开 AI 生成的 SVG 经常把 path 拆得乱七八糟 → 用 `Pathfinder → Merge` 合并。

### Inkscape（免费 AI 平替）

**适合**：预算紧 + 只做 SVG 编辑。

**和 Illustrator 的区别**：
- ✅ 免费
- ✅ SVG 原生支持，文件更干净
- ❌ 中文字体支持差
- ❌ 高级排版/印刷功能弱

### Figma（协作 / Poster）

**适合**：
- 团队几个人合作改一张大图
- 做学术 poster（A0 大小，多张子图拼接）
- 做 graphical abstract（要在 Twitter/小红书发的版本）

**不适合**：投稿用的高密度架构图（Figma 没专门的科研图标库）。

### PowerPoint / WPS

**适合**：
- 答辩 PPT 用的图（不要求矢量精度）
- 快速把 reviewer 提的"改个字、改个颜色"做掉
- 做规则的流程图（PowerPoint 的 SmartArt 模板够用）

**不适合**：投稿用的最终版本（PPT 导出的 PDF 经常字体走样）。

## 工具组合推荐

按场景挑搭配：

### 投顶会论文图（NeurIPS / ICML / ACL）
`Gemini Vision (理解) → GPT-image-2 (生图) → Gemini Vision (转 SVG) → Illustrator (精修) → 导出 PDF`

### 投 Nature / Science 期刊
`同上，但精修阶段加一步 → 严格按期刊 author guide 调字号/线宽 → 嵌入字体导出 EPS`

### Graphical Abstract（社交传播用）
`Nano Banana 2 (生图，flat design) → Figma (精修，加品牌色)`

### Survey / Taxonomy 图
`Gemini Vision → GPT-image-2 → draw.io（精修，方便团队改）`

### 答辩/汇报 PPT 配图
`GPT-image-2 → Gemini 转 PPTX → PowerPoint 直接改`

### 重做被 reviewer 嫌"图不清晰"的旧图
`原图 → Gemini Vision 出结构描述 + 加上 reviewer 指出的问题 → GPT-image-2 重生 → Illustrator 精修`

## API 成本参考（2026 年初）

| 调用 | 单次成本（粗略） |
|------|----------------|
| GPT-image-2 高质量 1792x1024 | $0.10-0.20 |
| Gemini Vision 看一张图 + 长输出 | $0.01-0.03 |
| Nano Banana 2 1024x1024 | $0.02-0.05 |
| Imagen 4.0 1024x1024 | $0.03-0.06 |

一张图全流程跑下来通常 < $1，比从头自己画半天的时间成本便宜得多。
