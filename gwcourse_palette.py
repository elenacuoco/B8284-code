"""
gwcourse_palette.py
===================
Central colour palette for "Python for Gravitational Waves".

Every figure in the course is drawn from these six colour families and from
nothing else, so that a plot made for one lesson sits beside a plot made for
another without either looking borrowed.

Import this module in every figure script:

    from gwcourse_palette import P, CYCLE, CYCLE3, CYCLE5, apply_style

Usage
-----
    fig, ax = plt.subplots()
    apply_style()                     # set rcParams once per script
    ax.plot(x, y, color=P["BRICK"])
    ax.plot(x, z, color=P["BLUE"])

Colour families
---------------
Three hue families, five tones each (dark → pale):

    Brick Red   #7A1E10 → #A63220 → #C0503E → #E8A99E → #FAF0EE
    Sage Green  #2D4A35 → #4A7C5F → #72A688 → #B8D4C2 → #EFF6F2
    Royal Blue  #0D2159 → #1A3A8F → #3A65C0 → #A8BFEC → #EEF2FB

Neutral
-------
    INK / GREY_DARK / GREY_MID / GREY_LIGHT / GREY_PALE / WHITE

Semantic roles
--------------
    ALERT     → brick red   (errors, warnings)
    SUCCESS   → sage green  (notes, confirmations)
    INFO      → royal blue  (information boxes)
    HIGHLIGHT → brick mid   (highlighted text, markers)
"""

# ── Full palette dictionary ──────────────────────────────────────────
P = {
    # Brick Red
    "BRICK_DARK":   "#7A1E10",
    "BRICK":        "#A63220",
    "BRICK_MID":    "#C0503E",
    "BRICK_LIGHT":  "#E8A99E",
    "BRICK_PALE":   "#FAF0EE",

    # Sage Green
    "SAGE_DARK":    "#2D4A35",
    "SAGE":         "#4A7C5F",
    "SAGE_MID":     "#72A688",
    "SAGE_LIGHT":   "#B8D4C2",
    "SAGE_PALE":    "#EFF6F2",

    # Royal Blue
    "BLUE_DARK":    "#0D2159",
    "BLUE":         "#1A3A8F",
    "BLUE_MID":     "#3A65C0",
    "BLUE_LIGHT":   "#A8BFEC",
    "BLUE_PALE":    "#EEF2FB",

    # Amber
    "AMBER_DARK":   "#7A5214",
    "AMBER":        "#A97420",
    "AMBER_MID":    "#C99A45",
    "AMBER_LIGHT":  "#EBD3A0",
    "AMBER_PALE":   "#FBF4E6",

    # Teal
    "TEAL_DARK":    "#0E4A52",
    "TEAL":         "#1A6B75",
    "TEAL_MID":     "#4A98A2",
    "TEAL_LIGHT":   "#A9D2D8",
    "TEAL_PALE":    "#EDF6F7",

    # Plum
    "PLUM_DARK":    "#4A2452",
    "PLUM":         "#7B3D86",
    "PLUM_MID":     "#A067A9",
    "PLUM_LIGHT":   "#D6B9DC",
    "PLUM_PALE":    "#F7F0F9",

    # Neutrals
    "INK":          "#1A1A1A",
    "GREY_DARK":    "#4A4A4A",
    "GREY_MID":     "#888888",
    "GREY_LIGHT":   "#D4D4D4",
    "GREY_PALE":    "#F5F5F5",
    "WHITE":        "#FFFFFF",

    # Semantic aliases
    "ALERT":        "#A63220",   # = BRICK
    "SUCCESS":      "#4A7C5F",   # = SAGE
    "INFO":         "#1A3A8F",   # = BLUE
    "HIGHLIGHT":    "#C0503E",   # = BRICK_MID
}

# ── Plot colour cycles ───────────────────────────────────────────────

# 3-colour cycle — one per family (primary tones)
CYCLE3 = [P["BLUE"], P["BRICK"], P["SAGE"]]

# 6-colour cycle — one per family. The default for categorical series.
CYCLE6 = [P["BLUE"], P["BRICK"], P["SAGE"], P["AMBER"], P["TEAL"], P["PLUM"]]

# 5-colour cycle — interleaved mid tones for dense plots
CYCLE5 = [
    P["BLUE"],
    P["BRICK"],
    P["SAGE"],
    P["BLUE_MID"],
    P["BRICK_MID"],
]

# 9-colour cycle — full spread for multi-line/multi-detector plots
CYCLE9 = [
    P["BLUE"],
    P["BRICK"],
    P["SAGE"],
    P["AMBER"],
    P["TEAL"],
    P["PLUM"],
    P["BLUE_MID"],
    P["BRICK_MID"],
    P["SAGE_MID"],
]

# Default cycle (used by apply_style)
CYCLE = CYCLE9


# ── rcParams style function ──────────────────────────────────────────
def apply_style(figsize=(7, 4.5), dpi=150):
    """
    Apply the book's Matplotlib style globally.

    Call once at the top of each figure script, before any plot commands:

        from gwbook_palette import apply_style
        apply_style()
    """
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    mpl.rcParams.update({
        # Figure
        "figure.figsize":        figsize,
        "figure.dpi":            dpi,
        "figure.facecolor":      P["WHITE"],
        "figure.edgecolor":      P["WHITE"],

        # Axes
        "axes.facecolor":        P["WHITE"],
        "axes.edgecolor":        P["GREY_LIGHT"],
        "axes.linewidth":        0.8,
        "axes.labelcolor":       P["INK"],
        "axes.labelsize":        10,
        "axes.titlesize":        11,
        "axes.titleweight":      "semibold",
        "axes.titlecolor":       P["BLUE_DARK"],
        "axes.spines.top":       False,
        "axes.spines.right":     False,
        "axes.prop_cycle":       mpl.cycler(color=CYCLE),
        "axes.grid":             True,
        "axes.axisbelow":        True,

        # Grid
        "grid.color":            P["GREY_LIGHT"],
        "grid.linewidth":        0.5,
        "grid.linestyle":        "--",
        "grid.alpha":            0.6,

        # Lines & markers
        "lines.linewidth":       1.8,
        "lines.markersize":      5,

        # Ticks
        "xtick.color":           P["GREY_DARK"],
        "ytick.color":           P["GREY_DARK"],
        "xtick.labelsize":       9,
        "ytick.labelsize":       9,
        "xtick.direction":       "in",
        "ytick.direction":       "in",

        # Legend
        "legend.frameon":        True,
        "legend.framealpha":     0.9,
        "legend.edgecolor":      P["GREY_LIGHT"],
        "legend.fontsize":       9,
        "legend.title_fontsize": 9,

        # Font — use LaTeX-compatible serif for math, sans for labels
        "font.family":           "sans-serif",
        "font.size":             10,
        "mathtext.fontset":      "cm",      # Computer Modern — matches LaTeX

        # Saving
        "savefig.dpi":           150,
        "savefig.bbox":          "tight",
        "savefig.facecolor":     P["WHITE"],
        "savefig.transparent":   False,
    })


# ── Convenience: colourmap based on book palette ─────────────────────
def brick_cmap():
    """Linear colormap from BRICK_PALE to BRICK_DARK."""
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(
        "gwbook_brick",
        [P["BRICK_PALE"], P["BRICK_LIGHT"], P["BRICK"], P["BRICK_DARK"]],
    )


def sage_cmap():
    """Linear colormap from SAGE_PALE to SAGE_DARK."""
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(
        "gwbook_sage",
        [P["SAGE_PALE"], P["SAGE_LIGHT"], P["SAGE"], P["SAGE_DARK"]],
    )


def blue_cmap():
    """Linear colormap from BLUE_PALE to BLUE_DARK."""
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(
        "gwbook_blue",
        [P["BLUE_PALE"], P["BLUE_LIGHT"], P["BLUE"], P["BLUE_DARK"]],
    )


def diverging_cmap():
    """Diverging colormap: BRICK ← neutral → BLUE."""
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(
        "gwbook_div",
        [P["BRICK"], P["BRICK_LIGHT"], P["GREY_PALE"],
         P["BLUE_LIGHT"], P["BLUE"]],
    )


# ── Quick swatch for visual inspection ──────────────────────────────
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    apply_style(figsize=(10, 4))
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Left: colour swatches
    ax = axes[0]
    families = [
        ("Brick Red",  ["BRICK_DARK","BRICK","BRICK_MID","BRICK_LIGHT","BRICK_PALE"]),
        ("Sage Green", ["SAGE_DARK","SAGE","SAGE_MID","SAGE_LIGHT","SAGE_PALE"]),
        ("Royal Blue", ["BLUE_DARK","BLUE","BLUE_MID","BLUE_LIGHT","BLUE_PALE"]),
        ("Neutrals",   ["INK","GREY_DARK","GREY_MID","GREY_LIGHT","GREY_PALE"]),
    ]
    for row, (family, keys) in enumerate(families):
        for col, key in enumerate(keys):
            rect = mpatches.Rectangle(
                (col, len(families)-1-row), 0.92, 0.85,
                facecolor=P[key], edgecolor=P["GREY_LIGHT"], linewidth=0.5
            )
            ax.add_patch(rect)
            ax.text(col+0.46, len(families)-1-row+0.42, P[key],
                    ha="center", va="center", fontsize=6.5,
                    color=P["WHITE"] if col < 3 else P["GREY_DARK"])
        ax.text(-0.15, len(families)-1-row+0.42, family,
                ha="right", va="center", fontsize=8,
                color=P["INK"], fontweight="semibold")
    ax.set_xlim(-1, 5); ax.set_ylim(-0.2, len(families))
    ax.axis("off")
    ax.set_title("GW Book Colour Palette", fontsize=11, fontweight="bold",
                 color=P["BLUE_DARK"])

    # Right: cycle demo
    ax2 = axes[1]
    import numpy as np
    x = np.linspace(0, 2*np.pi, 200)
    for i, col in enumerate(CYCLE9):
        ax2.plot(x, np.sin(x + i*0.35) * (1 - i*0.06),
                 color=col, label=list(P.keys())[list(P.values()).index(col)])
    ax2.set_title("9-colour plot cycle", fontsize=11)
    ax2.set_xlabel("$x$"); ax2.set_ylabel("$y$")
    ax2.legend(fontsize=7, ncol=2, loc="lower left")

    plt.tight_layout()
    plt.savefig("figures/palette_swatch.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Swatch saved to figures/palette_swatch.png")
