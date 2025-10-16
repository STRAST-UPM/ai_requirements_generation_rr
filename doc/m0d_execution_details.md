# Execution Details

Execution Time: 2025-10-16 19:31:38

This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.

| Step | Endpoint | Hyperparameters | Prompt Files |
|------|----------|-----------------|--------------|
| CHECK_APPLICABILITY_CHAIN (x1) | provider: mistral<br>model: open-mixtral-8x22b | top_p: 0.95<br>temperature: 0.6<br>timeout: 1500<br>verbose: False | (plain, check-applicability/mistral/plain-template.txt) |
| SEARCH_DOMAIN_ELEMENTS_CHAIN (x1) | provider: mistral<br>model: open-mixtral-8x22b | top_p: 0.95<br>temperature: 0.65<br>timeout: 1500<br>verbose: False | (plain, search-domain-elements/mistral/plain-template-lowsigma.txt) |
| GENERATE_CHAIN (x1) | provider: mistral<br>model: open-mixtral-8x22b | top_p: 0.95<br>temperature: 0.7<br>timeout: 1500<br>verbose: False | (plain, generate-requirements/mistral/plain-template.txt) |
| FORMAT_CHAIN (x1) | provider: mistral<br>model: open-mixtral-8x22b | top_p: 0.95<br>temperature: 0.5<br>timeout: 1500<br>verbose: False | (plain, format-json/mistral/plain-template.txt) |
