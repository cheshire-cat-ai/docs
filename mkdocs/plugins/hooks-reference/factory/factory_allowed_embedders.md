---
title: factory_allowed_embedders
---

# `factory_allowed_embedders`

Customize which embedders are available.

!!! info
    Useful to extend or restrict support of embedders.

## &#128196; Arguments

| Name      | Type                                                                    | Description                                                        |
|:----------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `allowed` | `List[EmbedderSettings]`                                                | List of EmbedderSettings classes, contains the allowed embedders.  |
| `cat`     | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Type: `List[EmbedderSettings]`

The list of embedders that the cat is allowed to use.

## &#9997; Example

```python
from cat.factory.embedder import EmbedderSettings
from langchain.embeddings import JinaEmbeddings

# Define your custome embedder based on the cat's "EmbedderSettings"
class JinaEmbedderConfig(EmbedderSettings):
    jina_api_key: str
    model_name: str='jina-embeddings-v2-base-en'
    _pyclass: Type = JinaEmbeddings
    
    model_config = ConfigDict(
        json_schema_extra = {
            "humanReadableName": "Jina embedder",
            "description": "Jina embedder",
            "link": "https://jina.ai/embeddings/",
        }
    )

# Add it to the allowed list.
@hook
def factory_allowed_embedders(allowed, cat) -> List:
    allowed.append(JinaEmbedderConfig)
    return allowed
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
