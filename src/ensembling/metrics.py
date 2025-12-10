import pandas as pd
import numpy as np

RESULTS_PATH = "../../results/analysis/ensembling"
CSV_PATH = f"{RESULTS_PATH}/composition.csv"
TOTAL_REQUIREMENTS = 76

METRIC_SPECS = [
    {
        "key": "E1",
        "col": "Prec. Macro",
        "type": "prob",
        "label": "Prec. Macro ranking",
    },
    {
        "key": "E2",
        "col": "Support",
        "type": "numeric",
        "label": "Support ranking",
    },
    {
        "key": "E3",
        "col": "Prec. Macro Balanced",
        "type": "prob",
        "label": "Prec. Macro Balanced ranking",
    },
    {
        "key": "E4",
        "col": "Prec. Micro A",
        "type": "prob",
        "label": "Prec. Micro A ranking",
    },
    {
        "key": "E5",
        "col": "Prec. Micro B",
        "type": "prob",
        "label": "Prec. Micro B ranking",
    },
]

def f_beta(precision: pd.Series, recall: pd.Series, beta: float) -> pd.Series:
    beta2 = beta ** 2
    denom = beta2 * precision + recall
    f = (1 + beta2) * precision * recall / denom
    f = f.astype(float)
    f[denom == 0] = 0.0
    return f

def build_metrics(df: pd.DataFrame, score_col: str, total: int):
    """
    Given a dataframe and a column name to use as ranking score,
    return (df_sorted, metrics_df) for that ranking.
    """
    hall_col = "Hall."

    df_local = df.copy()
    df_local[score_col] = pd.to_numeric(df_local[score_col], errors="coerce")
    df_valid = df_local[df_local[score_col].notna()].copy()

    df_sorted = df_valid.sort_values(score_col, ascending=False).reset_index(drop=True)
    df_sorted["Rank"] = df_sorted[score_col].rank(
        method="dense",
        ascending=False
    ).astype(int)

    is_hall = df_sorted[hall_col].astype(str).str.strip().str.lower().isin(
        ["yes", "y", "1", "true", "hallucination", "hall"]
    )
    df_sorted["is_hall"] = is_hall
    df_sorted["is_real"] = ~is_hall

    df_sorted["k"] = df_sorted.index + 1
    df_sorted["cum_covered"] = df_sorted["is_real"].cumsum()
    df_sorted["cum_hall"] = df_sorted["is_hall"].cumsum()

    metrics_df = pd.DataFrame({
        "k": df_sorted["k"],
        "covered": df_sorted["cum_covered"],
        "hallucinations": df_sorted["cum_hall"],
    })

    metrics_df["recall"] = metrics_df["covered"] / total
    metrics_df["precision"] = metrics_df["covered"] / (
        metrics_df["covered"] + metrics_df["hallucinations"]
    )

    metrics_df["F1"] = f_beta(metrics_df["precision"], metrics_df["recall"], beta=1.0)
    metrics_df["F0_5"] = f_beta(metrics_df["precision"], metrics_df["recall"], beta=0.5)
    metrics_df["F2"] = f_beta(metrics_df["precision"], metrics_df["recall"], beta=2.0)

    return df_sorted, metrics_df

def average_precision(recalls: np.ndarray, precisions: np.ndarray) -> float:
    """
    Compute Average Precision (AveP) from monotonic recall & corresponding precision.
    AP = sum_k (R_k - R_{k-1}) * P_k over points where recall increases.
    """
    ap = 0.0
    prev_r = 0.0
    for r, p in zip(recalls, precisions):
        if r > prev_r:
            ap += p * (r - prev_r)
            prev_r = r
    return float(ap)

def bpref(is_relevant: np.ndarray) -> float:
    """
    Compute bpref given a boolean relevance array in ranked order.

    bpref = (1/R) * sum_over_relevant r [ 1 - (#nonrel above r / min(R, N_nonrel)) ]
    """
    is_relevant = np.asarray(is_relevant, dtype=bool)
    R = int(is_relevant.sum())
    if R == 0:
        return 0.0

    N_nonrel = int((~is_relevant).sum())
    if N_nonrel == 0:
        return 1.0  # all are relevant

    max_nonrel = min(R, N_nonrel)

    score_sum = 0.0
    nonrel_seen = 0

    for rel in is_relevant:
        if rel:
            contrib = 1.0 - nonrel_seen / max_nonrel
            if contrib < 0:
                contrib = 0.0
            score_sum += contrib
        else:
            nonrel_seen += 1

    return float(score_sum / R)

def get_operating_point(metrics_df: pd.DataFrame):
    """
    Return operating point optimized for max F1:
    (max_f1, k_star, p_star, r_star)
    """
    idx = metrics_df["F1"].idxmax()
    max_f1 = float(metrics_df.loc[idx, "F1"])
    k_star = int(metrics_df.loc[idx, "k"])
    p_star = float(metrics_df.loc[idx, "precision"])
    r_star = float(metrics_df.loc[idx, "recall"])
    return max_f1, k_star, p_star, r_star


def main():
    df = pd.read_csv(CSV_PATH, sep=None, engine="python")

    for spec in METRIC_SPECS:
        key = spec["key"]
        col = spec["col"]
        score_col = f"{key}_score"

        if spec["type"] == "prob":
            df[score_col] = (
                df[col]
                .astype(str)
                .str.replace(",", ".", regex=False)
                .astype(float)
            )
        elif spec["type"] == "numeric":
            df[score_col] = pd.to_numeric(df[col], errors="coerce")
        else:
            raise ValueError(f"Unknown metric type: {spec['type']}")

    summary_rows = []

    for spec in METRIC_SPECS:
        key = spec["key"]
        score_col = f"{key}_score"

        df_sorted, metrics = build_metrics(df, score_col, TOTAL_REQUIREMENTS)

        ap = average_precision(
            metrics["recall"].to_numpy(),
            metrics["precision"].to_numpy()
        )
        bp = bpref(df_sorted["is_real"].to_numpy())

        avgF1 = float(metrics["F1"].mean())
        maxF1 = float(metrics["F1"].max())
        avgF2 = float(metrics["F2"].mean())
        maxF2 = float(metrics["F2"].max())

        max_f1_star, k_star, p_star, r_star = get_operating_point(metrics)

        summary_rows.append({
            "System": key,
            "label": spec.get("label", key),

            "AveP": ap,
            "bPref": bp,

            "avgF1": avgF1,
            "maxF1": maxF1,
            "avgF2": avgF2,
            "maxF2": maxF2,

            "k*": k_star,
            "F1@k*": max_f1_star,
            "P@k*": p_star,
            "R@k*": r_star,

            "n_ranked_items": int(len(df_sorted)),
            "total_requirements": int(TOTAL_REQUIREMENTS),
        })

        df_sorted.to_csv(f"{RESULTS_PATH}/rank/{key}.csv", index=False)
        metrics.to_csv(f"{RESULTS_PATH}/topk/{key}.csv", index=False)

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(f"{RESULTS_PATH}/summary.csv", index=False)


if __name__ == "__main__":
    main()
