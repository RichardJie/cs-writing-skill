---
description: Per-figure audit — claim alignment, caption takeaways, legibility, colorblind safety, vector/raster format, chart type.
argument-hint: "<figs dir|paper.tex>"
---

Audit the figures referenced by `$ARGUMENTS` — a figures directory, or a manuscript (locate its figures and captions). If the image files are readable, Read them and audit visually. Otherwise audit the source (TikZ, matplotlib/plotting scripts) plus the captions, and say which mode you used.

Six checks per figure, in this order. Claim alignment comes first: it is the highest-value check and the only one that can invalidate a figure outright.

### 1. Claim alignment

Find the sentence(s) in the manuscript that reference the figure. Does the figure actually evidence that sentence? Flag:
- prose claims pointing at a figure that does not support them (the worst case),
- figures no prose references — cut them or reference them,
- figure content that is interesting but the prose never uses.

### 2. Caption states the takeaway

A caption states the conclusion, not just the contents: "Accuracy saturates after layer 6" beats "Accuracy by layer." Rewrite weak captions with this formula: takeaway sentence first, then what is plotted, then details (n, what error bars mean, conditions).

### 3. Legibility at final size

- Fonts ≥ ~7 pt at column width — axis tick labels are the usual offender.
- Line weights that survive print; markers distinguishable in grayscale.
- No legend or annotation that requires zooming.

### 4. Colorblind safety

- Recommend Okabe–Ito or Paul Tol palettes for categorical series.
- Flag red–green encodings outright.
- Series should differ by more than hue: dash pattern, marker shape.

### 5. Vector vs raster

- Plots and diagrams must be vector (PDF/SVG). A rasterized line plot is a finding, not a taste issue.
- Photos and heatmaps are correctly raster — but ≥300 dpi at final printed size.

### 6. Chart-type appropriateness

- Bars for comparisons; lines for trends over an ordered axis.
- No dual-axis tricks. No truncated bar axes unless the caption flags the truncation.
- A pie chart is almost always a worse bar chart; say so.

## Report

Per figure, findings sorted by severity:

| Tier | Meaning |
|------|---------|
| **Blocking** | Misleads the reader or fails claim alignment |
| **Major** | A reviewer will notice: illegible text, red–green encoding, rasterized plot |
| **Minor** | Polish: caption wording, palette, marker choice |

End with two cross-cutting lists: figures no prose references, and prose claims no figure supports. If the figures are sound, say so — do not manufacture findings.
