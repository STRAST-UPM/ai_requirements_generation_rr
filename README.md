# A Case Study on AI-augmented Cybersecurity Requirements Generation leveraging LLMs Capabilities | Reproducible Research Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15641295.svg)](https://zenodo.org/record/15641295)

This repository accompanies the paper **“A Case Study on Cyber‑Security Requirement Elicitation: Leveraging Large‑Language‑Model Capabilities.”** It contains every script, dataset, prompt template and result needed to fully reproduce our empirical study.

## Research Description

This project investigates the practical use of state‑of‑the‑art Large Language Models (LLMs) to transform high‑level, standard‑driven cyber‑security controls into concrete, system‑specific requirements.  Using a synthetic yet industrially plausible case study—AI4I4, an IoT‑enabled automotive logistics platform—we benchmark thirteen frontier models (GPT‑4, LLaMa 3, Mistral, QWen, etc.), representing tge state of the art as of September 2024, across four prompting pipelines and three temperature regimes.

Key contributions include:

1. **Annotated benchmark** of 54 ISO‑27002 clauses with placeholder semantics suitable for automatic instantiation.
2. **LangChain pipelines** that decompose the task into applicability filtering, domain‑element search, requirement generation, and JSON formatting.
3. **Comprehensive evaluation** of accuracy (precision, recall, F2), creativity (F2‑synthetic), and consistency (Jaccard overlap across runs).
4. **Prompt library** enumerating >180 templates, showing how subtle changes in instruction design affect hallucination rate and coverage.

The artefacts and scripts below allow full replication—from raw prompts to final figures—on any infrastructure with access to the referenced models.

## Repository Structure

```text
.
├── data/                  # Experimental inputs
│   ├── ai4i4.md           # Functional specification of the AI4I4 case study
│   ├── annotated_standard_subset.json   # Annotated subset of ISO‑27002 clauses
│   └── prompt/            # Prompt templates organised by task and model
├── src/                   # LangChain pipelines and helper scripts
│   ├── generate_requirements/  # End‑to‑end automation
│   └── graph/                 # Scripts to render result figures
├── results/               # Raw outputs and aggregated metrics
│   ├── requirements/      # Requirement lists (human + models)
│   ├── analysis/          # Coverage, F‑scores, Jaccard, etc.
│   └── graph/             # Re‑generated figures from the manuscript
├── doc/                   # Execution logs for every configuration
├── LICENSE, LICENSE_DATA.txt
└── README.md              # This document
```

## Getting Started

Given that [python3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) are installed and correctly configured in the system, and assuming that you have (depending on the model(s) you intend to use):

- A valid [Huggingface PRO token](https://huggingface.co/pricing#pro).
- Granted acces the intended models on [AWS Bedrock](https://aws.amazon.com/bedrock/).
- A valid [OpenAI API key](https://platform.openai.com/docs/api-reference/authentication).
- A valid [Mistral API key](https://mistral.ai/).

You may follow the steps below to set up the environment and run the scripts.

### Prerequisites

1. Clone this repository locally.

```bash
git clone git@github.com:STRAST-UPM/ai_requirements_generation_rr.git
```

2. Change to the `generate_requirements` directory.

```bash
cd src/generate-requirements
```

3. Create a python [virtual environment](https://docs.python.org/3/library/venv.html) and activate it (**recommended**)

```bash
python -m venv .venv
source .venv/bin/activate 
```

4. Install all required dependencies.

```bash
pip install -r requirements.txt
```

5. Create a `.env` file with the following content (depending on the models you want to use):

```bash
HUGGINGFACE_API_TOKEN=<your_token>
MISTRAL_API_TOKEN=<your_token>
OPENAI_API_TOKEN=<your_token>
```

> [!TIP]
> You may find an example of the `.env` file at [.env.example](/src/generate-requirements/.env.example).

6. If you want to use models provided by AWS, configure AWS CLI with the credentials provided by the AWS administration console.

```bash
aws configure
```

## Execution

### Generation of Cybersecurity Requirements

To generate cybersecurity requirements for a given system description, you may use the [/src/generate
-requirements/main.py](/src/generate
-requirements/main.py) script. You may specify the following parameters:

`-s STANDARDS`, to set the path of the file containing the adapted cybersecurity standards, as a `.json` file.

`-d DOMAIN`, to set the path of the file containing the system description, as a `.md` file.

`-o OUTPUT`, to set the path of the folder containing the generated cybersecurity requirements, as a `.json` file and the execution details.

`-c CHAIN`, to set the name of the Langchain's chain topology declaration to use (located at [/src/generate
-requirements/templates/chain](/src/generate
-requirements/templates/chain)).

`--help`, to show the help message for the script.

Example:
```bash
python main.py \
    --standards data/annotated_standard_subset.json \
    --domain data/ai4i4.md \
    --output results/requirements \
    --chain cot_llama
```

> [!IMPORTANT]
> In its default configuration, the [requirements generation script](/src/generate-requirements/main.py) makes use of the _meta.llama3-1-405b-instruct-v1:0_ model provided by AWS for serverless inference.

## Key Artifacts

| Path                               | Brief description                                     |
| ---------------------------------- | ----------------------------------------------------- |
| `data/ai4i4.md`                    | System specification of the pilot use‑case.           |
| `annotated_standard_subset.json`   | Parameterised ISO‑27002 controls.                     |
| `data/prompt/**`                   | 180+ prompt templates, categorised by task and model. |
| `results/analysis/summary.csv`     | Precision, recall, F2 and uplift F2 for every run.    |
| `results/analysis/consistency.csv` | Jaccard indices across successive runs.               |
| `doc/*_execution_details.md`       | Detailed execution logs per configuration.            |

Complete dataset datasheets are provided in the [data/README.md](data/README.md) and [results/README.md](results/README.md) files.

## Reproducibility Notes

- **Determinism**  Because of the inherent stochasticity of LLMs, results may vary across runs. Please refer to the consistency metrics in `results/analysis/consistency.csv` to assess stability considerations.
- **Data licensing**  ISO‑27002 excerpts are replaced by identifiers to comply with copyright; users must possess the full standard.
- **Model access**  Some models (e.g., GPT‑4, Mistral) require API keys or specific access permissions. Ensure you have the necessary credentials before running the scripts.
- **Environment**  The scripts are tested on Python 3.10+ with the dependencies listed in `requirements.txt`. Ensure your environment matches these specifications to avoid compatibility issues.

## Ethics and Intended Use

This research is conducted under the principles of responsible AI. The generated requirements are intended for educational and research purposes only. Users must ensure compliance with local laws and ethical guidelines when applying these results in real-world scenarios.

Any use involving production compliance auditing, legal certification, or critical system design should involve human oversight and validation by qualified cybersecurity professionals.

## Version History

| Version | Date       | Highlights                                                  |
| ------- | ---------- | ----------------------------------------------------------- |
| 1.0     | 2025‑06‑30 | Initial public release, aligned with paper submission.      |

## License and Citation

This repository uses two licenses:

- **Software**: Proprietary license — personal, non-commercial research use only; no modification, redistribution, or commercial use permitted (see [LICENSE](LICENSE)).
- **Data**: Creative Commons Attribution 4.0 International (CC BY 4.0) (see [LICENSE](LICENSE_DATA.txt)).

If you use this repository in your research, please cite it as follows:

```bibtex
@misc{llmsec2025iso,
  author={Yelmo, Juan Carlos and Martín, Yod-Samuel and Perez-Acuna, Santiago},
  title={A Case Study on AI-augmented Cybersecurity Requirements Generation leveraging LLMs Capabilities | Reproducible Research Package},
  year={2025},
  url={https://github.com/STRAST-UPM/ai_requirements_generation_rr},
  doi={10.5281/zenodo.15641295},
  version={1.0},
}
```

## Contact

Juan Carlos Yelmo García - [juancarlos.yelmo@upm.es](mailto:juancarlos.yelmo@upm.es)

Yod Samuel Martín García - [ys.martin@upm.es](mailto:ys.martin@upm.es)

Santiago Pérez Acuña - [santiago.perez.acuna@upm.es](mailto:santiago.perez.acuna@upm.es)

---

*Last updated : 2025‑06‑30*
