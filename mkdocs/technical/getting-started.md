# &#128640; Getting started

## Quickstart

To run the Cheshire Cat, you need to have `docker` ([instructions](https://docs.docker.com/engine/install/)) and `docker-compose` ([instructions](https://docs.docker.com/compose/install/)) installed on your system.

### Setup

- Clone the repository on your machine

```bash
git clone https://github.com/cheshire-cat-ai/core.git cheshire-cat
```

- Enter the created folder

```bash
cd cheshire-cat
```
    
- Run docker containers

```bash
docker-compose up
```

The first time you run the `docker-compose up` command it will take several minutes as docker images occupy some GBs.  
Meet the Cat at `localhost:1865/admin` in your browser :)

### Next steps

- Create and API key on the language model provider website, most people use [chatGPT](https://platform.openai.com/docs/models/gpt-3-5):
    - visit your OpenAI [personal account](https://platform.openai.com/account/api-keys)
    - create an API key with `+ Create new secret key` and copy it
- Go back to the Cat in your browser at `localhost:1865/admin`
    - Configure a LLM in the `Settings` tab and paste your API key (as shown in the video below)
    - Start chatting!
- You can also interact via REST API and try out the endpoints on `localhost:1865/docs`


### Visual configuration

![type:video](../assets/vid/setup.mp4)

When you're done using the Cat, stop the terminal by clicking on it and press `CTRL + c`.  Then launch the command:

```bash
docker-compose down
```

## Update

As the project is still a work in progress, if you want to update it run the following:

- Enter the folder where you cloned the repository

```bash
cd cheshire-cat
```

- Pull updates from the GitHub repository

```bash
git pull
```

-  Build again the docker containers

```bash
docker-compose build --no-cache
```

-  Remove dangling images (optional)

```bash
docker rmi -f $(docker images -f "dangling=true" -q)
```

- Run docker containers

```bash
docker-compose up
```
