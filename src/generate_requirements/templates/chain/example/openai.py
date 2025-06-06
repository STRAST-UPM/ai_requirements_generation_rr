EXAMPLE_OPENAI_CHAIN = {
  "descriptor": "EXAMPLE_OPENAI_CHAIN",
  "endpoint": {
    "provider": "openai",
    "model_name": "gpt-4o-mini"
  },
  "parameters": {
    "temperature": 0.6,
    "request_timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "generate-requirements/gpt4/system-template.txt"),
      ("human", "generate-requirements/gpt4/user-template.txt"),
    ],
    "input_variables": ["domain_description", "input_requirement", "project_entities_relation"],
    "output_key": "requirements_document"
  },
  "early_stop": "Phrase to prevent further generation",
  "save_output": True,
  "verbose_input": False
}
