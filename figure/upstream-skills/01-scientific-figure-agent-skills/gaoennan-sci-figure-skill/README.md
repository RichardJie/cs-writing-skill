# sci-figure-skill

> Clean, journal-ready scientific **data figures** in matplotlib — an "Origin clean" style with a reusable palette and 14 ready-made plot templates. Ships as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skill, but the Python style module works standalone.
>
> 用 matplotlib 出**顶刊 / 一区 SCI（如 MSSP）风格**的科研数据图 —— "Origin 干净风" + 可复用调色板 + 14 类现成模板。以 Claude Code Skill 形式提供，Python 样式模块也可独立使用。

![overview](reference/overview.png)

*14 data-plot types × 2 simulated figures each. All labels are neutral placeholders; data is random (style demo only).*

---

## ✨ What you get / 内容

- **`sci_style.py`** — one call `set_style()` applies the whole look (Times-like serif, ticks-in, full box, no grid by default, 300 dpi) + a curated palette `C` and 4-class colors `CLASS4`.
- **`templates/plot_templates.py`** — 14 plot types (scatter, regression, per-sample, PCA/t-SNE, waveform, spectrum, real-vs-synthetic, training curve, method comparison, multi-line performance, bar, heatmap, spectrogram, 3D surface), 2 variants each.
- **`reference/style_spec.md`** — the full written style spec (中文).
- **`SKILL.md`** — the Claude Code skill definition.

## 🎨 The style in one breath / 风格一句话

White background · Times-like serif · italic math variables with bracketed units (`$x$ (mm)`) · ticks pointing **in** · four-sided box · **no grid** by default · restrained two-color palette · in-axes legend · annotate key values in place · export 300 dpi.

## 🚀 Quick start / 快速开始

```bash
git clone https://github.com/gaoennan/sci-figure-skill.git
cd sci-figure-skill
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt

# regenerate all 28 example figures
./.venv/bin/python templates/plot_templates.py
```

Use the style in your own script / 在你的脚本里复用：

```python
import sys; sys.path.insert(0, "/path/to/sci-figure-skill")
import sci_style as ss; ss.set_style()
import matplotlib.pyplot as plt
C = ss.C

fig, ax = plt.subplots(figsize=(4.4, 4.2))
ax.scatter(actual, predicted, s=20, c=C["orange"], label="Predicted")
ax.plot([0, 150], [0, 150], "--", color=C["red"])      # 1:1 reference line
ax.set_xlabel("Actual value (mm)"); ax.set_ylabel("Predicted value (mm)")
ax.legend(loc="upper left")
ss.save(fig, "out.png")
```

## 🎨 Palette / 调色板

| key | hex | role |
|---|---|---|
| `blue` | `#4472C4` | actual / true / real (primary) |
| `orange` | `#ED9A3D` | predicted (scheme A) |
| `red` | `#E8403A` | 1:1 line / emphasis / scheme B second line |
| `apricot` | `#F4C79A` | bars (with black edge) |
| `quad_bg` | `#F4F7E7` | quadrant background |
| `CLASS4` | red/blue/gold/cyan | 4-class clusters |
| colormap | `Reds` / `jet` | single-color weight heatmap / 3D & spectrogram |

Two interchangeable schemes: **A (blue + orange)** for quantitative eval (regression/scatter/bar), **B (blue + red)** for signal & training plots.

## 📊 The 14 types / 14 类

`localization` · `regression` · `per_sample` · `pca_domain` / `tsne` · `waveform` / `vibration` · `fft_spectrum` · `gan_overlay` · `training_curve` · `method_compare` · `performance_curve` · `bar_compare` · `heatmap` · `spectrogram` · `surface3d`

Each is a small function — copy it, swap in your data and labels, done. See `reference/style_spec.md` for the per-type recipe.

## 🤖 Use as a Claude Code Skill / 作为 Claude Code 技能

Copy this folder to `~/.claude/skills/sci-figure/` (so `SKILL.md` sits at its root). Then ask Claude things like *"draw a Loss curve / confusion matrix / t-SNE in journal (MSSP) style"* and it follows `SKILL.md`.

将本目录复制到 `~/.claude/skills/sci-figure/`，即可用"用顶刊/MSSP/Origin 风画一张…图"等触发。

## 🔤 Fonts / 字体

`sci_style` tries to register Times New Roman from common macOS/Windows/Linux paths; if none is found it falls back to Liberation Serif / matplotlib's built-in serif, so figures always render. On Linux, `sudo apt install fonts-liberation` (or msttcorefonts) gives the closest look.

## 📝 Notes / 说明

- Templates use **random data** — they demonstrate the *drawing style*, not real results. Replace with your data and remove demo-only annotations before publishing.
- Bundled figures and labels are neutral placeholders (`Signal A/B`, `Class 1–4`, `Method`, `Proposed`, …).

## 📄 License

MIT — see [LICENSE](LICENSE).

## 🙌 Contributing

Issues and PRs welcome: new plot types, better cross-platform fonts, or color-scheme presets. Keep the "Origin clean" invariants (white bg, ticks-in, no default grid, restrained color, in-place annotation).
