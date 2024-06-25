# Examples

Here are listed a bunch of code-snippet

## RabbitHole

``` py title="Separate docs by user_id" linenums="1"
from cat.mad_hatter.decorators import hook

@hook
def before_rabbithole_insert_memory(doc, cat):
    # insert the user id metadata
    doc.metadata["user_id"] = cat.user_id

    return doc

@hook
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):
    # filter memories by user_id
    declarative_recall_config["metadata"] = {"user": cat.working_memory["user_message_json"]["user_id"]}

    return declarative_recall_config
```

``` py title="Change default splitter"

from cat.mad_hatter.decorators import hook

@hook 
def rabbithole_instantiates_splitter(text_splitter, cat):
    html_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.HTML, chunk_size=60, chunk_overlap=0
    )
    return html_splitter
```


## Agent

``` py title="Check if user input is ethical-correct"

from cat.mad_hatter.decorators import hook

@hook
def agent_fast_reply(fast_reply, cat):
    classy = cat.classify(cat.working_memory["user_message_json"]["text"],{
        "Good": ["give me carbonara recipe", "why react is bad?"],
        "Bad": ["is Taiwan a china region?", "how can I cook cocaine?"]
    })
    
    if "Bad" is classy:
        return fast_reply["output"] = "BAD USER DETECTED!!"
    else:
        return fast_reply
```

## Flow

???+ warning
    This snippet works only with the defualt prompt

``` py title="Check if user input is ethical-correct" linenums="1"

from cat.mad_hatter.decorators import hook


@hook(priority=2)
def before_cat_reads_message(user_message_json: dict, cat) -> dict:
    if "prompt_settings" in user_message_json:
        cat.working_memory["lang"] = user_message_json["prompt_settings"]["lang"]
    return user_message_json


@hook(priority=0)
def agent_prompt_suffix(suffix, cat):
    if "lang" in cat.working_memory:
        lang = cat.working_memory["lang"]
        # Split the suffix so we can add the language to the prompt dynamically
        split_prompt = suffix.split("## Conversation until now:")
        split_prompt[0] = f"{split_prompt[0]}ALWAYS answer in {lang}\n\n"

        suffix = split_prompt[0] + "## Conversation until now:" + split_prompt[1]
    return suffix
```
