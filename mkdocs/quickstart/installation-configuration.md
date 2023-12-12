# &#128640; Installation and First configuration

## Requirements

To run the Cheshire Cat, you need to have `Docker` ([instructions](https://docs.docker.com/engine/install/)) and `docker compose` ([instructions](https://docs.docker.com/compose/install/)) already installed on your system.

The Cat is not a LLM, it uses a LLM.
Hence, when you run the Cat for the first time, you need to configure the LLM and the embedder.  
Most people use [ChatGPT](https://platform.openai.com/docs/models/gpt-3-5), it's quite cheap and powerful enough.
We will do the same during the next steps.

To use `ChatGPT`, you need an API key. You can request one on the provider's website: 
    - visit your OpenAI [API Keys](https://platform.openai.com/account/api-keys) page;  
    - create an API key with `+ Create new secret key` and copy it

## Setup

Create a folder on your machine, and inside it create a file named `compose.yml`.
Copy/paste the following inside:

```yaml
version: '3.7'

services:

  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:latest
    container_name: cheshire_cat_core
    ports:
      - ${CORE_PORT:-1865}:80
    environment:
      - PYTHONUNBUFFERED=1
      - WATCHFILES_FORCE_POLLING=true
    volumes:
      - ./static:/app/cat/static
      - ./plugins:/app/cat/plugins
      - ./data:/app/cat/data
```

## Starting the Cat
    
- Open a terminal inside the same folder and run:

```bash
docker compose up
```

The first time you run the `docker compose up` command,
it will take several minutes to build the Docker Cat image.

Once finished, the Cat will be living and running!

## First configuration of the LLM

- Open the Admin Portal in your browser at [`localhost:1865/admin`](http://localhost:1865/admin){:target="_blank"}
- Configure the LLM in the `Settings` tab and paste your API key ([video](../assets/vid/setup.mp4))


TODO: update the video  

## Next step
In the [next step](./play-with-the-cat.md), you will learn how to play with the Cat.