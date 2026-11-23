# nature-fig-env

English | [简体中文](README.zh-CN.md)

> Clear, restrained, publication-ready figures for environmental, climate, and energy research.

`nature-fig-env` turns plotting instructions into an auditable publication workflow for atmospheric, environmental, Earth-system, geographical, and energy research. It helps research teams produce consistent figures that remain readable after multi-panel assembly and are easier to revise, review, and reuse.

It does more than apply a color palette. The skill connects data semantics, normalization, typography, layout, editable export, and rule-based quality assurance in one reusable workflow. Every automated finding carries a stable rule ID, making figure QA reproducible rather than subjective.

## What it helps you do

- Select cmocean, ColorBrewer, or viridis-family palettes from the physical meaning and statistical structure of the variable.
- Center anomalies, differences, and signed changes on a scientifically meaningful neutral value, normally zero.
- Keep axis ranges, color limits, units, category colors, and legend order consistent across directly comparable figures.
- Enforce a hard 13 pt minimum for every essential text element at final assembled size, including ticks, legends, colorbars, map labels, and annotations.
- Export one panel per file without automatically adding `a`, `b`, or `c` labels.
- **Export legends and colorbars as separate, publication-ready files** for flexible manuscript assembly.
- Produce vector PDF/SVG and high-resolution PNG/TIFF outputs when appropriate.
- Audit font sizes at three layers—plotting source, metadata, and exported SVG/PDF—alongside raster geometry, color normalization, and legend or colorbar completeness.
- Explicitly record the plotted statistic, sample size `n`, unit of independence, and the definition of every error bar or uncertainty band.
- Require editable SVG/PDF output and audit the text sizes found in the exported vector file itself.

## Example gallery

All gallery figures below use deterministic synthetic demonstration data. They illustrate the visual workflow and must not be interpreted as observations.

<table>
  <tr>
    <td width="50%"><img src="examples/gallery/global-climate-region-types.png" alt="Synthetic global climate-region map"></td>
    <td width="50%"><img src="examples/gallery/global-annual-precipitation.png" alt="Synthetic global annual precipitation map"></td>
  </tr>
  <tr>
    <td align="center"><em>Global climate-region types</em></td>
    <td align="center"><em>Global annual precipitation</em></td>
  </tr>
  <tr>
    <td width="50%"><img src="examples/gallery/atmospheric-temperature-anomaly.png" alt="Synthetic atmospheric temperature anomaly field"></td>
    <td width="50%"><img src="examples/gallery/pm25-urban-rural-gradient.png" alt="Synthetic PM2.5 urban-rural gradient"></td>
  </tr>
  <tr>
    <td align="center"><em>Atmospheric temperature anomaly</em></td>
    <td align="center"><em>PM2.5 urban-rural gradient</em></td>
  </tr>
</table>

## Default behavior

When a task involves scientific plotting and no other journal, template, palette, or house style is specified, Codex should use `nature-fig-env` as the default visual system. Explicit user instructions and journal requirements always take precedence.

## Typography standard

Small text is one of the most common reasons an otherwise strong scientific figure fails after manuscript assembly. This skill therefore uses a stricter final-size standard:

- no essential text below 13 pt;
- 15–17 pt axis and colorbar labels by default;
- 13–15 pt tick labels, legend text, annotations, map labels, and inset labels;
- proportionally larger working fonts whenever a panel will be reduced during assembly.

Larger text is allowed when it improves readability, but every exported image is checked individually to ensure labels remain inside the canvas. The skill reduces tick density, shortens labels, enlarges the canvas, or revises the layout before allowing essential text to fall below 13 pt.

## Standalone legends are a primary output

Legends are exported separately rather than embedded over the data or cropped from a screenshot. A standalone legend can be placed consistently during final assembly, shared across comparison panels, and resized without altering the plotted data region.

Each standalone legend should:

- use at least 13 pt text at its intended final size and keep all text inside the legend canvas;
- preserve category colors, line styles, markers, and ordering used in the main figure;
- use a balanced one-row, one-column, or multi-column layout based on label length;
- remain readable on a transparent or white background;
- be saved beside the corresponding main figure with a name such as `legend_<family>.png` or `legend_<family>.pdf`.

## Install with Codex

The easiest option is to give Codex this instruction:

```text
Install the nature-fig-env skill from https://github.com/haohuresearch/nature-fig-env.git into my Codex skills directory. Validate the installed skill and tell me when it will be available.
```

After installation, restart or refresh Codex. The skill can then be invoked explicitly with `$nature-fig-env` or selected automatically for relevant scientific-figure tasks.

## Manual installation

### macOS or Linux

```bash
git clone https://github.com/haohuresearch/nature-fig-env.git ~/.codex/skills/nature-fig-env
python -m pip install -r ~/.codex/skills/nature-fig-env/requirements.txt
```

### Windows PowerShell

```powershell
git clone https://github.com/haohuresearch/nature-fig-env.git "$env:USERPROFILE\.codex\skills\nature-fig-env"
python -m pip install -r "$env:USERPROFILE\.codex\skills\nature-fig-env\requirements.txt"
```

## Prompts to try

```text
$nature-fig-env Create a global PM2.5 concentration map with a perceptually uniform sequential palette and export the colorbar separately.
```

```text
$nature-fig-env Plot historical and future climate scenarios as separate, directly comparable panels with shared color limits.
```

```text
$nature-fig-env Audit this figure for typography, palette choice, legend placement, clipping, and readability at final publication size, then revise and re-export it.
```

```text
$nature-fig-env Create a zero-centered temperature-anomaly map using a symmetric diverging scale and provide PNG, PDF, colorbar, and metadata outputs.
```

## Core visual principles

- Use perceptually uniform sequential palettes for absolute quantities.
- Use diverging palettes with a meaningful midpoint for anomalies and signed changes.
- Never use rainbow, jet, or similar non-perceptually-uniform palettes for ordered scientific data.
- Keep scales, units, category colors, and legend order consistent across comparison families.
- Use a white background, restrained boundaries, and minimal decoration by default.
- Avoid in-plot titles unless they are explicitly required.
- Keep every essential text element at least 13 pt at final assembled size; larger text must not cross the canvas boundary.
- Inspect the saved output rather than approving a figure from code alone.

## Personal reference library

Place reference figures that you are permitted to store and use in `assets/reference-images/`. The skill can generate a contact sheet and extract general traits such as type hierarchy, whitespace, line weight, palette logic, map framing, and legend placement.

It must not copy source data, labels, logos, or distinctive artwork from a reference image.

```bash
python scripts/make_reference_contact_sheet.py assets/reference-images work/reference-contact-sheet.jpg
```

## Included tools

- `scripts/figure_style.py`: Matplotlib defaults, semantic palette selection, pooled limits, zero-centered normalization, standalone legend export, and metadata writing.
- `scripts/audit_figure.py`: deterministic checks for raster geometry, metadata fields, font-size thresholds, color normalization, and legend or colorbar availability.
- `scripts/audit_source_fonts.py`: source-level checks for explicit Python font declarations below the 13 pt floor.
- `scripts/audit_vector_text.py`: checks actual SVG/PDF text-size commands and detects SVG exports whose labels were converted to paths.
- `scripts/make_reference_contact_sheet.py`: labeled contact-sheet generation for a local reference library.
- `references/palette-system.md`: palette classification and domain-semantic color guidance.
- `references/layout-typography.md`: final-size typography, panel geometry, and export guidance.
- `references/qa-checklist.md`: scientific, visual, accessibility, and delivery checks.
- `references/rule-registry.md`: stable rule IDs for machine-readable and human-readable QA reports.

Run the deterministic audit with:

```bash
python scripts/audit_figure.py figure.png figure.figure.json
python scripts/audit_source_fonts.py plot.py --minimum-pt 13
python scripts/audit_vector_text.py figure.svg --minimum-pt 13
python scripts/audit_figure.py colorbar_family.png figure.figure.json --asset-role legend
```

## Output contract

For each figure family, the skill normally produces:

- one independent file per panel;
- a vector PDF or SVG when compatible with the visualization;
- a high-resolution PNG or TIFF;
- a publication-ready standalone `legend_<family>.*` or `colorbar_<family>.*` file with text no smaller than 13 pt;
- a `<family>.figure.json` metadata sidecar;
- an optional contact sheet when reference images are consulted.

## Palette sources

This repository links to, but does not redistribute, third-party palette libraries. Consult their upstream documentation and licenses:

- [cmocean](https://matplotlib.org/cmocean/)
- [NASA GISS Panoply colorbars](https://www.giss.nasa.gov/tools/panoply/colorbars/)
- [ColorBrewer](https://colorbrewer2.org/)
- [viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)
- [Scientific Colour Maps by Fabio Crameri](https://www.fabiocrameri.ch/colourmaps/)
- [NCAR/NCL color tables](https://www.ncl.ucar.edu/Document/Graphics/color_tables.shtml)
- [Unidata MetPy colortables](https://unidata.github.io/MetPy/latest/api/generated/metpy.plots.ctables.html)
- [Generic Mapping Tools CPTs](https://docs.generic-mapping-tools.org/latest/cookbook/cpts.html)

## License

Released under the MIT License. See [LICENSE](LICENSE).
