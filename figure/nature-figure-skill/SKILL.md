---
name: nature-figure-skill
description: "Nature-grade scientific figure workflow and FigureForge visual studio: contract-first Python/R publication plotting (editable SVG/PDF/600-DPI TIFF, non-occluding legends, semantic palettes, 83-panel atlas) plus 22-template/16-palette browser editor."
---

# `nature-figure-skill` — Sub-Skill Entrypoint (`figure/nature-figure-skill/`)

Integrated upstream snapshot of [`jing1312/nature-figure-skill`](https://github.com/jing1312/nature-figure-skill) (building on [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills) and [`ChenLiu-1996/figures4papers`](https://github.com/ChenLiu-1996/figures4papers); MIT licensed — see [LICENSE](LICENSE) and [DERIVATIVE_NOTICE.md](DERIVATIVE_NOTICE.md)).

When dispatched from the parent [`../SKILL.md`](../SKILL.md) hub (via `:nature`, `:figureforge`, `:python`, `:r`, or default scientific plotting intent), load the exact entry file matching the execution route:

| Route | Primary Entrypoint | Supporting Playbooks & Assets |
|:---|:---|:---|
| **1. Scripted Publication Figure Workflow (`Python` / `R`)** | [skills/nature-figure/SKILL.md](skills/nature-figure/SKILL.md) | [figure-selection.md](skills/nature-figure/references/figure-selection.md), [figure-contract.md](skills/nature-figure/references/figure-contract.md), [atlas-gallery.md](skills/nature-figure/references/atlas-gallery.md), [backend-selection.md](skills/nature-figure/references/backend-selection.md), [api.md](skills/nature-figure/references/api.md), [r-workflow.md](skills/nature-figure/references/r-workflow.md), [common-patterns.md](skills/nature-figure/references/common-patterns.md), [design-theory.md](skills/nature-figure/references/design-theory.md), [nature-2026-observations.md](skills/nature-figure/references/nature-2026-observations.md), [chart-types.md](skills/nature-figure/references/chart-types.md), [tutorials.md](skills/nature-figure/references/tutorials.md), [demos.md](skills/nature-figure/references/demos.md), [qa-contract.md](skills/nature-figure/references/qa-contract.md) |
| **2. Visual No-Code / Layout-First Studio (`FigureForge`)** | [figureforge/README.md](figureforge/README.md) & [figureforge/index.html](figureforge/index.html) | 22 publication-grade SVG templates ([figureforge/js/templates.js](figureforge/js/templates.js)), 16 curated palettes ([figureforge/js/palettes.js](figureforge/js/palettes.js)), 9 showcase atlases / 83 panels ([assets/](assets/)), live hosted studio at <https://jing1312.github.io/nature-figure-skill/figureforge/> |
| **3. Upstream Overview & Bilingual Docs** | [README.md](README.md) / [README.zh-CN.md](README.zh-CN.md) | [install.md](install.md), [skills/nature-figure/README.md](skills/nature-figure/README.md), [skills/nature-figure/README.zh-CN.md](skills/nature-figure/README.zh-CN.md), [LICENSE](LICENSE), [DERIVATIVE_NOTICE.md](DERIVATIVE_NOTICE.md) |
| **4. Bundled Companion `nature-*` Modules** | `skills/nature-*/SKILL.md` | [nature-polishing](skills/nature-polishing/SKILL.md), [nature-writing](skills/nature-writing/SKILL.md), [nature-citation](skills/nature-citation/SKILL.md), [nature-data](skills/nature-data/SKILL.md), [nature-reader](skills/nature-reader/SKILL.md), [nature-response](skills/nature-response/SKILL.md), [nature-paper2ppt](skills/nature-paper2ppt/SKILL.md), [nature-academic-search](skills/nature-academic-search/SKILL.md) |

## Mandatory Execution Contract

1. **Triage `FigureForge` vs. Scripted Code FIRST**:
   - No-code, drag-and-drop, layout-skeleton, or WYSIWYG SVG tweaking requests route immediately to **FigureForge** ([figureforge/README.md](figureforge/README.md)) without asking `"Python or R?"`.
   - Reproducible data-to-figure pipelines, batch plotting, CSV/TSV rendering, or strict journal-spec bundles enter [skills/nature-figure/SKILL.md](skills/nature-figure/SKILL.md).
2. **Three Non-Negotiable Publication Laws** (enforced in [skills/nature-figure/SKILL.md](skills/nature-figure/SKILL.md)):
   - **Final Print Typography (`5–7 pt` at 1:1 journal width, `0.8 pt` axes)**: Never hardcode slide-sized `16–24 pt` defaults on `89 mm` / `183 mm` canvases.
   - **Zero Data Occlusion**: Legends sit frameless outside the data region; statistics sit in a frameless strip above the axes (`add_stat_strip`).
   - **Unified Submission Bundle (`save_pub_set` / `save_pub_r`)**: Export every independent figure as editable `.svg` (`svg.fonttype = 'none'`) + TrueType `.pdf` (`pdf.fonttype = 42`) + `600 DPI` `.tiff`—never silently merge separate manuscript figures into one collage.
