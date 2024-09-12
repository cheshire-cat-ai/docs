# Authentication

The Cat by default comes without authentication except for the Admin panel which handles its own authentication using username and password, generating a JWT token and using it to communicate with Cheshire Cat APIs.

However, if you want to secure your communication with the Cat as well you can do it pretty easily.

## Securing HTTP

To secure HTTP endpoints, set the `CCAT_API_KEY` environment variable. This will restrict access to the Cat's HTTP endpoints, requiring the value of `CCAT_API_KEY` to authenticate requests.

Enabling the API key also activates JWT authentication. For more information, see [JWT Authentication](#jwt-authentication).

## Securing WS

To secure WebSocket communication, set the `CCAT_API_KEY_WS` environment variable. This will lock down the Cat’s WebSocket endpoints used for conversations. You'll need to provide the `CCAT_API_KEY_WS` value to establish a connection.

Activating the API key also enables JWT authentication. If you're communicating via a browser, it’s recommended to use a [temporary token](#jwt-authentication) instead of including the API key directly in the connection URL.

## JWT Authentication

Once the Cat API key variables are enabled, you can also use JSON Web Tokens (JWT) to authenticate both HTTP and WebSocket requests. To generate a valid token, make an HTTP POST request to `/auth/token`, including your username and password in the payload.

```python

import requests

url = "http://localhost:1865/auth/token"

payload = {
    "username": "user",
    "password": "user"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

# Here's your JWT
jwt = response.json()["access_token"]

```

Once you get the JWT token you can easily append it to your HTTP or WS requests, like so:

```python

# HTTP Request

url = "http://localhost:1865/settings/"

headers = {"Authorization": f"Bearer {jwt}"}

response = requests.get(url, headers=headers)

print(response.json())
```

```python

# WebSocket Connection

async with websockets.connect(f"ws://localhost:1865/ws/user?token={jwt}") as websocket:
    await websocket.send(json.dumps(
        {
            "text": "Hola, I'm authenticated!",
            "user_id": "user"
        }
    ))
```