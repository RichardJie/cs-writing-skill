#!/usr/bin/env python3
"""Report biomedical figure Python and R capabilities as JSON."""

from __future__ import annotations

import argparse
import importlib
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path


PYTHON_PACKAGES = (
    "matplotlib",
    "seaborn",
    "scipy",
    "plotnine",
    "cnsplots",
    "pandas",
    "numpy",
    "PIL",
    "yaml",
)
R_PACKAGES = (
    "ggplot2",
    "patchwork",
    "ggrepel",
    "ComplexHeatmap",
    "survival",
    "survminer",
    "forestplot",
    "pROC",
    "ragg",
    "svglite",
    "tiff",
)


def package_version(name: str) -> str | None:
    try:
        module = importlib.import_module(name)
    except Exception:
        return None
    version = getattr(module, "__version__", None)
    if version is None and name == "PIL":
        version = getattr(module, "PILLOW_VERSION", None)
    return str(version or "installed")


def find_rscript(explicit: str | None) -> str | None:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    located = shutil.which("Rscript")
    if located:
        candidates.append(Path(located))
    program_files = Path("C:/Program Files/R")
    if program_files.exists():
        candidates.extend(sorted(program_files.glob("R-*/bin/Rscript.exe"), reverse=True))
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate.resolve())
    return None


def r_version(executable: str | None) -> str | None:
    if not executable:
        return None
    completed = subprocess.run(
        [executable, "--version"], capture_output=True, text=True, check=False
    )
    output = (completed.stdout or completed.stderr).strip().splitlines()
    return output[0] if output else None


def r_package_versions(executable: str | None, library_path: Path | None) -> dict[str, str | None]:
    if not executable:
        return {name: None for name in R_PACKAGES}
    library_text = ""
    if library_path and library_path.is_dir():
        quoted_library = json.dumps(library_path.resolve().as_posix())
        library_text = f".libPaths(c({quoted_library}, .libPaths()));"
    package_vector = ",".join(json.dumps(name) for name in R_PACKAGES)
    expression = (
        library_text
        + f"pkgs <- c({package_vector});"
        + "for (p in pkgs) {"
        + "v <- if (requireNamespace(p, quietly=TRUE)) as.character(packageVersion(p)) else 'NOT_INSTALLED';"
        + "cat(p, v, sep='\\t'); cat('\\n')}"
    )
    completed = subprocess.run(
        [executable, "-e", expression], capture_output=True, text=True, check=False
    )
    versions = {name: None for name in R_PACKAGES}
    for line in completed.stdout.splitlines():
        if "\t" in line:
            name, version = line.split("\t", 1)
            if name in versions:
                versions[name] = None if version == "NOT_INSTALLED" else version
    return versions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rscript", help="Explicit Rscript executable")
    parser.add_argument("--r-library", type=Path, help="Optional project-local R library")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    rscript = find_rscript(args.rscript)
    report = {
        "platform": platform.platform(),
        "python": {
            "executable": sys.executable,
            "version": platform.python_version(),
            "packages": {name: package_version(name) for name in PYTHON_PACKAGES},
        },
        "r": {
            "executable": rscript,
            "version": r_version(rscript),
            "packages": r_package_versions(rscript, args.r_library),
        },
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    missing = [name for name, version in report["python"]["packages"].items() if version is None]
    missing_r = [name for name, version in report["r"]["packages"].items() if version is None]
    return 1 if missing or not rscript or missing_r else 0


if __name__ == "__main__":
    raise SystemExit(main())
