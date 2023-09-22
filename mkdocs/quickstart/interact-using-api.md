# Interact using API

The Cat is an API-first framework, you can chat with it using the WebSocket protocol.

## Example of code
Here is an example of how to use it:

```python
import asyncio
import websockets
import json


async def cat_chat():
    # Creating a websocket connection
    async with websockets.connect("ws://localhost:1865/ws") as websocket:
        # Taking user input and sending it through the websocket
        user_input = input("Human: ")
        await websocket.send(json.dumps({"text": user_input}))

        # Receiving and printing the cat's response
        cat_response = json.loads(await websocket.recv())

        print("Cheshire Cat:", json.dumps(cat_response, indent=4))


# Running the function until completion
asyncio.get_event_loop().run_until_complete(cat_chat())
```

## Chatting with the Cat in the console
Run it and ask "what do you know about socks?" again, the output in the terminal should looks like:

```bash
❯ python3 test.py
Human: what do you know about socks?
Cheshire Cat: {
    "error": false,
    "type": "chat",
    "content": "Ah, socks! They're quite fascinating little things, aren't they? Well, let me tell you what I know about socks. They come in all shapes, sizes, and colors, and they're usually worn on the feet to keep them warm and cozy. Some people like their socks plain and simple, while others prefer them with funky patterns or cute designs. Socks can be made from different materials like cotton, wool, or even synthetic fibers. They can also have different lengths, from ankle socks to knee-highs. And let's not forget about those toe socks that give each little piggy its own little cozy home! So, there you have it, a little glimpse into the world of socks. Is there anything specific you'd like to know about them?",
    "why": {
        "input": "what do you know about socks?",
        "intermediate_steps": null,
        "memory": {
            "episodic": [],
            "declarative": [],
            "procedural": []
        }
    }
}
```

## Client Libraries
This example explains the low-level use of the Cat APIs. However, there are more convenient and ready-made libraries available for various languages. Take a look at the `Developers -> Client Libraries` section.


## Next Step
In the next step you will learn how load a text document in the documents memory.