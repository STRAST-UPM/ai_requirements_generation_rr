EXAMPLE_CHAIN = {
  "descriptor": "EXAMPLE_CHAIN",
  "endpoint": {
    "provider": "huggingface|openai|mistral",
    "repo_id": "meta-llama/Meta-Llama-3.1-405B-Instruct", # huggingfaceendpoint-specific
    "model_id": "meta.llama3-1-405b-instruct-v1:0", # aws-bedrock-specific
    "model": "mistral-large-latest", # mistral-specific
    "model_name": "gpt-4o-mini", # openai-specific
  },
  "parameters": {
    "top_k": 30, # huggingfaceendpoint-specific
    "top_p": 0.95, # not available for openai
    "temperature": 0.6,
    "repetition_penalty": 1.3, # huggingfaceendpoint-specific
    "max_gen_len": 2048, # aws-bedrock-specific
    "timeout": 1500, # not available for openai, use "request_timeout" instead
    "verbose": False
  },
  "prompt": {
    "prompt_type": "plain|chat",
    "template_files": [
      ("plain|system|human", "path/to/template.txt")
    ],
    "input_variables": ["input-var-1", "input-var-2"],
    "output_key": "output-var"
  },
  "early_stop": None,
  "save_output": True,
  "verbose_input": False
}

STEPS = [
  {
    "chains": [ EXAMPLE_CHAIN ],
    "parallels": 1,
  },
  {
    "chains": [ EXAMPLE_CHAIN, EXAMPLE_CHAIN ],
    "parallels": 4,
  }
]
