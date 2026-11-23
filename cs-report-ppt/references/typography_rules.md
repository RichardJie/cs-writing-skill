# Visual Typography & Card Grid Geometry Rules

This specification establishes the geometric, typographic, and visual design standards for the `academic-paper-presentation` generator.

Every slide adheres strictly to a **16:9 widescreen coordinate grid**, standard vertical zone partitions, responsive card structures, and a hierarchical typography scale to eliminate empty dead-space ("少留白", 高级简约).

---

## 1. 16:9 Widescreen Canvas Coordinate Space

Modern academic conference presentations are standardly projected in **16:9 widescreen**:

- **Physical Dimensions**:
  - Width: $W = 13.333\text{ inches}$ ($33.867\text{ cm}$)
  - Height: $H = 7.500\text{ inches}$ ($19.050\text{ cm}$)
- **OpenXML EMUs** ($1\text{ inch} = 914,400\text{ EMU}$):
  - Width: $12,192,000\text{ EMU}$
  - Height: $6,858,000\text{ EMU}$
- **Pixel Coordinates**:
  - Baseline (96 DPI): $1280 \times 720\text{ px}$
  - High-DPI (144 DPI): $1920 \times 1080\text{ px}$
  - Raster Preview (150 DPI): $2001 \times 1125\text{ px}$
  - Print / Archival (300 DPI): $4001 \times 2250\text{ px}$

---

## 2. Standard Vertical Zone Decomposition

Every slide is segmented into three strictly non-overlapping vertical zones:

```
0.00" ┌────────────────────────────────────────────────────────────────────────┐
      │ HEADER ZONE (Y: 0.35" -> 1.55", H: 1.20", W: 12.133")                   │
      │ • Category / Tracker Badge (Y: 0.35", H: 0.25", 10pt Bold Caps)         │
      │ • Slide Title (Y: 0.60", H: 0.50", 24-28pt Bold)                       │
      │ • Subtitle / Key Takeaway (Y: 1.10", H: 0.35", 14-16pt Medium/Italic)   │
      │ • Accent Divider Rule (Y: 1.50", H: 0.02")                             │
1.65" ├────────────────────────────────────────────────────────────────────────┤
      │ CONTENT ZONE (Y: 1.65" -> 6.85", H: 5.20", W: 12.133")                 │
      │                                                                        │
      │   ┌──────────────────────────────┐    ┌────────────────────────────┐   │
      │   │  MAIN CARD CONTAINER (65%)   │    │  RESEARCH SIDENOTE (35%)   │   │
      │   │  • Technical Equations / Fig │    │  🔬 OUR RESEARCH CONNECTION│   │
      │   │  • Structured Assertions     │    │  • Relevance to Lab        │   │
      │   └──────────────────────────────┘    └────────────────────────────┘   │
      │                                                                        │
6.85" ├────────────────────────────────────────────────────────────────────────┤
      │ FOOTER ZONE (Y: 7.00" -> 7.35", H: 0.35", W: 12.133")                  │
      │ Left: Paper Citation / DOI / Presenter       Right: Slide Number (XX/14)│
7.50" └────────────────────────────────────────────────────────────────────────┘
      0.60"                                                            12.733"
```

### Zone Coordinate Metrics:
- **Left Margin ($M_L$)**: `0.600"`
- **Right Margin ($M_R$)**: `0.600"`
- **Top Margin ($M_T$)**: `0.350"`
- **Bottom Margin ($M_B$)**: `0.150"`
- **Usable Canvas Width ($W_{\text{usable}}$)**: $13.333 - 1.200 = 12.133''$
- **Usable Content Height ($H_{\text{content}}$)**: $6.850 - 1.650 = 5.200''$

---

## 3. Responsive Card Grid Layout Models

The layout engine supports seven deterministic mathematical grid models:

### 1. `hero_1col` — Single Hero Card
- **Use cases**: Slide 1 Title hero, high-impact architecture diagrams, primary master benchmark tables.
- **Formulas**:
  - $x_0 = 0.600''$, $y_0 = 1.650''$
  - $w_0 = 12.133''$, $h_0 = 5.200''$

### 2. `split_equal_2col` — Balanced 50/50 Dual Cards
- **Use cases**: Slide 4 Hypothesis vs Gaps, Slide 6 Inputs vs Invariants, Slide 13 Author Claims vs Critique.
- **Formulas** (Gap $G = 0.300''$):
  - $w = (12.133 - 0.300) / 2 = 5.916''$
  - $\text{Card}_0: x_0 = 0.600'', y_0 = 1.650'', w = 5.916'', h = 5.200''$
  - $\text{Card}_1: x_1 = 6.816'', y_1 = 1.650'', w = 5.916'', h = 5.200''$

### 3. `split_65_35` — Asymmetric Side-Note Layout
- **Use cases**: Slide 2 Motivation + Callout, Slide 5 Lineage + Callout, Slide 8 Architecture + Callout, Slide 11 Trade-offs + Callout, Slide 14 Roadmap.
- **Formulas** (Gap $G = 0.300''$, $W_{\text{net}} = 11.833''$):
  - $\text{Main Card}: x = 0.600'', y = 1.650'', w = 7.700'', h = 5.200''$
  - $\text{Side-Note Card}: x = 8.600'', y = 1.650'', w = 4.133'', h = 5.200''$

### 4. `grid_3col` — Three Equal Vertical Columns
- **Use cases**: Slide 3 Taxonomy matrix, Slide 9 Datasets / Baselines / Compute Protocol.
- **Formulas** (Gap $G = 0.250''$, $W_{\text{net}} = 12.133 - 2(0.250) = 11.633''$):
  - $w = 11.633 / 3 = 3.877''$
  - $\text{Card}_i: x_i = 0.600'' + i \times (3.877 + 0.250)'', y_i = 1.650'', w = 3.877'', h = 5.200''$
  - Positions: $x_0 = 0.600''$, $x_1 = 4.727''$, $x_2 = 8.854''$

### 5. `grid_4col` — Four Equal Vertical Columns
- **Use cases**: 4-phase sequential execution pipeline, 4 seminar discussion prompts.
- **Formulas** (Gap $G = 0.200''$, $W_{\text{net}} = 12.133 - 3(0.200) = 11.533''$):
  - $w = 11.533 / 4 = 2.883''$
  - $\text{Card}_i: x_i = 0.600'' + i \times (2.883 + 0.200)'', y_i = 1.650'', w = 2.883'', h = 5.200''$
  - Positions: $x_0 = 0.600''$, $x_1 = 3.683''$, $x_2 = 6.766''$, $x_3 = 9.849''$

### 6. `quadrant_2x2` — Four Quadrant Matrix
- **Use cases**: Slide 12 Ablation studies (Component contribution, Hyperparameter sensitivity, Scaling laws, Failure modes).
- **Formulas** (GapX $G_x = 0.300''$, GapY $G_y = 0.250''$):
  - $w = (12.133 - 0.300) / 2 = 5.916''$
  - $h = (5.200 - 0.250) / 2 = 2.475''$
  - $\text{Top-Left}: x = 0.600'', y = 1.650'', w = 5.916'', h = 2.475''$
  - $\text{Top-Right}: x = 6.816'', y = 1.650'', w = 5.916'', h = 2.475''$
  - $\text{Bottom-Left}: x = 0.600'', y = 4.375'', w = 5.916'', h = 2.475''$
  - $\text{Bottom-Right}: x = 6.816'', y = 4.375'', w = 5.916'', h = 2.475''$

### 7. `asymmetric_2row` — Master Table + Takeaway Cards
- **Use cases**: Slide 10 Master benchmark result table + 2 quantitative takeaway cards.
- **Formulas**:
  - $\text{Top Hero Card}: x = 0.600'', y = 1.650'', w = 12.133'', h = 2.300''$
  - $\text{Bottom Left Card}: x = 0.600'', y = 4.150'', w = 5.916'', h = 2.700''$
  - $\text{Bottom Right Card}: x = 6.816'', y = 4.150'', w = 5.916'', h = 2.700''$

---

## 4. Typography Hierarchy & Sizing Matrix

To guarantee readability across auditoriums, monitors, and mobile previews, text styles strictly follow this hierarchy:

| Hierarchy Level | Font Size (pt) | Weight | Line Spacing | Color Role | Primary Usage | Constraints |
|---|---|---|---|---|---|---|
| **Slide Title** | `26 pt` (range 22-28) | Bold (700) | 1.10x | Theme `textPrimary` | Primary slide headline | Single line, no wrap |
| **Slide Subtitle** | `15 pt` (range 14-16) | Medium (500) | 1.20x | Theme `textSecondary` | 1-line key takeaway assertion | Italic / Medium |
| **Card Header** | `18 pt` (range 16-18) | Bold (700) | 1.20x | Theme `primary` | Title of individual card | `shrinkText: true` |
| **Card Body** | `13 pt` (range 12-14) | Regular (400) | 1.25x | Theme `textPrimary` | Bullet points, paragraph text | `autoFit: true`, `shrinkText: true` |
| **Card Body (Dense)**| `12 pt` | Regular (400) | 1.20x | Theme `textSecondary` | Multi-line dense descriptions | `autoFit: true` |
| **Note / Annotation**| `12 pt` | Regular/Italic | 1.20x | Theme `sideNoteText` | Marginal research connection | Pastel card text |
| **Category Tracker** | `10 pt` | Bold Uppercase | 1.00x | Theme `accent` | Top tracker badge | Uppercase tracking |
| **Footer Citation** | `10 pt` | Regular | 1.00x | Theme `textMuted` | DOI, venue, page number | Bottom margin |
| **Math Block** | `14 pt` | Regular | 1.20x | Native OMML font | Standalone centered equation | DrawingML OMML |

---

## 5. Visual Card Anatomy & Shape Styling

Every card container is assembled using structured DrawingML shape properties:

1. **Card Container**:
   - Shape: `roundRect` with corner radius `0.08"` (`6px`).
   - Background Fill: Solid `#FFFFFF` (or light conference tint).
   - Border Stroke: Solid `1.5pt` (`#E2E8F0` / theme card border).
   - Soft Outer Drop Shadow: Color `#000000`, Opacity `0.06`, Blur `6pt`, Offset `2pt`, Angle `45°`.
2. **Top Accent Strip** (Standard Cards):
   - Shape: `rect` or top-border line of height `0.08"` across card width.
   - Fill: Conference `primary` or `accent` color.
3. **Marginal Research Side-Note Card** ("旁注"):
   - Fill: Soft pastel tint matched to theme palette.
   - Left Accent Bar: Solid `0.08"` thick vertical rectangle spanning card height ($h = 5.20''$) in saturated theme accent.
   - Header Pill Badge: `[ 🔬 OUR RESEARCH CONNECTION ]` in `11pt Bold Uppercase`.
4. **Internal Padding**:
   - Top / Bottom: `0.20"`
   - Left / Right: `0.25"`

---

## 6. Theme Presets (Academic Minimalist Default + Conference Palettes)

1. **Academic Minimalist (Black & White, Default — `academic_mono`)**:
   - Primary Header: `#000000` | Body Text: `#1F2937` | Secondary Text: `#4B5563`
   - Background: `#FFFFFF` | Card Background: `#FFFFFF` | Card Border: `#D1D5DB`
   - Callout / Sidenote Tint: `#F9FAFB` | Sidenote Accent Strip: `#111827`
   - Philosophy: High-contrast, publication-grade academic monochrome keeping visual focus entirely on mathematical rigor and authentic paper figures.

2. **NeurIPS (Midnight Navy)**:
   - Primary: `#0F2042` | Accent: `#2563EB` | Secondary: `#475569`
   - Background: `#F8FAFC` | Callout Tint: `#EFF6FF` | Border: `#1D4ED8`
3. **ICML (Deep Teal / Emerald)**:
   - Primary: `#042F2E` | Accent: `#0D9488` | Secondary: `#475569`
   - Background: `#F0FDFA` | Callout Tint: `#CCFBF1` | Border: `#0F766E`
4. **CVPR (Crimson Rose / Slate)**:
   - Primary: `#4C0519` | Accent: `#E11D48` | Secondary: `#475569`
   - Background: `#FFF1F2` | Callout Tint: `#FFE4E6` | Border: `#BE123C`
5. **ICLR (Deep Purple / Violet)**:
   - Primary: `#2E1065` | Accent: `#7C3AED` | Secondary: `#475569`
   - Background: `#FAF5FF` | Callout Tint: `#F3E8FF` | Border: `#6D28D9`
6. **KDD (Warm Amber / Bronze)**:
   - Primary: `#451A03` | Accent: `#D97706` | Secondary: `#475569`
   - Background: `#FFFBEB` | Callout Tint: `#FEF3C7` | Border: `#B45309`

---

## 7. Zero Dead-Space Discipline ("少留白", 高级简约)

To achieve dense, high-signal presentation elegance:

1. **Horizontal Fill Rule**: Bullet point text should occupy at least 75-80% of card width before wrapping. Avoid single-word dangling lines.
2. **Vertical Rhythm Rule**: If a card contains only 2 bullet points, the line spacing expands to 1.35x, or is augmented with a bottom key metric highlight badge ($h = 0.85''$).
3. **High-DPI Figure Scaling & Aspect Ratio Preservation**:
   - When placing figures into cards, compute:
     $$s = \min\left(\frac{W_{\text{card}} - 2 \cdot P_x}{W_{\text{orig}}}, \frac{H_{\text{card}} - 2 \cdot P_y}{H_{\text{orig}}}\right)$$
   - Render image at scaled dimensions: $W_{\text{render}} = s \cdot W_{\text{orig}}, H_{\text{render}} = s \cdot H_{\text{orig}}$.
   - Center image symmetrically inside container:
     $$X_{\text{img}} = X_{\text{card}} + \frac{W_{\text{card}} - W_{\text{render}}}{2}, \quad Y_{\text{img}} = Y_{\text{card}} + \frac{H_{\text{card}} - H_{\text{render}}}{2}$$
