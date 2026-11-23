---
name: illustrator-edit
description: Safely refine, assemble, and export existing vector artwork in Adobe Illustrator (.ai, .svg, .eps, or PDF), especially scientific figures exported by Python, R, MATLAB, Origin, GIS, or network software and then manually adjusted. Use when Codex must preserve manual label placement while adjusting typography, consolidating fragmented imported text, refining annotations or legends, assembling panels, editing layers or vector paths, or producing publication exports through Illustrator MCP. Do not use it to analyze raw data, choose statistical methods, or generate data-driven plots that should be reproducible in code.
---

# Illustrator Edit

Use Illustrator as the final vector-editing stage, not as the default data-plotting engine.

## Keep the Workflow Split

```text
data and analysis
→ Python / R / MATLAB / other analytical backend
→ SVG or PDF
→ Illustrator working copy
→ vector refinement and verified export
```

- Route data selection, transformations, statistics, axes, scales, uncertainty, mark generation, and repeatable plotting to `mse-figure` and the existing analytical code.
- Use this skill after the analytical figure is fixed, or for non-data vector artwork that already exists.
- Do not use Illustrator Graph tools as a default replacement for Python, R, or Origin. Use them only when the user explicitly requests a simple manually maintained chart.

## Honor a Manual Layout Master

If a figure was generated in code and then manually adjusted, treat the current SVG or AI file as the authoritative layout master.

- Do not rerun Python, R, MATLAB, or Origin merely to change fonts, spacing, labels, or other vector styling. Rerun analytical code only when data, axes, mappings, or results must change and the user authorizes it.
- Preserve manually placed label anchors, leader lines, and data geometry. A font change can alter glyph bounds; compensate only within the explicitly permitted text or legend objects.
- Never replace a manual layout with an automatically re-laid-out figure just because the code is reproducible.

## Freeze the Edit Contract

Record the exact objects and properties permitted to change before writing.

Normally permitted:

- text contents supplied by the user;
- fonts, sizes, spacing, alignment, and panel-label hierarchy;
- legend position and layout without changing category mapping;
- multi-panel assembly, margins, artboards, grouping, and layer visibility;
- non-analytical strokes, fills, paths, clipping masks, and annotations;
- PDF, SVG, EPS, AI, and raster review exports.

Require explicit authorization before changing:

- data marks, paths, bars, points, flows, or network geometry;
- axis values, limits, transformations, units, or tick labels;
- category identities or color, shape, and size mappings;
- thresholds, uncertainty, significance, exclusions, or statistical results.

For a data-backed scientific figure, keep the `mse-figure` evidence gate and visual QA requirements.

## Protect the Source

1. Resolve the exact source path and record its SHA-256 hash.
2. Copy the source to a task-specific temporary directory or approved output path.
3. Open only the copy and read `get_document_info.documentRef`. Pass that exact value as `expected_document` for every edit, save, close, and export. The MCP checks it in the same JSX execution as the action; a separately verified active document is not sufficient.
4. Prefer a one-time SVG/PDF-copy → AI-working-copy conversion. Do not repeatedly round-trip the source.
5. Call `save_document(mode="save")` only when the active path exactly equals the approved AI working copy.
6. After save-as, read the new `documentRef` before further actions. Close the working document with its current `expected_document` and `save=false` after the intended copy has been saved.
7. Re-hash the source at handoff.

If the active path is missing, ambiguous, or points to the source, stop before writing.

## Version Material Edits

- Before a substantial crop, panel rearrangement, typography hierarchy change, or broad label-layout pass, copy the latest verified AI file to the next sequential name: `_v1.ai`, `_v2.ai`, `_v3.ai`, and so on. Ordinary font, label-content, and minor label-position edits do not require an extra material-edit version beyond the approved working copy.
- Open and write only the new version. Never overwrite an earlier verified version during a material edit.
- Give review previews the same version stem. Keep internal moderate-resolution QA previews distinct from final publication exports.
- Record the parent version and the permitted edit contract before writing.

## Prefer the Quiet MCP

Use the registered `illustrator-silent` server when available. Its launcher in [scripts/silent_server.py](scripts/silent_server.py) copies the pinned upstream 1.6.2 package from `~/Documents/Codex/mcp-servers/illustrator-mcp/1.6.2/node_modules/illustrator-mcp-server` to a temporary runtime. In that copy it removes explicit foreground-activation flags, raises ordinary/heavy JSX timeouts to 90/240 seconds by default, routes native open/save/close through the heavy timeout, normalizes artboard coordinates, adds character-range text styling to `modify_object`, and registers `batch_modify_text`. It does not modify the installed package. The source package and its dependency lock are kept in that dedicated tool directory; npm cache discovery is disabled. A missing package or a different version is an explicit startup failure, not permission to download or upgrade. Restore the approved runtime or obtain approval for an upgrade and revalidate the patches.

Check the existing registration with `codex mcp get illustrator-silent` and the live tool schema first. `batch_modify_text`, `modify_object`, `save_document`, and `close_document` must expose the required `expected_document` parameter. If it is absent, the task still has an old connection; reconnect before editing.

`python3 scripts/silent_server.py --probe` **prepares a runtime and writes temporary files**. Use it during installation or authorized integration maintenance, not as a read-only health check or before every artwork edit. A prepared runtime reports:

- `runtime_activation_flags_remaining: 0`;
- the intended ordinary and heavy timeout values;
- `character_runs_enabled: true`;
- `native_object_ids_enabled`, `document_binding_enabled`, and `cross_process_lock_enabled` as `true`;
- `safe_artboard_coordinates_enabled: true`;
- `batch_modify_text_enabled: true`;
- `applescript_timeout_enabled: true`;
- `open_uses_heavy_timeout`, `save_uses_heavy_timeout`, and `close_uses_heavy_timeout` as `true`.

Override the defaults only when justified:

```bash
python3 scripts/silent_server.py --probe --normal-timeout-ms 120000 --heavy-timeout-ms 300000
```

Do not install or upgrade Node, Python, npm packages, Illustrator, or other dependencies during an ordinary edit without approval. Use one MCP server process per task. Updated servers share an execution lock for the entire tool call; `ILLUSTRATOR_BUSY` means another task currently owns Illustrator and no action started. Do not retry repeatedly or use an old server to bypass it. Legacy connections do not participate in this lock.

Object reads return `native:` IDs without modifying object notes. Always use IDs read from the bound document. An ambiguous legacy note ID is rejected; read fresh native IDs rather than selecting the first match. For an unsaved document, use the exact `unsaved:` reference from `get_document_info` only for the initial save-as, then use the resulting file reference.

The patch-v7 runtime is built separately from older runtimes. The launcher and registered tool set are not hot-reloaded. After changing this skill or wrapper, start a fresh MCP process before claiming that the new behavior is active.

When raw stdio diagnosis is unavoidable, use newline-delimited JSON-RPC. Do not use `Content-Length` framing or repeatedly start `npx` processes.

## Separate Tool Repair from Artwork Editing

Do not develop or repair the Illustrator integration inside an active artwork-editing task. If progress would require changing `silent_server.py`, the installed MCP package, this skill, MCP registration, or timeout-layer code, stop the artwork workflow and move that work to a separate diagnostic task. Starting a fresh process from the existing registered server is ordinary recovery, not tool repair.

## Choose the Smallest Safe Edit Cycle

Use the ordinary cycle when changes are limited to text contents, fonts, sizes, alignment, or minor label positioning and do not alter data marks, analytical coordinates, category mappings, artboards, or panel geometry:

1. Open the approved working copy once and verify the active path.
2. Inspect only the target objects, required fonts, and coordinate context needed for the requested edit. Pass `coordinate_system` explicitly for every coordinate-bearing read or write.
3. Use `batch_modify_text` for supported text properties, including a single text frame, to obtain full preflight and attribute readback. Pass `expected_document`, explicit coordinates, and only the approved object IDs and properties. Use `modify_object` for other properties and verify them separately.
4. Export one moderate-resolution modified preview and inspect the actual image.
5. Save once, close, reopen the same working copy, verify its path, and export one reopened preview.
6. Require the reopened preview to match the saved modified preview, then close without saving and verify the source hash. Otherwise stop and mark the discrepancy `待核验`.

Do not create a separate baseline export for an ordinary edit when a trustworthy source or existing preview already provides the visual reference.

Use the full QA cycle only when changing data marks or geometry; axis values, limits, transformations, or analytical mappings; category color, shape, or size encodings; artboard bounds; panel assembly; or other large-scale layout. For this cycle, export a clean baseline, inspect the affected structure, apply the coherent edit, compare baseline and modified previews for localized differences, then save, close, reopen, export again, and compare the reopened result.

Do not rely on `undo` as recovery. Close without saving and reopen the last verified AI working copy.

For `batch_modify_text`, inspect `phase`, each `status`, `changed_fields`, and `verified.text_runs`:

- `preflight_rejected`: the entire batch was rejected before writing; fix the reported object, font, or character-range issue.
- `verified`: requested fields matched actual readback.
- `partial`: some fields changed; compare the returned state before proposing a smaller remaining edit.
- `needs_verification`: readback failed; inspect the bound document before any further write.
- `not_applied`: that item was not completed; check whether a prior item stopped the batch.

An error is not proof of zero changes. The MCP does not roll back a partial edit or automatically replay it. Preserve the save/reopen verification cycle.

## Resize Artboards Without Guessing

The quiet runtime gives `manage_artboards` the same top-left rectangle contract used by `get_artboards`:

- `document`: `x` and `y` are the native Illustrator coordinates of the requested top-left corner; width extends right and height extends down;
- `artboard-web`: `x` and `y` are offsets right and down from the target artboard's current top-left corner.

Always call `get_artboards` with an explicit coordinate system, then call `manage_artboards` with that same coordinate system. Do not pass `rawPosition.y` into a document-coordinate resize formula. After resizing, require the verified position and size to equal the intended rectangle and export a fresh preview before moving artwork or saving.

The upstream 1.6.2 `manage_artboards` interface uses a different Y-origin convention. Do not bypass the quiet wrapper for artboard edits unless the conversion has been independently checked.

## Handle Imported Objects Carefully

- Use `list_fonts` and exact PostScript font names such as `ArialMT`; a family name such as `Arial` can fail.
- SVG imports can split formulas, subscripts, units, or rotated axis titles into single-character text frames.
- Prefer stable complete labels over fragmented text. Inspect contents, font, bounds, clipping, and layer before and after editing.
- When unifying a font family, use `list_fonts` to map existing regular, bold, italic, and bold-italic semantics to installed PostScript names in the target family. Do not flatten emphasis or hierarchy unless the user requests it. Assign the mapped font to every nonblank text frame, then require every nonblank frame to report the intended family after save and reopen. Preserve existing sizes unless the user requests a hierarchy change.
- Avoid ungrouping or outlining text unless the user explicitly accepts the loss of editability.
- Treat a whole-layout shift after SVG/PDF import as unresolved; do not correct it by eye against the source.

### Consolidate a Fragmented Logical Label

For a title or formula that should be one editable label:

1. Record the aggregate bounds or center of the visible fragments and identify the stable main text frame.
2. Put the complete logical text in that main frame.
3. Use `character_runs` for subscripts, superscripts, or mixed sizes instead of separate positioned frames. Indices are zero-based; `start` is inclusive and `end` is exclusive.
4. Recenter only the reconstructed label against its recorded aggregate bounds. Do not move country labels, data marks, axes, or leader lines.
5. Clear or remove obsolete fragments only after the reconstructed label renders correctly. If deletion is unavailable, leave them blank and report the residual blank-frame count.

Example `batch_modify_text` request for a final `2` that must be 7 pt inside a 10.8 pt title:

```json
{
  "expected_document": "/absolute/path/to/approved-working-copy.ai",
  "coordinate_system": "document",
  "items": [{
    "uuid": "native:ID-returned-by-a-read",
    "properties": {
      "contents": "Cross-border transfer (kt CO2)",
      "font_name": "TimesNewRomanPSMT",
      "font_size": 10.8,
      "character_runs": [
        {"start": 28, "end": 29, "font_size": 7, "baseline_shift": 0}
      ]
    }
  }]
}
```

Calculate the actual character indices from the final string; never copy example indices blindly. Verify the rendered result because baseline treatment varies by source artwork.

## Treat Foreground and Timeout Behavior Honestly

The quiet server can keep open, read, modify, and PNG export operations in the background. Illustrator may still surface itself during native save or close. Batch those operations once.

The upstream server's 30/60-second JSX limits are too short for some deeply nested scientific figures. The quiet wrapper uses 90/240 seconds by default, routes open/save/close through the heavy channel, and keeps the AppleEvent timeout 30 seconds longer than the matching process timeout. Do not increase one timeout layer while leaving another shorter.

If a tool times out after a visible action may already have occurred, do not repeat it. First inspect `get_document_info`; for a save, also compare the expected file's path, size, modification time, and hash, then reopen and render the candidate if the disk file changed. Retry only when the active path is verified, the operation is confirmed not to have taken effect, and the expected disk file remained unchanged. Retry the same ordinary operation at most once. If that retry also times out or fails, stop and mark the result `待核验`; do not extend timeouts or repair the MCP inside the artwork task. If `open_document` times out from Illustrator's home screen, verify the UI and use an approved app-opening fallback only when needed; confirm the exact active path before any save.

`close_document(save=false)` can time out after the document has already closed. Re-probe with `get_document_info` before retrying; never close an unverified active document.

Read [references/known-limitations.md](references/known-limitations.md) when diagnosing focus changes, timeouts, font substitution, SVG fragmentation, or import/export instability.

## Handoff

Report:

- source and working-copy paths;
- parent and resulting version names for every material edit;
- permitted changes actually applied;
- source hash before and after;
- active-path verification before save;
- for full QA, baseline-versus-modified difference bounds or an equivalent deterministic comparison;
- whether saved and reopened previews match;
- verification results for the requested target text frames; when relevant, global nonblank font counts, combined-title count, and any residual blank fragments after consolidation;
- visual QA result and any `待核验` issue.
