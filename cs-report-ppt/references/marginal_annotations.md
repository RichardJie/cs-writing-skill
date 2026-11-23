# Marginal Annotations & Research Connection Taxonomy ("旁注" 规范)

In academic group seminars and lab presentations, a paper should not be reviewed in isolation. A presentation must bridge external methodological breakthroughs with the laboratory's own research agenda.

This specification defines the **5 Standardized Research Connection Classes**, visual callout styling, slide placement mappings, and concrete integration templates.

---

## 1. Taxonomy of Research Connection Classes

| # | Class Identifier | Scope & Theoretical Domain | Primary Trigger Scenarios | Target Slide Slot |
|---|------------------|----------------------------|---------------------------|-------------------|
| 1 | `[State Memory Inertia]` | Recurrent state retention, KV cache dynamics, context compression, historical activation decay. | Long-context models, state-space architectures (Mamba/S4), attention caching, memory-augmented networks. | Slide 2 / Slide 6 |
| 2 | `[Model Adaptivity / Generalization]` | Distribution shift resilience, OOD generalization, few-shot meta-adaptation, continual learning. | Domain adaptation, test-time compute, robustness under corruption, multi-task transfer. | Slide 2 / Slide 4 |
| 3 | `[Mechanistic Interpretability]` | Representation geometry, circuit discovery, attention head routing, feature superposition, polysemanticity. | Probing studies, sparse autoencoders (SAE), causal mediation analysis, steering vectors. | Slide 8 (Architecture) |
| 4 | `[Computational & Hardware Efficiency]` | FLOP reduction, memory bandwidth optimization, quantization (FP8/INT4), kernel fusion, parallelization. | Inference acceleration, hardware-software co-design, sparse compute, parameter pruning. | Slide 11 (Trade-offs) |
| 5 | `[Own Lab Synergy]` | Direct codebase migration, baseline replacement in ongoing projects, dataset re-use, collaborative hypotheses. | Direct overlap with active laboratory grant milestones or paper submissions. | Slide 5 / Slide 14 |

---

## 2. Visual Callout Card Styling Specification

Marginal research side-notes are rendered as dedicated callout cards using the `split_65_35` layout:

```
┌────────────────────────────────────────────────────────┐
│ ▌ 🔬 OUR RESEARCH CONNECTION                           │
│ ▌ Class: [State Memory Inertia]                        │
│ ▌                                                      │
│ ▌ Direct Bottleneck Resolution:                        │
│ ▌ • Latent KV compression reduces token cache memory   │
│ ▌   by 73%, resolving our agent multi-turn bottleneck. │
│ ▌                                                      │
│ ▌ Immediate Lab Action Item:                           │
│ ▌ • Benchmark rank-128 compression matrix on our       │
│ ▌   in-house long-context evaluation suite.            │
└────────────────────────────────────────────────────────┘
```

### Visual Styling Invariants:
1. **Container Dimensions**: Width: `4.133"`, Height: `5.200"`, Top: `1.650"`, Left: `8.600"`.
2. **Background Tint**: Soft pastel fill matched to conference theme:
   - NeurIPS: Soft Royal Tint (`#EFF6FF`)
   - ICML: Soft Teal Tint (`#F0FDFA`)
   - CVPR: Soft Rose Tint (`#FFF1F2`)
   - ICLR: Soft Purple Tint (`#FAF5FF`)
   - KDD: Soft Amber Tint (`#FEF3C7`)
3. **Left Accent Bar**: Solid `0.08"` thick vertical rectangle spanning the full card height (`h = 5.20"`), colored in theme `accent` (`#2563EB`, `#0D9488`, `#E11D48`, `#7C3AED`, `#D97706`).
4. **Header Badge**: `[ 🔬 OUR RESEARCH CONNECTION ]` in `11pt Bold Uppercase`.
5. **Class Pill**: `Class: [ClassName]` in `11pt Semi-bold`.
6. **Typography**:
   - Sub-headers (Labels): `12pt Bold`
   - Bullet text: `12pt Regular` (Line spacing: 1.25x)

---

## 3. Dedicated Slide Placement Rules

Marginal research annotations are selectively placed on 5 key slides of the 14-slide spine:

1. **Slide 2 (Background — Motivation & Discovery Context)**:
   - *Class*: `[State Memory Inertia]` or `[Model Adaptivity / Generalization]`
   - *Objective*: Explains how the paper's core problem context reflects bottlenecks in our lab.
2. **Slide 5 (Background — Historical Lineage & Affiliations)**:
   - *Class*: `[Own Lab Synergy]`
   - *Objective*: Identifies where our lab's current baseline sits relative to the paper's historical trajectory.
3. **Slide 8 (Methods — Technical Mechanism & Architecture)**:
   - *Class*: `[Mechanistic Interpretability]` or `[State Memory Inertia]`
   - *Objective*: Analyzes the internal mechanics of the paper and relevance to our circuit/architecture studies.
4. **Slide 11 (Results — Baseline Categories & Trade-off Analysis)**:
   - *Class*: `[Computational & Hardware Efficiency]`
   - *Objective*: Maps the paper's Pareto throughput/memory trade-offs to our lab's GPU cluster constraints.
5. **Slide 14 (Conclusion — Seminar Discussion & Lab Roadmap)**:
   - *Class*: `[Own Lab Synergy]`
   - *Objective*: Formulates a concrete, 3-stage actionable experimental roadmap for lab members.

---

## 4. Concrete Integration Templates & Examples

### Example 1: `[State Memory Inertia]` (Slide 2 or 6)
```json
{
  "type": "side_note",
  "badge": "🔬 OUR RESEARCH CONNECTION",
  "categoryClass": "[State Memory Inertia]",
  "title": "Relevance to Context Memory Scaling",
  "bullets": [
    {
      "label": "Observed Parallel",
      "text": "The authors' observation that KV cache memory exceeds compute FLOPs matches our 128k context agent profiling."
    },
    {
      "label": "Theoretical Overlap",
      "text": "Their low-rank projection preserves state decay rates while cutting cache footprint by 4x."
    },
    {
      "label": "Action Item",
      "text": "Profile our recurrent state cache with their rank-64 compression matrix."
    }
  ]
}
```

### Example 2: `[Model Adaptivity / Generalization]` (Slide 2 or 4)
```json
{
  "type": "side_note",
  "badge": "🔬 OUR RESEARCH CONNECTION",
  "categoryClass": "[Model Adaptivity / Generalization]",
  "title": "Out-of-Distribution Robustness",
  "bullets": [
    {
      "label": "Lab Benchmark Alignment",
      "text": "Addresses the severe distribution collapse observed in our cross-domain transfer experiments."
    },
    {
      "label": "Adaptation Efficiency",
      "text": "Requires only 100 test-time gradient steps to adapt without catastrophic forgetting."
    },
    {
      "label": "Action Item",
      "text": "Evaluate test-time adaptation loss on our perturbed sensor benchmark."
    }
  ]
}
```

### Example 3: `[Mechanistic Interpretability]` (Slide 8)
```json
{
  "type": "side_note",
  "badge": "🔬 OUR RESEARCH CONNECTION",
  "categoryClass": "[Mechanistic Interpretability]",
  "title": "Attention Head Routing & Circuit Analysis",
  "bullets": [
    {
      "label": "Circuit Dissection",
      "text": "Decoupled RoPE queries isolate positional encoding circuits from semantic content heads."
    },
    {
      "label": "Representation Geometry",
      "text": "Latent representations exhibit orthogonal subspace alignment across multi-head projections."
    },
    {
      "label": "Action Item",
      "text": "Apply our SAE feature extraction pipeline to the compressed latent vector c_t."
    }
  ]
}
```

### Example 4: `[Computational & Hardware Efficiency]` (Slide 11)
```json
{
  "type": "side_note",
  "badge": "🔬 OUR RESEARCH CONNECTION",
  "categoryClass": "[Computational & Hardware Efficiency]",
  "title": "Inference Latency & Cluster Scalability",
  "bullets": [
    {
      "label": "Hardware Throughput",
      "text": "Yields a 2.8x decoding throughput boost on single-GPU instances due to reduced memory traffic."
    },
    {
      "label": "Deployment Fit",
      "text": "Fits within our 24GB VRAM constraint without requiring multi-node tensor parallelism."
    },
    {
      "label": "Action Item",
      "text": "Benchmark FP8 quantized kernel execution on our RTX 4090 testbed."
    }
  ]
}
```

### Example 5: `[Own Lab Synergy]` (Slide 5 or 14)
```json
{
  "type": "side_note",
  "badge": "🔬 OUR RESEARCH CONNECTION",
  "categoryClass": "[Own Lab Synergy]",
  "title": "Actionable Laboratory Transfer Roadmap",
  "bullets": [
    {
      "label": "Week 1 (Reproduction)",
      "text": "Fork authors' open-source implementation and reproduce Table 1 on synthetic benchmarks."
    },
    {
      "label": "Week 2 (Integration)",
      "text": "Replace our baseline attention module in repo `project-alpha` with the decoupled MLA layer."
    },
    {
      "label": "Week 3 (Hypothesis Test)",
      "text": "Run ablation experiments comparing generalization under corrupted input conditions."
    }
  ]
}
```
