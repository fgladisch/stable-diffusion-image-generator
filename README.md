# Stable Diffusion Image Generator

Generate multiple images using Stable Diffusion 2.1 with a prompt and negativate prompt.

## Usage

Create a .env file with your prompt and a negative prompt:

```sh
PROMPT="(black cat), (digital art), cyberpunk, (sunglasses with purple reflection)"
NEGATIVE_PROMPT="watermark, text, blurry, human"
```

Run the python script:

```sh
python diffuse.py
```

Your output will be in the folder `output/<date>`.

## Setup

Install Python 3.11.3 using `pyenv`:

```sh
pyenv install 3.11.3
```

Create a Python environment using `pyenv-virtualenv` or `python -m venv`

```sh
pyenv virtualenv 3.11.3 stable-diffusion
```

Install the modules from `requirements.txt`:

```sh
pip install -r requirements.txt
```
