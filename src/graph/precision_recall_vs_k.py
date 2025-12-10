import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Config -----------------------------------------------------------------
ENSEMBLE = "E5"
TOTAL_REQUIREMENTS = 76

INPUT_CSV = f"../../results/analysis/ensembling/topk/{ENSEMBLE}.csv"
OUTPUT_PNG = f"../../results/graph/{ENSEMBLE}_precision_recall_vs_k.png"


def main():
    metrics = pd.read_csv(INPUT_CSV)

    # Required columns check
    required = {"k", "precision", "recall"}
    missing = required - set(metrics.columns)
    if missing:
        raise ValueError(f"Missing columns in {INPUT_CSV}: {missing}")

    k_vals = metrics["k"].values.astype(float)

    # Feasible upper limits
    recall_upper = np.minimum(k_vals / TOTAL_REQUIREMENTS, 1.0)
    precision_upper = np.where(
        k_vals <= TOTAL_REQUIREMENTS,
        1.0,
        TOTAL_REQUIREMENTS / k_vals,
    )

    plt.figure()
    ax = plt.gca()

    # Feasible limit lines
    recall_limit_line, = ax.plot(
        k_vals, recall_upper,
        linestyle="--",
        linewidth=0.8,
        color="tab:orange",
        alpha=0.7,
    )

    precision_limit_line, = ax.plot(
        k_vals, precision_upper,
        linestyle="--",
        linewidth=0.8,
        color="tab:blue",
        alpha=0.7,
    )

    # Actual curves
    precision_line, = ax.plot(
        metrics["k"], metrics["precision"],
        linewidth=1.2,
    )

    recall_line, = ax.plot(
        metrics["k"], metrics["recall"],
        linewidth=1.2,
    )

    ax.set_xlabel("k (top-k requirements)")
    ax.set_ylabel("Score")
    ax.grid(True)

    # Custom legend handles (under plot)
    legend_handles = [
        Line2D(
            [0], [0],
            marker="o", color="w",
            markerfacecolor=precision_line.get_color(),
            markersize=11,
            label="Precision@k"
        ),
        Line2D(
            [0], [0],
            marker="o", color="w",
            markerfacecolor=recall_line.get_color(),
            markersize=11,
            label="Recall@k"
        ),
        Line2D(
            [0], [0],
            color=precision_limit_line.get_color(),
            linestyle="--",
            linewidth=1.2,
            label="Precision@k feasible limit"
        ),
        Line2D(
            [0], [0],
            color=recall_limit_line.get_color(),
            linestyle="--",
            linewidth=1.2,
            label="Recall@k feasible limit"
        ),
    ]

    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.22),
        ncol=2,
        frameon=False,
        handletextpad=0.35
    )

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
