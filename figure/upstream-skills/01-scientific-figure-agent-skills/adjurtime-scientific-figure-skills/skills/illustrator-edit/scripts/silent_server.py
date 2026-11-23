#!/usr/bin/env python3
"""Start a temporary, quiet Illustrator MCP runtime with safer text editing."""

from __future__ import annotations

import argparse
import hashlib
import sys
import json
import os
import re
import shutil
import tempfile
from pathlib import Path


PACKAGE_NAME = "illustrator-mcp-server"
WRAPPER_PATCH_VERSION = 7
SUPPORTED_PACKAGE_VERSION = "1.6.2"
MANAGED_PACKAGE = (Path.home() / "Documents/Codex/mcp-servers/illustrator-mcp"
                   / SUPPORTED_PACKAGE_VERSION / "node_modules" / PACKAGE_NAME)
DEFAULT_NORMAL_TIMEOUT_MS = 90_000
DEFAULT_HEAVY_TIMEOUT_MS = 240_000


CHARACTER_RUNS_JSX = '''

      // illustrator-edit: character-runs
      if (props.character_runs) {
        try {
          for (var cri = 0; cri < props.character_runs.length; cri++) {
            var run = props.character_runs[cri];
            var startIndex = Math.max(0, Math.floor(run.start));
            var endIndex = Math.min(item.characters.length, Math.floor(run.end));
            if (endIndex <= startIndex) {
              errors.push("character_runs[" + cri + "]: empty or out-of-range interval");
              continue;
            }
            var runFont = null;
            if (run.font_name) {
              runFont = app.textFonts.getByName(run.font_name);
            }
            for (var ci = startIndex; ci < endIndex; ci++) {
              var runAttrs = item.characters[ci].characterAttributes;
              if (runFont) runAttrs.textFont = runFont;
              if (typeof run.font_size === "number") runAttrs.size = run.font_size;
              if (typeof run.baseline_shift === "number") runAttrs.baselineShift = run.baseline_shift;
            }
          }
        } catch(e) { errors.push("character_runs: " + e.message); }
      }
'''


CHARACTER_RUNS_SCHEMA = '''
                character_runs: z
                    .array(z.object({
                    start: z.number().int().min(0),
                    end: z.number().int().min(1),
                    font_name: z.string().optional(),
                    font_size: z.number().optional(),
                    baseline_shift: z.number().optional(),
                }))
                    .optional()
                    .describe('Character-range overrides. start is inclusive and end is exclusive.'),
'''


RUNTIME_SOURCES = Path(__file__).resolve().parent / "runtime"
BATCH_MODIFY_TEXT_JS = (RUNTIME_SOURCES / "batch-modify-text.js").read_text(encoding="utf-8")



def package_metadata(package_dir: Path) -> dict:
    return json.loads((package_dir / "package.json").read_text(encoding="utf-8"))


def locate_package(explicit: str | None) -> Path:
    candidate = explicit or os.environ.get("ILLUSTRATOR_MCP_PACKAGE") or MANAGED_PACKAGE
    package_dir = Path(candidate).expanduser().resolve()
    if not (package_dir / "package.json").is_file():
        raise SystemExit(f"Pinned Illustrator package not found: {package_dir}. "
                         "Restore the approved tool runtime; npm cache fallback is disabled.")
    metadata = package_metadata(package_dir)
    if (metadata.get("name") != PACKAGE_NAME or
            metadata.get("version") != SUPPORTED_PACKAGE_VERSION):
        raise SystemExit(f"Unsupported Illustrator package: {metadata.get('name')} "
                         f"{metadata.get('version')}; this wrapper requires "
                         f"{PACKAGE_NAME} {SUPPORTED_PACKAGE_VERSION}. Validate upgrades explicitly.")
    if not (package_dir / "dist/index.js").is_file():
        raise SystemExit(f"Pinned Illustrator entrypoint is missing: {package_dir}")
    return package_dir


def locate_node(explicit: str | None) -> Path:
    candidate = explicit or os.environ.get("ILLUSTRATOR_MCP_NODE")
    if candidate:
        node = Path(candidate).expanduser().resolve()
    else:
        found = shutil.which("node")
        node = Path(found).resolve() if found else Path("/opt/homebrew/bin/node")
    if not node.is_file():
        raise SystemExit(f"Node executable not found: {node}")
    return node


def count_activation_flags(package_dir: Path) -> int:
    return sum(
        javascript.read_text(encoding="utf-8").count("activate: true")
        for javascript in (package_dir / "dist").rglob("*.js")
    )


def js_integer(value: int) -> str:
    return f"{value:,}".replace(",", "_")


def patch_timeouts(package_dir: Path, normal_ms: int, heavy_ms: int) -> None:
    runner = package_dir / "dist" / "executor" / "jsx-runner.js"
    text = runner.read_text(encoding="utf-8")
    text, normal_count = re.subn(
        r"const TIMEOUT_NORMAL = [0-9_]+;",
        f"const TIMEOUT_NORMAL = {js_integer(normal_ms)};",
        text,
    )
    text, heavy_count = re.subn(
        r"const TIMEOUT_HEAVY = [0-9_]+;",
        f"const TIMEOUT_HEAVY = {js_integer(heavy_ms)};",
        text,
    )
    if normal_count != 1 or heavy_count != 1:
        raise SystemExit(
            "Could not patch illustrator-mcp-server timeouts safely; inspect "
            f"{runner} before continuing."
        )
    runner.write_text(text, encoding="utf-8")


def patch_applescript_timeout(package_dir: Path) -> None:
    """Keep AppleEvent timeout longer than the matching Node process timeout."""
    transport = package_dir / "dist" / "executor" / "file-transport.js"
    text = transport.read_text(encoding="utf-8")
    if "illustrator-edit: appleevent-timeout" not in text:
        option_anchor = "    const activateLine = options?.activate ? '\\n  activate' : '';\n"
        option_replacement = option_anchor + (
            "    // illustrator-edit: appleevent-timeout\n"
            "    const timeoutSeconds = Math.max(1, Math.ceil((options?.timeoutMs ?? 60000) / 1000) + 30);\n"
        )
        default_anchor = '''        script = [
            `tell application "Adobe Illustrator"${activateLine}`,
            jsxLine,
            'end tell',
        ].join('\\n');
'''
        default_replacement = '''        script = [
            `with timeout of ${timeoutSeconds} seconds`,
            `tell application "Adobe Illustrator"${activateLine}`,
            jsxLine,
            'end tell',
            'end timeout',
        ].join('\\n');
'''
        app_anchor = '''        script = [
            `tell application "${appPathEscaped}"${activateLine}`,
            jsxLine,
            'end tell',
        ].join('\\n');
'''
        app_replacement = '''        script = [
            `with timeout of ${timeoutSeconds} seconds`,
            `tell application "${appPathEscaped}"${activateLine}`,
            jsxLine,
            'end tell',
            'end timeout',
        ].join('\\n');
'''
        replacements = (
            (option_anchor, option_replacement),
            (default_anchor, default_replacement),
            (app_anchor, app_replacement),
        )
        for anchor, replacement in replacements:
            if text.count(anchor) != 1:
                raise SystemExit(
                    "Could not patch the AppleEvent timeout safely; the upstream "
                    f"layout changed. Inspect {transport} before continuing."
                )
            text = text.replace(anchor, replacement, 1)
        transport.write_text(text, encoding="utf-8")

    runner = package_dir / "dist" / "executor" / "jsx-runner.js"
    runner_text = runner.read_text(encoding="utf-8")
    if "timeoutMs: timeout" not in runner_text:
        call_anchor = (
            "await writeAppleScript(files.runnerPath, files.scriptPath, "
            "{ activate, appPath: getAppPath() });"
        )
        call_replacement = (
            "await writeAppleScript(files.runnerPath, files.scriptPath, "
            "{ activate, appPath: getAppPath(), timeoutMs: timeout });"
        )
        if runner_text.count(call_anchor) != 1:
            raise SystemExit(
                "Could not pass the process timeout to AppleScript safely; inspect "
                f"{runner} before continuing."
            )
        runner.write_text(
            runner_text.replace(call_anchor, call_replacement, 1),
            encoding="utf-8",
        )


def patch_character_runs(package_dir: Path) -> None:
    modifier = package_dir / "dist" / "tools" / "modify" / "modify-object.js"
    text = modifier.read_text(encoding="utf-8")
    if "illustrator-edit: character-runs" in text:
        return

    jsx_anchor = '''
      if (typeof props.font_size === "number") {
        try {
          for (var ri2 = 0; ri2 < item.textRanges.length; ri2++) {
            item.textRanges[ri2].characterAttributes.size = props.font_size;
          }
        } catch(e) { errors.push("font_size: " + e.message); }
      }
'''
    schema_anchor = "                font_size: z.number().optional().describe('Font size (for text frames)'),\n"
    if text.count(jsx_anchor) != 1 or text.count(schema_anchor) != 1:
        raise SystemExit(
            "Could not add character_runs safely; the upstream modify_object layout changed. "
            f"Inspect {modifier} before continuing."
        )
    text = text.replace(jsx_anchor, jsx_anchor + CHARACTER_RUNS_JSX, 1)
    text = text.replace(schema_anchor, schema_anchor + CHARACTER_RUNS_SCHEMA, 1)
    modifier.write_text(text, encoding="utf-8")


def patch_native_document_ops(package_dir: Path) -> None:
    """Route deep-document open/save/close operations through the heavy timeout."""
    for filename in ("open-document.js", "save-document.js", "close-document.js"):
        tool = package_dir / "dist" / "tools" / "modify" / filename
        text = tool.read_text(encoding="utf-8")
        if "executeJsxHeavy" in text:
            continue
        import_anchor = (
            "import { executeJsx } from '../../executor/jsx-runner.js';"
        )
        call_anchor = (
            "const result = await executeJsx(jsxCode, params, { activate: false });"
        )
        if text.count(import_anchor) != 1 or text.count(call_anchor) != 1:
            raise SystemExit(
                f"Could not route {filename} through the heavy timeout safely; "
                f"inspect {tool} before continuing."
            )
        text = text.replace(
            import_anchor,
            "import { executeJsxHeavy } from '../../executor/jsx-runner.js';",
            1,
        )
        text = text.replace(
            call_anchor,
            "const result = await executeJsxHeavy(jsxCode, params);",
            1,
        )
        tool.write_text(text, encoding="utf-8")


def patch_artboard_coordinates(package_dir: Path) -> None:
    """Make manage_artboards consume the same top-left rect contract it reports."""
    tool = package_dir / "dist" / "tools" / "modify" / "manage-artboards.js"
    text = tool.read_text(encoding="utf-8")
    if "illustrator-edit: safe-artboard-coordinates" in text:
        return

    add_anchor = '''        var r = params.rect;
        // artboardRect = [left, top, right, bottom] (document coordinates, Y-up)
        var abRect = [r.x, r.y + r.height, r.x + r.width, r.y];
'''
    add_replacement = '''        var r = params.rect;
        var coordSystem = params.coordinate_system || "document";
        // illustrator-edit: safe-artboard-coordinates
        // x/y always identify the top-left corner. artboard-web is relative to
        // the active artboard; document uses native Illustrator coordinates.
        var abRect;
        if (coordSystem === "artboard-web") {
          var activeRect = getActiveArtboardRect();
          var addLeft = activeRect[0] + r.x;
          var addTop = activeRect[1] - r.y;
          abRect = [addLeft, addTop, addLeft + r.width, addTop - r.height];
        } else {
          abRect = [r.x, r.y, r.x + r.width, r.y - r.height];
        }
'''
    resize_anchor = '''        var r2 = params.rect;
        // Artboard.artboardRect = [left, top, right, bottom] (document coordinates, Y-up)
        doc.artboards[params.index].artboardRect = [r2.x, r2.y + r2.height, r2.x + r2.width, r2.y];
        var resizedRect = doc.artboards[params.index].artboardRect;
        writeResultFile(RESULT_PATH, { success: true, index: params.index, verified: { artboardRect: resizedRect } });
'''
    resize_replacement = '''        var r2 = params.rect;
        var coordSystem2 = params.coordinate_system || "document";
        var targetRect = doc.artboards[params.index].artboardRect;
        var newRect;
        if (coordSystem2 === "artboard-web") {
          var resizeLeft = targetRect[0] + r2.x;
          var resizeTop = targetRect[1] - r2.y;
          newRect = [resizeLeft, resizeTop, resizeLeft + r2.width, resizeTop - r2.height];
        } else {
          newRect = [r2.x, r2.y, r2.x + r2.width, r2.y - r2.height];
        }
        doc.artboards[params.index].artboardRect = newRect;
        invalidateArtboardCache();
        var resizedRect = doc.artboards[params.index].artboardRect;
        writeResultFile(RESULT_PATH, {
          success: true,
          index: params.index,
          coordinateSystem: coordSystem2,
          verified: {
            artboardRect: resizedRect,
            position: { x: resizedRect[0], y: resizedRect[1] },
            size: {
              width: resizedRect[2] - resizedRect[0],
              height: resizedRect[1] - resizedRect[3]
            }
          }
        });
'''
    schema_anchor = '''                .optional()
                .describe('Position and size for add/resize (document coordinates)'),
            name: z.string().optional().describe('New name for rename action'),
'''
    schema_replacement = '''                .optional()
                .describe('Top-left position and size for add/resize'),
            coordinate_system: z
                .enum(['artboard-web', 'document'])
                .optional()
                .default('document')
                .describe('Rect coordinates. document uses native top-left x/y; artboard-web uses x/y down and right from the current artboard top-left.'),
            name: z.string().optional().describe('New name for rename action'),
'''

    replacements = (
        (add_anchor, add_replacement),
        (resize_anchor, resize_replacement),
        (schema_anchor, schema_replacement),
    )
    for anchor, replacement in replacements:
        if text.count(anchor) != 1:
            raise SystemExit(
                "Could not normalize manage_artboards coordinates safely; the "
                f"upstream layout changed. Inspect {tool} before continuing."
            )
        text = text.replace(anchor, replacement, 1)
    tool.write_text(text, encoding="utf-8")


def patch_batch_modify_text(package_dir: Path) -> None:
    """Add one heavy JSX operation for a verified set of text-frame edits."""
    tool = package_dir / "dist" / "tools" / "modify" / "batch-modify-text.js"
    tool.write_text(BATCH_MODIFY_TEXT_JS, encoding="utf-8")

    registry = package_dir / "dist" / "tools" / "registry.js"
    text = registry.read_text(encoding="utf-8")
    if "registerBatchModifyText" in text:
        return
    import_anchor = (
        "import { register as registerModifyObject } from './modify/modify-object.js';\n"
    )
    call_anchor = "    registerModifyObject(server);\n"
    if text.count(import_anchor) != 1 or text.count(call_anchor) != 1:
        raise SystemExit(
            "Could not register batch_modify_text safely; the upstream registry "
            f"layout changed. Inspect {registry} before continuing."
        )
    text = text.replace(
        import_anchor,
        import_anchor
        + "import { register as registerBatchModifyText } from './modify/batch-modify-text.js';\n",
        1,
    )
    text = text.replace(
        call_anchor,
        call_anchor + "    registerBatchModifyText(server);\n",
        1,
    )
    registry.write_text(text, encoding="utf-8")


def runtime_digest() -> str:
    digest = hashlib.sha256(Path(__file__).read_bytes())
    for path in sorted(RUNTIME_SOURCES.iterdir()):
        if path.is_file():
            digest.update(path.name.encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()[:12]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"Cannot apply {label}: expected one upstream anchor")
    return text.replace(old, new, 1)


def patch_phase1(package_dir: Path) -> None:
    dist = package_dir / "dist"
    for name in ("guarded-tools.js", "execution-lock.py"):
        shutil.copyfile(RUNTIME_SOURCES / name, dist / name)
    common = dist / "jsx/helpers/common.jsx"
    text = common.read_text()
    start = text.index("function ensureUUID(pageItem) {")
    end = text.index("// --- カラー変換 ---", start)
    text = text[:start] + text[end:]
    start = text.index("var _uuidIndex = null;")
    end = text.index("// --- レイヤー解決 ---", start)
    text = text[:start] + text[end:]
    common.write_text(text + "\n" + (RUNTIME_SOURCES / "document-helpers.jsx").read_text())

    duplicate = dist / "tools/modify/duplicate-objects.js"
    text = duplicate.read_text()
    start = text.index("        // 複製は元オブジェクト")
    end = text.index("        results.push", start)
    text = text[:start] + "        var newUuid = ensureUUID(dup);\n" + text[end:]
    duplicate.write_text(text)

    info = dist / "tools/read/get-document-info.js"
    text = replace_once(info.read_text(), "      filePath: filePath,", "      filePath: filePath,\n      documentRef: currentDocumentReference(),", "document reference readback")
    info.write_text(text)

    server = dist / "server.js"
    text = "import { installDocumentGuards } from './guarded-tools.js';\n" + server.read_text()
    text = replace_once(text, "    registerAllTools(server);", "    installDocumentGuards(server);\n    registerAllTools(server);", "tool guards")
    server.write_text(text)

    runner = dist / "executor/jsx-runner.js"
    text = "import { currentToolContext } from '../guarded-tools.js';\n" + runner.read_text()
    text = replace_once(text, "${toolScript}\n})();", """var guard = checkExpectedDocument(${JSON.stringify(currentToolContext().expectedDocument || null)});
if (guard) { writeResultFile(RESULT_PATH, guard); return; }
${toolScript}
})();""", "same-execution document guard")
    runner.write_text(text)


def inspect_runtime(package_dir: Path) -> dict:
    runner = package_dir / "dist" / "executor" / "jsx-runner.js"
    modifier = package_dir / "dist" / "tools" / "modify" / "modify-object.js"
    runner_text = runner.read_text(encoding="utf-8")
    modifier_text = modifier.read_text(encoding="utf-8")
    artboards_text = (
        package_dir / "dist" / "tools" / "modify" / "manage-artboards.js"
    ).read_text(encoding="utf-8")
    registry_text = (
        package_dir / "dist" / "tools" / "registry.js"
    ).read_text(encoding="utf-8")
    transport_text = (
        package_dir / "dist" / "executor" / "file-transport.js"
    ).read_text(encoding="utf-8")
    document_ops = {}
    for operation in ("open", "save", "close"):
        operation_text = (
            package_dir
            / "dist"
            / "tools"
            / "modify"
            / f"{operation}-document.js"
        ).read_text(encoding="utf-8")
        document_ops[f"{operation}_uses_heavy_timeout"] = (
            "executeJsxHeavy" in operation_text
        )
    normal_match = re.search(r"const TIMEOUT_NORMAL = ([0-9_]+);", runner_text)
    heavy_match = re.search(r"const TIMEOUT_HEAVY = ([0-9_]+);", runner_text)
    if not normal_match or not heavy_match:
        raise SystemExit("Could not inspect the patched MCP timeout values.")
    return {
        "normal_timeout_ms": int(normal_match.group(1).replace("_", "")),
        "heavy_timeout_ms": int(heavy_match.group(1).replace("_", "")),
        "character_runs_enabled": "illustrator-edit: character-runs" in modifier_text,
        "safe_artboard_coordinates_enabled": (
            "illustrator-edit: safe-artboard-coordinates" in artboards_text
        ),
        "native_object_ids_enabled": "illustrator-edit: native-object-id" in (package_dir / "dist/jsx/helpers/common.jsx").read_text(),
        "document_binding_enabled": "installDocumentGuards" in (package_dir / "dist/server.js").read_text(),
        "cross_process_lock_enabled": (package_dir / "dist/execution-lock.py").is_file(),
        "batch_modify_text_enabled": (
            "registerBatchModifyText" in registry_text
            and (
                package_dir
                / "dist"
                / "tools"
                / "modify"
                / "batch-modify-text.js"
            ).is_file()
        ),
        "applescript_timeout_enabled": (
            "illustrator-edit: appleevent-timeout" in transport_text
            and "timeoutMs: timeout" in runner_text
        ),
        **document_ops,
    }


def prepare_runtime(
    source: Path,
    normal_timeout_ms: int,
    heavy_timeout_ms: int,
) -> tuple[Path, int, dict]:
    metadata = package_metadata(source)
    version = str(metadata.get("version", "unknown"))
    source_flags = count_activation_flags(source)
    if source_flags == 0:
        raise SystemExit(
            "No activation flags were found. The upstream package may have changed; "
            "inspect it before using the quiet wrapper."
        )
    runtime_root = (
        Path(tempfile.gettempdir()).resolve()
        / f"codex-illustrator-mcp-silent-{version}-p{WRAPPER_PATCH_VERSION}-{runtime_digest()}"
    )
    runtime_package = runtime_root / "package"
    marker = runtime_root / "source.json"
    expected_marker = {
        "source": str(source),
        "version": version,
        "source_mtime_ns": (source / "package.json").stat().st_mtime_ns,
        "source_activation_flags": source_flags,
        "wrapper_patch_version": WRAPPER_PATCH_VERSION,
        "normal_timeout_ms": normal_timeout_ms,
        "heavy_timeout_ms": heavy_timeout_ms,
    }

    rebuild = True
    if marker.is_file() and runtime_package.is_dir():
        try:
            rebuild = json.loads(marker.read_text(encoding="utf-8")) != expected_marker
        except (OSError, json.JSONDecodeError):
            rebuild = True

    if rebuild:
        if runtime_root.exists():
            shutil.rmtree(runtime_root)
        runtime_root.mkdir(parents=True)
        shutil.copytree(source, runtime_package)
        dependency_link = runtime_root / "node_modules"
        dependency_link.symlink_to(source.parent, target_is_directory=True)

        for javascript in (runtime_package / "dist").rglob("*.js"):
            text = javascript.read_text(encoding="utf-8")
            patched = text.replace("activate: true", "activate: false")
            if patched != text:
                javascript.write_text(patched, encoding="utf-8")
        patch_timeouts(runtime_package, normal_timeout_ms, heavy_timeout_ms)
        patch_applescript_timeout(runtime_package)
        patch_character_runs(runtime_package)
        patch_native_document_ops(runtime_package)
        patch_artboard_coordinates(runtime_package)
        patch_batch_modify_text(runtime_package)
        patch_phase1(runtime_package)
        marker.write_text(
            json.dumps(expected_marker, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    entrypoint = runtime_package / "dist" / "index.js"
    if not entrypoint.is_file():
        raise SystemExit(f"MCP entrypoint not found: {entrypoint}")
    runtime_report = inspect_runtime(runtime_package)
    if runtime_report != {
        "normal_timeout_ms": normal_timeout_ms,
        "heavy_timeout_ms": heavy_timeout_ms,
        "character_runs_enabled": True,
        "native_object_ids_enabled": True,
        "document_binding_enabled": True,
        "cross_process_lock_enabled": True,
        "safe_artboard_coordinates_enabled": True,
        "batch_modify_text_enabled": True,
        "applescript_timeout_enabled": True,
        "open_uses_heavy_timeout": True,
        "save_uses_heavy_timeout": True,
        "close_uses_heavy_timeout": True,
    }:
        raise SystemExit(f"Unexpected patched runtime state: {runtime_report}")
    return entrypoint, source_flags, runtime_report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", help="Existing illustrator-mcp-server package directory")
    parser.add_argument("--node", help="Existing Node executable")
    parser.add_argument("--probe", action="store_true", help="Prepare and report without starting MCP")
    parser.add_argument(
        "--normal-timeout-ms",
        type=int,
        default=DEFAULT_NORMAL_TIMEOUT_MS,
        help=f"Timeout for ordinary JSX calls (default: {DEFAULT_NORMAL_TIMEOUT_MS})",
    )
    parser.add_argument(
        "--heavy-timeout-ms",
        type=int,
        default=DEFAULT_HEAVY_TIMEOUT_MS,
        help=f"Timeout for heavy JSX calls (default: {DEFAULT_HEAVY_TIMEOUT_MS})",
    )
    arguments = parser.parse_args()

    if arguments.normal_timeout_ms <= 0:
        parser.error("--normal-timeout-ms must be positive")
    if arguments.heavy_timeout_ms < arguments.normal_timeout_ms:
        parser.error("--heavy-timeout-ms must be greater than or equal to --normal-timeout-ms")

    source = locate_package(arguments.package)
    node = locate_node(arguments.node)
    entrypoint, source_flags, runtime_report = prepare_runtime(
        source,
        arguments.normal_timeout_ms,
        arguments.heavy_timeout_ms,
    )
    report = {
        "source_package": str(source),
        "source_version": package_metadata(source).get("version"),
        "node": str(node),
        "runtime_entrypoint": str(entrypoint),
        "source_activation_flags_removed_in_runtime": source_flags,
        "runtime_activation_flags_remaining": count_activation_flags(entrypoint.parent.parent),
        "wrapper_patch_version": WRAPPER_PATCH_VERSION,
        **runtime_report,
        "source_unchanged": True,
    }
    if arguments.probe:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    os.execv(str(node), [str(node), str(entrypoint)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
