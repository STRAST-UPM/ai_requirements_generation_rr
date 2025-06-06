GENERATE_CHAIN = {
  "descriptor": "GENERATE_CHAIN",
  "endpoint": {
    "provider": "aws-bedrock",
    "model_id": "meta.llama3-1-405b-instruct-v1:0",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.7,
    "max_gen_len": 2048,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "generate-requirements/deprecated/llama3-template.txt")
    ],
    "input_variables": ["domain_description", "input_requirement"],
    "output_key": "requirements_document"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": False
}

FORMAT_CHAIN = {
  "descriptor": "FORMAT_CHAIN",
  "endpoint": {
    "provider": "aws-bedrock",
    "model_id": "meta.llama3-1-405b-instruct-v1:0",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.5,
    "max_gen_len": 2048,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "format-json/llama3/plain-template-v2.txt")
    ],
    "input_variables": ["requirements_document"],
    "output_key": "requirements_list"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": False
}

STEPS = [
  {
    "chains": [ GENERATE_CHAIN ],
    "parallels": 1,
  },
  {
    "chains": [ FORMAT_CHAIN ],
    "parallels": 1,
  }
]
