# Architecture

The Cheshire Cat framework consists of four components: **the Core**, **the Vector Database**, **the LLM** and **the embedder**.

The Core and the Admin Portal are implemented within the framework, while the Vector Database, the LLM and the embedder are external dependencies.

The Core communicates with the Vector Database, the LLM and the embedder, while The Admin Portal communicates with the Core.

The Core is implemented in Python, Qdrant is utilized as Vector Database, the Core support different LLMs and Embbeders (see the [complete list](#compatible-models) below), the Admin Portal is implemented using the Vue framework.

# Core

## Docker Images

To facilitate, speed up, and standardize the Cat's user experience, the Cat contains configuration for use inside Docker.

You can use the pre-compiled images present in the Repo's Docker Registry or build it from scratch:

1. To use the pre-compiled image, add `ghcr.io/cheshire-cat-ai/core:<tag-version>` as value of `image` under the name of the service in the docker-compose:

    ```yml
    cheshire-cat-core:
        image: ghcr.io/cheshire-cat-ai/core:1.5.1
    ```

2. To build it from scratch execute `docker compose build` in the repo folder just cloned.

    This will generate two Docker images. The first one contains the Cat Core and Admin Portal.
    The container name of the core is `cheshire_cat_core`.

The Cat core path `./core` is mounted into the image `cheshire_cat_core`, by default changes to files in this folder force a restart of the Core, this behavior can be disabled using the [`DEBUG`](env-variables.md/#ccat_debug) environment variable.

## Admin Portal

The Admin Portal connects to the core using `localhost` through the port exposed when the container was created, this value can be customized using [environment variables](env-variables.md#ccat_core_host). This port is the only one exposed by the `cheshire_cat_core` image.

## Logging

All the log messages are printed on the standard output and log level can be configured with [`CCAT_LOG_LEVEL`](env-variables.md#ccat_log_level) environment variables. You can check logging system documentation [here](../../plugins/logging.md).

## Configuration

Some options of the Core can be customized using [environment variables](env-variables.md).

## Compatible Models

The cat is agnostic, meaning You can attach your preferred llm and embedder model/provider. The Cat supports the most used ones, but you can increase the number of models/providers by [plugins](../../plugins/hooks.md/#__tabbed_1_5), here is a list of the main ones:

1. OpenAI and Azure OpenAI
2. Cohere
3. Ollama (LLM model only)
4. HuggingFace TextInference API (LLM model only)
5. Google Gemini
6. Qdrant FastEmbed (Embedder model only)

# Vector Memory

## What we use as vector memory?

The Cat provides a connection to [qdrant](https://qdrant.tech/) through his Python client.
By default the Core tries to connect to a Qdrant database, if the connection fails then it switches to the `local Qdrant database`.
It is highly recommended to connect the Cat to a **Qdrant database** to increase performance and capacity!

## Qdrant Cloud or Self Hosting

**Qdrant** provides to 2 paths:

1. Self-host Qdrant by using docker, follows an example `compose.yml`:

```yaml
version: '3.7'

services:

	cheshire-cat-core:
		image: ghcr.io/cheshire-cat-ai/core:latest
		container_name: cheshire_cat_core
		depends_on:
			- cheshire-cat-vector-memory
		env_file:
			- .env
		ports:
			- ${CORE_PORT:-1865}:80
		volumes:
			- ./static:/app/cat/static
			- ./plugins:/app/cat/plugins
			- ./data:/app/cat/data
		restart: unless-stopped

	cheshire-cat-vector-memory:
		image: qdrant/qdrant:latest
		container_name: cheshire_cat_vector_memory
		expose:
			- 6333
		volumes:
			- ./long_term_memory/vector:/qdrant/storage
		restart: unless-stopped
```

2. Add this enviroment variables in your `.env` file:

```bash
# Qdrant server
QDRANT_HOST=cheshire_cat_vector_memory # <url of the cluster>
QDRANT_PORT=6333 # <port of the cluster, usually 6333>
QDRANT_API_KEY="" # optional <api-key>
```

# Admin Portal

## Use case

The Admin Portal is an administration/debugging panel to interact with the Cat by chatting, uploading files, exploring the memory, changing the LLM and Embedder Models while providing minimal authentication through an `api_key`.
