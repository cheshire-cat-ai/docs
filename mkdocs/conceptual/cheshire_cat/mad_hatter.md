# Mad Hatter

The Mad Hatter is the Cat's [plugins](../plugins.md) manager.
It takes care of loading, prioritizing and executing plugins.

Specifically, the Mad Hatter lists all available plugins in proper folder and sort their hooks in descending order of priority. 
When the Cat invokes them, it executes them following that order.

!!! note "Developer documentation"
    - [How to write a plugin](../../technical/plugins/plugins.md)
    - [Hooks](../../technical/plugins/hooks.md)
    - [Tools](../../technical/plugins/tools.md)
