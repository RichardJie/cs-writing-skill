# Scientific Plotting Skill

A reusable Codex skill for designing, building, and checking scientific figures. It includes figure-selection guidance, quality checks, and parameterized R/ggplot2 recipes. The skill is self-contained: the source book and its PDF are not included or required.

## Install

Place this directory at `~/.agents/skills/scientific-plotting` for use across projects, or at a repository's `.agents/skills/scientific-plotting` for repository-scoped use. See the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and invocation. The entrypoint is [SKILL.md](SKILL.md).

## Use

Ask Codex to design, revise, or quality-check a scientific figure, or invoke `$scientific-plotting` explicitly. The instructions route to the relevant guides in `references/`. R recipes live in `recipes/r/`; source `scripts/figure-tools.R` before sourcing a recipe. For a project script, adapt `assets/figure-template.R` to your own data and output path.

The recipes do not install R packages. They check for required packages when used. The full validation suite requires compatible versions of `ggplot2`, `patchwork`, `ggrepel`, `ggridges`, `sf`, `circlize`, `ggseqlogo`, `ragg`, `svglite`, `jsonlite`, and `systemfonts`. Individual recipes need only their relevant subset. Statistical methods, source data, and journal-specific export requirements remain the user's responsibility.

## Verify

Run the included synthetic-data checks without the book:

```sh
Rscript tests/validate_recipes.R . /path/to/output
```

An optional third argument supplies a non-default R library path. Tests write example figures, `validation.json`, and `session-info.txt` to the output directory. Some advanced packages may take time to install on a new system. Historical construction results and their limits are described in [validation status](references/validation-status.md); they do not validate an individual scientific analysis.

## Provenance And Rights

The plotting guidance was informed in part by *SCI论文绘图之道* (Leopard / 医学方, 2019). Page pointers in some references are attribution only; all usable instructions are included here. No PDF, book page, figure screenshot, source dataset, or verbatim code listing is distributed. The recipes are new parameterized implementations. This repository is not affiliated with or endorsed by the book's author or publisher.

The MIT license applies to the original skill content in this repository, not to third-party books, packages, or datasets.
