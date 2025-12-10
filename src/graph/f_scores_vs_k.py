import pandas as pd
import matplotlib.pyplot as plt

# --- Config -----------------------------------------------------------------
ENSEMBLE = "E5"

INPUT_CSV = f"../../results/analysis/ensembling/topk/{ENSEMBLE}.csv"
OUTPUT_PNG = f"../../results/graph/{ENSEMBLE}_f_scores_vs_k.png"

def main():
    metrics = pd.read_csv(INPUT_CSV)

    required = {"k", "F1", "F0_5", "F2"}
    missing = required - set(metrics.columns)
    if missing:
        raise ValueError(f"Missing columns in {INPUT_CSV}: {missing}")

    plt.figure()

    plt.plot(metrics["k"], metrics["F1"], label=f"F1 ({ENSEMBLE})")
    plt.plot(metrics["k"], metrics["F0_5"], label=f"F0.5 ({ENSEMBLE})")
    plt.plot(metrics["k"], metrics["F2"], label=f"F2 ({ENSEMBLE})")

    plt.xlabel("k (top-k requirements)")
    plt.ylabel("F-score")
    plt.legend(loc="lower left")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=300)


if __name__ == "__main__":
    main()
