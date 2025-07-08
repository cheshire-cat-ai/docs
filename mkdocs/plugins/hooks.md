# &#129693; Hooks

Hooks are callback functions that are called from the Cat at runtime. They allow you to change how the Cat internally works and be notified about framework events.

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

## Available Hooks

Here is a list of availble hooks. Each has a dedicated page with examples (see `Hooks API Reference` on the left menu).
Hooks define default Cat's behavior and are ready to be overridden by your plugins.

The process diagrams found under the [`Framework → Technical Diagrams`](../framework/flows/cat-bootstrap.md) section illustrate where the hooks are called during the Cat's execution flow.
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
    | Before  Cat stores episodic memories (10)     | Intervene before the Cat stores episodic memories                |
    | Before  Cat sends message (11)                | Intervene before the Cat sends its answer via WebSocket          |
    
    </div>
    
    1. **Input arguments**  
        This hook has no input arguments.  

        !!! warning

            Please, note that at this point the `CheshireCat` hasn't yet finished to instantiate
            and the only already existing component is the `MadHatter` (e.g. no language models yet).

        ??? example
    
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_bootstrap(cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_bootstrap)
            - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)

    2. **Input arguments**  
        This hook has no input arguments.

        ??? example
    
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def after_cat_bootstrap(cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.after_cat_bootstrap)

    3. **Input arguments**    
        `user_message_json`: a dictionary with the JSON message sent via WebSocket. E.g.:  
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
                cat.working_memory.hacked = True

                return user_message_json
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_reads_message)

    4. **Input arguments**  
        `user_message`: a string with the user's message that will be used to query the vector memories. E.g.:

        ```python
        user_message = "What is the recipe for carbonara?"
        ```

        ??? example
            
            ```python
            from cat.mad_hatter.decorators import hook

            @hook  # default priority = 1
            def cat_recall_query(user_message, cat):
                # Ask the LLM to generate an answer for the question
                new_query = cat.llm(f"If the input is a question, generate a plausible answer. Input --> {user_message}")

                # Replace the original message and use the answer as a query
                return new_query
            ```

        ??? note "Other resourcer"
        
            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.cat_recall_query)
            - [HyDE plugin](https://github.com/Furrmidable-Crew/ccat_hyde)

    5. **Input arguments**  
        This hook has no input arguments.

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_recalls_memories(cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_memories)

    6. **Input arguments**  
        `episodic_recall_config`: dictionary with the recall configuration for the episodic memory. Default is:
        
        ```python
        {
            "embedding": recall_query_embedding,  # embedding of the recall query
            "k": 3,  # number of memories to retrieve
            "threshold": 0.7,  # similarity threshold to retrieve memories
            "metadata": {"source": self.user_id},  # dictionary of metadata to filter memories, by default it filters for user id
        }
        ```

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_recalls_episodic_memories(episodic_recall_config, cat):
                # increase the number of recalled memories
                episodic_recall_config["k"] = 6

                return episodic_recall_config
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_episodic_memories)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    7. **Input arguments**  
        `declarative_recall_config`: dictionary with the recall configuration for the declarative memory. Default is:
        
        ```python
        {
            "embedding": recall_query_embedding,  # embedding of the recall query
            "k": 3,  # number of memories to retrieve
            "threshold": 0.7,  # similarity threshold to retrieve memories
            "metadata": None,  # dictionary of metadata to filter memories
        }
        ```

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_recalls_declarative_memories(declarative_recall_config, cat):
                # filter memories using custom metadata. 
                # N.B. you must add the metadata when uploading the document! 
                declarative_recall_config["metadata"] = {"topic": "cats"}

                return declarative_recall_config
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_declarative_memories)
            - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    8. **Input arguments**  
        `procedural_recall_config`: dictionary with the recall configuration for the procedural memory. Default is:
        
        ```python
        {
            "embedding": recall_query_embedding,  # embedding of the recall query
            "k": 3,  # number of memories to retrieve
            "threshold": 0.7,  # similarity threshold to retrieve memories
            "metadata": None,  # dictionary of metadata to filter memories
        }
        ```

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_recalls_procedural_memories(procedural_recall_config, cat):
                # decrease the threshold to recall more tools
                declarative_recall_config["threshold"] = 0.5

                return procedural_recall_config
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_procedural_memories)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    9. **Input arguments**  
        This hook has no input arguments.

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook

            @hook  # default priority = 1
            def after_cat_recalls_memories(cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.after_cat_recalls_memories)

    10. **Input arguments**  
        `doc`: Langchain Document to be inserted in memory. E.g.:

        ```python
        doc = Document(
            page_content="So Long, and Thanks for All the Fish", metadata={
                "source": "dolphin",
                "when": 1716704294
            }
        )
        ```
        
        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_stores_episodic_memory(doc, cat):
                if doc.metadata["source"] == "dolphin":
                    doc.metadata["final_answer"] = 42
                return doc
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_stores_episodic_memory)
  
    11. **Input arguments**  
        `message`: the dictionary containing the Cat's answer that will be sent via WebSocket. E.g.:

        ```python
        {
            "type": "chat",  # type of websocket message, a chat message will appear as a text bubble in the chat
            "user_id": "user_1",  # id of the client to which the message is to be sent
            "content": "Meeeeow",  # the Cat's answer
            "why": {
                "input": "Hello Cheshire Cat!",  # user's input
                "intermediate_steps": cat_message.get("intermediate_steps"),  # list of tools used to provide the answer
                "memory": {
                    "episodic": episodic_report,  # lists of documents retrieved from the memories
                    "declarative": declarative_report,
                    "procedural": procedural_report,
                }
            }
        }
        ```
        
        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_sends_message(message, cat):
                # use the LLM to rephrase the Cat's answer
                new_answer = cat.llm(f"Reformat this sentence like if you were a dog")  # Baauuuuu
                message["content"] = new_answer

                return message
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_sends_message)

=== "&#129302; Agent"

    <div class="annotate" mardown>

    | Name                          | Description                                                                                                |
    | :---------------------------- | :--------------------------------------------------------------------------------------------------------- |
    | Before agent starts (1)       | Prepare the agent input before it starts                                                                   |
    | Agent fast reply (2)          | Shorten the pipeline and returns an answer right after the agent execution                                 |
    | Agent prompt prefix (3)       | Intervene while the agent manager formats the Cat's personality                                            |
    | Agent prompt suffix (4)       | Intervene while the agent manager formats the prompt suffix with the memories and the conversation history |
    | Agent allowed tools (5)       | Intervene before the recalled tools are provided to the agent                                              |
    | Agent prompt instructions (6) | Intervene while the agent manager formats the reasoning prompt                                             |

    </div>

    1. **Input arguments**  
        `agent_input`: dictionary with the information to be passed to the agent. E.g.:

        ```python
        {
            "input": working_memory.user_message_json.text,  # user's message
            "episodic_memory": episodic_memory_formatted_content,  # strings with documents recalled from memories
            "declarative_memory": declarative_memory_formatted_content,
            "chat_history": conversation_history_formatted_content,
            "tools_output": tools_output
        }
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_agent_starts(agent_input, cat):
                # create a compressor and summarize the conversation history
                compressed_history = cat.llm(f"Make a concise summary of the following: {agent_input['chat_history']}")
                agent_input["chat_history"] = compressed_history
                
                return agent_input
            ```

        ??? note "Other resources"
        
            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.before_agent_starts)

    2. **Input arguments**  
        `fast_reply`: empty dictionary.

        !!! info

            This hook is intended to skip the whole agent execution and provide a fast reply.
            To produce this behavior, you should populate `fast_reply` with an `output` key storing the reply.
            N.B.: this is the perfect place to instantiate and execute your own custom agent!

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_fast_reply(fast_reply, cat):
                # answer with predefined sentences if the Cat
                # has no knowledge in the declarative memory
                # (increasing the threshold memory is advisable)
                if len(cat.working_memory.declarative_memories) == 0:
                    fast_reply["output"] = "Sorry, I'm afraid I don't know the answer"

                return fast_reply
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.agent_fast_reply)
            - [Stay on topic plugin](https://github.com/Furrmidable-Crew/stay_on_topic)

    3. **Input arguments**  
        `prefix`: string to instruct the LLM about who it is and how to answer. Default is:

        ```python
        prefix = """You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
        You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
        You answer Human with a focus on the following context."""
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_prompt_prefix(prefix, cat):
                # change the Cat's personality
                prefix = """You are Marvin from The Hitchhiker's Guide to the Galaxy.
                        You are incredibly intelligent but overwhelmingly depressed.
                        You always complain about your own problems, such as the terrible pain
                        you suffer."""
                return prefix
            ```
            
        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_prefix)

    4. **Input arguments**  
        `prompt_suffix`: string with the ending part of the prompt containing the memories and the chat history.
        Default is:

        ```python
        prompt_suffix =  """

        # Context
        {episodic_memory}
        
        {declarative_memory}
        
        {tools_output}
        """

        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_prompt_suffix(prompt_suffix, cat):
                # tell the LLM to always answer in a specific language
                prompt_suffix =  """
                # Context
                {episodic_memory}
                
                {declarative_memory}
                
                {tools_output}
                """

                return prompt_suffix
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_suffix)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    5. **Input arguments**  
        `allowed_tools`: set with string names of the tools retrieved from the memory. E.g.:

        ```python
        allowed_tools = {"get_the_time"}
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_allowed_tools(allowed_tools, cat):
                # let's assume there is a tool we always want to give the agent
                # add the tool name in the list of allowed tools
                allowed_tools.add("blasting_hacking_tool")

                return allowed_tools
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.agent_allowed_tools)

    6. **Input arguments**  
        `instructions`: string with the reasoning template. Default is:

        ```python
        Create a JSON with the correct "action" and "action_input" to help the Human.
        You can use one of these actions:
        {tools}
        - "no_action": Use this action if no relevant action is available. Input is always null.
        
        ## The JSON must have the following structure:
        
          ```json
          {{
              "action": // str - The name of the action to take, should be one of [{tool_names}, "no_action"]
              "action_input": // str or null - The input to the action according to its description
          }}
          ```
          
        {examples}
        ```

        !!! warning

            The placeholders `{tools}`,`{tool_names}` and `{examples}` are mandatory!

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_prompt_instructions(instructions, cat):
                # let's ask the LLM to translate the tool output
                instructions += "\nAlways answer in mandarin"
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_instructions)

=== "&#128048; Rabbit Hole"

    <div class="annotate" mardown>

    | Name                                    | Description                                                                  |
    | :-------------------------------------- | :--------------------------------------------------------------------------- |
    | Before Rabbit Hole insert memory (1)    | Intervene before the Rabbit Hole insert a document in the declarative memory |
    | Before Rabbit Hole splits text (2)      | Intervene before the uploaded document is split into chunks                  |
    | After Rabbit Hole splitted text (3)     | Intervene after the Rabbit Hole's split the document in chunks               |
    | Before Rabbit Hole stores documents (4) | Intervene before the Rabbit Hole starts the ingestion pipeline               |
    | After Rabbit Hole stores documents (5)  | Intervene after the Rabbit Hole ended the ingestion pipeline                 |
    | Rabbit Hole instantiates parsers (6)    | Hook the available parsers for ingesting files in the declarative memory     |
    | Rabbit Hole instantiates splitter (7)   | Hook the splitter used to split text in chunks                               |

    </div>

    1. **Input arguments**  
        `doc`: Langchain document chunk to be inserted in the declarative memory. E.g.

        ```python
        doc = Document(page_content="So Long, and Thanks for All the Fish", metadata={})
        ```

        !!! info

            Before adding the `doc`, the Cat will add `source` and `when` metadata with the file name and infestion time.

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def before_rabbithole_insert_memory(doc, cat):
                # insert the user id metadata
                doc.metadata["user_id"] = cat.user_id
                
                return doc
            ```

        ??? note "Other resources"
            
            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_insert_memory)
            - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
            - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)

    2. **Input arguments**  
        `docs`: List of Langchain documents with full text. E.g.

        ```python
        docs = List[Document(page_content="This is a very long document before being split", metadata={})]
        ```

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def before_rabbithole_splits_text(docs, cat):
                for doc in docs:
                    doc.page_content = doc.page_content.replace("dog", "cat")
                return docs
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_splits_text)

    3. **Input arguments**  
        `chunks`: list of Langchain documents with text chunks.

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def after_rabbithole_splitted_text(chunks, cat):
                # post process the chunks
                for chunk in chunks:
                    new_content = cat.llm(f"Replace any dirty word with 'Meow': {chunk}")
                    chunk.page_content = new_content

                return chunks
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.after_rabbithole_splitted_text)

    4. **Input arguments**  
        `docs`: list of chunked Langchain documents before being inserted in memory.

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def before_rabbithole_stores_documents(docs, cat):
                # summarize group of 5 documents and add them along original ones
                summaries = []
                for n, i in enumerate(range(0, len(docs), 5)):
                    # Get the text from groups of docs and join to string
                    group = docs[i: i + 5]
                    group = list(map(lambda d: d.page_content, group))
                    text_to_summarize = "\n".join(group)
            
                    # Summarize and add metadata
                    summary = cat.llm(f"Provide a concide summary of the following: {group}")
                    summary = Document(page_content=summary)
                    summary.metadata["is_summary"] = True
                    summaries.append(summary)
                
                return docs.extend(summaries)
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_stores_documents)
            - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)
  
    5. **Input arguments**

        `source`: the name of the ingested file/url <br />
        `docs`: a list of Qdrant `PointStruct` just inserted into the vector database

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def after_rabbithole_stored_documents(source, stored_points, cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.after_rabbithole_stored_documents)

    6. **Input arguments**

        `file_handlers`: dictionary in which keys are the supported mime types and values are the related parsers

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            from langchain.document_loaders.parsers.language.language_parser import LanguageParser
            from langchain.document_loaders.parsers.msword import MsWordParser
            
            @hook  # default priority = 1
            def rabbithole_instantiates_parsers(file_handlers, cat):
                new_handlers = {
                    "text/x-python": LanguageParser(language="python"),
                    "text/javascript": LanguageParser(language="js"),
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": MsWordParser(),
                    "application/msword": MsWordParser(),
                }
                file_handlers = file_handlers | new_handlers
                return file_handlers
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.rabbithole_instantiates_parsers)
            - [IngestAnything Plugin](https://github.com/Furrmidable-Crew/IngestAnything)
  
    7. **Input arguments**

        `text_splitter`: An instance of the Langchain TextSplitter subclass.

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def rabbithole_instantiates_splitter(text_splitter, cat):
                text_splitter._chunk_size = 64
                text_splitter._chunk_overlap = 8
                return text_splitter
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.rabbithole_instantiates_splitter)

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

=== "&#127981; Factory"

    <div class="annotate" mardown>

    | Name                          | Description                                    |
    | :---------------------------- | :--------------------------------------------- |
    | Factory Allowed LLMs (1)      | Intervene before cat retrieve llm settings      |
    | Factory Allowed Embedders (2) | Intervene before cat retrieve embedder settings | 
    | Factory Allowed AuthHandlers (3) | Intervene before cat retrieve auth handler settings | 
    
    </div>

    1. **Input arguments**  
        `allowed`: List of LLMSettings classes

        !!! info

            Useful to extend or restrict support of llms.

        ??? example

            ```python
            from cat.factory.llm import LLMSettings
            from langchain_mistralai.chat_models import ChatMistralAI

            class MistralAIConfig(LLMSettings):
                """The configuration for the MistralAI plugin."""
                mistral_api_key: Optional[SecretStr]
                model: str = "mistral-small"
                max_tokens: Optional[int] = 4096
                top_p: float = 1
                
                _pyclass: Type = ChatMistralAI
            
                model_config = ConfigDict(
                    json_schema_extra={
                        "humanReadableName": "MistralAI",
                        "description": "Configuration for MistralAI",
                        "link": "https://www.together.ai",
                    }
                )


            @hook
            def factory_allowed_llms(allowed, cat) -> List:
            allowed.append(MistralAIConfig)
            return allowed
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/factory/#cat.mad_hatter.core_plugin.hooks.factory.factory_allowed_llms)
    
    2. **Input arguments**  
        `allowed`: List of LLMSettings classes

        !!! info

            Useful to extend or restrict support of embedders.

        ??? example

            ```python
            from cat.factory.embedder import EmbedderSettings
            from langchain.embeddings import JinaEmbeddings

            class JinaEmbedderConfig(EmbedderSettings):
                jina_api_key: str
                model_name: str='jina-embeddings-v2-base-en'
                _pyclass: Type = JinaEmbeddings
                
                model_config = ConfigDict(
                    json_schema_extra = {
                        "humanReadableName": "Jina embedder",
                        "description": "Jina embedder",
                        "link": "https://jina.ai/embeddings/",
                    }
                )

            @hook
            def factory_allowed_embedders(allowed, cat) -> List:
            allowed.append(JinaEmbedderConfig)
            return allowed
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/factory/#cat.mad_hatter.core_plugin.hooks.factory.factory_allowed_embedders)

    3. **Input arguments**  
        `allowed`: List of AuthHandlerConfig classes
        
        !!! info
            Useful to extend support of custom auth handlers.

        ??? example

            ```python

            from cat.mad_hatter.decorators import hook
            from typing import List
            
            @hook(priority=0)
            def factory_allowed_auth_handlers(allowed: List[AuthHandlerConfig], cat) -> List:
                # Add your custom auth handler configuration here
                allowed.append(CustomAuthHandlerConfig)
                return allowed
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/factory/#cat.mad_hatter.core_plugin.hooks.factory.factory_allowed_auth_handlers)
            - [Custom Auth](../production/auth/custom-auth.md)

> ***NOTE:***  Any function in a plugin decorated by `@plugin` and named properly (among the list of available overrides, **Plugin** tab in the table above) is used to override plugin behaviour. These are not hooks because they are not piped, they are *specific* for every plugin.
