CHECK_APPLICABILITY_CHAIN = {
  "descriptor": "CHECK_APPLICABILITY_CHAIN",
  "endpoint": {
    "provider": "openai",
    "model_name": "gpt-4-turbo",
  },
  "parameters": {
    "temperature": 0.6,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "check-applicability/gpt4/system-template-v2.txt"),
      ("human", "check-applicability/gpt4/user-template-v2.txt"),
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
    "provider": "openai",
    "model_name": "gpt-4-turbo",
  },
  "parameters": {
    "temperature": 0.65,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "search-domain-elements/gpt4/system-template-v2.txt"),
      ("human", "search-domain-elements/gpt4/user-template-v3-lowsigma.txt"),
    ],
    "input_variables": ["domain_description", "input_requirement"],
    "output_key": "project_entities_relation"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": False
}

GENERATE_CHAIN = {
  "descriptor": "GENERATE_CHAIN",
  "endpoint": {
    "provider": "openai",
    "model_name": "gpt-4-turbo",
  },
  "parameters": {
    "temperature": 0.7,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "generate-requirements/gpt4/system-template-v2.txt"),
      ("human", "generate-requirements/gpt4/user-template-v2.txt"),
    ],
    "input_variables": ["domain_description", "input_requirement", "project_entities_relation"],
    "output_key": "requirements_document"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": False
}

FORMAT_CHAIN = {
  "descriptor": "FORMAT_CHAIN",
  "endpoint": {
    "provider": "openai",
    "model_name": "gpt-4o-mini",
  },
  "parameters": {
    "temperature": 0.5,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "chat",
    "template_files": [
      ("system", "format-json/gpt4/system-template-v2.txt"),
      ("human", "format-json/gpt4/user-template-v2.txt"),
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
