# Stray Cat

The StrayCat class is a key component of the Cheshire Cat framework, serving as the primary entry point to all its features. This component handles user sessions, manages working memory, facilitates conversations, and provides essential methods for LLM interaction, WebSocket messaging, and more.

## Main Entry Point to the Framework

The StrayCat class is designed to be your primary interface for leveraging the full capabilities of the framework. By using this class, you can access various features and functionalities without the need to instantiate objects that have already been created as singletons. It also provides convenient shortcuts to access nested or user-related structures within the Cat, streamlining your development process.

Whenever you see something like:

```python

from cat.mad_hatter.decorators import tool

@tool
def fancy_tool(fancy_arg, cat):
    """Fancy tool docstring, seen by the LLM"""
    return "Did something fancy"

```

Or:

```python

from cat.mad_hatter.decorators import hook

@hook
def before_cat_sends_message(final_output, cat):
    final_output.content = final_output.content.upper()
    return final_output

```

You'll probably notice the `cat` parameter being passed around. This cat is an instance of the `StrayCat` class. Like a wandering stray cat, this component roams through different parts of the framework, encapsulating the session's state and providing the necessary context for various operations within the Cheshire Cat ecosystem.

For more detail about useful methods, please see [Useful Methods and Shortcuts](#useful-methods-and-shortcuts).

## User session management

Whenever a user sends a message to the Cat, a `StrayCat` instance is called within the specific user context. This instance is responsible for several key tasks: handling incoming messages, updating the conversation history, managing working memory, delegating the framework agents to elaborate the response and finally gathering all relevant information about the response, including the content and the reasoning behind it (the "why"). This comprehensive response is then returned to the user.

## Examples

As mentioned above, the StrayCat class provides some shortcuts to access Cheshire Cat features.  
For example you can easily use the LLM:

```python

from cat.mad_hatter.decorators import hook

@hook
def agent_fast_reply(reply, cat):
    prompt = "Say a joke in german"
    reply["output"] = cat.llm(prompt)
    return reply

```

An example using the [White Rabbit](white_rabbit.md) scheduler:

```python

from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def schedule_say_hello(minutes, cat):
    """Say hello in a few minutes. Input is the number of minutes."""

    delay = int(minutes)

    # We can access the White Rabbit to schedule jobs
    job_id = cat.white_rabbit.schedule_chat_message("Hello", cat, minutes=delay)
    
    return f"Scheduled job {job_id} to say hello in {delay} minutes."

```

In the same way you can access other Cat components like the [Mad Hatter](mad_hatter.md) or the [Rabbit Hole](rabbit_hole.md).  
You can also access the [Working Memory](../memory/working_memory.md). Easily like so:

```python

from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def clear_working_memory(arg, cat):
    """Use this tool to clear / reset / delete the conversation history."""

    # We can access the Working Memory to clear the chat history
    cat.working_memory.history = []

    return "Chat history cleared"

```

## Useful Methods and Shortcuts

### Shortcuts


### Useful Methods

The `StrayCat` class exposes many methods, some are particularly useful for plugin developers:

- `cat.send_chat_message(...)`  
    Sends a message to the user using the active WebSocket connection. 
- `cat.send_notification(...)`  
    Sends a notification to the user using the active WebSocket connection.
- `cat.send_error(...)`  
    Sends an error message to the user using the active WebSocket connection.
- `cat.llm(...)`  
    Shortcut method for generating a response using the LLM and passing a custom prompt.
- `cat.embedder.embed_query(...)`  
    Shortcut method to embed a string in vector space.
- `cat.classify(...)`  
    Utility method for classifying a given sentence using the LLM. You can pass either a list of strings as possible labels or a dictionary of labels as keys and list of strings as examples.
- `cat.stringify_chat_history(...)`  
    Utility method to stringify the chat history.

These methods provide easy-to-use interfaces for interacting with LLMs and other components of the Cheshire Cat framework, making plugin development faster and more efficient.

For more details, see the [StrayCat API reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/looking_glass/stray_cat/)