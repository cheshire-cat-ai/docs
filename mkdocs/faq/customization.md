# Customization

#### I want to build my own plugin for the Cat: what should I know about licensing?

You can set set any licence you want and you are not limited to selling your plugin.  
The Cat core is GPL3, meaning you are free to fork and go on your own, but you are forced to open source changes to the core.

#### Port 1865 is not allowed by my operating system and/or firewall

Change the port as you wish in the `.env` file.

```text
# Set HOST and PORT for your Cat. Default will be localhost:1865  
CORE_HOST=localhost
CORE_PORT=9000
```

#### Can I use a different vector database than Qdrant?

At this moment we don't provide any way to switch the vector database 😿 but it is planned for the future.
