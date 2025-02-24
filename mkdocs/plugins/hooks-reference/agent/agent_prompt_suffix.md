---
title: agent_prompt_suffix
---

# `agent_prompt_suffix`

Intervene while the agent manager formats the prompt suffix with the memories and the conversation history.

Allows editing the suffix of the *Main Prompt* that the Cat feeds to the *Agent*.

The suffix is concatenated to [`agent_prompt_prefix`](agent_prompt_prefix.md) when RAG context is used.

## &#128196; Arguments 

| Name            | Type                                                                    | Description                                                                 |
|:----------------|:------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `suffix`        | `str`                                                                   | The ending part of the prompt containing the memories and the chat history. |
| `cat`           | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.          |

The default value of `suffix` is:
```
# Context
{episodic_memory}

{declarative_memory}

{tools_output}
```

The `suffix` can contain few placeholders:

| Name                   | Description                                                                   |
|:-----------------------|:------------------------------------------------------------------------------|
| `{episodic_memory}`    | Provides memories retrieved from *episodic* memory (past conversations)       |
| `{declarative_memory}` | Provides memories retrieved from *declarative* memory (uploaded documents)    |
| `{chat_history}`       | Provides the *Agent* the recent conversation history                          |
| `{input}`              | Provides the last user's input                                                |
| `{agent_scratchpad}`   | Is where the *Agent* can concatenate tools use and multiple calls to the LLM. |

## &#x21A9;&#xFE0F; Return

Type: `str`

The suffix string to be concatenated to the *Main Prompt* (prefix).

## &#9997; Example

[//]: # (TODO: The comments in the example seems to be irrelevant to the showed code)
```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_prompt_suffix(suffix, cat):
    # tell the LLM to always answer in a specific language
    prompt_suffix =  """
    # Context
    {episodic_memory}
    
    {declarative_memory}
    
    {tools_output}
    """

    return prompt_suffix
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)
