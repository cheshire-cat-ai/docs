To facilitate, speed up, and standardize the Cat's user experience, the Cat lives inside a Docker container. This allows for maximum power, flexibility and portability, but requires a little understanding from you on [how docker works](https://docs.docker.com/get-started/).


## Cat standalone

```yaml
services:

  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:latest
    container_name: cheshire_cat_core
    ports:
      - 1865:80
    volumes:
      - ./static:/app/cat/static
      - ./plugins:/app/cat/plugins
      - ./data:/app/cat/data
```

## Cat + Ollama

The Cat is model agnostic, meaning you can attach your preferred LLM and embedder model/provider. The Cat supports the most used ones, but you can increase the number of models/providers by [plugins](../../plugins/hooks.md/#__tabbed_1_5), here is a list of the main ones:

1. OpenAI and Azure OpenAI
2. Cohere
3. Ollama
4. HuggingFace TextInference API (LLM model only)
5. Google Gemini
6. Qdrant FastEmbed (Embedder model only)
7. (custom via plugin)

Let's see a full local setup for Cat + Ollama.  
To make this work properly, be sure your docker engine can see the GPU via [NVIDIA docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

As an alternative you can install Ollama directly on your machine and making the Cat aware of it in the Ollama LLM settings, inserting your local network IP or using `host.docker.internal`.

Example `compose.yml`:

```yaml
services:

  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:latest
    container_name: cheshire_cat_core
    depends_on:
      - ollama
    ports:
      - 1865:80
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

For a solid local embedder, choose one from the FastEmbed list.  
The Cat will download the embedder in `cat/data` and will use it to embed text.  
Congratulations, you are now free from commercial LLM providers.

## Cat + Qdrant

By default the Core uses an embedded version of [Qdrant](https://qdrant.tech/), based on SQLite.  
It is highly recommended to connect the Cat to a full Qdrant instance to increase performance and scalability!

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
      - 1865:80
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
CCAT_QDRANT_HOST=cheshire_cat_vector_memory # <url of the cluster>
CCAT_QDRANT_PORT=6333 # <port of the cluster, usually 6333>
CCAT_QDRANT_API_KEY="" # optional <api-key>
```

## Cat + Reverse proxy

### Cat with Caddy (automatic https)

This is your `compose.yml`

```yaml
services:

  cat:
    image: ghcr.io/cheshire-cat-ai/core:latest
    container_name: cheshire_cat_core
    env_file:
      - .env
    expose:
      - 80
    volumes:
      - ./cat/static:/app/cat/static
      - ./cat/plugins:/app/cat/plugins
      - ./cat/data:/app/cat/data

  caddy:
    image: caddy:latest
    depends_on:
      - cat
    ports:
      - 80:80
      - 443:443
      - 443:443/udp
    volumes:
      - ./caddy/Caddyfile:/etc/caddy/Caddyfile
      - ./caddy/data:/data
      - ./caddy/config:/config
    restart: unless-stopped
```

Add this enviroment variable in your `.env` file:

```bash
CCAT_HTTPS_PROXY_MODE=1
```

And in `caddy/Caddyfile`:
```
localhost {
    reverse_proxy cat:80
}
```

Now you can reach your cat at `https://localhost`!
