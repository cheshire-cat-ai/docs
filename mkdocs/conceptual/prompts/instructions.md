# Instructions Prompt

The Instruction Prompt explains the [Tool Agent](../cheshire_cat/agent.md#tool-chain) how to format its reasoning.  
The [Tool Agent](../cheshire_cat/agent.md) uses a [chain](https://docs.langchain.com/docs/components/chains/llm-chain)
to decide *when* and *which* [tool](../plugins.md) is the most appropriate to fulfill the user's needs.

By default, it is set to Langchain [instructions format](https://api.python.langchain.com/en/latest/agents/langchain.agents.conversational.base.ConversationalAgent.html?highlight=prompt%20format_instruction)
which looks like this:

```python
instructions = """
To use a tool, please use the following format:

Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

Thought: Do I need to use a tool? No

AI: [your response here]"""
```

where the placeholder `{tool_names}` is replaced with the list of Python [tools](../plugins.md) retrieved from the [procedural memory](../memory/long_term_memory.md).