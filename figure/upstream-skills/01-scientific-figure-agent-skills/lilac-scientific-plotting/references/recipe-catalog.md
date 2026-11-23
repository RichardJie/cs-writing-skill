# Recipe Catalog

All executable recipes are new parameterized R adaptations of cited source patterns. They preserve the named graphical/statistical method within the stated contract, not every variant shown in the book. Source `scripts/figure-tools.R` first, then only the relevant file. Inputs are data frames with column names passed as strings unless otherwise noted. Most functions return a ggplot that can be modified with `labs`, scales, guides and theme. No function downloads data or installs dependencies.

## Tested Executable Recipes

Validation: simulated-data tests on R 4.5.0, ggplot2 3.5.2; construction-time versions and limits are in [validation status](validation-status.md). `Source` below refers to rationale/method, not a verbatim transcription.

| File / function | Use and input | Safe controls | Invariant / common error | Output / source |
|---|---|---|---|---|
| `distributions.R`: `distribution_plot` | One finite continuous column | positive binwidth, labels, dimensions | Histogram and density use density units; not a count overlay. KDE unsupported for constant/tiny samples. | ggplot; pp.21-25 |
| `group_distribution` | Raw measurements and category | violin on/off, jitter seed, category factor order | Horizontal jitter only; raw points retain values; box outlier layer hidden only because all points are shown separately. | ggplot; pp.21-25 |
| `ridge_plot` | Raw values and grouping column | explicit bandwidth, category order | Same x units/bandwidth; normalized ridges are not sample-size counts. | ggplot; pp.44-45 |
| `relationships.R`: `scatter_fit` | Finite x/y, optional group | `fit_scope=group/overall`, CI level | OLS `y ~ x` only; >=3 rows and varying x per fit. No automatic log/LOESS/GAM substitution. Ribbon is pointwise fitted-mean CI. | list: plot/models/statistics/predictions; pp.58-60 |
| `bubble_plot` | x/y, nonnegative magnitude, optional group | maximum point size, labels | Area maps magnitude, zero area for zero; no aesthetic exclusion of extremes. Log-size variants need an explicit scientific decision. | ggplot; pp.37-40 |
| `density2d_plot` | Continuous x/y, >=10 varied rows | number of contours; adapt bandwidth only explicitly | Density levels, not contour spacing alone, encode concentration. Shared group comparisons require common estimation settings. | ggplot; pp.40-43 |
| `highlight_scatter` | x/y, labels, explicit logical selection | seed, font/point sizes after creation | Selection is user/analysis-defined, not automatically significant. Move labels, never measurements. Inspect crowding when many selected. | ggplot; pp.117-123 |
| `comparisons.R`: `trend_plot` | One value per numeric x/group | factor order, scale labels, theme | Duplicate keys fail; aggregate deliberately. Missing time intervals need explicit handling; this function does not infer an expected calendar. | ggplot; pp.48-52 |
| `paired_slope` | Real ID, occasion, value; two ordered occasions | point/line styling, axis title | Exactly two unique complete rows per ID. No inferred pairs, replacement zeros or changed y positions. | ggplot; pp.52-56 |
| `ordered_values` | One precomputed value per category | bar/lollipop; explicit bottom-to-top category order | Default sorts ascending bottom-to-top; override for natural order. Baseline zero remains in view. No automatic aggregation. | ggplot; pp.89-95 |
| `grouped_bars` | One nonnegative value per category/group | dodge, stack or fill | Precomputed values use geom_col, not row counting. Fill normalizes within category; denominator and missing category/group cells require caller review. | ggplot; pp.84-99 |
| `estimates.R`: `estimate_plot` | Precomputed estimate/lower/upper, x category, optional group | connect for ordered x, reference line, interval label | Unique x/group; bounds contain estimate; same dodge object for interval/line/point. Do not change bounds for aesthetics. | ggplot; pp.106-109 |
| `matrices.R`: `heatmap_plot` | Explicit rectangular long table incl. NA cells | midpoint only if meaningful, limits incl. all values | Duplicate/missing keys fail; no implicit clustering/standardization. Caller must say whether values are raw, normalized or ranks. Gray is missing. | ggplot; pp.112-117 |
| `correlation_plot` | >=2 varying numeric columns, complete rows | Pearson or Spearman | No automatic pairwise deletion, p-value stars or causal interpretation. Fixed [-1,1] diverging scale. | list: plot/matrix/n/method; pp.45-48 |
| `layouts.R`: `compose_panels` | List of compatible plot objects | ncol, widths/heights, tags | Guides retained unless caller explicitly confirms shared encoding. Layout choice does not harmonize scientific scales automatically. | patchwork; pp.196-201 |
| `specialized.R`: `sequence_logo` | >=2 aligned equal-length uppercase DNA strings ACGT | bits or prob | No alignment, amino acids, gaps or ambiguous bases in this narrow wrapper. Probability stacks sum to 1; bits indicate information. | ggplot; pp.130-134 |
| `draw_chord` | Nonnegative named matrix of source-target weights | direction, named sector colors, transparency | Understand matrix semantics, reciprocal duplicates and label length. Opens no device; draws on current device and clears circlize state. | invisible link table + base figure; pp.143-149 |
| `choropleth_plot` | sf geometry with CRS + unique keyed values | explicit unmatched opt-in, midpoint, value units | Data-only keys fail; geometry-only keys require review; all geometry kept with missing fill. Source rgdal replaced with sf explicitly. | list: plot/data/unmatched_geometry/missing_values; pp.149-161 |

## Use Example

```r
source(file.path(skill, "scripts", "figure-tools.R"))
source(file.path(skill, "recipes", "r", "estimates.R"))
p <- estimate_plot(results, "outcome", "estimate", "lower", "upper",
                   interval_label = "95% CI from the fitted mixed model", group = "treatment")
p <- p + ggplot2::labs(y = "Mean difference (mm)", x = NULL)
export_figure(p, file.path(project_output, "effects"), 170, 100)
```

`results`, its interval method and units must actually match the caption. Use `assets/figure-template.R` as a project starter; it is not a self-running analysis without inputs. For R on Windows, use a functioning UTF-8 locale when skill or project paths contain non-ASCII characters; this is an environment concern, not a setting the skill changes globally.

## Adaptation-only Patterns

The source also teaches stacked area, pie/donut/waffle, marginal distributions, ternary/radar, treemap, survival, Venn/UpSet, clustered heatmaps, phylogenetic annotation, and circular tracks. These are preserved as structured recipes in [specialized graphics](specialized-graphics.md), not silently advertised as tested functions. They need appropriate project data/dependencies and execution/visual checks before delivery. No Python copy of every function was manufactured.
