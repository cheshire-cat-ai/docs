# Authentication

The Cat by default comes without authentication except for the Admin panel which handles its own authentication using username and password, generating a JWT token and using it to communicate with Cheshire Cat APIs.

However, if you want to secure your communication with the Cat as well you can do it pretty easily.

## Securing HTTP

To enable authentication for HTTP endpoints you need to set the `CCAT_API_KEY` environment variable. This will lock the Cat HTTP endpoints and you will need to pass the value of the `CCAT_API_KEY` to authenticate your request.

Enabling the API key will also enable JWT authentication. For more details [JWT Authentication](#jwt-authentication).

## Securing WS

To enable authentication for WebSocket communication you need to set the `CCAT_API_KEY_WS` environment variable. This will lock the Cat WebSocket endpoint used for conversations. You'll need to pass the value of the `CCAT_API_KEY_WS` to ensure the Cat will open the connection.

Enabling the API key will also enable JWT authentication. If you are communicating via browser, you'll probably don't want to use an API key directly in the connection URL, indeed you'll want to use a [temporary token](#jwt-authentication).

## JWT Authentication

Once you've enabled the Cat API keys variable you can also use JSON Web Token to authenticate both HTTP and WebSocket requests. To generate a valid token you can make an HTTP POST request to `/auth/token` passing username and password in the payload.

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