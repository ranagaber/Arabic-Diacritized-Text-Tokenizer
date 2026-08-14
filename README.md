# Diacritized Arabic Text Tokenizer

A **SentencePiece Unigram tokenizer trained specifically for diacritized Arabic text**.

The tokenizer was trained on **1 million sentences from the Tashkeela Arabic diacritized text corpus**, with a vocabulary size of 30,000 tokens.

This project exposes the tokenizer through a **FastAPI API**, allowing it to be used from Python or any other application through HTTP requests.

## Project Structure

```text
diac_tokenizer/
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    ├── main.py
    └── sentpiece.py
```

## Installation

Install the dependencies with:

```bash
uv sync
```

Alternatively, install UV first if it is not already installed:

```bash
pip install uv
```

## Running the API

Start the FastAPI server with:

```bash
uv run uvicorn --app-dir src main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```


## Using the API with Python

You can interact with the tokenizer using the `requests` library.

Install `requests` if needed:

```bash
uv add requests
```

Then:

```python
import requests

url = "http://127.0.0.1:8000/get_tokens"

text = "يَسْتَخْدِمُونَ"

response = requests.post(
    url,
    json={"text": text}
)

tokens = response.json()["tokens"]

print(tokens)
```

Example output:

```python
['▁يَ', 'سْتَخْدِم', 'ُونَ']
```
