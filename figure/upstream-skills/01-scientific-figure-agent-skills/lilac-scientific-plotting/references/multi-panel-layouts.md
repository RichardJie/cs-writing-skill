# Multi-panel Layouts

Source pp.179-181,189-201: facets, cowplot alignment/nesting/insets/shared legends and patchwork composition.

## Decide The Comparison

- Facet a common grammar when the same variables repeat across groups. Fix scales for magnitude/slope comparisons; if using free scales, disclose the loss of cross-panel absolute comparison (pp.50-51,179-181).
- Compose different grammars when a scientific narrative needs complementary views. A, B, C should have stable reading order and concise captions, not accidental code order.
- Align panel interiors and axis baselines. Identical image sizes alone do not align panels with different tick-label widths (pp.190-193).
- Allocate widths/heights based on content: a narrow distribution sidebar need not be as wide as a trend panel. Keep common text sizes even with unequal panel widths.
- Collect a legend only when variable, units, scale limits, breaks, category order and color mapping are genuinely the same (pp.195-196). Similar colors do not prove compatible legends.
- Insets (pp.193-194) need nonoverlapping placement and a clear purpose; they must not hide outliers or intervals. Use a separate panel when no unused region exists.

Codex implementation note: `compose_panels()` wraps patchwork, preserving individual legends by default. `collect=TRUE` requires `shared_encoding=TRUE` as an explicit caller assertion; the helper cannot infer scientific equivalence. Inspect output because guide sizes and long labels can still crowd a layout. Base graphics need conversion/capture before combining with grid-based ggplots; do not treat any R plot as a grob automatically.
