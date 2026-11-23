# MiTeX — LaTeX Math in Typst

**Package**: `@preview/mitex:0.2.7`
**Category**: Math

## Description

LaTeX math support for Typst powered by Rust and WASM. Convert LaTeX equations to Typst content directly.

## Usage in Touying Slides

> **Important**: Always use raw content (backticks) instead of strings to avoid complex escape sequences.

```typst
#import "@preview/mitex:0.2.7": *

// Inline LaTeX — use backticks, NOT strings
#mi(`e^{i\pi} + 1 = 0`)        // ✅ correct
// #mi("e^{i\\pi} + 1 = 0")    // ❌ avoid — requires double backslash escaping

// Block LaTeX
#mitex(`\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}`)

// Convert to Typst string
#mitex-convert(`\alpha x`)
```

## Functions

| Function | Usage |
|----------|-------|
| `mi(...)` | Inline LaTeX equation |
| `mitex(...)` / `mimath(...)` | Block LaTeX equation |
| `mitext(...)` | LaTeX text mode |
| `mitex-convert(...)` | Convert LaTeX to Typst string |

> **Tip**: All functions accept raw content (`` `...` ``). This avoids the need to double-escape backslashes in LaTeX commands.
