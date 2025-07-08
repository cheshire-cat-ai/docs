# &#129693; Hooks

During execution the Cat emits a few events, for example when a user message arrives, or when a new document is uploaded to memory.
You can `hook` these events to execute your own code and change behavior, memory and anything the Cat does.

The [`Framework → Technical Diagrams`](../framework/flows/cat-bootstrap.md) section illustrates with a diagram where the hooks are called during the Cat's execution flow.
Not all the hooks have been documented yet. ( [help needed! &#128568;](https://discord.com/channels/1092359754917089350/1092360068269359206){:target="_blank"} ).

## Available Hooks

Here is a list of availble hooks. Each has a dedicated page with examples (see `Hooks API Reference` on the left menu).


=== "&#127754; Main Flow"

    ```mermaid
    flowchart TD
        C(before_cat_reads_message)
        D(cat_recall_query)
        E(before_cat_recalls_memories)
        F(before_cat_recalls_episodic_memories)
        G(before_cat_recalls_declarative_memories)
        H(before_cat_recalls_procedural_memories)
        I(after_cat_recalls_memories)
        J(before_cat_stores_episodic_memory)
        K(before_cat_sends_message)
    
        C-->D
        D-->E
        E-->F
        E-->G
        E-->H
        F-->I
        G-->I
        H-->I
        I-- Main Agent execution -->J
        J-->K
    
        click C "/docs/plugins/hooks-reference/flow/before_cat_reads_message"
        click D "/docs/plugins/hooks-reference/flow/cat_recall_query"
        click E "/docs/plugins/hooks-reference/flow/before_cat_recalls_memories"
        click F "/docs/plugins/hooks-reference/flow/before_cat_recalls_episodic_memories"
        click G "/docs/plugins/hooks-reference/flow/before_cat_recalls_declarative_memories"
        click H "/docs/plugins/hooks-reference/flow/before_cat_recalls_procedural_memories"
        click I "/docs/plugins/hooks-reference/flow/after_cat_recalls_memories"
        click J "/docs/plugins/hooks-reference/flow/before_cat_stores_episodic_memory"
        click K "/docs/plugins/hooks-reference/flow/before_cat_sends_message"
    ``` 

=== "&#129302; Agent"

    ```mermaid
        flowchart TD
            A(before_agent_starts)
            B(agent_fast_reply)
            C(agent_allowed_tools)
            D(agent_prompt_prefix)
            E(agent_prompt_suffix)

            A --> B
            B --> C
            C --> D
            D --> E

            click A "/docs/plugins/hooks-reference/agent/before_agent_starts"
            click B "/docs/plugins/hooks-reference/agent/agent_fast_reply"
            click C "/docs/plugins/hooks-reference/agent/agent_allowed_tools"
            click D "/docs/plugins/hooks-reference/agent/agent_prompt_prefix"
            click E "/docs/plugins/hooks-reference/agent/agent_prompt_suffix"
    ```

=== "&#128048; Rabbit Hole"

    ```mermaid
        flowchart TD
            subgraph Ingestion
                A(before_rabbithole_insert_memory)
                B(before_rabbithole_splits_text)
                C(after_rabbithole_splitted_text)
                D(before_rabbithole_stores_documents)
                E(after_rabbithole_stored_documents)

                A --> B
                B --> C
                C --> D
                D --> E
            end

            subgraph Instantiation
                F(rabbithole_instantiates_parsers)
                G(rabbithole_instantiates_splitter)
                F --> G
            end

            click A "/docs/plugins/hooks-reference/rabbit-hole/before_rabbithole_insert_memory"
            click B "/docs/plugins/hooks-reference/rabbit-hole/before_rabbithole_splits_text"
            click C "/docs/plugins/hooks-reference/rabbit-hole/after_rabbithole_splitted_text"
            click D "/docs/plugins/hooks-reference/rabbit-hole/before_rabbithole_stores_documents"
            click E "/docs/plugins/hooks-reference/rabbit-hole/after_rabbithole_stored_documents"
            click F "/docs/plugins/hooks-reference/rabbit-hole/rabbithole_instantiates_parsers"
            click G "/docs/plugins/hooks-reference/rabbit-hole/rabbithole_instantiates_splitter"
    ```

=== "&#128268; Plugin"

    <div class="annotate" mardown>

    | Name                | Description                                      |
    | :------------------ | :----------------------------------------------- |
    | Activated (1)       | Intervene when a plugin is enabled               |
    | Deactivated (2)     | Intervene when a plugin is disabled              |
    | Settings schema (3) | Override how the plugin's settings are retrieved |
    | Settings model (4)  | Override how the plugin's settings are retrieved |
    | Load settings (5)   | Override how the plugin's settings are loaded    |
    | Save settings (6)   | Override how the plugin's settings are saved     |

    </div>

    1. **Input arguments**  
        `plugin`: the `Plugin` object of your plugin with the following properties:
        
        ```python
        plugin.path = # the path of your plugin 
        plugin.id = # the name of your plugin
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from cat.looking_glass.cheshire_cat import CheshireCat

            ccat = CheshireCat()

            @plugin
            def activated(plugin):
                # Upload an url in the memory when the plugin is activated
                url = "https://cheshire-cat-ai.github.io/docs/technical/plugins/hooks/"
                ccat.rabbit_hole.ingest_file(stray=ccat, file=url)
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.activated)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    2. **Input arguments**  
        `plugin`: the `Plugin` object of your plugin with the following properties:
        
        ```python
        plugin.path = # the path of your plugin 
        plugin.id = # the name of your plugin
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from cat.looking_glass.cheshire_cat import CheshireCat

            ccat = CheshireCat()

            @plugin
            def deactivated(plugin):
                # Scroll the declarative memory to clean from memories
                # with metadata on plugin deactivation
                declarative_memory = ccat.memory.vectors.declarative

                response = declarative_memory.delete_points_by_metadata_filter(
                    self, metadata={"source": "best_plugin"}
                )
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.deactivated)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    3. **Input arguments**  
        This hook has no input arguments.

        !!! info

            Default `settings.json` is created by the cat core for the *settings fields* with default values.

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from pydantic import BaseModel, Field

            # define your plugin settings model
            class MySettings(BaseModel):
                prompt_prefix: str = Field(
                            title="Prompt prefix",
                            default="""You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
            You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
            You answer Human with a focus on the following context.
            """,
                            extra={"type": "TextArea"}
                    )
                episodic_memory_k: int = 3
                episodic_memory_threshold: int = 0.7
                declarative_memory_k: int = 3
                declarative_memory_threshold: int = 0.7
                procedural_memory_k: int = 3
                procedural_memory_threshold: int = 0.7

            # get your plugin settings schema
            @plugin
            def settings_schema():
                return MySettings.model_json_schema()

            # load your plugin settings
            settings = ccat.mad_hatter.get_plugin().load_settings()
            # access each setting
            prompt_prefix = settings["prompt_prefix"]
            episodic_memory_k = settings["episodic_memory_k"]
            declarative_memory_k = settings["declarative_memory_k"]
            ```

        ??? note "Other resources"
            - [Example Plugin: C.A.T. Cat Advanced Tools](https://github.com/Furrmidable-Crew/cat_advanced_tools)
            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.settings_schema)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    4. **Input arguments**  
        This hook has no input arguments.

        !!! info

            `settings_model` is preferred to `settings_schema`.

            Default `settings.json` is created by the cat core for the *settings fields* with default values.

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from pydantic import BaseModel, Field

            # define your plugin settings model
            class MySettings(BaseModel):
                prompt_prefix: str = Field(
                            title="Prompt prefix",
                            default="""You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
            You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
            You answer Human with a focus on the following context.
            """,
                            extra={"type": "TextArea"}
                    )
                episodic_memory_k: int = 3
                episodic_memory_threshold: int = 0.7
                declarative_memory_k: int = 3
                declarative_memory_threshold: int = 0.7
                procedural_memory_k: int = 3
                procedural_memory_threshold: int = 0.7

            # get your plugin settings Pydantic model
            @plugin
            def settings_model():
                return MySettings

            # load your plugin settings
            settings = ccat.mad_hatter.get_plugin().load_settings()
            # access each setting
            declarative_memory_k = settings["declarative_memory_k"]
            declarative_memory_threshold = settings["declarative_memory_threshold"]
            procedural_memory_k = settings["procedural_memory_k"]
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.settings_model)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    5. **Input arguments**  
        This hook has no input arguments.

        !!! info

            Useful to load settings via API and do custom stuff. E.g. load from a MongoDB instance.

        ??? example

            ```python
            from pymongo import MongoClient

            @plugin
            def load_settings():
                client = MongoClient('mongodb://your_mongo_instance/')
                db = client['your_mongo_db']
                collection = db['your_settings_collection']

                # Perform the find_one query
                settings = collection.find_one({'_id': "your_plugin_id"})

                client.close()

                return MySettings(**settings)

            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.load_settings)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    6. **Input arguments**  
        `settings`: the settings `Dict` to be saved.

        !!! info

            Useful for customizing the settings saving strategy. E.g. storing settings in a MongoDB instance.

        ??? example

            ```python
            from pymongo import MongoClient

            @plugin
            def save_settings(settings):
                client = MongoClient('mongodb://your_mongo_instance/')
                db = client['your_mongo_db']
                collection = db['your_settings_collection']

                # Generic filter based on a unique identifier in settings
                filter_id = {'_id': settings.get('_id', 'your_plugin_id')}

                # Define the update operation
                update = {'$set': settings}

                # Perform the upsert operation
                collection.update_one(filter_id, update, upsert=True)
                
                client.close()

            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.save_settings)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    > ***NOTE:***  Any function in a plugin decorated by `@plugin` and named properly (among the list of available overrides, **Plugin** tab in the table above) is used to override plugin behaviour. These are not hooks because they are not piped, they are *specific* for every plugin.

=== "&#127981; Factory"


    ```mermaid
        flowchart TD
            A(factory_allowed_llms)
            B(factory_allowed_embedders)
            C(factory_allowed_auth_handlers)

            A --> B
            B --> C

            click A "/docs/plugins/hooks-reference/factory/factory_allowed_llms"
            click B "/docs/plugins/hooks-reference/factory/factory_allowed_embedders"
            click C "/docs/plugins/hooks-reference/factory/factory_allowed_auth_handlers"
    ```

=== "&#x1F493; Lifecycle"

    ```mermaid
    flowchart TD
        B(before_cat_bootstrap)
        C(after_cat_bootstrap)
        B -- Cat components are loaded --> C
        
        click B "/docs/plugins/hooks-reference/lifecycle/before_cat_bootstrap"
        click C "/docs/plugins/hooks-reference/lifecycle/after_cat_bootstrap"
    ```


## How the Hooks work

To create a hook, you first need to create a [plugin](plugins.md) that contains it. Once the plugin is created, you can insert hooks inside the plugin, a single plugin can contain multiple hooks.

A hook is simply a Python function that uses the `@hook` decorator, the function's name determines when it will be called.

Each hook has its own signature name and arguments, the last argument being always `cat`, while the first one depends on the type of hook you're using.
Have a look at the table with all the [available hooks](#available-hooks) and their [detailed reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/agent/).

## Hook declaration

The Cat comes already with a hook that defines his behaviour.  
Let's take a look at it.
```python
@hook
def agent_prompt_prefix(prefix, cat):
    """Hook the main prompt prefix. """
    prefix = """You are the Cheshire Cat AI, an intelligent AI that passes 
             the Turing test. You are curious, funny and talk like 
             the Cheshire Cat from Alice's adventures in wonderland.
             You answer Human with a focus on the following context."""

    return prefix
```
This hook returns the default prefix that describes who the AI is and how it is expected to answer the Human.
### Hook arguments

When considering hooks' arguments, remember:

- `cat` will always be present, as it allows you to use the framework components. It will be always the last one. See [here](../framework/cat-components/cheshire_cat/stray_cat.md) for details and examples.
    ```python
    @hook
    def hook_name(cat):
        pass
    ```
- the first argument other than `cat`, if present, will be a variable that you can edit and return back to the framework. Every hook passes a different data structure, which you need to know and be able to edit and return.
    ```python
    @hook
    def hook_name(data, cat):
        # edit data and return it
        data.answer = "42"
        return data
    ```
    You are free to return nothing and use the hook as a simple event callback.
    ```python
    @hook
    def hook_name(data, cat):
        do_my_thing()
    ```
- other arguments may be passed, serving only as additional context.
    ```python
    @hook
    def hook_name(data, context_a, context_b, ..., cat):
        if context_a == "Caterpillar":
            data.answer = "U R U"
        return data
    ```

## Examples

### Before cat bootstrap

You can use the `before_cat_bootstrap` hook to execute some operations before the Cat starts:

```python
from cat.mad_hatter.decorators import hook

@hook
def before_cat_bootstrap(cat):
    do_my_thing()
```

Notice in this hook there is only the `cat` argument, allowing you to use the llm and access other Cat components.  
This is a pure event, with no additional arguments.

### Before cat sends message

You can use the `before_cat_sends_message` hook to alter the message that the Cat will send to the user.
In this case you will receive both `final_output` and `cat` as arguments.

```python
from cat.mad_hatter.decorators import hook

@hook
def before_cat_sends_message(final_output, cat):
    # You can edit the final_output the Cat is about to send back to the user
    final_output.content = final_output.content.upper()
    return final_output
```


## Hooks chaining and priority

Several plugins can implement the same hook. The argument `priority` of the `@hook` decorator allows you to set the priority of the hook, the default value is 1.

```python
@hook(priority=1) # same as @hook without priority
def hook_name(data, cat):
    pass
```

The Cat calls hooks with the same name in order of `priority`. Hooks with a higher priority number will be called first. The following hook will receive the value returned by the previous hook. In this way, hooks can be chained together to create complex behaviors.

```python
# plugin A
@hook(priority=5)
def hook_name(data, cat):
    data.content += "Hello"
    return data
```

```python
# plugin B
@hook(priority=1)
def hook_name(data, cat):
    if "Hello" in data.content:
        data.content += " world"
    return data
```

If two plugins have the same priority, the order in which they are called is not guaranteed.

## Custom hooks in plugins

You can define your own hooks, so other plugins can listen and interact with them.

```python
# plugin cat_commerce
@hook
def before_cat_reads_message(msg, cat):
    default_order = [
        "wool ball",
        "catnip"
    ]
    chain_output = cat.mad_hatter.execute_hook(
        "cat_commerce_order", default_order, cat=cat
    )
    do_my_thing(chain_output)
```

Other plugins may be able to edit or just track the event:

```python
# plugin A
@hook
def cat_commerce_order(order, cat):
    if "catnip" in order:
        order.append("free teacup")
    return order
```

```python
# plugin B
@hook
def cat_commerce_order(order, cat):
    if len(order) > 1:
        # updating working memory
        cat.working_memory.bank_account = 0
        # send websocket message
        cat.send_ws_message("Cat is going broke")
```

