---
title: "Installation"
---

The Cheshire Cat is a Python package. The only prerequisite is [`uv`](https://docs.astral.sh/uv/getting-started/installation/), the Python package manager.

## Install and run

In an empty folder:

```bash
uv init --bare
uv add cheshire-cat-ai
uv run ccat
```

The first run downloads the dependencies and scaffolds a minimal project (a `plugins/` folder and a `data/` folder for persistence. When you see the Cheshire Cat logo in the terminal, everything is up and running.

## Where the Cat lives

Once running, the Cat exposes three addresses on port `1865`:

| Address | What it is | For |
| --- | --- | --- |
| [localhost:1865](http://localhost:1865) | Web UI | humans |
| [localhost:1865/docs](http://localhost:1865/docs) | REST API playground | humans |
| [localhost:1865/openapi.json](http://localhost:1865/openapi.json) | OpenAPI schema | agents |

:::tip[For coding agents]
Point your agent at [localhost:1865/openapi.json](http://localhost:1865/openapi.json). It is the full, machine-readable contract of every endpoint — the Cat's API surface in one file, no scraping required.
:::

## Configure the LLM

The Cat is not an LLM, it *uses* one. A fresh install ships with a placeholder LLM that just replies "configure me", so the first thing to do is point the Cat at a real model.

You can do this in two ways:

- **From the UI** — open [localhost:1865](http://localhost:1865), go to **Settings**, pick a provider (e.g. OpenAI) and set your API key, then go to Core Settings and select a model (e.g. `openai:gpt-4o`). The choice is persisted.
- **From code** — create a `config.py` in your project folder. It is plain Python, so you can read your key from `.env` / `os.environ`:

  ```python
  DEFAULT_LLM = "openai:gpt-4o"
  DEFAULT_EMBEDDER = "openai:text-embedding-3-small"
  ```

The LLM and embedder are written as `"provider:model"` strings (e.g. `"openai:gpt-4o"`, `"ollama:llama3.2"`).

## Stopping the Cat

Stop the process with `CTRL + C` in the terminal.  
To start it again: `uv run ccat`.
