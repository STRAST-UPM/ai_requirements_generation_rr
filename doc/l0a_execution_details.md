# Execution Details

Execution Time: 2024-12-07 10:09:22

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.6<br>max_gen_len: 2048<br>verbose: False | (plain, check-applicability/llama3/plain-template-v2.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.65<br>max_gen_len: 2048<br>verbose: False | (plain, search-domain-elements/llama3/plain-template-norepeat.txt) |
| GENERATE_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.7<br>max_gen_len: 2048<br>verbose: False | (plain, generate-requirements/llama3/plain-template-norepeat.txt) |
| FORMAT_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-70b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.5<br>max_gen_len: 2048<br>verbose: False | (plain, format-json/llama3/plain-template-v2.txt) |
