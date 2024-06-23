# Plugins

Plugins are add-ons that can be installed to extend and customize the Cheshire Cat.  
A plugin is nothing but a collection of hooks and tools.

## Hooks

The Cat uses functions known as *hooks*, which can be overridden, to customize the behavior of the framework in specific execution places.  
Hooks come with a *priority* property.  
The [plugins manager](cheshire_cat/mad_hatter.md) takes care of collecting all the hooks, sorting and executing them in descending order of priority.

## Tools

Tools are custom Python functions that are called by the [Tool Agent](cheshire_cat/agent.md#tool-chain).  
They come with a rich docstring upon with the [Tool Agent](cheshire_cat/agent.md) chooses *whether* and *which* tool is the most suitable to fulfill the user's request.
The list of available tools ends up in the [Instruction Prompt](prompts/instructions.md), that instructs the [Tool Agent](cheshire_cat/agent.md) on how to structure its reasoning.

![Schema of the Cheshire Cat components](../../assets/img/diagrams/plugin2.jpg){width=300px}

!!! note "Developer documentation"  
    - [How to write a plugin](../../plugins/plugins.md)
    - [Hooks](../../plugins/hooks.md)
    - [Tools](../../plugins/tools.md)
