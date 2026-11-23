---
name: scientific-plotting
description: Design, implement, revise, and quality-check scientific and publication figures, including statistical graphics, multi-panel layouts, annotations, colors, and reproducible exports. Use for research plotting in R/ggplot2 or for applying visual principles in the user's existing plotting language. Not a general dashboard or illustration skill.
---

# Scientific Plotting

Turn a research question into a truthful, readable figure at its final physical size. This skill provides independent plotting guidance informed in part by *SCI论文绘图之道*; it is not a journal's mandatory specification. Retain the user's language and analysis method; executable recipes are R-first, not a reason to migrate a Python project. The book and its PDF are not required for any workflow here.

## Workflow

1. Identify the claim/comparison, observational unit, variable types, units, sample sizes, missingness, and repeated/paired structure. Inspect actual data before selecting a chart. Ask only when missing information changes statistical meaning.
2. Choose the estimand and uncertainty definition, then the chart and encodings. Use [chart selection](references/chart-selection-guide.md) and [statistics](references/statistical-graphics.md) when needed. Never invent CI, pairing, weights, or significance to finish a plot.
3. Choose layout, scale sharing, final dimensions, and text hierarchy before detailed styling. Read [layouts](references/multi-panel-layouts.md) for facets/composites, [style](references/visual-style-guide.md), [colors](references/colors-and-accessibility.md), or [axes/annotations](references/annotations-legends-axes.md) only for relevant decisions.
4. Find a pattern in [recipe catalog](references/recipe-catalog.md). Read that recipe's contract before sourcing its R file. Source `scripts/figure-tools.R` first. Recipes take explicit columns and do not load the source PDF or install packages. For specialized graphics, consult [specialized graphics](references/specialized-graphics.md); distinguish tested implementations from adaptation-only patterns.
5. Render at final size, inspect the image, test data/statistical invariants, revise, then export. Apply [figure QC](references/figure-qc.md) and [export](references/export-publication.md). A successful script is not visual validation. If viewing or execution is unavailable, state what remains unverified.
6. Deliver the figure, reproducible code, key statistical/visual decisions, and limitations. Keep source data unchanged. Write project outputs to the user's project, never into the installed skill.

## Essential Constraints

- Preserve measurements and model meaning. Do not remove valid extremes, move points, replace missing values by zero, or edit branch lengths for appearance.
- Bars encoding magnitude need a meaningful baseline; log scales and free facets need explicit labels. A secondary axis must be a known invertible transformation, not an independently fitted visual match.
- Label what intervals mean, how groups were summarized, and what sample size counts. A paired design needs real IDs. Inferential choices belong to analysis, not decoration.
- Give each color, shape, size, line, and panel a job. Map the same group consistently across panels. Redundant color plus shape can improve accessibility.
- Readability is judged at publication dimensions. Check legends, label collisions, panel alignment, visible uncertainty, units, fonts, and output devices, not only the enlarged preview.

## Provenance And Routing

- [Source index](references/source-index.md): optional provenance map; not needed to apply the skill.
- [Principles](references/plotting-principles.md): source-derived reasoning and visual comparisons.
- [Corrections](references/provenance-and-corrections.md): extraction limitations, source errors, dated APIs, engineering additions. Read before reproducing legacy source code.
- [Anti-patterns](references/anti-patterns.md): audit an existing figure or resolve conflicting rules.
- `assets/figure-brief.md`: reusable decision/QC record, adapt without filling irrelevant fields.
- `assets/figure-template.R`: minimal project script; replace only with real data and explicit choices.

Page citations identify provenance only; they are never instructions to obtain the book. `Source` means a method discussed there; `Derived synthesis` combines examples; `Codex implementation note` is an added guardrail or implementation. Use the guidance and code in this folder, plus current package documentation when an optional package is involved. Do not imply that untested source examples were validated against unavailable original datasets.
