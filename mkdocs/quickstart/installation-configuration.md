# &#128640; Installation and First configuration

## Prerequisites

To run the Cheshire Cat, you need to have `Docker` ([instructions](https://docs.docker.com/engine/install/)) and `docker-compose` ([instructions](https://docs.docker.com/compose/install/)) already installed on your system.

The Cat is not a LLM, it uses a LLM. So when you run the Cat for the first time, you need to configure the LLM and the encoder you choose to use.  
Most people use [ChatGPT](https://platform.openai.com/docs/models/gpt-3-5), it's quite cheap and enough powerful, we will use `ChatGPT` during the next steps.

You need an API key for use `ChatGPT`, you can request an API key on the provider's website:  
    - visit your OpenAI [API Keys](https://platform.openai.com/account/api-keys) page  
    - create an API key with `+ Create new secret key` and copy it

TODO: _(fare riferimento al link con il pricing?)_

## Setup

- Clone the repository on your machine

```bash
git clone https://github.com/cheshire-cat-ai/core.git cheshire-cat
```

## Starting the Cat
- Enter the created folder

```bash
cd cheshire-cat
```
    
- Run docker containers

```bash
docker-compose up
```

The first time you run the `docker-compose up` command it will take several minutes as the Docker Cat image will be build.

When finished the Cat will be live and running!

## First configuration of the LLM

- Open the Admin Portal in your browser at [`localhost:1865/admin`](http://localhost:1865/admin){:target="_blank"}
- Configure the LLM in the `Settings` tab and paste your API key ([video](../assets/vid/setup.mp4))


TODO: update the video  
TODO: configure both, LLM and encoder?

## Next step
In the next step you will learn how to play with the Cat