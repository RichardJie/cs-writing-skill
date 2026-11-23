# Template Resources

> **Discovery contract**: Use the README files for human browsing and the adjacent `index.json` files for programmatic lookup. JSON indexes are the source of truth for current entries, versions, metadata, and totals; do not copy their counts into this hub.

## Design Specification References

Three reference templates cover content planning, theme planning, and generated theme API summaries:

- **`content_design_spec_reference.md`** — Content planning: slide-by-slide outline, image lists, chart references, packages
  [View Content Design Spec Reference](./content_design_spec_reference.md)

- **`theme_design_spec_reference.md`** — Visual theme design: color scheme, typography, slide type visuals, component designs
  [View Theme Design Spec Reference](./theme_design_spec_reference.md)

- **`theme_reference.md`** — Template for generating `theme.md` API summary files
  [View Theme Reference](./theme_reference.md)

## Theme Templates

The `themes/` directory contains Touying theme templates organized by source:

- **`builtin/`** — Touying built-in themes (demo files only, imported directly from Touying)
- **`universe/`** — Community themes from [typst.app/universe](https://typst.app/universe/search/?kind=templates&q=touying)
- **`custom-plain/`** — Plain-tier theme templates (simple color/font customization)
- **`custom-rich/`** — Rich-tier theme templates (data components, multi-layout)
- **`custom-canvas/`** — Canvas-tier theme templates (full per-slide bespoke design)
- **`user/`** — User-created themes (generated during sessions, stored locally)

**Lookup**:
- **Dispatch**: [themes/README.md](./themes/README.md) (routes to the right tier by model capability)
- **AI / Programmatic**: Per-tier index files (e.g. `themes/custom-rich/index.json`, `themes/custom-canvas/index.json`)

> Themes are organized by complexity tier: **Plain** (color/typography only), **Rich** (structured components), **Canvas** (full editorial/SVG compositions). See `themes/README.md` for routing.

> To create a new Touying theme from scratch, use the `${SKILL_DIR}/workflows/create-template.md` workflow.

## Chart Components

The `charts/` directory contains reusable chart and infographic components organized by communication purpose and implementation package.

- **Human browsing**: [charts/README.md](./charts/README.md)
- **AI / Programmatic lookup and current inventory**: [charts/index.json](./charts/index.json)

## Useful Packages

The `packages/` directory contains curated Typst packages for presentation-specific needs such as math, code, diagrams, charts, annotations, tables, and utilities.

- **Human browsing**: [packages/README.md](./packages/README.md)
- **AI / Programmatic lookup, versions, and current inventory**: [packages/index.json](./packages/index.json)

## Scenario Templates

The `scenarios/` directory contains Typst demos for CVs, social covers, and posters. Social-cover
examples use a local `template.typ` plus `demo.typ`; CV and poster examples usually remain direct
`.typ` starters. These are starting points for the scenario references, not Touying deck themes.

- **Human browsing**: [scenarios/README.md](./scenarios/README.md)
- **AI / Programmatic routing**: [scenarios/index.json](./scenarios/index.json)

## Icon Resources

The `icons/` directory catalogs built-in symbols and optional icon packages for slides. **Emoji and Typst symbols are the default when they fit the content.**

- **Human browsing**: [icons/README.md](./icons/README.md)
- **AI / Programmatic lookup, versions, and current inventory**: [icons/index.json](./icons/index.json)
