# Biomedical Figure Production Skill

A personal Codex skill for reproducible biomedical figures, scientific illustrations, mechanism schematics, graphical abstracts, and submission-ready export packages.

## What it integrates

- Python plotting: Matplotlib, Seaborn, SciPy, Plotnine, and cnsplots
- R plotting: ggplot2, ComplexHeatmap, patchwork, survival-focused and ROC/forest-plot tooling
- Illustration workflow: generated non-data components plus deterministic vector labels and evidence coding
- Statistical review: design-aware checks before significance marks are accepted
- Origin/OriginPro-compatible export guidance
- PNG, TIFF, SVG, and PDF quality-control checks

The workflow distinguishes measured data, statistical estimates, computational inference, cross-model extrapolation, and hypothesis. Generated artwork must never be presented as experimental evidence.

## Install the skill

Copy the `biomedical-figure-production` directory into your Codex skills directory and restart Codex. The Python and R setup scripts create project-local environments; they do not place environments inside the skill folder.

## Quick checks

```powershell
& '<venv>\Scripts\python.exe' .\biomedical-figure-production\scripts\check_environment.py
& '<venv>\Scripts\python.exe' .\biomedical-figure-production\scripts\smoke_test.py --output-dir .\test-output
& '<venv>\Scripts\python.exe' .\biomedical-figure-production\scripts\validate_figure.py .\test-output\*.png .\test-output\*.tiff .\test-output\*.svg
```

The smoke-test data are synthetic and are labelled as such.

## Scope and limitations

This repository provides workflow instructions and validation helpers. It does not verify biological truth automatically, replace statistical review, or authorize alteration of experimental images. Always follow the target journal's current artwork and generative-AI policies.

## License

MIT. Third-party Python/R packages and Codex skills retain their own licenses and are not vendored here.

