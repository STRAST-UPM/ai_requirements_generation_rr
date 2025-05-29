# Execution Details

Execution Time: 2024-10-16 17:27:47

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.6<br>verbose: False | (plain, check-applicability/llama3/plain-template.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.65<br>verbose: False | (plain, search-domain-elements/llama3/plain-template.txt) |
| GENERATE_CHAIN | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.7<br>verbose: False | (plain, generate-requirements/llama3/plain-template.txt) |
| FORMAT_CHAIN | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.5<br>verbose: False | (plain, format-json/llama3/plain-template.txt) |
