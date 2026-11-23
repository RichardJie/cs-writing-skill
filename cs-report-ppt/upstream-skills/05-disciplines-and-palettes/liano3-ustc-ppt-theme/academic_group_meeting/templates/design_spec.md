---
deck_id: academic_group_meeting
kind: deck
display_name: Academic Group Meeting
display_name_zh: 简约学术组会
category: scenario
summary: 论文精读与组会汇报模板：四段导航、四种正文、完整开场与收尾，保留科大蓝标题带、校徽和论文页尾。
keywords:
- 学术
- 组会
- 论文精读
- 研究进展
- 简约
primary_color: '#004098'
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: 0 0 1280 720
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: 0 0 1280 720
replication_mode: standard
native_structure_mode: structured
page_count: 10
placeholders:
  01_cover:
  - '{{TITLE}}'
  - '{{SUBTITLE}}'
  - '{{AUTHOR}}'
  - '{{DATE}}'
  02_toc:
  - '{{TITLE}}'
  - '{{SUBTITLE}}'
  - '{{TOC_ITEM_1_TITLE}}'
  - '{{TOC_ITEM_1_DESC}}'
  - '{{TOC_ITEM_2_TITLE}}'
  - '{{TOC_ITEM_2_DESC}}'
  - '{{TOC_ITEM_3_TITLE}}'
  - '{{TOC_ITEM_3_DESC}}'
  - '{{TOC_ITEM_4_TITLE}}'
  - '{{TOC_ITEM_4_DESC}}'
  03_chapter:
  - '{{CHAPTER_TITLE}}'
  - '{{CHAPTER_CONTEXT}}'
  - '{{CHAPTER_FIGURE}}'
  04a_content_figure:
  - '{{PAGE_TITLE}}'
  - '{{SOURCE}}'
  - '{{PAGE_NUM}}'
  - '{{CONTENT_AREA}}'
  - '{{FIGURE_AREA}}'
  - '{{FIGURE_CAPTION}}'
  - '{{NAV_1}}'
  - '{{NAV_2}}'
  - '{{NAV_3}}'
  - '{{NAV_4}}'
  04b_content_wide:
  - '{{PAGE_TITLE}}'
  - '{{SOURCE}}'
  - '{{PAGE_NUM}}'
  - '{{FIGURE_AREA}}'
  - '{{FIGURE_CAPTION}}'
  - '{{NAV_1}}'
  - '{{NAV_2}}'
  - '{{NAV_3}}'
  - '{{NAV_4}}'
  04c_content_compare:
  - '{{PAGE_TITLE}}'
  - '{{SOURCE}}'
  - '{{PAGE_NUM}}'
  - '{{COLUMN_1_TITLE}}'
  - '{{COLUMN_1_BODY}}'
  - '{{COLUMN_2_TITLE}}'
  - '{{COLUMN_2_BODY}}'
  - '{{NAV_1}}'
  - '{{NAV_2}}'
  - '{{NAV_3}}'
  - '{{NAV_4}}'
  04d_content_free:
  - '{{PAGE_TITLE}}'
  - '{{SOURCE}}'
  - '{{PAGE_NUM}}'
  - '{{CONTENT_AREA}}'
  - '{{NAV_1}}'
  - '{{NAV_2}}'
  - '{{NAV_3}}'
  - '{{NAV_4}}'
  05_summary:
  - '{{PAGE_TITLE}}'
  - '{{CONTENT_AREA}}'
  06_references:
  - '{{PAGE_TITLE}}'
  - '{{REFERENCES}}'
  07_ending:
  - '{{THANK_YOU}}'
  - '{{ENDING_SUBTITLE}}'
  - '{{CONTACT_INFO}}'
---
# 简约学术组会 — Design Specification

## I. Template Overview
用于单篇论文精读与组会报告。模板共10种版式：封面、目录、图文过渡、四种正文、总结、参考文献、尾页。默认叙事为问题与挑战、方法设计、实验对比、结论；具体报告按内容调整。
视觉设计沿用本仓库 USTC 主题的科大蓝与标识，重新组织组会汇报结构；当前包为1个母版、10个版式。来源与许可见仓库根目录 THIRD_PARTY_NOTICES.md。

## II. Color Scheme
| Role | HEX | Use |
|---|---|---|
| Primary | #004098 | 标题带、侧栏、导航高亮 |
| Body | #172B43 | 正文、参考文献 |
| Secondary | #5E6D80 | 图注和辅助说明 |
| Field | #EEF3FA | 可替换图表的轻量占位区域 |
| Rule | #CFD9E6 | 分隔线 |
| Background | #FFFFFF | 页面背景与反白文字 |

## III. Typography
统一字体栈：Arial, Microsoft YaHei, PingFang SC, sans-serif。Latin使用Arial，中文使用Microsoft YaHei；PingFang SC作为Mac预览后备，不嵌入字体。

导出检查：SVG 的后备字体列表不等于 PPTX 内嵌字体，也不保证 Office 使用相同后备字体。制作前检查渲染环境能发现中文字体；换机演示前确认实际使用的字体。Linux 可安装 Noto Sans CJK SC 并在渲染环境中明确替换。对保留手工换行的正文，导出器应保留合理宽度余量，计入中文引号及中英／数字混排的间距；不要统一放大所有文本框、逐页缩字或改动精确占位框来掩盖测量误差。交付前检查实际 PPTX 导出的 PDF，尤其是长标题、中文日期和多行正文。仓库的 `docs/font-rendering.md` 提供环境检查脚本及版本限定的导出器补丁。

| Role | SVG px | PowerPoint pt | Weight |
|---|---:|---:|---|
| 封面 / 尾页主标题 | 48 | 36 | Bold |
| 目录 / 总结侧栏标题 | 44 | 33 | Bold |
| 参考文献竖排标题 | 40 | 30 | Bold |
| 章节过渡标题 | 38 | 28.5 | Bold |
| 正文页标题 | 34 | 25.5 | Bold |
| 正文 / 栏目小标题 | 28 | 21 | Regular / Bold |
| 姓名 / 联系信息 | 26 | 19.5 | Regular |
| 日期 / 参考文献 / 图表占位提示 | 24 | 18 | Regular |
| 目录描述 | 22 | 16.5 | Regular |
| 导航 / 图注 | 20 | 15 | Regular；当前导航Bold |
| 页尾 / 页码 | 18 | 13.5 | Regular |
正文不整段加粗；仅概念标签或短关键词可用粗体。封面主标题可1–3行，长标题使用1.2倍行距，不把长英文题目强行塞成一行。正文常用行距1.35倍，段落间留0.6倍字号，文献1.4倍行距。图注支持两行。具体实际内容须按框测量，溢出优先拆页或改选布局，不逐页任意缩字。空白是容纳真实图表和研究内容的空间，不要求AI填满。

## IV. Signature Design Elements
封面与尾页：x=32/y=32的完整校名标识（360×60.38），中央y=160–430深蓝横幅，短标题、来源与姓名居中。目录与总结：360px左侧蓝栏，校徽x=32/y=32、64px，标题x=48/y=320。参考文献：右侧340px蓝栏，64px校徽距右/顶32px，标题逐字纵向排列。过渡页：上部文字与图示，下部y=545–675标题蓝带，64px校徽距右32px。
四种正文：顶部30px四段导航，y=30–98标题带，54px校徽距右32px，底部y=692–720蓝色页尾。独立校徽白底外扩2px。内容页保留可编辑标题、导航、论文出处与页码。默认用左文右图，宽图用上图下文，明确比较用双栏，特殊内容用自由页。不要另外发明流程、公式或实验专用版式。
导航高亮只由实际章节决定，不能由正文版式决定。手工编辑可复制当前章节的页面再替换内容；切换章节时移动高亮块并调整相应标签颜色。AI生成时，高亮作为Slide-local状态（不要增加或修改同一Layout的固定原子），或为状态显式建立不同Layout身份；不可悄悄改变共享版式结构。
单位标识、色带为固定版式元素，避免误拖；真实图表应替换object内容区域，保留原始比例、图例与坐标轴。示例文字、图提示、论文出处均须替换，参考文献示例不代表真实条目。

## V. Page Roster
| File | Layout / Picker | Editable slot frames (x y w h) |
|---|---|---|
| `01_cover.svg` | 01-cover / 封面 | title: 64 180 1152 180; subtitle: 80 370 1120 50; author: 80 475 1120 45; date: 80 530 1120 42 |
| `02_toc.svg` | 02-toc / 目录 | title: 48 320 264 84; subtitle: 48 420 264 76; toc-item-1-title: 500 85 700 48; toc-item-1-desc: 500 141 700 50; toc-item-2-title: 500 230 700 48; toc-item-2-desc: 500 286 700 50; toc-item-3-title: 500 375 700 48; toc-item-3-desc: 500 431 700 50; toc-item-4-title: 500 520 700 48; toc-item-4-desc: 500 576 700 50 |
| `03_chapter.svg` | 03-chapter / 章节过渡 | chapter-title: 64 570 1060 80; chapter-context: 64 80 548 400; chapter-figure: 670 90 546 390 |
| `04a_content_figure.svg` | 04a-content-figure / 左文右图 | page-title: 40 42 1095 54; source: 40 693 1100 27; page-num: 1174 693 66 27; content-area: 64 202 390 410; figure-area: 524 222 668 328; figure-caption: 500 599 716 50; nav-1: 20 1 184 28; nav-2: 230 1 184 28; nav-3: 440 1 184 28; nav-4: 650 1 184 28 |
| `04b_content_wide.svg` | 04b-content-wide / 上图下文 | page-title: 40 42 1095 54; source: 40 693 1100 27; page-num: 1174 693 66 27; figure-area: 90 222 1100 312; figure-caption: 64 582 1152 64; nav-1: 20 1 184 28; nav-2: 230 1 184 28; nav-3: 440 1 184 28; nav-4: 650 1 184 28 |
| `04c_content_compare.svg` | 04c-content-compare / 双栏对照 | page-title: 40 42 1095 54; source: 40 693 1100 27; page-num: 1174 693 66 27; column-1-title: 64 200 548 48; column-1-body: 64 294 548 266; column-2-title: 668 200 548 48; column-2-body: 668 294 548 266; nav-1: 20 1 184 28; nav-2: 230 1 184 28; nav-3: 440 1 184 28; nav-4: 650 1 184 28 |
| `04d_content_free.svg` | 04d-content-free / 自由内容 | page-title: 40 42 1095 54; source: 40 693 1100 27; page-num: 1174 693 66 27; content-area: 64 170 1152 470; nav-1: 20 1 184 28; nav-2: 230 1 184 28; nav-3: 440 1 184 28; nav-4: 650 1 184 28 |
| `05_summary.svg` | 05-summary / 总结 | page-title: 48 320 264 84; content-area: 410 110 810 500 |
| `06_references.svg` | 06-references / 参考文献 | page-title: 968 88 80 320; references: 80 94 800 540 |
| `07_ending.svg` | 07-ending / 致谢与讨论 | thank-you: 64 230 1152 90; ending-subtitle: 80 350 1120 50; contact-info: 80 490 1120 50 |

## VI. Assets
images/ustc-emblem.png：科大蓝圆形校徽；images/ustc-wordmark.png：无阴影完整中英文校名标识。两者来源于 https://jbyang1987.github.io/ustclogo/图片.html ，保持原始比例与颜色。

## VII. Placeholder Overrides
Frontmatter是完整token清单。参考文献PAGE_TITLE填入“参、考、文、献”四行；其余长正文左上对齐、按宽度换行。章节过渡图示可替换为概念图或章节关键问题。总结使用单一正文框自由组织贡献、局限与启发，不要求固定条数。参考文献过多可复制续页。
