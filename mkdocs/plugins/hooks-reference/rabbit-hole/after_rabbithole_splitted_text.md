---
title: after_rabbithole_splitted_text
---

# `after_rabbithole_splitted_text`

Intervene after the *RabbitHole* has split the document in chunks.

Allows editing the list of `Document` right after the *RabbitHole* chunked them in smaller ones.

## &#128196; Arguments

| Name     | Type                                                                    | Description                                                        |
|:---------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `chunks` | `List[Document]`                                                        | List of Langchain `Document`s with text chunks.                    |
| `cat`    | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Type: `List[Document]`

List of modified chunked Langchain `Document`s to be stored in the episodic memory.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def after_rabbithole_splitted_text(chunks, cat):
    # post process the chunks
    for chunk in chunks:
        new_content = cat.llm(f"Replace any dirty word with 'Meow': {chunk}")
        chunk.page_content = new_content

    return chunks
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
