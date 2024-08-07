# Stray Cat

The StrayCat class is a key component of the Cheshire Cat framework, serving as the primary entry point to all its features. This component handles user sessions, manages working memory, facilitates conversations, and provides essential methods for LLM interaction, WebSocket messaging, and more.

## Main Entry Point to the Framework

The StrayCat class is designed to be your primary interface for leveraging the full capabilities of the framework. By using this class, you can access various features and functionalities without the need to instantiate objects that have already been created as singletons. It also provides convenient shortcuts to access nested or user-related structures within the Cat, streamlining your development process.

Whenever you see something like:

```python

from cat.mad_hatter.decorators import tool

@tool
def some_fancy_tool(some_fancy_arg, cat):
    pass

```

Or:

```python

from cat.mad_hatter.decorators import hook

@hook(priority=1)
def before_cat_sends_message(final_output, cat):
    return final_output.upper()

```

You'll probably notice the `cat` parameter being passed around. This cat is an instance of the `StrayCat` class. Like a wandering stray cat, this component roams through different parts of the framework, encapsulating the session's state and providing the necessary context for various operations within the Cheshire Cat ecosystem.

For more detail about useful methods, please see [Useful Methods and Shortcuts](#useful-methods-and-shortcuts).

## User session management

Whenever a user sends a message to the Cat, a `StrayCat` instance is called within the specific user context. This instance is responsible for several key tasks: handling incoming messages, updating the conversation history, managing working memory, delegating the framework agents to elaborate the response and finally gathering all relevant information about the response, including the content and the reasoning behind it (the "why"). This comprehensive response is then returned to the user.

## Useful Methods and Shortcuts

### Shortcuts

As mentioned above, the StrayCat class provides some shortcuts to access Cheshire Cat features. For example:

```python

from cat.mad_hatter.decorators import tool

@tool
def some_fancy_scheduling_tool(some_fancy_arg, cat):
    # We can access the White Rabbit to schedule jobs
    job_id = cat.white_rabbit.schedule_chat_message("Hello", cat, minutes=5)
    return job_id

```

In the same way you can access other Cat components like the [Mad Hatter](/framework/cat-components/cheshire_cat/mad_hatter/) or the [Rabbit Hole](/framework/cat-components/cheshire_cat/rabbit_hole/)

Beside Cat components, you can also access the [Working Memory](/framework/cat-components/cheshire_cat/working_memory/). easily like so:

```python

from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def some_fancy_tool(some_fancy_arg, cat):
    # We can access the Working Memory to clear the chat history if this tool is used
    cat.working_memory.user_message_json.history = []
    return "Chat history cleared"

```

### Useful Methods

The `StrayCat` class exposes many methods, some of which are used internally by the framework. However, there are several methods that are particularly useful for developers:

- `send_chat_message`: sends a message to the user using the active WebSocket connection. 
- `send_notification`: sends a notification to the user using the active WebSocket connection.
- `send_error`: sends an error message to the user using the active WebSocket connection.
- `llm`: shortcut method for generating a response using the LLM and passing a custom prompt.
- `classify`: utility method for classifying a given sentence using the LLM. You can pass either a list of strings as possible labels or a dictionary of labels as keys and list of strings as examples.
- `stringify_chat_history`: utility method to stringify the chat history.

These methods provide easy-to-use interfaces for interacting with LLMs and other components of the Cheshire Cat framework, making plugin development faster and more efficient.

For more details, see the [StrayCat API reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/looking_glass/stray_cat/)