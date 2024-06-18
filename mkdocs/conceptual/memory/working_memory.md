# Working Memory

## Introduction

The Working Memory is a crucial component for storing temporary data. It can be used to share data across plugins or any function that receives an instance of the Cat as an argument.

By default, the Working Memory stores the *chat history* that ends up in the [Main Prompt](../prompts/main_prompt.md).
Additionally, it collects relevant context from the *episodic*, *declarative* and
*procedural* memories in the [Long Term Memory](long_term_memory.md).

The Working Memory can be used also to store custom data during a session. This capability is essential for creating a [state machine](#use-the-working-memory-as-a-state-machine) within your own plugin.

![Schema of the Cheshire Cat memories](../../assets/img/diagrams/working-memory.jpg){width=500px style="display: block; margin: 0 auto"}

## Interacting with the Working Memory

As mentioned above, the Working Memory is a key component in the Cheshire Cat framework and can be leveraged within your own plugins.

Whenever you have a StrayCat instance, you can access the Working Memory through the `working_memory` property, like so:

```python
from cat.mad_hatter.decorators import hook

@hook
def agent_fast_reply(fast_reply, cat):
    if len(cat.working_memory.declarative_memories) == 0:
        fast_reply["output"] = "Sorry, I'm afraid I don't know the answer"

    return fast_reply
```

The `working_memory` property returns an instance of the `WorkingMemory` class, which acts as a key-value store with a dual nature. It can store data as key-value pairs like a dictionary and also benefit from Pydantic's data validation and serialization features for its default properties.

This flexibility allows you to access and set attributes using dot notation, creating and assigning arbitrary attributes on the fly. This makes the Working Memory highly adaptable for handling dynamic data structures.

## Use the Working Memory as a State Machine

One of the most powerful features of the Working Memory is its ability to function as a state machine.

Each time you send a message to the Cat, it stores useful data in the Working Memory, which can be retrieved to produce the output for the next message. This, along with the ability to store custom data throughout the session, is the key to implementing your specific agent in a more programmatic way.

An example of this usage in the Cheshire Cat is the [Conversational Form](../../technical/plugins/forms.md) which provides a well-crafted and comprehensive state machine to guide both the user and LLM during the conversation.

### Example of the Working Memory as a State Machine

Given that the Conversational Form state-machine implementation is quite advanced, let's create a simpler example: a technical support agent for the Cheshire Cat.

First of all, we need to create a new plugin. [Plugin? Is that some kind of exotic dish?](../../quickstart/prepare-plugin.md)

Once there, we need to define what are the states of our conversation. This can be done by creating a `SupportRequest` enum. Like so:

```python
from enum import Enum

class SupportRequest(Enum):
    START = 1
    CHECK_LOGS = 2
    ASK_HELP = 3
```

Now, we need to build a state machine to manage the conversation flow without blocking users who do not require support. To achieve this, we will use the [`agent_fast_reply`](../../technical/plugins/hooks.md#available-hooks) hook. This hook will check if a support request has already been initiated in the current session using the Working Memory. If no request exists, it will classify the user input as either support-related or not. If it is, the request state will begin to be tracked in the Working Memory.

```python

from cat.mad_hatter.decorators import hook

@hook
def agent_fast_reply(fast_reply, cat):
    support_request = getattr(cat.working_memory, "support_request", None)
    user_message = cat.working_memory.user_message_json.text

    if support_request is None:
        support_request_intent = cat.classify(
            user_message,
            labels={
                "need_support": ["I need help with my Cat instance"],
                "no_need_for_support": ["Whatever"]
            }
        )

        if support_request_intent == "need_support":
            cat.working_memory.support_request = SupportRequest.START
            fast_reply["output"] = "What seems to be the problem with your Cat instance?"
            return fast_reply
        else:
            return fast_reply

```

Now we can write some code to control the conversation flow in a more granular and stateful manner.

```python

# ... agent_fast_reply code

    if support_request == SupportRequest.START:
        cat.working_memory.support_request = SupportRequest.CHECK_LOGS
        fast_reply["output"] = "Have you checked if there are any errors in your logs?"

    elif support_request == SupportRequest.CHECK_LOGS:
        cat.working_memory.support_request = SupportRequest.ASK_HELP
        fast_reply["output"] = "Did you manage to find the error or do you want to ask for support?"

    elif support_request == SupportRequest.ASK_HELP:
        response = cat.classify(user_message, labels=["need_help", "solved"])
        fast_reply["output"] = "You can ask for support here: https://discord.gg/bHX5sNFCYU" if response == "need_help" else "Good for you!"
        cat.working_memory.support_request = None

    return fast_reply

```

As you've noticed, this state machine is quite basic and does not include comprehensive features such as handling conversation exits. Additionally, strict control flow chatbot like this belong to an older generation of chatbot design. 

For a more dynamic and stateful approach you can check the [Conversational Form](https://github.com/CheshireCatAI/conversational-forms). 

Nevertheless, if you need complete control over your conversation flow, you can extend this example by incorporating more dynamic steps, interactions with LLMs, and other features.