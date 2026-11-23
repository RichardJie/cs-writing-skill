# Copyright And Repository Hygiene

This repository is a reusable skills library. It should not contain copied
paper PDFs, copyrighted paper figures, or screenshots from papers.

## Repository policy

- Do not commit source paper PDFs.
- Do not commit extracted figures from copyrighted papers.
- Do not commit screenshots from copyrighted papers.
- Do not add paper text beyond short, fair-use snippets needed for examples.
- Keep examples synthetic, original, or explicitly permissively licensed.
- Keep generated deck outputs in paper-reading workspaces, not in this skills
  repository.

## Workspace policy

It is normal for a local workspace to contain source PDFs and extracted figures
for personal research use. Treat those workspaces as local project material,
not reusable library content.

When a deck reuses a paper figure, label it in the slide or notes as:

```text
From the paper.
```

or:

```text
Adapted from the paper.
```

The label is attribution and traceability, not a license grant. Check the paper
publisher's terms before redistributing the generated deck.

## Examples and tests

Tests generate synthetic mini PDFs from shapes and short original text. The
examples gallery is synthetic-only. This keeps the repository safe to clone,
fork, publish, and test.

## Automated checks

The repo-level hygiene check rejects tracked PDFs and likely-large binary files:

```bash
python3 scripts/check_repo_hygiene.py
```

This is a guardrail, not legal advice.
