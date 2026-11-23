# Palette system

Use this reference whenever selecting, revising, or auditing colors.

## First classify the data

1. **Sequential**: ordered values from low to high, such as concentration, temperature, precipitation, energy use, population, or capacity. Use a perceptually uniform light-to-dark palette.
2. **Diverging**: signed change around a meaningful neutral value, such as anomaly, difference, bias, residual, avoided emissions, or net benefit. Use two perceptually balanced arms and centre the normalization on the neutral value, normally 0.
3. **Cyclic**: direction, phase, day of year, or wind direction. Use a cyclic palette whose endpoints meet smoothly.
4. **Categorical**: unordered technologies, scenarios, land-cover classes, regions, or models. Use a limited qualitative set and add marker or line-style redundancy when needed.
5. **Binary or thresholded**: attainment/non-attainment, hazard/no hazard, significance, or mask. Use a restrained two-state scheme and distinguish missing data from either state.

## Preferred scientific sources

Use upstream implementations instead of manually copying screenshots or approximate RGB values.

- [cmocean](https://matplotlib.org/cmocean/): preferred for oceanographic and many atmospheric variables. Useful families include `thermal`, `haline`, `solar`, `ice`, `gray`, `oxy`, `deep`, `dense`, `algae`, `matter`, `turbid`, `speed`, `amp`, `tempo`, `balance`, `delta`, `curl`, and `phase`.
- [NASA GISS Panoply color tables](https://www.giss.nasa.gov/tools/panoply/colorbars/): useful for geophysical raster maps and established Earth-science conventions. Preserve licensing and attribution requirements for any redistributed table.
- [ColorBrewer](https://colorbrewer2.org/): use color-blind-safe sequential, diverging, or qualitative schemes. Good defaults include `RdBu`, `PuOr`, `BrBG`, `PRGn`, `YlGnBu`, `Blues`, and `Set2`, with direction reversed when semantics require it.
- [viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html): preferred general sequential family (`viridis`, `magma`, `inferno`, `plasma`, `cividis`) because it is perceptually uniform and robust in greyscale.
- [Scientific Colour Maps by Fabio Crameri](https://www.fabiocrameri.ch/colourmaps/): geoscience-oriented, perceptually uniform, colour-vision-deficiency-friendly and citable palettes. Useful additions include `batlow` for general sequential data, `roma`/`vik` for signed change, `oleron` for topography–bathymetry and `romaO` for cyclic quantities. Use an upstream package such as `cmcrameri` rather than sampling colours from screenshots.
- [NCAR/NCL color-table gallery](https://www.ncl.ucar.edu/Document/Graphics/color_tables.shtml): a broad meteorology and climate collection, including MeteoSwiss and colour-deficiency-oriented tables. Treat it as a specialist reference library rather than assuming every legacy table is perceptually uniform.
- [Unidata MetPy colortables](https://unidata.github.io/MetPy/latest/api/generated/metpy.plots.ctables.html): operational meteorology palettes and boundary-aware normalization tools, particularly useful for radar and convention-bound weather products. Use these when community conventions carry quantitative meaning.
- [Generic Mapping Tools color palette tables](https://docs.generic-mapping-tools.org/latest/cookbook/cpts.html): Earth-science, bathymetry, topography and cartographic CPT resources with continuous, discrete, categorical and hinged palettes. Verify perceptual behavior and translate ranges and hinges explicitly when using them outside GMT.

## Domain-semantic guidance

The scientific structure comes first; domain semantics choose among valid palettes.

| Topic or quantity | Recommended direction | Avoid |
|---|---|---|
| Ocean depth, water content, precipitation | blue, blue-green, or cmocean `deep`/`rain`-like sequential | saturated rainbow |
| Temperature or heat load | cmocean `thermal`, `inferno`, or yellow-orange-red sequential | blue-to-red if values are unsigned |
| Vegetation, greenness, ecosystem benefit | green or blue-green sequential; `algae`, `YlGn`, `YlGnBu` | red-green binary contrast |
| Air-pollutant concentration | `magma`, `inferno`, `cividis`, orange-red-purple sequential | categorical hues for continuous values |
| Hazard, mortality, damage, exceedance | orange-red, red-purple, or `matter` sequential | bright green for high risk |
| Energy demand, capacity, infrastructure | blue, teal, purple, or neutral grey sequential | semantically overloaded traffic-light colors |
| Emission reduction or avoided impact | diverging with beneficial reductions in blue/green and increases in orange/red | inconsistent sign-to-color mapping |
| Anomaly, bias, delta, net flux | `balance`, `delta`, `RdBu`, `PuOr`, `BrBG`, or `PRGn`, centred on 0 | uncentred normalization |
| Wind or aspect direction | cyclic `phase`/`twilight` style | sequential palette with a seam |

## Shared-range rules

- Pool directly comparable arrays before computing limits.
- Prefer domain-defined limits. Otherwise use robust pooled quantiles and disclose clipping.
- For a zero-centred diverging scale, use equal absolute limits: `[-M, M]`, where `M` is the larger absolute pooled bound.
- Preserve identical limits across scenarios, decades, regions, and model variants when the reader is expected to compare magnitude.
- If a common range hides a scientifically important pattern, retain the common main figure and add a clearly labelled supplemental zoom rather than silently rescaling a panel.

## Accessibility checks

- Simulate common color-vision deficiencies when tools are available.
- Check greyscale ordering for continuous palettes.
- Add shape, line style, hatching, or direct labels to categorical comparisons.
- Ensure missing values use a neutral, explicit color such as light grey and appear in the caption.
- Avoid more than 6 to 8 categorical hues in one view. Split or group categories when necessary.
