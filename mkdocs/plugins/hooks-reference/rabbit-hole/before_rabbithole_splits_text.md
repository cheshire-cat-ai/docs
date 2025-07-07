---
title: before_rabbithole_splits_text
---

# `before_rabbithole_splits_text`

Intervene before the uploaded document is split into chunks.

Allows editing the uploaded document main `Document`(s) before the *RabbitHole* recursively splits it in shorter ones.
Please note that this is a list because parsers can output one or more `Document`, that are afterward split.

For instance, the hook allows to change the text or edit/add metadata.

## &#128196; Arguments

| Name   | Type                                                                    | Description                                                                         |
|:-------|:------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `docs` | `List[Document]`                                                        | Langchain `Document`s resulted after parsing the file uploaded in the *RabbitHole*. |
| `cat`  | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.                  |

`doc` example:

```python
docs = List[Document(page_content="This is a very long document before being split", metadata={})]
```

## &#x21A9;&#xFE0F; Return

Type: `List[Document]`

Edited Langchain `Document`s.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_rabbithole_splits_text(docs, cat):
    for doc in docs:
        doc.page_content = doc.page_content.replace("dog", "cat")
    return docs
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
