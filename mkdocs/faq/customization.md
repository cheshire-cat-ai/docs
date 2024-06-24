# Customization

#### I want to build my own plugin for the Cat: what should I know about licensing?

Plugins are any license you wish, you can also sell them.
The Cat core is GPL3, meaning you are free to fork and go on your own, but you are forced to open source changes to the core.

#### Port 1865 is not allowed by my operating system and/or firewall

Change the port as you wish in the `.env` file.

```text
# Decide host and port for your Cat. Default will be localhost:1865
CORE_HOST=localhost
CORE_PORT=9000
```

#### Can I use a different vector database than Qdrant?
At the moment, we don't provide any way to switch the vector database 😿 but it is planned for the future.