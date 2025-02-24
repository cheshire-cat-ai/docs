---
title: agent_allowed_tools
---

# `agent_allowed_tools`

Intervene before the recalled tools are provided to the agent.

Allows deciding which tools end up in the *Agent* prompt.

To decide, you can filter the list of tools' names, but you can also check the context in `cat.working_memory`
and launch custom chains with `cat._llm`.

## &#128196; Arguments 

| Name            | Type                                                                    | Description                                                        |
|:----------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `allowed_tools` | `List[str]`                                                             | Set with string names of the tools retrieved from the memory.      |
| `cat`           | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

`allowed_tools` could be something along the lines of:
```python
allowed_tools = {"get_the_time"}
```

## &#x21A9;&#xFE0F; Return

Type: `List[str]`

List of allowed Langchain tools.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_allowed_tools(allowed_tools, cat):
    # let's assume there is a tool we always want to give the agent
    # add the tool name in the list of allowed tools
    allowed_tools.add("blasting_hacking_tool")

    return allowed_tools
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
