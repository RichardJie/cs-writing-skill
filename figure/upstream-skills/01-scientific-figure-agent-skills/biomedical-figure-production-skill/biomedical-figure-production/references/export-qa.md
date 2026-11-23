# Export and visual QA

## Before export

- Obtain the journal's current figure instructions.
- Set physical dimensions before tuning fonts and stroke widths.
- Confirm panel order, labels, units, abbreviations, and citations.
- Use embedded or outlined fonts only as the journal permits.
- Test color-vision accessibility and grayscale interpretation.

## Recommended defaults

These are fallback values, not substitutes for journal instructions:

- continuous-tone raster: TIFF, 300 ppi;
- line art: TIFF, 600–1200 ppi;
- mixed line/continuous content: TIFF, 600 ppi;
- editable master: SVG or PDF;
- review preview: PNG, 150–300 ppi;
- RGB for online-only workflows unless CMYK is explicitly required.

Avoid JPEG for plots, line art, and repeated revision cycles.

## Readback checks

1. Reopen each exported file, not only the source canvas.
2. Inspect at full page for hierarchy and at 100% for text, symbols, and artifacts.
3. Confirm TIFF dimensions, DPI metadata, compression, and color mode.
4. Confirm SVG/PDF text and strokes survived export.
5. Check that rasterization did not remove transparency, thin lines, Greek characters, or superscripts.
6. Run `scripts/validate_figure.py` and review warnings manually.
7. Compute a SHA-256 manifest for the final package.

Automated validation cannot establish scientific correctness. It supplements visual and source-data review.

