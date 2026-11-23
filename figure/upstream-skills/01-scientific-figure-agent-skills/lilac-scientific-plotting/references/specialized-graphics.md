# Specialized Graphics And Adaptation Recipes

These document methods, inputs and design decisions without falsely claiming that every pattern was executed. Only the three executable wrappers identified below were implemented and tested. Other items are adaptation recipes: use the inputs and safeguards in the table, then verify the current package API when implementing one for a project. No access to the source book is needed. Common core: source data -> validate semantics/keys -> render -> inspect final size -> export and report assumptions.

## Tested Advanced Wrappers

### Sequence Logo
Source pp.130-134, codes 71-74. Input: aligned sequences or source frequency matrix. Original method: `ggseqlogo`, with optional `geom_logo`, region rectangles and text. Why it works: positions align across sequences; stacked character heights reveal conserved positions; selective region shading can mark a motif without covering letters. Probability and bits are different scales.

Codex implementation note: `sequence_logo(sequences, method)` handles ungapped ACGT strings only, checks equal length, requires an explicit chosen method when the default is not intended, and labels the y quantity. Tested for bits and probability. FASTA reading, protein logos, custom alphabets, and matrix input remain source patterns, not supported by this narrow wrapper. Do not treat display alignment as biological sequence alignment. Upstream ggseqlogo 0.2.2 emits a deprecated `guides(FALSE)` warning with ggplot2 3.5.2; figures rendered successfully, but future compatibility needs review.

### Chord
Source pp.143-149, code80. Input: named nonnegative matrix or source-target-weight table. Original method: `circlize::chordDiagram`, sector colors, alpha. Why it works: angular sectors establish entity identity and link widths show relationships; too many links become clutter and defeat exact comparison.

Codex implementation note: `draw_chord` is base graphics, not a ggplot; open a PNG/PDF device, draw, close that device in the caller. It clears circlize state even on error. Customize direction only when data actually represent directional flows. Distinct source/target names prevent unintended sector merging; symmetric undirected matrices may double-count conceptual edges if not prepared deliberately. Label length and device margins still need inspection.

### Spatial Choropleth
Source pp.149-161, codes84-89. Original method: polygon map + keyed region data, continuous or binned fill, diverging change, optional proportional symbols/pies. Why it works: neutral boundaries preserve spatial reference while fill or symbol size encodes an interpretable quantity. Binning reveals contrast but loses within-bin values, so record breakpoints.

Codex implementation note: `choropleth_plot` uses sf instead of legacy rgdal, requires CRS and unique joins, reports unmatched geography, retains all polygons and maps missing values to gray. Test used synthetic polygons, not a verified real-world boundary dataset. Use rates rather than raw counts when the question requires population-normalized risk; the function cannot infer denominators. Bivariate maps and map pies require separate explicit scales/legends and are not implemented here.

## Source Patterns Requiring Project-time Implementation

| Pattern / source | Input and original core | Controls and visual rationale | Do not change / verify | Status |
|---|---|---|---|---|
| Marginal distributions, pp.43-44 | scatter + `ggExtra::ggMarginal` | marginal type/size; align distributions to shared x/y | bin/bandwidth and group normalization; not a second unrelated scale | dependency absent, not run |
| Stacked area, pp.56-58 | ordered x, component, nonnegative values; `geom_area(position='fill')` for proportions | component order, palette, common denominator | no invented zero rows; upper bands lack common baseline; legend order follows stacks | method preserved, not run |
| Survival, pp.60-63 | time, event 0/1, group; `survival::survfit(Surv(time,event) ~ group)` + `survminer::ggsurvplot` | CI, censor marks, risk table, time units | event coding, risk-set definition and support; no substituted mean-time line | survminer absent, not run |
| Ternary, pp.63-67 | three nonnegative components; ggtern or Ternary | triangle labels, grid, color/size | meaningful common total and compositional interpretation; no unconstrained independent x/y/z | optional packages absent, not run |
| Radar, pp.67-70 | group rows, comparable normalized columns; ggradar | axis order, common normalization, few groups | disclose normalization; preserve original data separately; polygon area is not an effect size | not run |
| Pie/donut/rose, pp.70-77 | nonnegative category totals; geom_bar/col + coord_polar, optional ggpubr | consistent order, direct percentage labels, limited categories | denominator; radius/area distortion in rose plots; never hide tiny nonzero parts | not run |
| Waffle, pp.77-79 | counts/proportions -> grid cell categories; geom_tile | square aspect, cell size, named colors | document integer allocation/rounding and total cells; small parts may disappear | not run |
| Treemap, pp.79-81 | leaf values + nested category; treemapify area/fill/subgroup | subgroup borders, sparse fitting labels | areas nonnegative/additive; no overlapping unreadable labels | dependency absent, not run |
| Nested order/dumbbell, pp.95-100 | category/group value table; interaction order or segments + paired points | rank within category, horizontal labels, group colors | two values must share a meaningful category, not arbitrary pairings; IDs not regex-truncated blindly | not run; simpler ordered plot tested |
| Population pyramid, pp.101-104 | age band, sex/group, nonnegative population | mirror one group's coordinates, absolute-value tick labels | sign flip is display-only; preserve raw counts; state denominator/time, shared domain | not run |
| Venn/UpSet, pp.109-112 | unique element sets or list-column membership; VennDiagram/ggupset | small Venn or ordered intersection bars/dot matrix | count exclusive intersections correctly; no unlimited readability claim | optional dependencies absent, not run |
| Clustered heatmap, pp.113-116 | numeric feature matrix; heatmap/pheatmap | scaling direction, distance/linkage, row/column order | standardization changes quantity; arbitrary IDs are not distance features; avoid hidden missing-value imputation | clustering variant not run |
| Statistical brackets, pp.123-130 | chosen comparisons and valid analysis results; ggsignif/ggstatsplot | y placement, effect/interval annotation, declared p adjustment | test choice, pairing and multiplicity; formatting is not an analysis decision | not run |
| Phylogeny + metadata, pp.134-143 | validated tree + tip/node metadata; ggtree, tidytree, ape | tip/clade labels, posterior size, aligned heatmap/rings | unique tip joins, topology/branch lengths/time calibration intact; missing metadata explicit | specialist dependencies/data not run |
| Circular scatter/histogram tracks, pp.147-149 | sector, x, y; circos.initialize + trackPlotRegion + points/hist | common track scales, radial spacing, sector gaps | tracks need explicit y ranges and units; clear global circlize state | chord tested, track variants not run |
| Inset/shared-legend cowplot, pp.190-196 | ggplot/grob objects | plot_grid alignment, draw_plot inset, get_legend | no overlap with evidence; true common encodings before shared legend | patchwork composition tested; cowplot variants not run |

The artificial-ID dendrogram pp.82-84 is retained only as a historical case, not recommended analysis. Circle packing at p.84 is a mention without teaching code, so no recipe is fabricated. This separation preserves source breadth without shipping plausible but untested code.
