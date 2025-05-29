CHECK_APPLICABILITY_CHAIN = {
  "descriptor": "CHECK_APPLICABILITY_CHAIN",
  "endpoint": {
    "provider": "huggingface",
    "repo_id": "Qwen/Qwen2-72B-Instruct",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.6,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "check-applicability/qwen/system-template.txt"),
      ("human", "check-applicability/qwen/user-template.txt")
    ],
    "input_variables": ["domain_description", "input_requirement"],
    "output_key": "applicability_reason"
  },
  "early_stop": "The requirement is not applicable",
  "save_output": True,
  "verbose_input": False
}

SEARCH_DOMAIN_ELEMENTS_CHAIN = {
  "descriptor": "SEARCH_DOMAIN_ELEMENTS_CHAIN",
  "endpoint": {
    "provider": "huggingface",
    "repo_id": "Qwen/Qwen2-72B-Instruct",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.65,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "search-domain-elements/qwen/system-template-lowsigma.txt"),
      ("human", "search-domain-elements/qwen/user-template-lowsigma.txt")
    ],
    "input_variables": ["domain_description", "input_requirement"],
    "output_key": "project_entities_relation"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": True
}

GENERATE_CHAIN = {
  "descriptor": "GENERATE_CHAIN",
  "endpoint": {
    "provider": "huggingface",
    "repo_id": "Qwen/Qwen2-72B-Instruct",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.7,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "generate-requirements/qwen/system-template.txt"),
      ("human", "generate-requirements/qwen/user-template.txt")
    ],
    "input_variables": ["domain_description", "input_requirement", "project_entities_relation"],
    "output_key": "requirements_document"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": True
}

FORMAT_CHAIN = {
  "descriptor": "FORMAT_CHAIN",
  "endpoint": {
    "provider": "huggingface",
    "repo_id": "Qwen/Qwen2-72B-Instruct",
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.5,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "format-json/qwen/system-template.txt"),
      ("human", "format-json/qwen/user-template.txt")
    ],
    "input_variables": ["requirements_document"],
    "output_key": "requirements_list"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": True
}

STEPS = [
  {
    "chains": [ CHECK_APPLICABILITY_CHAIN ],
    "parallels": 1,
  },
  {
    "chains": [ SEARCH_DOMAIN_ELEMENTS_CHAIN ],
    "parallels": 1,
  },
  {
    "chains": [ GENERATE_CHAIN ],
    "parallels": 1,
  },
  {
    "chains": [ FORMAT_CHAIN ],
    "parallels": 1,
  }
]
