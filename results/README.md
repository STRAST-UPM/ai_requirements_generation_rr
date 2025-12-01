# Results Datasheet – `results/`

This datasheet documents the provenance, structure, and intended use of the artefacts stored in the `results/` directory, following the **Datasheets for Datasets** framework (Gebru et al., 2021).  The directory captures every machine‑generated output, intermediate metric, and plot referenced in the accompanying paper and is required for full reproducibility.

## Motivation

| Question                          | Answer                                                                                                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why were these results saved?** | To provide verifiable evidence of each experiment reported in the paper and to allow third‑party re‑analysis without rerunning all LLM calls. |
| **Who is the target audience?**   | Researchers interested in benchmarking prompt‑engineering strategies, auditors of the empirical study, and educators needing ready‑made evaluation corpora. |

## Dataset Composition

| Sub‑folder                         | Content                                                                       | Instances / Files | Size     | Notes                                             |
| ---------------------------------- | ----------------------------------------------------------------------------- | ----------------- | -------- | ------------------------------------------------- |
| `requirements/`                    | JSON or Markdown requirement lists for each run (human and 15 model configs). | 30 files          | \~1.9 MB | `h_requirements.md` is the expert baseline.       |
| `analysis/coverage/`               | Model requirement presence in human baseline [Present, Hallucination, Rationale].                                   | 30 CSV            | 30.6 KB  | One row per model generated requirement.                           |
| `analysis/relations/completeness/` | CSV tables indicating model-generated related requirements for each requirement of the human baseline.        | 29 CSV          | 17.6 KB  |  |
| `analysis/relations/support/`      | CSV tables indicating human-generated related requirements for each requirement of the model generation.        | 29 CSV          | 18.1 KB  |  |
| `analysis/consistency.csv`         | Jaccard index analysis across repeated runs and inter-model, including raw data and summaries                                         | 12 CSV             | 16.7 KB     |                |
| `analysis/summary.csv`             | Precision, recall, F2, relative F2 and other key metrics extracted from the raw data.                                          | 1 CSV             | 5.9 KB     |              |
| `analysis/gold_standard.csv`       | De‑duplicated union of all positives.                                    | 1 CSV             | 12 KB     | 76 requirements.                                  |
| `graph/`                           | PNG figures A & B.                                                            | 2 PNG             | 569 KB   | Regenerated via `src/graph/*.py`.                 |

## Data Generation Process

1. **LLM Invocation** Each run executed a LangChain pipeline defined in `src/generate_requirements/templates/chain/*.py`, with hyper‑parameters specified in the corresponding `doc/*_execution_details.md` log.
2. **Figure rendering** `src/graph/results_figure_*.py` consumed the summary CSVs to produce PNGs.

Timestamps for each run are embedded in the execution logs; UTC time zone.

## Uses and Limitations

**Recommended**

* Verifying the paper’s claims without re‑running expensive LLM calls.
* Deriving secondary metrics (e.g., Matthews correlation) on the same outputs.
* Teaching examples of reproducible ML evaluation.

**Discouraged**

* Training new models: the corpus is too small and biased.
* Compliance certification: generated requirements are illustrative, not legally vetted.

## Licensing & Distribution

The result files are distributed under **CC‑BY‑4.0**. You may remix, adapt and build upon the data, provided you credit the original authors.

## Version History

| Version | Date       | Change                                            |
| ------- | ---------- | ------------------------------------------------- |
| 1.0     | 2025‑06-30 | Initial public release matching paper submission. |
| 2.0     | 2025‑12-01 | Second release including additional executions.   |

---

*Last updated : 2025‑12‑01*