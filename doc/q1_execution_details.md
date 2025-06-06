# Execution Details

Execution Time: 2024-11-26 15:51:59

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN | provider: huggingface<br>repo_id: Qwen/Qwen2-72B-Instruct | top_p: 0.95<br>temperature: 0.6<br>verbose: False | (plain, check-applicability/qwen/plain-template.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN | provider: huggingface<br>repo_id: Qwen/Qwen2-72B-Instruct | top_p: 0.85<br>temperature: 0.55<br>verbose: False | (plain, search-domain-elements/qwen/plain-template-lowsigma.txt) |
| GENERATE_CHAIN | provider: huggingface<br>repo_id: Qwen/Qwen2-72B-Instruct | top_p: 0.85<br>temperature: 0.6<br>verbose: False | (plain, generate-requirements/qwen/plain-template.txt) |
| FORMAT_CHAIN | provider: huggingface<br>repo_id: Qwen/Qwen2-72B-Instruct | top_p: 0.95<br>temperature: 0.5<br>verbose: False | (plain, format-json/qwen/plain-template.txt) |
