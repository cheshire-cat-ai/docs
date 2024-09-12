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
Here is an example of how to do it in Javascript and Python:

=== "JavaScript"
    ```javascript
    let ws = new WebSocket("ws://localhost:1865/ws")

    let humanTurn = function(){
        let msg = prompt("Human message:")
        if(msg) {
            ws.send(JSON.stringify({"text": msg}))
        }
    }

    ws.onopen = function(){
        humanTurn()
    }

    ws.onmessage = function(msg){
        let msg_parsed = JSON.parse(msg.data)
        console.log(msg_parsed.content)
        if(msg_parsed.type == "chat") {
            humanTurn()   
        }
    }
    ```
=== "Python"
    ```python
    import json
    import asyncio
    from websockets.asyncio.client import connect

    async def cat_chat():
        # Creating a websocket connection
        async with connect("ws://localhost:1865/ws") as websocket:
            while True:
                # Taking user input and sending it through the websocket
                user_input = input("Human: ")
                await websocket.send(json.dumps({"text": user_input}))

                # Receiving and printing the cat's response
                async for message in websocket:
                    cat_response = json.loads(message)
                    print(cat_response["content"])

                    # Human turn!
                    if cat_response["type"] == "chat":
                        break

    # To stop the script: CTRL + c
    asyncio.run(cat_chat())
    ```

Run it and ask `what do you know about socks?` again, the output in the terminal should look like:

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
