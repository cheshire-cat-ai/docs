---
title: before_rabbithole_insert_memory
---

# `before_rabbithole_insert_memory`

Intervene before the *RabbitHole* insert a `Document` in the declarative memory.

Allows editing and enhancing a single `Document` before the *RabbitHole* add it to the declarative vector memory.

Example of the Langchain document:

```python
doc = Document(page_content="So Long, and Thanks for All the Fish", metadata={})
```

## &#128196; Arguments

| Name  | Type                                                                    | Description                                                        |
|:------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `doc` | `Document`                                                              | Langchain `Document` to be inserted in memory.                     |
| `cat` | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The `Document` has two properties:

- `page_content`: the string with the text to save in memory;
- `metadata`: a dictionary with at least two keys:
    - `source`: where the text comes from;
    - `when`: timestamp to track when it's been uploaded.

!!! info 
    Before adding the `doc`, the Cat will add `source` and `when` metadata with the file name and ingestion time.

## &#x21A9;&#xFE0F; Return

Type: `Document`

Langchain `Document` that is added in the declarative vector memory.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_rabbithole_insert_memory(doc, cat):
    # insert the user id metadata
    doc.metadata["user_id"] = cat.user_id
    
    return doc
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
    - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)
