# Provenance And Corrections

## Extraction And Scope

The source is an R plotting book with code and figure examples. The original datasets and scripts referred to by the author were not available during construction. The page-specific notes below identify advice that needs qualification; they do not require the reader to consult the book.

The original book and its PDF are not bundled or needed. This skill contains independent synthesis and parameterized implementations, not a repackaged copy of the book. The included [validation script](../tests/validate_recipes.R) uses synthetic data and can be rerun without the book.

Classes: A principles; B patterns; C reusable code; D historical/specific cases. `Source` cites an author's method; `Derived synthesis` combines cited examples; `Codex implementation note` identifies additions/corrections. Every shipped R function is an engineering adaptation, not claimed verbatim source code.

## Source Claims Requiring Qualification

| Pages | Source issue | Codex implementation note |
|---|---|---|
| 16-17 | Only long-format data framed as drawable | Long/tidy is useful for repeated measures and facets, not a requirement that all ggplot data frames have one universal shape. |
| 24 | Alpha direction described incorrectly | 0 transparent, 1 opaque. |
| 28-29 | Filled/solid point terminology | `fill` controls shapes 21-25; solid 15-20 are colored by `colour`. |
| 39 | Removing extremes for bubble appearance | Never discard valid observations for aesthetics alone. |
| 41 | Close contour lines treated as high density | Spacing conveys gradient at chosen contour levels; evaluate density values. |
| 50-51 | Free-scale slopes compared | Equal visual slopes need not mean equal absolute rates. |
| 53-54 | Slopegraph preprocessing changes coordinates/NA | Retain actual values and missingness; label-only displacement. |
| 59-60 | Default smoother / GAM equivalence oversimplified | Choose method/formula explicitly; a smooth term is not a linear term. |
| 61 | Risk-table description vague | Risk set excludes previous events/censoring; not simple live/dead counts. |
| 63-66 | Ternary framed as general three-variable plot | Use interpretable nonnegative composition with a meaningful common total. |
| 68 | Radar rescaling | Normalization removes original units; disclose range/reference. |
| 82-83 | hclust on manufactured numeric IDs | Demonstrates a picture, not valid scientific dissimilarity. Retain as D. |
| 111 | Venn central intersection described as smallest | Exclusive-region counts have no such ordering rule. |
| 122 | Typed R-squared in annotation | Compute from the model and data actually plotted. |
| 125,130 | Package/style preferences | Do not turn personal criticism of ggpubr into a universal ban. |
| 130-134 | Logo scales | Probability and information height answer different questions. |
| 153 | Removing NA before map drawing | Keep geographic coverage and disclose missing values/join failures. |
| 157 | Historical boundary-source commentary | Choose documented appropriate geography/CRS/version; no manual boundary fabrication. |
| 160 | Repeated scale discussion | A new fill scale can replace an earlier scale; it is not invariably an error. |
| 174,177 | No-grid/no-redundant-encoding preference | Keep useful grids and accessibility-supporting redundant encodings. |
| 188 | Dual axes | Require a one-to-one transform of the same scale. |
| 196 | Combining base and grid plots | Base plots require capture/conversion, not automatic grob compatibility. |
| 201-204 | Vector/DPI/antialiasing statements | Vector containers can contain raster; antialiasing is not infinite resolution. |

## Declared API Adaptations

- `..density..` / `..level..` -> `after_stat(density)` / `after_stat(level)` where needed; same computed statistic, modern syntax.
- Line `size` -> `linewidth`; point `size` remains size. `expand_scale` -> `expansion`.
- Numeric legend position -> `legend.position='inside'` and `legend.position.inside` when an internal legend is appropriate.
- Legacy rgdal/maptools workflows -> explicit `sf` geometry and join validation. This is a declared implementation migration, not the source's original code.
- Recipe functions use explicit column arguments and namespace calls. Dependencies are checked, not auto-installed. Missingness fails clearly rather than being silently dropped.

The tree-integrity rule at p.136 agrees with the author: formatting must not change evolutionary distances. It is a retained source invariant, not a correction.

Official documentation consulted during construction (2026-09-27; recheck when migrating versions): [aesthetics](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html), [line/point size](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html), [computed aesthetics](https://ggplot2.tidyverse.org/reference/aes_eval.html), [smoothing](https://ggplot2.tidyverse.org/reference/geom_smooth.html), [secondary axes](https://ggplot2.tidyverse.org/reference/sec_axis.html), [theme](https://ggplot2.tidyverse.org/reference/theme.html), [spatial package retirement](https://r-spatial.org/r/2023/05/15/evolution4.html), [ggseqlogo](https://omarwagih.github.io/ggseqlogo/).
