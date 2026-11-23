# Useful Packages for Touying Slides

Curated collection of Typst packages commonly used in Touying presentations. Each package directory contains:
- `demo.typ` — Working example with Touying simple theme (16:9)
- `README.md` — Package documentation and usage guide

> **For AI**: Use `index.json` for programmatic lookup. This README is for human browsing.

## Contents

- [Package Categories](#package-categories)
- [Quick Reference](#quick-reference)
- [Usage Pattern](#usage-pattern)

---

## Package Categories

### Heading & Numbering

| Package | Version | Description |
|---------|---------|-------------|
| **[numbly](./numbly/)** | 0.1.0 | Custom heading numbering formats per level |

### Math & Theorems

| Package | Version | Description |
|---------|---------|-------------|
| **[theorion](./theorion/)** | 0.6.0 | Theorem, definition, lemma, proof environments |
| **[mitex](./mitex/)** | 0.2.7 | LaTeX math equations in Typst (WASM) |

### Code Display

| Package | Version | Description |
|---------|---------|-------------|
| **[lovelace](./lovelace/)** | 0.3.1 | Pseudocode with arbitrary keywords |
| **[codly](./codly/)** | 1.3.0 | Beautiful code blocks with line numbers and annotations |
| **[zebraw](./zebraw/)** | 0.6.3 | Lightweight code blocks with line highlighting (zebra-striped) |

### Lists & Tables

| Package | Version | Description |
|---------|---------|-------------|
| **[cheq](./cheq/)** | 0.4.0 | Markdown-like checklists (`[x]`, `[ ]`, `[/]`, `[-]`) |
| **[tablem](./tablem/)** | 0.3.0 | Markdown-like tables, three-line-table preset |

### Layout & Annotation

| Package | Version | Description |
|---------|---------|-------------|
| **[pinit](./pinit/)** | 0.2.2 | Relative positioning, text highlighting, annotations |

### Data Visualization

| Package | Version | Description |
|---------|---------|-------------|
| **[lilaq](./lilaq/)** | 0.6.0 | Mature Typst-native plotting; default for existing SeaSlides statistical chart templates |
| **[gribouille](./gribouille/)** | 0.6.0 | Layered Grammar of Graphics API for mapped aesthetics and statistical transformations |

Use Lilaq for the existing SeaSlides line, bar, scatter, area, and distribution
templates or when direct mark/axis control is clearest. Use Gribouille when the
plot is naturally expressed as data mappings plus layers, statistics, scales,
and themes. Gribouille is in active development, so pin the catalog version and
read its current documentation before authoring.

### Declarative Diagrams

| Package | Version | Description |
|---------|---------|-------------|
| **[merman](./merman/)** | 0.1.0 | Mermaid source rendered to SVG during Typst compilation via a bundled WASM plugin |

### Utility

| Package | Version | Description |
|---------|---------|-------------|
| **[tiaoma](./tiaoma/)** | 0.3.0 | QR codes and barcodes (50+ types) |
| **[cuti](./cuti/)** | 0.4.0 | Fake bold/italic for CJK fonts |

---

## Quick Reference

```
Need what?
├── Custom heading numbering → numbly
├── Theorem/proof environments → theorion
├── LaTeX equations → mitex
├── Pseudocode → lovelace
├── Beautiful code blocks → codly or zebraw
├── Checklists → cheq
├── Markdown tables → tablem
├── Text annotations / arrows → pinit
├── Standard statistical charts → lilaq
├── Layered grammar-of-graphics plots → gribouille
├── Mermaid diagrams → merman
├── QR codes / barcodes → tiaoma
└── CJK fake bold → cuti
```

---

## Usage Pattern

All demos follow the same structure as `${SKILL_DIR}/templates/charts/`:

```typst
#import "@preview/touying:0.7.4": *
#import themes.simple: *
#import "@preview/<package>:<version>": *

#show: simple-theme.with(aspect-ratio: "16-9")

#set text(size: 18pt)

== Slide Title

// Package usage here
```
