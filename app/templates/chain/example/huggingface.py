EXAMPLE_HUGGINGFACE_CHAIN = {
  "descriptor": "EXAMPLE_HUGGINGFACE_CHAIN",
  "endpoint": {
    "provider": "huggingface",
    "repo_id": "meta-llama/Meta-Llama-3.1-405B-Instruct",
  },
  "parameters": {
    "top_k": 30,
    "top_p": 0.95,
    "temperature": 0.7,
    "repetition_penalty": 1.3,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "generate-requirements/llama3/system-template-v3.txt"),
      ("plain", "generate-requirements/llama3/user-template-v3.txt")
    ],
    "input_variables": ["domain_description", "input_requirement", "project_entities_relation"],
    "output_key": "requirements_document"
  },
  "early_stop": "Phrase to prevent further generation",
  "save_output": True,
  "verbose_input": False
}