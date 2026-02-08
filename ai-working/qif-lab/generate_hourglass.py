#!/usr/bin/env python3
"""
QIF v4.0 Hourglass Diagram — Generated from config.py (as-code).

Axes:
  Y-axis:  Band (vertical stack, N7 top → S3 bottom)
  Width:   State space / possibility space (hourglass geometry)
  Color:   Clinical severity (LETHAL=red, CRITICAL=orange, High=amber, Severe=yellow, N/A=blue)
  Left:    Frequency (dominant oscillation / carrier)
  Right:   L = v/f (wavelength / spatial extent)
  Far-left arrow: Determinacy spectrum (Deterministic → Quantum Uncertain)

Output: qif-hourglass-v4.png
"""

import sys
sys.path.insert(0, "/Users/mac/Documents/PROJECTS/qinnovates/mindloft/drafts/ai-working/qif-lab")

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from src.config import BANDS, ZONES, QUANTUM_PROOF_SCENARIO

# ── Configuration ──
FIG_W, FIG_H = 18, 22
BAR_MAX_W = 6.0       # max width for hourglass_width=1.0
CENTER_X = 9.0         # horizontal center of hourglass
Y_START = 20.0         # top of first band
BAR_H = 1.3            # height per band bar
GAP = 0.35             # vertical gap between bands
ZONE_GAP = 0.6         # extra gap between zones

# Severity → color mapping
SEVERITY_COLORS = {
    "LETHAL":   "#dc2626",   # red-600
    "CRITICAL": "#ea580c",   # orange-600
    "High":     "#d97706",   # amber-600
    "Severe":   "#ca8a04",   # yellow-600
    "Depends on adjacent N band": "#6b7280",  # gray-500
    "N/A (silicon)": "#2563eb",  # blue-600
}

# Determinacy → color for left arrow
DET_COLORS = {
    "Quantum Uncertain":  "#7c3aed",  # violet
    "Chaotic → Quantum Uncertain": "#8b5cf6",
    "Chaotic":            "#c026d3",  # fuchsia
    "Stochastic → Chaotic": "#db2777",
    "Stochastic":         "#e11d48",  # rose
    "Stochastic (analog noise)": "#e11d48",
    "Quasi-quantum (ΓD ∈ (0,1))": "#6366f1",  # indigo
    "Deterministic":      "#6b7280",  # gray
}

# Zone colors
ZONE_BG = {
    "neural":    "#dcfce7",   # green-100
    "interface": "#fee2e2",   # red-100
    "silicon":   "#dbeafe",   # blue-100
}

def format_freq(f_str):
    """Shorten frequency string for label."""
    if not f_str or f_str.startswith("N/A") or f_str.startswith("Reflex"):
        return f_str[:25] if f_str else ""
    # Take first part before parenthetical detail
    parts = f_str.split("(")
    main = parts[0].strip()
    detail = parts[1].rstrip(")").strip() if len(parts) > 1 else ""
    if detail:
        return f"{main}\n({detail[:35]})"
    return main

def format_L(L_val):
    """Format L range for label."""
    if L_val is None:
        return "N/A"
    if isinstance(L_val, (list, tuple)):
        lo, hi = L_val
        if lo is None and hi is None:
            return "N/A"
        if hi is None:
            return f"≥ {format_m(lo)}"
        if lo is None:
            return f"≤ {format_m(hi)}"
        return f"{format_m(lo)} – {format_m(hi)}"
    return str(L_val)

def format_m(v):
    """Format meters to human-readable."""
    if v is None:
        return "?"
    if v >= 1000:
        return f"{v/1000:.0f} km"
    if v >= 1:
        return f"{v:.1f} m"
    if v >= 0.01:
        return f"{v*100:.1f} cm"
    if v >= 0.001:
        return f"{v*1000:.1f} mm"
    if v >= 1e-6:
        return f"{v*1e6:.0f} μm"
    return f"{v:.1e} m"


def main():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H + 1)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(CENTER_X, FIG_H + 0.5, "QIF v4.0 — Hourglass Architecture (7-1-3)",
            ha="center", va="bottom", fontsize=20, fontweight="bold", fontfamily="monospace")
    ax.text(CENTER_X, FIG_H + 0.1,
            "Generated from config.py  •  L = v / f  •  QI(b,t) = exp(-S(b,t))",
            ha="center", va="bottom", fontsize=11, color="#6b7280", fontfamily="monospace")

    # Column headers
    header_y = Y_START + 1.0
    ax.text(1.5, header_y, "DETERMINACY", ha="center", va="bottom", fontsize=9,
            fontweight="bold", color="#6b7280", fontfamily="monospace")
    ax.text(4.2, header_y, "FREQUENCY", ha="center", va="bottom", fontsize=9,
            fontweight="bold", color="#6b7280", fontfamily="monospace")
    ax.text(CENTER_X, header_y, "BAND", ha="center", va="bottom", fontsize=9,
            fontweight="bold", color="#6b7280", fontfamily="monospace")
    ax.text(13.8, header_y, "L (SPATIAL)", ha="center", va="bottom", fontsize=9,
            fontweight="bold", color="#6b7280", fontfamily="monospace")
    ax.text(16.3, header_y, "SEVERITY", ha="center", va="bottom", fontsize=9,
            fontweight="bold", color="#6b7280", fontfamily="monospace")

    y = Y_START
    prev_zone = None
    band_positions = []

    for band in BANDS:
        zone = band["zone"]

        # Extra gap between zones
        if prev_zone and prev_zone != zone:
            y -= ZONE_GAP
            # Zone separator label
            if zone == "interface":
                ax.axhline(y=y + ZONE_GAP/2, xmin=0.15, xmax=0.85,
                          color="#e5e7eb", linewidth=1, linestyle="--")
            elif zone == "silicon":
                ax.axhline(y=y + ZONE_GAP/2, xmin=0.15, xmax=0.85,
                          color="#e5e7eb", linewidth=1, linestyle="--")

        # Hourglass width
        w = band["hourglass_width"] * BAR_MAX_W
        x_left = CENTER_X - w / 2
        x_right = CENTER_X + w / 2

        # Severity color
        severity = band.get("severity", "N/A (silicon)")
        color = SEVERITY_COLORS.get(severity, "#94a3b8")

        # Draw band bar (rounded rectangle)
        rect = FancyBboxPatch(
            (x_left, y - BAR_H),
            w, BAR_H,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor="white",
            linewidth=2,
            alpha=0.85,
        )
        ax.add_patch(rect)

        # Band label (center of bar)
        bar_center_y = y - BAR_H / 2
        ax.text(CENTER_X, bar_center_y + 0.15, band["id"],
                ha="center", va="center", fontsize=16, fontweight="bold",
                color="white", fontfamily="monospace")
        ax.text(CENTER_X, bar_center_y - 0.25, band["name"],
                ha="center", va="center", fontsize=9, color="white",
                fontfamily="monospace", alpha=0.95)

        # Left: Determinacy
        det = band.get("determinacy", "")
        det_color = DET_COLORS.get(det, "#6b7280")
        det_short = det.replace("Quasi-quantum (ΓD ∈ (0,1))", "Quasi-quantum")
        ax.text(1.5, bar_center_y, det_short,
                ha="center", va="center", fontsize=7.5, color=det_color,
                fontfamily="monospace", fontweight="bold")

        # Left-center: Frequency
        freq = band.get("dominant_freq_hz", "")
        freq_label = format_freq(freq)
        ax.text(4.2, bar_center_y, freq_label,
                ha="center", va="center", fontsize=7, color="#374151",
                fontfamily="monospace", linespacing=1.1)

        # Right-center: L
        L_val = band.get("L_m", None)
        L_label = format_L(L_val)
        ax.text(13.8, bar_center_y, L_label,
                ha="center", va="center", fontsize=8, color="#374151",
                fontfamily="monospace")

        # Far right: Severity badge
        sev_label = severity if severity != "Depends on adjacent N band" else "Variable"
        sev_label = sev_label if sev_label != "N/A (silicon)" else "—"
        ax.text(16.3, bar_center_y, sev_label,
                ha="center", va="center", fontsize=9, fontweight="bold",
                color=color if sev_label != "—" else "#94a3b8",
                fontfamily="monospace")

        band_positions.append((band["id"], y, y - BAR_H, bar_center_y))
        prev_zone = zone
        y -= (BAR_H + GAP)

    # ── Zone labels (vertical, left side) ──
    neural_bands = [bp for bp in band_positions if bp[0].startswith("N")]
    silicon_bands = [bp for bp in band_positions if bp[0].startswith("S")]
    i0_bands = [bp for bp in band_positions if bp[0] == "I0"]

    if neural_bands:
        n_top = neural_bands[0][1]
        n_bot = neural_bands[-1][2]
        n_mid = (n_top + n_bot) / 2
        ax.text(-0.3, n_mid, "N E U R A L", ha="center", va="center",
                fontsize=12, fontweight="bold", color=ZONES["neural"]["color"],
                rotation=90, fontfamily="monospace")
        # Zone background
        bg = mpatches.FancyBboxPatch(
            (0.3, n_bot - 0.2), FIG_W - 0.6, n_top - n_bot + 0.4,
            boxstyle="round,pad=0.2", facecolor=ZONE_BG["neural"],
            edgecolor=ZONES["neural"]["color"], linewidth=1.5, alpha=0.3, zorder=-1)
        ax.add_patch(bg)

    if i0_bands:
        i_top = i0_bands[0][1]
        i_bot = i0_bands[0][2]
        i_mid = (i_top + i_bot) / 2
        ax.text(-0.3, i_mid, "I0", ha="center", va="center",
                fontsize=12, fontweight="bold", color=ZONES["interface"]["color"],
                rotation=90, fontfamily="monospace")
        bg = mpatches.FancyBboxPatch(
            (0.3, i_bot - 0.2), FIG_W - 0.6, i_top - i_bot + 0.4,
            boxstyle="round,pad=0.2", facecolor=ZONE_BG["interface"],
            edgecolor=ZONES["interface"]["color"], linewidth=1.5, alpha=0.3, zorder=-1)
        ax.add_patch(bg)

    if silicon_bands:
        s_top = silicon_bands[0][1]
        s_bot = silicon_bands[-1][2]
        s_mid = (s_top + s_bot) / 2
        ax.text(-0.3, s_mid, "S I L I C O N", ha="center", va="center",
                fontsize=12, fontweight="bold", color=ZONES["silicon"]["color"],
                rotation=90, fontfamily="monospace")
        bg = mpatches.FancyBboxPatch(
            (0.3, s_bot - 0.2), FIG_W - 0.6, s_top - s_bot + 0.4,
            boxstyle="round,pad=0.2", facecolor=ZONE_BG["silicon"],
            edgecolor=ZONES["silicon"]["color"], linewidth=1.5, alpha=0.3, zorder=-1)
        ax.add_patch(bg)

    # ── Hourglass outline (connecting the widths) ──
    left_xs = []
    right_xs = []
    ys = []
    for band in BANDS:
        w = band["hourglass_width"] * BAR_MAX_W
        bp = [p for p in band_positions if p[0] == band["id"]][0]
        mid_y = bp[3]
        left_xs.append(CENTER_X - w/2)
        right_xs.append(CENTER_X + w/2)
        ys.append(mid_y)

    # Smooth hourglass silhouette
    ax.plot(left_xs, ys, color="#374151", linewidth=1.5, alpha=0.3, linestyle=":")
    ax.plot(right_xs, ys, color="#374151", linewidth=1.5, alpha=0.3, linestyle=":")

    # ── Quantum Proof annotation ──
    # Small callout showing what changes IF proven
    qp = QUANTUM_PROOF_SCENARIO
    n7_pos = [p for p in band_positions if p[0] == "N7"][0]
    ax.annotate(
        "IF quantum proven:\n→ Quantum Indeterminate (Level 7)\n→ No-cloning PROVEN at I0\n→ Unforgeable neural identity",
        xy=(CENTER_X + BAR_MAX_W/2 + 0.3, n7_pos[3]),
        xytext=(CENTER_X + BAR_MAX_W/2 + 1.5, n7_pos[3] + 1.5),
        fontsize=7, fontfamily="monospace", color="#7c3aed",
        ha="left", va="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f3ff", edgecolor="#7c3aed", alpha=0.8),
        arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=1.2),
    )

    # ── Legend ──
    legend_y = y - 1.0
    ax.text(CENTER_X, legend_y, "SEVERITY LEGEND", ha="center", va="top",
            fontsize=10, fontweight="bold", color="#374151", fontfamily="monospace")
    legend_items = [
        ("LETHAL", SEVERITY_COLORS["LETHAL"]),
        ("CRITICAL", SEVERITY_COLORS["CRITICAL"]),
        ("High", SEVERITY_COLORS["High"]),
        ("Severe", SEVERITY_COLORS["Severe"]),
        ("Silicon", SEVERITY_COLORS["N/A (silicon)"]),
    ]
    for i, (label, color) in enumerate(legend_items):
        lx = CENTER_X - 4 + i * 2.2
        ly = legend_y - 0.7
        rect = FancyBboxPatch((lx - 0.4, ly - 0.2), 0.6, 0.4,
                              boxstyle="round,pad=0.05", facecolor=color, alpha=0.85)
        ax.add_patch(rect)
        ax.text(lx + 0.5, ly, label, ha="left", va="center", fontsize=8,
                color="#374151", fontfamily="monospace")

    # ── Equation at bottom ──
    eq_y = legend_y - 1.8
    ax.text(CENTER_X, eq_y, "QI(b, t) = e^(−Σ(b, t))", ha="center", va="center",
            fontsize=14, fontfamily="monospace", fontweight="bold", color="#1e293b",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8fafc", edgecolor="#cbd5e1"))
    ax.text(CENTER_X, eq_y - 0.8,
            "Σ = Σ_classical(b) + Σ_quantum(b,t)   •   L = v / f   •   One equation, all bands, all devices",
            ha="center", va="center", fontsize=9, color="#6b7280", fontfamily="monospace")

    # ── Footer ──
    footer_y = eq_y - 1.6
    ax.text(CENTER_X, footer_y,
            "Kevin Qi  •  Qinnovate  •  qinnovates/mindloft  •  2026-02-06",
            ha="center", va="center", fontsize=8, color="#9ca3af", fontfamily="monospace")

    plt.tight_layout()
    outpath = "/Users/mac/Documents/PROJECTS/qinnovates/mindloft/drafts/ai-working/qif-lab/qif-hourglass-v4.png"
    fig.savefig(outpath, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"Saved: {outpath}")
    plt.close()


if __name__ == "__main__":
    main()
