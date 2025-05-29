import os
import sys
import time
import json
import regex
import argparse
from dotenv import load_dotenv

from langchain.chains import LLMChain

from helper import LLMEndpointCreator, LLMPromptCreator
from custom_chains import EarlyStoppingSequentialChain, RetryingSequentialChain, ParallelChain

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
load_dotenv()

JSON_PATTERN = regex.compile(r'\{(?:[^{}]|(?R))*\}')
ENABLE_DEBUGGING = True

def main(args):
  with open(args.domain, 'r') as file:
    domain = file.read()
    file.close()
  with open(args.standards, 'r') as file:
    standards = json.load(file)
    file.close()

  original_stdout = sys.stdout
  original_stderr = sys.stderr

  if not ENABLE_DEBUGGING:
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

  chains = []
  stop_conditions = []

  for STEP in config.STEPS:
    input_variables = STEP['chains'][0]['prompt']['input_variables']
    sequential_branches = []
    for i in range(STEP['parallels']):
      branched_chains = []
      for CHAIN in STEP['chains']:
        llm = LLMEndpointCreator.create_endpoint(
          **CHAIN['endpoint'],
          **CHAIN['parameters']
        )
        prompt = LLMPromptCreator.create_prompt(
          **CHAIN['prompt']
        )
        if CHAIN['early_stop']:
          stop_conditions.append(
            lambda results, key=CHAIN['prompt']['output_key'], condition=CHAIN['early_stop']: 
            condition in results[key] if key in results else False
          )
        branched_chains.append(LLMChain(
          llm=llm,
          prompt=prompt,
          output_key=CHAIN['prompt']['output_key'],
          verbose=CHAIN['verbose_input']
        ))
      sequential_branches.append(RetryingSequentialChain(
        chains = branched_chains,
        input_variables = input_variables,
        verbose = ENABLE_DEBUGGING
      ))
    chains.append(ParallelChain(
      chains = sequential_branches,
      input_variables = input_variables,
      verbose = ENABLE_DEBUGGING
    ))
  if not ENABLE_DEBUGGING:
    sys.stdout = original_stdout
    sys.stderr = original_stderr

  main_chain = EarlyStoppingSequentialChain(
    chains = chains,
    input_variables = config.STEPS[0]['chains'][0]['prompt']['input_variables'],
    stop_conditions = stop_conditions,
    return_all = True,
    verbose = ENABLE_DEBUGGING
  )

  output_dir = create_output_dir(os.path.dirname(args.output), config)
  adapted_requirements = []

  for norm in standards:
    for nfr in norm["nfrs"]:
      errorCount = 0
      adapted_nfr = "Invalid"
      while adapted_nfr == "Invalid" and errorCount < 3:
        try:
          adapted_nfr = process_nfr(nfr, domain, main_chain)
        except Exception as e:
          if ENABLE_DEBUGGING:
            print(f"Error: {e}")
          errorCount += 1
      adapted_requirements.append({
        "nfr": nfr,
        "adapted_nfr": adapted_nfr
      })
      print(f"Original norm NFR: {nfr}")
      print(f"Adapted domain requirements:")
      if adapted_nfr['requirements_list']:
        for req in adapted_nfr['requirements_list']:
          try:
            print(f"- {req['name']}: {req['description']}")
          except Exception as e:
            print("- **Unable to parse**")
      else:
        print("- No requirements found")
      print()

      # Rewrite result file every iteration, in case an error occurs during long processes
      save_output(output_dir, adapted_requirements)
  
  print(f"Results saved to {output_dir}")

def process_nfr(nfr, domain, chain):
  response = None
  while response is None:
    try:
      response = chain.invoke({
        "domain_description": domain,
        "input_requirement": nfr
      })
    except Exception as e:
      if ENABLE_DEBUGGING:
        print(f"[!] Received error from model ({e}), retrying...")
      time.sleep(5)
  
  key_prefixes_to_save = []
  for STEP in config.STEPS:
    for CHAIN in STEP['chains']:
      if CHAIN['save_output']:
        key_prefixes_to_save.append(CHAIN['prompt']['output_key'])
  keys = []
  for prefix in key_prefixes_to_save:
    keys.extend([key for key in response.keys() if key.startswith(prefix)])

  processed_response = {key: response[key] for key in keys if key in response}
  if config.STEPS[-1]['chains'][-1]['prompt']['output_key'] in processed_response:
    processed_response['requirements_list'] = parse_json_response(processed_response[config.STEPS[-1]['chains'][-1]['prompt']['output_key']])
  else:
    processed_response['requirements_list'] = []
  return processed_response

def parse_json_response(response):
  parsed_response = []
  for r in JSON_PATTERN.findall(response):
    try:
      parsed_response.append(json.loads(r))
    except Exception as e:
      if ENABLE_DEBUGGING:
        print(f"Warning: non-json bracketed object found in response: {r}")
  if len(parsed_response) == 0:
    if ENABLE_DEBUGGING:
      print(f"Warning: no valid JSON found in response")
    return []
  return parsed_response

def create_output_dir(path, config):
  execution_time = time.strftime("exec_%Y-%m-%d_%H-%M-%S")
  output_dir = os.path.join(path, execution_time)
  os.makedirs(output_dir, exist_ok=False)
  execution_details_path = os.path.join(output_dir, 'execution_details.md')
  with open(execution_details_path, 'w') as file:
    file.write("# Execution Details\n\n")
    file.write(f"Execution Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    file.write("This document provides details about each step of the execution, including the endpoint used, hyperparameters, and the prompt file.\n\n")
    file.write("| Step | Endpoint | Hyperparameters | Prompt Files |\n")
    file.write("|------|----------|-----------------|--------------|\n")
    for STEP in config.STEPS:
      for CHAIN in STEP['chains']:
        endpoint_str = "<br>".join([f"{k}: {v}" for k, v in CHAIN['endpoint'].items()])
        parameters_str = "<br>".join([f"{k}: {v}" for k, v in CHAIN['parameters'].items()])
        prompt_files_str = "<br>".join([f"({t[0]}, {t[1]})" for t in CHAIN['prompt']['template_files']])
        file.write(f"| {CHAIN['descriptor']} (x{STEP['parallels']}) | {endpoint_str} | {parameters_str} | {prompt_files_str} |\n")
  return output_dir

def save_output(output_dir, requirements):
  with open(os.path.join(output_dir, 'requirements.json'), 'w') as file:
    json.dump(requirements, file, indent=2)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description='Adapts given cybersecurity standards to the provided domain model'
  )
  parser.add_argument(
    '--chain', '-c', type=str,
    default="cot_llama",
    help='the name of the chain configuration file to be used'
  )
  parser.add_argument( 
    '--domain', '-d', type=str,
    default=os.path.join(os.path.dirname(__file__), '../artifacts/ai4i4.md'),
    help='the path to the domain model to be used, interpreted as plain text'
  )
  parser.add_argument(
    '--standards', '-s', type=str,
    default=os.path.join(os.path.dirname(__file__), '../artifacts/annotated_standard_subset.json'),
    help='the path to the cybersecurity standards to be used, interpreted as JSON'
  )
  parser.add_argument(
    '--output', '-o', type=str,
    default=os.path.join(os.path.dirname(__file__), '../generated/requirements/'),
    help='the directory to save the generated non-functional requirements'
  )
  args = parser.parse_args()
  match args.chain:
    case "cot_llama":
      import templates.chain.cot_llama as config
    case "cot_llama_x4":
      import templates.chain.cot_llama_x4 as config
    case "cot_llama_fewshot":
      import templates.chain.cot_llama_fewshot as config
    case "cot_gpt4":
      import templates.chain.cot_gpt4 as config
    case "cot_gpt4_x4":
      import templates.chain.cot_gpt4_x4 as config
    case "cot_qwen":
      import templates.chain.cot_qwen as config
    case "cot_mistral":
      import templates.chain.cot_mistral as config
    case "aio_llama":
      import app.templates.chain.aio_llama as config
    case _:
      raise ValueError(f"Chain {args.chain} not found")
  main(args)
