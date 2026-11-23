# Academic Layouts

本项目提供论文答辩高频页面布局，可从 `templates/single-page/` 复制到任意 deck 中使用。

| Layout | File | 用途 |
|---|---|---|
| Thesis Cover | `thesis-cover.html` | 论文题目、答辩人、导师、学院、日期 |
| Research Background | `research-background.html` | 研究背景、技术挑战、研究价值 |
| Literature Review | `literature-review.html` | 文献脉络、方法演进、研究空白 |
| Technical Route | `technical-route.html` | 研究目标、技术路线、整体流程 |
| Experiment Setup | `experiment-setup.html` | 数据集、指标、对比方法、环境 |
| Result Comparison | `result-comparison.html` | 指标对比、关键提升、结果解读 |
| Contributions | `contributions.html` | 创新点、贡献和论文价值 |
| Defense Q&A | `defense-qa.html` | 答辩备份问题和回答提示 |

## 使用方式

1. 打开对应 `templates/single-page/*.html`。
2. 复制完整 `<section class="slide">...</section>`。
3. 粘贴到目标 deck 的 `<main class="deck">` 内。
4. 替换示例内容。
5. 更新 `<aside class="notes">` 中的讲稿。
