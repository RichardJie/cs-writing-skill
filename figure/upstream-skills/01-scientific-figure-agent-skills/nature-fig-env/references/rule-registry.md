# Rule registry

Use these stable IDs in automated findings, QA notes, and revision records.

| Rule ID | Requirement |
|---|---|
| `FONT-01` | Every essential text element is at least 13 pt at final assembled size. |
| `FONT-02` | SVG/PDF text remains editable and is not converted to outlines or paths. |
| `FONT-03` | Actual text sizes can be determined from the exported vector artifact. |
| `STAT-01` | The plotted statistic or aggregation is explicitly identified. |
| `STAT-02` | Sample size `n` and its independent observational or experimental unit are stated. |
| `UNC-01` | Every error bar, interval, band, whisker, or ensemble envelope is defined. |
| `UNIT-01` | Axes and colorbars state the quantity and units. |
| `COLOR-01` | Rainbow and jet are prohibited for ordered scientific data. |
| `COLOR-02` | Signed changes use the correct neutral centre, normally symmetric around zero. |
| `COLOR-03` | Directly comparable panels share colormaps, limits, normalization, and category colors. |
| `SCALE-01` | Axis and color limits are valid and scientifically defensible. |
| `PANEL-01` | Each scientific panel is exported as a separate file by default. |
| `PANEL-02` | Panel identifiers such as a/b/c are omitted unless explicitly requested. |
| `LEGEND-01` | Legend or colorbar is exported separately and is available beside the panel files. |
| `TITLE-01` | In-plot titles are omitted unless explicitly required. |
| `GRID-01` | Background grids are absent unless they materially improve quantitative reading. |
| `LAYOUT-01` | Labels and graphical elements fit inside the canvas without overlap or extreme geometry. |
| `LAYOUT-02` | Intended final physical dimensions are recorded and positive. |
| `LAYOUT-03` | Visible content, especially text, remains inside the canvas and does not touch the export boundary. |
| `EXPORT-01` | Editable SVG and PDF are delivered for vector-compatible figures. |
| `EXPORT-02` | Required raster companion has adequate dimensions and resolution. |
| `META-01` | The figure metadata sidecar exists and includes every required field. |
| `FILE-01` | Required figure files exist and can be opened. |
| `FILE-02` | Plotting source is readable and syntactically valid for static audit. |

An intentional exception must name the rule ID, scientific or journal reason, affected file, and approving user instruction.
