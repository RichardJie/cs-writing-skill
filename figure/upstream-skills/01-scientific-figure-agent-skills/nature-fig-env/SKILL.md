---
name: nature-fig-env
description: Create, revise, standardize, and audit publication-ready environmental and energy figures in a restrained Nature-style visual system. Use for atmospheric science, climate, ocean, air pollution, urban systems, hydrology, ecology, and energy-system plots; apply this style by default for scientific plotting unless the user requests another style.
---

# Nature Fig Env

Create scientifically meaningful figures whose color, scale, typography, and layout remain legible after multi-panel assembly. Treat visual choices as part of the scientific argument, not decoration.

## Default activation

For scientific plotting tasks, use this visual system by default when the user does not specify another journal, template, palette, or house style. Preserve explicit user and journal requirements whenever they differ from these defaults. Do not restyle non-scientific graphics merely because this skill is available.

## Required workflow

1. Identify the scientific variable, sign convention, units, comparison groups, uncertainty, spatial or temporal structure, and intended final panel size. Before plotting, explicitly record the statistic shown, sample size `n` and its unit of independence, and the error-bar or uncertainty definition; use `not applicable` only when the figure genuinely contains none.
2. If `assets/reference-images/` contains user examples, run `scripts/make_reference_contact_sheet.py` and inspect the contact sheet. Extract reusable traits such as type hierarchy, spacing, line weights, legend placement, and palette logic. Do not copy data, labels, logos, or distinctive artwork.
3. Select colors by data semantics and statistical structure. Read [references/palette-system.md](references/palette-system.md) whenever choosing or revising a palette.
4. Set typography and geometry for the final assembled size, not only the standalone panel. Enforce a 13 pt minimum for every essential text element after assembly [FONT-01]. Read [references/layout-typography.md](references/layout-typography.md) for panel sets, maps, or journal export.
5. Draw the data before annotations. Keep the plot free of titles and unnecessary background grids. Put the descriptive title in the filename or manuscript caption.
6. Export an editable SVG and PDF for every compatible figure, plus the requested raster format. Keep SVG text as `<text>` and PDF text as TrueType by enforcing `svg.fonttype = none` and `pdf.fonttype = 42`. Export the standalone legend or colorbar in editable vector form too. Use `scripts/figure_style.py` where useful.
7. Run `scripts/audit_source_fonts.py` on the plotting source, inspect every rendered image at final publication size, run `scripts/audit_vector_text.py` on every exported SVG or PDF to measure rendered font commands, and run `scripts/audit_figure.py` on every raster output to detect content touching the canvas [LAYOUT-03]. Then complete [references/qa-checklist.md](references/qa-checklist.md). Revise until every applicable check passes. Use the stable identifiers in [references/rule-registry.md](references/rule-registry.md) when reporting failures.

## Non-negotiable defaults

- [FONT-01] Use a clean sans-serif typeface: Arial first, Helvetica second, then a metrically stable sans-serif fallback. No essential text may be smaller than 13 pt at the final assembled size. This minimum applies to axis labels, tick labels, legends, colorbar labels and ticks, map labels, annotations, significance marks, and inset labels.
- [FONT-01, LAYOUT-03] Use 15–17 pt axis and colorbar labels and 13–15 pt ticks, legends, and annotations at final size by default. Larger text is allowed when it improves readability, but it must remain fully inside the canvas without crowding, overlap, or clipping. Increase working font sizes in proportion to planned downscaling; never solve crowding by reducing essential text below 13 pt.
- Do not add a plot title unless the user or journal explicitly requires it.
- Export every scientific panel as its own figure file by default. Do not assemble panels and do not add panel identifiers such as a, b, c, `(a)`, or `A`. The user will assemble and label the final composite. Only add panel identifiers when explicitly requested.
- Keep x-axis labels, y-axis labels, tick labels, annotations, legends, and colorbars inside the exported canvas. Use constrained layout or explicit margin control and verify the saved file.
- Avoid background gridlines by default. If a grid materially aids quantitative reading, use thin, low-contrast major gridlines only.
- Never use a rainbow or jet palette for ordered scientific data.
- Use perceptually uniform, color-vision-deficiency-aware palettes. Do not encode an essential distinction by hue alone when line style, marker, hatching, or direct labels can add redundancy.
- For signed anomalies, differences, changes, residuals, flux divergence, or effects with a meaningful neutral value, use a diverging palette centred exactly at 0 by default. Use an asymmetric centre only when the scientific neutral value is not 0 and state it explicitly.
- For panels or files that show the same variable or comparison, keep identical colorbar limits, normalization, units, tick locations, category colors, and legend order unless the shared range makes the data genuinely unreadable. Document any exception.
- Match semantic colors to the subject without overriding perceptual accuracy: vegetation and beneficial environmental states generally use green or blue-green; water and ocean variables use blue-family palettes; heat, exposure, hazard, damage, emissions, or risk may use orange, red, magenta, or purple; neutral infrastructure uses greys. Avoid simplistic red-versus-green contrasts.
- [LEGEND-01, FONT-01, LAYOUT-03] Export legends separately as first-class figure assets. Choose one row, one column, or a multi-row/multi-column arrangement according to the number and label length of entries and the dimensions of the final composite. Keep standalone legend text at least 13 pt and fully inside its canvas at the intended final size.
- Every colorbar must state the variable or quantity and unit, either on the bar or unambiguously in the adjacent caption. A bare color scale is incomplete.
- State the plotted statistic, sample size `n`, experimental or observational unit represented by `n`, and uncertainty/error-bar definition in metadata and the caption or legend. Never let readers infer whether bars show SD, SE, CI, quantiles, ensemble range, or another quantity.
- Editable vector output is mandatory whenever the figure consists of vector-compatible marks and text. Do not deliver PNG/TIFF alone. Raster-only source imagery may remain rasterized inside an SVG/PDF container, but labels, axes and annotations must remain editable text.

## Comparison and scale policy

Before plotting, group outputs into comparison families. A family is a set of panels or files that a reader will compare directly.

- Compute shared axis and color limits from the whole family, preferably using scientifically defensible fixed limits or robust pooled quantiles.
- Preserve the same category-to-color mapping across all members of a family.
- Use consistent significant figures and units.
- Show uncertainty consistently, for example confidence bands, intervals, ensemble spread, or distribution marks. Define it in the caption or legend.
- Do not use independent autoscaling that exaggerates small differences across panels.

## Output contract

For each figure family, save:

- Main figure(s): one file per panel, using identical dimensions for comparable panels; vector PDF/SVG when possible, plus PNG/TIFF at the required resolution.
- `legend_<family>.*` or `colorbar_<family>.*` as a separate file in the same folder.
- A short metadata sidecar such as `<family>.figure.json` when the workflow is scripted. Record variable, units, statistic, sample size `n`, unit of independence, uncertainty/error-bar definition, palette, normalization, limits, final width, final font size, and comparison-family name.
- Optional contact sheet when user examples were consulted.

Use transparent backgrounds only when the downstream assembly requires them. Otherwise use white.

## Tools supplied

- `scripts/figure_style.py`: Nature-oriented Matplotlib defaults, semantic palette selection, shared limits, zero-centred normalization, standalone legend export, and metadata writing.
- `scripts/audit_figure.py`: deterministic audit of a figure metadata sidecar and raster geometry.
- `scripts/audit_source_fonts.py`: inspect explicit font declarations in Python plotting source and fail below 13 pt.
- `scripts/audit_vector_text.py`: inspect exported SVG/PDF text commands and fail when actual text falls below the required final-size threshold or SVG text has been converted to paths.
- `scripts/make_reference_contact_sheet.py`: creates a labelled contact sheet from user-provided reference images.

These helpers support judgment; they do not replace visual inspection.

## Final visual audit

After export, inspect the actual saved files and answer all applicable questions:

- Does every colorbar include a quantity and unit?
- Is a signed delta or anomaly centred at 0?
- Do directly comparable panels share the same scale and color range?
- Is each panel a separate file with no a/b/c identifier unless explicitly requested?
- Is every essential text element at least 13 pt and comfortably legible at final assembled size [FONT-01]?
- Are all labels fully inside the canvas, including when a larger font is used [LAYOUT-03]?
- Does the legend obscure data or consume disproportionate space?
- Is the palette perceptually ordered and color-blind friendly?
- Is any rainbow palette, unnecessary grid, title, decoration, or redundant annotation present?
- Are uncertainty and missing data represented honestly?

If any answer is unsatisfactory, revise and re-export before delivery.
