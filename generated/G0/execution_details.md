# Execution Details

Execution Time: 2024-10-17 16:07:31

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.6<br>verbose: False | (system, check-applicability/gpt4/system-template.txt)<br>(human, check-applicability/gpt4/user-template.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.65<br>verbose: False | (system, search-domain-elements/gpt4/system-template.txt)<br>(human, search-domain-elements/gpt4/user-template.txt) |
| GENERATE_CHAIN | provider: openai<br>model_name: gpt-4-turbo | temperature: 0.7<br>verbose: False | (system, generate-requirements/gpt4/system-template.txt)<br>(human, generate-requirements/gpt4/user-template.txt) |
| FORMAT_CHAIN | provider: openai<br>model_name: gpt-4o-mini | temperature: 0.5<br>verbose: False | (system, format-json/gpt4/system-template.txt)<br>(human, format-json/gpt4/user-template.txt) |
