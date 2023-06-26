
# :anatomical_heart: The Cat Core

The core functionalities of The Cheshire Cat resides in the `/core` folder. The core exposes all of its APIs via the address `localhost:1865/`.
The program has several endpoints that can be accessed via this address. All of these endpoints are thoroughly documented and can be easily tested using Swagger (available at `localhost:1865/docs`) or ReDoc (available at `localhost:1865/redoc`).

Some of these endpoints include:

| Endpoint           | Method      | Description                                                                         |
|--------------------|:------------|:------------------------------------------------------------------------------------|
| ___/___            | `GET`       | :handshake: Return the message `"We're all mad here, dear!"` if the cat is running. |
| ___/ws/___         | `WEBSOCKET` | :speech_balloon: Start a chat with the cat using websockets.                        |
| ___/rabbithole/___ | `POST`      | :rabbit: Send a file (`.txt`, `.md` or `.pdf`) to the cat.                          |

## :yarn: The Admin Interface

The frontend interface of The Cheshire Cat can be accessed via `localhost:1865/admin`. This interface provides users with an easy-to-use chat that act as playground and can be used to interact with your application. The Cat core uses a static build of the admin, source code can be found [here](https://github.com/cheshire-cat-ai/admin-vue).

All the cat's settings are available under this GUI's `Settings` menu.











