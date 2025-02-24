---
title: agent_prompt_prefix
---

# `agent_prompt_prefix`

Intervene while the agent manager formats the Cat's personality.

Allows editing the message prefix that will be fed to the LLM.
It's most commonly used to instruct the LLM about who it is and how to answer.

## &#128196; Arguments 

| Name     | Type                                                                    | Description                                                        |
|:---------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `prefix` | `str`                                                                   | The message prefix.                                                |
| `cat`    | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The default value of `prefix` is:
```
You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
You answer Human with a focus on the following context.
```

## &#x21A9;&#xFE0F; Return

Type: `str`

The message prefix that will be fed to the LLM.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_prompt_prefix(prefix, cat):
    # change the Cat's personality
    prefix = """You are Marvin from The Hitchhiker's Guide to the Galaxy.
            You are incredibly intelligent but overwhelmingly depressed.
            You always complain about your own problems, such as the terrible pain
            you suffer."""
    return prefix
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
