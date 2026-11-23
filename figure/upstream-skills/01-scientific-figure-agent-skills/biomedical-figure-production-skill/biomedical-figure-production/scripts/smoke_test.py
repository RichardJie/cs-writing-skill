#!/usr/bin/env python3
"""Generate synthetic, clearly labelled figure exports for environment testing."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import cnsplots  # noqa: E402,F401 - verifies the optional publication plotting layer
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260801)
    group_a = rng.normal(0.0, 1.0, 24)
    group_b = rng.normal(0.75, 1.0, 24)

    sns.set_theme(style="ticks", context="paper")
    fig, ax = plt.subplots(figsize=(3.35, 2.7))
    sns.boxplot(data=[group_a, group_b], width=0.5, color="white", ax=ax)
    sns.stripplot(data=[group_a, group_b], jitter=0.18, size=3.2, palette=["#2878B5", "#D55E00"], ax=ax)
    ax.set_xticks([0, 1], labels=["Synthetic A", "Synthetic B"])
    ax.set_ylabel("Synthetic response (a.u.)")
    ax.set_title("Environment smoke test — not research data", fontsize=9)
    sns.despine(ax=ax)
    fig.tight_layout()

    stem = args.output_dir / "biomedical_figure_smoke_test"
    fig.savefig(stem.with_suffix(".png"), dpi=300)
    fig.savefig(stem.with_suffix(".tiff"), dpi=600, pil_kwargs={"compression": "tiff_lzw"})
    fig.savefig(stem.with_suffix(".svg"))
    plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
