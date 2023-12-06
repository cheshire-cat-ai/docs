# &#129693; Hooks

Hooks are Python functions that are called directly from the Cat at runtime, they allow you to change how the Cat internally works without directly modifying the Cat itself.

## How the Hooks work
To create a hook, you first need to create a [plugin](plugins.md) that contains it. Once the plugin is created, you can insert hooks inside the plugin, a single plugin can contain multiple hooks.

A hook is simply a Python function that uses the `@hook` decorator, the function's name determines when it will be called.

There are two kinds of hooks. The first type of hook receives only the Cat instance as a parameter, while the second type of hook receives both the Cat instance and the value determined by default Cat implementation.

With the first type, you can perform actions at specific points in the Cat's execution flow. For example, you can use the `before_cat_bootstrap` hook to execute some operations before the Cat starts:

```python
from cat.mad_hatter.decorators import hook

@hook(priority=1)
def before_cat_bootstrap(cat):
    # You can perform operations with the cat (modify working memory, access LLM, etc.)
    do_my_thing()
```

You can use the second type of hook to modify the value determined by the default Cat implementation. For example, you can use the `before_cat_sends_message` hook to alter the message that the Cat will send to the user.

```python
from cat.mad_hatter.decorators import hook

@hook(priority=1)
def before_cat_sends_message(final_output, cat):
    # You can perform operations with the cat (modify working memory, access LLM, etc.)
    do_my_thing()
    # You can return a new value that will be used instead of Cat calculated value
    return final_output.upper()
```

*Some hooks receive more than one argument, the value determined by the Cat is always the first argument, all the other parameters are solely context parameters, which hooks cannot modify, the last parameter is always the Cat instance.*

## Multiple Implementations
Several plugins can implement the same hook. The argument `priority` of the `@hook` decorator allows you to set the priority of the hook, the default value is 1. 

The Cat calls the implementations in order of priority. Hooks with a higher priority number will be called first. The following hooks will receive the value returned by the previous hook. In this way, hooks can be chained together to create complex behaviors.

If two plugins have the same priority, the order in which they are called is not guaranteed.

## Available Hooks
You can view the list of available hooks by exploring the Cat source code under the folder `core/cat/mad_hatter/core_plugin/hooks`.
All the hooks you find in there define default Cat's behavior and are ready to be overridden by your plugins.

The process diagrams found under the menu `Developers → Core Process Diagrams` illustrate where the hooks are called during the Cat's execution flow.
Not all of the hooks have been documented yet. ( [help needed! &#128568;](https://discord.com/channels/1092359754917089350/1092360068269359206){:target="_blank"} ).

## More Examples

TODO
## Hook List

### Agent Hooks
  - before_agent_starts
  - agent_fast_reply
  - agent_allowed_tools
  - #### Prompt Hooks:
     - agent_prompt_prefix
     - agent_prompt_instructions
     - agent_prompt_suffix



### Execution pipeline Hooks
- before_cat_bootstrap
- after_cat_bootstrap
- before_cat_reads_message
- cat_recall_query
- before_cat_recalls_memories
- before_cat_recalls_episodic_memories
- before_cat_recalls_declarative_memories
- before_cat_recalls_procedural_memories
- after_cat_recalls_memories
- before_cat_sends_message
### Rabbit Hole Hooks
- rabbithole_instantiates_parsers
- before_rabbithole_insert_memory
- before_rabbithole_splits_text
- after_rabbithole_splitted_text
- before_rabbithole_stores_documents
## Hook search

TODO
