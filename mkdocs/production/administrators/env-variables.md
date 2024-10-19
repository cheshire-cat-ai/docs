# Environment Variables

The Core can be configured using environment variables, the values are read during Cat bootstrap.

## How to set Environment Variables

To set environment variables:

 - Create a file named `.env` at the same level of the `compose.yml` file.
 - [Here](https://github.com/cheshire-cat-ai/core/blob/main/.env.example){:target="_blank"} there is a example you can use as a reference.
 - Add to `compose.yml` the command to read the `.env`:

    ```yml hl_lines="5 6"
    services:
      cheshire-cat-core:
      image: ghcr.io/cheshire-cat-ai/core:latest
      container_name: cheshire_cat_core
      env_file:
        - .env
      ports:
        - ${CORE_PORT:-1865}:80
      volumes:
        - ./static:/app/cat/static
        - ./plugins:/app/cat/plugins
        - ./data:/app/cat/data
    ```

 - The command `docker compose up` will now read the `.env` file and set the environment variables for the container.


## Network

### CCAT_CORE_HOST
Default value: `localhost`

The host at which the Cat is running. The variable is used by Admin Portal to determine the host to connect to.  
If your installation has to be served on mywebsite.com, have in your `.env`: `CCAT_CORE_HOST=mywebsite.com`

### CCAT_CORE_PORT
Default value: `1865`

The port the Cat has to listen to, for both admin and REST API.  
Easter egg: `1865` is the year "Alice in Wonderland" was published.

### CCAT_CORE_USE_SECURE_PROTOCOLS
Default value: `false`

By default, the core APIs are exposed using the HTTP/WS protocol, set this parameter to `true` if you expose the API using the HTTPS/WSS protocol, for example using NGIX in front of the Cat.

### CCAT_CORS_ALLOWED_ORIGINS
Default value: `*`

By default, the core APIs can be consumed from all origins, using the parameter you can restrict which origins can consume the APIs.

### CCAT_HTTPS_PROXY_MODE
Default value: `false`

Enable this variable if you are using a proxy like Nginx with SSL in front of the Cat, otherwise https will give redirection problems.

This option is mapped to the `--proxy_headers` Uvicorn option, you can reference the [Uvicorn HTTP setting](https://www.uvicorn.org/settings/#http){:target="_blank"} page for more info.

### CCAT_CORS_FORWARDED_ALLOW_IPS
Default value: `*`

When the `CCAT_HTTPS_PROXY_MODE` option is enabled, this option is mapped to the `--forwarded-allow-ips` Uvicorn option, you can reference the [Uvicorn HTTP setting](https://www.uvicorn.org/settings/#http){:target="_blank"} page for more info.

## Security

### CCAT_API_KEY
Default value: `[empty]`

By default, the core HTTP API does not require any authorization. If you set this variable all HTTP endpoints will require an `Authorization: Bearer <ccat_api_key>` header.  
Failure to provide the correct key will result in a 403 error.  
Websocket endpoints will remain open, unless you set `CCAT_API_KEY_WS` (see below).

If along the HTTP API call you want to communicate the endpoint also which user is making the request, use the `user_id: <my_user_id>` header.  
If you don't, the Cat will assume `user_id: user`.

Keep in mind that api keys are intended for machine-2-machine communication; If you are talking to the Cat from a browser, set the api keys to secure your installation, but only communicate with the Cat via JWT (TODO: insert JWT tutorial).

### CCAT_API_KEY_WS
Default value: `[empty]`

By default, WebSocket endpoints are open to the public.
If you want to lock them down, set this environment variable, e.g. `CCAT_API_KEY_WS=meows`.

To pass the gate, call the WS endpoint using a `token` query parameter:  
Example `ws://localhost:1865/ws/<user_id>?token=<ccat_api_key_ws>`.

Keep in mind that api keys are intended for machine-2-machine communication; If you are talking to the Cat from a browser, set the api keys to secure your installation, but only communicate with the Cat via JWT (TODO: insert JWT tutorial).


### CCAT_JWT_SECRET
Default value: `secret`

Secret for issueing and validating JWTs. Must be personalized along `CCAT_API_KEY` and `CCAT_APIKEY_WS` to make the installation secure.

### CCAT_JWT_ALGORITHM
Default value: `HS256`

Algorithm to sign the JWT with `CCAT_JWT_SECRET`.

### CCAT_JWT_EXPIRE_MINUTES
Default value: `1440` 

By default a JWT expires after 1 day.




## Debug

### CCAT_DEBUG
Default value: `true`

By default changes to files in the root folder of the Cat force a restart of the Core.  
This is useful during the development of Plugins. This behavior can be switched off in production by setting to `false`.

### CCAT_LOG_LEVEL
Default value: `INFO`

The log level, available levels are:  
- `DEBUG`  
- `INFO`  
- `WARNING`  
- `ERROR`  
- `CRITICAL`  

## Vector DB

### CCAT_QDRANT_HOST
Default value: `[empty]`

The host on which Qdrant is running. Cat provides a ready-to-use file based Qdrant, embedded in `cat/data/local_vector_memory`. If you want to use an external instance of Qdrant or a separated container in `compose.yml`, use this parameter to specify the host where it is running. You can also optionally specify the protocol to use in the URL to make a secure connection (for example `https://example.com`).

See the [`local-cat`](https://github.com/cheshire-cat-ai/local-cat) repo for an example usage of Qdrant as a container.

### CCAT_QDRANT_PORT
Default value: `6333`

The port on which Qdrant is running, in case you use an external host or another container inside the `compose.yml`.

### CCAT_QDRANT_API_KEY
Default value: `[empty]`

This is used to set the Qdrant Api Key in the client connection statement. It should be configured if an Api Key is set up on the Qdrant Server, or if you are using the cloud version.

### CCAT_SAVE_MEMORY_SNAPSHOTS
Default value: `false`

Set to `ftrue` to turn on Vector Database snapshots, so when you change embedder an automatic backup will be saved on disk. Please note:

 - Snapshots are painfully slow.
 - We have not implemented a routine to reimport the snapshot.


## Others

### CCAT_METADATA_FILE
Default value: `cat/data/metadata.json`

The name of the file that contains all the Cat settings.

