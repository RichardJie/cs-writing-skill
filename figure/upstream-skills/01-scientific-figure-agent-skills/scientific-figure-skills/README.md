# Scientific Figure Skills

**An agent skill suite for planning, rendering, auditing, and packaging publication-grade scientific figures, distributed for Claude Code and OpenAI Codex.**

[![Validation](https://github.com/enesgul23/scientific-figure-skills/actions/workflows/validation.yml/badge.svg)](https://github.com/enesgul23/scientific-figure-skills/actions/workflows/validation.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](VERSION)

Scientific Figure Skills treats a figure as an evidence-bearing artifact rather
than a graphic. The suite equips a coding agent with a governed production
pipeline for manuscript figures: intent scoping, dataset inspection, renderer
and library selection, visual-claim tracking, journal-style status, render and
layout quality audits, reproducible export packaging, dry-run agentic runbooks,
and project-local figure memory.

Two platform packages are provided from one shared core:

| Package | Platform | Invocation | Project memory |
|---|---|---|---|
| [`claude-code/`](claude-code/) | Claude Code (Anthropic) | `/scientific-figure-suite`, `/fig:<name>`, or natural language | `.claude/scientific-figure-memory/` |
| [`codex/`](codex/) | Codex (OpenAI) | `$scientific-figure-suite` or `fig-<name>` aliases | `.codex/scientific-figure-memory/` |

The suite is governed by a fixed scientific priority:

```text
truth > reproducibility > interpretability > journal compliance > visual elegance > novelty
```

It does not fabricate data, does not install packages silently, does not
download external data without explicit approval, and does not claim verified
journal compliance unless current official or user-provided guidance is
available in the active task.

## Contents

1. [Capabilities](#capabilities)
2. [Architecture](#architecture)
3. [Installation for Claude Code](#installation-for-claude-code)
4. [Installation for Codex](#installation-for-codex)
5. [Usage](#usage)
6. [Command Aliases](#command-aliases)
7. [Python Runtime and Scripts](#python-runtime-and-scripts)
8. [Shell Helpers](#shell-helpers)
9. [Render Registry and Assets](#render-registry-and-assets)
10. [Project Memory](#project-memory)
11. [Output Status Contract](#output-status-contract)
12. [Platform Packages and Differences](#platform-packages-and-differences)
13. [Validation](#validation)
14. [Requirements](#requirements)
15. [Citation](#citation)
16. [License](#license)

## Capabilities

The suite covers the full life cycle of a manuscript figure.

**Scoping and design.** Underspecified requests are routed to a scoping
workflow that asks at most five targeted questions (scientific message, data
status, figure type, journal or manuscript context, output format) and produces
a `figure_intake` artifact before any rendering takes place. Domain workflows
then design statistical plots, model-performance figures, clinical and
biomedical figures, geospatial maps, omics and bioinformatics figures,
multi-panel compositions, mechanism schematics, and graphical abstracts.

**Rendering.** Figures are rendered from registry-backed Python templates
(Matplotlib-based, with optional pandas, NumPy, seaborn, scikit-learn,
GeoPandas, and related stacks). Dataset inspection covers CSV, JSON, Excel,
GeoJSON, Shapefile, GeoTIFF, NetCDF, and AnnData-like inputs. The local
Python environment is probed without installation, and a dependency plan lists
required, recommended, optional, blocked, and fallback libraries together with
install commands for the user's review.

**Auditing.** Independent audits check render quality (blank or near-blank
rasters, missing files, SVG label presence, hashes, visual regression sanity),
multi-panel layout (optical grid alignment, panel overlap, colorbar spacing and
titles, semantic color consistency, controlled direct labels), text layout
(overlap, clipping, axis bounds, minimum font size, excessive rotation,
colorbar-title crowding, domain terminology), accessibility (color, contrast,
alt text), statistical honesty, image integrity, and journal-style status.
Text layout defects can be repaired deterministically (wrap, shorten, rotate,
reserve margins, hide low-priority labels) and re-audited.

**Packaging.** Export packages combine figure specifications, runnable code,
captions and alt text, visual-claim ledgers, quality reports, submission
manifests with file hashes, reproducibility notes, and journal-style status.
Submission readiness is decided from quality gates and audit ledgers, never
from memory alone.

**Memory and orchestration.** Project-local, file-based memory (Figure
Passports, dataset registries, claim ledgers, audit histories, hash-linked
reset/resume boundaries, optional author style profiles) persists across
sessions. A dry-run orchestration layer builds agentic runbooks from that
memory, selects the next safe action, and executes only whitelisted suite
scripts when the user explicitly requests execution.

## Architecture

Each platform package contains a single discoverable root skill and a set of
internal workflows that are deliberately not registered as separate skills.

```text
<platform>/skills/scientific-figure-suite/
  SKILL.md                         # Root router skill (the only discovered entry point)
  manifest.json                    # Public interface and package metadata
  MODE_REGISTRY.md                 # Command and mode registry
  POSITIONING.md                   # Scope and integrity boundary
  commands/                        # Command alias recipes (fig-*.md)
  fig/<workflow>/WORKFLOW.md       # 13 internal workflows with role-prompt agents
  shared/                          # Protocols, quality gates, state machine, handoff schemas
  shared/contracts/                # 32 JSON schemas for suite artifacts
  references/                      # Figure design references (statistics, journals, domains)
  templates/                       # Reusable artifact templates
  examples/                        # Realistic non-binary fixtures
  assets/render_registry/          # Chart type to renderer and dependency metadata
  assets/render_templates/         # Python starter render templates
  assets/library_pool/             # Python library metadata pool
  assets/style_tokens/             # Estimated journal style token profiles
  assets/panel_layout_templates/   # Multi-panel layout templates
  assets/text_profiles/            # Bundled domain terminology profiles
  scripts/                         # 53 Python runtime, validation, memory, and audit scripts
  scripts/bin/                     # POSIX shell helpers
  tests/                           # Sample fixtures, smoke prompts, expected routing
  docs/                            # Architecture and validation notes
```

The router in `SKILL.md` selects one workflow per request and loads only the
files that workflow needs. Agent files under `fig/<workflow>/agents/` are
scoped role prompts executed inline in the current conversation; parallel
subagents are used only when the user explicitly asks for delegation.

| Workflow | Scope |
|---|---|
| `intake-design` | Scoping, planning, scientific message, figure intake |
| `statistical-plots` | Quantitative results, distributions, uncertainty displays |
| `model-performance` | AI/ML metrics, calibration, validation splits, diagnostics |
| `clinical-biomedical` | Trials, survival, diagnostic accuracy, denominators and endpoints |
| `geospatial-maps` | Vector and raster maps, study areas, spatial integrity |
| `omics-bioinformatics` | Volcano plots, heatmaps, thresholds, pathway figures |
| `multipanel-composer` | Panel architecture, cross-panel consistency |
| `schematic-mechanism` | Conceptual and mechanism diagrams, claim boundaries |
| `graphical-abstract` | Visual narrative within evidence boundaries |
| `journal-style-translator` | Journal style tokens and verification status |
| `caption-alttext` | Captions, legends, notes, alt text, caption integrity |
| `figure-auditor` | Visual integrity, statistical, and accessibility review |
| `export-packager` | Export manifests, reproducibility packaging |

## Installation for Claude Code

Claude Code discovers skills from `~/.claude/skills/<name>/SKILL.md`
(global) or `<project>/.claude/skills/<name>/SKILL.md` (project). The suite
also ships an optional command pack that installs to `~/.claude/commands/fig/`
and appears as namespaced slash commands (`/fig:plan`, `/fig:audit`, and so on).

Clone the repository:

```bash
git clone https://github.com/enesgul23/scientific-figure-skills.git
cd scientific-figure-skills
```

Linux, macOS, and WSL:

```bash
bash install.sh                        # skill + /fig:* command pack into ~/.claude
bash install.sh --link                 # symlink the checkout instead of copying
bash install.sh --no-commands          # skill only
bash install.sh --project              # install into ./.claude of the current project
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1                 # skill + /fig:* command pack
powershell -ExecutionPolicy Bypass -File .\install.ps1 -NoCommands     # skill only
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Project        # into .\.claude of the current project
```

Manual installation (any platform):

```bash
mkdir -p ~/.claude/skills ~/.claude/commands
cp -R claude-code/skills/scientific-figure-suite ~/.claude/skills/scientific-figure-suite
cp -R claude-code/claude-commands/fig ~/.claude/commands/fig
```

Set `CLAUDE_HOME` (shell) or `CLAUDE_CONFIG_DIR` (PowerShell) to target a
non-default Claude Code configuration directory. Start a new Claude Code
session after installation; `/skills` lists the skill and `/help` lists the
`/fig:*` commands.

## Installation for Codex

Codex discovers skills from `~/.codex/skills/<name>/SKILL.md`. The Codex
package carries the `agents/openai.yaml` interface descriptor and supports
implicit invocation.

Linux, macOS, and WSL:

```bash
bash install.sh --platform codex       # copy into ~/.codex/skills
bash install.sh --platform codex --link
bash install.sh --platform all         # Claude Code and Codex together
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Platform codex
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Platform all
```

Manual installation:

```bash
mkdir -p ~/.codex/skills
cp -R codex/skills/scientific-figure-suite ~/.codex/skills/scientific-figure-suite
```

Set `CODEX_HOME` to target a non-default Codex home directory. Restart Codex
or reload skills after installation.

## Usage

The suite is invoked explicitly by name, by command alias, or implicitly when
the request concerns a scientific, manuscript, or journal-style figure.

Claude Code:

```text
/scientific-figure-suite plan a journal-ready multi-panel model performance figure
/fig:scope Nature-style scientific figure for a flood forecasting paper
/fig:plan-libraries for data/predictions.csv and a parity scatter figure
/fig:render-template parity_scatter from predictions.csv
/fig:audit-render exported files in figures/output
fig-agent-plan for the current project memory
```

Codex:

```text
Use $scientific-figure-suite to plan a journal-ready multi-panel model performance figure.
fig-scope Nature-style scientific figure for a flood forecasting paper
fig-plan-libraries for data/predictions.csv and a parity scatter figure
fig-render-template parity_scatter from predictions.csv
fig-audit-render exported files in figures/output
```

Plain aliases of the form `fig-<name> ...` work on both platforms. When a
request lacks a clear scientific message, data status, figure type, journal
context, or output format, the suite routes to scoping first and does not
render or export until those inputs are resolved.

## Command Aliases

Thirty-eight aliases are defined as prompt recipes under `commands/`. On
Claude Code each alias is additionally available as `/fig:<name>`; on Codex the
plain form `fig-<name>` is used.

| Alias | Purpose |
|---|---|
| `fig-scope` | Clarify an underspecified figure request without rendering. |
| `fig-plan` | Produce a structured figure plan and workflow chain. |
| `fig-full` | Run the full staged figure production chain. |
| `fig-model-performance` | Design and audit model-performance figures. |
| `fig-graphical-abstract` | Design a graphical abstract within evidence boundaries. |
| `fig-style` | Apply an estimated or verified journal style profile. |
| `fig-verify-journal` | Record journal guideline verification evidence. |
| `fig-caption` | Produce captions, legends, notes, and alt text. |
| `fig-audit` | Run quality, integrity, accessibility, and journal-status audits. |
| `fig-audit-render` | Run visual QA and render-quality checks. |
| `fig-audit-multipanel-layout` | Audit panel geometry, colorbars, semantic colors, and optical grid. |
| `fig-audit-text-layout` | Audit text overlap, clipping, axis bounds, colorbar titles, and terminology. |
| `fig-repair-text-layout` | Repair crowded text layout deterministically, then re-audit. |
| `fig-audit-visual-artifact` | Append a file-level visual audit artifact. |
| `fig-audit-figure-set` | Audit cross-figure consistency for a figure set. |
| `fig-audit-readiness` | Decide submission readiness from memory and audit ledgers. |
| `fig-audit-repro-lock` | Detect stale outputs from data, code, or environment hash drift. |
| `fig-export` | Produce export packages and submission manifests. |
| `fig-build-figure-set` | Build a manuscript-level figure set manifest. |
| `fig-build-submission-package` | Build a hash-indexed submission package. |
| `fig-render-template` | Render from the registry-backed Python templates. |
| `fig-plan-libraries` | Inspect data and plan plotting and data libraries. |
| `fig-probe-environment` | Probe available Python imports and versions. |
| `fig-select-render-stack` | Select a minimal Python render stack. |
| `fig-plan-external-data` | Decide whether external data are scientifically justified. |
| `fig-init-memory` | Initialize project-local Figure Passport memory. |
| `fig-load-memory` | Validate and summarize project memory. |
| `fig-update-memory` | Update passports, dataset registry, and claim ledger. |
| `fig-summarize-memory` | Summarize project memory state. |
| `fig-validate-memory` | Validate memory files against the contracts. |
| `fig-migrate-memory` | Migrate memory to the current schema. |
| `fig-forget-memory` | Remove selected memory scopes with explicit confirmation. |
| `fig-resume-project` | Resume from a hash-linked reset/resume boundary. |
| `fig-status` | Build a pipeline dashboard from project memory. |
| `fig-agent-plan` | Build a dry-run agentic runbook. |
| `fig-agent-next` | Select the next safe action from a runbook. |
| `fig-agent-resume` | Rebuild the runbook from memory and resume planning. |
| `fig-doctor` | Diagnose environment, registry, library pool, and memory fixtures. |

## Python Runtime and Scripts

The runtime is a set of standalone Python 3.11+ scripts under `scripts/`. They
are plan-first and side-effect-aware: none of them installs packages, downloads
data, or overwrites project memory without an explicit flag. Scripts are
executed from the user's project root and referenced by their installed skill
path so that project-local files resolve correctly. For a Claude Code
installation:

```bash
SFS=~/.claude/skills/scientific-figure-suite     # Codex: ~/.codex/skills/scientific-figure-suite
```

| Group | Scripts |
|---|---|
| Data and environment | `inspect_dataset.py`, `probe_python_environment.py`, `select_library_stack.py`, `build_dependency_plan.py`, `plan_external_data.py`, `validate_data_acquisition_plan.py`, `validate_library_pool.py` |
| Rendering and export | `render_from_registry.py`, `export_static_figure.py`, `export_multipanel.py`, `generate_style_tokens.py`, `select_text_profile.py`, `validate_render_template_registry.py`, `validate_style_tokens.py` |
| Audits | `audit_render_quality.py`, `audit_multipanel_layout.py`, `audit_text_layout.py`, `repair_text_layout.py`, `audit_accessibility.py`, `audit_export_files.py`, `audit_journal_profile.py`, `audit_journal_verification.py`, `audit_reproducibility.py`, `audit_repro_lock.py`, `audit_visual_artifact.py`, `audit_figure_set_consistency.py`, `audit_submission_readiness.py` |
| Packaging | `build_figure_manifest.py`, `build_figure_set_manifest.py`, `build_submission_package_index.py`, `build_pipeline_dashboard.py` |
| Project memory | `init_memory.py`, `validate_memory.py`, `summarize_memory.py`, `migrate_memory.py`, `forget_memory.py`, `update_figure_passport.py`, `update_dataset_registry.py`, `append_visual_claim.py`, `append_figure_decision.py`, `resume_figure_project.py` |
| Agentic orchestration | `build_agentic_runbook.py`, `validate_agentic_runbook.py`, `advance_agentic_runbook.py`, `summarize_agentic_run.py` |
| Contracts and validation | `validate_figure_spec.py`, `validate_visual_claim_ledger.py`, `validate_handoff_artifact.py`, `validate_contracts.py`, `validate_skill.py`, `validate_repo_hygiene.py` |

Representative invocations:

```bash
# Inspect data, probe the environment, and plan dependencies (no installation)
python "$SFS/scripts/inspect_dataset.py" --input data/predictions.csv --out dataset_profile.json
python "$SFS/scripts/probe_python_environment.py" --out environment_probe.json
python "$SFS/scripts/build_dependency_plan.py" --chart-type parity_scatter \
  --dataset-profile dataset_profile.json --environment-probe environment_probe.json \
  --out dependency_plan.json

# Render from the registry and audit the result
python "$SFS/scripts/render_from_registry.py" --chart-type parity_scatter \
  --data data/predictions.csv --outdir figures/output --formats pdf,svg,png
python "$SFS/scripts/audit_render_quality.py" --file figures/output/parity_scatter.pdf \
  --file figures/output/parity_scatter.png --expected-formats pdf,png

# Text layout audit and deterministic repair
python "$SFS/scripts/select_text_profile.py" --domain model-performance --chart-type roc_pr_curve \
  --out text_profile_selection.json
python "$SFS/scripts/audit_text_layout.py" --layout text_layout.yaml \
  --text-profile text_profile_selection.json --out text_layout_report.json
python "$SFS/scripts/repair_text_layout.py" --layout text_layout.yaml --out repaired_text_layout.yaml

# Multi-panel layout audit
python "$SFS/scripts/audit_multipanel_layout.py" --layout layout.yaml --out multipanel_layout_audit.json

# External data decision (plan only)
python "$SFS/scripts/plan_external_data.py" --chart-type geospatial_choropleth \
  --goal "need basemap context" --source-name "Natural Earth" \
  --source-url "https://www.naturalearthdata.com/" --license "public domain" \
  --citation "Natural Earth contributors" --out data_acquisition_plan.json

# Project memory (Claude Code path shown; Codex uses .codex/scientific-figure-memory)
python "$SFS/scripts/init_memory.py" --project-root .
python "$SFS/scripts/validate_memory.py" --memory-dir .claude/scientific-figure-memory
python "$SFS/scripts/build_pipeline_dashboard.py" --memory-dir .claude/scientific-figure-memory

# Dry-run orchestration
python "$SFS/scripts/build_agentic_runbook.py" --memory-dir .claude/scientific-figure-memory --out agentic_runbook.json
python "$SFS/scripts/advance_agentic_runbook.py" --runbook agentic_runbook.json --out agentic_run_report.json
```

Every script exposes `--help`. Structured outputs conform to the JSON schemas
under `shared/contracts/` and can be validated with
`validate_handoff_artifact.py --type <artifact_type>`.

## Shell Helpers

POSIX shell wrappers under `scripts/bin/` provide stable entry points for
validation, diagnostics, and orchestration. They wrap the Python runtime and
never install, download, push, or mutate project memory on their own. On
Windows they run under Git Bash or WSL; the Python scripts remain the canonical
runtime.

| Helper | Function |
|---|---|
| `sfs-doctor.sh` | Report repository and skill paths, Python version, availability of pandas, NumPy, and Matplotlib, and render registry validity. |
| `sfs-validate.sh [--no-quick]` | Run skill structure, contract, registry, library-pool, and repository hygiene validation; `--no-quick` skips the full `quick_validate.py` run. |
| `sfs-release-check.sh` | Release gate: `git diff --check`, shell syntax check, repository hygiene, and full validation. |
| `sfs-agent-plan.sh <args>` | Build a dry-run agentic runbook (wraps `build_agentic_runbook.py`). |
| `sfs-agent-next.sh <args>` | Select the next safe action (wraps `advance_agentic_runbook.py`). |
| `sfs-clean-generated.sh` | Remove `__pycache__`, `.pytest_cache`, and `*.pyc` inside the repository only; refuses paths outside it. |

Helper behaviour is controlled by three environment variables: `PYTHON`
selects the interpreter (default `python`, falling back to `python3`),
`PYTHONDONTWRITEBYTECODE` defaults to `1`, and `SFS_REPO_ROOT` overrides the
repository root when the skill is installed outside a git checkout (in that
case the helpers fall back to the skill directory itself).

```bash
bash "$SFS/scripts/bin/sfs-doctor.sh"
bash "$SFS/scripts/bin/sfs-agent-plan.sh" --memory-dir .claude/scientific-figure-memory --out agentic_runbook.json
bash "$SFS/scripts/bin/sfs-agent-next.sh" --runbook agentic_runbook.json
```

## Render Registry and Assets

`assets/render_registry/render_registry.json` maps chart types to Python
templates, required and optional columns, supported domains, default output
formats, compatible style tokens, audit hooks, library stacks, text profiles,
and colorbar and axis-label policies. Registered chart types:

| Chart type | Required columns | Domains |
|---|---|---|
| `parity_scatter` | `observed`, `predicted` | model-performance, statistical-plots |
| `roc_pr_curve` | `y_true`, `score` | model-performance, clinical-biomedical, statistical-plots |
| `bland_altman_plot` | `method_a`, `method_b` | clinical-biomedical, statistical-plots |
| `dose_response_curve` | `dose`, `response` | clinical-biomedical, statistical-plots |
| `time_series_band` | `time`, `value` | statistical-plots, model-performance, geospatial-maps |
| `raincloud_plot` | `group`, `value` | statistical-plots, clinical-biomedical, omics-bioinformatics |
| `forest_plot` | `label`, `estimate`, `lower`, `upper` | clinical-biomedical, statistical-plots |

Additional starter templates (calibration plot, survival plot, volcano plot,
heatmap, geospatial map, residual diagnostic panel, multipanel composer, text
layout) are provided under `assets/render_templates/` for adaptation.

Further assets include estimated style token profiles for Nature, Science,
Cell, The Lancet, NEJM, JAMA, and a universal high-impact profile
(`assets/style_tokens/`); multi-panel layout templates (two-panel, three-panel
horizontal, four-panel grid, Nature double column, clinical trial figure); a
Python library metadata pool with install-risk and publication-grade ratings;
and bundled domain terminology profiles for statistical, model-performance,
clinical, geospatial, omics, and hydrology figures. Journal style profiles are
estimates until verified against current official or user-provided guidelines
in the active task.

## Project Memory

Project memory is file-based, auditable, and local to the user's project. It
is never written into the installed skill directory and it is distinct from
the agent's own memory mechanisms.

```text
.claude/scientific-figure-memory/    # Claude Code
.codex/scientific-figure-memory/     # Codex
```

Memory files include `memory_manifest.json` (single source of truth),
`project_profile.json`, `journal_targets.json`, `figure_passport.json`,
`figure_set_manifest.json`, `submission_package_index.json`,
`dataset_registry.json`, an optional `author_visual_style_profile.json`, and
append-only ledgers: `visual_claim_ledger.jsonl`,
`quality_audit_history.jsonl`, `revision_boundary_ledger.jsonl`,
`journal_guideline_verification.jsonl`, `visual_audit_artifact.jsonl`,
`cross_figure_consistency_history.jsonl`,
`submission_readiness_history.jsonl`, `figure_decision_log.jsonl`,
`visual_regression_history.jsonl`, `multipanel_layout_history.jsonl`,
`text_layout_history.jsonl`, `dependency_plan_history.jsonl`,
`external_data_plan_history.jsonl`, `agentic_task_queue.jsonl`, and
`agentic_run_history.jsonl`.

Memory rules: ledgers are append-only; memory is never overwritten silently;
journal targets are `VERIFIED` only from current official or user-provided
guidelines; memory is never imported across projects without an explicit
request; readiness is never inferred from memory alone; author style is a soft
preference ranked below truth, reproducibility, journal requirements,
accessibility, and statistical honesty; stored outputs are marked stale when
data, code, output, or environment hashes drift from the repro-lock.

## Output Status Contract

Every figure package or plan reports a fixed set of status tags:

```text
DATA_STATUS: PROVIDED / INFERRED / MISSING / MOCKUP
STYLE_STATUS: VERIFIED / ESTIMATED / UNVERIFIED
REPRODUCIBILITY_STATUS: CODED / DESIGN_ONLY / PARTIAL
EXPORT_STATUS: READY / NEEDS_RENDER / NEEDS_JOURNAL_CHECK
INTEGRITY_STATUS: PASS / PASS_WITH_WARNINGS / FAIL
```

Phrases such as "Nature-compliant" or "submission-ready for [journal]" are
permitted only when `STYLE_STATUS` is `VERIFIED`. Figures produced without
supplied data are labelled `NON_DATA_MOCKUP`.

## Platform Packages and Differences

Both packages share the same workflows, protocols, references, contracts,
assets, templates, and Python runtime. They differ only in the platform
adapter layer.

| Aspect | `claude-code/` | `codex/` |
|---|---|---|
| Root skill frontmatter | Single-line `name` and `description` with trigger phrases | Folded multi-line description |
| Interface descriptor | None (`manifest.json` kind `claude_code_skill`) | `agents/openai.yaml` with `$scientific-figure-suite` default prompt and implicit invocation |
| Runtime mapping in `SKILL.md` | Read, Bash, WebFetch and WebSearch tools; Task-tool subagents only on explicit request; permission-gated script execution | Codex filesystem and safety rules; Codex subagents only on explicit request |
| Command aliases | `commands/fig-*.md` recipes plus `claude-commands/fig/*.md` slash commands (`/fig:<name>`) | `commands/fig-*.md` recipes, plain `fig-<name>` form |
| Default project memory | `.claude/scientific-figure-memory/` | `.codex/scientific-figure-memory/` |
| Default decision actor | `claude-code` | `codex` |
| Structural validator | Rejects `agents/openai.yaml`; checks the command pack | Requires `agents/openai.yaml` |

A change to the shared core should be applied to both packages; the CI matrix
validates each independently.

## Validation

Validation is executed per package from the repository root:

```bash
python -m pip install -r requirements-dev.txt
python claude-code/quick_validate.py
python codex/quick_validate.py
```

Each run validates skill structure and manifest consistency, JSON contract
schemas, render registry and library pool metadata, style tokens, memory
initialization and migration, dashboard generation, handoff artifact
validation, renderer smoke tests, dependency planning, external data planning,
render-quality, multi-panel and text-layout audits (including expected failure
fixtures), agentic runbook validation, and repository hygiene (version
synchronization, description length, no generated caches). The same checks run
in GitHub Actions for every push and pull request.

## Requirements

- Python 3.11 or later.
- Runtime and validation dependencies: `PyYAML`, `numpy`, `pandas`, `matplotlib`, `Pillow` (`requirements-dev.txt`). Domain-specific stacks (GeoPandas, seaborn, scikit-learn, and others) are proposed by the dependency planner and installed only with the user's approval.
- Claude Code or Codex with skill discovery enabled.
- A POSIX shell (bash) for the optional helpers; on Windows, Git Bash or WSL.

## Citation

If this suite supports academic work, please cite it. GitHub can generate
citation metadata directly from `CITATION.cff`.

```text
Gul, E. (2026). Scientific Figure Skills (Version 0.9.0) [Computer software]. GitHub. https://github.com/enesgul23/scientific-figure-skills
```

```bibtex
@software{gul_scientific_figure_skills_2026,
  author = {Gul, Enes},
  title = {Scientific Figure Skills},
  year = {2026},
  version = {0.9.0},
  url = {https://github.com/enesgul23/scientific-figure-skills},
  license = {MIT}
}
```

## License

MIT License. See [LICENSE](LICENSE).
