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
    
    1. **Input arguments**  
        This hook has no input arguments.  

        ??? example
    
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_bootstrap(cat):
                # do whatever here
            ```

        ??? warning

            Please, note that at this point the `CheshireCat` hasn't yet finished to instantiate
            and the only already existing component is the `MadHatter` (e.g. no language models yet).
    
        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_bootstrap)
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.after_cat_bootstrap)

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
                cat.working_memory["hacked"] = True

                return user_message_json
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_reads_message)

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
        
            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.cat_recall_query)
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_memories)

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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_episodic_memories)
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_declarative_memories)
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_procedural_memories)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    9. **Input arguments**  
        This hook has no input arguments.

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
    
            @hook  # default priority = 1
            def before_cat_recalls_memories(cat):
                # do whatever here
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.after_cat_recalls_memories)

    10. **Input arguments**  
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_sends_message)

=== "&#129302; Agent"
    
    <div class="annotate" mardown>

    | Name                          | Description                                                                      |
    | :---------------------------- | :------------------------------------------------------------------------------- |
    | Before agent starts (1)       | Intervene before the agent starts                                                |
    | Agent fast reply (2)          | Shorten the pipeline and returns an answer right after the agent execution       |
    | Agent prompt prefix (3)       | Intervene while the agent manager formats the Cat's personality                  |
    | Agent prompt suffix (4)       | Intervene while the agent manager formats the prompt suffix with the memories and the conversation history |
    | Agent allowed tools (5)       | Intervene before the recalled tools are provided to the agent                    |
    | Agent prompt instructions (6) | Intervent while the agent manager formats the reasoning prompt                   |

    </div>

    1. **Input arguments**  
        `agent_input`: dictionary with the information to be passed to the agent. E.g.:

        ```python
        {
            "input": working_memory["user_message_json"]["text"],  # user's message
            "episodic_memory": episodic_memory_formatted_content,  # strings with documents recalled from memories
            "declarative_memory": declarative_memory_formatted_content,
            "chat_history": conversation_history_formatted_content,
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
                
                return anget_input
            ```

        ??? note "Other resources"
        
            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.before_agent_starts)

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
                if len(cat.working_memory["declarative_memories"]) == 0:
                    fast_reply["output"] = "Sorry, I'm afraid I don't know the answer"

                return fast_reply
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.agent_fast_reply)
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
                        you suffer.
            ```
            
        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_prefix)

    4. **Input arguments**  
        `prompt_suffix`: string with the ending part of the prompt containing the memories and the chat history.
        Default is:

        ```python
        prompt_suffix = """
        # Context
        
        {episodic_memory}
        
        {declarative_memory}
        
        {tools_output}
        
        ## Conversation until now:{chat_history}
         - Human: {input}
         - AI: 
        """
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_prompt_suffix(prompt_suffix, cat):
                # tell the LLM to always answer in a specific language
                prompt_suffix = """ 
                # Context
        
                {episodic_memory}
                
                {declarative_memory}
                
                {tools_output}
                
                ALWAYS answer in Czech!

                ## Conversation until now:{chat_history}
                 - Human: {input}
                   - AI: 
                """
            ```

        !!! warning

            The placeholders `{episodic_memory}`, `{declarative_memory}`, `{tools_output}`,
            `{chat_history}` and `{input}` are mandatory!

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_suffix)
            - [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools)

    5. **Input arguments**  
        `allowed_tools`: list with string names of the tools retrieved from the memory. E.g.:

        ```python
        allowed_tools = ["get_the_time"]
        ```

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_allowed_tools(allowed_tools, cat):
                # let's assume there is a tool we always want to give the agent
                # add the tool name in the list of allowed tools
                allowed_tools.append("blasting_hacking_tool")

                return allowed_tools
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/agent/#cat.mad_hatter.core_plugin.hooks.agent.agent_allowed_tools)

    6. **Input arguments**  
        `instructions`: string with the reasoning template. Default is:

        ```python
        Answer the following question: `{input}`
        You can only reply using these tools:
        
        {tools}
        none_of_the_others: none_of_the_others(None) - Use this tool if none of the others tools help. Input is always None.
        
        If you want to use tools, use the following format:
        Action: the name of the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ...
        Action: the name of the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        
        When you have a final answer respond with:
        Final Answer: the final answer to the original input question
        
        Begin!
        
        Question: {input}
        {agent_scratchpad}
        ```

        !!! warning

            The placeholders `{input}`, `{tools}` and `{tool_names}` are mandatory!

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def agent_prompt_instructions(instructions, cat):
                # let's ask the LLM to translate the tool output
                instructions += "\nAlways answer in mandarin"
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/prompt/#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_instructions)

=== "&#128048; Rabbit Hole"
    
    <div class="annotate" mardown>

    | Name                                      | Description                                                    |
    | :---------------------------------------- | :------------------------------------------------------------- |
    | Rabbit Hole instantiates parsers (1)      | Intervene before the files' parsers are instiated              |
    | Before Rabbit Hole insert memory (2)      | Intervene before the Rabbit Hole insert a document in the declarative memory |
    | Before Rabbit Hole splits text (3)        | Intervene before the uploaded document is split into chunks    |
    | After Rabbit Hole splitted text (4)       | Intervene after the Rabbit Hole's split the document in chunks |
    | Before Rabbit Hole stores documents (5)   | Intervene before the Rabbit Hole starts the ingestion pipeline |

    </div>

    1. **Input arguments**  
        `file_handlers`: dictionary with mime types and related file parsers. Default is:

        ```python
        {
            "application/pdf": PDFMinerParser(),  # pdf parser
            "text/plain": TextParser(),  # txt parser
            "text/markdown": TextParser(),  # md parser fallback to txt parser
            "text/html": BS4HTMLParser()  # html parser
        }
        ```

        ??? example

            ```python
            from langchain.document_loaders.parsers.txt import TextParser
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def rabbithole_instantiates_parsers(file_handlers, cat):
                # use the txt parser to parse also .odt files
                file_handlers["application/vnd.oasis.opendocument.text"] = TextParser()

                return file_handlers
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.rabbithole_instantiates_parsers)
            - [IngestAnything plugin](https://github.com/Furrmidable-Crew/IngestAnything)

    2. **Input arguments**  
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
            
            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_insert_memory)
            - [RabbitHole segmentation plugin](https://github.com/team-sviluppo/cc_rabbithole_segmentation)
            - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)

    3. **Input arguments**  
        `doc`: Langchain document with full text. E.g.

        ```python
        doc = Document(page_content="This is a very long document before being split", metadata={})
        ```

        ??? example
        
            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def before_rabbithole_splits_text(doc, cat):
                # do whatever with the doc
                return doc
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_splits_text)

    4. **Input arguments**  
        `chunks`: list of Langchain documents with text chunks.

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook
            
            @hook  # default priority = 1
            def after_rabbithole_splitted_text(chunks, cat):
                # post process the chunks
                edited_chunks = []
                for chunk in chunks:
                    new_chunk = cat.llm(f"Replace any dirty word with 'Meow': {chunk}")
                    edited_chunks.append(new_chunk)

                return edited_chunks
            ```

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.after_rabbithole_splitted_text)

    5. **Input arguments**  
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole/#cat.mad_hatter.core_plugin.hooks.rabbithole.before_rabbithole_stores_documents)
            - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)

=== "&#128268; Plugin"
    
    <div class="annotate" mardown>

    | Name                | Description                                        |
    | :-------------------| :------------------------------------------------- |
    | Activated (1)       | Intervene when a plugin is enabled                 |
    | Deactivated (2)     | Intervene when a plugin is disabled                |
    | Settings schema (3) | Override how the plugin's settings are retrieved   |
    | Settings model (4)  | Override how the plugin's settings are retrieved   |
    | Load settings (5)   | Override how the plugin's settings are loaded      |
    | Save settings (6)   | Override how the plugin's settings are saved       |

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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.activated)
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

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.deactivated)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    3. **Input arguments**  
        This hook has no input arguments.

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from pydantic import BaseModel, Field

            # define your plugin settings model
            class MySettings(BaseModel):
            text_field: str = Field(
                title="Your field title",
                description="Your field description",
                default="""default value""",
                extra={"type": "Text"}
            )
            bool_field: bool = Field(
            default=True,
            title="Your field title",
            )
            int_field: int = 3

            # get your plugin settings schema
            @plugin
            def settings_schema():
                return MySettings.model_json_schema()

            # load your plugin settings
            settings = ccat.mad_hatter.get_plugin().load_settings()
            # access settings
            text_field = settings["text_field"]
            bool_field = settings["bool_field"]
            int_field = settings["int_field"]
            ```

        ??? warning

            Note that `settings["field_name"]` works if you have a `settings.json` file in your plugin folder,
            otherwise you get `KeyError`.

            You can solve that by:

            1. creating a default `settings.json` file
            2. using a `try-catch` block when accessing plugin settings

            Soon, `settings.json` will be created by the cat core for the *settings fields* with default values only.
    
        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.settings_schema)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    4. **Input arguments**  
        This hook has no input arguments.

        ??? example

            ```python
            from cat.mad_hatter.decorators import plugin
            from pydantic import BaseModel, Field

            # define your plugin settings model
            class MySettings(BaseModel):
            text_field: str = Field(
                title="Your field title",
                description="Your field description",
                default="""default value""",
                extra={"type": "Text"}
            )
            bool_field: bool = Field(
            default=True,
            title="Your field title",
            )
            int_field: int = 3

            # get your plugin settings Pydantic model
            @plugin
            def settings_model():
                return MySettings

            # load your plugin settings
            settings = ccat.mad_hatter.get_plugin().load_settings()
            # access settings
            text_field = settings["text_field"]
            bool_field = settings["bool_field"]
            int_field = settings["int_field"]
            ```

        ??? warning

            Note that `settings_model` is preferred to `settings_schema`.

            Consider that `settings["field_name"]` works if you have a `settings.json` file in your plugin folder,
            otherwise you get `KeyError`.

            You can solve that by:

            1. creating a default `settings.json` file
            2. using a `try-catch` block when accessing plugin settings

            Soon, `settings.json` will be created by the cat core for the *settings fields* with default values only.

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.settings_model)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    5. **Input arguments**  
        This hook has no input arguments.

        ??? example

            ```python
            @plugin
            def load_settings():
                return MySettings
            ```

        ??? warning

            Useful to load settings via API and do custom stuff.

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.load_settings)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

    6. **Input arguments**  
        `settings`: the settings `Dict` to be saved

        ??? example

            ```python
            @plugin
            def save_settings():
                return MySettings
            ```

        ??? warning

            Useful to load settings via API and do custom stuff.

        ??? note "Other resources"

            - [Python reference](https://cheshire-cat-ai.github.io/docs/technical/API_Documentation/mad_hatter/core_plugin/settings/#cat.mad_hatter.core_plugin.settings.save_settings)
            - [Plugin object](https://github.com/cheshire-cat-ai/core/blob/main/core/cat/mad_hatter/plugin.py#L25)

> **_NOTE:_**  Any function in a plugin decorated by `@plugin` and named properly (among the list of available overrides, **Plugin** tab in the table above) is used to override plugin behaviour. These are not hooks because they are not piped, they are *specific* for every plugin.
