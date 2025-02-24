---
title: before_cat_stores_episodic_memory
---

# `before_cat_stores_episodic_memory`

Intervene before the Cat stores episodic memories.

Allows intercepting the user message `Document` before is inserted in the vector memory.

The `Document` can then be edited and enhanced before the Cat stores it in the episodic vector memory.

## &#x1F4C4; Arguments

| Name  | Type                                                                    | Description                                                        |
|:------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `doc` | `Document`                                                              | Langchain `Document` to be inserted in memory.                     |
| `cat` | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The `Document` has two properties:

- `page_content`: the string with the text to save in memory;
- `metadata`: a dictionary with at least two keys:
    - `source`: where the text comes from;
    - `when`: timestamp to track when it's been uploaded.

## &#x21A9;&#xFE0F; Return

Type: `Document`

Langchain `Document` that is added in the episodic vector memory.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_cat_stores_episodic_memory(doc, cat):
    if doc.metadata["source"] == "dolphin":
        doc.metadata["final_answer"] = 42
    return doc
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
