---
name: sci-figure
description: 科研数据图绘制（顶刊 / 一区SCI / MSSP 风格）—— "Origin 干净风"：Times 衬线、刻度朝内、默认无网格、双色克制配色、关键值就地标注、300 dpi；内置 14 类数据图模板与可复用 matplotlib 样式。当用户要画/出/重画科研数据图（散点·折线·柱状·热力矩阵·时频谱·3D曲面等），或要求"顶刊风格 / 一区SCI 风格 / MSSP 风格 / SCI 期刊风格 / Origin 风 / 美观的论文配图"时使用。
---

# 科研数据图绘制（顶刊 / 一区SCI / MSSP 风格）

用 matplotlib 出符合一区 SCI（如 MSSP）排版习惯的 **"Origin 干净风"** 科研数据图。本技能 = 风格规范 + 调色板 + 14 类现成模板。

## 触发场景
- "用顶刊 / 一区SCI / MSSP / SCI 期刊 / Origin 风画一张 …图（Loss 曲线 / t-SNE / 散点 / 柱状 / 热力图 / 时频谱 / 3D 曲面 …）"
- "把这张图改美观一点 / 改成论文配图风格"
- 给真实数据，要求按该风格出图

## 环境（重要）
需要 `numpy` 与 `matplotlib`。若系统 python 缺少，建一个 venv（位置随意）：
```bash
python3 -m venv .venv && ./.venv/bin/pip install -q numpy matplotlib
```
脚本里先 `import sci_style as ss; ss.set_style()`（`sci_style.py` 在本技能根目录；`templates/` 已自动把根目录加入 `sys.path`）。
字体：`sci_style` 会尝试注册 Times New Roman（macOS/Windows/Linux 常见路径），找不到时回退到 Liberation Serif / matplotlib 内置衬线，图仍可正常出。Linux 上如需 Times 外观可装 `fonts-liberation` 或 msttcorefonts。

## 快速开始
```python
import sys; sys.path.insert(0, "<本技能目录>")
import sci_style as ss; ss.set_style()
import matplotlib.pyplot as plt
C = ss.C
fig, ax = plt.subplots(figsize=(4.4, 4.2))
ax.scatter(actual, pred, s=20, c=C["orange"], label="$x$ coordinate")  # predicted
ax.plot([0,150],[0,150], "--", color=C["red"])                          # 1:1 基准
ax.set_xlabel("Actual value (mm)"); ax.set_ylabel("Predicted value (mm)")
ax.legend(loc="upper left"); ss.save(fig, "out.png")
```

## 风格铁律（必须遵守）
1. **字体**：Times New Roman 衬线；数学变量斜体 `$x$ $\lambda$ $R^2$`；单位用正体括号 `(mm) (Hz) (V) (%)`。
2. **底/框/刻度**：纯白底（空间定位散点除外）、四边全框、刻度**朝内**。
3. **网格**：默认**无**；仅"性能多线曲线"用浅灰 Excel 网格。
4. **图例**：图内（顶部/角落），细框或无框，字号略小。
5. **标注就地化**：柱顶写数值、方框包裹关键指标（如 `Domain Distance: 3.364`）、红圈+红箭头点重点/平均。
6. **配色克制**：数据图以双色为主，别花。输出 300 dpi、`bbox_tight`。

## 配色板（`sci_style.C`）
| key | 色值 | 用途 |
|---|---|---|
| blue | `#4472C4` | 真值/实际/Real（主色）|
| orange | `#ED9A3D` | 预测（配色方案 A，蓝●+橙×）|
| red | `#E8403A` | 1:1 基准虚线 / 强调 / 配色方案 B 第二条线 |
| apricot | `#F4C79A` | 柱状图柱色（+黑描边）|
| black | `#000000` | 节点 / Base 信号 |
| quad_bg | `#F4F7E7` | 空间定位散点淡黄绿底 |
| CLASS4 | 红/蓝/金/青 | 4 分类（如 t-SNE 聚类）|
| colormap | `Reds`(白→红) / `jet` | 单色权重热力图 / 3D 曲面·时频谱 |

## 14 类数据图速查（模板在 `templates/plot_templates.py`）
| # | 类型 | 模板函数 | 要点 |
|---|---|---|---|
| 1 | 空间定位散点 | `localization` | 象限+角点黑节点+蓝●/橙×，可加红箭头"Average" |
| 2 | 回归对角线散点 | `regression` | 蓝+橙点 + 红虚线 1:1 |
| 3 | 逐样本散点 | `per_sample` | Sample index–value，●/× |
| 4 | 降维特征散点 | `pca_domain` / `tsne` | PCA 方框标注 / t-SNE 四色聚类 |
| 5 | 信号波形 | `waveform` / `vibration` | 黑/红双线 / 蓝Real+红Synthetic |
| 6 | 频谱+峰值标注 | `fft_spectrum` | 蓝线 + 峰值斜体标注 $f_1,2f_1$ |
| 7 | 真实vs生成对比 | `gan_overlay` | 蓝Real/红Synthetic 叠加，按条件分图 |
| 8 | 训练收敛曲线 | `training_curve` | Loss/Score–Epoch，蓝/红 |
| 9 | 方法对比折线 | `method_compare` | Accuracy–SNR，开口marker，"Proposed"金色加粗 |
| 10 | 多线性能曲线 | `performance_curve` | Value–$x$，多线+marker+**网格** |
| 11 | 柱状对比 | `bar_compare` | 杏色柱+黑边+柱顶数值 |
| 12 | 单色权重热力图 | `heatmap` | 白→红 + colorbar + 数值 |
| 13 | 时频谱 | `spectrogram` | jet（蓝为底），Freq–Time |
| 14 | 3D 曲面 | `surface3d` | jet + colorbar + 峰值文字箭头 |

用法：`from plot_templates import regression` 改数据/标签直接出图；或复制对应片段改成真实数据。一次性重出全部示例：`python templates/plot_templates.py`（写到其同目录 `sim_figs/`）。

## 两种配色方案（可按刊物/审美切换）
- **方案 A（蓝 + 橙）**：蓝●真值 / 橙×预测；热力图用白→红单色；几乎无网格 → 偏定量评估（回归/散点/柱状）。
- **方案 B（蓝 + 红）**：蓝 Real / 红 Synthetic 或 baseline；3D/时频/云图用 **jet 彩虹**；性能曲线带网格 → 偏信号+训练过程。

## 注意
- 模板用随机数据仅演示画法；出正式图请替换真实数据，并去掉演示性标注。
- 详细规范见 `reference/style_spec.md`，整体观感见 `reference/overview.png`。
- EMF/WMF（Origin/Visio/Word 矢量图）转 PNG：用 LibreOffice `soffice --headless --convert-to pdf` 再 `pdftoppm`（ImageMagick 无 EMF 委托）。
