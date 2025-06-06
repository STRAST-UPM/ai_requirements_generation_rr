CHECK_APPLICABILITY_CHAIN = {
  "descriptor": "CHECK_APPLICABILITY_CHAIN",
  "endpoint": {
    "provider": "mistral",
    "model": "open-mixtral-8x22b"
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.6,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "check-applicability/mistral/plain-template.txt")
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
    "provider": "mistral",
    "model": "open-mixtral-8x22b"
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.65,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "search-domain-elements/mistral/plain-template-lowsigma.txt")
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
      ("plain", "generate-requirements/mistral/plain-template.txt")
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
    "provider": "mistral",
    "model": "open-mixtral-8x22b"
  },
  "parameters": {
    "top_p": 0.95,
    "temperature": 0.5,
    "timeout": 1500,
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain",
    "template_files": [
      ("plain", "format-json/mistral/plain-template.txt")
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
