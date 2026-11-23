# Chart Selection

Start with question -> observational unit -> variables -> estimand -> graphical encoding. The table is a derived synthesis of the cited examples; the cautions are Codex implementation notes.

| Question / structure | Candidate | Source | Check before drawing |
|---|---|---|---|
| Distribution of one measurement | histogram/KDE, box/violin plus raw points | pp.21-25 | n, binwidth/bandwidth, bounded domains; density is not count |
| Association between two quantities | scatter, optional explicit model | pp.26-43,58-60 | independent units, transformations, confounding; correlation is not causation |
| Association with a third magnitude | bubble with area scale | pp.37-40 | nonnegative magnitude, units and size legend; do not hide extremes |
| Many overlapping observations/groups | 2D density, facets, ridgelines | pp.40-45 | count versus normalized density, consistent scales/bandwidth |
| Ordered sequence / time | line with observed points | pp.48-52 | true ordering, missing time points, separate subjects/groups |
| Two observations per subject | slopegraph / paired lines | pp.52-56 | real IDs and complete pairs; do not link unrelated averages |
| Group estimates with uncertainty | dot-and-interval, optionally bars | pp.106-109 | estimator, CI/SE/SD and confidence level, repeated measurements |
| Category magnitudes / rank | ordered bars, lollipop | pp.84-106 | preaggregated versus count, zero baseline, natural order |
| Part-to-whole | stacked bar; few-category pie/donut or waffle | pp.70-81 | nonnegative parts, denominator, rounding; bars allow better comparisons |
| Composition over ordered x | stacked area | pp.56-58 | mutually exclusive components, common denominator, order |
| Three-part composition | ternary | pp.63-67 | same meaningful total; not arbitrary independent dimensions |
| Matrix / associations | heatmap / correlation matrix | pp.45-48,112-117 | scaling direction, missing cells, comparable units, clustering method |
| Time to event | survival curve with CI and risk table | pp.60-63 | censoring definition, event coding, risk-set support |
| Intersections of sets | Venn for few sets, UpSet for many | pp.109-112 | unique IDs, exclusive intersection counts, readable combinations |
| Aligned sequences | logo | pp.130-134 | alignment, alphabet, gaps, probability versus information |
| Evolutionary hierarchy | phylogeny + metadata | pp.134-143 | valid tree, tip joins, topology/branch-length integrity |
| Weighted source-target relationships | chord diagram | pp.143-146 | directional meaning, weights, duplicated reciprocal edges |
| Spatially indexed measurements | choropleth / proportional symbols | pp.149-161 | boundary version, CRS, join completeness, count versus rate |

Radar and polar bars (pp.67-70,73-75,100-104) are source patterns, not default upgrades. Axis ordering, area distortion, and normalization can obscure comparisons; choose them only when their structure answers the question. Circle packing has no substantive tutorial in this source.
