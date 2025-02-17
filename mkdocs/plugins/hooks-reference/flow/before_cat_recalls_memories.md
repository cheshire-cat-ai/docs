---
title: before_cat_recalls_memories
---

# `before_cat_recalls_memories(cat)`

Intervene before the Cat searches into the specific memories.

Allows intercepting when the Cat queries the memories using the embedded user's input.

The hook is executed just before the Cat searches for the meaningful context in both memories
and stores it in the *Working Memory*.

## &#x1F4C4; Arguments

This hook has no input arguments, other than the default cat:

| Name  | Type                                                                    | Description                                                        |
|:------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `cat` | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Returns? Oh no, dear developer, this function is a one-way trip into the rabbit hole.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_cat_recalls_memories(cat):
    # do whatever here
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
