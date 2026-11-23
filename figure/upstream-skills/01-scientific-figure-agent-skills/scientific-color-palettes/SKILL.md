---
name: scientific-color-palettes
description: Choose, apply, audit, or revise color systems for scientific figures, plots, heatmaps, spectra, mechanism diagrams, and multi-panel publication graphics. Use when a user asks for research-figure colors, publication-ready palettes, gradient design, consistent cross-panel color mapping, or color accessibility; do not trigger for general branding or decorative illustration palettes.
---

# Scientific Color Palettes

Build a color system around the scientific meaning of the data. A polished figure is not merely colorful: color direction, lightness, emphasis, legends, and panel-to-panel mappings must remain interpretable and reproducible.

## Route the task

- Read [references/palette-catalog.md](references/palette-catalog.md) when exact HEX values, a named palette, or a ready-to-use color list is needed.
- Read [references/application-guide.md](references/application-guide.md) when designing, revising, or auditing an actual figure. It contains data-type and chart-type rules.
- Use `scripts/palette.py` to list or export exact palettes for Python, R, CSS, JSON, or plain HEX.

## Core workflow

1. Identify the visual variable before selecting hues: unordered categories, ordered conditions, continuous magnitude, signed deviation around a reference, density, uncertainty, or semantic roles in a schematic.
2. Select the palette type that matches that variable:
   - categorical for unordered groups;
   - sequential with monotonic lightness for ordered or one-directional values;
   - diverging with a defensible midpoint for signed effects or deviations;
   - role-based colors for mechanisms, workflows, and annotations.
3. Establish hierarchy. Reserve the strongest/darkest color for the principal result or key annotation; use medium colors for primary series, pale colors for uncertainty bands and broad fills, and charcoal/soft gray for axes, text, grids, and context.
4. Apply one semantic mapping consistently across panels, legends, captions, and related figures. Never change a group's color merely to make one panel look balanced.
5. Validate at final size: inspect color-vision robustness, grayscale separation, thin-line visibility, text contrast, white-background and print behavior, and whether the legend explicitly explains the mapping.
6. Report the chosen palette, direction, midpoint if any, role mapping, and exact HEX values so the figure is reproducible.

## Non-negotiable scientific rules

- Color must encode meaning, not decorate. Do not use a rainbow scale for scalar data or a smooth gradient for nominal groups.
- A sequential scale must change lightness monotonically. A diverging scale must place its neutral color at a meaningful value such as zero, baseline, control, or a stated threshold—not automatically at the numerical midpoint.
- Do not infer positive/negative meaning from arbitrary endpoints. State the direction of every colorbar.
- Keep raw observations visible when they matter. Use lighter fills and darker outlines/points rather than hiding distributions under saturated blocks.
- Use redundant cues when colors may be confused: marker shape, line style, direct labels, hatching, or panel separation. Red–green opposition alone is insufficient.
- Avoid pale colored text and low-opacity thin lines. Use dark charcoal for small text; white text belongs only on demonstrably dark fills.
- Large backgrounds stay white or nearly white. Pastels are support colors, not substitutes for contrast.
- Preserve user-specified semantic conventions and journal requirements. Do not alter data, normalization, statistics, or chart geometry merely to fit a palette.

## Deliverables

For a recommendation, provide a compact mapping such as `Control → #...`, `Treatment → #...`, plus the palette type and rationale. For code edits, define the palette once as a named constant and reuse it across panels. For an audit, identify concrete collisions or hierarchy failures and propose the smallest consistent correction.
