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

The process diagrams found under the menu `Developers → Core Process Diagrams` illustrates where the hooks are called during the Cat's execution flow.
Not all the hooks have been documented yet. ( [help needed! &#128568;](https://discord.com/channels/1092359754917089350/1092360068269359206){:target="_blank"} ).

=== "&#127754; Flow"

    <div class="annotate" mardown>

    | Name                                          | Description                                                      |
    | :-------------------------------------------- | :--------------------------------------------------------------- |
    | Before Cat bootstrap (1)                      | Intervene before the Cat's instantiate its components            |
    | After Cat bootstrap (2)                       | Intervene after the Cat's instantiated its components            |
    | Before Cat reads message (3)                  | Intervene as soon as a WebSocket message is received             |
    | Cat recall query (4)                          | Intervene before the recall query is embedded                    |
    | Before  Cat recalls memories (5)              | Intervene before the Cat searches into the specific memories     |
    | Before  Cat recalls episodic memories (6)     | Intervene before the Cat searches in previous users' messages    |
    | Before  Cat recalls declarative memories (7)  | Intervene before the Cat searches in the documents               |
    | Before  Cat recalls procedural memories (8)   | Intervene before the Cat searches among the action it knows      |
    | After  Cat recalls memories (9)               | Intervene after the Cat's recalled the content from the memories |
    | Before  Cat sends message (10)                | Intervene before the Cat sends its answer via WebSocket          |
    
    </div>
    
    1. ### Input arguments
    2. ### Input arguments
    3. ### Input arguments  
        `user_message_json`, i.e. the JSON message sent via WebSocket done like this:  
        ```JSON
        {
            "text": # user's message here
        }
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook

            @hook  # default priority = 1 
            def before_cat_reads_message(user_message_json, cat):
                user_message_json["text"] = "The original message has been replaced"
                cat.working_memory["hacked"] = True

                return user_message_json
            ```

        ??? note "Other resources"

            - [Python reference]()

    4. ### Input arguments
    5. ### Input arguments
    6. ### Input arguments
    7 .### Input arguments
    8. ### Input arguments
    9. ### Input arguments
    10. ### Input arguments

=== "&#129302; Agent"
    
    <div class="annotate" mardown>

    | Name                          | Description                                             |
    | :---------------------------- | :------------------------------------------------------ |
    | Before agent starts (11)      | Intervene before the agent starts                                                |
    | Agent fast reply (12)         | Shorten the pipeline and returns an answer right after the agent execution       |
    | Agent prompt prefix (13)      | Intervene while the agent manager formats the Cat's personality                  |
    | Agent prompt suffix (14)      | Intervene while the agent manager formats the prompt suffix with the memories and the conversation history |
    | Agent allowed tools (15)      | Intervene before the recalled tools are provided to the agent                    |
    | Agent prompt instructions (16)| Intervent while the agent manager formats the reasoning prompt                   |

    </div>

    11. ### **Input arguments**  
    12. ### **Input arguments**  
    13. ### **Input arguments**  
    14. ### **Input arguments**  
    15. ### **Input arguments**
    16. ### **Input arguments**  

=== "&#128048; Rabbit Hole"
    
    <div class="annotate" mardown>

    | Name                                      | Description                                                    |
    | :---------------------------------------- | :------------------------------------------------------------- |
    | Rabbit Hole instantiates parsers (17)      | Intervene before the files' parsers are instiated              |
    | Before Rabbit Hole insert memory (18)      | Intervene before the Rabbit Hole insert a document in the declarative memory |
    | Before Rabbit Hole splits text (19)        | Intervene before the uploaded document is split into chunks    |
    | After Rabbit Hole splitted text (20)       | Intervene after the Rabbit Hole's split the document in chunks |
    | Before Rabbit Hole stores documents (21)   | Intervene before the Rabbit Hole starts the ingestion pipeline |

    </div>

    17. ### **Input arguments**
    18. ### **Input arguments**
    19. ### **Input arguments**
    20. ### **Input arguments**  
    21. ### **Input arguments**  