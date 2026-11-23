# Palette catalog

These palettes were distilled from the user's 12 reference images. HEX values are transcribed from the source sheets. Treat the names below as stable identifiers for reproducible use.

## Quick chooser

| Need | Preferred palette | Character |
|---|---|---|
| Broad 5–8 group comparison | `balanced-8` | Balanced blue/green/warm set with charcoal |
| Soft 5–7 group comparison | `coral-teal-violet-8` | Muted, modern, good for distributions and networks |
| Strong two-sided contrast | `orange-blue-6` | Clear warm–cool opposition |
| Soft biological/material schematic | `green-pink-8` | Natural, gentle, role-oriented |
| Molecular/charge-transfer schematic | `blue-pink-8` | Cool, clean, strong navy endpoint |
| Ordered warm conditions | `orange-5` or `amber-5` | Dark-to-light warm sequence |
| Ordered cool conditions | `aqua-5`, `muted-teal-5`, or `blue-5` | Dark-to-light cool sequence |
| Diverging values around zero | `blue-yellow-orange-7` | Blue → light neutral → orange; label the midpoint |

## Exact palettes

### balanced-8

General-purpose categorical palette, especially when warm and cool groups coexist.

`#2C6E7E`, `#1FAE9D`, `#7BC48F`, `#F2C14E`, `#F28E2B`, `#E4572E`, `#E63946`, `#4D4D4D`

Suggested roles: deep teal primary; cyan-green and green supporting groups; yellow/orange/coral/red contrasting groups; charcoal reference/control. Avoid using all warm endpoints for adjacent thin lines without marker or line-style redundancy.

### blue-yellow-orange-7

Muted cool-to-warm palette suited to ordered groups or a diverging scale when the pale yellow region is assigned to a stated reference.

`#497AB7`, `#7EB6D5`, `#BDE2ED`, `#F0FAD9`, `#FEEAA1`, `#FCB567`, `#F27144`

The center is light and low-emphasis. For a true diverging map, anchor the center at zero/control and show endpoint labels. For unordered categories, select separated positions rather than neighboring tints.

### coral-teal-violet-8

Muted categorical/diverging family for correlations, clustered scatter, networks, violins, and grouped bars.

`#E76F51`, `#F4A582`, `#CFE8E6`, `#7BC7C4`, `#4DAAA7`, `#6C5B95`, `#D9D9D9`, `#333333`

Suggested roles: coral for positive/highlight, teal for negative/secondary, violet for a distinct third state, light gray for inactive/context, charcoal for text/experimental traces.

### orange-blue-6

Compact warm–cool system with pale support tones.

`#F26A1D`, `#F7B891`, `#FFF3E6`, `#DCE6F2`, `#6EA6D6`, `#1E5FA8`

Suggested roles: orange primary contrast/high density; peach secondary warm; pale cream and pale blue backgrounds/support; medium blue secondary series; deep blue principal cool series or dark accent.

### orange-5

`#EA5514`, `#EB6821`, `#EC7A2E`, `#ED8B3C`, `#EE9C4B`

Narrow warm sequence. Its lightness span is modest, so use it mainly for lines/markers with adequate thickness; add line styles for grayscale or dense overlays.

### amber-5

`#F7A049`, `#F9BD6F`, `#FBD18B`, `#FDE4AF`, `#FEF2D6`

Light warm sequence for fills, uncertainty regions, stacked areas, or secondary ordered series. Reverse it when higher values must be darker. The palest two tones need dark outlines on white.

### aqua-5

`#22B5AF`, `#3FC4BF`, `#63D1D0`, `#95E6E8`, `#BFFEF8`

Fresh cyan sequence for ordered conditions and cool fills. Reverse it for the conventional low-light/high-dark direction. Do not use the palest tone for thin lines.

### blue-gray-5

`#E3F8F8`, `#CAEEF2`, `#A4D2D9`, `#80AAB7`, `#547A8A`

Quiet sequential scale with a strong dark endpoint. Effective for backgrounds-to-primary hierarchy and low-saturation heatmaps.

### muted-teal-5

`#D3F5EF`, `#B4E3DE`, `#96C8C7`, `#6FA1A5`, `#4F808A`

Muted cool sequence for materials and environmental figures. Suitable for broad areas because saturation is restrained.

### blue-5

`#154778`, `#397AAA`, `#5FA9D1`, `#95D4EE`, `#C8EBF6`

Strong blue sequence. The listed order is dark-to-light; reverse for increasing magnitude when high values should be dark.

### green-pink-8

Role-based soft palette for biological, chemical, materials, and environmental graphics.

`#FBE4E6`, `#E7A8B3`, `#F4C4B8`, `#DFF0E6`, `#B8CDB0`, `#7FB59B`, `#538F7B`, `#2E5B47`

Roles from the source: blush background/base; dusty rose highlight/soft data; peach warm accent; light mint neutral background; sage support; jade mid primary; teal strong primary; moss dark accent. When accessibility matters, do not rely on pink versus green alone—also vary lightness, shape, or line style.

### blue-pink-8

Role-based soft palette for spectra, charge-transfer mechanisms, porous-structure illustrations, and clean multi-panel figures.

`#FCE7EC`, `#E8B3C6`, `#D79AB7`, `#D8D4EA`, `#D4E4F2`, `#9CC6E6`, `#5B7FAF`, `#0F2B55`

Roles from the source: blush background/base; dusty pink soft highlight; rose-mauve warm accent; lavender neutral; mist blue support; sky blue mid primary; slate blue strong primary; deep navy dark accent/text.

## Combining families

- Use one family as the dominant system. Borrow at most one contrasting accent from another family unless the figure has genuinely separate semantic domains.
- For two emphasized conditions, pair endpoints with strong lightness and hue separation, such as `#F26A1D` and `#1E5FA8`.
- For control versus several treatments, keep control charcoal (`#4D4D4D` or `#333333`) and assign treatments from one coherent hue family.
- For uncertainty bands, use the same series hue at reduced opacity or a documented pale companion; do not introduce a new category color.
