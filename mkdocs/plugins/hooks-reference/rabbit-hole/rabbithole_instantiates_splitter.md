---
title: rabbithole_instantiates_splitter
---

# `rabbithole_instantiates_splitter`

Hook the splitter used to split text in chunks.

Allows replacing the default text splitter to customize the splitting process.

## &#128196; Arguments

| Name            | Type                                                                    | Description                                                                     |
|:----------------|:------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `text_splitter` | `TextSplitter`                                                          | The text splitter used by default, currently is the Langchain's `TextSplitter`. |
| `cat`           | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.              |

## &#x21A9;&#xFE0F; Return

Type: `TextSplitter`

An instance of a TextSplitter subclass.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def rabbithole_instantiates_splitter(text_splitter, cat):
    text_splitter._chunk_size = 64
    text_splitter._chunk_overlap = 8
    return text_splitter
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
