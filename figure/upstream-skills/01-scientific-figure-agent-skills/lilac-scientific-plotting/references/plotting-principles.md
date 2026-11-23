# Plotting Principles

## Decisions Before Decoration

- Source pp.8-20: establish purpose and data organization, then build mappings, geometry, scales, coordinates, and theme. A chart is an argument supported by observations, not a gallery choice.
- Derived synthesis pp.21-25,48-60,84-109: distinguish raw observations, distribution summaries, model predictions, and category totals. Similar shapes can encode different quantities; state the statistical layer.
- Source pp.26-37: a mapped aesthetic communicates variation; a fixed aesthetic supplies styling. Put category-to-color mappings inside `aes`, a uniform point color outside. Independent outline/fill requires an appropriate point shape.

## What The Visual Comparisons Teach

| Source | Observed comparison | Reusable decision and tradeoff |
|---|---|---|
| pp.21-25 | Histogram/KDE/box/violin expose different distribution features | Choose bins/bandwidth and disclose sample size; a box is compact but hides multimodality. Raw points are valuable for small groups. |
| pp.28-37 | Point size, fill, border, alpha and palettes | Hollow/filled symbols alter overlap readability. Fine borders rescue pale marks; large dark borders can dominate. Alpha changes occlusion, not sample weighting. |
| pp.40-45 | Scatter versus density contours and ridges | Density can reveal concentration where points overlap, but smoothing can erase structure. Ridgelines share x units and trade some baseline clarity for compactness. |
| pp.49-51 | Points over lines; fixed versus free facets | Drawing points last keeps observation locations distinct. Free scales expose within-panel shape but sacrifice absolute slope comparison. |
| pp.52-55 | Paired endpoints connected directly | Linking reveals direction and within-person change; dense endpoint labels need repulsion or subsetting, not changed measurements. |
| pp.87-95 | Default bars versus reference lines, sorted horizontal bars, lollipops | Perpendicular light guides help value lookup. Ordering reduces search. Horizontal orientation gives long labels room; lollipops reduce ink without removing zero baseline. |
| pp.97-98 | Alphabetical/mixed categories versus nested ordering | Preserve meaningful higher-level grouping and sort within it. Do not use a global rank if it hides the hierarchy under study. |
| pp.107-109 | Bars/points/lines with intervals | Interval endpoints belong to the same group and x-position as the estimate. Point-range plots emphasize estimates without implying an area or total. |
| pp.114-116 | Heatmap values, clustering, overlaid ranks | Color reveals a matrix pattern; sparse labels enable exact lookup. Rank and raw magnitude are not interchangeable. Cluster only justified distances. |
| pp.118-123 | Full labels versus selective labels/highlights | A neutral context layer plus a few labeled focal observations establishes hierarchy. Annotations need actual model results, not manually typed statistics. |
| pp.173-179 | Background, guides, guide size and encoding repetition | Remove noninformative grid directions, not all grids. Put legends in real whitespace; accessibility can justify two encodings of one variable. |
| pp.190-200 | Unaligned panels versus aligned/nested layouts | Align plotting regions, not merely image edges. Allocate width based on content; use a small inset only when it leaves evidence visible. |

## Limits Of The Book's Advice

Codex implementation note: this book's examples and aesthetic preferences are not statistical or accessibility standards. Review [corrections](provenance-and-corrections.md) before treating a claim as universal. Do not copy the book's watermarks, specimen data, or visual distortions. Preserve a short decision record using `assets/figure-brief.md` when a complex figure would otherwise be hard to reproduce.
