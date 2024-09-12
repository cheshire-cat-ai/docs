# Authentication

All the Cat endpoints are wide open by default, and so anyone can authenticate and administer the installation. Before going to production, follow the steps below to secure communication. We will provide Javascript and Python examples to test each step and show you how to authenticate from external clients.

**TL;DR**: to secure your Cat add the following to your `.env`:

```bash
CCAT_API_KEY=a-very-long-and-alphanumeric-secret
CCAT_API_KEY_WS=another-very-long-and-alphanumeric-secret
CCAT_JWT_SECRET=yet-another-very-long-and-alphanumeric-secret
```

Make sure docker is loading your `.env` file containing these environment variables. See [here](../administrators/env-variables.md).

## 1. Securing API keys

Two environment variables allow you to secure Cat's endpoints and require authentication for each request:

 - `CCAT_API_KEY`: locks down HTTP endpoints
 - `CCAT_API_KEY_WS`: locks down WebSocket endpoints

!!! warning
    Even if you set both `CCAT_API_KEY` and `CCAT_API_KEY_WS`, an intruder can still hack you by self signing a JWT.  
    See below [how to secure JWT](#2-securing-jwt).

### HTTP key

On a fresh installation, the Cat is talking to strangers:

=== "JavaScript"
    ```javascript
    let response = await fetch("http://localhost:1865")
    let json = await response.json()

    console.log(response.status, json)
    ```
=== "Python"
    ```python
    import requests

    response = requests.get("http://localhost:1865")

    print(response.status_code, response.json())
    ```

Output will be:
```json
200 {"status": "We're all mad here, dear!", "version": "x.y.z"}
```

To secure HTTP endpoints, set the `CCAT_API_KEY` environment variable. This will restrict access requiring the value of `CCAT_API_KEY` to authenticate requests.

Example `.env`:
```bash
CCAT_API_KEY=meow
```

If we try the same client code as above, we obtain:
```json
403 {"detail": {"error": "Invalid Credentials"}}
```

To pass the gate, we need to set an header in the format `Authorization: Bearer <CCAT_API_KEY>`.  
We can optionally set a `user_id` header to tell the Cat which specific user is making the request, otherwise `user_id: user` will be assumed.

=== "JavaScript"
    ```javascript hl_lines="3-8"
    let response = await fetch(
        "http://localhost:1865",
        {
            "headers": {
                "Authorization": "Bearer meow",
                "user_id": "Caterpillar" // optional
            }
        }
    )
    let json = await response.json()

    console.log(response.status, json)
    ```
=== "Python"
    ```python hl_lines="5-8"
    import requests

    response = requests.get(
        "http://localhost:1865",
        headers = {
            "Authorization": "Bearer meow",
            "user_id": "Caterpillar" # optional
        }
    )
    
    print(response.status_code, response.json())
    ```

The Cat is open again, but only to real friends.

### WebSocket key

To secure WebSocket communication, set the `CCAT_API_KEY_WS` environment variable. This will lock down the Cat’s WebSocket endpoints used for conversations. You'll need to provide the `CCAT_API_KEY_WS` value to establish a connection.

On a fresh installation we can chat to the Cat like this:

=== "JavaScript"
    ```javascript
    let ws = new WebSocket("ws://localhost:1865/ws")

    ws.onopen = function() {
        ws.send(JSON.stringify({"text": "It's late"}))
    }

    ws.onmessage = function(msg){
        console.log(JSON.parse(msg.data))
    }
    ```
=== "Python"
    ```python
    import json
    import asyncio
    from websockets.asyncio.client import connect

    async def cat_chat():
        async with connect(f"ws://localhost:1865/ws") as websocket:
            
            await websocket.send(json.dumps({"text": "It's late"}))

            async for message in websocket:
                cat_response = json.loads(message)
                print(cat_response["content"])
                if cat_response["type"] == "chat":
                    break

    asyncio.run(cat_chat())
    ```

You will see a stream of tokens and the final message.  
Now set `CCAT_API_KEY_WS` in our `.env`:

```bash
CCAT_API_KEY_WS=meow_ws
```
Running the code above will result in a `403` status code and refused connection, just as we wanted.

To communicate again with the Cat using the WebSocket key, we just add a `token` query parameter to the connection URL: `ws://localhost:1865/ws?token=<CCAT_API_KEY_WS>`.

=== "JavaScript"
    ```javascript
    let ws = new WebSocket("ws://localhost:1865/ws?token=meow_ws")

    ws.onopen = function() {
        ws.send(JSON.stringify({"text": "It's late"}))
    }

    ws.onmessage = function(msg){
        console.log(JSON.parse(msg.data))
    }
    ```
=== "Python"
    ```python
    import json
    import asyncio
    from websockets.asyncio.client import connect

    async def cat_chat():
        async with connect(f"ws://localhost:1865/ws?token=meow_ws") as websocket:
            
            await websocket.send(json.dumps({"text": "It's late"}))

            async for message in websocket:
                cat_response = json.loads(message)
                print(cat_response["content"])
                if cat_response["type"] == "chat":
                    break

    asyncio.run(cat_chat())
    ```

In the case of WebSocket, to indicate the `user_id` we can insert it into the address.  
For example if our user id is `Caterpillar`, we connect to `ws://localhost:1865/ws/Caterpillar?token=meow_ws`


## 2. Securing JWT

Even if we lock down HTTP and WebSocket endpoints with API keys, there is another access channel in the Cat we need to secure that is independent from the ones described above.

[JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) (JWT) authentication works for both HTTP and WebSocket endpoints, and it's recommended especially when using the Cat via browser:

 - JWTs have a temporary lifespan, afterwards a new token must be generated. If somebody steals it from the browser, it can only be used for a short time.
 - JWTs can contain additional information, in our case user id and [permissions](./authorization.md). No need to specify user id in the headers or in the address.
 - We can reserve `CCAT_API_KEY` and `CCAT_API_KEY_WS` only for machine-to-machine communication.

JWTs are secured by the environment variable `CCAT_JWT_SECRET`, which is used to generate and validate tokens.
On a fresh installation, JWTs are already enabled with `CCAT_JWT_SECRET=secret`. This value **must** be changed.


To complete our security setup, our `.env` should contain three secrets: 

```bash
CCAT_API_KEY=meow
CCAT_API_KEY_WS=meow_ws
CCAT_JWT_SECRET=meow_jwt
```

!!! note "Admin Panel already uses JWT"
    The Admin panel handles authentication asking username and password, then asks the core to generate a JWT and then uses it to communicate with Cheshire Cat APIs. Choose a strong admin password and set a custom `CCAT_JWT_SECRET` if you expose the admin panel to the public.

### Obtaining a JWT

To generate a valid token make an HTTP POST request to `/auth/token`, including your username and password in the payload.

=== "JavaScript"
    ```javascript
    let response = await fetch(
        "http://localhost:1865/auth/token",
        {
            "method": "POST",
            "headers": {
                "Content-type": "application/json",
            },
            "body": JSON.stringify({
                "username": "admin",
                "password": "admin"
            })
        }
    )
    let json = await response.json()
    let jwt = json["access_token"]

    console.log(jwt)
    ```
=== "Python"
    ```python
    import requests

    response = requests.post(
        "http://localhost:1865/auth/token",
        json = {
            "username": "admin",
            "password": "admin"
        }
    )

    # Here's your JWT
    jwt = response.json()["access_token"]
    print(jwt)
    ```

As you can see having an [internal user](./user-management.md#internal-users) in the Cat with specific username and password is a prerequisite to obtain a JWT.
The same is not true for API key authentication, in which user can be created on the fly (see [shadow users](./user-management.md#shadow-users)).

You can make JWT work also for [external users](./user-management.md) (e.g via identity provider or CMS) implementing a custom [`AuthHandler`](./custom-auth.md)

### Using JWT for HTTP

Once you get the JWT token you can easily append it to your HTTP requests, like so:

=== "JavaScript"
    ```javascript
    response = await fetch(
        "http://localhost:1865",
        {
            "headers": {
                "Authorization": `Bearer ${jwt}`
            }
        }
    )
    json = await response.json()

    console.log(json)
    ```
=== "Python"
    ```python
    response = requests.get(
        "http://localhost:1865",
        headers={
            "Authorization": f"Bearer {jwt}"
        }
    )

    print(response.json())
    ```

### Using JWT for WebSocket

Same goes to authenticate WebSocket:

=== "JavaScript"
    ```javascript
    let url = `ws://localhost:1865/ws?token=${jwt}`
    let ws = new WebSocket(url)

    ws.onopen = function() {
        ws.send(JSON.stringify({"text": "It's late"}))
    }

    ws.onmessage = function(msg){
        console.log(JSON.parse(msg.data))
    }
    ```
=== "Python"
    ```python
    import json
    import asyncio
    from websockets.asyncio.client import connect

    async def cat_chat():
        url = f"ws://localhost:1865/ws?token={jwt}"
        async with connect(url) as websocket:

            await websocket.send(json.dumps({"text": "It's late"}))

            async for message in websocket:
                cat_response = json.loads(message)
                print(cat_response["content"])
                if cat_response["type"] == "chat":
                    break

    asyncio.run(cat_chat())
    ```

### Refresh JWT

TODO


## 3. Use Secure Protocols

The final step is to have the Cat behind a reverse proxy, hopefully with automatic TLS certificates.

There are many open source reverse proxies available, most of them automatically manage certificates via [Let's Encrypt](https://letsencrypt.org/){:target="_blank"}.
A few example setups are available [here](../administrators/docker-compose.md#cat-reverse-proxy).
