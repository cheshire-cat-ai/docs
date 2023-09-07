# &#128640; Installation and First configuration

## Prerequisites

To run the Cheshire Cat, you need to have `docker` ([instructions](https://docs.docker.com/engine/install/)) and `docker-compose` ([instructions](https://docs.docker.com/compose/install/)) already installed on your system.

The Cat is not a LLM, it uses a LLM. So when you run the Cat for the first time, you need to configure the LLM and the encoder you choose to use.  
You need an API key for the chosen LLM, most people use [chatGPT](https://platform.openai.com/docs/models/gpt-3-5), you can request an API key on the provider's website (fare riferimento a possibili costi?):  
    - visit your OpenAI [personal account](https://platform.openai.com/account/api-keys)  
    - create an API key with `+ Create new secret key` and copy it

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

The first time you run the `docker-compose up` command it will take several minutes as docker images occupy some GBs.  

When finished the Cat will be live and running!

## First configuration of the LLM

- Open the Cat admin portal in your browser at `localhost:1865/admin`
- Configure a LLM in the `Settings` tab and paste your API key ([video](../assets/vid/setup.mp4))

## Stopping the Cat

When you're done using the Cat, stop the terminal by clicking on it and press `CTRL + c`.  Then launch the command:

```bash
docker-compose down
```