# Scientific Figures & UI Design De-AI Guide (科研绘图与前端界面去 AI 味)

Eliminate glowing sci-fi academic diagram slop (赛博发光大脑、霓虹伪 3D 方块、乱码位图) and vibe-coded SaaS UI slop (蓝紫渐变、等宽三列图标卡片、泛滥魔法星标). Build publication-grade **Nature / Science / NeurIPS** vector figures and intentional, human-crafted interfaces.

> **Module Cross-Navigation ([../SKILL.md](../SKILL.md)):** Pair Part I (Scientific Figures) with [../paper-boundaries.md](../paper-boundaries.md) and [academic-prose-and-rebuttal.md](academic-prose-and-rebuttal.md) so Figure 1 visually spotlights your core contribution. For photographic/editorial AI image generation, see [visual-image-de-ai.md](visual-image-de-ai.md).

---

# Part I: Scientific & Academic Figures De-AI (科研配图与顶会架构图)

## 1. Why AI-Generated Academic Figures Trigger Instant Reviewer Distrust

When authors paste raw outputs from Midjourney, DALL-E, or `gpt-image-1` into a manuscript, reviewers spot the tell within two seconds—and immediately question the rigor of the underlying experiments. Raster image generators optimize for **visual drama**, whereas scientific figures exist for **topological truth, dimensional precision, and typographic legibility**.

### Publisher & Venue Policy Matrix

| Venue / Publisher | Policy on Generative AI in Figures | Mandatory Workflow Rule |
|-------------------|------------------------------------|-------------------------|
| **Science (AAAS)** | Prohibits AI generation or editing of illustrative figures and data images without explicit prior editor permission | Build 100% of schematics and plots deterministically in vector/plotting tools (`Illustrator`, `TikZ`, `R`, `matplotlib`). |
| **Nature / Springer Nature** | Strictly bans AI in primary data (blots, microscopy, clinical); AI-assisted schematics require verification + explicit disclosure in Methods/Legend | Never submit raw AI pixels; redraw every element as clean editable vectors and verify every biological/mathematical arrow. |
| **Cell Press / Elsevier** | Bans generative AI in experimental data; requires transparent caption disclosure for graphical abstracts or conceptual schematics | Prefer deterministic scientific libraries (`BioRender`, `Inkscape`, `Illustrator`) over raster diffusion art. |
| **NeurIPS / ICML / ICLR / CVPR / ACL / IEEE** | Reviewers penalize "blog-post sci-fi slop," misspelled module names, and unverified tensor pathways as signs of rushed or shallow work | Figure 1 and architecture diagrams must be crisp `.pdf` vectors with exact LaTeX math parity ($B \times T \times d$). |

---

## 2. Diagnostic Catalog of Scientific Figure AI Tells (`SF1–SF10`)

| ID | Academic Slop Tell (CN / EN) | Visual Symptoms | Fix |
|----|------------------------------|-----------------|-----|
| **SF1** | **Glowing Sci-Fi Brain / Robot Cliché** (`发光赛博大脑与科幻堆砌`) | Glowing blue synapses, robot hands touching holograms, starry space backgrounds inside an ML or systems diagram | Delete 100% of metaphorical sci-fi clip art. Represent models strictly via input data samples, tensor blocks, mathematical operators ($\oplus, \otimes$), and output predictions. |
| **SF2** | **Neon Isometric 3D Cubes** (`霓虹伪3D等轴测方块与重阴影`) | Glossy dark-mode 3D blocks with cyan/magenta neon edges, bevels, and heavy drop shadows encoding zero information | Flatten to **2D orthographic blocks** (or restrained flat 2.5D tensor slabs when showing `[C, H, W]` volume depth) on a pure `#FFFFFF` background. |
| **SF3** | **Raster Gibberish & Fake Math** (`文字乱码与变形公式`) | Labels reading `"Atetntion"`, `"Encdoer"`, melted Greek letters ($\alpha, \mathcal{L}$), inconsistent font weights inside boxes | Strip all AI-rendered text. Typeset every label manually in `Arial`/`Helvetica` (`6–8 pt`) and every equation via native LaTeX (`TikZ`, `LaTeXiT`, SVG math). |
| **SF4** | **Topological & Dimension Hallucination** (`拓扑连线幻觉与维度失配`) | Arrows pointing into empty space, skip connections with no target operator, 5 input tokens turning into 3 output nodes arbitrarily | Trace every arrow from source tensor to target operation. Annotate explicit tensor shapes (`[B, N, D]`) along transitions. |
| **SF5** | **Bitmap / JPEG Lock-In** (`位图锯齿与压缩伪影`) | Fuzzy edges and JPEG mosquito noise around text when zooming PDF to `400%` | Export exclusively as vector `.pdf` (for `pdflatex`/`xelatex`), `.eps`, or `.svg`—never rasterize line art or text layers. |
| **SF6** | **Warm Cream Background & Comic Strokes** (`GPT暖黄底色与卡通粗黑边`) | `#FDF6E3` yellow-cream rectangle visibly clashing against white journal paper, paired with thick `3pt` cartoon outlines | Force `#FFFFFF` (or transparent) artboard background; standardize structural borders to crisp `0.6–1.0 pt` dark slate (`#1E293B`). |
| **SF7** | **Decorative Icon Pollution** (`无意义小图标泛滥`) | Putting a tiny gear, magnifying glass, shield, rocket, or lightbulb inside every algorithm box | Use icons **only** for concrete domain entities (camera sensor, microphone, protein receptor, user prompt); use clean typography for abstract math modules. |
| **SF8** | **Rainbow / `jet` & Red-Green Traps** (`彩虹色阶与红绿色盲灾难`) | `jet`/rainbow heatmaps creating false perceptual boundaries; pure `#FF0000` vs. `#00FF00` curves | Use `viridis`, `cividis`, or `magma` for sequential heatmaps, `RdBu_r` for zero-centered diverging maps, and **Okabe-Ito** for categorical curves. |
| **SF9** | **Raw Matplotlib / Excel Defaults** (`未修饰默认统计图`) | Four-sided black box frame, tiny shrunken `4pt` tick text, distant legend box forcing eye-jumping, bare bar charts hiding variance | `despine()` top/right axes, size artboard to exact column width before plotting, direct-label curves, plot individual seed dots or 95% CI bands. |
| **SF10** | **Equal-Weight Kitchen-Sink Figure 1** (`无主次流水账架构图`) | Giving standard data loading, frozen ResNet/ViT backbones, and your novel module identical saturated colors and box sizes | Apply the **Press-Conference Principle ([`paper-boundaries`](../paper-boundaries.md))**: mute standard/frozen scaffolding in neutral grey (`#F1F5F9` fill, `#64748B` dashed border) so your **core contribution** commands immediate focal contrast. |

---

## 3. Nature / Science / NeurIPS Clean Vector Specification Standards

### 3.1 Exact Artboard & Column Geometry (Design at 1:1 Scale)

**Never** draw a figure on a `1920×1080` slide canvas and shrink it with `\includegraphics[width=\columnwidth]`. Shrinking scales `14 pt` labels down to illegible `4.5 pt` micro-text and turns `0.75 pt` lines into invisible `0.2 pt` hairlines. Set your Illustrator, Figma, Inkscape, or `matplotlib` canvas to **exact published millimeter/inch dimensions** at the start:

| Venue | Single Column Width | 1.5 Column Width | Full / Double Column Width | Max Page Height |
|-------|---------------------|------------------|----------------------------|-----------------|
| **Nature / Nature Portfolio** | `89 mm` (`3.50 in`) | `120–136 mm` (`4.72–5.35 in`) | `183 mm` (`7.20 in`) | `247 mm` (`9.72 in`) |
| **Science (AAAS)** | `55 mm` (1-col of 3) / `90 mm` | `120 mm` (`4.72 in`) | `184 mm` (`7.24 in`) | `230 mm` (`9.05 in`) |
| **NeurIPS / ICLR** (1-col text) | `67 mm` (`2.65 in` half-fig) | `100 mm` (`3.94 in`) | `139.7 mm` (`5.50 in` `\textwidth`) | `200 mm` (`7.87 in`) |
| **CVPR / ICCV / ACL / IEEE** | `83 mm` (`3.27 in`) | — | `174–178 mm` (`6.85–7.00 in`) | `225 mm` (`8.85 in`) |

### 3.2 Typography, Mathematical Parity & Stroke Hierarchy

1. **Font Family:** `Arial`, `Helvetica`, or `Helvetica Neue` throughout all panels. Never mix 3 font families (`Calibri` + `Comic Sans` + `Times`) in one figure; reserve `Computer Modern` / `Latin Modern Math` strictly for mathematical variables ($x_t, \theta, \mathcal{L}_{\text{KL}}$).
2. **Point Sizes (at 1:1 Final Width):**
   - **Panel Identifiers:** `8 pt Bold` upright lowercase **`a`, `b`, `c`** (*Nature* style) or `(a)`, `(b)` (*IEEE/CVPR* subfigure style). Never exceed `10 pt`.
   - **Module Titles & Axis Labels:** `7 pt` Regular or Medium.
   - **Tick Labels, Legend Entries & Tensor Shapes:** `6 pt` Regular (hard floor: **`5.5 pt`**; anything smaller fails print/PDF review).
3. **Symbol Parity Rule:** If Equation (4) writes $\hat{\mathbf{y}} = f_\theta(\mathbf{h}^{(l)})$, the diagram **must** write $\hat{\mathbf{y}}$ and $\mathbf{h}^{(l)}$—never `y_hat` or `H_l` in plain sans-serif.
4. **Stroke Weights & Geometry:**
   - **Primary Module Outlines:** `0.75 pt – 1.0 pt` in dark slate (`#1E293B` or `#334155`, softer and cleaner than `#000000`).
   - **Data-Flow Arrows & Axes:** `0.6 pt – 0.8 pt` orthogonal (right-angle) connectors with small `4 pt` solid triangular arrowheads (`45°` miter or `2 px` rounded bend). Avoid swooping Bezier spaghetti unless illustrating continuous trajectories.
   - **Grouping / Stage Containers:** `0.5 pt` dashed border (`3 pt` dash, `2 pt` gap) in cool grey (`#94A3B8`) with `#F8FAFC` subtle background tint.
   - **Corner Radius:** `2 px – 4 px` (`0.8–1.5 mm`) technical corners. Avoid giant `20 px` pill-shaped marketing boxes.
   - **Hybrid Resolution:** Keep line art/text 100% vector; embed unavoidable raster crops (microscopy, autonomous driving frames, qualitative image grids) at **`300–600 DPI`** lossless PNG inside the vector container.

### 3.3 Scholarly & Colorblind-Safe HEX Palettes

#### A. Okabe-Ito Universal Palette (Gold Standard for Plots & Multi-Method Comparisons)

Optimized for protanopia, deuteranopia, tritanopia, and monochrome laser printing:

| Role | Color Name | HEX | Recommended Usage |
|------|------------|-----|-------------------|
| **Primary (Ours)** | Vermillion / Red-Orange | `#D55E00` | Our proposed method curve / focal highlight bar |
| **Strong Baseline 1** | Deep Blue | `#0072B2` | Primary competing SOTA baseline |
| **Strong Baseline 2** | Bluish Green / Teal | `#009E73` | Secondary baseline or orthogonal paradigm |
| **Accent / Ablation 1** | Warm Orange | `#E69F00` | Variant A / confidence region highlight |
| **Accent / Ablation 2** | Sky Blue | `#56B4E9` | Variant B / secondary data stream |
| **Accent / Ablation 3** | Reddish Purple | `#CC79A7` | Variant C / auxiliary loss term |
| **Caution Highlight** | Yellow | `#F0E442` | Filled area/marker **only** with dark `#334155` outline (low contrast alone on white) |
| **Scaffolding / Baseline** | Neutral Slate Grey | `#94A3B8` / `#64748B` | Frozen modules, reference gridlines, classical baselines |

#### B. NeurIPS / CVPR Architecture Two-Tone Fill + Stroke System

Never put white text on saturated neon blocks. Pair **high-luminance pastel fills** (`92–96%` lightness) with **saturated dark borders** so `#0F172A` text and LaTeX math remain razor-sharp:

| Semantic Module Role | Fill HEX | Stroke HEX (`0.8 pt`) | Visual Convention |
|----------------------|----------|-----------------------|-------------------|
| **Frozen / Pretrained Backbone** | `#F1F5F9` | `#64748B` (dashed) | Muted visual weight (`❄️` or `Frozen` `5.5pt` tag); never steals focus |
| **Standard Input / Token Stream** | `#EFF6FF` | `#2563EB` (solid) | Calm technical blue for embeddings, encoders, standard layers |
| **Auxiliary / Conditioning Context** | `#F0FDFA` | `#0D9488` (solid) | Muted teal for retrieval memory, geometry priors, or multimodal cues |
| **Core Novel Mechanism (OURS)** | `#FFF7ED` | `#C2410C` (`1.1 pt` solid) | Warm burnt-orange spotlight; visually anchors the paper's press-conference claim |
| **Objective / Loss Computation** | `#FEF2F2` | `#DC2626` (solid) | Crisp crimson accent reserved strictly for $\mathcal{L}_{\text{total}}$ / gradient supervision paths |

---

## 4. Production Workflows: From AI Draft to Publication Vector

### Workflow A: Code-First Deterministic Vectors (`TikZ`, `Typst CeTZ`, `matplotlib`)

Ask LLMs to write **vector source code** rather than raster pixels. Below is a drop-in publication-grade `matplotlib` configuration sized directly to a *Nature* single-column (`89 mm`) figure with Okabe-Ito styling and direct line labeling:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 1. Exact Nature single-column width (89 mm -> 3.504 inches) & editable PDF TrueType/Type42 fonts
MM_TO_INCH = 1.0 / 25.4
mpl.rcParams.update({
    "pdf.fonttype": 42,          # Editable text in Illustrator/Inkscape (never Type 3 bitmaps!)
    "ps.fonttype": 42,
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 7.0,
    "axes.labelsize": 7.0,
    "xtick.labelsize": 6.0,
    "ytick.labelsize": 6.0,
    "axes.linewidth": 0.6,
    "axes.edgecolor": "#334155",
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "axes.spines.top": False,    # Remove boxy AI/default clutter
    "axes.spines.right": False,
})

fig, ax = plt.subplots(figsize=(89 * MM_TO_INCH, 62 * MM_TO_INCH), constrained_layout=True)

tokens = np.array([1, 2, 4, 8, 16, 32])
ours = np.array([74.2, 78.9, 82.4, 85.1, 86.8, 87.6])
baseline_a = np.array([71.0, 74.5, 76.8, 78.1, 78.9, 79.2])
baseline_b = np.array([69.5, 72.1, 74.0, 74.8, 75.1, 75.0])

ax.plot(tokens, ours, "-o", color="#D55E00", lw=1.3, ms=3.5, label="Ours")
ax.plot(tokens, baseline_a, "--s", color="#0072B2", lw=1.0, ms=3.0, label="Baseline A")
ax.plot(tokens, baseline_b, ":^", color="#64748B", lw=0.9, ms=3.0, label="Baseline B")

# Direct end-of-curve labels (eliminates eye-jumping to a boxed legend)
ax.annotate("Ours (+8.4%)", xy=(32, 87.6), xytext=(18, 88.3), color="#D55E00", fontweight="bold", fontsize=6.5)
ax.annotate("Baseline A", xy=(32, 79.2), xytext=(19, 80.2), color="#0072B2", fontsize=6.0)
ax.annotate("Baseline B", xy=(32, 75.0), xytext=(19, 73.2), color="#64748B", fontsize=6.0)

ax.set_xscale("log", base=2)
ax.set_xticks(tokens, labels=[f"{k}k" for k in tokens])
ax.set_xlabel("Context Budget (Tokens)")
ax.set_ylabel("Exact-Match Accuracy (%)")
ax.grid(axis="y", linestyle="--", linewidth=0.4, color="#E2E8F0")

fig.savefig("fig_scaling_curve.pdf", bbox_inches="tight")
```

### Workflow B: Constrained AI Layout Ideation → Illustrator / Figma Vector Redraw

When designing complex Figure 1 pipelines where visual brainstorming helps:

1. **Generate a Constrained Flat Wireframe (Never Sci-Fi Art):** Prompt a multimodal model to output either a `Mermaid`/`D2` structural graph or a strictly flat wireframe sketch:
   > *"Draft a clean 2D orthographic technical layout blueprint for a CVPR architecture diagram on a pure `#FFFFFF` background. Left-to-right pipeline: [list exact stages and tensor shapes]. Flat rectangles only, crisp 1pt dark grey orthogonal arrows, muted slate grey for frozen encoders, single warm orange accent for [Our Module], zero 3D bevels, zero glowing icons, zero background gradients, placeholder text boxes only."*
2. **Lock & Trace on a 1mm / 4px Grid:** Place the AI sketch in **Figma** or **Adobe Illustrator** on a locked layer at `20%` opacity on an exact `183 mm` or `174 mm` artboard.
3. **Rebuild Every Primitive Manually:** Draw crisp vector rectangles, align spacing mathematically with Auto-Layout / Distribute Spacing, typeset `Arial 7pt` + SVG LaTeX equations, and **delete the locked AI raster layer completely** before exporting `.pdf`.
4. **Run the 3-Point Pre-Submission Audit:**
   - **800% Zoom Test:** Are all borders and characters razor-sharp vector curves?
   - **`Ctrl+F` Search Test:** Can you highlight and search module names inside the exported PDF?
   - **Grayscale Squint Test:** In grayscale, does your novel contribution still stand out structurally from frozen baselines?

---

## 5. Before-vs-After Scientific Figure Specifications

### Example 1: NeurIPS / CVPR Multimodal Architecture Figure 1

- **Before (AI Slop Prompt):**
  > `Create an impressive scientific diagram of a multimodal Vision-Language-Action robot brain architecture, glowing neural network connections, futuristic 3D isometric blocks, vibrant blue and purple gradients, high resolution.`
  - *Result:* Unpublishable dark-navy poster with a glowing cybernetic skull, misspelled `"Visoin Tokneizer"`, arbitrary glowing tubes, and zero mathematical content.
- **After (Clean Vector Blueprint Specification):**
  - **Canvas:** `174 mm × 68 mm` vector PDF (`#FFFFFF` ground).
  - **Left Column (`Input Modalities`):** Real `300 DPI` RGB wrist-camera frame (`224×224×3`) + state vector $\mathbf{q}_t \in \mathbb{R}^7$ + instruction string in `6.5pt` monospace.
  - **Middle-Left (`Frozen Encoders`):** Muted slate boxes (`#F1F5F9` fill, `#64748B` `0.7pt` dashed border) for `Frozen SigLIP ViT` and `Text Tokenizer`, outputting $\mathbf{Z}_v \in \mathbb{R}^{256 \times d}$.
  - **Center Spotlight (`Ours: Sparse Cross-Scale Router`):** `#FFF7ED` container with `1.0pt` `#C2410C` border, zoomed callout inset showing top-$k$ token gating mask $\mathbf{M}_t \in \{0,1\}^{256}$ and complexity reduction $\mathcal{O}(N^2) \to \mathcal{O}(Nk)$.
  - **Right (`Action Flow Head`):** Orthogonal `0.75pt` arrows into velocity field $v_\theta(\mathbf{a}_t^\tau, \tau)$ producing trajectory $\hat{\mathbf{a}}_{t:t+H}$.

### Example 2: Drop-In LaTeX `TikZ` NeurIPS Two-Tone Pipeline Template

Compile directly inside LaTeX (`\usepackage{tikz}`, `\usetikzlibrary{arrows.meta,positioning}`) for zero-raster, 100%-searchable architecture blocks that spotlight your core contribution (`paper-boundaries` hierarchy):

```latex
\definecolor{slateFill}{HTML}{F1F5F9}
\definecolor{slateLine}{HTML}{64748B}
\definecolor{streamFill}{HTML}{EFF6FF}
\definecolor{streamLine}{HTML}{2563EB}
\definecolor{oursFill}{HTML}{FFF7ED}
\definecolor{oursLine}{HTML}{C2410C}
\definecolor{inkDark}{HTML}{0F172A}

\begin{tikzpicture}[
  font=\sffamily\scriptsize,
  node distance=7mm and 9mm,
  >= {Latex[length=1.6mm, width=1.2mm]},
  frozen/.style={draw=slateLine, dashed, line width=0.65pt, fill=slateFill,
    rounded corners=1.2pt, text=inkDark, minimum height=9mm, inner xsep=3mm, align=center},
  stream/.style={draw=streamLine, line width=0.75pt, fill=streamFill,
    rounded corners=1.2pt, text=inkDark, minimum height=9mm, inner xsep=3mm, align=center},
  ours/.style={draw=oursLine, line width=1.05pt, fill=oursFill,
    rounded corners=1.2pt, text=inkDark, minimum height=10.5mm, inner xsep=3.5mm, align=center},
  flow/.style={->, draw=inkDark, line width=0.65pt}
]
  \node[frozen] (enc) {Frozen ViT\\[-1pt]{\tiny $\mathbf{X}\in\mathbb{R}^{B\times N\times d}$}};
  \node[ours, right=of enc] (router) {\textbf{Sparse Spectral Gate (Ours)}\\[-1pt]{\tiny $\tilde{\mathbf{Z}} = \sigma(\mathbf{W}_g\mathbf{X})\odot\mathbf{X}$}};
  \node[stream, right=of router] (head) {Task Decoder\\[-1pt]{\tiny $\hat{\mathbf{Y}}\in\mathbb{R}^{B\times K}$}};

  \draw[flow] (enc) -- node[above, font=\tiny]{$[B,256,768]$} (router);
  \draw[flow] (router) -- node[above, font=\tiny]{$[B,32,768]$} (head);
\end{tikzpicture}
```

### Example 3: Biomedical / Systems Mechanism Graphical Abstract

- **Before (AI Slop):** 3D glossy translucent cells floating in purple outer space with glowing orange lightning bolts labeled `"Inflamation Singaling"`.
- **After (*Nature* Clean Vector Standard):** `89 mm × 75 mm` flat 2D schematic on `#FFFFFF`; phospholipid bilayer rendered as a clean `#CBD5E1` geometric band; wild-type pathway in muted `#64748B` (`0.6pt` arrows) on left vs. inhibited therapeutic pathway in `#009E73` (`0.9pt` inhibition T-bar `⊣`) on right; exact protein/gene capitalization (`*TP53*` italic gene vs. `p53` upright protein) in `6.5pt Arial`.

---

# Part II: Web, SaaS & Product UI Design De-AI (前端界面与 Vibe Coding 去 AI 味)

## 6. Why Vibe-Coded & AI-Generated UIs Collapse Into Slop

Ask any LLM coding agent (*"Build a modern landing page or dashboard for my analytics tool"*) without aesthetic constraints, and it computes the **mode of 2021–2024 Tailwind templates and Dribbble shots**: `#09090B` dark background, `#6366F1 → #A855F7` indigo-purple gradient text, `Inter` font, a glowing `✨ AI-Powered` pill badge, and three identical `rounded-2xl` Lucide-icon cards. Users now associate this exact aesthetic with disposable, untrustworthy weekend wrappers.

---

## 7. Diagnostic Catalog of UI AI Slop (`UI1–UI12`)

| ID | UI Slop Tell (CN / EN) | Code / Visual Signature | Human-Crafted Replacement |
|----|------------------------|-------------------------|---------------------------|
| **UI1** | **Indigo-Purple Gradient Virus** (`蓝紫渐变癌`) | `bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 bg-clip-text text-transparent` + blurred radial purple orbs | Solid high-contrast ink (`#111315` or `#F4F4F5`) + **one** grounded solid brand accent (e.g., `#0F766E` deep teal, `#C2410C` burnt sienna, or pure monochrome). |
| **UI2** | **Centered Pill-Badge Hero Formula** (`居中胶囊徽章三件套`) | `✨ Introducing X 2.0` pill → centered gradient H1 → 2-line grey subtitle → dual buttons → generic tilted mockup | Left-aligned or asymmetric 12-column editorial split (`col-span-5` concrete claim + `col-span-7` interactive live workspace/CLI preview). |
| **UI3** | **Uniform 3-Column Icon-Card Grid** (`等宽三列图标卡片阵`) | `grid-cols-3 gap-6` of identical `rounded-2xl border p-6` cards, each with a tinted `40×40` icon box + 3-word header + 2-line blurb | Break uniformity: use hairline-divided specification rows, alternating narrative + artifact sections, or asymmetric `8+4` / `7+5` functional spans. |
| **UI4** | **Sparkles ✨ & Emoji Chrome** (`魔法星标与 Emoji 泛滥`) | `<Sparkles />`, `<Rocket />`, `<Zap />`, or `🚀 💡 🔒 📈` pasted onto buttons, tabs, sidebar items, and section headers | Zero emojis in product UI chrome. Use restrained `1.5px`-stroke geometric icons *only* where icons aid spatial scanning (navigation rails, toolbar actions). |
| **UI5** | **Typographic Monoculture (`Inter` Default)** (`默认字体无层级无数字对齐`) | Unconfigured `Inter`/`Roboto` everywhere, loose letter-spacing on 56px titles, proportional digits causing jittery metric columns | Deliberate font pairing (e.g., `Instrument Serif` / `Newsreader` + `Geist` / `Plus Jakarta Sans` + `JetBrains Mono`), `tracking-[-0.03em]` on display titles, and `tabular-nums` on all numbers. |
| **UI6** | **Fake Bento Filler & Meaningless Rings** (`伪 Bento 装饰卡与假图表`) | Bento boxes stuffed with animated concentric radar rings, avatar bubbles, or `+240% Faster!` badges with no axes | Every grid cell must show a **real domain artifact**: actual query diff, latency percentile (`p99: 14.2 ms`), real schema tree, or interactive toggle. |
| **UI7** | **Glassmorphism & Nested Box Soup** (`毛玻璃与套娃圆角框`) | Cards inside cards inside cards (`p-6` inside `p-6`), `backdrop-blur-xl bg-white/5 rounded-3xl` everywhere, muddy `3.0:1` grey text | Flatten container nesting. Separate regions with crisp `1px` hairline rules (`border-zinc-200` / `border-white/8`) and generous whitespace instead of nested boxes. |
| **UI8** | **AI Marketing Slop & Fake Testimonials** (`假证言与赋能套话文案`) | *"Supercharge your workflow seamlessly"* + quotes from `"Sarah Chen, CTO at TechFlow"` and `"Marcus Vance, VP at NexusAI"` | State concrete mechanism and numbers (*"Streams 10M Parquet rows in 380ms via DuckDB WASM"*). Never invent fake customer quotes or fake logos. |
| **UI9** | **Happy-Path-Only Blindness** (`缺失空状态/加载态/溢出态`) | Hardcoded 5-row tables with 10-character names; breaks on zero rows, 80-character filenames, API errors, or `375px` mobile screens | Design all **5 mandatory states**: Empty (with primary onboarding action), Loading (layout-matched skeleton), Populated, Overflow (`truncate` + tooltip), and Error (actionable retry). |
| **UI10** | **Hover-Bounce Gymnastics** (`非交互卡片浮夸弹跳`) | Static text cards running `hover:-translate-y-2 hover:scale-105 transition-all duration-500` and `animate-pulse` dots everywhere | Only clickable controls get hover elevation. Keep productivity UI transitions fast (`120–180ms cubic-bezier(0.16, 1, 0.3, 1)`), subtle, and purposeful. |
| **UI11** | **Muddy Black Drop Shadows** (`脏黑阴影与圆角混乱`) | Mixing `rounded-md`, `rounded-xl`, `rounded-3xl`, and heavy `shadow-xl` black blurs on light cards | Lock border-radius tokens globally (e.g., `4px` controls / `8px` panels, or `8px` / `14px`). Prefer `1px` border + ultra-subtle `0 1px 2px rgba(0,0,0,0.04)` shadow. |
| **UI12** | **Reflexive Dark-Mode Cyberpunk** (`不分场景硬套暗黑霓虹`) | Building medical EHRs, tax software, academic portals, or reading apps in `#05050A` neon dark mode | Match luminance to task ergonomics: long-form reading, clinical/legal forms, and daylight B2B workflows default to warm or crisp light surfaces; dev/media consoles earn dark mode. |

---

## 8. Concrete Human-Crafted UI Rules & Design Archetypes

### 8.1 Pick an Intentional Design Archetype First

Before writing a single line of CSS, commit to **one** coherent aesthetic archetype instead of "modern SaaS":

| Archetype | Reference Feel | Surface & Ink HEX | Accent & Border HEX | Font Pairing (Display / UI / Mono) | Radius & Density |
|-----------|----------------|-------------------|---------------------|------------------------------------|------------------|
| **1. Warm Editorial Paper** | *Anthropic, Stripe Press, Read.cv* | Ground `#FAF9F5`, Card `#F3F1EA`, Ink `#141413`, Muted `#5E5D59` | Accent `#C96442` (terracotta), Rule `#E5E2D9` | `Newsreader` or `Instrument Serif` / `Plus Jakarta Sans` / `Commit Mono` | `6px` crisp, generous editorial breathing room |
| **2. Precision Utilitarian Pro-Tool** | *Linear, Raycast, Vercel* | Ground `#0B0C0E` (or `#FAFAFA`), Surface `#121417`, Ink `#F3F4F6` | Accent `#3B82F6` or `#10B981` (status only), Rule `rgba(255,255,255,0.08)` | `Geist` / `Geist` (`13px` UI) / `Geist Mono` | `6px` controls, `10px` panels, high keyboard-first density |
| **3. Quantitative / Systems Terminal** | *Grafana, Bloomberg, DuckDB UI* | Ground `#FFFFFF` or `#0F1115`, Zebra `#F8FAFC`, Ink `#0F172A` | Accent `#0284C7`, Alert `#DC2626`, Rule `#E2E8F0` | `IBM Plex Sans` / `IBM Plex Sans` / `JetBrains Mono` | `2px–4px` sharp technical edges, tabular grid lines |
| **4. Swiss Architectural Grid** | *Vitsoe, Are.na, Bauhaus catalogs* | Ground `#FFFFFF`, Surface `#F5F5F4`, Ink `#0A0A0A` | Accent `#DC2626` (signal red) or pure `#0A0A0A`, Rule `#D6D3D1` (`1px` full-bleed) | `Space Grotesk` or `Helvetica Neue` / `Work Sans` / `Space Mono` | `0px` (`rounded-none`), visible structural grid hairlines |
| **5. Organic Consumer Craft** | *Kinfolk, Wise, Notion* | Ground `#FCFBF9`, Surface `#F4F6F3`, Ink `#1C241E` | Accent `#1B4332` (deep forest), Rule `#E2E7E0` | `Fraunces` / `DM Sans` / `DM Mono` | `10px–16px` tactile warmth, real photography |

### 8.2 Non-Negotiable CSS Typography & Layout Discipline

Apply these structural CSS rules across every generated interface:

```css
/* 1. Display typography: tight optical tracking & balanced line wraps */
.heading-display {
  font-size: clamp(2rem, 4vw, 3.5rem);
  line-height: 1.08;
  letter-spacing: -0.03em;
  text-wrap: balance;
}

/* 2. Readable prose measure & orphan prevention */
.prose-measure {
  max-width: 64ch;
  line-height: 1.6;
  text-wrap: pretty;
}

/* 3. Mandatory tabular numerals on EVERY metric, price, timestamp, and table cell */
.metric, table td, time, .price {
  font-variant-numeric: tabular-nums lining-nums;
}
```

### 8.3 Drop-In `DESIGN.md` / Agent Anti-Slop Guardrail Prompt

Paste this block into `DESIGN.md`, `AGENTS.md`, or system prompts when directing coding agents (Claude Code, Antigravity, Cursor, v0):

```markdown
# UI Anti-Slop Design System Rules

## Hard Bans
1. NO indigo/violet/purple gradients (`indigo-500`, `purple-500`, `violet-600`, or gradient hero text).
2. NO floating blurred neon background blobs (`blur-3xl bg-purple-500/20`).
3. NO centered hero formula (`✨ pill badge` -> gradient H1 -> 2-line blurb -> 3 equal icon cards).
4. NO `<Sparkles />`, `<Rocket />`, or raw emojis (`🚀 ✨ 💡 🔒`) as UI icons.
5. NO unconfigured `Inter`/`Roboto` defaults, and NO proportional numbers in tables/metrics (enforce `tabular-nums`).
6. NO invented testimonials ("Sarah Chen at TechFlow") or hollow AI slogans ("Supercharge your workflow").

## Mandatory Craft Standards
1. Declare a concrete palette upfront: tinted neutral background + high-contrast ink (>= 7:1) + ONE solid functional accent color.
2. Pair a distinctive display/editorial header font with a crisp UI sans and monospace data font; apply `tracking-tight` (`-0.025em` to `-0.035em`) on headings >= 28px.
3. Structure pages using asymmetric 12-column grids, 1px hairline dividers, specification tables, and real interactive product states rather than uniform 3-column rounded cards.
4. Implement Empty, Loading, Populated, Long-Text Overflow, and Error states for every data view using realistic domain records.
```

---

## 9. Before-vs-After UI Code Refactor (React + Tailwind)

### Before: Classic Vibe-Coded SaaS Slop (`UI1 + UI2 + UI3 + UI4 + UI8`)

```tsx
// ❌ AI SLOP: Purple gradient text, sparkles pill, centered symmetry, 3 identical icon cards, zero mechanism
export function SlopHero() {
  return (
    <section className="bg-slate-950 py-24 text-center text-white relative overflow-hidden">
      <div className="absolute inset-0 bg-purple-600/20 blur-3xl rounded-full" />
      <span className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-sm">
        ✨ Next-Gen AI Log Analytics
      </span>
      <h1 className="mt-6 text-5xl font-bold bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
        Supercharge Your Observability Workflow
      </h1>
      <p className="mt-4 text-slate-400 max-w-xl mx-auto">
        Unlock seamless insights across your entire stack with blazing-fast AI-powered telemetry.
      </p>
      <div className="mt-16 max-w-5xl mx-auto grid grid-cols-3 gap-6 px-6">
        {["🚀 Blazing Fast", "🔒 Enterprise Security", "💡 Smart AI Insights"].map((title) => (
          <div key={title} className="rounded-2xl bg-white/5 border border-white/10 p-6 backdrop-blur-md hover:scale-105 transition">
            <h3 className="font-semibold text-lg">{title}</h3>
            <p className="mt-2 text-sm text-slate-400">Empowering teams to scale effortlessly in today's cloud landscape.</p>
          </div>
        ))}
      </div>
    </section>
  );
}
```

### After: Intentional Utilitarian Engineering UI (Asymmetric Split + Concrete Artifact + `tabular-nums`)

```tsx
// ✅ HUMAN-CRAFTED: Warm alabaster + slate ink, asymmetric 12-col split, concrete SQL/latency artifact, hairline spec row
export function TraceIndexHero() {
  return (
    <section className="bg-[#FAF9F5] text-[#141413] border-b border-[#E5E2D9]">
      <div className="max-w-6xl mx-auto px-6 py-20 grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        {/* Left 5 cols: Direct mechanism claim + verifiable specs */}
        <div className="lg:col-span-5">
          <p className="font-mono text-xs uppercase tracking-wider text-[#5E5D59]">
            Columnar OpenTelemetry Engine · v2.4
          </p>
          <h1 className="mt-3 font-serif text-4xl sm:text-5xl leading-[1.06] tracking-[-0.03em] text-balance">
            Grep 40 billion trace spans without hydrating cold object storage.
          </h1>
          <p className="mt-5 text-[15px] leading-relaxed text-[#4A4945] max-w-[52ch]">
            Writes Parquet bloom indexes directly to S3 and executes predicate pushdown in Rust. No JVM heap tuning, no hot-tier ingestion tax.
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-3">
            <a
              href="/docs/quickstart"
              className="px-4 py-2.5 rounded-md bg-[#141413] text-[#FAF9F5] text-sm font-medium hover:bg-[#2A2A28] transition-colors duration-150"
            >
              Read 3-minute quickstart
            </a>
            <code className="px-3 py-2.5 rounded-md bg-[#F0EEE6] border border-[#DFDDD2] font-mono text-xs text-[#141413]">
              curl -fsSL https://get.traceidx.dev | sh
            </code>
          </div>

          <dl className="mt-12 pt-6 border-t border-[#E5E2D9] grid grid-cols-3 gap-6 tabular-nums">
            <div>
              <dt className="text-xs text-[#5E5D59]">p99 cold scan (1 TB)</dt>
              <dd className="mt-1 font-mono text-lg font-medium">410 ms</dd>
            </div>
            <div>
              <dt className="text-xs text-[#5E5D59]">S3 index overhead</dt>
              <dd className="mt-1 font-mono text-lg font-medium">1.8%</dd>
            </div>
            <div>
              <dt className="text-xs text-[#5E5D59]">License</dt>
              <dd className="mt-1 font-mono text-lg font-medium">Apache-2.0</dd>
            </div>
          </dl>
        </div>

        {/* Right 7 cols: Real product artifact instead of decorative marketing cards */}
        <div className="lg:col-span-7 rounded-lg bg-[#141413] text-[#EAE8E1] border border-[#2C2C2A] overflow-hidden">
          <div className="px-4 py-2.5 border-b border-[#262624] flex items-center justify-between font-mono text-xs text-[#8E8D87] tabular-nums">
            <span>prod-us-east · s3://telemetry-archive/2026-11/</span>
            <span className="text-[#4ADE80]">248.4 GB scanned in 0.38s</span>
          </div>
          <pre className="p-4 font-mono text-xs leading-relaxed overflow-x-auto text-[#D6D4CC]">
{`SELECT service_name, count(*) AS err_spans, approx_quantile(duration_ms, 0.99) AS p99_ms
FROM s3_traces('2026-11-23T00:00Z', '2026-11-23T06:00Z')
WHERE http.status_code >= 500 AND tenant_id = 'acme_corp'
GROUP BY 1 ORDER BY err_spans DESC LIMIT 4;`}
          </pre>
          <table className="w-full text-left font-mono text-xs border-t border-[#262624] tabular-nums">
            <thead className="bg-[#1C1C1A] text-[#8E8D87]">
              <tr>
                <th className="py-2 px-4 font-normal">service_name</th>
                <th className="py-2 px-4 font-normal text-right">err_spans</th>
                <th className="py-2 px-4 font-normal text-right">p99_ms</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#232321]">
              <tr><td className="py-2 px-4">checkout-grpc</td><td className="py-2 px-4 text-right text-[#F87171]">1,402</td><td className="py-2 px-4 text-right">842.1</td></tr>
              <tr><td className="py-2 px-4">ledger-worker</td><td className="py-2 px-4 text-right">189</td><td className="py-2 px-4 text-right">319.4</td></tr>
              <tr><td className="py-2 px-4">auth-token-edge</td><td className="py-2 px-4 text-right">14</td><td className="py-2 px-4 text-right">41.8</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
```

### 9.1 Automated Codebase UI Anti-Slop Scanner (`ripgrep`)

Run this one-liner over generated frontend directories (`src/`, `app/`, `components/`) before shipping to catch residual AI UI clichés:

```bash
rg -n "(from-indigo-|via-purple-|to-pink-|blur-3xl|<Sparkles|hover:scale-105|Supercharge your|Sarah Chen|TechFlow|NexusAI)" src/ app/ components/
```

### 9.2 The 5 Mandatory States Audit (Beyond the Happy Path)

Before marking any UI view complete, verify every data component implements:

1. **Empty State (`0` records):** Explains *why* it is empty in one plain sentence + renders the exact primary button/CLI command to create the first record (no sad cartoon robots).
2. **Loading State:** Geometry-matched subtle shimmer or instant cached shell (`<150ms` delay threshold before showing spinner so fast responses never flash).
3. **Populated State:** Realistic domain strings with jagged lengths (`12 chars` vs. `68 chars`), realistic distributions (power-law numbers, not `100, 200, 300`), and `tabular-nums`.
4. **Edge / Overflow State:** `min-w-0` inside flex/grid children + `truncate` (`text-overflow: ellipsis`) on long identifiers, emails, and S3 paths, plus horizontal scroll containment on mobile tables.
5. **Error / Degraded State:** Specific HTTP/RPC failure reason, request ID in monospace for support copy-paste, and a non-destructive `Retry` button preserving user form input.

---

# Part III: Anti-Overcorrection Guardrails (防矫枉过正边界)

### Scientific Figures: What NOT to Strip

1. **Do Not Make Multi-Curve Plots Monochrome Grey:** Minimalism fails if 5 ablation curves share indistinguishable grey shades. Use 4–6 distinct **Okabe-Ito** hues paired with distinct line styles (`solid`, `dashed`, `dotted`) and marker shapes (`o`, `s`, `^`).
2. **Do Not Ban Domain-Accurate Illustrations:** Wet-lab protocols, anatomical cell membranes, surgical pathways, and robotic hardware rigs *need* clear domain schematics (via `BioRender`, CAD vector exports, or clean annotated photos). Ban **hallucinated sci-fi art**, not accurate physical schematics.
3. **Never Alter Empirical Pixels for Aesthetics:** Never apply smoothing, inpainting, contrast-clipping, or generative cleanup to microscopy, gel electrophoresis, medical scans, or benchmark qualitative outputs.

### UI Design: What NOT to Over-Correct

1. **Existing Brand Design Systems Always Win:** If a company's established design system (e.g., Stripe, Twitch, Linear, or an internal corporate Figma token library) explicitly specifies `Inter` or a violet brand primary, **obey the user's design tokens** over generic anti-slop bans.
2. **Do Not Force Editorial Serifs Into Dense Enterprise CRUD Apps:** A warehouse inventory table, IDE debugger, or hospital EHR needs fast-scanning neo-grotesk/system UI typography (`13–14px`), standard form affordances, and predictable navigation—not avant-garde brutalist magazine layouts.
3. **Cards Are Valid for Genuine Peer Entities:** Banning uniform 3-column *marketing blurb* cards does not mean banning cards altogether. E-commerce product catalogs, photo galleries, Kanban boards, and video grids represent homogeneous records where uniform card grids are the right information architecture.
4. **Never Sacrifice Accessibility for "Subtlety":** Ultra-faint `1px` borders and low-contrast `#A1A1AA` body text on `#FAFAFA` look sleek on a calibrated Apple Studio Display in a dark room, then vanish on office projectors and fail WCAG AA (`4.5:1`). Verify contrast ratios before shipping.
