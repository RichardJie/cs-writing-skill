# Export And Publication

Source pp.201-205: export directly from code, specify figure dimensions, distinguish vector from raster, and use suitable devices/fonts. The book discusses ggplot export and Cairo; it is not a current journal specification.

Codex implementation workflow:
1. Obtain target width/height, permitted formats, font requirements and raster resolution from the actual venue if publication compliance is requested. Otherwise state provisional dimensions. No universal DPI makes every journal compliant.
2. Render at those dimensions. Raster pixels = mm / 25.4 * DPI; DPI metadata alone cannot restore lost detail. Inspect both fit-to-page and actual-size readability.
3. Prefer vector PDF/SVG for line/text graphics when accepted, PNG/TIFF for raster requirements. A vector container may include raster layers. Maps and dense point clouds may make enormous vector files.
4. Use explicit font family and a device that supports it. Test Chinese text with an installed appropriate font; the default generic sans is not a promise of CJK coverage. Inspect glyphs and font embedding/substitution in the exported file.
5. Save data transformation and plotting code, seed when stochastic, dimensions/device, and session/package versions. Keep a caption with estimand, units, interval method, n and exclusions.
6. Reopen the exported artifact, not only the interactive plot. Check clipping, transparent backgrounds, missing glyphs, line visibility and panel tags. Avoid post-export cosmetic editing that breaks reproducibility.

`export_figure(plot, stem, width_mm, height_mm, formats, dpi)` supports PNG using ragg, PDF using cairo_pdf, and SVG using svglite. It rejects existing output files unless `overwrite=TRUE` and writes a metadata sidecar. It does not install fonts, certify journal rules, or verify embedding automatically. Circular base-graphics recipes use explicit devices in the calling script and must receive the same QC.
