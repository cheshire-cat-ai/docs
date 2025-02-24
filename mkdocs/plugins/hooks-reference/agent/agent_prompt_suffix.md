---
title: agent_prompt_suffix
---

# `agent_prompt_suffix`

Intervene while the agent manager formats the prompt suffix with the memories and the conversation history.

## &#128196; Arguments 

| Name            | Type                                                                    | Description                                                                 |
|:----------------|:------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `prompt_suffix` | `str`                                                                   | The ending part of the prompt containing the memories and the chat history. |
| `cat`           | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.          |

The default value of `prompt_suffix` is:
```
# Context
{episodic_memory}

{declarative_memory}

{tools_output}
```

## &#x21A9;&#xFE0F; Return

Type: `str`

The prompt suffix with the memories and the conversation history.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_prompt_suffix(prompt_suffix, cat):
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
