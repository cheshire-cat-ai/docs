---
title: rabbithole_instantiates_parsers
---

# `rabbithole_instantiates_parsers`

Hook the available parsers for ingesting files in the declarative memory.

Allows replacing or extending existing supported mime types and related parsers to customize the file ingestion.

## &#128196; Arguments

| Name            | Type                                                                    | Description                                                                                 |
|:----------------|:------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `file_handlers` | `dict`                                                                  | A dictionary in which keys are the supported mime types and values are the related parsers. |
| `cat`           | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.                          |

## &#x21A9;&#xFE0F; Return

Type: `dict`

Edited dictionary of supported mime types and related parsers.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook
from langchain.document_loaders.parsers.language.language_parser import LanguageParser
from langchain.document_loaders.parsers.msword import MsWordParser

@hook  # default priority = 1
def rabbithole_instantiates_parsers(file_handlers, cat):
    new_handlers = {
        "text/x-python": LanguageParser(language="python"),
        "text/javascript": LanguageParser(language="js"),
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MsWordParser(),
        "application/msword": MsWordParser(),
    }
    file_handlers = file_handlers | new_handlers
    return file_handlers
```

!!! note
    - [IngestAnything Plugin](https://github.com/Furrmidable-Crew/IngestAnything)
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
