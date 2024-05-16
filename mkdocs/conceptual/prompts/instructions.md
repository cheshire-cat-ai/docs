# Instructions Prompt

The Instruction Prompt explains the [Tool Agent](../cheshire_cat/agent.md#tool-chain) how to format its reasoning.
The [Tool Agent](../cheshire_cat/agent.md) uses a [chain](https://docs.langchain.com/docs/components/chains/llm-chain)
to decide *when* and *which* [tool](../plugins.md) is the most appropriate to fulfill the user's needs.

By default, it is set to Langchain [instructions format](https://api.python.langchain.com/en/latest/agents/langchain.agents.conversational.base.ConversationalAgent.html?highlight=prompt%20format_instruction)
which looks like this:

```python
instructions = """Create a JSON action to complete the action sequence, with the correct "action" and "action_input" to help the Human.
You can use one of these actions:
{tools}
- "final_answer": Use this action to finish or no relevant action is available. Input is always null.

## To add an action, use only the following format:
\```json
{{
    "action": // str - The name of the action to take, should be one of [{tool_names}, "final_answer"]
    "action_input": // str or null - The input to the action
}}
\```

{examples}

## Action output
After each action there will be an action output in this format:
\```json
{{
    "action_output": // output of the preceding action
}}
\```

## Final answer / no action available
When you have a final answer (or no tools are relevant), use the following format:
\```json
{{
    "action": "final_answer",
    "action_input": null
}}
\```

## Conversation with Human:
{chat_history}

## Actions sequence used until now:
{agent_scratchpad}

## Next action:
\```json
"""
```

where:

- the placeholder `{tools}` is replaced with the list of Python [tools](../plugins.md) retrieved from the [procedural memory](../memory/long_term_memory.md);
- the `{examples}` is replaced with some example actions given to the model;
- the `{chat_history}` is replaced with the chat history with the user;
- the `{agent_scratchpad}` is replaced with the agent scratchpad information about the actions' sequence used until that iteration.