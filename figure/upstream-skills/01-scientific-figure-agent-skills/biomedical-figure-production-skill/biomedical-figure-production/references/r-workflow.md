# R plotting workflow

## Environment

Use the detected Rscript executable and a project-local library. Run:

```powershell
& 'C:\Program Files\R\R-4.6.1\bin\Rscript.exe' .\scripts\setup_r.R
```

The setup script installs common figure packages into `Documents/Codex/environments/biomedical-figure-production/R-library` unless another library path is supplied.

## Recommended roles

- `ggplot2`: primary grammar of graphics;
- `patchwork` or `cowplot`: deterministic panel assembly;
- `ggrepel`: controlled label placement;
- `ComplexHeatmap`: annotated omics heatmaps;
- `survminer` and `survival`: survival plots and risk tables;
- `forestplot`: forest plots;
- `pROC`: ROC analysis;
- `ragg`, `svglite`, and `tiff`: stable raster/vector export.

## Analysis order

Keep data preparation, statistical modelling, plot construction, and export in distinct functions. Use `set.seed()` for any randomized placement or subsampling. Save `sessionInfo()` and exact plotted values. Do not rely on the active RStudio state.

For survival figures, report the time origin, event code, censoring definition, number at risk, follow-up scale, model assumptions, hazard-ratio confidence interval, and whether the cut-point was prespecified. Avoid data-driven “optimal” cut-points without correction and validation.

