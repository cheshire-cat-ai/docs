To facilitate, speed up, and standardize the Cat's user experience, the Cat lives inside a Docker container.


## Cat standalone

```yaml
services:

  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:latest
    container_name: cheshire_cat_core
    ports:
      - ${CORE_PORT:-1865}:80
    volumes:
      - ./static:/app/cat/static
      - ./plugins:/app/cat/plugins
	  - ./data:/app/cat/data
```

## Cat + Ollama

The cat is agnostic, meaning You can attach your preferred llm and embedder model/provider. The Cat supports the most used ones, but you can increase the number of models/providers by [plugins](../../plugins/hooks.md/#__tabbed_1_5), here is a list of the main ones:

1. OpenAI and Azure OpenAI
2. Cohere
3. Ollama (LLM model only)
4. HuggingFace TextInference API (LLM model only)
5. Google Gemini
6. Qdrant FastEmbed (Embedder model only)
7. (custom via plugin)

If you want a setup Cat + Ollama, here an example `compose.yml`:

```yaml
services:
  cheshire-cat-core:
	image: ghcr.io/cheshire-cat-ai/core:latest
	container_name: cheshire_cat_core
	depends_on:
	  - ollama
	ports:
	  - ${CORE_PORT:-1865}:80
	volumes:
	  - ./static:/app/cat/static
	  - ./plugins:/app/cat/plugins
	  - ./data:/app/cat/data
	restart: unless-stopped

	ollama:
	  container_name: ollama_cat
	  image: ollama/ollama:latest
	  volumes:
		- ./ollama:/root/.ollama
	  expose:
		- 11434
	  environment:
	    - gpus=all
	  deploy:
	    resources:
	      reservations:
	        devices:
              - driver: nvidia
                count: 1
                capabilities: [gpu]
```

## Cat + Qdrant

By default the Core uses an embedded version of [Qdrant](https://qdrant.tech/), based on SQLite.  
It is highly recommended to connect the Cat to a full Qdrant instance to increase performance and capacity!

```yaml
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

Add this enviroment variables in your `.env` file:

```bash
# Qdrant server
QDRANT_HOST=cheshire_cat_vector_memory # <url of the cluster>
QDRANT_PORT=6333 # <port of the cluster, usually 6333>
QDRANT_API_KEY="" # optional <api-key>
```


