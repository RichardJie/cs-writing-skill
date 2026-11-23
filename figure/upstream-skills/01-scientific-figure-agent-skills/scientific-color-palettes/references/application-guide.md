# Applying color to scientific figures

## Start from data semantics

| Data meaning | Correct color structure | Key decision |
|---|---|---|
| Unordered groups | Categorical | Maximize separability; do not imply rank |
| Ordered treatments/time/temperature | Sequential | Make lightness monotonic and state direction |
| Continuous nonnegative magnitude | Sequential colorbar | High and low must be immediately legible |
| Signed effect/deviation | Diverging colorbar | Put neutral at zero/baseline/control |
| Density | Usually sequential | Darker/more saturated should consistently mean more |
| Network polarity/correlation | Diverging or two semantic hues | Encode sign with hue and strength with lightness/width |
| Mechanism/workflow roles | Role-based | Reuse the same role color in every node/panel |

## Hierarchy recipe

Use color roles rather than giving every object equal intensity:

- Background/canvas: white or near-white; colored panels only when the tint carries grouping meaning.
- Axes and labels: charcoal, typically `#333333`–`#4D4D4D`.
- Gridlines/reference structure: light neutral gray, visually behind the data.
- Primary data: medium-to-dark chroma with clear contrast.
- Secondary/context data: lower saturation, lighter tone, or thinner stroke.
- Uncertainty/fitted components: pale fill, transparent band, or light companion color; keep the observed trace darker.
- Key finding/annotation: one reserved accent. Repeating accents everywhere destroys emphasis.

## Chart-specific patterns

### Lines, spectra, and time series

- Ordered experimental conditions should progress through one sequence in the same direction as the legend.
- Give thin curves enough darkness; pale steps can become fills, thicker strokes, or dashed/context lines.
- In peak fitting, keep the experimental trace charcoal, the total fit a distinct dark accent, and components as translucent/pale fills. This separates evidence, model, and decomposition.
- When curves overlap, add line styles, markers, direct labels, or small multiples; hue alone is fragile.

### Scatter and density

- For categories, use discrete colors and repeat them in outlines/centroids/labels.
- For continuous density, use a monotonic sequential scale. Use a diverging scale only if the quantity is truly signed around a reference.
- Plot raw points with moderate transparency but keep representative statistics or fit lines darker.
- Bubble size, hue, and lightness must not redundantly suggest conflicting rankings.

### Bars, boxes, and violins

- Use medium fills with dark outlines/error bars. Error bars and statistical brackets should usually be charcoal, not a new data color.
- Keep the same group mapping across bar, box, violin, and raw-point layers.
- Avoid adjacent near-identical tints for unordered groups. If more than 6–8 groups are present, consider faceting or redundant markers rather than expanding the rainbow.

### Heatmaps and matrices

- Sequential quantities: use one hue family with monotonic lightness.
- Correlations, z-scores, residuals, or changes: use a diverging scale centered at the scientifically meaningful neutral value.
- Show the colorbar with units, endpoints, midpoint, and direction. Use a distinct missing-data color rather than the numeric midpoint.
- Do not discretize a continuous map merely for decoration; discretize only when thresholds or bins are scientifically meaningful.

### Stacked areas and stacked bars

- Maintain identical bottom-to-top ordering and legend ordering.
- Prefer neighboring tones only when categories are ordered; otherwise select more separated hues.
- Thin separators or direct labels help when pale layers touch.

### Correlation networks

- Map sign to two opposing hues, magnitude to saturation/width, and statistical status to opacity or line style.
- Keep node-group colors separate from edge-meaning colors. Avoid using the same hue to mean both cluster identity and correlation sign.

### Mechanisms, workflows, and material schematics

- Use pale tints for large objects and darker companions for boundaries, arrows, active sites, and labels.
- Assign stable semantic roles: material A/B, electron/hole, reactant/product, pore classes, or process stages.
- Black/charcoal arrows are safest for causal flow. Use colored arrows only when arrow color itself has defined meaning.
- Reserve the darkest endpoint for the key pathway, active phase, or final conclusion.

## Multi-panel consistency

- Create one figure-level palette dictionary before styling individual panels.
- A treatment, phase, species, or mechanism retains its color everywhere.
- Use local variations of saturation/opacity for layer type, not a new hue for each geometry.
- Align legend order with reading order and data order. Prefer a shared legend for repeated mappings.
- If a panel requires a different color meaning, make the difference explicit with a separate legend/colorbar and visual separation.

## Accessibility and production checks

1. Simulate common color-vision deficiencies when tooling permits. Pink–green and red–green comparisons need redundant cues.
2. View the figure in grayscale. Important series, endpoints, and annotations must remain separable by lightness, line style, marker, or labels.
3. Inspect at final publication size. Thin pale lines and small colored text that look fine when enlarged often disappear.
4. Check both screen and white-paper output. Keep backgrounds white and use transparency cautiously because compositing changes apparent color.
5. Prefer perceptual color interpolation (Lab/OKLab or a trusted scientific colormap) when generating intermediate steps. Do not invent many RGB-interpolated stops across unrelated hues.
6. Record exact HEX values, direction, alpha, and semantic mapping in code or the figure specification.

## Audit questions

- Does every color have one stable meaning?
- Is the palette type appropriate for the data type?
- Is lightness ordered where the data are ordered?
- Is the diverging midpoint scientifically justified?
- Can the main claim be found before reading the legend?
- Are raw data, fitted data, uncertainty, and annotations distinguishable?
- Does the figure survive grayscale and color-vision checks?
- Are all mappings reproducible from exact values?
