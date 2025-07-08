---
title: before_cat_sends_message
---

# `before_cat_sends_message`

Intervene before the Cat sends its answer via WebSocket.

Allows editing the JSON dictionary that will be sent to the client via WebSocket connection.

This hook can be used to edit the message sent to the user or to add keys to the dictionary.

## &#x1F4C4; Arguments

| Name      | Type                                                                    | Description                                                        |
|:----------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `message` | `dict`                                                                  | JSON dictionary to be sent to the WebSocket client.                |
| `cat`     | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

TODO: Resolve doc mismatch

The default value of `episodic_recall_config` is:
```python
{
    "type": "chat",
    "content": cat_message["output"],
    "why": {
        "input": cat_message["input"],
        "output": cat_message["output"],
        "intermediate_steps": cat_message["intermediate_steps"],
        "memory": {
            "vectors": {
                "episodic": episodic_report,
                "declarative": declarative_report
            }
        },
    },
}

{
    "type": "chat",  # type of websocket message, a chat message will appear as a text bubble in the chat
    "user_id": "user_1",  # id of the client to which the message is to be sent
    "content": "Meeeeow",  # the Cat's answer
    "why": {
        "input": "Hello Cheshire Cat!",  # user's input
        "intermediate_steps": cat_message.get("intermediate_steps"),  # list of tools used to provide the answer
        "memory": {
            "episodic": episodic_report,  # lists of documents retrieved from the memories
            "declarative": declarative_report,
            "procedural": procedural_report,
        }
    }
}
```

## &#x21A9;&#xFE0F; Return

Type: `dict`

Edited JSON dictionary with the Cat's answer.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_cat_sends_message(message, cat):
    # use the LLM to rephrase the Cat's answer
    new_answer = cat.llm(f"Reformat this sentence like if you were a dog")  # Baauuuuu
    message["content"] = new_answer

    return message
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
