# Source Index

Bibliographic inspiration: *SCI论文绘图之道*, Leopard / 医学方, postscript July 2019. This index is optional provenance, not an operating manual or a substitute for the book.

The source is an R/ggplot2 book; no Python plotting chapter was found. Pages below are inclusive and may overlap at topic transitions. Code numbers are printed labels, not unique IDs: 35 is reused; axis text says 108 while the screenshot says 109. These page pointers provide attribution only. Every usable instruction needed for this skill is in the other files in this directory.

Classes: A principle, B reusable pattern, C parameterized code family, D case/version-specific example. `Keep` refers to knowledge retention, not verbatim reproduction or proof every source script runs.

| Chapter / pages | Topic / chart | Language / libraries | Visual design | Code | Keep |
|---|---|---|---|---|---|
| Front 1-4 | Cover, contents | none | navigation | no | index only |
| Preface 5-7 | Motivation | none | purpose | no | contextual D |
| 1 / 8-11 | Research figure planning | R context | intent, sketch, data | no | A/B |
| 2 / 11-20 | Grammar, data, layers | R, ggplot2 | mapping, scales, themes | yes | A/B/C |
| 3 / 20-25 | Distributions | R, ggplot2 | bins, density, box, violin | yes | A/B/C |
| 3 / 26-37 | Scatter encodings | R, ggplot2 | color/fill/shape/size/stroke | yes | A/B/C |
| 3 / 37-40 | Bubbles | R, ggplot2 | size range, extremes | yes | B/C with correction |
| 3 / 40-43 | 2D density | R, ggplot2 | contours, occlusion | 18 | B/C |
| 3 / 43-45 | Marginals, ridges | R, ggExtra, ggridges | shared scales, distributions | 19-21 | B/C |
| 3 / 45-48 | Correlation matrix | R, ggcorrplot | triangle, diverging scale | 22-23 | B/C |
| 3 / 48-52 | Line trends | R, ggplot2 | layer order, scale/facet | yes | A/B/C |
| 3 / 52-56 | Paired slopegraphs | R, ggplot2 | links, direct labels | 27-28 | B/C; case distortion D |
| 3 / 56-58 | Stacked area | R, ggplot2 | total versus composition | 29 | B/C |
| 3 / 58-60 | Fitted smooths | R, ggplot2 | group/global fits, ribbons | 30-31 | B/C with correction |
| 3 / 60-63 | Survival | R, survival, survminer | step, CI, risk table | 32 | B/C pattern |
| 3 / 63-67 | Ternary | R, ggtern, Ternary | three-part composition | 33-35 | B/C pattern |
| 3 / 67-70 | Radar | R, ggradar | normalization, axis order | 35 reused | B/D pattern |
| 3 / 70-79 | Pie, rose, donut, waffle | R, ggplot2, ggpubr | proportion, polar, tiled units | 36-41 | B/C; caveats |
| 3 / 79-84 | Treemap, dendrogram | R, treemapify, dendextend | hierarchy, area, leaves | 42-43 | B; artificial-ID clustering D |
| 3 / 84-95 | Bars, lollipop | R, ggplot2 | count/identity, order, orientation | 44-51 | A/B/C |
| 3 / 95-106 | Grouped/dumbbell/radial bars | R, ggplot2 | nested order, dodge/stack | 52-55 | B/C |
| 3 / 106-109 | Error bars/lines/points | R, ggplot2 | interval and point alignment | 56-57 | A/B/C |
| 3 / 109-112 | Venn, UpSet | R, VennDiagram, ggupset (UpSetR mentioned) | set sizes, intersections | 58-59 | B/C pattern |
| 3 / 112-117 | Heatmaps | R, ggplot2, pheatmap | scaling, ordering, clustering | 60-62 | A/B/C |
| 3 / 117-123 | Highlight, labels | R, ggrepel, gghighlight | emphasis, computed annotation | 63-66 | A/B/C |
| 3 / 123-130 | Statistical annotations | R, ggsignif, ggstatsplot | tests, paired comparisons | 67-70 | B; assumptions required |
| 3 / 130-134 | Sequence logos | R, ggseqlogo | probability versus bits | 71-74 | B/C |
| 3 / 134-143 | Phylogenetic trees | R, ggtree, tidytree, ape | topology, tip/clade annotation | 75-79 | B/C pattern |
| 3 / 143-149 | Chord/circular tracks | R, circlize | sectors, links, track space | 80-83 | B/C |
| 3 / 149-161 | Maps | R, ggplot2, legacy rgdal, scatterpie | joins, projection, fill, symbols | 84-89 | A/B/C; sf migration explicit |
| 4 / 161-170 | Color systems | R, ggsci, RColorBrewer, paletteer | categorical, sequential, diverging | 90-95 | A/B/C |
| 5 / 170-174 | Themes/background | R, ggplot2 | useful grid, hierarchy | 96-97 | A/B/C |
| 5 / 174-179 | Legends | R, ggplot2 | position, guide size, redundancy | 98-100 | A/B/C |
| 5 / 179-181 | Facets | R, ggplot2 | shared/free scales, spacing | 101-102 | A/B/C |
| 5 / 181-184 | Mark sizes | R, ggplot2 | point, bar, legend balance | 103-105 | A/B/C |
| 6 / 184-189 | Axes | R, ggplot2 | transformations, ticks, second axis | 106-107,109 | A/B/C with correction |
| 7 / 189-196 | Multi-panel composition | R, cowplot | alignment, nesting, inset, legend | 110-115 | A/B/C |
| 7 / 196-201 | Layout grammar | R, patchwork | relative dimensions, layout | 116-117 | A/B/C |
| 7 / 201-205 | Output | R, ggplot2, Cairo, export | physical size, raster/vector | 118 (p.205) | A/B/C |
| End / 205-206 | Postscript | none | context | no | D, not core |
| End / 207 | Promotion | none | none | no | exclude |

Circle packing is only mentioned at p.84, not taught: no invented recipe. Source case files are not supplied; reconstructed executable recipes use new simulated data. See [provenance](provenance-and-corrections.md) for extraction coverage and [catalog](recipe-catalog.md) for validation status rather than assuming every row is executable.
