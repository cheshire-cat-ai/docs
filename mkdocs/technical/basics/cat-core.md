
# &#129728; API Endpoints

The core exposes all of its APIs via the address `localhost:1865/`.
The program has several endpoints that can be accessed via this address. All of these endpoints are thoroughly documented and can be easily tested using Swagger (available at `localhost:1865/docs`) or ReDoc (available at `localhost:1865/redoc`).

Some of these endpoints include:

| Endpoint           | Method      | Description                                                                         |
|--------------------|:------------|:------------------------------------------------------------------------------------|
| ___/___            | `GET`       | &#129309; Return the message `"We're all mad here, dear!"` if the cat is running. |
| ___/ws/___         | `WEBSOCKET` | &#128172; Start a chat with the cat using websockets.                        |
| ___/rabbithole/___ | `POST`      | &#128007; Send a file (`.txt`, `.md` or `.pdf`) to the cat.                          |
