# &#128450;&#65039; Memory Backup

## Create a full backup

To create a complete backup for the memories of your Cheshire Cat, you simply need to copy the `long_term_memory` folder located in the root directory. This will allow you to later load all the (declarative and episodic) memories into a new instance whenever you wish.   

## Restore a full backup

To load your backup into a clean installation of Cheshire Cat, you just need to copy the `long_term_memory` folder into the root directory at the same level as the `core` folder. In case you've already started an instance of Cheshire Cat, you will find the `long_term_memory` folder there; you can safely overwrite it.

!!! warning
    The `long_term_memory` folder may be protected, and you might need to use the admin permissions of your system to access it.

The terminal command to perform this operation is as follows:

```bash
sudo cp -r /path/to/source/cheshire_cat/long_term_memory /path/to/destination/cheshire_cat
```