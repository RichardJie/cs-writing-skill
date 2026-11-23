"""Minimal use of the skill's Matplotlib helpers."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from figure_style import (  # noqa: E402
    apply_nature_style,
    export_publication_figure,
    pooled_limits,
    scientific_norm,
    semantic_cmap,
    write_figure_metadata,
)


def main() -> None:
    output = Path(__file__).resolve().parent / "output"
    output.mkdir(exist_ok=True)
    rng = np.random.default_rng(7)
    fields = [rng.normal(loc=offset, scale=1.2, size=(30, 40)) for offset in (-0.3, 0.3)]
    vmin, vmax = pooled_limits(fields, center=0)

    apply_nature_style(scale=1.0)
    panel_paths = []
    image = None
    for scenario, field in zip(("baseline", "future"), fields):
        fig, ax = plt.subplots(figsize=(3.25, 2.8), layout="constrained")
        image = ax.imshow(
            field,
            cmap=semantic_cmap("temperature", "diverging"),
            norm=scientific_norm(vmin, vmax, center=0),
        )
        ax.set_xlabel("Grid column")
        ax.set_ylabel("Grid row")
        panel_path = output / f"temperature_anomaly_{scenario}.png"
        export_publication_figure(fig, panel_path.with_suffix(""), dpi=600)
        plt.close(fig)
        panel_paths.append(panel_path.name)

    assert image is not None
    colorbar_fig, colorbar_ax = plt.subplots(figsize=(3.8, 0.95), layout="constrained")
    colorbar_fig.colorbar(image, cax=colorbar_ax, orientation="horizontal", label="Temperature anomaly (°C)")
    colorbar_path = output / "colorbar_temperature_anomaly.png"
    colorbar_fig.savefig(colorbar_path, dpi=300)
    plt.close(colorbar_fig)

    write_figure_metadata(
        output / "temperature_anomaly_comparison.figure.json",
        {
            "variable": "temperature anomaly",
            "units": "°C",
            "statistic": "synthetic grid-cell value",
            "sample_size_n": "not applicable",
            "unit_of_independence": "not applicable",
            "uncertainty_definition": "not applicable; no uncertainty marks are shown",
            "data_kind": "diverging",
            "palette": "cmocean.balance or RdBu_r fallback",
            "vmin": vmin,
            "vmax": vmax,
            "center": 0,
            "final_width_mm": 170,
            "minimum_font_pt": 13.0,
            "comparison_family": "temperature_anomaly",
            "panel_files": panel_paths,
            "panel_identifiers": False,
            "legend_file": colorbar_path.name,
            "has_title": False,
        },
    )


if __name__ == "__main__":
    main()
