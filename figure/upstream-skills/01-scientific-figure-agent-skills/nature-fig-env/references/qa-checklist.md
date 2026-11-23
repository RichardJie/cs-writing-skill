# Figure QA checklist

Run this audit after rendering the actual saved output. Do not approve a figure from code alone.

## Scientific encoding

- [ ] The plotted quantity, aggregation, baseline, sign convention, and uncertainty are correct.
- [ ] The statistic shown is explicitly named; sample size `n` and its independent observational/experimental unit are recorded.
- [ ] Every error bar, band, whisker, interval, ensemble envelope, or spread mark is defined as SD, SE, CI with level, quantiles, range, or another explicit quantity.
- [ ] Units are present on axes and colorbars or are unambiguous in the caption.
- [ ] Missing, masked, censored, and zero values are visually distinct where relevant.
- [ ] A delta, anomaly, residual, or signed effect uses the scientifically correct neutral centre, normally 0.
- [ ] The palette type matches the data type: sequential, diverging, cyclic, categorical, or binary.
- [ ] No interpolation, smoothing, or clipping creates a misleading pattern.

## Cross-panel consistency

- [ ] Comparable panels use identical axes, color limits, normalization, units, ticks, category colors, and legend order.
- [ ] Map projection, extent, and boundaries are consistent where comparison is intended.
- [ ] Independent autoscaling does not exaggerate differences.
- [ ] Any exception to a shared scale is conspicuous and justified.

## Readability at final size

- [ ] [FONT-01] All essential text is at least 13 pt at the final assembled size.
- [ ] [FONT-01] `scripts/audit_source_fonts.py` passes on the plotting source, and `scripts/audit_vector_text.py` passes on the actual exported SVG or PDF; metadata alone is insufficient.
- [ ] Axis labels, tick labels, annotations, and units are legible.
- [ ] [LAYOUT-03] Every image has been checked individually; x-labels, y-labels, tick labels, annotations, legends, and colorbars remain fully inside the exported canvas even when larger fonts are used.
- [ ] Lines, markers, hatching, and uncertainty bands remain distinguishable.
- [ ] Tick density and numeric precision are appropriate.

## Color and accessibility

- [ ] The palette is perceptually ordered where values are ordered.
- [ ] Essential distinctions remain understandable under common color-vision deficiencies and in greyscale.
- [ ] A rainbow/jet palette is absent.
- [ ] Hazard, benefit, water, vegetation, heat, and infrastructure colors are semantically coherent without overriding data structure.
- [ ] Missing data use an explicit neutral color.

## Layout

- [ ] Every panel is exported separately and has no a/b/c identifier unless the user explicitly requested one.
- [ ] No plot title is present unless explicitly requested.
- [ ] Background grids are absent or demonstrably useful and visually restrained.
- [ ] The legend does not obscure data and is exported separately.
- [ ] The standalone legend uses an appropriate row/column arrangement.
- [ ] Shared colorbars and legends reduce redundancy across panels.
- [ ] There is no clipping, overlap, excessive whitespace, or accidental misalignment.

## Delivery

- [ ] Editable SVG and PDF outputs open correctly; text remains selectable/editable and has not been converted to paths.
- [ ] A high-resolution PNG or TIFF companion opens correctly when required.
- [ ] Fonts and scientific symbols render correctly in exported files.
- [ ] Main figures, legends/colorbars, metadata, and optional contact sheet are in the same clearly named folder.
- [ ] Filenames identify variable, region, scenario, and period where needed without relying on an in-plot title.

Revise and re-export whenever an applicable item fails.
