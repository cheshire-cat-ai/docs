---
title: before_cat_recalls_procedural_memories
---

# `before_cat_recalls_procedural_memories`

Intervene before the Cat searches among the action it knows.

Allows intercepting when the Cat queries the memories using the embedded user's input.

The hook is executed just before the Cat searches for the meaningful context in both memories
and stores it in the *Working Memory*.

The hook returns the values for maximum number (k) of items to retrieve from memory and the score threshold applied
to the query in the vector memory (items with score under the threshold are not retrieved)
It also returns the embedded query (embedding) and the conditions on recall (metadata).

## &#x1F4C4; Arguments

| Name                       | Type                                                                    | Description                                                         |
|:---------------------------|:------------------------------------------------------------------------|---------------------------------------------------------------------|
| `procedural_recall_config` | `dict`                                                                  | Dictionary with data needed to recall tools from procedural memory. |
| `cat`                      | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.  |

The default value for `procedural_recall_config` is:
```python
{
    "embedding": recall_query_embedding,  # embedding of the recall query
    "k": 3,  # number of memories to retrieve
    "threshold": 0.7,  # similarity threshold to retrieve memories
    "metadata": None,  # dictionary of metadata to filter memories
}
```
## &#x21A9;&#xFE0F; Return

Type: `dict`

Edited dictionary that will be fed to the embedder.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_cat_recalls_procedural_memories(procedural_recall_config, cat):
    # decrease the threshold to recall more tools
    declarative_recall_config["threshold"] = 0.5

    return procedural_recall_config
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)
