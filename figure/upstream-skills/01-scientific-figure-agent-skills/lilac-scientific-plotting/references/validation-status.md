# Validation Status

Construction validation date: 2026-09-27. Test input: seeded simulated data, not the book's unavailable datasets. The reproducible checks are included at `tests/validate_recipes.R`; run them with a compatible R installation and the listed packages. They do not require the source PDF.

- 18 plotting/composition functions were executed; 23 figure outputs exercise variants including distribution, group violin/box/raw points, ridges, grouped/overall regression, bubbles, density contours, labels, trends, pairing, lollipop/bars, proportions, estimates/CI, heatmap/correlation, multi-panel, logo bits/probability, chord, sf map, and Chinese font export. 56 execution/semantic/guardrail checks passed.
- Tested artifacts: PNG and vector PDF; SVG additionally for the distribution example. `export_figure` saved session metadata and rejected accidental overwrite.
- Semantic tests include unchanged raw values, complete/unique paired IDs, CI bounds and matching dodge coordinates, actual model n/R-squared, correlation agreement, missing matrix cells retained, map join safeguards and preservation of geometry, invalid bubble magnitudes, palette capacity and circlize state cleanup.
- All 23 PNGs were visually inspected via review sheets, with closer inspection of the multi-panel, CI, advanced and CJK examples. All 23 PDFs were reopened and programmatically checked for nonblank content, text within page boundaries and embedded fonts; selected PDF renders were inspected. Chinese labels rendered correctly with the installed Microsoft YaHei family. This does not prove suitability for an unspecified journal or a future dataset.
- R 4.5.0; ggplot2 3.5.2; patchwork 1.3.2; ggseqlogo 0.2.2; circlize 0.4.18; sf 1.0.21; ragg 1.4.0. A new test run writes its own `session-info.txt` to the selected output directory.
- Known warning: ggseqlogo internally uses deprecated `guides(FALSE)`; output succeeded. No warning was hidden. Review upstream compatibility after package upgrades.
- Advanced R packages are optional for normal use but required by the full validation script. Install compatible versions in your own R library or pass a library path to the script; no private construction environment is required.
- All adaptation-only patterns in [specialized graphics](specialized-graphics.md) remain explicitly unexecuted. Statistical-method selection, biological interpretation, real geography, font coverage for new text and venue compliance must be verified for each future task.

Do not claim that every screenshot/code label in the source was reexecuted, that every optional package is installed, or that simulated-data tests validate a user's scientific analysis.
