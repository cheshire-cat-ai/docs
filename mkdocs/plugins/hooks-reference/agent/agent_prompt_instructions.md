---
title: agent_prompt_instructions
---

# `agent_prompt_instructions`

Intervene while the agent manager formats the reasoning prompt.

Allows editing the instructions that the Cat feeds to the *Agent* to select tools and forms.

!!! note
    This prompt explains to the *Agent* how to select a tool or form.

## &#128196; Arguments 

| Name           | Type                                                                    | Description                                                        |
|:---------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `instructions` | `str`                                                                   | Instructions prompt to select tool or form.                        |
| `cat`          | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

The default value of `instructions` is:
```
Create a JSON with the correct "action" and "action_input" to help the Human.
You can use one of these actions:
{tools}
- "no_action": Use this action if no relevant action is available. Input is always null.

## The JSON must have the following structure:

  ```json
  {{
      "action": // str - The name of the action to take, should be one of [{tool_names}, "no_action"]
      "action_input": // str or null - The input to the action according to its description
  }}
  ```

{examples}
```

!!! warning
    The placeholders `{tools}`,`{tool_names}` and `{examples}` are mandatory!

## &#x21A9;&#xFE0F; Return

Type: `str`

Instructions prompt to select tool or form.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_prompt_instructions(instructions, cat):
    # let's ask the LLM to translate the tool output
    instructions += "\nAlways answer in mandarin"

    return instructions
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
