EXAMPLE_BEDROCK_CHAIN = {
  "descriptor": "EXAMPLE_BEDROCK_CHAIN",
  "endpoint": {
    "provider": "aws-bedrock",
    "model_id": "meta.llama3-1-405b-instruct-v1:0",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.6,
    "max_gen_len": 2048,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "generate-requirements/llama3-template.txt")
    ],
    "input_variables": ["domain_description", "input_requirement", "project_entities_relation"],
    "output_key": "requirements_document"
  },
  "early_stop": "Phrase to prevent further generation",
  "save_output": True,
  "verbose_input": False
}