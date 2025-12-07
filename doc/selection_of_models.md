# Selection of Models

This document provides a traceable description of the selection of large language models (LLMs) used in our experimental evaluation, as shown in the corresponding leaderboard queries and benchmark datasets.

Our model selection was based primarily on a snapshot of the **Hugging Face Open LLM Leaderboard** (by *open-llm-leaderboard*) taken on **September 15th, 2024**, filtered to include **high-performing**, **instruction-following**, **non-domain-finetuned**, **decoder-only frontier models**.

We further cross-referenced performance metrics from additional public leaderboards to ensure robustness and traceability, including:  

- **[Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/?pinned=Qwen%2FQwen2-72B-Instruct_bfloat16_1af63c698f59c4235668ec9c1395468cb7cd7e79%2Cmeta-llama%2FLlama-3.1-70B-Instruct_bfloat16_b9461463b511ed3c0762467538ea32cf7c9669f2_True%2CQwen%2FQwen2-72B-Instruct_bfloat16_1af63c698f59c4235668ec9c1395468cb7cd7e79_False%2Cmistralai%2FMixtral-8x22B-Instruct-v0.1_bfloat16_b0c3516041d014f640267b14feb4e9a84c8e8c71_True&columns=rank%2Cmodel.type_icon%2Cid%2Cmodel.average_score%2Cevaluations.musr.normalized_score%2Cevaluations.mmlu_pro.normalized_score%2Cmetadata.upload_date%2Cmetadata.submission_date%2Cfeatures.is_highlighted_by_maintainer%2Cevaluations.ifeval.normalized_score%2Cevaluations.bbh.normalized_score%2Cevaluations.gpqa.normalized_score%2Cmetadata.hub_hearts%2Cmetadata.base_model%2Cfeatures.is_official_provider%2Cmodel.architecture%2Cfeatures.is_moe&averageMode=visible&rankingMode=dynamic&official=true&types=chat%2Cmerge)** (by *open-llm-leaderboard*): Sept. 15th, 2024 snapshot, from commit `2f9a8f919661132e2f904c3ac59810facd94c4d7`, including only chat and merge model types from official providers.
- **[LMArena Leaderboard](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)** (by *lmarena-ai*, also known as *[Text Arena | LMArena](https://lmarena.ai/leaderboard/text)*): Sept. 15th, 2024 snapshot (`elo_results_20240915.pkl`), including all available models.
- **[HELM (Holistic Evaluation of Language Models)](https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard)** capabilities benchmark: Mar. 20th, 2025 snapshot (first release), including all available models.

## Selected Models

The following models were included in our analysis:

- **Meta/LLaMa-3.1-405B-Instruct-v1.0**
- **Qwen/Qwen2-72B-Instruct**
- **mistralai/Mixtral-8x22B-Instruct-v0.1**
- **GPT-4-Turbo-2024-04-09**

## Cross-Leaderboard Reference Data

The following table summarizes model identifiers and performance metrics as reported across referenced leaderboards:

| Model                                 | Open LLM Leaderboard Average (score) | Open LLM Leaderboard Rank | LMArena Rating (score)         | LMArena Rank | HELM Capabilities Mean score | HELM Capabilities Rank |
|:--------------------------------------|:------------------------------------:|:--------------------------:|:------------------------------:|:------------:|:----------------------------:|:----------------------:|
| **Meta/LLaMa-3.1-405B-Instruct-v1.0** | 41.7357*                             | 2                          | 1265.532 / 1265.702 (bf16/fp8) | 11 / 12      | 0.618                        | 8                      |
| **Qwen2-72B-Instruct**                | 42.4863                              | 1                          | 1186.909                       | 58           | 0.599*                       | 11                     |
| **Mixtral-8×22B-Instruct-v0.1**       | 33.8857                              | 9                          | 1147.468                       | 83           | 0.478                        | 19                     |
| **GPT-4-Turbo-2024-04-09**            | –                                    | –                          | 1256.745                       | 21           | –                            | –                      |

\* Open LLM Leaderboard score for **Meta/LLaMa-3.1-405B-Instruct-v1.0** is taken from **Meta-Llama-3.1-70B-Instruct**.  
\* HELM Capabilities mean score for **Qwen2-72B-Instruct** is taken from **Qwen2.5 Instruct Turbo (72B)**.

## Version History

| Version | Date       | Change                                            |
| ------- | ---------- | ------------------------------------------------- |
| 1.0     | 2025‑06-30 | Initial public release matching paper submission. |
| 2.0     | 2025‑12-01 | Second release including additional executions.   |

---

*Last updated : 2025‑12‑01*