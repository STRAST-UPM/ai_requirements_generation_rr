# Dataset Datasheet – `data/`

This datasheet follows the structure proposed by **Gebru et al. (2021) *“Datasheets for Datasets.”***  It documents the provenance, composition, and intended use of all artefacts under the `data/` directory, enabling transparent and responsible reuse.

## Motivation

| Question                          | Answer                                                                                                                                                                              |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why was this dataset created?     | To provide a reproducible benchmark for evaluating Large Language Models (LLMs) on the task of instantiating cyber-security controls (ISO-27002) into system-specific requirements. |
| Intended audience                 | Researchers in Requirements Engineering, Cyber-Security, and NLP; practitioners experimenting with security-centric LLM workflows.                                                  |

## Dataset Composition

| File                             | Instances     | Size      | Content                                                                                                            |
| -------------------------------- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `ai4i4.md`                       | 1 document    | 33.8 KB   | Functional & domain specification of the AI4I4 pilot system.                                                       |
| `annotated_standard_subset.json` | 10 control definitions    | 1.8 KB    | ISO‑27002 control definitions selection with parameter placeholders (`{…}`).                                            |
| `annotated_standard.json`        | 54 control definitions    | 8.6 KB    | ISO‑27002 control definitions extended selection with parameter placeholders (`{…}`).                                            |
| `prompt/**`                      | 184 templates |  ≈ 201 KB | System / user prompts grouped by task (`check‑applicability`, `search‑domain‑elements`, etc.) and by model family. |

## Collection and Annotation Process

* **Source standard** ISO/IEC 27002 : 2022. Only restructured requirements provided, in order to respect copyright.
* **Annotators** Three security engineers tagged placeholders and control types.
* **Timeline** Annotation performed Apr–May 2024; minor edits Sept 2024 when extending prompts.

## Pre‑processing and Cleaning

1. Clause text tokenised, references removed.
2. Variable components replaced by braces `{…}` (e.g., `{user credentials}`)..

## Uses and Limitations

### Recommended

* Benchmarking prompt‑engineering strategies for security requirement generation.
* Few‑shot or zero‑shot evaluation of new LLM checkpoints.

### Discouraged

* Production‑grade compliance audits.
* Training commercial models without acknowledging ISO copyright.

## Distribution & Licensing

* **Data licence** Creative Commons BY‑4.0 for annotations and metadata.
* **ISO text** © ISO. Only restructured requirements provided; users must hold an ISO licence to reconstruct full control definitions.

## Version History

| Version | Date       | Change                                            |
| ------- | ---------- | ------------------------------------------------- |
| 1.0     | 2025‑06-30 | Initial public release.                           |
| 2.1     | 2025‑12-03 | Terminology fixes.                                          |

---

*Last updated : 2025‑12-03*