# Colors And Accessibility

Source pp.32-37,161-170: categorical palettes distinguish classes, sequential palettes order magnitude, diverging palettes distinguish direction around a meaningful midpoint. The book demonstrates ggsci, RColorBrewer, paletteer, manual colors, and grayscale. A publisher-named palette does not itself confer publication quality.

Derived synthesis pp.35-37,118-123,174-179:
- Use one hue family for a magnitude; two ordered branches for meaningful positive/negative contrast; distinct hues for unordered categories.
- Carry the same named category mapping across panels; do not let factor reordering silently remap colors.
- Dark outlines can preserve very pale filled marks, but thick outlines obscure small marks.
- Gray context plus a targeted highlight can be clearer than many saturated categories.
- Put palette choice after the encoding decision. Do not apply a categorical palette to a continuous scale because its colors look attractive.

Codex implementation notes:
- Do not rely on red versus green alone. Supplement group identity with shape, line type, position, or direct labels; inspect grayscale and a color-vision simulation where available.
- The helper provides seven distinct categorical colors as a starting palette and fails rather than silently recycling beyond seven. This is not a formal accessibility certification.
- `scale_fill_viridis_c` is used as an engineering default for unsigned heatmaps/maps; diverging blue-neutral-red is reserved for an explicit midpoint. Check actual contrast at final size, especially labels over fills.
- Do not use a diverging scale centered on the observed mean unless that center has scientific meaning. Missing values need a distinct, documented appearance, not the same color as a true zero.
- A legend with many almost-identical colors is a signal to facet or simplify the representation, not merely enlarge the legend.
