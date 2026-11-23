---
name: BIT-PPT-literature
description: 读取学术论文PDF，自动生成北京理工大学学术风格的文献汇报PPT。适用于组会文献报告、论文答辩、学术分享等场景。
argument-hint: "[PDF文件路径]"
user-invocable: true
allowed-tools: Read, Write, Bash, Glob, Grep
---

# BIT-PPT-literature

你是学术PPT生成器。当用户调用 `/BIT-PPT-literature <pdf_path>` 时，自动阅读论文PDF并生成北京理工大学学术风格的文献汇报PPT。

## 核心策略

**复制迷你模板 → 按需克隆页面 → 删除5个原始页 → 替换文本 + 插入图片**。

模板：`D:/BIT_ppt_skills/北理工模板_mini.pptx`（仅5页，预提取自完整模板） | 主题色：BIT绿 `#006C39` | 字体：微软雅黑 | 尺寸：960pt×540pt（16:9）

---

## 一、模板页速查（迷你模板，共5页）

| 用途 | 源Slide | 关键Shape |
|------|---------|-----------|
| 封面 | `/slide[1]` | `shape[@name="标题 1"]` 标题, `shape[@name="文本占位符 2"]` 副标题, `shape[@name="文本占位符 3"]` 作者/日期 |
| 正文（单栏+图） | `/slide[2]` | `shape[@name="标题 8"]` 标题, `shape[@name="文本框 9"]` 编号, `shape[@name="内容占位符 1"]` 正文 |
| 观点对比（双栏） | `/slide[3]` | `shape[@name="标题 9"]` 标题, `shape[@name="文本占位符 4"]` 左栏, `shape[@name="文本占位符 5"]` 右栏, `shape[@name="文本占位符 6"]` 左标签, `shape[@name="文本占位符 7"]` 右标签 |
| 三点卡片（三列） | `/slide[4]` | `shape[@name="标题 9"]` 标题, `shape[@name="文本框 52"]` 编号; 每组: `group[@name="组合 10"]/shape[@name="文本框 12"]` 小标题, `group[@name="组合 10"]/shape[@name="文本框 13"]` 正文（其余两组类推：组合14→文本框16/17, 组合18→文本框20/21） |
| 结尾 | `/slide[5]` | `shape[@name="文本框 10"]` 主文字, `shape[@name="文本框 15"]` 作者信息 |

---

## 二、排版布局系统（必须先读！）

**核心原则：用矩形框分割画面 → 每个框内填内容 → 占满全页不留大片空白。**

PPT 画布 34cm×19cm。以 1.5cm 为页边距，可用区域 31cm×16cm（标题区 y≈1.5-3.5cm，内容区 y≈3.5-18cm）。

### 套路：先画框，再填内容

每页操作顺序：
1. **用矩形 shape 画出分割框**（虚线/浅色边框，划分区域）
2. **缩小 `内容占位符 1`** 文本框到对应区域
3. **填入文字**（含关键文字标红 + 结论框）
4. **插入图片**（只设 width，保持宽高比）→ **添加图注文本框**
5. 检查画面是否占满（四边留白 ≤ 2cm）

### 常用分割模式

#### 模式 1：左文右图（方法页、架构说明）

```
┌──────────────────────────────────────────┐
│  Title                               1.5cm
├────────────────────┬─────────────────────┤
│                    │                     │
│  • Bullet 1        │     图片/架构图     │
│  • Bullet 2        │   (width=16cm,      │
│  • Bullet 3        │    height自动计算)  │
│                    │   [图注文本框]      │
│  (12cm×13.5cm)    │                     │
│                    │                     │
└────────────────────┴─────────────────────┘
 ← 1.5cm →← 13cm →← 0.8cm →← 15.5cm →← 1.5cm →
```

```bash
# Step 1: 虚线框分区（BIT绿色虚线，划分左右区域）
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=13cm --prop height=13.5cm
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=15.3cm --prop y=3.5cm --prop width=17cm --prop height=13.5cm

# Step 2: 左区文本框 + 填入文字 ...
# Step 3: 右区插入图片 ...
# Step 4: 图注 + 结论色块
```

#### 模式 2：上文下图（实验结果、数据展示）

```
┌──────────────────────────────────────────┐
│  Title                               1.5cm
├──────────────────────────────────────────┤
│  • Bullet 1  • Bullet 2  • Bullet 3     │  ← 文字区 h≈4cm
│  [结论色块: 关键发现一句话]              │
├──────────────────────────────────────────┤
│                                          │
│           图片 / 数据图表                 │  ← 图片区 h≈8cm
│          (width=30cm)                    │
│          [图注]                          │
│                                          │
└──────────────────────────────────────────┘
```

```bash
# 虚线框分区
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=4.5cm
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=1.5cm --prop y=8.5cm --prop width=31cm --prop height=8.5cm

# 隐藏原始占位符
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='内容占位符 1']" \
  --prop width=0cm --prop height=0cm --prop text=""

# ... 加独立小文本框 + 文字 ...

# 结论色块
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F0F7F3 \
  --prop x=2cm --prop y=7.2cm --prop width=30cm --prop height=0.8cm \
  --prop text='■ 结论：<一句话>' \
  --prop size=10pt --prop bold=true --prop color=FF0000 --prop align=left

# 图片（★防溢出：用height限高，width自动计算★）
officecli add "$OUT" "/slide[$SLIDE]" --type picture \
  --prop src="..." --prop x=2cm --prop y=9cm --prop height=8cm
```

#### 模式 3：全宽文字（研究背景、总结展望）

```bash
# 虚线框分区
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=14cm

# 隐藏原始占位符
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='内容占位符 1']" \
  --prop width=0cm --prop height=0cm --prop text=""
# 4-5 条独立小文本框 + 底部结论框
```

#### 模式 4：双栏对比（优缺点、方法对比、消融实验）

双栏文字在上，图片在下（如有对比图）。

#### 模式 5：三列卡片（核心贡献、未来方向）

用 slide[4] 模板自带的三列卡片布局，每组内有小标题+正文。

#### 模式 6：网格四象限（2×2，四组并行内容）

```
┌──────────────────────────────────────────┐
│  Title                               1.5cm
├──────────────────┬───────────────────────┤
│  Q1: 场景/数据   │  Q2: 方法/指标        │  ← 各 h≈6.5cm
├──────────────────┼───────────────────────┤
│  Q3: 结果对比    │  Q4: 结论/优势        │  ← 各 h≈6.5cm
└──────────────────┴───────────────────────┘
```

```bash
# 四个象限虚线框
for q in "1.5cm,3.5cm,15cm,6.5cm" "17cm,3.5cm,15.5cm,6.5cm" "1.5cm,10.5cm,15cm,6.5cm" "17cm,10.5cm,15.5cm,6.5cm"; do
  IFS=',' read -r qx qy qw qh <<< "$q"
  officecli add "$OUT" "/slide[$SLIDE]" --type shape \
    --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
    --prop x="$qx" --prop y="$qy" --prop width="$qw" --prop height="$qh"
done
# 每象限独立 textbox
```

#### 模式 7：中央大图 + 四角文字（核心架构展示）

```
┌──────────────────────────────────────────┐
│  Title                               1.5cm
├────────┬──────────────────┬──────────────┤
│ 左上文  │                  │  右上方文    │
│ (要点)  │   核心框架图      │  (要点)     │
│         │   (居中大图)     │             │
├────────┴──────────────────┴──────────────┤
│  结论色块: 一句话总结                    │
└──────────────────────────────────────────┘
```

适合大的 Mermaid 架构图或论文核心框架图。

#### 模式 8：左图右文（逆向模式1，适合纵向框图）

文字在右，图表在左。适合纵向长图或流程图。

### 图片安全尺寸规则（防溢出）

**图片插入前必须判断**：原图宽高比决定了设 width 还是设 height。

| 区域 | 可用尺寸 | 对横图(宽>高) | 对方图 | 对竖图(高>宽) |
|------|---------|--------------|--------|--------------|
| 模式1 右区 | 17×13.5cm | `width=16cm` ✓ | `width=14cm` ✓ | `height=12cm` (width自动) |
| 模式2 底区 | 31×8.5cm | `height=8cm` (优先!) | `height=8cm` | `height=8cm` |
| 模式8 左区 | 17×13.5cm | `width=16cm` ✓ | `width=14cm` ✓ | `height=12cm` |

**铁律**：
1. 先判断原图宽高比 → 选对约束维度
2. **模式2 底区必须设 `height=8cm`**（设 width=30cm 会导致竖图/方图高度溢出至 13cm+）
3. 如果原图宽>高（横图），设 `width` 更安全
4. 如果原图高>宽（竖图），设 `height` 更安全
5. 插入后必须验证：`y + height < 18.5cm`，`x + width < 32.5cm`

### 画面占满自检

- [ ] 最左元素 x ≤ 2cm，最右元素 right-edge ≥ 32cm
- [ ] 最上元素 y ≤ 4cm，最下元素 bottom-edge ≥ 17cm
- [ ] 没有 > 3cm 的连续空白区域
- [ ] 每个内容区有矩形框、图片或图表填充
- [ ] 图片宽度 ≥ 12cm

### 装饰元素速查

**虚线矩形框**（画面分割）：
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none \
  --prop line=006C39:1.5:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=14cm
```

**实心填充色块**（标题栏、重点标注）：
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=006C39 \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=1cm
officecli set "$OUT" "/slide[$SLIDE]/shape[-1]" \
  --prop text='核心发现' --prop size=14pt --prop bold=true --prop color=FFFFFF
```

**结论色块**（每页底部，红色方块前缀+统一格式）：
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F0F7F3 \
  --prop x=1.5cm --prop y=16.5cm --prop width=31cm --prop height=1.2cm
officecli set "$OUT" "/slide[$SLIDE]/shape[-1]" \
  --prop text='■ 核心结论：<一句话概括，≤50字>' \
  --prop size=12pt --prop bold=true --prop color=FF0000 --prop align=left
```
> 结论色块统一规范：红色字体 `FF0000`、**12pt**、bold、左对齐、以 `■` 方块开头。高度 1.2cm（不能太扁）。所有正文页（背景、方法、结果、总结）都必须有。

**箭头**：
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rightArrow --prop fill=006C39 \
  --prop x=14cm --prop y=9.5cm --prop width=2cm --prop height=1.2cm
```

**图注文本框**（图片下方，灰色小字）：
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=none \
  --prop x=<图片x> --prop y=<图片bottom+0.2cm> --prop width=<图片width> --prop height=0.8cm \
  --prop text='Fig.X: <一句话描述图片内容>' --prop size=9pt --prop color=3F3F3F --prop align=center
```

> 一个画面中矩形框 2-3 个、箭头 1-2 个、色块 1 个。用 BIT 绿统一色调。

### 小文本框策略（替代单个大文本框）

**问题**：一个大的 `内容占位符 1` 文本框难以精确控制，容易与图片区域重叠。

**方案**：用多个独立的小 textbox shape 替代单一内容占位符，每个 box 承载 1-2 句话，灵活定位填充画面空白区。

```bash
# 不用内容占位符 1，改为添加多个小 textbox
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=4cm --prop width=12cm --prop height=3cm \
  --prop text='要点一：<1-2句话描述>' \
  --prop size=14pt --prop bold=true --prop color=333333

officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=7.5cm --prop width=12cm --prop height=3cm \
  --prop text='要点二：<1-2句话描述>' \
  --prop size=14pt --prop bold=true --prop color=333333

officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=11cm --prop width=12cm --prop height=3cm \
  --prop text='要点三：<1-2句话描述>' \
  --prop size=14pt --prop bold=true --prop color=333333
```

**使用原则**：
- 每个小文本框 2-3 行文字，14pt bold，浅灰底 `F5F5F5`
- 文本框之间间距 0.5cm
- y 坐标从 4cm 开始，每个框间隔算出精确位置
- 总高度不超过图片区域（模式1 不超过 14cm）
- 这样没有"大文本框越界到图片区"的问题

### 图文防重叠 & 图片防溢出

**插入每张图片前必须验证**：

```bash
# 插入图片后立即检查
officecli get "$OUT" "/slide[$SLIDE]" --depth 1 2>&1 | grep picture
# 验证: y + height < 18cm 且 x + width < 32.5cm
# 如果不满足 → 减小 width/height 直到满足
```

**铁律**：
1. 右区图片 y 起点 = 文字最下方 textbox 的 bottom + 0.5cm（绝不等于文字起点 y）
2. 右区图片 bottom（y + height）≤ 17cm（给结论栏留足空间）
3. 全宽图片（模式2）：y=9cm, **设 height=8cm**（width 自动），bottom ≤ 17cm
4. 结论栏在 y=16.5cm，图片必须在 y=16.5cm 之前结束
5. 双图并排时：先算每张图的 max-height，两张图 y 起点对齐

---

## 三、工作流程

### Step 1: 读取PDF + 提取图片

**1.1 读取文本**：用 Read 工具读取PDF全文。覆盖 Abstract、Introduction、Method、Results、Conclusion。

**1.2 提取PDF内嵌图片**（PyMuPDF）：

```python
import fitz, os
doc = fitz.open(r"<PDF绝对路径>")
out_dir = r"<PDF所在目录>/<PDF文件名>_images"
os.makedirs(out_dir, exist_ok=True)

# 获取每页尺寸（pt），用于过滤整页渲染图
page_sizes = {}
for i in range(doc.page_count):
    rect = doc[i].rect
    page_sizes[i] = (rect.width, rect.height)

images_info = []
for i in range(doc.page_count):
    pw, ph = page_sizes[i]
    for j, img in enumerate(doc[i].get_images()):
        xref = img[0]
        base = doc.extract_image(xref)
        w, h = base["width"], base["height"]
        # 跳过太小的图（<200px 是图标/logo）
        if w < 200 and h < 200:
            continue
        # ★ 跳过整页渲染图（宽高比接近页面 + 面积大，是PDF渲染整页，非论文原图）★
        page_aspect = pw / ph if ph > 0 else 1.0
        img_aspect = w / h if h > 0 else 1.0
        aspect_match = abs(img_aspect - page_aspect) < 0.08
        large_area = w * h > 2000000  # >2M 像素
        if aspect_match and large_area:
            print(f"  [跳过] page{i+1}_fig{j+1}: {w}x{h} 疑似整页渲染图 (页面宽高比{page_aspect:.2f})")
            continue
        ext = base["ext"]
        name = f"page{i+1}_fig{j+1}_{w}x{h}.{ext}"
        path = os.path.join(out_dir, name)
        with open(path, "wb") as f:
            f.write(base["image"])
        images_info.append({
            "page": i+1, "name": name, "path": path,
            "width": w, "height": h, "size_kb": len(base["image"]) // 1024
        })
        print(f"  Fig {len(images_info)}: {name} (p{i+1}, {w}x{h}, {len(base['image'])//1024}KB)")

doc.close()
print(f"\n共提取 {len(images_info)} 张图片 → {out_dir}")

for img in images_info:
    if img["width"] > 800 or img["width"] * img["height"] > 400000:
        print(f"  [重要] {img['name']} (p{img['page']})")
```

Python 路径：`/path/to/user/AppData/Local/Programs/Python/Python39/python`

### Step 2: 分析论文 → 产出PPT大纲

```
## 论文元信息
- 标题: <完整标题>
- 第一作者: <Name>
- 期刊/年份: <Journal> <Year>

## PPT规划 (共 M 页)

### Slide 1: 封面
- 标题: <精简标题，≤30中文字>
- 副标题: <FirstAuthor> et al. | <Journal> <Year>
- 底部: 汇报人：    日期：<today>

### Slide 2: 研究背景与动机
- 模板: slide[2]（内容页）
- 分割: 模式3（全宽文字）——无图，大虚线框占满
- 标题: 研究背景与动机
- Bullets（4条，每条≤50中文字，含关键词标红）:
  1. <领域背景，精确到具体问题>
  2. <现有方法分类与核心不足>
  3. <本文核心思路——标红关键词>
  4. <预期贡献>
- 底部: 结论色块（1句话概括动机）

### Slide 3: 方法/框架总览
- 模板: slide[2]
- 分割: 模式1（左文右图）或 模式7（中央大图+四角文字）
- 标题: <方法名称>
- Bullets（3条，≤50字/条）:
  1. <整体框架描述>
  2. <核心创新机制>
  3. <关键技术优势>
- **框架总览图（Mermaid）**：如果论文原图不够清晰，必须用 Mermaid 自己画总览架构图。**这是PPT最重要的视觉元素！禁止简单线性A→B→C串流，必须包含 subgraph分组 + 并行分支 + 样式着色 + 反馈回路中至少3种。**
- 有清晰原图时：原图放右侧 + Mermaid 可放备用
- 图注: Fig.X: <图片描述>

### Slide 4: 方法细节
- 模板: slide[2]
- 分割: 模式1 或 模式4（灵活选）
- Bullets（3条）+ 1-2张细节原图 + 图注

### Slide 5: 实验设置与结果
- 模板: slide[2]
- 分割: 模式2（上文下图）
- 标题: 实验结果
- Bullets（3条核心发现，带精确数字，数字标红）:
  1. <发现一 + 数据>
  2. <发现二 + 数据>
- 结论色块: <一句话总结>
- 图片: Results 章节原图（设 width=30cm，不设 height）+ 图注

### Slide 6: 对比分析（可选）
- 模板: slide[3]（观点对比）或 slide[2]+模式4
- 左栏: 本文方法优点（3条）
- 右栏: 现有方法局限（3条）

### Slide 7: 总结与展望
- 模板: slide[2] 或 slide[4]（三点卡片）
- 分割: 模式3 或 模式5
- 标题: 总结与展望
- Bullets（4条）:
  1. 核心贡献（标红关键术语）
  2. 关键结论（标红核心数据）
  3. 局限性
  4. 未来方向
- 底部: 结论色块

### Slide 8: 结尾感谢
```

**内容提炼铁律**：
- 每个bullet ≤ 50中文字（≈2行），用简练短语
- 关键术语首次出现时加粗标红
- 数据精确："Acc↑3.2%（82.1→85.3）"，数字标红
- **图片优先**：论文原图 > Mermaid > Chart > 纯文字
- **画面占满**：分割框到边距 1.5cm，不留 > 3cm 空白

**图片分配策略**：
- Method 章节大图（架构/流程图）→ Slide 3（方法总览），width=16cm
- Method 章节细节图 → Slide 4
- Results 章节对比图 → Slide 5（实验），**必须设 `height=8cm`**（防溢出）
- **框架总览图（Mermaid）**：如果论文没有清晰的架构原图，或原图不够直观，必须自己用 Mermaid 画。这是PPT最重要的视觉元素
- 图片不够时：Mermaid 补架构、Chart 补数据
- 并非每页都需要图片——背景和总结页用大面积文字框也好

### Step 3: 生成PPT

#### 3.1 准备文件

```bash
OUT="<PDF目录>/<PDF文件名>_汇报.pptx"
cp "D:/BIT_ppt_skills/北理工模板_mini.pptx" "$OUT"
```

迷你模板只有5页（封面、内容、对比、三列、结尾），比原来的580页模板快100倍以上。

#### 3.2 克隆需要的页面

按PPT大纲克隆：封面 → K页内容 → 结尾。

```bash
# 迷你模板的5页索引:
# /slide[1]=封面  /slide[2]=内容  /slide[3]=对比  /slide[4]=三点卡片  /slide[5]=结尾

officecli add "$OUT" / --from '/slide[1]'      # 封面（1份）
officecli add "$OUT" / --from '/slide[2]'      # 内容页（×K份，含所有带图页）
officecli add "$OUT" / --from '/slide[3]'      # 对比页（可选）
officecli add "$OUT" / --from '/slide[4]'      # 三点卡片（可选）
officecli add "$OUT" / --from '/slide[5]'      # 结尾（1份）
```

克隆完成后，新slide在文件末尾。**记下每页对应的实际 slide 索引。**

#### 3.3 删除原始模板页（仅5页，秒级完成）

```bash
for i in 1 2 3 4 5; do
  officecli remove "$OUT" '/slide[1]'
done
```

删除后 slide[1] = 封面, slide[2..K+1] = 内容页, slide[K+2] = 结尾。

#### 3.4 填充封面

```bash
officecli set "$OUT" '/slide[1]/shape[@name="标题 1"]' --prop text='<论文标题>'
officecli set "$OUT" '/slide[1]/shape[@name="文本占位符 2"]' \
  --prop text='<FirstAuthor> et al. | <Journal> <Year>'
officecli set "$OUT" '/slide[1]/shape[@name="文本占位符 3"]' \
  --prop text='汇报人：         日期：<YYYY/MM/DD>'
```

#### 3.5 填充内容页（含标红 + 结论框）

**★ 用小文本框替代单个大占位符 ★** 模板克隆后的 `内容占位符 1` 宽度 24cm 无法精确控制，必须拆分为独立小 textbox。

```bash
SLIDE=2  # 当前内容页索引

# 设置编号和标题（★修复编号字体为微软雅黑，模板默认Century Gothic★）
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本框 9']" \
  --prop text='1' --prop font=微软雅黑
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='标题 8']" --prop text='研究背景与动机'

# ★ 第1步：隐藏原始内容占位符（清空文字 + 缩小到0，彻底隐藏）★
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='内容占位符 1']" \
  --prop width=0cm --prop height=0cm --prop text=""

# ★ 第2步：添加独立小文本框（每个 2-3 行，浅灰底，精确位置不重叠）★
# 模式1（左文右图）：3个小文本框在左侧，y 坐标依次排列
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=4cm --prop width=12cm --prop height=3cm \
  --prop text='要点一：智能网联汽车自主换道决策直接影响行车安全与交通效率，是混合交通核心难题\n现有方法分三类：规则驱动(僵化)、数据驱动(海量数据)、博弈论(未区分AV/HV角色)' \
  --prop size=14pt --prop bold=true --prop color=333333

officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=7.5cm --prop width=12cm --prop height=3cm \
  --prop text='要点二：Stackelberg博弈采用"领导者-跟随者"架构\nAV作为Leader优先决策，HV根据驾驶风格后响应' \
  --prop size=14pt --prop bold=true --prop color=333333

officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=11cm --prop width=12cm --prop height=3cm \
  --prop text='要点三：LSTM轨迹预测+K-means风格分类 + MPC+GA双层优化\n冲突率↓30%，jerk↓40%，换道成功率→95%' \
  --prop size=14pt --prop bold=true --prop color=333333

# 模式2（上文下图）：用小文本框替代大占位符
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=2cm --prop y=4cm --prop width=15cm --prop height=3.5cm \
  --prop text='发现一：<描述>' --prop size=14pt --prop bold=true
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F5F5F5 \
  --prop x=17.5cm --prop y=4cm --prop width=15cm --prop height=3.5cm \
  --prop text='发现二：<描述>' --prop size=14pt --prop bold=true

# 第3步：关键文字标红（--find 匹配词 → --prop color=FF0000）
for box_path in "/slide[$SLIDE]/shape[-3]" "/slide[$SLIDE]/shape[-2]" "/slide[$SLIDE]/shape[-1]"; do
  officecli set "$OUT" "$box_path" --find '关键词' --prop bold=true --prop color=FF0000
done

# 第4步（必须！每页都要）：添加结论色块（12pt红字+方块前缀）
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=F0F7F3 \
  --prop x=1.5cm --prop y=16.5cm --prop width=31cm --prop height=1.2cm \
  --prop text='■ 核心结论：<一句话，≤50字>' \
  --prop size=12pt --prop bold=true --prop color=FF0000 --prop align=left
```

**关键规则**：
- **第1步必须缩小文本框**（默认24cm会溢出！）
- 始终 `--prop list=bullet --prop level=0`
- 始终 `--prop size=16pt --prop bold=true --prop lineSpacing=1.25x`
- 每页 3-4 个bullet，每个 ≤ 50 中文字
- **标红**：用 `--find '匹配词' --prop color=FF0000 --prop bold=true`，对核心术语、关键数据标红
- 有图片时先缩小文本框再填文字再插图片

**标红指南**（每页2-4处）：
- 论文核心方法名（如"Stackelberg博弈""LSTM编码器""K-means聚类"）
- 关键性能数字（如"30%""89.7%""↓40%"）
- 对比结论（如"优于SOTA方法""显著降低"）
- 不要整段标红，只标关键词/数字

**结论色块指南**（必须！）：
- 位置：页面底部 y=16.5cm，width=31cm，height=1.2cm
- 格式：填充 `F0F7F3`（浅绿底），**文字 `FF0000`（红色）**，12pt bold，**左对齐**
- **以 `■` 方块开头**，统一格式：`■ 核心结论/核心动机/框架要点/算法优势：<一句话>`
- 内容：1句话概括本页核心结论，≤50字
- 背景/动机/方法/结果/总结页**必须**加结论色块

#### 3.6 插入论文原图（★保持宽高比 + 图注★）

**图片插入铁律：**
1. **先判断原图宽高比，选对约束维度**（横图设 width，竖图设 height）
2. **模式2（上文下图）底部区域：必须设 `height=8cm`**，否则 width=30cm 会导致竖图/方图高度溢出画布
3. **插入后验证**：`y + height < 18.5cm`，`x + width < 32.5cm`
4. 只设一个维度，officecli 自动计算另一个维度。

```bash
# 正确：只设width，高度自动保持比例
officecli add "$OUT" "/slide[$SLIDE]" --type picture \
  --prop src="<images_dir>/pageX_figY_WxH.jpeg" \
  --prop x=15.8cm --prop y=4cm --prop width=16cm

# 错误（禁止！）：同时设width和height会强制拉伸变形
# officecli add ... --prop width=16cm --prop height=12cm  ← 禁止！

# 图注：图片下方灰色小字描述
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=none \
  --prop x=15.8cm --prop y=... --prop width=16cm --prop height=0.8cm \
  --prop text='图X: <图片内容简述，如"模型架构总览：LSTM编码器+Stackelberg博弈决策模块">' \
  --prop size=9pt --prop color=3F3F3F --prop align=center
```

**图注 y 坐标计算**：图片 y + 图片实际高度 + 0.2cm 间距。不确定图片实际高度时，插入图片后用 `officecli get "$OUT" "/slide[$SLIDE]" --depth 1 | grep picture` 查看实际 height，再设图注位置。

**图文排版参考**（width-only，高度自动）：

| 原图宽高比 | x | y | width | 说明 |
|-----------|-----|-----|-------|------|
| 横图（宽>高，如架构图） | 15.8cm | 4cm | 16cm | 右侧，高度自动≈8-10cm |
| 方图（≈1:1） | 16cm | 5cm | 14cm | 右侧居中，高度自动≈14cm |
| 竖图（高>宽） | 17cm | 4cm | 10cm | 右侧，高度自动≈13cm |
| 全宽图（实验结果，模式2） | 2cm | 9cm | **height=8cm**（width自动） | 文字下方，防溢出 |

#### 3.6-alt 插入 Mermaid 框架图（推荐！方法页核心视觉元素）

**如果论文没有清晰架构原图，或原图过于复杂/模糊，必须自己用 Mermaid 画总览框架图。**

**★ 禁止简单线性 A→B→C 串流图！必须包含以下至少 3 种元素：**

| 元素 | 说明 | 示例 |
|------|------|------|
| **subgraph 分组** | 将相关模块归入逻辑组 | `subgraph 感知层` ... `end` |
| **并行分支** | 多路并行处理 | `A --> B; A --> C; A --> D` |
| **反馈回路** | 输出反馈到输入 | `F -->|反馈| A` |
| **样式着色** | 关键节点用不同颜色 | `style X fill:#006C39,color:#fff` |
| **不同节点形状** | 区分输入/处理/输出 | `[]` 矩形 `{}` 菱形 `(())` 圆形 |
| **虚线/粗线** | 区分主数据流和辅助流 | `==>` 粗线 `-.->` 虚线 |

**Bitgreen 配色方案：**
- 输入/数据节点：`fill:#E8F5E9,color:#333`（浅绿底）
- 核心算法节点：`fill:#006C39,color:#fff`（Bitgreen 实心底 + 白字）
- 输出/结果节点：`fill:#F0F7F3,color:#006C39,stroke:#006C39`（浅绿底 + 绿框绿字）
- 损失/优化节点：`fill:#FFE0E0,color:#CC0000`（浅红底，突出优化目标）
- 子图背景：`fill:#FAFAFA,stroke:#006C39`

**推荐布局：**
- 横向为主 `graph LR`（适合流水线式）
- 纵向为主 `graph TB`（适合分层架构）
- 节点文字 ≤ 12 字符，用 `<br/>` 换行

**示例 1：分层并行架构（graph TB + subgraph + 并行 + 样式）**
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type diagram \
  --prop text='graph TB
    subgraph 输入层[" 输入层 "]
      A[V2V通信<br/>车辆状态共享]
      B[高精地图<br/>车道几何信息]
    end
    subgraph 感知预测[" 感知与预测层 "]
      C[交互特征提取]
      D[LSTM编码器<br/>时序建模]
      E[轨迹预测模块<br/>多模态输出]
      A --> C
      B --> C
      C --> D
      D --> E
    end
    subgraph 决策优化[" 决策与优化层 "]
      F[代价函数设计<br/>安全+舒适+效率]
      G[联盟博弈模型<br/>风格权重自适应]
      H[MPC滚动优化<br/>约束条件:安全/舒适/执行器]
      I{收敛?}
    end
    E --> F
    F --> G
    G --> H
    H --> I
    I -->|否,更新权重| F
    I -->|是| J[最优决策输出]
    J --> K[底层运动执行]
    style A fill:#E8F5E9,color:#333
    style B fill:#E8F5E9,color:#333
    style G fill:#006C39,color:#fff
    style H fill:#006C39,color:#fff
    style F fill:#FFE0E0,color:#CC0000
    style J fill:#F0F7F3,color:#006C39,stroke:#006C39
    style I fill:#FFF9C4,color:#333' \
  --prop x=3cm --prop y=3.5cm --prop width=28cm --prop height=13cm
```

**示例 2：横向数据流 + 分支对比（graph LR + 双分支并行 + 合并）**
```bash
officecli add "$OUT" "/slide[$SLIDE]" --type diagram \
  --prop text='graph LR
    A[原始轨迹数据] --> B[特征工程]
    B --> C[驾驶风格聚类<br/>K-means++]
    C --> D1[激进型<br/>权重: ωe≫ωs,ωc]
    C --> D2[稳健型<br/>权重均衡]
    C --> D3[保守型<br/>权重: ωs,ωc≫ωe]
    D1 --> E[Stackelberg博弈<br/>AV-Led/AV-Fol模式]
    D2 --> E
    D3 --> E
    E --> F{联盟形成}
    F -->|满足个体理性| G[大联盟协同]
    F -->|不满足| H[子联盟拆分]
    G --> I[MPC最优控制]
    H --> I
    I --> J{碰撞风险?}
    J -->|安全| K[执行换道]
    J -->|危险| L[保持原车道]
    L -.->|重新规划| E
    style D1 fill:#FFE0E0,color:#CC0000
    style D2 fill:#E8F5E9,color:#333
    style D3 fill:#BBDEFB,color:#333
    style E fill:#006C39,color:#fff
    style K fill:#F0F7F3,color:#006C39,stroke:#006C39' \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=13cm
```

#### 3.7 实验结果页：原图优先 或 Chart 备选

**优先使用论文 Results 原图**：

```bash
# 全宽原图（★模式2防溢出：必须设height=8cm，width自动★）
officecli add "$OUT" "/slide[$SLIDE]" --type picture \
  --prop src="<images_dir>/pageX_figY_WxH.jpeg" \
  --prop x=2cm --prop y=9cm --prop height=8cm

# 图注
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop preset=rect --prop fill=none --prop line=none \
  --prop x=2cm --prop y=<图片bottom+0.2cm> --prop width=30cm --prop height=0.8cm \
  --prop text='图X: <实验对比描述>' --prop size=9pt --prop color=3F3F3F --prop align=center
```

**无原图时用 Chart**：

```bash
officecli add "$OUT" "/slide[$SLIDE]" --type chart \
  --prop chartType=column \
  --prop categories='Method A,Method B,Method C,Ours' \
  --prop data='Accuracy:82.1,85.3,80.7,89.7;F1-Score:79.5,83.1,78.9,88.2' \
  --prop x=1.5cm --prop y=10cm --prop width=22cm --prop height=4.5cm \
  --prop legend=bottom \
  --prop dataLabels=outsideEnd \
  --prop colors='A2A2A2,A2A2A2,A2A2A2,006C39'
```

#### 3.8 公式 textbox（可选）

```bash
officecli add "$OUT" "/slide[$SLIDE]" --type shape \
  --prop text='L_total = L_task + λ₁·L_consistency + λ₂·L_diversity' \
  --prop x=2cm --prop y=12.5cm --prop width=20cm --prop height=1cm \
  --prop font='Consolas' --prop size=13pt \
  --prop align=center --prop fill='F0F7F3' --prop color='006C39'
```

#### 3.9 填充对比页（slide[3]）

```bash
SLIDE=6

officecli set "$OUT" "/slide[$SLIDE]/shape[@name='标题 9']" --prop text='方法对比'

# 左栏（本文方法优点）
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 6']" --prop text='本文方法'
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 4']" \
  --prop size=14pt --prop lineSpacing=1.25x \
  --prop text='耦合轨迹预测与博弈决策\n多驾驶风格自适应交互\n加速度序列优化→jerk↓40%'
for p in 1 2 3; do
  officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 4']/paragraph[$p]" \
    --prop list=bullet --prop level=0
done

# 标红关键数据
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 4']" \
  --find '40%' --prop bold=true --prop color=FF0000

# 右栏（现有方法局限）
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 7']" --prop text='现有方法'
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 5']" \
  --prop size=14pt --prop lineSpacing=1.25x \
  --prop text='规则方法：复杂场景灵活性差\n强化学习：数据量大+鲁棒性不足\nNash均衡：未区分AV/HV角色差异'
for p in 1 2 3; do
  officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本占位符 5']/paragraph[$p]" \
    --prop list=bullet --prop level=0
done
```

#### 3.10 填充三点卡片页（slide[4]）

```bash
SLIDE=7

officecli set "$OUT" "/slide[$SLIDE]/shape[@name='标题 9']" --prop text='核心贡献'
officecli set "$OUT" "/slide[$SLIDE]/shape[@name='文本框 52']" --prop text='4'

# 第1列
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 10']/shape[@name='文本框 12']" \
  --prop text='创新点一'
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 10']/shape[@name='文本框 13']" \
  --prop size=14pt --prop lineSpacing=1.25x \
  --prop text='要点描述（≤50字）\n关键数据支撑'

# 第2列
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 14']/shape[@name='文本框 16']" \
  --prop text='创新点二'
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 14']/shape[@name='文本框 17']" \
  --prop size=14pt --prop lineSpacing=1.25x \
  --prop text='要点描述（≤50字）\n关键数据支撑'

# 第3列
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 18']/shape[@name='文本框 20']" \
  --prop text='创新点三'
officecli set "$OUT" "/slide[$SLIDE]/group[@name='组合 18']/shape[@name='文本框 21']" \
  --prop size=14pt --prop lineSpacing=1.25x \
  --prop text='要点描述（≤50字）\n关键数据支撑'
```

#### 3.11 填充结尾页

```bash
LAST=$((K + 2))
officecli set "$OUT" "/slide[$LAST]/shape[@name='文本框 10']" \
  --prop text='谢谢观看\n敬请各位老师批评指正'
officecli set "$OUT" "/slide[$LAST]/shape[@name='文本框 15']" \
  --prop text='汇报人：\n导　师：'
```

#### 3.12 保存

```bash
officecli close "$OUT"
```

### Step 4: 清理 + 报告结果

**4.1 删除提取的图片目录**（PDF 图片已嵌入 PPT，不再需要）：

```bash
rm -rf "<PDF所在目录>/<PDF文件名>_images"
```

**4.2 报告结果**：

告知用户输出路径、页数、每页内容摘要、使用的图片数。

---

## 四、排版强制规范

### 每页自检清单

- [ ] **先画矩形分割框**，再缩小文本框，再填内容
- [ ] body text size=16pt, bold=true, lineSpacing=1.25x
- [ ] 每个段落 `--prop list=bullet --prop level=0`
- [ ] 该页 3-4 个bullet，每个 ≤ 50 中文字
- [ ] **关键术语和数据标红**（`--find '词' --prop color=FF0000`，每页2-4处）
- [ ] **底部有结论色块**（红字 `FF0000` + `■` 方块前缀，背景/方法/结果/总结页**必备**）
- [ ] 图片只设 `--prop width=`，**绝不设 height**（保持原始宽高比）
- [ ] **每张图片下方有图注**（灰色9pt小字描述图片内容）
- [ ] 画面四边都有元素，不留 > 3cm 空白区
- [ ] **图片无溢出**：插入后验证 y+height < 18cm（给底部结论栏留至少 1cm 间距），模式2 底部设 height=8cm
- [ ] **图文不重叠**：右区图片 y 起点 ≥ 文字最下方 textbox bottom + 0.5cm
- [ ] **用小文本框拆分**：不用单个大内容占位符，拆为 2-4 个独立小 textbox 精确控制位置和边界
- [ ] **有框架总览图**：方法页必须有丰富 Mermaid 图（subgraph + 并行分支 + 样式着色，禁止简单线性串流）
- [ ] 图片足够大（width ≥ 12cm），不与文字区重叠

### 禁止事项

1. **禁止** 不缩小文本框就直接加图片——必重叠！
2. **禁止** 图片同时设 `width` 和 `height`——强制拉伸变形！
3. **禁止** 插入了论文原图却不加图注——读者不知道图在说什么
4. **禁止** 内容挤在一角，旁边大面积空白
5. **禁止** body text bold=false 或 lineSpacing≠1.25x
6. **禁止** 忘记 `list=bullet`（只设 level=0 无效）
7. **禁止** 单个bullet超过50中文字
8. **禁止** 明明提取到了论文原图却不使用
9. **禁止** 照搬论文原文——必须提炼为简练短语
10. **禁止** 关键术语和数据不加标红——读者抓不住重点
11. **禁止** 模式2（上文下图）设 `width=30cm`——竖图/方图高度会溢出画布，必须设 `height=8cm`
12. **禁止** 结论色块用绿色字体或小于 12pt——必须统一用红色 `FF0000` + `■` 方块前缀 + 12pt
13. **禁止** 方法页没有框架总览图——如果论文原图不够清晰，必须自己用 Mermaid 画（必须含 subgraph/并行分支/样式着色/反馈回路中至少 3 种，禁止简单 A→B→C 串流）
14. **禁止** 图片 bottom 超过 18cm——必须留至少 1cm 给底部结论栏
15. **禁止** 图文重叠——右区图片 y 必须 > 所有文字 textbox 的 bottom + 0.5cm
16. **禁止** 用单个超大内容占位符——必须拆分为 2-4 个小 textbox，每个精确设定位置和边界
17. **禁止** 添加无文字的空 textbox 占位——每个 textbox 必须有实际文字内容。但 BIT 绿色虚线分区框（`fill=none, line=006C39:1:dash`）是合法的视觉元素
18. **禁止** 隐藏占位符时不清空文字——`width=0cm` 必须配合 `--prop text=""`，否则残留文字仍可见

---

## 五、图表速查

### 论文原图（优先使用，width-only）
```bash
officecli add "$OUT" '/slide[N]' --type picture \
  --prop src="<images_dir>/pageX_figY_WxH.jpeg" \
  --prop x=15.8cm --prop y=4cm --prop width=16cm

# 图注（紧跟图片）
officecli add "$OUT" '/slide[N]' --type shape \
  --prop preset=rect --prop fill=none --prop line=none \
  --prop x=15.8cm --prop y=<图bottom+0.2cm> --prop width=16cm --prop height=0.8cm \
  --prop text='图X: 图片内容描述' --prop size=9pt --prop color=3F3F3F --prop align=center
```

### Mermaid 框架图（推荐！方法页核心视觉）

**★ 禁止简单 A→B→C 串流图！必须包含 subgraph 分组 + 并行分支 + 样式着色。**

Bitgreen 配色：输入 `#E8F5E9` | 核心算法 `#006C39` 白字 | 输出 `#F0F7F3` 绿框 | 优化目标 `#FFE0E0`

```bash
# 丰富 Mermaid 骨架（填充论文具体内容）：
officecli add "$OUT" '/slide[N]' --type diagram \
  --prop text='graph TB
    subgraph 输入[" 输入层 "]
      A[数据1] --> B[特征]
    end
    subgraph 核心[" 核心方法层 "]
      C[算法A] --> D[算法B]
      D --> E{判定}
    end
    B --> C
    E -->|分支1| F[输出1]
    E -->|分支2| G[输出2]
    E -.->|反馈| C
    style C fill:#006C39,color:#fff
    style D fill:#006C39,color:#fff
    style F fill:#F0F7F3,color:#006C39,stroke:#006C39' \
  --prop x=2cm --prop y=3.5cm --prop width=30cm --prop height=13cm
```

### Column 柱状图（实验结果，无原图时）
```bash
officecli add "$OUT" '/slide[N]' --type chart \
  --prop chartType=column \
  --prop categories='A,B,C,Ours' \
  --prop data='Metric1:v1,v2,v3,v4;Metric2:w1,w2,w3,w4' \
  --prop x=1.5cm --prop y=10cm --prop width=22cm --prop height=4.5cm \
  --prop legend=bottom --prop dataLabels=outsideEnd \
  --prop colors='A2A2A2,A2A2A2,A2A2A2,006C39'
```

### 公式 textbox
```bash
officecli add "$OUT" '/slide[N]' --type shape \
  --prop text='L = L_CE + λ·L_KL' \
  --prop x=2cm --prop y=12.5cm --prop width=20cm --prop height=1cm \
  --prop font='Consolas' --prop size=13pt \
  --prop align=center --prop fill='F0F7F3' --prop color='006C39'
```

---

## 六、快捷命令全集

```bash
# === 准备（迷你模板，仅5页！） ===
cp "D:/BIT_ppt_skills/北理工模板_mini.pptx" "OUT.pptx"
# 先提取PDF图片（Python脚本见Step 1.2）

# === 克隆（从迷你模板） ===
officecli add "OUT.pptx" / --from '/slide[1]'     # 封面
officecli add "OUT.pptx" / --from '/slide[2]'     # 内容页（×K）
officecli add "OUT.pptx" / --from '/slide[3]'     # 对比页
officecli add "OUT.pptx" / --from '/slide[4]'     # 三点卡片
officecli add "OUT.pptx" / --from '/slide[5]'     # 结尾

# === 删除原始页（仅5页！） ===
for i in 1 2 3 4 5; do officecli remove "OUT.pptx" '/slide[1]'; done

# === 封面 ===
officecli set "OUT.pptx" '/slide[1]/shape[@name="标题 1"]' --prop text='Title'
officecli set "OUT.pptx" '/slide[1]/shape[@name="文本占位符 2"]' --prop text='Author | Venue'
officecli set "OUT.pptx" '/slide[1]/shape[@name="文本占位符 3"]' --prop text='汇报人：    日期：YYYY/MM/DD'

# === 内容页（★先缩小文本框！★） ===
S=2
officecli set "OUT.pptx" "/slide[$S]/shape[@name='文本框 9']" --prop text='1'
officecli set "OUT.pptx" "/slide[$S]/shape[@name='标题 8']" --prop text='标题'
# 1. 缩小文本框
officecli set "OUT.pptx" "/slide[$S]/shape[@name='内容占位符 1']" \
  --prop x=2.5cm --prop y=4.5cm --prop width=29cm --prop height=12cm
# 2. 设置文字（16pt + bold + 1.25x）
officecli set "OUT.pptx" "/slide[$S]/shape[@name='内容占位符 1']" \
  --prop size=16pt --prop bold=true --prop lineSpacing=1.25x \
  --prop text='要点一（≤50字）\n要点二（≤50字）\n要点三（≤50字）\n要点四（≤50字）'
# 3. 激活bullet
for p in 1 2 3 4; do
  officecli set "OUT.pptx" "/slide[$S]/shape[@name='内容占位符 1']/paragraph[$p]" \
    --prop list=bullet --prop level=0
done
# 4. 标红关键词（每页2-4处）
officecli set "OUT.pptx" "/slide[$S]/shape[@name='内容占位符 1']" \
  --find '关键词一' --prop bold=true --prop color=FF0000
officecli set "OUT.pptx" "/slide[$S]/shape[@name='内容占位符 1']" \
  --find '30%' --prop bold=true --prop color=FF0000
# 5. 结论色块（页面底部，红字+方块前缀，必须！）
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rect --prop fill=F0F7F3 \
  --prop x=1.5cm --prop y=16.5cm --prop width=31cm --prop height=1.2cm \
  --prop text='■ 核心结论：<一句话概括>' --prop size=12pt --prop bold=true \
  --prop color=FF0000 --prop align=left
# 6. 插入图片（横图设width，竖图设height，模式2必须设height=8cm）
officecli add "OUT.pptx" "/slide[$S]" --type picture \
  --prop src="images_dir/pageX_figY_WxH.jpeg" \
  --prop x=15.8cm --prop y=4cm --prop width=16cm
# 模式2（上文下图）: --prop x=2cm --prop y=9cm --prop height=8cm
# 7. 图注（图片下方）
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rect --prop fill=none --prop line=none \
  --prop x=15.8cm --prop y=<图bottom+0.2> --prop width=16cm --prop height=0.8cm \
  --prop text='图X: <图片描述>' --prop size=9pt --prop color=3F3F3F --prop align=center

# === 虚线矩形框 ===
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rect --prop fill=none \
  --prop line=006C39:1.5:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=31cm --prop height=14cm

# === 箭头 ===
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rightArrow --prop fill=006C39 \
  --prop x=10cm --prop y=7cm --prop width=1.5cm --prop height=0.8cm

# === 模式6: 网格四象限 ===
# 4个虚线框 + 4个独立 textbox
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=1.5cm --prop y=3.5cm --prop width=15cm --prop height=6.5cm
officecli add "OUT.pptx" "/slide[$S]" --type shape \
  --prop preset=rect --prop fill=none --prop line=006C39:1:dash \
  --prop x=17cm --prop y=3.5cm --prop width=15.5cm --prop height=6.5cm
# ... (下排类推)

# === Mermaid 框架图（方法页必备！） ===
officecli add "OUT.pptx" "/slide[$S]" --type diagram \
  --prop text='graph TD
    A[输入] --> B[特征提取模块]
    B --> C[核心算法模块]
    B --> D[辅助模块]
    C --> E[输出结果]
    D --> E' \
  --prop x=12cm --prop y=5.5cm --prop width=12cm --prop height=7.5cm

# === 结尾 + 保存 ===
officecli set "OUT.pptx" '/slide[LAST]/shape[@name="文本框 10"]' \
  --prop text='谢谢观看\n敬请各位老师批评指正'
officecli close "OUT.pptx"
```
