# aadarwal/plugins

A marketplace of focused agent capabilities for academic work, organized around two modes: **producing papers** and **understanding things**. Installable as both a [Claude Code](https://claude.com/claude-code) plugin marketplace (`aadarwal-plugins`) and a [Pi](https://pi.dev) package (`aadarwal-pi-plugins`).

Each plugin provides **skills** (model-invoked domain knowledge), **commands** (user-invoked workflows), and where useful, **subagents** (isolated, focused critics and analysts). The design stance throughout: the tools audit, verify, and polish the human's work — they do not generate papers. Checks that can be deterministic (compilation, DOI lookups, page counts, linters, rendered output) are scripts and real commands, not model opinions. Findings are quote-anchored with severity tiers, never numeric scores.

## `plugins/paper/` — producing papers

| Plugin | Skills | Commands |
|---|---|---|
| [`science-writing`](plugins/paper/science-writing) | imrad-structure, abstract-writing, citation-formatting, citation-verification | `/peer-review` `/style-critic` `/verify-citations` `/check-claims` `/presubmit` `/arxiv-prep` `/rebuttal` `/critique-figures` |
| [`tikz`](plugins/paper/tikz) | tikz-diagrams, tikz-cd, pgfplots | `/render-tikz` (compile → render → **look** → fix loop) |
| [`writing-styles`](plugins/paper/writing-styles) | hemingway, academic, plain-language, technical-blog | — |

Highlights:
- `/verify-citations` checks every reference against Crossref, OpenAlex, and Semantic Scholar (2-source rule, chimeric-reference detection, retraction checks). `/check-claims` verifies that cited papers actually support the sentences citing them, with side-by-side quotes.
- `/peer-review` is built on the ICLR reviewer guide's four questions and the ACL Rolling Review form — desk-check first, numbered quote-anchored weaknesses, soundness separated from significance, optional `--variance N` to report a distribution of verdicts instead of a false point estimate.
- `/rebuttal` parses referee reports into a point ledger, classifies each point, drafts responses, and verifies every "we have revised…" claim against the actual diff before the letter ships.
- `/render-tikz` reads the rendered PNG and audits it against a visual checklist (label collisions, arrowheads, clipping) before declaring a figure done.

## `plugins/understanding/` — understanding things

| Plugin | Skills | Commands |
|---|---|---|
| [`explore`](plugins/understanding/explore) | explore-report, decision-inference | `/explore` |
| [`manim`](plugins/understanding/manim) | manim-scenes, manim-animations, manim-3d, manim-ce-vs-gl | `/manim-preview` `/manim-review` |
| [`marimo`](plugins/understanding/marimo) | marimo-authoring | `/new-marimo` |

Highlights:
- `/explore` generates a **single self-contained interactive HTML report** of an unfamiliar codebase: a clickable architecture tree (C4 altitudes, ≤24 nodes), 5–10 design choices inferred from code and git history as evidence-backed ADR cards with confidence labels, a traced main path, churn hotspots, and hidden seams (change-coupled files with no import edge). Fixed template, fixed taste — every repo gets the same artifact shape. Three analyst subagents (structure-mapper, flow-tracer, historian) fan out in parallel.
- `/manim-review` doesn't just lint the code — it renders, extracts frames with ffmpeg, and watches the animation: reading-time per text line, overlaps, out-of-frame elements, dead air, effect-before-cause ordering.
- The marimo plugin follows marimo's official agent rules and treats `uvx marimo check --fix` as the post-edit contract.

## Install

### Claude Code

```
/plugin marketplace add aadarwal/plugins
/plugin install science-writing@aadarwal-plugins
/plugin install explore@aadarwal-plugins
```

> The GitHub repo is `aadarwal/plugins`; the marketplace name inside `marketplace.json` is `aadarwal-plugins` — `marketplace add` takes the repo slug, `install` takes the marketplace name.

### Pi

```bash
pi install git:github.com/aadarwal/plugins   # or a local path
pi -e <source>                               # one-off trial without installing
```

Pi loads the package via the root `package.json` manifest (`pi.skills`, `pi.prompts` globs). Skills are bit-identical across both harnesses (shared Agent Skills standard); commands become flat `/name` prompts. Two consequences we honor repo-wide: **command filenames are globally unique** (pi has no plugin namespacing), and **every skill has a rich `description`** (pi silently drops skills without one). Subagents (`agents/*.md`) are Claude Code-only; commands that use them degrade gracefully to sequential passes.

Future pi-specific enhancement worth building: a small TypeScript extension rendering TikZ/manim output as inline terminal images after each edit (pi supports inline images in Kitty/iTerm2/Ghostty/WezTerm).

## How it's organized

```
plugins/                               # repo root
├── package.json                       # Pi package manifest
├── .claude-plugin/marketplace.json    # Claude marketplace manifest
└── plugins/
    ├── paper/<name>/                  # plugins for producing papers
    └── understanding/<name>/          # plugins for understanding code, math, data
        ├── .claude-plugin/plugin.json
        ├── skills/<skill>/SKILL.md    # model-invoked knowledge (may carry assets, e.g. template.html)
        ├── commands/<cmd>.md          # user-invoked workflows
        └── agents/<agent>.md          # focused subagents (Claude Code)
```

## Adding a new plugin

1. `mkdir -p plugins/<group>/<name>/{.claude-plugin,skills,commands,agents}` where `<group>` is `paper` or `understanding`.
2. Write `plugins/<group>/<name>/.claude-plugin/plugin.json` with `name`, `version`, `description`.
3. Add skills (`skills/<skill>/SKILL.md` with `name` + rich `description` frontmatter) and commands (`commands/<cmd>.md` — filename globally unique across all plugins).
4. Register the plugin in `.claude-plugin/marketplace.json`. The Pi globs (`plugins/*/*/skills`, `plugins/**/commands/*.md`) pick it up automatically.

## License

MIT — see [LICENSE](LICENSE).
