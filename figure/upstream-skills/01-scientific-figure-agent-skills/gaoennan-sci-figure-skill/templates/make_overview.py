"""Tile the 28 generated PNGs into one overview sheet (7 rows x 4 cols)."""
import os, glob
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim_figs")
files = sorted(f for f in glob.glob(os.path.join(D, "*.png"))
               if os.path.basename(f)[0].isdigit())
n = len(files)
cols, rows = 4, 7
fig, axes = plt.subplots(rows, cols, figsize=(cols * 3.4, rows * 2.7))
for ax in axes.ravel():
    ax.axis("off")
for ax, f in zip(axes.ravel(), files):
    ax.imshow(mpimg.imread(f))
    ax.set_title(os.path.basename(f).replace(".png", ""), fontsize=8)
fig.suptitle("14 data-plot types x 2 simulated figures (Origin clean style)", fontsize=13)
fig.tight_layout(rect=[0, 0, 1, 0.985])
out = os.path.join(D, "_OVERVIEW.png")
fig.savefig(out, dpi=140, bbox_inches="tight", facecolor="white")
print("OVERVIEW", out, "from", n, "figures")
