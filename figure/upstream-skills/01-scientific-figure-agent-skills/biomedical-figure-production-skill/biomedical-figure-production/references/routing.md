# Workflow routing

## Choose by evidence source

| Input or objective | Primary route | Secondary checks |
|---|---|---|
| CSV/XLSX, statistical comparison, clinical outcomes | Python or R | Clinical biostatistics review |
| Gene-expression matrix, enrichment, single-cell summary | Python with cnsplots/Scanpy or R/Bioconductor | Denominator, normalization, multiplicity |
| Existing Origin project or journal graph template | Origin workflow | Export and readback QA |
| Mechanism diagram, pathway, study design, graphical abstract | Illustration workflow | Evidence-class legend and disclosure |
| Measured panels plus mechanism cartoon | Hybrid workflow | Separate data and illustration layers |
| Existing PNG/TIFF/SVG/PDF needing audit | Export/audit workflow | Provenance and figure-text consistency |

## Choose Python or R

Prefer Python when the upstream analysis is Python, when Scanpy or cnsplots supplies the required plot, or when programmatic SVG assembly is central. Prefer R when the upstream analysis is R/Bioconductor, when ComplexHeatmap or established ggplot2 extensions are required, or when the source repository is already R-based.

When both are equally suitable and the user needs reusable source code, ask once: “Python or R?” Do not change languages merely for aesthetics.

## Compose multi-panel figures

- Map one claim to one panel.
- Keep panel labels and legend conventions global.
- Use shared axes only when scales and units are genuinely comparable.
- Avoid duplicating the same result in several chart types.
- Put essential interpretation in the legend and manuscript, not as decorative prose inside the plot.

