# Contributing

Thank you for considering code contribution.
If you wanto to learn how the Cat works and join its development, there is a different installation process to follow.

## Development setup

- Clone the repository on your machine

```bash
git clone https://github.com/cheshire-cat-ai/core.git cheshire-cat
```

- Enter the created folder

```bash
cd cheshire-cat
```
    
- Run docker container

```bash
docker compose up
```

The first time you run the `docker compose up` command,
it will take several minutes to build the Docker Cat image. Once finished, the Cat will be living and running!  

To stop the Cat hit CTRL-C in the terminal, you should see the logs stopping. Then run:

```bash
docker compose down
```

## Update development setup

Remember to update often both your fork and your local clone.  
Before each session, follow these steps:

- Enter the folder where you cloned the repository

```bash
cd cheshire-cat
```

- Pull updates from the GitHub repository

```bash
git pull
```

-  Build again the docker container

```bash
docker compose build --no-cache
```

-  Remove dangling images (optional)

```bash
docker rmi -f $(docker images -f "dangling=true" -q)
```

- Run docker containers

```bash
docker compose up
```

## Your First Code Contribution

1. Checkout the `develop` branch (`git checkout -b develop` and then `git pull origin develop`)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request against the `develop` branch (if it contains lots of code, please discuss it beforehand opening a issue)

## Important notes

- try to discuss your contribution beforehand in an issue, to make an actually useful PR
- try to keep your PR small, single feature / fix and to the point
- branch out from `develop` and make your PR against `develop`; branch `main` is only used for releases

## Improving The Documentation

Docs contribution are highly valuable for the project.
See details on how to help with the docs [here](https://github.com/cheshire-cat-ai/docs/).

