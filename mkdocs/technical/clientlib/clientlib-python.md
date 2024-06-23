# &#128640; Client Library Python

The Cheshire Cat provides a Python API client that allows you to chat with the Cat (using WebSocket) and provides APIs to interact with all the control plane endpoints.

The package is public released on the Python Package Index (PyPI) repository:  
[Cheshire Cat Python API client](https://pypi.org/project/cheshire_cat_api/){:target="_blank"}

## Setup

To add the client to your project, install it with pip:

```bash
pip install cheshire_cat_api
```

Then, you can import the base class like this: 

```python
import cheshire_cat_api as ccat
```

## Example connection

Here is an example
to establish a connection with the Cheshire Cat backend to interact both via WebSocket and the HTTP endpoints.

### Interact with the WebSocket endpoint

The WebSocket connection allows defining four callbacks to handle WebSocket events.

```python
def on_open():
    # This is triggered when the connection is opened
    print("Connection opened!")

def on_message(message: str):
    # This is triggered when a new message arrives 
    # and grabs the message
    print(message)

def on_error(exception: Exception):
    # This is triggered when a WebSocket error is raised
    print(str(exception))

def on_close(status_code: int, message: str):
    # This is triggered when the connection is closed
    print(f"Connection closed with code {status_code}: {message}")
```

!!! note

    The aforementioned callbacks are optional and intended for custom behaviors.
    The client already handles the events with default logging.

Now, you can connect to the backend:

```python
import time
import cheshire_cat_api as ccat

# Connection settings with default values
config = ccat.Config(
    base_url="localhost",
    port=1865,
    user_id="user",
    auth_key="",
    secure_connection=False
)

# Cat Client
cat_client = ccat.CatClient(
    config=config,
    on_open=on_open,
    on_close=on_close,
    on_message=on_message,
    on_error=on_error
)

# Connect to the WebSocket API
cat_client.connect_ws()

while not cat_client.is_ws_connected: 
# A better handling is strongly advised to avoid an infinite loop 
    time.sleep(1)
    
# Send the message
cat_client.send(message="Hello Cat!")

# Close connection
cat_client.close()
```

### Interact with the HTTP endpoints

Like in the WebSocket case, you should first connect to the Cat backend:

```python
import cheshire_cat_api as ccat

# Connection settings with default values
config = ccat.Config(
    base_url="localhost",
    port=1865,
    user_id="user",
    auth_key="",
    secure_connection=False
)

# Cat Client
cat_client = ccat.CatClient(
    config=config,
    on_open=on_open,
    on_close=on_close,
    on_message=on_message,
    on_error=on_error
)
```

Now, you can interact with the [available APIs]()

#### Plugin API - Retrieve plugins

```python
# Retrieve a list of the available plugins
plugins = cat_client.plugins.get_available_plugins()
```

#### RabbitHole API - Upload a URL

```python
from cheshire_cat_api.models.body_upload_url import BodyUploadUrl

# Please note that interacting with the RabbitHole to upload
# a URL requires structuring the body like this

body_upload_url = BodyUploadUrl(
    url="https://cheshire-cat-ai.github.io/docs/conceptual/cheshire_cat/rabbit_hole/"
)

# then you can make the request as follows
response = cat_client.rabbit_hole.upload_url(body_upload_url)
```

#### Memory API - wipe collections

```python
# Delete the episodic and declarative memories
response = cat_client.memory.wipe_collections()
```

### Available APIs

| API           | HTTP Method | Class Method     | Description |
|---------------|-------------|------------------|-------------|
| `settings`    | `GET`       | `get_settings()` |             |
|               | `POST`      |                  |             |
|               | `GET`       |                  |             |
|               | `PUT`       |                  |             |
|               | `DELETE`    |                  |             |
| `llm`         | `GET`       |                  |             |
|               | `GET`       |                  |             |
|               | `PUT`       |                  |             |
| `embedder`    | `GET`       |                  |             |
|               | `GET`       |                  |             |
|               | `PUT`       |                  |             |
| `plugins`     | `GET`       |                  |             |
|               | `POST`      |                  |             |
|               | `POST`      |                  |             |
|               | `PUT`       |                  |             |
|               | `GET`       |                  |             |
|               | `DELETE`    |                  |             |
|               | `GET`       |                  |             |
|               | `GET`       |                  |             |
|               | `PUT`       |                  |             |
| `memory`      | `GET`       |                  |             |
|               | `GET`       |                  |             |
|               | `DELETE`    |                  |             |
|               | `DELETE`    |                  |             |
|               | `DELETE`    |                  |             |
|               | `DELETE`    |                  |             |
|               | `GET`       |                  |             |
|               | `DELETE`    |                  |             |
| `rabbit_hole` | `POST`      |                  |             |
|               | `POST`      |                  |             |
|               | `POST`      |                  |             |
|               | `GET`       |                  |             |