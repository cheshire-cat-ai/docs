---
title: "Write an Agent"
---

You define an agent by subclassing `Agent` inside a plugin. The Cat discovers it at startup and registers it by its `slug` - the id clients use to talk to it. No other wiring is necessary.

## The smallest agent

The smallest possible agent is just a name and a system prompt. No tools, no directives:

```python
from cat import Agent


class Poet(Agent):
    # `slug` is the id clients use to address this agent. Keep it short.
    slug = "poet"
    # `name` and `description` show up in agent listings (e.g. the UI).
    name = "Poet"
    description = "Answers every message in rhyme."

    # Main instructions.
    system_prompt = "Whatever the user says, you answer in rhyme."
```

Drop this in `plugins/my_plugin/my_agent.py`, and the Cat picks it up automatically.

## Giving the agent hands: tools

A tool is a method decorated with `@tool`. Its name, docstring and type hints become the schema the LLM sees - so the docstring *is* the tool's manual. Tools are `async`, so they can `await` a database, the network, anything.

```python
from cat import Agent, tool, user


class TodoAgent(Agent):
    slug = "todo"
    name = "Todo Agent"
    description = "Keeps a personal to-do list, saved per user."

    system_prompt = (
        "You are a friendly to-do list assistant. Use your tools to read and "
        "change the user's list — never invent items. After changing the list, "
        "briefly confirm what you did."
    )

    @tool
    async def list_todos(self) -> str:
        """List all of the user's todos with their id and done state."""
        todos = await user.load("todos", [])
        if not todos:
            return "The to-do list is empty."
        return "\n".join(f"#{t['id']} {t['text']}" for t in todos)

    @tool
    async def create_todo(self, text: str) -> str:
        """Add a new todo with the given text. Returns the created item's id."""
        todos = await user.load("todos", [])
        new_id = max((t["id"] for t in todos), default=0) + 1
        todos.append({"id": new_id, "text": text, "done": False})
        await user.save("todos", todos)
        return f"Created todo #{new_id}: {text}"
```

Say *"add milk and eggs, then show my list"* and watch the agentic loop work: the agent calls `create_todo` twice, then `list_todos`, then answers - several turns of the loop, each a tool call.

Two things to notice:

- **Tools are agent-scoped.** This agent sees exactly the tools defined on it. There is no global tool pool like in v1. To share tools across agents, put them in a mixin and inherit it; to add them programmatically, use a directive.
- **State is scoped to the caller.** `from cat import user` is the ambient handle to whoever sent the message. `user.save("todos", todos)` allows you to persist the todo lists per user, so two users talking to the same agent never see each other's data. If you want to share data across users, you can use `store.save("key", "value")`.

## Talking to an agent

Send a message and name the agent by its `slug`:

```http
POST /agents/{slug}/message
{ "messages": [{ "role": "user", "content": "add milk and eggs, then show my list" }] }
```

The built-in agent is `default`. Any agent in any installed plugin can be addressed by its `slug`. You can browse every registered agent - and its argument schema - via `GET` [localhost:1865/agents](http://localhost:1865/agents), or feed [localhost:1865/openapi.json](http://localhost:1865/openapi.json) to your own coding agent.

## Where to go next

- [Tools](/docs/plugins/tools/) — the agent's hands, in depth.
- [Hooks](/docs/plugins/hooks/) — adapt the Cat's flow around your agent.
