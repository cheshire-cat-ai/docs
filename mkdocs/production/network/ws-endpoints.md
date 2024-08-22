

## Why WebSocket

While most network communication with LLMs is performed via HTTP, the Cat features full duplex communication using the WebSocket protocol, for the following reasons:

- two way communication:  
  you send messages to the Cat, and the Cat can send messages to you, even if you did not summon it (think about an alarm clock). This would not be possible via HTTP.
- multiprompt agent: each message to the Cat may involve the execution of multiple prompts and API calls done from plugins, making HTTP streaming risky of a timeout.
- token streaming: each token will have its own dedicated ws message.
- notifications: your client will receive ws notifications, e.g. when an upload is finished or when a plugin wants to send one.

If you are new to WebSocket, we suggest you use one of the community [client libraries](clients.md) that do most of the work for you.

## Example

TODO