"""Audit raster geometry and figure metadata for common publication failures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


REQUIRED_METADATA = {
    "variable",
    "units",
    "statistic",
    "sample_size_n",
    "unit_of_independence",
    "uncertainty_definition",
    "data_kind",
    "palette",
    "vmin",
    "vmax",
    "final_width_mm",
    "minimum_font_pt",
    "comparison_family",
    "legend_file",
}


def audit(image_path: Path, metadata_path: Path, asset_role: str = "panel") -> list[str]:
    issues: list[str] = []
    if not image_path.exists():
        return [f"[FILE-01] missing image: {image_path}"]
    if not metadata_path.exists():
        return [f"[META-01] missing metadata: {metadata_path}"]

    with Image.open(image_path) as image:
        image = image.convert("RGBA")
        width, height = image.size
        if asset_role == "panel" and (width < 800 or height < 500):
            issues.append(f"[EXPORT-02] raster may be too small ({width}x{height} px)")
        if asset_role == "panel" and (width / max(height, 1) > 6 or height / max(width, 1) > 6):
            issues.append("[LAYOUT-01] extreme aspect ratio; verify labels and assembly placement")
        background = image.getpixel((0, 0))
        border = []
        border.extend(image.crop((0, 0, width, 2)).getdata())
        border.extend(image.crop((0, height - 2, width, height)).getdata())
        border.extend(image.crop((0, 0, 2, height)).getdata())
        border.extend(image.crop((width - 2, 0, width, height)).getdata())
        tolerance = 8
        if any(max(abs(pixel[i] - background[i]) for i in range(4)) > tolerance for pixel in border):
            issues.append("[LAYOUT-03] visible content touches the canvas edge; inspect labels for clipping")

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_METADATA - set(metadata))
    if missing:
        issues.append("[META-01] missing metadata fields: " + ", ".join(missing))
        return issues

    if not str(metadata["units"]).strip():
        issues.append("[UNIT-01] units are empty")
    for field in ("statistic", "sample_size_n", "unit_of_independence", "uncertainty_definition"):
        if not str(metadata[field]).strip():
            rule = {"statistic": "STAT-01", "sample_size_n": "STAT-02", "unit_of_independence": "STAT-02", "uncertainty_definition": "UNC-01"}[field]
            issues.append(f"[{rule}] {field} is empty; use an explicit value or 'not applicable'")
    if float(metadata["minimum_font_pt"]) < 13:
        issues.append("[FONT-01] minimum final font size is below 13 pt")
    if float(metadata["final_width_mm"]) <= 0:
        issues.append("[LAYOUT-02] final_width_mm must be positive")
    if float(metadata["vmin"]) >= float(metadata["vmax"]):
        issues.append("[SCALE-01] vmin must be smaller than vmax")
    if str(metadata["data_kind"]).lower() == "diverging":
        center = metadata.get("center")
        if center is None:
            issues.append("[COLOR-02] diverging data require an explicit center")
        elif float(center) == 0 and abs(float(metadata["vmin"]) + float(metadata["vmax"])) > 1e-8:
            issues.append("[COLOR-02] zero-centred diverging limits are not symmetric")
    palette = str(metadata["palette"]).lower()
    if "jet" in palette or "rainbow" in palette:
        issues.append("[COLOR-01] rainbow/jet palette is prohibited")
    legend_path = metadata_path.parent / str(metadata["legend_file"])
    if not legend_path.exists():
        issues.append(f"[LEGEND-01] standalone legend/colorbar not found: {legend_path.name}")
    if metadata.get("has_title", False):
        issues.append("[TITLE-01] plot title present; move identifying text to filename/caption")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("--asset-role", choices=("panel", "legend"), default="panel")
    args = parser.parse_args()
    issues = audit(args.image, args.metadata, args.asset_role)
    if issues:
        print("AUDIT FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("AUDIT PASSED: deterministic checks complete; visual inspection is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
