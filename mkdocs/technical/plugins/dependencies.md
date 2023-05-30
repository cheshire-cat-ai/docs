# Plugin dependencies

If your plugin requires additional python packages, add a `requirements.txt` file to your plugin.
The file should contain *only* additional dependencies.  

The Cat will install your dependencies on top of the default ones, as soon as you rebuild the docker image.

## Example

Your plugin makes the Cat a crypto bro.  
You decide to use the `pycrypto` package, from the version 2.6.1 up.

Insert a `requirements.txt` file in your plugin root folder:

```
pycrypto>=2.6.1
```

To make changes effective, stop the Cat and run the [update instructions](../getting-started.md#update).