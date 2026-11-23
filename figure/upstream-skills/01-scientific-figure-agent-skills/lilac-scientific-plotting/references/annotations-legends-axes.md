# Annotations, Legends, Axes

## Annotation

Source pp.117-123: selectively label interesting observations, use ggrepel for placement, mute background points, and make annotation color agree with the highlighted group. Keep original points at their measured coordinates. Label displacement needs a connecting segment when association is unclear. Do not copy the example's manually typed R-squared: compute it from the fitted data/model and identify the model.

## Legends

Source pp.174-179,195-196: adjust guide order, title, key size and position; avoid redundant guides when a direct label is enough. Choose truly unused plot space for an internal guide and inspect for collisions. `guide_legend(override.aes=...)` can make a transparent-point legend readable without changing plotted alpha.

Codex implementation note: a color-and-shape legend is not inherently redundant. It may remain readable in grayscale. Shared legends require common mappings, not only matching aesthetics. Modern ggplot2 supports `legend.position='inside'` plus `legend.position.inside`; numeric `legend.position` is a legacy API.

## Axes

Source pp.184-189: scale limits, breaks, labels, transformations and secondary axes are separate operations. Use readable units and only as many ticks as aid reading.

Codex implementation notes:
- `scale_*_continuous(limits=...)` can remove observations before statistical layers; `coord_cartesian` zooms the viewport without this data deletion. State transformations and visible truncation.
- A bar's length encodes magnitude from its baseline. Avoid a truncated baseline that exaggerates differences. A point-range plot can use a focused domain if the reference and units remain clear.
- A secondary axis must be a known one-to-one transform of the primary scale (e.g. unit conversion), not an independent outcome rescaled until curves match.
- Log axes require positive observations and explicit treatment of zero/negative values; do not silently add a pseudocount.
- Prefer horizontal categories or wrapped labels to unreadably rotated text; retain scientifically meaningful natural order rather than sorting automatically.
