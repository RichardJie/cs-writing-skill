# Scientific Color Palettes

A reusable Codex skill for choosing, applying, and auditing publication-ready color systems for scientific figures.

面向科研绘图的 Codex 配色技能。它不是简单提供一组“好看的颜色”，而是根据数据语义选择分类色、连续色、发散色或机理图角色色，并检查跨面板一致性、灰度可读性和色觉可访问性。

## What it provides

- 12 curated palette families with exact HEX values
- Decision rules for categorical, sequential, diverging, density, and role-based color encodings
- Guidance for spectra, heatmaps, scatter plots, bars, box/violin plots, networks, mechanisms, workflows, and multi-panel figures
- A small dependency-free exporter for Python, R, CSS, JSON, and plain HEX
- Guardrails against rainbow scales, unjustified diverging midpoints, low-contrast pastels, and inconsistent group mappings

The original reference images are not redistributed in this repository.

## Installation

Clone the repository into the Codex skills directory:

```bash
git clone https://github.com/muzark/scientific-color-palettes.git ~/.codex/skills/scientific-color-palettes
```

If `CODEX_HOME` points elsewhere, place the repository in its `skills` directory.

## Usage

Invoke explicitly:

```text
Use $scientific-color-palettes to choose and apply a publication-ready palette for this scientific figure.
```

中文示例：

```text
使用 $scientific-color-palettes 给这张多面板科研图统一配色，并检查色盲和灰度可读性。
```

Codex can also discover the skill automatically for scientific-figure color requests.

## Palette exporter

List palette names:

```bash
python scripts/palette.py list
```

Export a palette:

```bash
python scripts/palette.py get orange-blue-6 --format python
python scripts/palette.py get blue-5 --format r --reverse
python scripts/palette.py get green-pink-8 --format json
```

Supported formats are `hex`, `python`, `r`, `css`, and `json`.

## Repository structure

```text
scientific-color-palettes/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── application-guide.md
│   └── palette-catalog.md
└── scripts/palette.py
```

## Design principle

Color should encode scientific meaning, not decorate the figure. Exact palettes are useful, but the data type, meaningful midpoint, visual hierarchy, final publication size, and redundant visual cues determine whether a palette is scientifically effective.

## License

MIT. See [LICENSE](LICENSE).
