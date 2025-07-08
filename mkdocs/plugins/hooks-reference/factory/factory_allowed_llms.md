---
title: factory_allowed_llms
---

# `factory_allowed_llms`

Customize which LLMs are available.

!!! info
    Useful to extend or restrict support of LLMs.

## &#128196; Arguments

| Name      | Type                                                                    | Description                                                        |
|:----------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `allowed` | `List[LLMSettings]`                                                     | List of LLMSettings classes, contains the allowed language models. |
| `cat`     | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Type: `List[LLMSettings]`

The list of the LLMs that the cat is allowed to use.

## &#9997; Example

```python
from cat.factory.llm import LLMSettings
from langchain_mistralai.chat_models import ChatMistralAI

# Define your custome LLM based on the cat's "LLMSettings"
class MistralAIConfig(LLMSettings):
    """The configuration for the MistralAI plugin."""
    mistral_api_key: Optional[SecretStr]
    model: str = "mistral-small"
    max_tokens: Optional[int] = 4096
    top_p: float = 1

    _pyclass: Type = ChatMistralAI

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "MistralAI",
            "description": "Configuration for MistralAI",
            "link": "https://www.together.ai",
        }
    )

# Add it to the allowed list.
@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(MistralAIConfig)
    return allowed
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
