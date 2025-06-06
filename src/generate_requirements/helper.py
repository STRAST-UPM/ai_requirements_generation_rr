from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_community.chat_models import ChatOpenAI
from langchain_aws import ChatBedrock

from langchain.prompts import PromptTemplate, ChatPromptTemplate

import os

class LLMEndpointCreator:
  @staticmethod
  def create_endpoint(provider, **kwargs):
    match provider:
      case 'huggingface':
        llm = HuggingFaceEndpoint(
          huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_TOKEN"),
          **kwargs
        )
        return ChatHuggingFace(llm=llm)
      case 'huggingface-dedicated':
        return HuggingFaceEndpoint(
          huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_TOKEN"),
          **kwargs
        )
      case 'openai':
        return ChatOpenAI(
          openai_api_key = os.getenv("OPENAI_API_TOKEN"),
          **kwargs
        )
      case 'mistral':
        return ChatMistralAI(
          mistral_api_key = os.getenv("MISTRAL_API_TOKEN"),
          **kwargs
        )
      case 'aws-bedrock':
        return ChatBedrock(
          model_id = kwargs.pop("model_id"),
          model_kwargs = {parameter: kwargs.pop(parameter)
                          for parameter in ["top_p", "temperature", "max_gen_len"]},
          **kwargs
        )
      case _:
        raise ValueError(f"Unknown provider: {provider}")

class LLMPromptCreator:
  @staticmethod
  def create_prompt(prompt_type, template_files, input_variables, **kwargs):
    messages = []
    for (role, template_file) in template_files:
      with open(os.path.join(os.path.dirname(__file__), f"templates/prompt/{template_file}"), 'r') as file:
        messages.append((role, file.read()))
        file.close()
    match prompt_type:
      case 'plain':
        return PromptTemplate(
          template = messages[0][1],
          input_variables = input_variables
        )
      case 'chat':
        return ChatPromptTemplate(
          messages = messages,
          input_variables = input_variables
        )
      case _:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
