# Statistical Graphics

## Source Patterns

- Distributions: histogram, density, box and violin (pp.21-25). A distribution summary is not a confidence interval. KDE requires enough observations and a declared smoothing choice.
- Regression: group-wise versus overall fits and smooth families (pp.58-60). A colored grouping aesthetic changes which data feed the model. Choose the scientific model first, then draw it.
- Survival: step curves, confidence regions and risk table (pp.60-63). Report event coding, censoring, time unit and groups.
- Estimates with intervals: use matched position adjustments for marks and intervals (pp.106-109). Dot/line/column geoms may represent the same estimates; choose the one that makes the relevant comparison easiest.
- Tests on plots: bracket/annotation tools and paired workflows (pp.123-130). A plotting package does not establish that the test's assumptions hold.

## Added Statistical Guardrails

Codex implementation notes, not claims that the PDF teaches these rigorously:

1. State the observational unit and effective n. Technical replicates, repeated times and nested units are not automatically independent observations. Do not use a naive independent t interval for clustered data.
2. Label intervals as SD, SE, CI, prediction interval or other defined quantity; include confidence level and method. Plotting precomputed bounds must not silently recalculate them.
3. A pointwise fitted-mean ribbon is not a prediction interval or simultaneous confidence band. The supplied `scatter_fit` uses OLS with pointwise mean CI and returns fitted models for inspection.
4. Preserve pair IDs. Report excluded incomplete pairs and reasons. The paired recipe fails on incomplete/duplicated pairs rather than inventing them.
5. Document correlation method and missing-data handling. Pairwise deletion changes n between cells and may produce a non-positive-semidefinite matrix. The recipe instead requires complete finite input; preprocessing is explicit.
6. Report effect sizes and uncertainty when scientifically relevant; do not add stars purely to make a plot look like a paper. Multiplicity and paired versus independent tests need analysis decisions.
7. Density integrates to one per group; different group sample sizes do not make comparable density peaks into frequency counts. Histogram overlays must use the same y quantity.
8. Number at risk is event-free and not yet censored immediately before the time of interest, not a generic live/dead count. Do not extrapolate survival beyond observed support.
9. Bars of means can hide outliers, multimodality and sample-size imbalance. Consider raw points/box/violin or estimates with intervals according to the question, not a blanket ban on bars.

See `recipes/r/estimates.R` for precomputed-interval rendering. It requires an interval label and validates bounds; inference remains the caller's responsibility.
