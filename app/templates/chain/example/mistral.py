EXAMPLE_MISTRAL_CHAIN = {
  "descriptor": "EXAMPLE_MISTRAL_CHAIN",
  "endpoint": {
    "provider": "mistral",
    "model": "open-mixtral-8x22b"
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.7,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "generate-requirements/mistral-template.txt")
    ],
    "input_variables": ["domain_description", "input_requirement"],
    "output_key": "applicability_reason"
  },
  "early_stop": "Phrase to prevent further generation",
  "save_output": True,
  "verbose_input": False
}