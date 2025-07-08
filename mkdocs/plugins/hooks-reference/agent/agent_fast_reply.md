---
title: agent_fast_reply
---

# `agent_fast_reply`

Shorten the pipeline and return an answer right after the agent execution.

This hook allows for a custom response after memory recall, skipping default agent execution.
It's useful for custom agent logic or when you want to use recalled memories, but you want to avoid the main agent.

!!! info
    To skip the agent execution, you should populate `fast_reply` with an `output` key storing the reply.

    P.S.: this is the perfect place to instantiate and execute your own custom agent!

## &#128196; Arguments 

| Name         | Type                                                                    | Description                                                        |
|:-------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `fast_reply` | `dict`                                                                  | An initially empty dict that can be populated with a response.     |
| `cat`        | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

[//]: # (TODO: Could be nice to add a reference to AgentOutput)
Type: `None | dict | AgentOutput`

If you want to bypass the main agent, return an `AgentOutput` or a dict with an `output` key.
Return `None` to continue with normal execution.

## &#9997; Example

The cat has no memory (no uploaded document) about a specific topic:
```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def agent_fast_reply(fast_reply, cat):
	# answer with predefined sentences if the Cat
	# has no knowledge in the declarative memory
	# (increasing the threshold memory is advisable)
	if len(cat.working_memory.declarative_memories) == 0:
		fast_reply["output"] = "Sorry, I have no memories about that."

	return fast_reply
```

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [Stay on topic plugin](https://github.com/Furrmidable-Crew/stay_on_topic)
