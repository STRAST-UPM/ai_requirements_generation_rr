import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Config -----------------------------------------------------------------
ENSEMBLES = ["E1", "E2", "E3", "E4", "E5"]
INPUT_TEMPLATE = "../../results/analysis/ensembling/topk/{sys}.csv"
OUTPUT_PNG = "../../results/graph/precision_recall_over_k.png"


def main():
    plt.figure()
    ax = plt.gca()

    # Plot PR curves for each system
    for sys_id in ENSEMBLES:
        path = INPUT_TEMPLATE.format(sys=sys_id)
        metrics = pd.read_csv(path)

        required = {"precision", "recall"}
        missing = required - set(metrics.columns)
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")

        ax.plot(
            metrics["recall"],
            metrics["precision"],
            linewidth=1.2,
        )

    # F2 iso-curves (not in legend)
    beta = 2.0
    beta2 = beta ** 2
    coef = 1 + beta2

    r_grid = np.linspace(0.001, 1.0, 500)

    for f_target in np.arange(0.6, 1.01, 0.1):
        denom = coef * r_grid - beta2 * f_target
        p_grid = f_target * r_grid / denom

        mask = (denom > 0) & (p_grid >= 0) & (p_grid <= 1)
        if not np.any(mask):
            continue

        ax.plot(
            r_grid[mask],
            p_grid[mask],
            linestyle="--",
            linewidth=0.8,
            color="gray",
            alpha=0.6
        )

        # light label at end of curve
        r_end = r_grid[mask][-1]
        p_end = p_grid[mask][-1]
        ax.text(
            r_end, p_end,
            f"{f_target:.1f}",
            fontsize=6,
            color="gray",
            ha="left", va="bottom"
        )

    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.grid(True)

    # Legend: dot style for E1..E5 only, placed under plot
    # Use the plotted line colors as they were assigned
    lines = ax.get_lines()
    # The first len(ENSEMBLES) lines are the main PR curves
    pr_lines = lines[:len(ENSEMBLES)]

    legend_handles = []
    for sys_id, line in zip(ENSEMBLES, pr_lines):
        legend_handles.append(
            Line2D(
                [0], [0],
                marker="o",
                color="w",
                markerfacecolor=line.get_color(),
                markersize=11,
                label=sys_id
            )
        )

    plt.subplots_adjust(bottom=0.28)

    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.18),
        ncol=len(legend_handles),
        frameon=False,
        handletextpad=0.35,
        columnspacing=0.9
    )

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
