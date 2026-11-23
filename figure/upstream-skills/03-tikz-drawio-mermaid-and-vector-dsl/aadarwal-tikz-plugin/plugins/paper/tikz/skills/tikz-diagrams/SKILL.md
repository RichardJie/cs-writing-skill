---
name: tikz-diagrams
description: Use when authoring TikZ figures in LaTeX — geometric diagrams, flowcharts, graphs, circuit-like figures, anything drawn with \draw/\node/\path. Covers the coordinate system, path syntax (-- to arc), node positioning, common libraries (arrows.meta, positioning, calc, shapes), the patterns that keep diagrams maintainable, plus publication-quality standards (consistent arrowheads, computed-not-eyeballed coordinates, label clearance) and a pre-flight figure audit checklist.
---

# TikZ diagrams

TikZ is the dominant LaTeX drawing library. Verbose but precise — for figures where you need exact placement, math-perfect coordinates, or LaTeX-rendered labels, it beats raster tools.

## Minimum file

```latex
\documentclass[tikz, border=2mm]{standalone}
\usetikzlibrary{arrows.meta, positioning, calc, shapes.geometric}

\begin{document}
\begin{tikzpicture}
  \node[circle, draw] (a) at (0,0) {A};
  \node[circle, draw, right=2cm of a] (b) {B};
  \draw[-Stealth] (a) -- (b);
\end{tikzpicture}
\end{document}
```

`\documentclass{standalone}` produces a one-figure PDF with tight cropping — ideal for inclusion in papers or beamer slides via `\includegraphics`.

## Coordinate system

```
\draw (0,0) -- (3,2);             % cartesian
\draw (0:1) -- (60:1) -- (120:1); % polar (angle:radius)
\draw (a) -- (b);                 % named nodes
\draw (a.east) -- (b.west);       % anchor points
```

Default unit is 1cm. Override with `[x=0.5cm, y=0.5cm]` on the `tikzpicture` or globally.

## Paths

```latex
\draw[options] (start) -- (mid) -- (end);     % straight segments
\draw (a) to[bend left=30] (b);               % curved
\draw (a) arc (start_angle:end_angle:radius); % circular arc
\draw (0,0) circle (1cm);                     % full circle (radius)
\draw (0,0) rectangle (2,1);                  % rectangle (opposite corner)
\fill[blue!30] (0,0) circle (0.5);            % filled
\draw[fill=red!30] ...                        % drawn AND filled
```

`->` arrow, `<-` reverse, `<->` both, `-Stealth` for arrowtip style from `arrows.meta`.

Cycle:
```latex
\draw (0,0) -- (1,0) -- (1,1) -- cycle;       % closes the path
```

## Nodes

```latex
\node[options] (name) at (x,y) {Content};
\node[circle, draw, fill=blue!20, minimum size=1cm] (a) at (0,0) {$\alpha$};
```

Common node options:
- Shape: `circle`, `rectangle`, `diamond` (from `shapes.geometric`), `ellipse`.
- `draw` — draw border. `fill=color` — fill. `text=color` — text color.
- `minimum size=`, `minimum width=`, `minimum height=`.
- `inner sep=` — padding inside border. `outer sep=` — gap before path edges connect.
- `rounded corners`.

## Positioning library

```latex
\usetikzlibrary{positioning}

\node (a) at (0,0) {A};
\node[right=2cm of a] (b) {B};        % 2cm right of a
\node[below right=1cm and 2cm of a] (c) {C};  % vertical, horizontal
\node[above=of a] (d) {D};            % default distance
```

Far more readable than computing absolute coordinates.

## calc library — coordinate arithmetic

```latex
\usetikzlibrary{calc}

\coordinate (mid) at ($(a)!0.5!(b)$);                 % midpoint
\coordinate (third) at ($(a)!0.333!(b)$);             % 1/3 of way
\coordinate (perp) at ($(a)!1cm!90:(b)$);             % perpendicular
\coordinate (sum) at ($(a) + (b) - (origin)$);        % vector arithmetic
```

The `$...$` here is *not* math mode — it's calc syntax. Critical for parametric figures.

## Styles — define once, reuse

```latex
\begin{tikzpicture}[
  every node/.style={font=\small},
  state/.style={circle, draw, minimum size=8mm},
  edge/.style={-Stealth, thick},
]
  \node[state] (q0) at (0,0) {$q_0$};
  \node[state, right=of q0] (q1) {$q_1$};
  \draw[edge] (q0) -- (q1) node[midway, above] {$a$};
\end{tikzpicture}
```

Reusable styles keep diagrams consistent and editable — change `state` once, update everywhere.

## Labels on edges

```latex
\draw (a) -- (b) node[midway, above] {label};
\draw (a) -- (b) node[pos=0.3, right] {label};
\draw (a) -- (b) node[near start, sloped, above] {label};
```

`midway`, `near start`, `near end`, `at start`, `at end`, or `pos=0..1`.

## Loops with foreach

```latex
\foreach \i in {0,1,2,3,4}
  \node[circle, draw] at (\i, 0) {$\i$};

\foreach \angle/\label in {0/E, 90/N, 180/W, 270/S}
  \node at (\angle:2) {\label};
```

## Publication quality — what separates real figures from slop

1. **All styles top-level.** Every style lives in a `\tikzset` or the picture's option block; zero inline styling repetition. Change one style, restyle the whole figure.
2. **One arrowhead family per document.** `-Stealth` (from `arrows.meta`). Never mix legacy `->` tips with Stealth/Latex in the same paper.
3. **Fonts match the including document.** The standalone preamble mirrors the paper's font/math packages, and a figure is never `\scalebox`/`\resizebox`'d into place — scaled text is the classic slop tell. Control size inside the picture.
4. **Relative placement everywhere.** `positioning`, named nodes, `calc`. Absolute coordinates only for a small number of deliberate anchors.
5. **Math accuracy.** Never hardcode a coordinate that should lie on a curve — compute it with `\pgfmathsetmacro` from the same expression that draws the curve. Intersections are solved (algebraically, or with the `intersections` library), never eyeballed. Marked points, dashed reference lines, and tangents all derive from the math:
   ```latex
   \pgfmathsetmacro{\ya}{exp(-\xa*\xa)}    % same formula as the curve
   \draw[dashed] (\xa, 0) -- (\xa, \ya);   % lands exactly ON the curve
   ```
6. **Semantic line styles**, used consistently: solid = real/observed; dashed = hypothetical/counterfactual/reference.
7. **Label clearance.** Labels never overlap curves, lines, or other labels; keep ≥ 0.2 units of clearance; stagger when stacking.

## Pre-flight audit checklist

Verify on the *rendered* output before calling a figure done:

- Axes extend slightly past the data.
- Dashed reference lines terminate exactly ON the curve — not short, not through.
- Arrowheads consistent: one family, one size.
- Edge labels fit their gaps.
- Nothing clipped by the standalone crop.
- Fonts at target size after inclusion — no scaling applied.

**Document integration**: `\usetikzlibrary{external}` + `\tikzexternalize[prefix=figures/]` caches compiled figures and speeds real-document builds, but is incompatible with the `standalone` class (pgf issue #932) — it's a document-side concern, not for iteration.

## Common gotchas

- **Compile errors point to wrong line** because TikZ expands inside. Read context, not just the line number.
- **`tikzpicture` inside an `align*`** environment will sometimes break — wrap in `\begin{center}...\end{center}` instead, or use `\vcenter`.
- **Forgotten semicolon** at the end of a `\draw` is the #1 compile failure.
- **`-` in node names** — use underscores or camelCase. `node (a-1)` confuses some libraries.
- **Coordinates outside `\draw`** — `\path (0,0) coordinate (origin);` defines without drawing.
- **Standalone class crop** — `border=2mm` adds 2mm whitespace; use `border=0pt` for tight, `border=5mm` for slides.

## When to choose TikZ over alternatives

- **Beats Inkscape/Illustrator** when the figure has math labels, when you want it source-controlled, when it lives next to LaTeX equations that need to match.
- **Beats matplotlib** for non-data figures (concept diagrams, geometric proofs, state machines).
- **Loses to** raster tools for organic illustration, photo overlays, or any figure where pixel-pushing is the point.

Related: [[tikz-cd]] for commutative diagrams, [[pgfplots]] for plots.
