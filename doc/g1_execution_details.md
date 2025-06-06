# Execution Details

Execution Time: 2024-11-26 16:59:00

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN (x1) | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.6<br>verbose: False | (system, check-applicability/gpt4/system-template-v2.txt)<br>(human, check-applicability/gpt4/user-template-v2.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN (x1) | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.55<br>verbose: False | (system, search-domain-elements/gpt4/system-template-v2.txt)<br>(human, search-domain-elements/gpt4/user-template-v3-lowsigma.txt) |
| GENERATE_CHAIN (x1) | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.6<br>verbose: False | (system, generate-requirements/gpt4/system-template-v2.txt)<br>(human, generate-requirements/gpt4/user-template-v2.txt) |
| FORMAT_CHAIN (x1) | provider: openai<br>model_name: gpt-4o-mini | temperature: 0.5<br>verbose: False | (system, format-json/gpt4/system-template-v2.txt)<br>(human, format-json/gpt4/user-template-v2.txt) |
