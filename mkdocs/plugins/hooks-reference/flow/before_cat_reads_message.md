---
title: before_cat_reads_message
---

# `before_cat_reads_message(user_message_json, cat)`

Intervene as soon as a WebSocket message is received.

Allows editing and enrich the incoming message received from the WebSocket connection.

For instance, this hook can be used to translate the user's message before feeding it to the Cat.
Another use case is to add custom keys to the JSON dictionary.

The incoming message is a JSON dictionary with keys:
```json
{
    "text": "<message content>"
}
```

## &#x1F4C4; Arguments

| Name                | Type                                                                    | Description                                                        |
|:--------------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `user_message_json` | `dict`                                                                  | JSON dictionary with the message received from the chat.           |
| `cat`               | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

| Name                | Type   | Description                                         |
|:--------------------|:-------|-----------------------------------------------------|
| `user_message_json` | `dict` | Edited JSON dictionary that will be fed to the Cat. |

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1 
def before_cat_reads_message(user_message_json, cat):
    user_message_json["text"] = "The original message has been replaced"
    cat.working_memory.hacked = True

    return user_message_json
```

You can also add custom keys to store any custom data, such as the resulting dictionary:
```
{
    "text": "Hello Cheshire Cat!",
    "custom_key": True
}
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
