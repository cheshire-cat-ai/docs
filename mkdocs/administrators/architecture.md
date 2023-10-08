# Architecture

The Cheshire Cat framework consists of four components: the Core, the Vector Database, the LLM and the Admin Portal.

The Core and the Admin Portal are implemented within the framework, while the Vector Database and the LLM are external dependencies. 

The Core communicates with both the Vector Database and the LLM, while The Admin Portal communicates with the Core.

The Core is implemented in Python, Qdrant is utilized as Vector Database, the Core support different LLMs (see the [complete list](#compatible-llms) below), the Admin Portal is implemented using the Vue framework.

## Docker Compose Images
To facilitate, speed up, and standardize the Cat's user experience, the Cat  contains configuration for use inside Docker.

When executing `docker compose build` two Docker images are generated. The first one contains the Cat Core and Admin Portal, while the second one contains the Vector Database. The container name of the core is `cheshire_cat_core` and the name of the Vector Database image is `cheshire_vector_memory`.

The local Cat core path `./core` is mounted to the image `cheshire_cat_core`, by default changes to files in this folder force a restart of the Core, this behavior can be disable using the [`DEBUG`](env-variables.md/#debug) environment variables.

As default the Admin Portal connect to the core using `localhost` and port `1678`, these values can be customized using [environment variables](env-variables.md#core_host). This port is the only one exposed by the `cheshire_cat_core` image.

## Logging
All the log messages are printed on the standard output and log level can be configured with [`LOG_LEVEL`](env-variables.md#log_level) environment variables.

## Configuration
Some options of the Core can be customized using [environment variables](env-variables.md).

## Compatible LLMs
TODO