# Visual Style Guide

Derived synthesis from pp.26-37,117-123,170-184,189-205.

- Hierarchy: focal data first, supporting data second, guides third. Use a restrained context color with one intentional highlight before assigning every observation a distinct color.
- Typography: explicit axis units, concise legend titles, consistent panel tags. Judge text at actual millimeters, not zoomed screen size. The helper's 9 pt base is a starting point, not a journal rule.
- Lines/marks: point outlines must remain thinner than the marks; interval lines must be visible without competing with estimates. Draw connection lines before points (p.49). Use `linewidth` for modern line geoms, `size` for points.
- Background/grid: p.173 shows that light reference lines can help bar comparisons. Keep only useful directions and ticks; a blank background is not automatically more truthful or readable.
- Whitespace: leave enough room for long labels and a legend, but avoid shrinking data into a tiny center. Change orientation/layout before reducing all text sizes.
- Aspect: preserve spatial proportions with `coord_sf`; use equal cells for a matrix when geometry is meaningful. Time-trend aspect affects apparent slope, so compare panels using deliberate shared scales/aspects.
- Density/alpha: use overlap to motivate alpha or aggregation. Alpha=0 is transparent, 1 opaque. Pale points on white need sufficient contrast or outlines.
- Scale consistency: same categories retain the same named colors and order across figures. Fixed facet scales support absolute comparisons; free scales support within-panel shapes only.

Codex implementation note: `theme_scientific()` is deliberately local (no `theme_set`). It removes minor grids and uses bottom legends, but callers should retain or remove major grids according to the chart. Do not make every chart identical regardless of purpose. Physical size and publisher requirements override default parameter values.
