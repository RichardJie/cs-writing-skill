"""Reusable matplotlib style + palette for an 'Origin clean' journal figure look.

Cross-platform: tries to register a serif font close to Times New Roman; if none
is found, falls back to matplotlib's built-in serif so figures still render.

Usage::

    import sci_style as ss
    ss.set_style()
    fig, ax = plt.subplots()
    ax.plot(..., color=ss.C["blue"])
    ss.save(fig, "out.png")
"""
import os
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- try to register a Times-like serif across platforms ---
# macOS (Supplemental), common Windows, and Linux (msttcorefonts / liberation).
_FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Times New Roman*.ttf",   # macOS
    "/Library/Fonts/Times New Roman*.ttf",                       # macOS (user)
    "C:/Windows/Fonts/times*.ttf",                               # Windows
    "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman*.ttf",  # Linux msttcorefonts
    "/usr/share/fonts/truetype/liberation/LiberationSerif-*.ttf",    # Linux fallback
    "/usr/share/fonts/**/Times*.ttf",                           # generic Linux
]

_registered = []
for _pat in _FONT_CANDIDATES:
    for _p in glob.glob(_pat, recursive=True):
        try:
            fm.fontManager.addfont(_p)
            _registered.append(os.path.basename(_p))
        except Exception:
            pass

# Preferred serif stack: Times New Roman -> Liberation Serif -> matplotlib default.
_SERIF_STACK = ["Times New Roman", "Liberation Serif", "Times", "DejaVu Serif"]

# --- palette ---
C = {
    "blue":    "#4472C4",   # actual / true / real (shared primary)
    "orange":  "#ED9A3D",   # predicted (scheme A)
    "red":     "#E8403A",   # baseline / emphasis / scheme B second line
    "black":   "#000000",
    "apricot": "#F4C79A",   # bars
    "green":   "#70AD47",
    "gold":    "#F2B500",   # 'proposed' highlight
    "quad_bg": "#F4F7E7",   # pale yellow-green quadrant background
}
# 4-class colors (e.g. t-SNE clusters)
CLASS4 = ["#E8403A", "#2E5BBF", "#F2B500", "#19B5C9"]


def set_style():
    """Apply the Origin-clean rcParams globally."""
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": _SERIF_STACK,
        "mathtext.fontset": "stix",
        "font.size": 12,
        "axes.linewidth": 1.2,
        "axes.edgecolor": "black",
        "axes.labelsize": 13,
        "axes.titlesize": 13,
        "axes.unicode_minus": False,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "xtick.major.size": 5, "ytick.major.size": 5,
        "xtick.major.width": 1.1, "ytick.major.width": 1.1,
        "legend.frameon": False,
        "legend.fontsize": 10.5,
        "legend.handlelength": 1.8,
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "lines.linewidth": 1.4,
    })


def save(fig, path):
    """Save at 300 dpi with a tight bounding box and white background."""
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
