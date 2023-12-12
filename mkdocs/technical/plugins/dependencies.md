# Plugin dependencies

If your plugin requires additional python packages, add a `requirements.txt` file to your plugin.

  - The file should contain *only* additional dependencies.  
  - Express minimal dependencies, to avoid regression problems (i.e. use `langchain>=x.x.x` instead of `langchain==x.x.x`)
  - The Cat will install your dependencies on top of the default ones, as soon as you install a plugin from the admin.
  - If you are coding a plugin from inside the `cat/plugins` folder, to install dependencies you need to stop and restart the Cat.

## Example

Your plugin makes the Cat a crypto bro.  
You decide to use the `pycrypto` package, from the version 2.6.1 up.

Insert a `requirements.txt` file in your plugin root folder:

```txt
pycrypto>=2.6.1
```
