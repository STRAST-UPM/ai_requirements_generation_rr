# TODO: Name of the paper

## TODO: Research Description

## TODO: About This Repository

### TODO Review: Built Using

Base technologies:

* [Python](https://www.python.org/)
* [LangChain](https://www.langchain.com/)
* [LLaMa 3](https://www.llama.com/)

Additional dependencies:

* [NumPy](https://numpy.org/)
* [HuggingFace Hub](https://huggingface.co/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

Given that [python3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) are installed and correctly configured in the system, and assuming that you have a valid [Huggingface PRO token](https://huggingface.co/pricing#pro), you may follow these steps.

### Prerequisites

1. Clone this repository locally.

```bash
git clone git@github.com:STRAST-UPM/ai_requirements_generation_rr.git
```

2. Create python [virtual environment](https://docs.python.org/3/library/venv.html) and activate it (**recommended**)

```bash
python -m venv .venv
source .venv/bin/activate 
```

3. Install all required dependencies.

```bash
pip install -r app/requirements.txt
```

4. Create a `.env` file at the [/app](/app) directory with the following content (depending on the models you want to use):

```bash
HUGGINGFACE_API_TOKEN=<your_token>
MISTRAL_API_TOKEN=<your_token>
OPENAI_API_TOKEN=<your_token>
```

> [!TIP]
> You may find an example of the `.env` file at [/app/.env.example](/app/adapt-standard/.env.example).

5. If you want to use models provided by AWS, configure AWS CLI with the credentials provided by the AWS administration console.

```bash
aws configure
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Execution

### Generation of Cybersecurity Requirements

To generate cybersecurity requirements for a given system description, you may use the [/app/main.py](/app/main.py) script. You may specify the following parameters:

`-s STANDARDS`, to set the path of the file containing the adapted cybersecurity standards, as a `.json` file.

`-d DOMAIN`, to set the path of the file containing the system description, as a `.md` file.

`-o OUTPUT`, to set the path of the folder containing the generated cybersecurity requirements, as a `.json` file and the execution details.

`-c CHAIN`, to set the name of the Langchain's chain topology declaration to use (located at [/app/templates/chain](/app/templates/chain)).

`--help`, to show the help message for the script.

Example:
```bash
python app/main.py \
    --standards artifacts/annotated_standard_subset.json \
    --domain artifacts/ai4i4.md \
    --output generated/requirements \
    --chain cot_llama
```

> [!IMPORTANT]
> In its default configuration, the [requirements generation script](/app/generate-requirements/main.py) makes use of the _meta.llama3-1-405b-instruct-v1:0_ model provided by AWS for serverless inference.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

This repository uses two licenses:

- **Code**: MIT License (see [LICENSE](LICENSE)).
- **Data**: Creative Commons Attribution 4.0 International (CC BY 4.0) (see [LICENSE](LICENSE_DATA.txt)).

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

Juan Carlos Yelmo García - juancarlos.yelmo@upm.es

Yod Samuel Martín García - ys.martin@upm.es

Santiago Pérez Acuña - santiago.perez.acuna@upm.es

<p align="right">(<a href="#top">back to top</a>)</p>