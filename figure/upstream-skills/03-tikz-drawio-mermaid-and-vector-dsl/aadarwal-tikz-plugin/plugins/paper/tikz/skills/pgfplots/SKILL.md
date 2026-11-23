---
name: pgfplots
description: Use when authoring scientific plots in LaTeX with pgfplots — 2D function plots, scatter from CSV/inline data, error bars, multi-axis plots, log scales, contour plots, 3D surfaces. Covers axis options, plot styles, legends, the difference between \addplot and \addplot+, publication sizing (axis width, never \resizebox), groupplots panel figures, cycle list / ColorBrewer styling, and the tradeoffs vs matplotlib.
---

# pgfplots

pgfplots is the standard LaTeX library for math-quality plots that compose with TikZ and use LaTeX fonts/labels. Slower to render than matplotlib but produces vector PDFs whose typography matches the surrounding document exactly.

## Minimum file

```latex
\documentclass[tikz, border=2mm]{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}     % pin to a known-good version

\begin{document}
\begin{tikzpicture}
\begin{axis}[
  xlabel={$x$}, ylabel={$f(x)$},
  domain=-3:3, samples=100,
  grid=both,
]
  \addplot[blue, thick] {x^2};
  \addplot[red,  thick] {sin(deg(x))};
\end{axis}
\end{tikzpicture}
\end{document}
```

Pin `\pgfplotsset{compat=1.18}` (or whatever current version is). Without it, behavior changes silently across TeX Live releases.

## Function plots

```latex
\addplot[blue, thick] {x^2};                       % implicit domain from axis
\addplot[domain=0:2*pi, samples=200] {sin(deg(x))};% override
\addplot[red, dashed] {exp(-x^2)};
```

Math functions are pgfplots-flavored, not C: `sin/cos/tan` take **degrees** by default. Use `deg(x)` to convert radians, or `sin(rad(x))` — both work.

Useful math:
- `exp(x)`, `ln(x)`, `log10(x)`, `sqrt(x)`, `abs(x)`
- `^` for powers (also `pow(a,b)`)
- `pi`, `e` constants

## Data plots

From CSV:
```latex
\addplot[mark=*, mark size=1pt] table[x=time, y=value, col sep=comma] {data.csv};
```

Inline data:
```latex
\addplot+[only marks] coordinates {
  (1, 2.1)
  (2, 3.7)
  (3, 5.0)
  (4, 7.2)
};
```

`\addplot+` (with `+`) inherits a colored mark/line cycle automatically — useful for "give me distinguishable series" without picking colors manually.

## Axis options — the cheat sheet

```latex
\begin{axis}[
  xlabel={Time (s)},
  ylabel={Voltage (V)},
  title={Capacitor discharge},
  xmin=0, xmax=10,
  ymin=0, ymax=5,
  xtick={0, 2, 4, 6, 8, 10},
  ytick={0, 1, 2, 3, 4, 5},
  minor tick num=4,            % minor ticks between majors
  grid=major,                  % or both, or minor
  legend pos=north east,       % nw, ne, sw, se, outer north east
  legend cell align={left},
  width=10cm, height=6cm,      % overrides default size
  axis lines=middle,           % cartesian-style axes through origin
  enlargelimits=false,         % tight to data
]
```

## Legends

```latex
\addplot {x^2}; \addlegendentry{$x^2$}
\legend{$x^2$, $x^3$}    % or bulk — entries pair with each \addplot in order
```

## Log scales

```latex
\begin{semilogyaxis}[...]    % y log, x linear
\begin{semilogxaxis}[...]    % x log, y linear
\begin{loglogaxis}[...]      % both log
```

Or `\begin{axis}[ymode=log]`.

## Error bars

```latex
\addplot+[
  error bars/.cd,
  y dir=both, y explicit,
] table[x=t, y=mean, y error=std, col sep=comma] {data.csv};
```

`y dir` can be `plus`, `minus`, or `both`. `y explicit` reads from the named column.

## 3D plots

Surfaces:
```latex
\begin{axis}[view={60}{30}]   % azimuth, elevation degrees
  \addplot3[surf, samples=30, domain=-2:2, y domain=-2:2]
    {x*y*exp(-x^2 - y^2)};
\end{axis}
```

Parametric 3D curves:
```latex
\addplot3[
  variable=t, samples=200, samples y=0,
  domain=0:6*pi,
] ({cos(deg(t))}, {sin(deg(t))}, {t/(6*pi)});
```

3D surface styles: `surf` (lit), `mesh` (wireframe), `surf, shader=interp` (smooth).

## Contour plots

```latex
\addplot3[
  contour gnuplot={number=15},
  samples=40, domain=-2:2, y domain=-2:2,
] {x*y};
```

Requires `gnuplot` installed and `\write18` (or `-shell-escape` at compile time).

## Tikz-style customization

Because pgfplots is built on TikZ, all TikZ tricks work inside an axis:

```latex
\begin{axis}[...]
  \addplot {x^2};
  \node[anchor=south] at (axis cs:1, 1.2) {\small label};
  \draw[red, dashed] (axis cs:1, 0) -- (axis cs:1, 1);
\end{axis}
```

`(axis cs:x, y)` is the data coordinate system. Use it for annotations that should move with the data.

## Publication plots

- **Size via the axis, never `\resizebox`.** `width=0.8\linewidth` (or the venue's column width) keeps fonts at document size; scaled text is the classic slop tell.
- **Panel figures: `groupplots`** — shared axis labels, ticks only on the bottom row / left column:
  ```latex
  \usepgfplotslibrary{groupplots}
  \begin{groupplot}[group style={group size=2 by 2,
      x descriptions at=edge bottom, y descriptions at=edge left,
      horizontal sep=1em, vertical sep=1em}, width=0.48\linewidth]
    \nextgroupplot \addplot {x};   \nextgroupplot \addplot {x^2};
    \nextgroupplot \addplot {x^3}; \nextgroupplot \addplot {exp(x)};
  \end{groupplot}
  ```
- **One `cycle list` for the whole paper** — define it once in the preamble so series styling matches across every plot. ColorBrewer palettes via the `colorbrewer` library:
  ```latex
  \usepgfplotslibrary{colorbrewer}
  \pgfplotsset{cycle list/Dark2}
  ```
- **Real data lives in files.** `\addplot table {data.dat};` over inlined `coordinates` — regenerable, diffable, keeps the figure source readable.

## Gotchas

- **`samples=` too low** → spiky curves. 50–100 for smooth single curves; 200+ for high-frequency content.
- **"Dimension too large"** — TeX hit its ~16384pt dimension cap: domain too wide, or a divide-by-zero/pole in the expression. Restrict `domain=`, raise `samples=`; for poles, `restrict y to domain=`.
- **Trig in radians** — `sin(x)` uses degrees. `sin(deg(x))` if `x` is in radians.
- **Slow compile** — pgfplots is slow on big datasets. For > a few thousand points: pre-rasterize (`unbounded coords=jump`), use `each nth point=N`, or render in matplotlib and `\includegraphics` the PNG.
- **`legend pos=outer north east`** — places legend outside the axis box; needs `enlarge x limits` adjustments sometimes.
- **Mixing `axis cs:` and absolute `(x, y)`** — `(2, 1)` is *centimeters* inside an axis. `(axis cs:2, 1)` is *data*. Always be explicit.
- **Negative powers in labels** — `$10^{-3}$` is fine; raw `10e-3` from CSV needs `xticklabel style={/pgf/number format/.cd, sci}` or manual ticks.

## When to choose pgfplots vs matplotlib

**pgfplots wins**: the plot lives in a LaTeX document (typography consistency), math figures (analytic functions, geometric annotations), print-quality vector PDF.

**matplotlib wins**: pandas pipelines you already have, large datasets (> 10k points), fast iteration, statistical plots (seaborn/plotnine). For matplotlib output destined for LaTeX, use the `pgf` backend (`matplotlib.use("pgf")`) — typography then matches.

Related: [[tikz-diagrams]], [[tikz-cd]].
