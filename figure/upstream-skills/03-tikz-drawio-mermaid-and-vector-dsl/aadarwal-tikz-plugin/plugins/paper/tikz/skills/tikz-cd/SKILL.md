---
name: tikz-cd
description: Use when drawing commutative diagrams in LaTeX (category theory, algebraic topology, abstract algebra). Covers the tikz-cd package syntax — matrix-style row/column placement, arrow shortcuts (rar/lar/dar/uar), bent and curved arrows, double/dashed arrows, labels with above/below/swap, and the common subtleties (column gaps, two-line arrow labels, isomorphism marks). Mentions quiver (q.uiver.app), the visual editor that round-trips tikz-cd.
---

# tikz-cd — commutative diagrams

`tikz-cd` is the standard package for commutative diagrams. Way more ergonomic than rolling your own with bare TikZ. Imports:

```latex
\usepackage{tikz-cd}
% or with TikZ already loaded:
\usetikzlibrary{cd}
```

## The matrix syntax

Nodes go in a matrix; arrows are declared per cell.

```latex
\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, "k"'] & D
\end{tikzcd}
```

Renders:

```
A ──f──→ B
│        │
g        h
│        │
↓        ↓
C ──k──→ D
```

- Rows separated by `\\`, columns by `&` (like a LaTeX `array`).
- Each `\arrow[direction, "label"]` is attached to the node it follows.
- Directions: `r` right, `l` left, `u` up, `d` down. Combine: `dr` down-right, `urr` up-right-right (across two columns).
- Label after a direction: `\arrow[r, "f"]`.
- Trailing `'` (apostrophe) on a label = below/swap side: `\arrow[d, "g"']`.

## Direction shortcuts

`\rar`, `\lar`, `\dar`, `\uar` are aliases for `\arrow[r], \arrow[l], \arrow[d], \arrow[u]`:

```latex
\begin{tikzcd}
A \rar{f} \dar{g} & B \dar{h} \\
C \rar[swap]{k} & D
\end{tikzcd}
```

Cleaner for simple diagrams; verbose `\arrow[...]` form needed for advanced options.

## Arrow styles

```latex
\arrow[r, "f"]                       % standard
\arrow[r, "f", dashed]               % dashed
\arrow[r, "f", hook]                 % hooked (monomorphism / inclusion)
\arrow[r, "f", two heads]            % epimorphism
\arrow[r, "\sim", "f"']              % above-label "~" (iso), below-label "f"
\arrow[r, Rightarrow, "f"]           % double arrow
\arrow[r, leftrightarrow, "f"]       % bidirectional
\arrow[r, dotted]
\arrow[r, no head]                   % undirected line
```

For a "$\cong$" or "$\simeq$" iso marker, double-label trick:
```latex
\arrow[r, "f", "\sim"']
```
puts `f` on top and `~` on the bottom.

## Bending and curving

```latex
\arrow[r, bend left, "f"]
\arrow[r, bend right=30, "g"']
\arrow[loop right, "h"]              % self-loop (no direction key — loop returns to source)
\arrow[loop above, "h"]              % loop positioned above
```

Common pattern: two arrows between same pair of objects, one bent each way (for natural transformations etc.):
```latex
A \arrow[r, bend left, "F"] \arrow[r, bend right, "G"'] & B
```

## Multi-column / row arrows

```latex
\arrow[rr, "f"]            % two columns right
\arrow[ddr, "g"]           % down, down, right
```

Useful for diagonal "skew" arrows in 3×3 diagrams.

## Two-line labels

```latex
\arrow[r, "{f \\ \text{iso}}"]
```

The `{...}` groups; `\\` inside it gives a two-line label. Alternative: use `\substack`:
```latex
\arrow[r, "\substack{f \\ \text{iso}}"]
```

## Spacing and sizing

```latex
\begin{tikzcd}[column sep=large, row sep=small]
  ...
\end{tikzcd}
```

Sizes: `tiny`, `small`, `scriptsize`, `normal`, `large`, `huge`, or explicit `column sep=2em`.

When labels overlap arrows, increase the relevant sep, or use `description` placement:
```latex
\arrow[r, "f"description]   % places label *on* the arrow (with background)
```

## Common diagrams — patterns to copy

**Pullback / pushout**:
```latex
\begin{tikzcd}
P \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & X \arrow[d, "f"] \\
Y \arrow[r, "g"'] & Z
\end{tikzcd}
```
The phantom arrow places `\lrcorner` to mark the corner. For a pushout, mark from the bottom-right object instead: `\arrow[ul, phantom, "\ulcorner", very near start]`.

**Exact sequence**:
```latex
\begin{tikzcd}
0 \rar & A \rar{f} & B \rar{g} & C \rar & 0
\end{tikzcd}
```

**Square with diagonal**:
```latex
\begin{tikzcd}
A \rar \dar \arrow[dr, "h" description] & B \dar \\
C \rar & D
\end{tikzcd}
```

## Gotchas

- **Label apostrophe vs prime** — `"f'"` is "label f with a prime"; `"f"'` is "label f, below the arrow." Subtle.
- **Empty cells** — leave blank between `&` separators; tikz-cd handles spacing.
- **Phantom arrows** for placement-only — `\arrow[r, phantom, "\bullet"]` draws nothing but places the label.
- **Equality arrows** — the built-in style is `\arrow[r, equal]` (singular; `equals` is not a key). Fallback on old versions: `\arrow[r, double, no head]`.
- **`description` placement** stacks badly with multiple labels on the same arrow — use it sparingly.

## Tooling

[quiver](https://q.uiver.app) is a visual editor that round-trips tikz-cd: sketch the diagram by hand, paste the exported code. Its output style is a sane canonical format — useful when a diagram is too fiddly to write blind.

Related: [[tikz-diagrams]] for general TikZ, [[pgfplots]] for plots.
