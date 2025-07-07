---
title: after_rabbithole_stored_documents
---

# `after_rabbithole_stored_documents`

Intervene after the Rabbit Hole ended the ingestion pipeline.

Allows editing and enhancing the list of `Document` after is inserted in the vector memory.

## &#128196; Arguments

| Name     | Type                                                                    | Description                                                          |
|:---------|:------------------------------------------------------------------------|----------------------------------------------------------------------|
| `source` | `str`                                                                   | Name of ingested file/url.                                           |
| `docs`   | `List[PointStruct]`                                                     | List of Qdrant `PointStruct` just inserted into the vector database. |
| `cat`    | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.   |

## &#x21A9;&#xFE0F; Return

Returns? Oh no, dear developer, this function is a one-way trip into the rabbit hole.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def after_rabbithole_stored_documents(source, stored_points, cat):
    # do whatever here
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
