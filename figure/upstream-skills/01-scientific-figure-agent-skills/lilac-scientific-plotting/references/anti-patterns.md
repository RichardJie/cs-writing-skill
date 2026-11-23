# Anti-patterns

| Symptom | Why it misleads or impairs reading | Repair / source context |
|---|---|---|
| Pick a spectacular chart before defining the question | Geometry can obscure the estimand | Start with data/unit/question, pp.8-20 |
| Drop extreme bubbles to improve size balance | Deletes valid evidence | Transform/label the size scale or select a documented scientific subset, pp.37-40 |
| Move slopegraph points or replace NA by zero | Changes observations and creates false change | Preserve values and ID pairing; move labels only, pp.52-56 |
| Free-scale panels described as equal growth | Apparent slopes depend on scales/aspect | Fix axes or compare modeled rates, pp.50-51 |
| Smooth line with unspecified method | Automatic choices can change meaning | Explicit method/formula/level, pp.58-60 |
| CI-like bars with no definition | SD, SE, CI are different | State interval method and unit/n, pp.106-109 |
| Hard-coded R-squared or decorative significance | Detaches annotation from analysis | Compute from tested model, pp.122-130 |
| Cluster numeric category IDs | Arbitrary codes become fake distances | Use meaningful features or an explicit hierarchy, pp.82-84 |
| Map deletes missing regions | Missing data appears as absent geography | Left-join geometry and show NA fill, pp.149-161 |
| Independent second axis tuned for overlap | Visual correlation is engineered | Known invertible unit transform only, pp.187-188 |
| Tiny text to fit a dense panel | Becomes unreadable after reduction | Reduce clutter, wrap/orient labels, change layout, pp.181-184,189-205 |
| Remove every grid or duplicate encoding | Sacrifices value lookup or accessibility | Keep useful guides and purposeful redundancy, pp.173-179 |
| Enlarge bitmap and call it high resolution | Interpolation adds no information | Re-export from code at dimensions/DPI, pp.201-205 |

These repairs are Codex implementation notes informed by the source. They do not claim the source itself rejects every listed practice. Source-specific errors and API changes are tracked separately in [corrections](provenance-and-corrections.md).
