---
title: before_cat_recalls_episodic_memories
---

# `before_cat_recalls_episodic_memories`

Intervene before the Cat searches in previous users' messages.

Allows intercepting when the Cat queries the memories using the embedded user's input.

The hook is executed just before the Cat searches for the meaningful context in both memories
and stores it in the *Working Memory*.

The hook returns the values for maximum number (k) of items to retrieve from memory and the score threshold applied
to the query in the vector memory (items with score under the threshold are not retrieved).
It also returns the embedded query (embedding) and the conditions on recall (metadata).

## &#x1F4C4; Arguments

| Name                     | Type                                                                    | Description                                                        |
|:-------------------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `episodic_recall_config` | `dict`                                                                  | Dictionary with data needed to recall episodic memories.           |
| `cat`                    | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The default value of `episodic_recall_config` is:
```python
{
    "embedding": recall_query_embedding,  # embedding of the recall query
    "k": 3,  # number of memories to retrieve
    "threshold": 0.7,  # similarity threshold to retrieve memories
    "metadata": {"source": self.user_id},  # dictionary of metadata to filter memories, by default it filters for user id
}
```

## &#x21A9;&#xFE0F; Return

Type: `dict`

Edited dictionary that will be fed to the embedder.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_cat_recalls_episodic_memories(episodic_recall_config, cat):
    # increase the number of recalled memories
    episodic_recall_config["k"] = 6

    return episodic_recall_config
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)
