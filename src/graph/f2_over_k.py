import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Config -----------------------------------------------------------------
ENSEMBLES = ["E1", "E2", "E3", "E4", "E5"]
INPUT_TEMPLATE = "../../results/analysis/ensembling/topk/{sys}.csv"

OUTPUT_PNG = "../../results/graph/f2_over_k.png"

# Baseline for L0 (as in your earlier script)
L0_BASELINE = 0.53


def main():
    plt.figure()
    ax = plt.gca()

    # L0 baseline line
    ax.axhline(
        L0_BASELINE,
        linestyle="--",
        linewidth=1.0,
        color="black",
        alpha=0.85
    )

    legend_handles = []

    # Plot F2@k for each system
    for sys_id in ENSEMBLES:
        path = INPUT_TEMPLATE.format(sys=sys_id)
        metrics = pd.read_csv(path)

        required = {"k", "F2"}
        missing = required - set(metrics.columns)
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")

        line, = ax.plot(
            metrics["k"],
            metrics["F2"],
            linewidth=1.2,
        )

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

    # Baseline legend handle
    legend_handles.append(
        Line2D(
            [0], [0],
            color="black",
            linestyle="--",
            linewidth=1.2,
            label="L0"
        )
    )

    ax.set_xlabel("k (top-k requirements)")
    ax.set_ylabel("F2-score")
    ax.set_ylim(0.0, 1.0)
    ax.grid(True)

    # Legend under plot, one line
    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.22),
        ncol=len(legend_handles),
        frameon=False,
        handletextpad=0.35,
        columnspacing=0.9
    )

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
