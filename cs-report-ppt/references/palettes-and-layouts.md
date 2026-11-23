# Scholarly Color Palettes, Anti-AI-Slop Visual Rules & 16:9 Coordinate Layouts

> **Module Role**: Definitive visual styling and spatial geometry specification for [`cs-report-ppt`](../SKILL.md). Governs the **6 curated scholarly HEX color palettes**, **10 enforceable Anti-AI-Slop visual laws**, **aspect-ratio-driven adaptive figure framing**, and **12 exact `(x, y, w, h)` coordinate layout recipes** on the `13.333" × 7.500"` widescreen canvas, directly powering [`resources/template_config.json`](../resources/template_config.json) and [`scripts/build_deck.js`](../scripts/build_deck.js) alongside [`typography_rules.md`](typography_rules.md) and [`architecture_diagrams.md`](architecture_diagrams.md).

---

## 1. Six Curated Scholarly HEX Color Palettes

Academic slides fail visually when they use **tinted pastel slide backgrounds** (pink, lavender, pale yellow) that clash with white-background PDF crops, or **loud startup gradients** that steal chromatic attention from empirical figures.

All 5 light-mode scholarly palettes enforce a **pure `#FFFFFF` canvas** so harvested 300+ DPI paper figures blend seamlessly without ugly bounding-box seams, governed by the **70 / 25 / 5 Scholarly Ink Budget**:
- **$\ge 70\%$ Neutral Canvas**: Pure `#FFFFFF` (or `#0F1117` in `keynote_dark_oral`) + subtle neutral card surfaces (`#F8FAFC` / `#F9FAFB`).
- **$\sim 25\%$ Structural Ink**: Deep charcoal/slate typography, `booktabs` table rules, and muted captions.
- **$\le 5\%$ Chromatic Accent Ink**: Tracker pills, `0.08"` card accent bars, SOTA delta highlights, and focal annotations.

### 1.1 Quick Palette Routing Matrix

| Palette ID | Aesthetic Archetype | Primary / Accent HEX | Canvas HEX | Ideal Scenarios & Disciplines |
|:---|:---|:---|:---|:---|
| **`academic_mono`** *(Default)* | Publication Monochrome | `#000000` / `#111827` | `#FFFFFF` | CS/AI journal clubs, Math/Theory seminars, papers whose embedded PDF figures already carry rich multi-color curves |
| **`oxford_navy`** | Institutional Navy & Crimson Point | `#002147` / `#1D4ED8` (`#B91C1C` delta) | `#FFFFFF` | PhD/Master thesis defenses (硕博毕业答辩), NSFC/grant reviews (国自然答辩), Economics/Finance, NeurIPS/ACL/ICLR talks |
| **`nature_slate_teal`** | Journal Slate & NPG Teal | `#0F3D3E` / `#0F766E` (`#C2410C` delta) | `#FFFFFF` | Biomedical, Clinical Medicine, Neuroscience, Chemistry, Bioinformatics, ICML, AI4Science, Ecology |
| **`mit_crimson_neutral`** | Engineering Crimson & Warm Stone | `#18181B` / `#A31F34` (`#0369A1` counter) | `#FFFFFF` | Computer Systems, Semiconductors/Hardware, Robotics, Physics, Mechanical/Control Engineering, Faculty Job Talks |
| **`cvpr_clean_blue`** | Crisp IEEE/CVF Cobalt & Slate | `#0F172A` / `#0284C7` (`#B45309` delta) | `#FFFFFF` | Computer Vision (CVPR/ICCV/ECCV), Graphics, Medical Imaging, Autonomous Driving (zero color-cast on RGB visual grids) |
| **`keynote_dark_oral`** | Auditorium Dark Slate Stage | `#F8FAFC` / `#38BDF8` (`#F59E0B` delta) | `#0F1117` | High-impact Conference Keynote / Spotlight / Lightning Talks (3–15 min) in darkened auditoriums, live demo videos |

---

### 1.2 Complete Semantic Token Specifications (All 6 Palettes)

Every HEX code below has been verified against **WCAG 2.1 AA/AAA projection contrast thresholds** (`textPrimary` contrast $\ge 13.5:1$ against canvas; `accent` badge/text contrast $\ge 4.6:1$).

#### 1. `academic_mono` — Minimalist Grayscale (Skill Default)
- **Design Rationale**: Zero decorative hue. Lets multi-colored paper plots, heatmaps, and microscopy take 100% chromatic priority while maintaining razor-sharp typographic authority.
- **Core Tokens**:
  - `background`: `#FFFFFF` | `cardBg`: `#FFFFFF` | `cardHeaderBg`: `#F9FAFB` | `cardBorder`: `#D1D5DB` (`1.0pt`)
  - `primary`: `#000000` (21.0:1) | `accent`: `#111827` | `secondary`: `#374151`
  - `textPrimary`: `#111827` (18.1:1) | `textSecondary`: `#4B5563` (7.5:1) | `textMuted`: `#6B7280` (4.8:1)
  - `sideNoteBg`: `#F9FAFB` | `sideNoteBorder`: `#374151` | `sideNoteAccent`: `#111827` | `sideNoteText`: `#111827`
  - `badgeBg`: `#F3F4F6` | `badgeText`: `#111827` | `highlightBg`: `#F3F4F6` | `highlightText`: `#000000`
  - **Table & Delta Semantics**: `tableRule`: `#111827` | `sotaRowBg`: `#F3F4F6` | Best metric: **Bold `#000000`** (optional restrained delta ink when requested: `#047857` positive / `#B91C1C` negative).
- **Colorblind-Safe Native Chart Series (Okabe-Ito High-Contrast Subset)**: `["#000000", "#0072B2", "#D55E00", "#009E73", "#7F7F7F"]`

#### 2. `oxford_navy` — Institutional Deep Navy & Academic Crimson Point
- **Design Rationale**: Classic university & funding-agency authority ("牛津蓝主调 + 万蓝丛中一点绛红"). Deep Oxford Blue anchors headers and structural rules; soft slate-gray softens body text; Academic Crimson (`#B91C1C`) is rationed to $\le 2$ focal metrics per slide.
- **Core Tokens**:
  - `background`: `#FFFFFF` | `cardBg`: `#FFFFFF` | `cardHeaderBg`: `#F8FAFC` | `cardBorder`: `#CBD5E1` (`1.0pt`)
  - `primary`: `#002147` (16.2:1) | `accent`: `#1D4ED8` (6.7:1) | `focalDelta`: `#B91C1C` (6.5:1)
  - `textPrimary`: `#0F172A` (17.8:1) | `textSecondary`: `#334155` (10.3:1) | `textMuted`: `#64748B` (4.8:1)
  - `sideNoteBg`: `#EFF6FF` | `sideNoteBorder`: `#BFDBFE` | `sideNoteAccent`: `#002147` | `sideNoteText`: `#1E3A8A`
  - `badgeBg`: `#EFF6FF` | `badgeText`: `#002147` | `highlightBg`: `#FEF2F2` | `highlightText`: `#991B1B`
  - **Table & Delta Semantics**: `tableRule`: `#002147` | `sotaRowBg`: `#EFF6FF` | `positiveDelta`: `#B91C1C` (CN NSFC/Defense convention: red = breakthrough gain) or `#047857` (EN convention).
- **Colorblind-Safe Native Chart Series (Paul Tol Bright)**: `["#002147", "#2563EB", "#B91C1C", "#0D9488", "#D97706", "#94A3B8"]`

#### 3. `nature_slate_teal` — Scientific Journal Slate & NPG Teal
- **Design Rationale**: Modeled directly on *Nature Reviews* / `ggsci` NPG editorial layouts. Pairs calm botanical slate-teal structure with NPG Vermilion (`#E64B35` / `#C2410C`) for statistical significance stars (`***`) and treatment effects.
- **Core Tokens**:
  - `background`: `#FFFFFF` | `cardBg`: `#FFFFFF` | `cardHeaderBg`: `#F8FAFC` | `cardBorder`: `#E2E8F0` (`1.0pt`)
  - `primary`: `#0F3D3E` (12.1:1) | `accent`: `#0D9488` / `#0F766E` (5.4:1) | `focalDelta`: `#C2410C` (5.2:1)
  - `textPrimary`: `#1E293B` (14.6:1) | `textSecondary`: `#475569` (7.6:1) | `textMuted`: `#64748B` (4.8:1)
  - `sideNoteBg`: `#F0FDFA` | `sideNoteBorder`: `#99F6E4` | `sideNoteAccent`: `#0F766E` | `sideNoteText`: `#134E4A`
  - `badgeBg`: `#CCFBF1` | `badgeText`: `#115E59` | `highlightBg`: `#FFF7ED` | `highlightText`: `#9A3412`
  - **Table & Delta Semantics**: `tableRule`: `#0F3D3E` | `sotaRowBg`: `#F0FDFA` | `positiveDelta`: `#0F766E` | `negativeDelta`: `#C2410C`.
- **Colorblind-Safe Native Chart Series (NPG Curated)**: `["#3C5488", "#00A087", "#E64B35", "#4DBBD5", "#7E6148", "#8491B4"]`

#### 4. `mit_crimson_neutral` — Engineering Crimson & Warm Stone Neutral
- **Design Rationale**: Inspired by MIT / Stanford engineering Monograph style. Uses MIT Crimson (`#A31F34`) strictly as a crisp structural razor (tracker text, `0.08"` bar, key SOTA delta) while keeping 95% of the slide in warm architectural charcoal and stone gray—never turning the slide pink or red-heavy.
- **Core Tokens**:
  - `background`: `#FFFFFF` | `cardBg`: `#FFFFFF` | `cardHeaderBg`: `#FAFAF9` | `cardBorder`: `#D6D3D1` (`1.0pt`)
  - `primary`: `#18181B` (17.9:1) | `accent`: `#A31F34` (6.8:1) | `focalDelta`: `#0369A1` (5.9:1 steel-blue counter-accent)
  - `textPrimary`: `#18181B` (17.9:1) | `textSecondary`: `#44403C` (9.7:1) | `textMuted`: `#78716C` (4.7:1)
  - `sideNoteBg`: `#FAFAF9` | `sideNoteBorder`: `#E7E5E4` | `sideNoteAccent`: `#A31F34` | `sideNoteText`: `#292524`
  - `badgeBg`: `#FEF2F2` | `badgeText`: `#991B1B` | `highlightBg`: `#FEF2F2` | `highlightText`: `#A31F34`
  - **Table & Delta Semantics**: `tableRule`: `#18181B` | `sotaRowBg`: `#F5F5F4` | `positiveDelta`: `#A31F34` | `secondaryMetric`: `#0369A1`.
- **Colorblind-Safe Native Chart Series**: `["#A31F34", "#18181B", "#0369A1", "#D97706", "#0F766E", "#8A8B8C"]`

#### 5. `cvpr_clean_blue` — Crisp IEEE/CVF Cobalt & Cool Slate
- **Design Rationale**: Replaces pink/tinted conference templates with neutral white + calibrated IEEE Cobalt (`#0284C7` / `#0369A1`). Preserves 100% color accuracy for RGB computer-vision crops, segmentation masks, depth maps, and generative image galleries.
- **Core Tokens**:
  - `background`: `#FFFFFF` | `cardBg`: `#FFFFFF` | `cardHeaderBg`: `#F8FAFC` | `cardBorder`: `#E2E8F0` (`1.0pt`)
  - `primary`: `#0F172A` (17.8:1) | `accent`: `#0284C7` / `#0369A1` (5.9:1) | `focalDelta`: `#D97706` / `#B45309` (5.0:1)
  - `textPrimary`: `#0F172A` (17.8:1) | `textSecondary`: `#334155` (10.3:1) | `textMuted`: `#64748B` (4.8:1)
  - `sideNoteBg`: `#F0F9FF` | `sideNoteBorder`: `#BAE6FD` | `sideNoteAccent`: `#0284C7` | `sideNoteText`: `#0C4A6E`
  - `badgeBg`: `#E0F2FE` | `badgeText`: `#075985` | `highlightBg`: `#FEF3C7` | `highlightText`: `#92400E`
  - **Table & Delta Semantics**: `tableRule`: `#0F172A` | `sotaRowBg`: `#F0F9FF` | `positiveDelta`: `#0369A1` | `negativeDelta`: `#B91C1C`.
- **Colorblind-Safe Native Chart Series (Okabe-Ito)**: `["#0072B2", "#E69F00", "#009E73", "#D55E00", "#56B4E9", "#64748B"]`

#### 6. `keynote_dark_oral` — High-Contrast Dark Slate Stage Oral
- **Design Rationale**: Engineered for Keynote-style Spotlight, Lightning, and Plenary Oral talks in darkened halls. Avoids pure `#000000` (causes projector black-crush) and pure `#FFFFFF` body text (causes halation/astigmatism blur), using Deep Charcoal-Navy `#0F1117` and Soft Off-White `#F8FAFC`.
- **Core Tokens**:
  - `background`: `#0F1117` | `cardBg`: `#161B26` | `cardHeaderBg`: `#1E293B` | `cardBorder`: `#334155` (`1.0pt`, zero outer drop shadow)
  - `primary`: `#F8FAFC` (17.4:1 vs `#0F1117`) | `accent`: `#38BDF8` (9.6:1) | `focalDelta`: `#F59E0B` (9.1:1)
  - `textPrimary`: `#F1F5F9` (16.3:1) | `textSecondary`: `#94A3B8` (6.8:1) | `textMuted`: `#64748B` (3.7:1 footer only)
  - `sideNoteBg`: `#172554` | `sideNoteBorder`: `#1E40AF` | `sideNoteAccent`: `#38BDF8` | `sideNoteText`: `#E0F2FE`
  - `badgeBg`: `#1E293B` | `badgeText`: `#38BDF8` | `highlightBg`: `#422006` | `highlightText`: `#FCD34D`
  - **Table & Delta Semantics**: `tableRule`: `#475569` | `sotaRowBg`: `#1E293B` | `positiveDelta`: `#34D399` | `negativeDelta`: `#F87171`.
- **Colorblind-Safe Dark-Stage Chart Series**: `["#38BDF8", "#F59E0B", "#34D399", "#FB7185", "#A78BFA", "#94A3B8"]`

> [!WARNING]
> **Mandatory White-Background PDF Figure Protocol for `keynote_dark_oral`**:
> Harvested academic PDF figures almost always have opaque `#FFFFFF` backgrounds. Dropping a raw `#FFFFFF` rectangle directly onto `#0F1117` creates an amateurish "glaring white sticker" flash. When using `keynote_dark_oral`, apply **one** of these two clean treatments:
> 1. **Rounded Crisp Matte Frame (Default Safe Rule — 100% fidelity)**: Place a solid `#FFFFFF` (or `#F8FAFC`) `roundRect` container (`cornerRadius: 0.08"`, internal padding `0.12"`, subtle `1pt` `#475569` border) behind the figure so the white viewport looks like an intentional gallery plate, **never** touching dark card text directly.
> 2. **Selective Vector/Line-Plot Re-Plotting**: Re-render pure 1D/2D benchmark curves or native tables directly using the dark palette tokens (`#161B26` fill, `#94A3B8` axes). **NEVER** run bitwise color inversion (`255 - RGB`) on photographs, heatmaps, microscopy, or multi-color scatter plots!

---

### 1.3 Drop-In `THEMES` JSON Dictionary (Compatible with `template_config.json` & `build_deck.js`)

```json
{
  "academic_mono": {
    "id": "academic_mono", "name": "Academic Minimalist Grayscale",
    "background": "FFFFFF", "cardBg": "FFFFFF", "cardHeaderBg": "F9FAFB", "cardBorder": "D1D5DB",
    "primary": "000000", "accent": "111827", "secondary": "374151", "focalDelta": "111827",
    "textPrimary": "111827", "textSecondary": "4B5563", "textMuted": "6B7280",
    "sideNoteBg": "F9FAFB", "sideNoteBorder": "374151", "sideNoteAccent": "111827", "sideNoteText": "111827",
    "highlightBg": "F3F4F6", "highlightText": "000000", "badgeBg": "F3F4F6", "badgeText": "111827"
  },
  "oxford_navy": {
    "id": "oxford_navy", "name": "Oxford Institutional Navy",
    "background": "FFFFFF", "cardBg": "FFFFFF", "cardHeaderBg": "F8FAFC", "cardBorder": "CBD5E1",
    "primary": "002147", "accent": "1D4ED8", "secondary": "334155", "focalDelta": "B91C1C",
    "textPrimary": "0F172A", "textSecondary": "334155", "textMuted": "64748B",
    "sideNoteBg": "EFF6FF", "sideNoteBorder": "BFDBFE", "sideNoteAccent": "002147", "sideNoteText": "1E3A8A",
    "highlightBg": "FEF2F2", "highlightText": "991B1B", "badgeBg": "EFF6FF", "badgeText": "002147"
  },
  "nature_slate_teal": {
    "id": "nature_slate_teal", "name": "Nature Journal Slate & Teal",
    "background": "FFFFFF", "cardBg": "FFFFFF", "cardHeaderBg": "F8FAFC", "cardBorder": "E2E8F0",
    "primary": "0F3D3E", "accent": "0F766E", "secondary": "475569", "focalDelta": "C2410C",
    "textPrimary": "1E293B", "textSecondary": "475569", "textMuted": "64748B",
    "sideNoteBg": "F0FDFA", "sideNoteBorder": "99F6E4", "sideNoteAccent": "0F766E", "sideNoteText": "134E4A",
    "highlightBg": "FFF7ED", "highlightText": "9A3412", "badgeBg": "CCFBF1", "badgeText": "115E59"
  },
  "mit_crimson_neutral": {
    "id": "mit_crimson_neutral", "name": "MIT Engineering Crimson & Stone",
    "background": "FFFFFF", "cardBg": "FFFFFF", "cardHeaderBg": "FAFAF9", "cardBorder": "D6D3D1",
    "primary": "18181B", "accent": "A31F34", "secondary": "44403C", "focalDelta": "0369A1",
    "textPrimary": "18181B", "textSecondary": "44403C", "textMuted": "78716C",
    "sideNoteBg": "FAFAF9", "sideNoteBorder": "E7E5E4", "sideNoteAccent": "A31F34", "sideNoteText": "292524",
    "highlightBg": "FEF2F2", "highlightText": "A31F34", "badgeBg": "FEF2F2", "badgeText": "991B1B"
  },
  "cvpr_clean_blue": {
    "id": "cvpr_clean_blue", "name": "CVPR Clean Cobalt & Slate",
    "background": "FFFFFF", "cardBg": "FFFFFF", "cardHeaderBg": "F8FAFC", "cardBorder": "E2E8F0",
    "primary": "0F172A", "accent": "0284C7", "secondary": "334155", "focalDelta": "B45309",
    "textPrimary": "0F172A", "textSecondary": "334155", "textMuted": "64748B",
    "sideNoteBg": "F0F9FF", "sideNoteBorder": "BAE6FD", "sideNoteAccent": "0284C7", "sideNoteText": "0C4A6E",
    "highlightBg": "FEF3C7", "highlightText": "92400E", "badgeBg": "E0F2FE", "badgeText": "075985"
  },
  "keynote_dark_oral": {
    "id": "keynote_dark_oral", "name": "Keynote Dark Stage Oral",
    "background": "0F1117", "cardBg": "161B26", "cardHeaderBg": "1E293B", "cardBorder": "334155",
    "primary": "F8FAFC", "accent": "38BDF8", "secondary": "94A3B8", "focalDelta": "F59E0B",
    "textPrimary": "F1F5F9", "textSecondary": "94A3B8", "textMuted": "64748B",
    "sideNoteBg": "172554", "sideNoteBorder": "1E40AF", "sideNoteAccent": "38BDF8", "sideNoteText": "E0F2FE",
    "highlightBg": "422006", "highlightText": "FCD34D", "badgeBg": "1E293B", "badgeText": "38BDF8"
  }
}
```

---

## 2. Strict Anti-AI-Slop Visual Rules (去AI视觉廉价感十诫)

Reviewers and seminar audiences spot generic LLM/SaaS-generated slides in under 500 milliseconds. Enforce these **10 deterministic visual hygiene laws** without exception:

| # | Anti-Slop Law | ❌ AI-Slop Tell (Strictly Banned) | ✅ Scholarly Publication Standard (Required) |
|:---|:---|:---|:---|
| **1** | **Ban AI Purple-Indigo Gradients** | Linear/radial gradients (`#6366F1 → #A855F7 → #EC4899`), gradient headline text, glowing aurora blobs | **100% solid flat fills** from the 6 curated scholarly palettes; zero gradient fills on backgrounds, cards, or typography |
| **2** | **Zero Emoji Bullet Soup** | Emoji prefixes on bullets or headers (`🚀 Fast Inference`, `💡 Key Insight`, `🔥 SOTA Results`, `🧠 Memory`) | Clean typographic numerals (`01`, `02`, `①`, `②`), crisp square bullets (`▪`), or bold text lead-ins (`Latency:`) |
| **3** | **Kill "3-Equal-Bento-Cards" Autopilot** | Repeating 3 identical rounded Bento boxes with top icons on 4+ consecutive slides regardless of content | **Layout variety driven by figure geometry**: alternate panorama top/bottom, 62/38 split, `booktabs` table, OMML workbench, and 2×2 matrix; **never repeat the exact same grid on >2 adjacent slides** |
| **4** | **Zero AI Sci-Fi Filler Art** | DALL-E / Midjourney glowing 3D brains, isometric neon server cubes, abstract glass spheres, cartoon clipart | **100% authentic empirical visuals**: cropped 300+ DPI paper figures, clean vector block diagrams, or real data plots. If no figure exists, use structured typographic synthesis |
| **5** | **Eliminate Nested "Box-in-Box" Clutter** | Putting a bordered box inside a bordered card inside a tinted background panel ("套娃边框") + heavy drop shadows | **Max 1 container depth level**. Card stroke `0.75–1.0pt` subtle gray (`#D1D5DB`/`#E2E8F0`), corner radius `0.06"–0.08"` (never pill `>0.12"`), shadow **off** (or `opacity <= 0.04, blur <= 4pt`). For clean white-bg figures, prefer **frameless placement**! |
| **6** | **Ban Full-Width Colored Title Banners** | Heavy 1.2-inch dark blue/red top ribbon bars across every slide (1990s corporate/old Beamer template look) | Clean open top header: `10pt` accent tracker pill + bold dark headline on `#FFFFFF` + `0.75pt` hairline rule at `y = 1.500"` |
| **7** | **Tufte `booktabs` Table Discipline** | Default PowerPoint rainbow header fills, heavy zebra striping, thick vertical gridlines around every cell | **Zero vertical lines**. Horizontal rules only: top rule `1.5pt`, header separator `0.75pt`, bottom rule `1.5pt`; subtle tint *only* on the "Ours" row; **bold** 1st, <u>underline</u> 2nd |
| **8** | **Ban Meaningless Gauges & Fake Progress Bars** | Circular percentage donuts or progress bars for non-partitioned metrics (e.g., a bar fill for `BLEU = 34.2`) | Exact tabular numerals + explicit baseline delta badge (`34.2 BLEU (+2.9 vs. Transformer)`) or calibrated axis bar chart |
| **9** | **Zero Decorative Corner Shapes & Watermarks** | Triangles/circles floating in slide corners, giant low-opacity gear/atom watermarks behind text | Pure, unobstructed margin gutters (`0.600"` left/right, `0.350"` top) |
| **10** | **Zero Flashy Slide Animations** | Fly-in, bounce, spiral, blinds, 3D cube transitions | Static crisp slides (or subtle progressive step-reveal via separate slides / instant fade for complex math derivations) |

---

## 3. Master 16:9 Coordinate Space & Aspect-Ratio Geometry Engine

### 3.1 Physical, EMU & Pixel Reference Grid
All coordinates `(x, y, w, h)` are specified in **inches** from the **top-left origin `(0.000, 0.000)`**:
- **Canvas Size**: `W = 13.333"` (`12,192,000 EMU`, `1920 px @ 144 DPI`, `2000 px @ 150 DPI`) $\times$ `H = 7.500"` (`6,858,000 EMU`, `1080 px @ 144 DPI`, `1125 px @ 150 DPI`).
- **Outer Safe Margins**: Left `M_L = 0.600"`, Right `M_R = 0.600"` (Right boundary `X_max = 12.733"`), Top `M_T = 0.350"`, Bottom `M_B = 0.150"`.
- **Usable Horizontal Span (`W_usable`)**: `12.733 - 0.600 = 12.133"`.

### 3.2 Standard 3-Zone Vertical Partition (Slides 2–14)

| Zone | Element | `x` (in) | `y` (in) | `w` (in) | `h` (in) | Styling & Collision Notes |
|:---|:---|:---|:---|:---|:---|:---|
| **Header** | `tracker_pill` | `0.600` | `0.350` | `8.000` | `0.240` | `10pt Bold` section eyebrow / pill |
| **Header** | `slide_title_1line` | `0.600` | `0.610` | `12.133` | `0.460` | `24–26pt Bold` single-line claim (+ `subtitle` below) |
| **Header** | `slide_subtitle` | `0.600` | `1.090` | `12.133` | `0.340` | `14–15pt` secondary takeaway or metric context |
| **Header** | `slide_title_2line` *(Alt)* | `0.600` | `0.610` | `12.133` | `0.800` | Use when Assertion Headline wraps to 2 lines (**omit `slide_subtitle`** to prevent vertical collision!) |
| **Header** | `header_divider` | `0.600` | `1.500` | `12.133` | `0.012` | `0.75pt` subtle horizontal rule (`cardBorder` or `primary`) |
| **Content** | **`content_viewport`** | **`0.600`** | **`1.650`** | **`12.133`** | **`5.200`** | **All cards, figures, OMML math & tables live in `y ∈ [1.650, 6.850]`** |
| **Footer** | `footer_citation` | `0.600` | `7.000` | `9.500` | `0.300` | `10pt` `textMuted`: `[FirstAuthor et al., Venue Year]` |
| **Footer** | `footer_pagenum` | `10.500` | `7.000` | `2.233` | `0.300` | `10pt` right-aligned: `08 / 14` |

### 3.3 Aspect-Ratio-Driven Layout Selector & `fitContain` Formula

Never pick a slide layout before inspecting the pixel dimensions $(W_{\text{px}}, H_{\text{px}})$ of the harvested figure! Compute $R = W_{\text{px}} / H_{\text{px}}$ and route deterministically:

- **$R > 2.0$ (Wide Panorama Pipeline / Multi-Stage Timeline)** $\rightarrow$ **Recipe 02 (`panorama_arch_top_bottom`)**
- **$1.15 \le R \le 2.0$ (Standard Landscape Plot / Architecture / Heatmap)** $\rightarrow$ **Recipe 03 (`asymmetric_62_38_figure_left`)** or **Recipe 06 (`split_65_35_sidenote`)**
- **$0.85 \le R < 1.15$ (Square Confusion Matrix / Scatter / Latent t-SNE)** $\rightarrow$ **Recipe 05 (`split_equal_50_50_ab`)** or **Recipe 03**
- **$R < 0.85$ (Tall Portrait Flowchart / Algorithm / CONSORT Tree)** $\rightarrow$ **Recipe 04 (`tall_diagram_38_62_split`)**
- **Master Wide Table / Multi-Column SOTA Benchmark** $\rightarrow$ **Recipe 08 (`benchmark_table_kpi_strip`)**
- **4 Sub-Plots / Sensitivity Curves** $\rightarrow$ **Recipe 09 (`quadrant_2x2_ablation`)**

#### Exact Zero-Distortion Image Framing (`fitContain`)
Given target container box $(X_c, Y_c, W_c, H_c)$, internal padding $(P_x, P_y)$, and image pixel size $(W_{\text{px}}, H_{\text{px}})$ with aspect ratio $R = W_{\text{px}} / H_{\text{px}}$:
$$W_{\text{avail}} = W_c - 2 P_x, \quad H_{\text{avail}} = H_c - 2 P_y$$
$$W_{\text{img}} = \begin{cases} W_{\text{avail}} & \text{if } \dfrac{W_{\text{avail}}}{H_{\text{avail}}} \le R \\[6pt] H_{\text{avail}} \cdot R & \text{otherwise} \end{cases}, \qquad H_{\text{img}} = \frac{W_{\text{img}}}{R}$$
$$X_{\text{img}} = X_c + \frac{W_c - W_{\text{img}}}{2}, \qquad Y_{\text{img}} = Y_c + \frac{H_c - H_{\text{img}}}{2}$$

> [!TIP]
> **Dead-Space Prevention Rule**: If `fitContain` leaves $> 28\%$ empty vertical or horizontal margin inside $(W_c, H_c)$, **switch layout recipes** (e.g., from `split_65_35` to `panorama_arch_top_bottom` for wide figures, or `tall_diagram_38_62_split` for tall figures) instead of leaving awkward blank bands around a tiny shrunk image!

---

## 4. Twelve Concrete `(x, y, w, h)` Coordinate Layout Recipes (in Inches)

Every coordinate recipe below satisfies $x \ge 0.600''$, $x + w \le 12.733''$, and (for Content Zone slides) $1.650'' \le y < y + h \le 6.850''$ with $\ge 0.200''$ inter-card gutters. Internal card padding defaults to `padX = 0.240"`, `padY = 0.200"`.

---

### Recipe 01: `title_hero_split` — Opening Title, Metadata & Teaser Split
- **Use Cases**: Slide 1 Cover for Conference Talks, Journal Clubs, and Paper Overviews (pairs bibliographic metadata with the paper's Teaser / Core Trade-off Figure). *(For pure centered Thesis/NSFC formal covers without a teaser figure, set `title_stack` width to `12.133"` centered).*

```
0.60" ┌───────────────────────────────┐  ┌──────────────────────────────┐ 12.733"
0.85" │ [VENUE · YEAR BADGE]          │  │                              │
      │ Paper Title (28-32pt Bold)    │  │   TEASER / HERO FIGURE       │
      │ Authors & Affiliations        │  │   (Frameless or Clean Plate) │
5.35" └───────────────────────────────┘  └──────────────────────────────┘
5.65" ┌─────────────────────────────────────────────────────────────────┐
      │ CORE TAKEAWAY / 3 CONTRIBUTION PILLS STRIP                      │
6.85" └─────────────────────────────────────────────────────────────────┘
```

| Slot ID | Role | `x` | `y` | `w` | `h` | Typography / Styling |
|:---|:---|:---|:---|:---|:---|:---|
| `venue_badge` | Conference / Track Pill | `0.600` | `0.850` | `4.200` | `0.320` | `11pt Bold` `badgeBg` / `badgeText` |
| `paper_title` | Full Paper Title (2–3 lines) | `0.600` | `1.300` | `5.850` | `1.850` | `28–32pt Bold` `primary` (Title Case EN / Bold CN) |
| `authors_meta` | Authors, Affiliations, Links | `0.600` | `3.250` | `5.850` | `1.200` | `14pt` `textSecondary` + `12pt` `textMuted` |
| `presenter_box` | Presenter / Date / Lab | `0.600` | `4.550` | `5.850` | `0.800` | `13pt Medium` left `0.06"` accent rule |
| `teaser_canvas` | Right Teaser Figure Viewport | `6.750` | `0.850` | `5.983` | `4.500` | `fitContain` (`pad = 0.15"`) |
| `contrib_strip` | Bottom 1-Sentence Core Claim | `0.600` | `5.650` | `12.133` | `1.200` | `cardHeaderBg` fill, `14pt` key contribution summary |

---

### Recipe 02: `panorama_arch_top_bottom` — Wide Panorama Figure + Bottom 3-Col Dissection
- **Use Cases**: Wide end-to-end system architectures (Slide 8), multi-epoch evolutionary timelines (Slide 5), wide wet-lab/clinical workflows ($R = W/H > 2.0$).

```
1.650" ┌─────────────────────────────────────────────────────────────────┐
       │             TOP PANORAMA FIGURE VIEWPORT (h = 3.150")           │
4.800" └─────────────────────────────────────────────────────────────────┘
5.000" ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
       │ ① Stage / Module 1│  │ ② Stage / Module 2│  │ ③ Stage / Module 3│
6.850" └───────────────────┘  └───────────────────┘  └───────────────────┘
       0.600"                 4.728"                 8.856"        12.733"
```

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `hero_figure` | Wide Pipeline / Timeline | `0.600` | `1.650` | `12.133` | `3.150` | `fitContain` (`R ∈ [2.0, 3.8]`), frameless on `#FFFFFF` |
| `stage_card_1` | Mechanism Step ① | `0.600` | `5.000` | `3.877` | `1.850` | `16pt` header + `2` micro-bullets (`12–13pt`) |
| `stage_card_2` | Mechanism Step ② | `4.728` | `5.000` | `3.877` | `1.850` | `16pt` header + `2` micro-bullets (`12–13pt`) |
| `stage_card_3` | Mechanism Step ③ | `8.856` | `5.000` | `3.877` | `1.850` | `16pt` header + `2` micro-bullets (`12–13pt`) |

---

### Recipe 03: `asymmetric_62_38_figure_left` — Visual Left (62%) + Analysis & Sidenote Right (38%)
- **Use Cases**: Workhorse figure-dominant slide (Motivation failure modes, Pareto curves, Kaplan-Meier survival, DID event-study plots) with both analytical bullets and a compact marginal callout (`R ∈ [1.15, 2.0]`).

```
1.650" ┌──────────────────────────────────────┐  ┌───────────────────────┐
       │                                      │  │ ANALYTICAL DISSECTION │
       │      PRIMARY FIGURE VIEWPORT         │  │ • 3 anchored bullets  │
       │      (w = 7.450", h = 5.200")        │  ├───────────────────────┤ 5.100"
       │                                      │  │ 🔬 LAB SYNERGY CALLOUT│ 5.300"
6.850" └──────────────────────────────────────┘  └───────────────────────┘
       0.600"                           8.050"  8.300"             12.733"
```

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `figure_left` | Primary Empirical Plot / Diagram | `0.600` | `1.650` | `7.450` | `5.200` | `fitContain` + optional `11pt` source caption at bottom |
| `analysis_top` | Visual Dissection Card | `8.300` | `1.650` | `4.433` | `3.450` | `17pt` header + `3` bullets (`13–14pt`) |
| `synergy_bot` | Marginal Synergy / Verdict Box | `8.300` | `5.300` | `4.433` | `1.550` | `sideNoteBg` + `0.08"` left accent bar + `2` lines (`12–13pt`) |

---

### Recipe 04: `tall_diagram_38_62_split` — Portrait Flowchart Left (38%) + Stacked Stages Right (62%)
- **Use Cases**: Tall vertical architectures, CONSORT clinical trial flowcharts, compiler passes, vertical multi-layer neural blocks, recursive algorithms ($R < 0.90$).

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `tall_figure` | Portrait Diagram / Flowchart | `0.600` | `1.650` | `4.550` | `5.200` | `fitContain` (`R ∈ [0.45, 0.90]`) |
| `row_stage_1` | Top Mechanism / Phase Card | `5.400` | `1.650` | `7.333` | `1.600` | Horizontal card: left badge + `16pt` header + `2` bullets |
| `row_stage_2` | Middle Mechanism / Phase Card | `5.400` | `3.450` | `7.333` | `1.600` | Horizontal card: left badge + `16pt` header + `2` bullets |
| `row_stage_3` | Bottom Complexity / Verdict Card | `5.400` | `5.250` | `7.333` | `1.600` | Includes inline OMML complexity or quantified gain |

---

### Recipe 05: `split_equal_50_50_ab` — Balanced 50/50 Dual Comparison (Prior Art vs. Ours)
- **Use Cases**: Slide 4 Bottleneck vs. Hypothesis, Slide 6 Inputs vs. Invariants, Slide 13 Core Contributions vs. Critical Limitations, Before/After visual comparisons (`gap = 0.301"`).

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `left_panel` | Baseline Bottleneck / Claim A | `0.600` | `1.650` | `5.916` | `5.200` | Top `0.06"` muted gray bar; figure (`h=2.90"`) + `3` bullets |
| `right_panel` | Proposed Solution / Critique B | `6.817` | `1.650` | `5.916` | `5.200` | Top `0.06"` `accent` bar; matched viewport (`h=2.90"`) + `3` bullets |

---

### Recipe 06: `split_65_35_sidenote` — Main Technical Canvas (65%) + Full-Height Sidenote (35%)
- **Use Cases**: Classic `cs-report-ppt` seminar layout when a deep 5-Class Laboratory Research Synergy callout (`[Mechanistic Interpretability]`, `[Own Lab Synergy]`) requires full vertical breathing room (`gap = 0.300"`).

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `main_card` | Figure + Core Technical Claims | `0.600` | `1.650` | `7.700` | `5.200` | Figure (`y=1.85, h=3.20`) + `2–3` anchored bullets below |
| `side_note` | Full-Height Research Sidenote | `8.600` | `1.650` | `4.133` | `5.200` | `sideNoteBg` fill, `0.08"` left `sideNoteAccent` bar (`x=8.600`), `3` bullets |

---

### Recipe 07: `formula_omml_workbench` — Native OMML Master Equation + Symbol Glossary & Intuition Plot
- **Use Cases**: Slide 7 Mathematical Formulation, Theoretical CS Theorem Box + Geometric Toy Example, Econometric Identification Specification (zero wall-of-proof clutter!).

```
1.650" ┌─────────────────────────────────────────────────────────────────┐
       │      MASTER NATIVE OMML EQUATION DISPLAY BOX (15-17pt Math)     │
3.400" └─────────────────────────────────────────────────────────────────┘
3.600" ┌─────────────────────────────────┐  ┌────────────────────────────┐
       │ TERM-BY-TERM SYMBOL GLOSSARY    │  │ GEOMETRIC INTUITION /      │
       │ • Color/role mapped variables   │  │ LOSS LANDSCAPE PLOT        │
6.850" └─────────────────────────────────┘  └────────────────────────────┘
       0.600"                     6.800"    7.050"                 12.733"
```

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `omml_hero` | Master Objective / Theorem Box | `0.600` | `1.650` | `12.133` | `1.750` | Centered DrawingML OMML (`15–17pt Cambria Math`) + 1-line label |
| `symbol_table` | Notation & Term Role Breakdown | `0.600` | `3.600` | `6.200` | `3.250` | `4–5` clean rows mapping symbol $\rightarrow$ physical/intuitive role |
| `intuition_fig` | 2D Toy Geometry / Spectral Plot | `7.050` | `3.600` | `5.683` | `3.250` | `fitContain` visual intuition proving *why* the equation works |

---

### Recipe 08: `benchmark_table_kpi_strip` — Master SOTA `booktabs` Table + Bottom KPI Badges
- **Use Cases**: Slide 10 Primary Quantitative Benchmarks, Economics 5-Row Focal Regression Table, Clinical Outcome Summary Table.

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `master_table` | `booktabs` Native Table / Crop | `0.600` | `1.650` | `12.133` | `3.650` | Max `7–9` rows $\times$ `6–8` cols (`12–13pt`), `sotaRowBg` on Ours |
| `kpi_badge_1` | Primary SOTA Gain Callout | `0.600` | `5.500` | `3.877` | `1.350` | Big `24pt Bold` metric (`+4.8% EM`) + `12pt` baseline context |
| `kpi_badge_2` | Efficiency / Speedup Callout | `4.728` | `5.500` | `3.877` | `1.350` | Big `24pt Bold` metric (`2.7× Faster`) + `12pt` hardware spec |
| `kpi_badge_3` | Parameter / OOD Robustness | `8.856` | `5.500` | `3.877` | `1.350` | Big `24pt Bold` metric (`−41% VRAM`) + `12pt` generalization verdict |

---

### Recipe 09: `quadrant_2x2_ablation` — Four-Quadrant $2 \times 2$ Ablation & Sensitivity Matrix
- **Use Cases**: Slide 12 Multi-dimensional Ablations (Component knock-out, Hyperparameter $\lambda$ sensitivity, Context/Batch scaling, Hardware latency breakdown; `gapX = 0.301"`, `gapY = 0.250"`).

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `quad_tl` | Ablation A: Component Drop | `0.600` | `1.650` | `5.916` | `2.475` | `15pt` header + sub-table/plot (`w=3.3"`) + right takeaway (`w=2.1"`) |
| `quad_tr` | Ablation B: Hyperparameter | `6.817` | `1.650` | `5.916` | `2.475` | `15pt` header + sensitivity curve + sweet-spot callout |
| `quad_bl` | Ablation C: Scaling Law | `0.600` | `4.375` | `5.916` | `2.475` | `15pt` header + scaling plot + slope/exponent note |
| `quad_br` | Ablation D: Edge / Failure Case | `6.817` | `4.375` | `5.916` | `2.475` | `15pt` header + boundary condition / failure regime diagnosis |

---

### Recipe 10: `grid_3col_taxonomy` — Three-Column Parallel Taxonomy, Protocol, or Roadmap
- **Use Cases**: Slide 3 Literature Taxonomy, Slide 9 Experimental Setup (Datasets / Baselines / Compute), Slide 14 Three-Phase Actionable Lab Roadmap (`gap = 0.251"`). *(Anti-Slop Rule: Never use on >2 consecutive slides!)*

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `col_1` | Stream 1 / Phase 1 Card | `0.600` | `1.650` | `3.877` | `5.200` | Top index tag `01` + `17pt` symmetric header + mini-diagram/3 bullets |
| `col_2` | Stream 2 / Phase 2 Card | `4.728` | `1.650` | `3.877` | `5.200` | Top index tag `02` + `17pt` symmetric header + mini-diagram/3 bullets |
| `col_3` | Stream 3 / Phase 3 (Target) | `8.856` | `1.650` | `3.877` | `5.200` | Highlighted `1.5pt` `accent` border + `03` + target positioning |

---

### Recipe 11: `qualitative_gallery_matrix` — Multi-Row Visual Comparison Grid (Input / Prior Art / Ours / GT)
- **Use Cases**: Computer Vision qualitative comparisons, Microscopy/Histology multi-stain panels, Robotics rollout frame strips, Generative restoration zoom-ins (`4` visual columns + right commentary rail).

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `col_headers` | 4 Method Labels (`w = 2.150` each) | `0.600` | `1.650` | `9.050` | `0.360` | `x = [0.600, 2.900, 5.200, 7.500]`, `13pt Bold` centered (`Ours` in `accent`) |
| `visual_row_1` | Sample Scene 1 (`4` cells) | `0.600` | `2.150` | `9.050` | `1.460` | Each cell `w = 2.150, h = 1.460` (`gapX = 0.150`), synchronized crop |
| `visual_row_2` | Sample Scene 2 (`4` cells) | `0.600` | `3.770` | `9.050` | `1.460` | Identical aspect lock across all 4 columns |
| `visual_row_3` | Sample Scene 3 (`4` cells) | `0.600` | `5.390` | `9.050` | `1.460` | Optional `1pt` crimson/amber zoom-in ROI indicator box |
| `verdict_rail` | Right Qualitative Takeaway Rail | `9.900` | `1.650` | `2.833` | `5.200` | Dissects specific visual artifacts fixed in Rows 1–3 (`12–13pt`) |

---

### Recipe 12: `defense_roadmap_tracker_canvas` — Thesis Defense / NSFC Grant Innovation Slide
- **Use Cases**: Chinese & International Master/PhD Defense (`硕博答辩核心创新点章节`) and NSFC Grant Reviews (`国自然研究内容/关键科学问题`), featuring a **5-segment persistent top progress bar** + Mechanism/Proof split + Bottom Innovation Verdict Banner.

```
0.320" ┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
       │ 01 立项依据   │ 02 总体路线   │[03 创新点二 ★]│ 04 系统实证   │ 05 总结展望   │
0.600" └──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
0.680"   动宾/量化结论式主标题（26pt 加粗，单行不折行）
1.650" ┌─────────────────────────────────────────┐  ┌─────────────────────────────┐
       │   核心方法机理图 / 算法架构 (w = 7.200") │  │  实证对比图表与消融证据       │
5.500" └─────────────────────────────────────────┘  └─────────────────────────────┘
5.700" ┌──────────────────────────────────────────────────────────────────────────┐
       │ ★ 本章核心突破小结：痛点 → 原始创新方法 → 关键指标增益 → 论文/专利成果支撑   │
6.850" └──────────────────────────────────────────────────────────────────────────┘
```

| Slot ID | Role | `x` | `y` | `w` | `h` | Content Constraint |
|:---|:---|:---|:---|:---|:---|:---|
| `nav_seg_1..5` | 5-Stage Top Progress Bar | `0.600` | `0.320` | `12.133` | `0.280` | 5 pills (`w = 2.346"`, `gap = 0.100"`); active chapter filled in `primary` |
| `defense_title` | Single-Line Conclusion Title | `0.600` | `0.680` | `12.133` | `0.480` | `26–28pt Bold` (`zh_defense` single-line claim); divider at `y = 1.500"` |
| `mech_canvas` | Left Innovation Architecture | `0.600` | `1.650` | `7.200` | `3.850` | High-DPI architecture diagram + `2` callout pointers |
| `proof_canvas` | Right Benchmark / Proof Card | `8.050` | `1.650` | `4.683` | `3.850` | Core SOTA sub-table or curve + quantified $\Delta$ highlight |
| `verdict_strip` | Bottom Closed-Loop Takeaway | `0.600` | `5.700` | `12.133` | `1.150` | `sideNoteBg` + left `0.08"` `focalDelta` bar; links innovation $\rightarrow$ published paper/patent |

---

## 5. Stage 4 Vision-in-the-Loop Spatial & Palette Audit Checklist

After rendering slides to `150+ DPI PNG` via `soffice` + `pdftoppm`/`pymupdf`, visually inspect every slide image (`view_file`) against these 8 geometric and chromatic gates:

1. **Zero Header-to-Content Collision**: Confirm `slide_title` (especially 2-line titles) never touches `header_divider` (`y = 1.500"`) or bleeds into `y = 1.650"` cards.
2. **Zero Card Overflow & Bottom Clipping**: Confirm bullet text, OMML equations, and table bottom rules terminate cleanly above `y = 6.850"`, leaving clear white space above the `y = 7.000"` footer.
3. **True Aspect Ratio (`s_x == s_y`)**: Visually verify circles are circular and embedded table fonts are unstretched.
4. **White-Box Seamlessness**: On light themes, confirm PDF figures sit on `#FFFFFF` with zero gray/pink background seams; on `keynote_dark_oral`, confirm `#FFFFFF` figures are framed inside clean padded `#FFFFFF`/`#F8FAFC` rounded plates.
5. **Dead-Space Ceiling (`< 25%` vacant void)**: If a figure card looks half-empty due to mismatched aspect ratio, switch between Recipes `02` (wide), `03` (landscape), and `04` (tall) and re-render.
6. **Layout Cadence Diversity**: Scan all slide thumbnails side-by-side; verify no 3 consecutive slides share an identical 3-column Bento grid.
7. **Anti-Slop Chromatic Purity**: Zero purple/neon gradients, zero emoji bullets, zero heavy drop shadows, and $\le 5\%$ saturated accent ink.
8. **WCAG Legibility Check**: Step back optically—every axis label, footnote, and badge must pass crisp high-contrast readability without squinting.
