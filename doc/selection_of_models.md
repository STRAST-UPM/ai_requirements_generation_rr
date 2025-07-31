# Selection of Models

This document provides a traceable description of the selection of LLMs used in our experimental evaluation, as shown in the corresponding leaderboard query.

Our selection was based on a snapshot of the Hugging Face Open LLM Leaderboard taken on 15 September 2024, filtered to include high-performing, instruction-following, non-domain-finetuned, decoder-only frontier models. We included the following models:

- **Meta/LLaMa-3.1-70B-Instruct**
- **Qwen/Qwen2-72B-Instruct**
- **mistralai/Mixtral-8x22B-Instruct-v0.1**
- **GPT-4-Turbo** (as a proprietary benchmark reference)

The exact leaderboard configuration used to pin the models can be revisited [at this link](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/?pinned=Qwen%2FQwen2-72B-Instruct_bfloat16_1af63c698f59c4235668ec9c1395468cb7cd7e79%2Cmeta-llama%2FLlama-3.1-70B-Instruct_bfloat16_b9461463b511ed3c0762467538ea32cf7c9669f2_True%2CQwen%2FQwen2-72B-Instruct_bfloat16_1af63c698f59c4235668ec9c1395468cb7cd7e79_False%2Cmistralai%2FMixtral-8x22B-Instruct-v0.1_bfloat16_b0c3516041d014f640267b14feb4e9a84c8e8c71_True&columns=rank%2Cmodel.type_icon%2Cid%2Cmodel.average_score%2Cevaluations.musr.normalized_score%2Cevaluations.mmlu_pro.normalized_score%2Cmetadata.upload_date%2Cmetadata.submission_date%2Cfeatures.is_highlighted_by_maintainer%2Cevaluations.ifeval.normalized_score%2Cevaluations.bbh.normalized_score%2Cevaluations.gpqa.normalized_score%2Cmetadata.hub_hearts%2Cmetadata.base_model%2Cfeatures.is_official_provider%2Cmodel.architecture%2Cfeatures.is_moe&averageMode=visible&rankingMode=dynamic&official=true&types=chat%2Cmerge).
