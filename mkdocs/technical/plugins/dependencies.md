# Plugin dependencies

If your plugin requires additional python packages, add a `requirements.txt` file to your plugin.
The file should contain *only* additional dependencies.  

The Cat will install your dependencies on top of the default ones, as soon as you install a plugin from the admin.
If you are coding a plugin from inside the `cat/plugins` folder, to install dependencies you need to stop and restart the Cat.

## Example

Your plugin makes the Cat a crypto bro.  
You decide to use the `pycrypto` package, from the version 2.6.1 up.

Insert a `requirements.txt` file in your plugin root folder:

```txt
pycrypto>=2.6.1
```

Stop the terminal with `CTRL + C`, then

```bash
docker compose down
```

And to see dependencies installed,

```bash
docker compose up
```

To make changes permanent and avoid dependencies installation at every startup, stop the Cat and rebuild the docker image as explained in the [update instructions](../getting-started.md#update).
