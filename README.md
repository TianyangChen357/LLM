# LLM Demo Repository

This repository contains lightweight Python examples for using the OpenAI Python SDK and a simple agent orchestration pattern.

## Contents

- `0_test_online_llm_simple.py` - one-shot OpenAI chat request using `gpt-4o`
- `1_test_online_llm_loop.py` - interactive loop for repeated OpenAI chat requests
- `2_test_online_llm_chat.py` - chat session history with repeated back-and-forth conversation
- `3_test_online_llm_agent.py` - agent pattern that asks the model for `command:` or `complete:` responses and executes shell commands
- `4_test_online_llm_agent_with_md.py` - same agent pattern, with system prompts loaded from `Agent/Agent.md`
- `Agent/Agent.py` - standalone agent orchestration script for interacting with OpenAI and executing generated shell commands
- `Agent/Agent.md` - system prompt and behavior instructions for the agent
- `Agent/SKILL.md` - skill definition for the agent environment

## Requirements

- Python 3.12
- `pip` installed
- `python-dotenv` package
- OpenAI SDK installed in the project environment

## Setup

1. Create and activate the Python virtual environment (if not already created):

```bash
cd /home/tchen19/LLM
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
./.venv/bin/pip install openai python-dotenv
```

3. Create a `.env` file in the repo root with your OpenAI key:

```ini
OPENAI_API_KEY=sk-your-openai-key-here
```

4. Secure the `.env` file:

```bash
chmod 600 .env
```

## Usage

### Run a simple OpenAI test

```bash
./.venv/bin/python 0_test_online_llm_simple.py
```

You will be prompted for input and the script will send that message to the OpenAI model.

### Run an interactive loop

```bash
./.venv/bin/python 1_test_online_llm_loop.py
```

### Run a chat session with history

```bash
./.venv/bin/python 2_test_online_llm_chat.py
```

### Use the agent-style executor

```bash
./.venv/bin/python 3_test_online_llm_agent.py
```

This script sends user input to the model and expects responses in one of two forms:
- `command: <shell command>`
- `complete: <final answer>`

The script then executes shell commands and continues the conversation accordingly.

### Use markdown-enhanced agent prompts

```bash
./.venv/bin/python 4_test_online_llm_agent_with_md.py
```

This version loads agent instructions from `Agent/Agent.md`.

## Agent directory

- `Agent/Agent.py` - an orchestrator for the model and shell execution flow
- `Agent/Agent.md` - system prompt/behavior rules
- `Agent/SKILL.md` - additional skill metadata used by the agent

## Notes

- All scripts use the OpenAI Python SDK and expect `OPENAI_API_KEY` to be defined in `.env`.
- Do not commit your `.env` file to source control.
- The agent examples are experimental: they execute shell commands returned by the model, so use them carefully.

## Recommended workflow

1. Activate the `.venv` environment.
2. Confirm your `.env` file contains a valid OpenAI API key.
3. Run the desired demo script.
4. If you want to modify behavior, edit `Agent/Agent.md` or the prompt block inside the script.

## Acknowledgements

This repo was built following guidance from the YouTube tutorial:

- https://www.youtube.com/watch?v=WxDCQhKCS7g&list=PLWPtmU3Rasdis1DSgb6-UXNvvISbwGgXf

Thanks to the author for the instructional example on building an agent with LLMs.
