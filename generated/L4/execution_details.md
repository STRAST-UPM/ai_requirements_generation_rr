# Execution Details

Execution Time: 2024-12-03 11:01:02

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| GENERATE_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.7<br>max_gen_len: 2048<br>verbose: False | (plain, generate-requirements/deprecated/llama3-template.txt) |
| FORMAT_CHAIN (x1) | provider: aws-bedrock<br>model_id: meta.llama3-1-405b-instruct-v1:0 | top_p: 0.95<br>temperature: 0.5<br>max_gen_len: 2048<br>verbose: False | (plain, format-json/llama3/plain-template-v2.txt) |
