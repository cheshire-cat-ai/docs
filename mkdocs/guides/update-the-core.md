# &#128640; Update the Cat Core

If you want to update it run the following:

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
