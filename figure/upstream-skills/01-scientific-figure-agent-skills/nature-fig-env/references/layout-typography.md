# Layout and typography

Read this reference for multi-panel figures, maps, journal export, or any figure that will be downscaled.

## Final-size-first design

Choose the expected assembled width before plotting. Common Nature Portfolio layouts are approximately single-column, one-and-a-half-column, or double-column width; verify the current target journal instructions. Design and inspect at the final millimetre width rather than trusting the large working canvas.

Required final-size typography:

- Axis and colorbar labels: 15–17 pt by default; never below 13 pt [FONT-01].
- Tick labels and legend text: 13–15 pt; never below 13 pt [FONT-01].
- Annotation, map-label, significance, and inset text: at least 13 pt [FONT-01].
- Lines: normally at least 0.8 pt after reduction.
- Markers: remain distinguishable without relying on color alone.

When individual panels will be reduced during assembly, divide the intended final font size by the reduction factor to obtain the minimum working font size. For example, a panel reduced to 70% of its working width needs at least 18.6 pt working text to retain 13 pt after reduction. Larger text is welcome when legible, but it must not cross the canvas boundary [LAYOUT-03]. Never shrink text simply to fit more content; reduce tick density, shorten labels, enlarge the canvas, or revise the layout first.

## Typeface

Use Arial when available, Helvetica second, then Liberation Sans or DejaVu Sans as stable fallbacks. Keep one font family across axes, legends, annotations, and colorbars. Use math text sparingly and keep its visual weight compatible with the surrounding sans-serif type.

## Separate-panel geometry

- Export each intended panel as a separate file. Do not create a combined subplot canvas by default.
- Do not add a, b, c or equivalent panel letters. The user assembles and labels the composite later.
- Use identical canvas and plotting-region sizes for comparable plots so they align cleanly during assembly.
- Reserve shared space for a common legend or colorbar instead of repeating it in every panel.
- Avoid large blank margins. Do not crop labels, coastlines, uncertainty bands, or annotations.
- Keep map projection, extent, coastline resolution, boundaries, and scale consistent across comparable maps.
- Use one shared colorbar for panels with the same variable and normalization.

## Axes and labels

- Use concise variable names and put units in parentheses, for example `Temperature anomaly (°C)` or `Waste heat (PJ yr⁻¹)`.
- Use typographic minus signs and true superscripts where supported.
- Keep labels within the export boundary. Prefer `layout="constrained"`; otherwise adjust margins deliberately and inspect the saved output.
- Reduce tick density before reducing font size.
- Avoid rotated tick labels unless necessary. If rotation is required, align and pad them so they remain inside the canvas.
- Use consistent numeric precision across panels.

## Legends and colorbars

- Export the legend or colorbar as a separate file in the same folder as the figure family.
- Treat the standalone legend as a required publication asset rather than a screenshot or afterthought. Its labels must remain at least 13 pt and inside the canvas at the intended placement size [FONT-01, LAYOUT-03].
- Use one row when entries are few and short; one column for long labels; multiple columns for many short labels. Balance the footprint with the final composite.
- Keep legend order stable across figures and match the visual order of lines, bars, or scenarios where possible.
- For continuous fields, label the colorbar with the quantity and unit. Use a small number of interpretable ticks.
- Do not let a legend or colorbar cover data.

## Background and decoration

- Default to a white background.
- Remove top and right spines for ordinary Cartesian plots unless a boxed frame is scientifically useful.
- Do not use a background grid by default. If a grid is needed, show only major lines with low opacity and thin weight.
- Do not include plot titles. Put the identifying phrase in the filename and scientific explanation in the caption.
- Avoid shadows, 3D effects, glossy gradients, pictograms, and decorative icons that do not encode data.

## Export

- Export both SVG and PDF for vector-compatible charts and labels; raster-only delivery is not acceptable unless the source itself is intrinsically raster and no vector annotations exist.
- Keep SVG text editable with `svg.fonttype = "none"` and PDF text as TrueType with `pdf.fonttype = 42`. Confirm selectability in the exported files.
- Also provide high-resolution PNG or TIFF when required by the journal or assembly software.
- Raster maps should be exported at sufficient resolution for the final physical size; do not upscale low-resolution data and imply added detail.
- Embed or outline fonts only when required by the target workflow, and verify that symbols render correctly.
- Inspect each exported format, because layout and font substitution can differ from the interactive canvas.
- Run `python scripts/audit_source_fonts.py plot.py --minimum-pt 13` before export, `python scripts/audit_vector_text.py figure.svg --minimum-pt 13` (or the equivalent PDF command) on every vector output, and `python scripts/audit_figure.py figure.png figure.figure.json` on every raster output. The source and vector audits enforce actual size [FONT-01]; the raster audit flags content touching the canvas [LAYOUT-03]. Visually inspect each image because automated boundary checks cannot always distinguish text from other marks.
