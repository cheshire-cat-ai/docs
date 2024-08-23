# Procedures Prompt

The Procedures Prompt explains the [ Procedures Agent](../cheshire_cat/tool_chain.md) how to format its reasoning.  
The [Agent](../cheshire_cat/agent.md) uses a [chain](https://python.langchain.com/v0.2/docs/introduction/)
to decide *when* and *which* [tool](../../../plugins/tools.md) or [form](../../../plugins/forms.md) is the most appropriate to fulfill the user's needs.

The prompt looks like this:

```python
TOOL_PROMPT = """Create a JSON with the correct "action" and "action_input" to help the Human.
You can use one of these actions:
{tools}
- "no_action": Use this action if no relevant action is available. Input is always null.

## The JSON must have the following structure:

{{
    "action": // str - The name of the action to take, should be one of [{tool_names}, "no_action"]
    "action_input": // str or null - The input to the action according to its description
}}

{examples}
"""
```

where the placeholders `{tools}` and `{tool_names}` is replaced with the list of Python tools retrieved from the [procedural memory](../memory/long_term_memory.md).

