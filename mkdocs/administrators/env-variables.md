# Environment Variables
The Core can be configured using environment variables, the values are read during Cat bootstrap.

To set an environment variable, create a file with name `.env` at the same level of the `docker-compose.yml` file. The command `docker compose up` reads the `.env` file and sets the environment variable.

The root folder contains the `.env.example`, you can use this file as a reference.

### CORE_HOST
The host at which the Cat is running. The parameter is used by Admin Portal to determine the host to connect to.

Default value: `localhost`

### CORE_PORT
The port the Cat has to use. The parameter is used by Admin Portal to determine the port to connect to.

Default value: `1865`

### CORE_USE_SECURE_PROTOCOLS
By default, the core APIs are exposed using the HTTP/WS protocol, set this parameter to `true` if you expose the API using the HTTPS/WSS protocol, for example using NGIX in front of the Cat. The parameter is read by the Admin Portal to determine the protocol to use.

Default value: `false`

### QDRANT_HOST
The host on which Qdrant is running. Cat provides a ready-to-use Docker image for Qdrant. If you want to use an external instance of Qdrant, use this parameter to specify the host where it is running.

Default value: `localhost`

### QDRANT_PORT
The port on which Qdrant is running. Cat provides a ready-to-use Docker image for Qdrant. If you want to use an external instance of Qdrant, use this parameter to specify the port where it is running.

Default value: `6333`

### API_KEY
By default, the core APIs don't require any authorization, if you set this parameter all endpoints will require an `access_token` header for authentication such as `access_token: your-key-here`. Failure to provide the correct access token will result in a 403 error.

Multiple keys can be accepted by separating them with a pipe (`|`) as follows: `API_KEY=your-key-here|secondary_client_key`.

Default value: `[empty]`

### CORS_ALLOWED_ORIGINS
By default, the core APIs can be consumed from all origins, using the parameter you can specify which origins can consume the APIs.

Default value: `*`

### LOG_LEVEL
The log level, available levels are:  
- `DEBUG`  
- `INFO`  
- `WARNING`  
- `ERROR`  
- `CRITICAL`  

Default value: `WARNING`

### METADATA_FILE
The name of the file that contains all the Cat settings.

Default value: `metadata.json`

### SAVE_MEMORY_SNAPSHOTS
Set to `false` to turn off Vector Database snapshot.

Default value: `true`

### DEBUG
By default, changes to files in the root folder of the Cat force a restart of the Core, this useful during the development of Plugins. This behavior can be switch off by setting this parameter to `false`.

Default value: `true`