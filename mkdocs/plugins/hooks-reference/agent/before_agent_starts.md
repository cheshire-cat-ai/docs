---
title: before_agent_starts
---

# `before_agent_starts`

Prepare the agent input before it starts.

This hook allows reading and editing the agent input.

## &#128196; Arguments 

| Name          | Type                                                                    | Description                                                        |
|:--------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `agent_input` | `dict`                                                                  | The information that is about to be passed to the agent.           |
| `cat`         | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The value of `agent_input` will be:
```python
{
    "input": working_memory.user_message_json.text,  # user's message
    "episodic_memory": episodic_memory_formatted_content,  # strings with documents recalled from memories
    "declarative_memory": declarative_memory_formatted_content,
    "chat_history": conversation_history_formatted_content,
    "tools_output": tools_output
}
```

## &#x21A9;&#xFE0F; Return

Type: `dict`

The agent input.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def before_agent_starts(agent_input, cat):
    # create a compressor and summarize the conversation history
    compressed_history = cat.llm(f"Make a concise summary of the following: {agent_input['chat_history']}")
    agent_input["chat_history"] = compressed_history
    
    return agent_input
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
