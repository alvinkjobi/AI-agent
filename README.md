# AI Agent Project

A small Python project for trying an AI model through an OpenAI-compatible chat completions API. The Day 1 examples include a one-shot question and an interactive terminal chat.

## Requirements

- Python 3.10 or later
- Ollama running locally, or another service that provides an OpenAI-compatible API
- A model available to that service

## Setup

From the project directory, create and activate a virtual environment, then install the Python packages:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install openai python-dotenv
```

Create a `.env` file in the project directory with the connection details for your model service:

```dotenv
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=llama3.2
```

These values are an example for Ollama. Make sure Ollama is running and the model named in `MODEL` is available. For another OpenAI-compatible service, use its API base URL, API key, and model name instead. Keep real API keys private; `.env` is excluded from Git.


