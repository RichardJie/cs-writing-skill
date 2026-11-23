# Three checks

1. **Grayscale.** Convert the chart to grayscale (any image editor, or the grayscale filter in a browser print preview). If two slices look the same, change the lighter one.
2. **Color-blind simulation.** Chrome DevTools, Rendering panel, "Emulate vision deficiencies" shows protanopia, deuteranopia and tritanopia. Look for pairs that merge.
3. **Contrast.** White text needs a slice darker than about #767676 to reach 4.5 to 1; near-black text works on light slices. Check with any WCAG contrast checker.

If a check fails, change lightness first, hue second.
