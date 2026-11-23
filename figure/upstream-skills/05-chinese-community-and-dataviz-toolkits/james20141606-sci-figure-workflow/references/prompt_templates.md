# Prompt 模板速查

## 核心咒语（每个生图 prompt 末尾必须加）

```
Do not simplify, follow every detail exactly.
```

加强版（用于复杂图）：

```
Do not simplify or omit any element. Follow every detail exactly as specified.
Match all hex colors, arrow types, font sizes, and spatial layout precisely.
```

## Step 1 — 图片模式（复刻参考图）

### 主模板（中文输出）

```
分析这张科研图，输出用于重绘的完整结构描述：
1. 整体布局（横向/纵向/几列/几层）
2. 每个模块的：形状、填充颜色（十六进制）、文字标签、尺寸比例
3. 连接关系：箭头类型（实线/虚线）、方向、粗细、颜色
4. 特殊元素：图标、数学符号、嵌套关系
5. 整体配色方案（列出所有使用的十六进制色值）
请用中文输出，尽量详细，不遗漏任何细节。
```

### 加强版（强制结构化输出）

```
你是一位资深科研图表分析师。请把这张图拆解成以下 JSON 结构（用中文填字段值）：

{
  "layout": {
    "orientation": "横向 | 纵向 | 矩阵",
    "columns": <int>,
    "rows": <int>,
    "panels": [{"id": "a", "label": "...", "position": "..."}]
  },
  "modules": [{
    "id": "...",
    "shape": "矩形 | 圆形 | 六边形 | ...",
    "fill_color_hex": "#......",
    "stroke_color_hex": "#......",
    "label": "...",
    "icon": "如有 emoji 或图标，描述",
    "position": "相对哪个模块、什么方位"
  }],
  "arrows": [{
    "from": "...",
    "to": "...",
    "style": "solid | dashed | dotted",
    "color_hex": "#......",
    "thickness": "1pt | 2pt | ...",
    "label": "如有 label"
  }],
  "color_palette": ["#......", "#......", ...],
  "fonts": {"main": "...", "math": "..."},
  "special_elements": ["..."]
}

不遗漏任何元素。
```

## Step 1 — 文字模式（原创设计）"黄金模板"

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

### 增量补丁

如果产出的英文 prompt 缺细节，追加：

```
请补充以下信息：
- 每个箭头的语义（数据流 / 控制流 / 反馈循环）
- 每种颜色对应的概念（如蓝=输入，绿=处理，红=输出）
- 字号层级（panel label > module title > body text > caption）
- 是否需要分 panel 标注 (a)(b)(c)
```

## Step 2 — 英文生图 prompt 骨架

无论用 GPT-image-2 还是 Nano Banana 2，骨架结构都一样：

```
A publication-quality scientific architecture diagram for a top-tier ML/AI conference (NeurIPS / ICML / Nature).

LAYOUT: <horizontal flow | vertical stack | 3-column | 4-quadrant | matrix>
DIMENSIONS: <16:9 | 4:3 | 1:1>, white background, 300 DPI.

PANELS:
- Panel (a) <name>: <position>, dashed border, contains: ...
- Panel (b) <name>: <position>, dashed border, contains: ...
- Panel (c) <name>: <position>, dashed border, contains: ...

MODULES (per panel, with exact specs):
- "<label>": <shape>, fill #<hex>, stroke #<hex>, position <relative>
- ...

ARROWS:
- <from> → <to>: <solid | dashed>, color #<hex>, thickness <Npx>, label "<text>"
- ...

ICONS / MATH:
- <description of any icons, equations, formulas>

TYPOGRAPHY:
- All text: Times New Roman (or serif), title bold 14pt, module 11pt, caption 9pt italic.
- Math symbols: italic serif, inline.

COLOR PALETTE (semantic):
- #<hex>: <semantic, e.g., "input data">
- #<hex>: <semantic, e.g., "processing">
- #<hex>: <semantic, e.g., "output">
- (max 4 colors)

STYLE: flat design, no shadows, no gradients, no 3D, thin strokes (1px black).

PANEL LABELS: bold, bottom-center of each panel: "(a) <Name>"  "(b) <Name>"  "(c) <Name>"

CAPTION below entire figure: "Figure N: <title>."

Do not simplify, follow every detail exactly.
```

## Step 2 — 多轮迭代话术

每轮只改**一处**。常见迭代指令：

- "Keep everything the same. Only change the color of the 'Encode' box from #FFE4E1 to #D4E4F7."
- "Keep everything the same. Only swap panels (a) and (c) so the order is: Operations → Structures → Forms."
- "Keep everything the same. Only make the arrows in panel (b) dashed instead of solid."
- "Keep everything the same. Only enlarge the panel (c) by 20% to fit longer labels."
- "Keep everything the same. Only replace the icon in 'Memory' with a database stack icon."

如果一次想改多处，**拆成多轮**，不要在一条 prompt 里堆。

## Step 3 — 转可编辑格式 prompt

### 转 SVG（最推荐）

```
Convert this scientific figure into a clean, editable SVG file.

Requirements:
- Each module is a separate <g> group, properly named (id="module-encode" etc.)
- Each arrow is a separate <path> with marker-end for arrowhead
- All text is real <text> elements (NOT outlined paths), in Times New Roman or serif
- Preserve exact hex colors and stroke widths from the source
- Use viewBox for scalability; no embedded raster images
- Add comments inside SVG marking each panel

Output the full SVG code.
```

### 转 PPTX

```
Generate Python code using python-pptx to recreate this figure as an editable .pptx file.

Requirements:
- One slide, 16:9 layout
- Each module = MSO_SHAPE rectangle/oval with editable text and exact hex fill
- Each arrow = MSO_CONNECTOR with the right line style (solid/dashed) and color
- All text is real text frames (editable in PowerPoint), Times New Roman
- Group elements by panel using slide_layouts.shapes
- Save as memory_taxonomy_editable.pptx
```

### 转 draw.io

```
Convert this figure to draw.io XML format (.drawio file).

Requirements:
- Use mxGraph cell structure
- Each module = mxCell with style="shape=rectangle;fillColor=#hex;strokeColor=#hex;..."
- Each arrow = mxCell edge with style="endArrow=classic;dashed=0|1;..."
- Use draw.io's built-in scientific shape library where applicable (e.g., mxgraph.cisco19)
- Preserve all labels, colors, and connections
- Output as valid <mxfile> XML

Output the full .drawio XML.
```

## 何时复用 / 不复用

- ✅ **复用模板**：每次都用同一套骨架，只改具体内容字段。AI 对结构化 prompt 反应远好过自由文本。
- ❌ **不要乱发挥**：不要在 prompt 里加"美观""漂亮""清晰""专业"这种形容词，AI 会按它的审美胡来。所有"质量"诉求必须翻译成具体规格（DPI、字体、配色数、布局）。
