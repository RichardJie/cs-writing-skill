# Native DrawingML Architecture Flowcharts & Vector Diagram Guide

This specification defines the standards for generating high-fidelity, fully editable DrawingML vector architecture diagrams and multi-branch execution flowcharts in PowerPoint presentations (`academic-paper-presentation`).

---

## 1. Core Principles: Native Vector Primitives vs Static Bitmaps

Conference-grade academic presentations require razor-sharp vector diagrams that remain editable and scalable across arbitrary projector resolutions:

1. **Zero Blurry Bitmaps for System Schematics**: Architecture diagrams must be constructed from native PowerPoint OpenXML shape primitives (`roundRect`, `oval`, `rect`, `rightArrow`, `line`, connectors) or harvested high-DPI (300+) PDF vector assets.
2. **Distinct Component Taxonomy**:
   - **Proposed / Novel Modules**: Highlighted in warm amber/gold (`#FEF3C7` fill, `#F59E0B` border, `#92400E` text) with a `✦ PROPOSED / NOVEL` indicator badge.
   - **Baseline / Standard Modules**: Styled in clean cool blue/slate (`#E0F2FE` fill, `#0284C7` border, `#0F172A` text) with a `◼ BASELINE / INPUT` indicator badge.
   - **Loss / Terminal / Objective Nodes**: Rendered as native `oval` or circular nodes (`ShapeType.oval`).
   - **Data Tensors / Embeddings**: Rendered as crisp rectangular boxes (`ShapeType.rect`).

---

## 2. Diagram Coordinate & Canvas Specifications

Architecture diagrams typically occupy the `hero_1col` layout box ($W = 12.133'', H = 5.200'', X = 0.600'', Y = 1.650''$) or the 65% primary card in `split_65_35` ($W = 7.700'', H = 5.200''$).

```
0.60" ┌────────────────────────────────────────────────────────────────────────┐
      │ ▌ Slide 8: Technical Mechanism Architecture Diagram                    │
      │ ▌ [✦ PROPOSED / NOVEL]                         [◼ BASELINE / INPUT]    │
      ├────────────────────────────────────────────────────────────────────────┤
      │                                                                        │
      │   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐          │
      │   │  Input Data  │ ──> │ Tokenization │ ──> │ Multi-Head   │ ──┐       │
      │   │  (Baseline)  │     │   (Linear)   │     │  Attention   │   │       │
      │   └──────────────┘     └──────────────┘     └──────────────┘   │       │
      │                                                     │          ▼       │
      │                                                     │   ┌───────────┐  │
      │                                                     │   │ Loss / Obj│  │
      │                                                     ▼   │  (Oval)   │  │
      │                        ┌──────────────┐     ┌───────────┴──┐└───────────┘  │
      │                        │ State Flow   │ ──> │ Dual-Stream  │           │
      │                        │ (✦ Novel)    │     │ Fusion Block │           │
      │                        └──────────────┘     └──────────────┘           │
      │                                                                        │
      └────────────────────────────────────────────────────────────────────────┘
```

### Geometric Parameters:
- **Card Container**: `roundRect` with corner radius `0.08"`, solid white fill `#FFFFFF`, 1.5pt border `#E2E8F0`, soft drop shadow (`opacity: 0.05, blur: 5pt, offset: 2pt, angle: 45°`), and top accent strip ($h = 0.08''$, fill: `theme.accent`).
- **Internal Available Zone**: $X_{\text{start}} = box.x + 0.25'', Y_{\text{start}} = box.y + 0.65'', W_{\text{avail}} = box.w - 0.50'', H_{\text{avail}} = box.h - 0.85''$.
- **Module Box Radius**: `rectRadius: 0.08` (6–8 pt).
- **Module Stroke Width**: $1.5\text{ pt}$ for standard modules, $2.0\text{ pt}$ for novel/proposed modules.

---

## 3. Node & Connector Anatomy

### Node Specifications:
| Node Type | Shape Primitive | Fill Color | Border Color | Stroke Width | Text Color | Usage |
|---|---|---|---|---|---|---|
| **Novel Module** | `roundRect` | Theme `calloutBg` (`#FEF3C7`) | Theme `calloutBorder` (`#F59E0B`) | `2.0 pt` | `#92400E` | Proposed architectural innovations, novel recurrence mechanisms |
| **Baseline Module** | `roundRect` | Theme `badgeBg` (`#E0F2FE`) | Theme `accent` (`#0284C7`) | `1.5 pt` | `#0F172A` | Standard transformer blocks, feedforward layers, embeddings |
| **Terminal / Loss Node**| `oval` | `#FEE2E2` (Soft Red) | `#EF4444` (Rose Red) | `1.5 pt` | `#991B1B` | Objective functions, cross-entropy loss, Hamiltonian energy |
| **Data Tensor** | `rect` | `#F1F5F9` (Slate Tint) | `#94A3B8` (Slate Border) | `1.0 pt` | `#334155` | Input batches, hidden state matrices $S_t \in \mathbb{R}^{d \times d}$ |

### Connector & Flow Direction Primitives:
1. **Direct Sequential Data Flow**:
   - Primitive: `ShapeType.rightArrow`
   - Fill: Theme `secondary` (`#475569`) or theme `accent` (`#2563EB`)
   - Dimensions: Width $0.35''-0.50''$, Height $0.18''-0.22''$.
2. **Multi-Branching / Skip-Connections**:
   - Primitive: `ShapeType.line` with solid or dashed stroke (`dashType: 'dash'`) and labeled intermediate text badges.
3. **Branching Split / Fusion Nodes**:
   - Dual branches running in parallel (e.g. Row 1: Attention Flow; Row 2: Recurrent State Inertia Flow) merging into a downstream Fusion Block.

---

## 4. JSON Presentation IR Diagram Schema

Presentation slide IR definitions declare vector architecture diagrams via the `diagram` object:

```json
{
  "slide_index": 8,
  "section": "Methods",
  "title": "Technical Mechanism & System Architecture",
  "subtitle": "Dual-Inertia State Flow Transformer with Adaptive Gating",
  "diagram": {
    "title": "State Flow Transformer Execution Architecture",
    "nodes": [
      {
        "name": "Input Tokens x_t",
        "type": "baseline",
        "shape": "rect",
        "w": 1.8,
        "h": 0.8,
        "x": 0.05,
        "y": 0.3
      },
      {
        "name": "Local Sliding Attention",
        "type": "baseline",
        "shape": "roundRect",
        "w": 2.2,
        "h": 0.9,
        "x": 0.30,
        "y": 0.1
      },
      {
        "name": "Adaptive Inertia Gate α_t",
        "type": "novel",
        "highlight": true,
        "shape": "roundRect",
        "w": 2.2,
        "h": 0.9,
        "x": 0.30,
        "y": 0.55
      },
      {
        "name": "Dual-Stream Fusion Block",
        "type": "novel",
        "highlight": true,
        "shape": "roundRect",
        "w": 2.4,
        "h": 1.1,
        "x": 0.65,
        "y": 0.3
      },
      {
        "name": "Loss H(S_t)",
        "type": "terminal",
        "shape": "oval",
        "w": 1.2,
        "h": 1.2,
        "x": 0.92,
        "y": 0.3
      }
    ],
    "arrows": [
      { "x": 0.23, "y": 0.20, "w": 0.06, "h": 0.15, "color": "475569" },
      { "x": 0.23, "y": 0.60, "w": 0.06, "h": 0.15, "color": "F59E0B" },
      { "x": 0.53, "y": 0.20, "w": 0.10, "h": 0.15, "color": "475569" },
      { "x": 0.53, "y": 0.60, "w": 0.10, "h": 0.15, "color": "F59E0B" },
      { "x": 0.88, "y": 0.40, "w": 0.04, "h": 0.15, "color": "2563EB" }
    ]
  }
}
```

---

## 5. Verification Invariants

When evaluating vector diagrams during visual audits:
1. **Native OpenXML Validation**: Slides containing architecture diagrams must contain $>10$ native `<p:sp>` / `<a:spPr>` DrawingML shape tags and zero low-resolution raster blips.
2. **Scalability**: All node labels and connector arrowheads must render sharp and clear at 150+ DPI and 300+ DPI.
3. **Taxonomic Clarity**: Novel contributions must be immediately distinguishable from standard components at a single glance.
