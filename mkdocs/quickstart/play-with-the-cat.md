# Play with the Cat

## Chatting with the Cat: the Admin Portal playground

The Cat is an API-first framework, and it doesn't provide a ready-to-use UI for the end user.
It is your responsibility to implement this UI.
However, the Cat offers a playground that you can use to quickly test the AI you are implementing.

To access playground, go to the Admin Portal at `localhost:1865/admin`, and click on the `Home` tab.
This tab serves as the playground for chatting with the Cat.

Try to ask something about socks, e.g. "what do you know about socks?".
The Cat will give a generic answer.
Afterward, we will expand this general knowledge with more specific information.

![Alt text](../assets/img/quickstart/play-with-the-cat/play-with-the-cat.png)



## Chatting with the Cat: API interaction

The Cat is an API-first framework, you can chat with it using the WebSocket protocol.

First, set the API key by creating a file named `.env` in the same folder as the `compose.yml` file with the following content. Then, restart the Cat with `docker compose down` followed by `docker compose up`.
```
CCAT_API_KEY_WS=meow_secret
```

Here is an example of how to use it in Python:

```python
import asyncio
import json

from websockets.asyncio.client import connect


async def cat_chat():
    # Creating a websocket connection
    async with connect("ws://localhost:1865/ws?token=meow_secret") as websocket:

        # Taking user input and sending it through the websocket
        user_input = input("Human: ")
        await websocket.send(json.dumps({"text": user_input}))

        # Receiving and printing the cat's response
        async for message in websocket:
            cat_response = json.loads(message)

            if cat_response["type"] == "chat":
                print("Cheshire Cat:", cat_response["content"])
                break


# Running the function until completion
asyncio.run(cat_chat())
```

Run it and ask `what do you know about socks?` again, the output in the terminal should looks like:

```
❯ python main.py
Human: what do you know about socks?
Cheshire Cat: Socks, my dear, are like the hidden wonders of the wardrobe! They can be plain or patterned, warm or cool, and often seem to vanish into thin air. Do you have a favorite pair?
```

#### More Info

This example explains the **Raw** use of the Cat APIs, however there are convenient and ready-made libraries available for various languages! [`Production → Client Libraries`](../production/network/clients.md)

For more methods of authentication look at [`Production → Authentication`](../production/auth/authentication.md)

## Next Step
In the [next step](./upload-document.md), you will learn how to load information into the Cat by uploading documents.
