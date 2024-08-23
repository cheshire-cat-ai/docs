
## Backups

To perform a full backup, just save your folder containing the `compose.yml` file and all the volumes (`data`, `plugins` and `static`). Cat's code and runtime is fully encapsulated in the docker image, no need to copy it anywhere.

Same goes for the vector memory:

- if you are not using the Qdrant container, all the collections are saved in `cat/data/local_vector_memory`, which pertains the case described above.
- if you are using the Qdrant container, and you defined volumes for it, just save the volumes' contents.

You can easily setup an automated backup system using tools like [rsync](https://linux.die.net/man/1/rsync) and a simple [cron](https://linux.die.net/man/8/cron).

## Backup restoration

You should be able to restore a full backed up installation simply putting the folder you saved, containing `compose.yml` and volumes, anywhere on a docker enabled system. Then run:

```bash
cd <folder>
docker compose pull
docker compose up -d
```

## Updates

We are trying to respect [semantic versioning](https://semver.org/), but the project is really young and there may be some retrocompatibility hiccups. We are sorry for any inconvenience.

If you have version `x.y.z` you should be able to update your Cat to any `x.*.*` version by just changing container tag in the `compose.yml` file.

Example:

```yaml
  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:1.6.3
```

Becomes:

```yaml
  cheshire-cat-core:
    image: ghcr.io/cheshire-cat-ai/core:1.7.1
```

Then you pull the new image and you are good to go.

```bash
# enter the installation folder
cd <folder>

# stop the cat
docker compose down

# change the tag in `compose.yml`

# update image
docker compose pull

# start the cat
docker compose up -d
```