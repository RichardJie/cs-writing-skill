# Prompt Templates

These prompts are written for an agent working inside a paper-reading
workspace that has `papers/`, `slides/`, `analysis/`, and `skills/`.

## Single-paper deck

```text
Read papers/<paper>.pdf and create a detailed paper-reading Beamer deck.
Use the paper-beamer-deck skill.
Use risk-targeted visual QA.
Run deterministic figure extraction first and consume build/figures/<paper>/figures.json.
Generate quality_report.md before finishing.
```

## High-stakes or defense-style deck

```text
Read papers/<paper>.pdf and build a presentation-ready Beamer deck for a
high-stakes research talk. Use incremental visual QA. Be especially careful
with result interpretation, limitations, figure attribution, source
traceability, and final quality checks.
```

## Figure extraction QA only

```text
Run figure extraction for papers/<paper>.pdf into build/figures/<paper>.
Inspect the preview, explain any needs_manual_review records, and prepare
figure_overrides.json if reliable manual bboxes are needed.
Do not generate slides yet.
```

## Repair an existing deck

```text
Review slides/<deck>/ for compilation, log-gate, source-traceability, figure
usage, and visual-QA issues. Fix broken slides by splitting or redesigning,
not by shrinking everything. Regenerate quality_report.md before finishing.
```

## Multi-paper research-gap analysis

```text
Analyze the papers in papers/ and produce a research-gap analysis.
Use memo+deck mode unless the LaTeX toolchain is unavailable.
Ground claims in the papers, grade gaps by evidence strength, and avoid
overclaiming novelty.
```

## Memo-only gap analysis

```text
Analyze the papers in papers/ and produce a memo-only research-gap analysis.
Do not build a Beamer deck. Prioritize a careful paper matrix, graded gaps,
limitations, and concrete next research questions.
```
