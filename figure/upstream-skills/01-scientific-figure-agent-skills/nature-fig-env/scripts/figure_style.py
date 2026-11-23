"""Reusable Matplotlib helpers for environmental and energy-system figures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Colormap, Normalize, TwoSlopeNorm


FONT_FAMILY = ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"]


def apply_nature_style(scale: float = 1.0, grid: bool = False) -> None:
    """Apply clean, enlarged defaults suitable for later panel assembly."""
    if scale <= 0:
        raise ValueError("scale must be positive")
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": FONT_FAMILY,
            "font.size": 13.0 * scale,
            "axes.labelsize": 15.0 * scale,
            "xtick.labelsize": 13.0 * scale,
            "ytick.labelsize": 13.0 * scale,
            "legend.fontsize": 13.0 * scale,
            "axes.titlesize": 15.0 * scale,
            "axes.titleweight": "normal",
            "axes.grid": grid,
            "grid.alpha": 0.18,
            "grid.linewidth": 0.45,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.7,
            "lines.linewidth": 1.2 * scale,
            "lines.markersize": 4.0 * scale,
            "xtick.major.width": 0.7,
            "ytick.major.width": 0.7,
            "xtick.major.size": 3.0,
            "ytick.major.size": 3.0,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.03,
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def _cmocean(name: str) -> Colormap | None:
    try:
        import cmocean  # type: ignore

        return getattr(cmocean.cm, name)
    except (ImportError, AttributeError):
        return None


def semantic_cmap(topic: str, data_kind: str = "sequential") -> Colormap:
    """Return a restrained palette from data structure and domain semantics."""
    topic_key = topic.lower().strip()
    kind = data_kind.lower().strip()
    if kind == "diverging":
        ocean = _cmocean("balance")
        return ocean if ocean is not None else mpl.colormaps["RdBu_r"]
    if kind == "cyclic":
        ocean = _cmocean("phase")
        return ocean if ocean is not None else mpl.colormaps["twilight"]
    if kind != "sequential":
        raise ValueError("data_kind must be sequential, diverging, or cyclic")

    candidates = {
        "ocean": ("deep", "Blues"),
        "water": ("deep", "Blues"),
        "precipitation": ("rain", "YlGnBu"),
        "temperature": ("thermal", "inferno"),
        "heat": ("thermal", "inferno"),
        "vegetation": ("algae", "YlGn"),
        "greenness": ("algae", "YlGn"),
        "air pollution": ("matter", "magma"),
        "ozone": ("matter", "magma"),
        "pm2.5": ("matter", "magma"),
        "hazard": ("matter", "magma"),
        "risk": ("matter", "magma"),
        "mortality": ("matter", "magma"),
        "energy": ("tempo", "viridis"),
        "capacity": ("tempo", "viridis"),
        "infrastructure": ("tempo", "cividis"),
    }
    cmo_name, fallback = candidates.get(topic_key, ("tempo", "viridis"))
    ocean = _cmocean(cmo_name)
    return ocean if ocean is not None else mpl.colormaps[fallback]


def pooled_limits(
    arrays: Iterable[np.ndarray | Sequence[float]],
    *,
    robust_percentiles: tuple[float, float] | None = (2.0, 98.0),
    center: float | None = None,
) -> tuple[float, float]:
    """Compute shared limits across a comparison family."""
    values = [np.asarray(a, dtype=float).ravel() for a in arrays]
    finite_parts = [a[np.isfinite(a)] for a in values if a.size]
    if not finite_parts:
        raise ValueError("no finite values supplied")
    finite = np.concatenate(finite_parts)
    if finite.size == 0:
        raise ValueError("no finite values supplied")
    if robust_percentiles is None:
        low, high = float(finite.min()), float(finite.max())
    else:
        q0, q1 = robust_percentiles
        if not (0 <= q0 < q1 <= 100):
            raise ValueError("robust_percentiles must satisfy 0 <= low < high <= 100")
        low, high = (float(x) for x in np.percentile(finite, [q0, q1]))
    if center is not None:
        radius = max(abs(low - center), abs(high - center))
        low, high = center - radius, center + radius
    if low == high:
        pad = 1.0 if low == 0 else abs(low) * 0.05
        low, high = low - pad, high + pad
    return low, high


def scientific_norm(vmin: float, vmax: float, center: float | None = None) -> Normalize:
    """Create a normalizer, centring signed quantities on zero by default upstream."""
    if not np.isfinite([vmin, vmax]).all() or vmin >= vmax:
        raise ValueError("vmin and vmax must be finite with vmin < vmax")
    if center is None:
        return Normalize(vmin=vmin, vmax=vmax)
    if not vmin < center < vmax:
        raise ValueError("center must lie strictly between vmin and vmax")
    return TwoSlopeNorm(vmin=vmin, vcenter=center, vmax=vmax)


def export_standalone_legend(
    handles: Sequence,
    labels: Sequence[str],
    output: str | Path,
    *,
    ncol: int | None = None,
    fontsize: float = 13.0,
    frameon: bool = False,
    dpi: int = 300,
) -> Path:
    """Export a tightly cropped legend independent of the main plot."""
    if len(handles) != len(labels) or not labels:
        raise ValueError("handles and labels must be non-empty and equal in length")
    if ncol is None:
        ncol = len(labels) if len(labels) <= 4 and max(map(len, labels)) <= 18 else 1
    ncol = max(1, min(int(ncol), len(labels)))
    fig = plt.figure(figsize=(max(2.0, 1.2 * ncol), max(0.35, 0.28 * np.ceil(len(labels) / ncol))))
    legend = fig.legend(
        handles,
        labels,
        loc="center",
        ncol=ncol,
        frameon=frameon,
        fontsize=fontsize,
        handlelength=2.2,
        columnspacing=1.2,
    )
    fig.canvas.draw()
    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches=bbox.expanded(1.04, 1.12), dpi=dpi, transparent=True)
    plt.close(fig)
    return output_path


def export_publication_figure(
    fig,
    output_stem: str | Path,
    *,
    dpi: int = 600,
    raster_format: str = "png",
) -> dict[str, Path]:
    """Export editable SVG/PDF plus one high-resolution raster companion."""
    stem = Path(output_stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    raster = raster_format.lower().lstrip(".")
    if raster not in {"png", "tif", "tiff"}:
        raise ValueError("raster_format must be png, tif, or tiff")
    outputs = {
        "svg": stem.with_suffix(".svg"),
        "pdf": stem.with_suffix(".pdf"),
        raster: stem.with_suffix(f".{raster}"),
    }
    fig.savefig(outputs["svg"], format="svg")
    fig.savefig(outputs["pdf"], format="pdf")
    fig.savefig(outputs[raster], format=raster, dpi=dpi)
    return outputs


def write_figure_metadata(output: str | Path, metadata: Mapping) -> Path:
    """Write a JSON sidecar used by the deterministic audit helper."""
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dict(metadata), indent=2, ensure_ascii=False), encoding="utf-8")
    return path


if __name__ == "__main__":
    apply_nature_style(scale=1.25)
    x = np.linspace(-3, 3, 200)
    y = np.sin(x)
    fig, ax = plt.subplots(figsize=(3.4, 2.2), layout="constrained")
    line = ax.plot(x, y, color="#287D8E", label="Example scenario")[0]
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Standardized response")
    ax.legend().remove()
    demo_dir = Path(__file__).resolve().parent / "_demo"
    demo_dir.mkdir(exist_ok=True)
    fig.savefig(demo_dir / "example.png", dpi=200)
    export_standalone_legend([line], [line.get_label()], demo_dir / "legend_example.png")
    plt.close(fig)
