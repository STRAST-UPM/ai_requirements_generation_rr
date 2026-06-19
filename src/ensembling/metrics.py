import pandas as pd
import numpy as np
import math

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
    {
        "key": "E6",
        "col": "Optimal numeric",
        "type": "prob",
        "label": "Optimal numeric ranking",
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

def expected_average_precision_with_ties(
    df_sorted: pd.DataFrame,
    score_col: str,
    rel_col: str = "is_real",
) -> float:
    """
    Compute expected Average Precision (AP) under uniform random
    permutations of items *within each tie block* of equal score.

    df_sorted: dataframe sorted in descending order by score_col.
    score_col: column with the ranking score (may have ties).
    rel_col:   boolean column indicating relevance (True = real).
    """
    scores = df_sorted[score_col].to_numpy()
    is_rel = df_sorted[rel_col].to_numpy().astype(bool)

    n = len(scores)
    R_total = int(is_rel.sum())
    if R_total == 0:
        return 0.0

    S_total = 0.0  # numerator: sum_i E[1_rel(i) * Prec(i)]
    R_prev = 0     # # relevant before current block
    pos = 0        # 0-based index in the full ranking

    while pos < n:
        start = pos
        s_val = scores[start]

        # find end of this tie block (same score)
        pos += 1
        while pos < n and scores[pos] == s_val:
            pos += 1
        end = pos  # [start, end)

        g = end - start
        block_rels = is_rel[start:end]
        r = int(block_rels.sum())

        if r == 0:
            # no relevant docs in this block; contribution is zero
            continue

        if g == 1:
            # single-item block, trivial
            i = start + 1  # 1-based rank
            S_total += (R_prev + 1) / i
            R_prev += 1
            continue

        # g > 1 : use analytic expectation for each position in the block
        for j in range(1, g + 1):  # j = 1..g (position within block)
            i = start + j          # 1-based global rank
            # E[T_j] = (r/g) * (R_prev + 1 + (j-1)(r-1)/(g-1)) / i
            S_total += (r / g) * (
                R_prev + 1 + (j - 1) * (r - 1) / (g - 1)
            ) / i

        R_prev += r

    return float(S_total / R_total)

def reorder_for_bpref_extreme(
    df_sorted: pd.DataFrame,
    score_col: str,
    rel_col: str = "is_real",
    nonrel_first: bool = True,
) -> pd.DataFrame:
    """
    Return a copy of df_sorted where, within each tie block of equal score_col,
    rows are reordered to make bpref as bad as possible (nonrel_first=True)
    or as good as possible (nonrel_first=False).

    - We *only* permute within tie blocks (same score).
    - rel_col is True for relevant (real) items.
    """
    df = df_sorted.copy()
    scores = df[score_col].to_numpy()
    is_rel = df[rel_col].to_numpy().astype(bool)

    n = len(df)
    blocks = []
    start = 0
    while start < n:
        end = start + 1
        while end < n and scores[end] == scores[start]:
            end += 1
        blocks.append((start, end))
        start = end

    new_indices = []
    for (start, end) in blocks:
        block_idx = np.arange(start, end)
        block_rel = is_rel[start:end]

        # relevant = True (1), nonrel = False (0)
        if nonrel_first:
            # worst case: nonrelevant first -> sort by rel ascending (0 then 1)
            order = np.argsort(block_rel.astype(int), kind="mergesort")
        else:
            # best case: relevant first -> sort by rel descending (1 then 0)
            order = np.argsort(-block_rel.astype(int), kind="mergesort")

        new_indices.extend(block_idx[order])

    return df.iloc[new_indices].reset_index(drop=True)


def bpref_from_df(df_sorted: pd.DataFrame, rel_col: str = "is_real") -> float:
    """
    Convenience wrapper around your existing bpref() function.
    """
    return bpref(df_sorted[rel_col].to_numpy())

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

def expected_bpref(
    df_sorted: pd.DataFrame,
    score_col: str,
    rel_col: str = "is_real",
) -> float:
    """
    Expected bpref under uniform random permutations *within each tie block*
    of equal score_col, with block order fixed by descending score.

    This mirrors the behavior of bpref() implemented below (including the
    clamp of negative contributions to 0).

    Parameters
    ----------
    df_sorted : pd.DataFrame
        DataFrame sorted in descending order by score_col.
    score_col : str
        Column containing ranking scores (may contain ties).
    rel_col : str
        Boolean relevance column (True = relevant/real).

    Returns
    -------
    float
        Expected bpref with random tie-breaking within equal-score blocks.
    """
    scores = df_sorted[score_col].to_numpy()
    is_rel = df_sorted[rel_col].to_numpy().astype(bool)

    n = len(scores)
    R_total = int(is_rel.sum())
    if R_total == 0:
        return 0.0

    N_nonrel_total = n - R_total
    if N_nonrel_total == 0:
        return 1.0

    # Same denominator as your bpref() implementation
    max_nonrel = min(R_total, N_nonrel_total)

    def hypergeom_pmf(x: int, N: int, K: int, n_draws: int) -> float:
        """
        Hypergeometric PMF:
        Population size N, K successes in population,
        draw n_draws without replacement, probability of x successes.
        """
        if x < 0 or x > K or x > n_draws or (n_draws - x) > (N - K):
            return 0.0
        return (
            math.comb(K, x) * math.comb(N - K, n_draws - x)
        ) / math.comb(N, n_draws)

    expected_sum = 0.0  # expected sum of per-relevant contributions
    nonrel_before = 0   # deterministic count of nonrel in earlier blocks

    pos = 0
    while pos < n:
        start = pos
        s_val = scores[start]

        # identify tie block [start, end)
        pos += 1
        while pos < n and scores[pos] == s_val:
            pos += 1
        end = pos

        g = end - start
        block_rel = is_rel[start:end]
        r = int(block_rel.sum())
        nr = g - r

        if r == 0:
            # all nonrelevant: just advance the nonrel counter
            nonrel_before += nr
            continue

        if g == 1:
            # single item; since r>0 here it's relevant
            contrib = 1.0 - nonrel_before / max_nonrel
            if contrib < 0:
                contrib = 0.0
            expected_sum += contrib
            nonrel_before += nr
            continue

        # For each position j inside the block, compute:
        # P(position j is relevant) * E[contrib | position j relevant]
        # With uniform random placement of r relevant items among g positions:
        # P(position j relevant) = r/g
        #
        # Conditional on position j being relevant, the number of nonrel
        # before it within the block follows a Hypergeom distribution with:
        #   N = g-1 remaining items
        #   K = nr nonrelevant among them
        #   n_draws = j-1 positions before j
        N_pop = g - 1
        K_succ = nr

        for j in range(1, g + 1):
            draws = j - 1

            exp_contrib_if_rel = 0.0
            # feasible x range for hypergeom
            x_min = max(0, draws - (r - 1))
            x_max = min(nr, draws)

            for x in range(x_min, x_max + 1):
                pmf = hypergeom_pmf(x, N_pop, K_succ, draws)
                contrib = 1.0 - (nonrel_before + x) / max_nonrel
                if contrib < 0:
                    contrib = 0.0
                exp_contrib_if_rel += contrib * pmf

            expected_sum += (r / g) * exp_contrib_if_rel

        # After the block is fully processed in the ranked list,
        # all its nonrelevant items have been "seen".
        nonrel_before += nr

    return float(expected_sum / R_total)

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

        # OLD versions (deterministic within ties)
        ap_base = average_precision(
            metrics["recall"].to_numpy(),
            metrics["precision"].to_numpy()
        )
        bp_base = bpref(df_sorted["is_real"].to_numpy())

        # NEW: expected metrics under random tie-breaking within equal-score blocks
        ap_exp = expected_average_precision_with_ties(df_sorted, score_col)
        bp_exp = expected_bpref(df_sorted, score_col=score_col, rel_col="is_real")

        df_worst = reorder_for_bpref_extreme(
            df_sorted, score_col=score_col, rel_col="is_real", nonrel_first=True
        )
        bp_worst = bpref_from_df(df_worst, rel_col="is_real")
        df_best = reorder_for_bpref_extreme(
            df_sorted, score_col=score_col, rel_col="is_real", nonrel_first=False
        )
        bp_best = bpref_from_df(df_best, rel_col="is_real")

        avgF1 = float(metrics["F1"].mean())
        maxF1 = float(metrics["F1"].max())
        avgF2 = float(metrics["F2"].mean())
        maxF2 = float(metrics["F2"].max())

        max_f1_star, k_star, p_star, r_star = get_operating_point(metrics)

        summary_rows.append({
            "System": key,
            "label": spec.get("label", key),

            "AveP": ap_exp,
            "AveP_det": ap_base,

            "bPref": bp_exp,
            "bPref_det": bp_base,
            "bPref_best": bp_best,
            "bPref_worst": bp_worst,

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
