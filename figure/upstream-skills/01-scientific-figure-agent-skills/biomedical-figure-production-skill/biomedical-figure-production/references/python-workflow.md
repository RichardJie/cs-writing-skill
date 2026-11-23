# Python plotting workflow

## Environment

Use a project-specific virtual environment. The tested stack is recorded in the repository lock file and includes Matplotlib, Seaborn, SciPy, Plotnine, cnsplots, pandas, NumPy, lifelines, Scanpy, gseapy, and PyComplexHeatmap.

Run:

```powershell
.\scripts\setup_python.ps1
```

or point the script to an explicit Python executable and environment root.

## Analysis order

1. Load immutable input data and validate identifiers, units, missingness, and duplicate samples.
2. Create an analysis table with explicit transformations.
3. Compute estimates, uncertainty, and tests separately from plotting code.
4. Store exact plotted values in a machine-readable table.
5. Render with explicit physical size, fonts, color palette, axis limits, and random seed where jitter or sampling occurs.
6. Export vector and raster variants from the same figure object.

## Plotting rules

- Do not use a bar chart to hide a small distribution when points, boxplots, or interval plots are feasible.
- Do not imply paired analysis unless patient/sample pairing is verified.
- Use log axes only with clear base, zero handling, and back-transform interpretation.
- Label adjusted P values as adjusted and name the correction method.
- Preserve category order explicitly.
- Keep legends and annotations out of the data region when they obscure observations.

Use cnsplots for supported high-level chart types, but verify input mapping and statistical annotations against the underlying data before accepting defaults.

