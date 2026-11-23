"""Generate 2 simulated-data figures for each of the 14 data-plot types,
following the 'Origin clean' journal style. Output -> sim_figs/.

All labels are neutral placeholders (Signal A/B, Class 1-4, Series, ...).
Replace them with your real labels when plotting actual data.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import matplotlib.pyplot as plt
import sci_style as ss

ss.set_style()
C = ss.C
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim_figs")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(20260531)


def p(name):
    return os.path.join(OUT, name)


# ----------------------------------------------------------------------
# 1. spatial scatter (quadrant)
# ----------------------------------------------------------------------
def localization(fname, average=False):
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    ax.add_patch(plt.Rectangle((100, 100), 300, 300, fc=C["quad_bg"], ec="none", zorder=0))
    ax.axhline(250, color="0.6", lw=0.8, zorder=1)
    ax.axvline(250, color="0.6", lw=0.8, zorder=1)
    # reference node grid (corners/edges)
    gx, gy = np.meshgrid([100, 250, 400], [100, 250, 400])
    ax.scatter(gx, gy, s=45, c="black", marker="o", zorder=5, label="Reference nodes")
    n = 28
    ax_ = rng.uniform(110, 390, n); ay = rng.uniform(110, 390, n)
    px = ax_ + rng.normal(0, 9, n); py = ay + rng.normal(0, 9, n)
    ax.scatter(ax_, ay, s=34, c=C["blue"], marker="o", zorder=4, label="Actual position")
    ax.scatter(px, py, s=40, c=C["orange"], marker="x", linewidths=1.4,
               zorder=4, label="Predicted position")
    ax.text(150, 380, "Region III", fontsize=11); ax.text(320, 380, "Region IV", fontsize=11)
    ax.text(150, 120, "Region I", fontsize=11); ax.text(320, 120, "Region II", fontsize=11)
    if average:
        k = 5
        ax.annotate("Average", xy=(px[k], py[k]), xytext=(px[k] + 70, py[k] + 40),
                    color=C["red"], fontsize=11,
                    arrowprops=dict(arrowstyle="->", color=C["red"], lw=1.4))
        ax.scatter([ax_[k]], [ay[k]], s=120, facecolors="none", edgecolors=C["red"], lw=1.4, zorder=6)
    ax.set_xlim(50, 450); ax.set_ylim(50, 450)
    ax.set_xlabel("$x$ (mm)"); ax.set_ylabel("$y$ (mm)")
    ax.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.13),
              fontsize=8.5, columnspacing=1.0, handletextpad=0.4)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 2. regression vs 1:1 line
# ----------------------------------------------------------------------
def regression(fname, spread=6.0):
    fig, ax = plt.subplots(figsize=(4.4, 4.2))
    for col, lab in [(C["orange"], "$x$ coordinate"), (C["blue"], "$y$ coordinate")]:
        a = rng.uniform(0, 150, 150)
        pr = a + rng.normal(0, spread, 150)
        ax.scatter(a, pr, s=20, c=col, alpha=0.8, edgecolors="none", label=lab)
    ax.plot([0, 150], [0, 150], "--", color=C["red"], lw=1.5)
    ax.set_xlim(0, 150); ax.set_ylim(0, 150)
    ax.set_xticks(range(0, 151, 30)); ax.set_yticks(range(0, 151, 30))
    ax.set_xlabel("Actual value (mm)"); ax.set_ylabel("Predicted value (mm)")
    ax.legend(loc="upper left")
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 3. per-sample scatter
# ----------------------------------------------------------------------
def per_sample(fname, axis="x"):
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    n = 150
    idx = np.arange(n)
    actual = rng.uniform(0, 150, n)
    pred = actual + rng.normal(0, 7, n)
    ax.scatter(idx, actual, s=34, c=C["blue"], marker="o", label=f"Actual ${axis}$")
    ax.scatter(idx, pred, s=34, c=C["orange"], marker="x", linewidths=1.3,
               label=f"Predicted ${axis}$")
    ax.set_xlim(0, n); ax.set_ylim(0, 160)
    ax.set_xlabel("Sample index"); ax.set_ylabel(f"${axis}$ (mm)")
    ax.legend(loc="upper right", ncol=2)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 4. dimensionality reduction (PCA / t-SNE)
# ----------------------------------------------------------------------
def pca_domain(fname):
    fig, ax = plt.subplots(figsize=(4.6, 4.3))
    src = rng.normal([1.2, 0], [1.5, 1.0], (320, 2))
    tgt1 = rng.normal([-2.8, 0], [0.9, 1.0], (70, 2))
    tgt2 = rng.normal([-3.2, 0.2], [1.1, 1.2], (55, 2))
    ax.scatter(src[:, 0], src[:, 1], s=14, facecolors="none", edgecolors=C["blue"],
               linewidths=0.7, label="Source domain")
    ax.scatter(tgt1[:, 0], tgt1[:, 1], s=34, facecolors="none", edgecolors=C["red"],
               marker="^", linewidths=1.1, label="Target (group 1)")
    ax.scatter(tgt2[:, 0], tgt2[:, 1], s=34, facecolors="none", edgecolors=C["orange"],
               marker="^", linewidths=1.1, label="Target (group 2)")
    ax.scatter([-2.7, 0.6], [0, 0], s=40, c=["#7a1d17", "#1a2f66"], marker="s", zorder=6)
    ax.plot([-2.7, 0.6], [0, 0], "k--", lw=1.0)
    ax.text(-5.5, 2.6, "Domain distance: 3.364", fontsize=10,
            bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="black", lw=1.0))
    ax.set_xlim(-6, 6); ax.set_ylim(-3, 3)
    ax.set_xlabel("PC1 (31.5% variance)"); ax.set_ylabel("PC2 (8.0% variance)")
    ax.legend(loc="lower right", fontsize=8.5)
    ss.save(fig, p(fname))


def tsne(fname):
    fig, ax = plt.subplots(figsize=(4.8, 4.3))
    centers = [(-12, 22), (-8, -10), (18, -8), (16, 14)]
    labs = ["Class 1", "Class 2", "Class 3", "Class 4"]
    for c, col, lab in zip(centers, ss.CLASS4, labs):
        pts = rng.normal(c, [3.0, 3.0], (45, 2))
        ax.scatter(pts[:, 0], pts[:, 1], s=14, c=col, edgecolors="none", label=lab)
    ax.set_xlim(-25, 30); ax.set_ylim(-25, 30)
    ax.set_xlabel("Dimension 1"); ax.set_ylabel("Dimension 2")
    ax.legend(loc="upper right", fontsize=8.5, markerscale=1.4)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 5. signal waveform
# ----------------------------------------------------------------------
def waveform(fname):
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    t = np.linspace(0, 200, 1000)
    env = np.exp(-((t - 60) ** 2) / (2 * 18 ** 2)) + 0.4 * np.exp(-((t - 110) ** 2) / (2 * 40 ** 2))
    a = env * np.sin(2 * np.pi * 0.18 * t) * 0.006
    b = a * (1 + 0.12 * np.sin(2 * np.pi * 0.02 * t)) + rng.normal(0, 5e-5, t.size)
    ax.plot(t, a, color="black", lw=1.0, label="Signal A")
    ax.plot(t, b, color=C["red"], lw=1.0, label="Signal B")
    ax.set_xlim(0, 200); ax.set_ylim(-0.008, 0.008)
    ax.set_xlabel("Time (s)"); ax.set_ylabel("Amplitude (V)")
    ax.text(0.5, 0.93, "Ch 1", transform=ax.transAxes, fontsize=12, ha="center")
    ax.legend(loc="upper right")
    ss.save(fig, p(fname))


def vibration(fname):
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    t = np.linspace(0, 0.4, 4000)
    real = (np.sin(2 * np.pi * 35 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)) * \
        (1 + 0.6 * np.sin(2 * np.pi * 8 * t)) + rng.normal(0, 0.3, t.size)
    synth = real + rng.normal(0, 0.28, t.size)
    real /= np.abs(real).max(); synth /= np.abs(synth).max()
    ax.plot(t, real, color=C["blue"], lw=0.5, label="Real")
    ax.plot(t, synth, color=C["red"], lw=0.5, alpha=0.8, label="Synthetic")
    ax.set_xlim(0, 0.4); ax.set_ylim(-1, 1)
    ax.set_xlabel("Time (s)"); ax.set_ylabel("Normalized amplitude")
    ax.legend(loc="upper right", fontsize=9)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 6. spectrum with peak labels
# ----------------------------------------------------------------------
def fft_spectrum(fname, two_panel=True):
    def one(ax, peaks, labels):
        f = np.linspace(0, 500, 2000)
        amp = np.abs(rng.normal(0, 0.0006, f.size))
        for pk, h in peaks:
            amp += h * np.exp(-((f - pk) ** 2) / (2 * 2.0 ** 2))
        ax.plot(f, amp, color=C["blue"], lw=0.7)
        for (pk, h), lab in zip(peaks, labels):
            ax.annotate(lab, xy=(pk, h), xytext=(pk, h + 0.0009),
                        fontsize=10, ha="center")
        ax.set_xlim(0, 500); ax.set_ylim(0, 0.010)
        ax.set_ylabel("Amplitude")
    if two_panel:
        fig, axes = plt.subplots(2, 1, figsize=(5.2, 4.4), sharex=True)
        one(axes[0], [(90, 0.0035), (175, 0.0045), (210, 0.0068), (355, 0.0052), (415, 0.0038)],
            ["$f_1$", "$2f_1$", "$f_2$", "$4f_1$", "$2f_2$"])
        one(axes[1], [(90, 0.0028), (175, 0.0030), (210, 0.0080), (270, 0.0025), (355, 0.0030), (415, 0.0070)],
            ["$f_1$", "$2f_1$", "$f_2$", "$3f_1$", "$4f_1$", "$2f_2$"])
        axes[1].set_xlabel("Frequency (Hz)")
    else:
        fig, ax = plt.subplots(figsize=(5.2, 3.0))
        one(ax, [(120, 0.0050), (240, 0.0090), (360, 0.0040), (420, 0.0050)],
            ["$f_1$", "$f_2$", "$3f_1$", "$2f_2$"])
        ax.set_xlabel("Frequency (Hz)")
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 7. real vs synthetic spectrum overlay
# ----------------------------------------------------------------------
def gan_overlay(fname, title="Condition A"):
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    f = np.linspace(0, 8000, 4000)
    base = np.abs(rng.normal(0, 0.004, f.size))
    peak = 0.07 * np.exp(-((f - 2000) ** 2) / (2 * 120 ** 2)) + \
        0.05 * np.exp(-((f - 1200) ** 2) / (2 * 150 ** 2))
    real = base + peak
    synth = np.abs(rng.normal(0, 0.006, f.size)) + 0.9 * peak + \
        0.02 * np.exp(-((f - 600) ** 2) / (2 * 200 ** 2))
    ax.plot(f, real, color=C["blue"], lw=0.5, label="Real")
    ax.plot(f, synth, color=C["red"], lw=0.5, alpha=0.75, label="Synthetic")
    ax.set_xlim(0, 8000); ax.set_ylim(0, 0.10)
    ax.set_xlabel("Frequency (Hz)"); ax.set_ylabel("Amplitude")
    ax.text(0.02, 0.92, title, transform=ax.transAxes, fontsize=10)
    ax.legend(loc="upper right", fontsize=9)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 8. training convergence curves
# ----------------------------------------------------------------------
def training_curve(fname, kind="loss"):
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    e = np.arange(0, 101)
    if kind == "loss":
        a = 0.9 * np.exp(-e / 8) + 0.13 + rng.normal(0, 0.02, e.size)
        b = 0.9 * np.exp(-e / 7) + 0.05 + rng.normal(0, 0.018, e.size)
        ax.plot(e, np.clip(a, 0, 1), color=C["blue"], lw=1.0, label="Baseline")
        ax.plot(e, np.clip(b, 0, 1), color=C["red"], lw=1.0, label="Proposed")
        ax.set_ylim(0, 1.0); ax.set_ylabel("Loss")
    else:
        e = np.arange(0, 201)
        a = 0.83 - 0.4 * np.exp(-e / 18) + rng.normal(0, 0.008, e.size)
        b = 0.87 - 0.45 * np.exp(-e / 15) + rng.normal(0, 0.007, e.size)
        ax.plot(e, a, color=C["blue"], lw=1.0, label="Setting A")
        ax.plot(e, b, color=C["red"], lw=1.0, label="Setting B")
        ax.set_ylim(0.4, 0.9); ax.set_ylabel("Score")
    ax.set_xlim(0, e[-1]); ax.set_xlabel("Epoch")
    ax.legend(loc="upper right", fontsize=9.5)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 9. method comparison line (Accuracy vs SNR)
# ----------------------------------------------------------------------
def method_compare(fname, setb=False):
    fig, ax = plt.subplots(figsize=(5.0, 3.4))
    snr = np.array([-8, -6, -4, -2, 0])
    if not setb:
        methods = [("Method 1", "black", "s"), ("Method 2", C["red"], "o"),
                   ("Method 3", "#7a5cc0", "^"), ("Method 4", C["green"], "v"),
                   ("Method 5", "#d089c0", "D"), ("Proposed", C["gold"], "*")]
        base = [56, 66, 79, 87, 96]
    else:
        methods = [("Method A", "black", "s"), ("Method B", C["blue"], "^"),
                   ("Method C", "#b07cc6", "D"), ("Method D", C["red"], "o"),
                   ("Method E", C["green"], "v"), ("Proposed", C["gold"], "*")]
        base = [40, 41, 42, 43, 45]
    for i, (name, col, mk) in enumerate(methods):
        if name == "Proposed":
            y = np.array([81, 87, 93, 97, 98.5])
            lw, ms = 1.8, 8
        else:
            off = (i - len(methods) / 2) * 1.6
            y = np.clip(np.array(base) + off + np.linspace(0, 6, 5) + rng.normal(0, 0.6, 5), 35, 99)
            lw, ms = 1.1, 6
        ax.plot(snr, y, color=col, lw=lw, marker=mk, ms=ms,
                markerfacecolor="none", markeredgecolor=col, label=name)
    ax.set_xlim(-8.5, 0.5); ax.set_xticks(snr)
    ax.set_xlabel("SNR (dB)"); ax.set_ylabel("Accuracy (%)")
    ax.legend(loc="lower right", fontsize=8, ncol=2)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 10. multi-line performance curves (with grid)
# ----------------------------------------------------------------------
def performance_curve(fname, variant=0):
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    x = np.linspace(0, 1.0, 11)
    s1 = 0.40 - 0.40 * x + 0.02
    s2 = 0.50 - 0.45 * x + 0.05 * (1 - x)
    s3 = (x * s1) / (2 * np.pi * (s2 / 10) + 1e-6)
    s3 = np.clip(s3 / s3.max() * 0.70, 0, 0.72)
    fac = 0.95 if variant else 1.0
    ax.plot(x, s1, color=C["blue"], marker="D", ms=5, label="Series 1 (Config 1)")
    ax.plot(x, s1 * 0.95, color=C["blue"], ls="--", marker="d", ms=5, label="Series 1 (Config 2)")
    ax.plot(x, s2, color="black", marker="^", ms=5, label="Series 2 (Config 1)")
    ax.plot(x, s2 * 0.95, color="black", ls="--", marker="^", ms=5, mfc="none", label="Series 2 (Config 2)")
    ax.plot(x, s3 * fac, color=C["red"], marker="o", ms=5, label="Series 3 (Config 1)")
    ax.plot(x, s3 * 0.85 * fac, color=C["red"], ls="--", marker="o", ms=5, mfc="none", label="Series 3 (Config 2)")
    ax.set_xlim(0, 1.0); ax.set_ylim(0, 0.80)
    ax.set_xlabel("$x$"); ax.set_ylabel("Value")
    ax.grid(True, color="0.8", lw=0.6)
    ax.legend(loc="upper center", ncol=3, fontsize=8, columnspacing=1.0)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 11. bar comparison
# ----------------------------------------------------------------------
def bar_compare(fname, metric="R2"):
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    if metric == "R2":
        cats = ["Variant 1", "Variant 2", "Variant 3",
                "Variant 4", "Variant 5", "Proposed"]
        vals = [93.8, 95.7, 96.4, 95.1, 96.9, 99.3]
        ylab, lo = "$R^2$ (%)", 90
    else:
        cats = ["Method 1", "Method 2", "Method 3", "Method 4", "Method 5", "Proposed"]
        vals = [91.2, 93.5, 95.0, 94.1, 96.7, 99.1]
        ylab, lo = "Accuracy (%)", 88
    x = np.arange(len(cats))
    ax.bar(x, vals, width=0.6, color=C["apricot"], edgecolor="black", lw=1.0)
    for xi, v in zip(x, vals):
        ax.text(xi, v + 0.1, f"{v:.1f}", ha="center", va="bottom", fontsize=10)
    ax.set_xticks(x); ax.set_xticklabels(cats, rotation=0, fontsize=8.5)
    ax.set_ylim(lo, 100); ax.set_ylabel(ylab)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 12. single-color weight heatmap (white->red)
# ----------------------------------------------------------------------
def heatmap(fname, n=3):
    fig, ax = plt.subplots(figsize=(4.6, 3.9))
    if n == 3:
        M = np.array([[0.510, 0.395, 0.095],
                      [0.098, 0.817, 0.085],
                      [0.097, 0.385, 0.518]])
        labs = ["Unit 1", "Unit 2", "Unit 3"]
    else:
        M = rng.uniform(0, 0.3, (n, n)); np.fill_diagonal(M, rng.uniform(0.7, 0.95, n))
        M /= M.sum(1, keepdims=True)
        labs = [f"U{i+1}" for i in range(n)]
    im = ax.imshow(M, cmap="Reds", vmin=0, vmax=1, aspect="equal")
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f"{M[i,j]:.3f}" if n == 3 else f"{M[i,j]:.2f}",
                    ha="center", va="center",
                    color="white" if M[i, j] > 0.6 else "black", fontsize=9)
    ax.set_xticks(range(n)); ax.set_yticks(range(n))
    ax.set_xticklabels(labs); ax.set_yticklabels(labs)
    ax.set_xlabel("Target unit"); ax.set_ylabel("Source unit")
    if n == 3:
        ax.set_title("Weight matrix", fontsize=12)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.outline.set_linewidth(1.0)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 13. time-frequency spectrogram (blue-dominant jet)
# ----------------------------------------------------------------------
def spectrogram(fname, seed_band=2):
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    nt, nf = 200, 200
    Z = np.abs(rng.normal(0, 0.12, (nf, nt)))
    for band, amp in [(500, 0.6), (1600, 0.9), (2100, 0.7)][:seed_band + 1]:
        fi = int(band / 4000 * nf)
        Z[max(0, fi - 6):fi + 6, :] += amp * (0.5 + 0.5 * rng.random((min(12, nf - max(0, fi - 6)), nt)))
    im = ax.imshow(Z, aspect="auto", origin="lower", cmap="jet",
                   extent=[0, 0.2, 0, 4000], vmax=1.0)
    ax.set_xlabel("Time (s)"); ax.set_ylabel("Frequency (Hz)")
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
# 14. 3D surface (jet + colorbar)
# ----------------------------------------------------------------------
def surface3d(fname, seed=0):
    fig = plt.figure(figsize=(5.2, 4.2))
    ax = fig.add_subplot(projection="3d")
    aa = np.linspace(0, 1, 40); bb = np.linspace(0, 1, 40)
    A, B = np.meshgrid(aa, bb)
    r = np.random.default_rng(seed)
    Z = 98 + 1.6 * np.sin(3 * A + seed) * np.cos(3 * B) + 0.6 * r.standard_normal(A.shape)
    Z = np.clip(Z, 97, 100)
    surf = ax.plot_surface(A, B, Z, cmap="jet", vmin=97, vmax=100,
                           rstride=1, cstride=1, linewidth=0, antialiased=True)
    ax.set_xlabel("$\\alpha$"); ax.set_ylabel("$\\beta$"); ax.set_zlabel("Accuracy (%)")
    ax.set_zlim(97, 100); ax.view_init(elev=22, azim=-60)
    i, j = np.unravel_index(np.argmax(Z), Z.shape)
    ax.text(A[i, j], B[i, j], 100.3, "$\\alpha$=0.5, $\\beta$=1\nAccuracy=100%", fontsize=8)
    cb = fig.colorbar(surf, ax=ax, shrink=0.6, pad=0.10, label="Accuracy")
    cb.outline.set_linewidth(1.0)
    ss.save(fig, p(fname))


# ----------------------------------------------------------------------
TASKS = [
    lambda: localization("01_localization_a.png", average=False),
    lambda: localization("01_localization_b.png", average=True),
    lambda: regression("02_regression_a.png", spread=5),
    lambda: regression("02_regression_b.png", spread=9),
    lambda: per_sample("03_persample_a.png", axis="x"),
    lambda: per_sample("03_persample_b.png", axis="y"),
    lambda: pca_domain("04_dimreduction_a_pca.png"),
    lambda: tsne("04_dimreduction_b_tsne.png"),
    lambda: waveform("05_waveform_a.png"),
    lambda: vibration("05_waveform_b_vibration.png"),
    lambda: fft_spectrum("06_fft_a.png", two_panel=True),
    lambda: fft_spectrum("06_fft_b.png", two_panel=False),
    lambda: gan_overlay("07_gan_a.png", title="Condition A"),
    lambda: gan_overlay("07_gan_b.png", title="Condition B"),
    lambda: training_curve("08_training_a_loss.png", kind="loss"),
    lambda: training_curve("08_training_b_score.png", kind="score"),
    lambda: method_compare("09_method_a.png", setb=False),
    lambda: method_compare("09_method_b.png", setb=True),
    lambda: performance_curve("10_performance_a.png", variant=0),
    lambda: performance_curve("10_performance_b.png", variant=1),
    lambda: bar_compare("11_bar_a_r2.png", metric="R2"),
    lambda: bar_compare("11_bar_b_acc.png", metric="ACC"),
    lambda: heatmap("12_heatmap_a_3x3.png", n=3),
    lambda: heatmap("12_heatmap_b_6x6.png", n=6),
    lambda: spectrogram("13_spectrogram_a.png", seed_band=2),
    lambda: spectrogram("13_spectrogram_b.png", seed_band=1),
    lambda: surface3d("14_surface_a.png", seed=0),
    lambda: surface3d("14_surface_b.png", seed=3),
]

if __name__ == "__main__":
    ok = 0
    for fn in TASKS:
        try:
            fn(); ok += 1
        except Exception as e:
            print("ERR", fn, repr(e))
    print(f"DONE {ok}/{len(TASKS)} -> {OUT}")
