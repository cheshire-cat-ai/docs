# Agent Manager

The Agent Manager is the Cat's component that manages the execution of language models [chains](https://docs.langchain.com/docs/components/chains/llm-chain).
A language model chain is a pipeline that takes one or more input variables, it formats them in a prompt,
submits the prompt to a language model and, optionally, parses the output.

The Cat's Agent Manager orchestrates two chains: 

1. the **tool chain**, which, in turn, is a component of the Tool Agent;
2. the **memory chain**.

When suitable tools for the task at hand are retrieved from the [procedural memory](../memory/long_term_memory.md),
the Agent Manager calls the Tool Agent to execute the tool chain; otherwise the memory chain is executed to answer the user's
question with the context retrieved from the episodic and declarative [memories](../memory/long_term_memory.md).

Specifically, the default execution pipeline is the following:

1. the Cat receives the user's message;
2. the Cat looks for relevant context in each memory collection (i.e. procedural, declarative and episodic) using the user's message as a query;
3. if meaningful context is retrieved from the procedural memory, the Tool Agent starts, otherwise the **memory chain** starts;
4. if executed, the Tool Agent provides an output. If the output answer the user's input, such output is returned to the user, otherwise the **memory chain** starts;
5. if executed, the **memory chain** provides the output using the context retrieved from the declarative and episodic memories.

## Tool Chain

Sometimes a simple answer from the [language model](../llm.md#completion-model) is not enough.
For this reason, the Cat can exploit a set of custom tools (e.g. API calls and Python functions) coming from the [plugins](../plugins.md).  
The decision on *whether* and *which* action should be taken to fulfill the user's request is delegated to an Agent, i.e. the Tool Agent.

The Tool Agent uses the language model to outline a "reasoning" and accomplish the user's request with the tools retrieved
from the Cat's [procedural memory](../memory/long_term_memory.md).
The tools selection and usage is planned according to a set of [instructions](../prompts/main_prompt.md#instructions).
Finally, the Tool Agent parses the formatting of the tool output.

## Memory Chain

The Memory Chain is a simple chain that takes the user's input and the context retrieved from the episodic and declarative
[memories](../memory/long_term_memory.md) and formats them in the [main prompt](../prompts/main_prompt.md). Such prompt
is submitted to the language model.

## Agent flow :material-information-outline:{ title="click on the nodes with hooks to see their documentation" }

!!! note "Developer documentation"
    [Agent hooks](../../technical/API_Documentation/mad_hatter/core_plugin/hooks/agent.md)

[//]: # (TODO improve this flowchart)

```mermaid
flowchart TB
    subgraph Cat 
       subgraph Agent["Agent Manager"]
       H1["#129693;"] %% before_agent_starts
       LM["Language Model"]
        subgraph TA["Tool Agent"]
            H2["#129693;"] %% agent_allowed_tools
            Instructions
        end
        subgraph MA["Memory Chain"]
           subgraph MP["Main Prompt"]
                H3["#129693;"] %% agent_prompt_prefix
                H4["#129693;"] %% agent_prompt_suffix
                Prefix
                Suffix
           end
        end 
        end
    end
    User --> H1
    H1 --> LM
    LM ---> User
    User --> H2
    H2 --> Instructions
    Instructions --> LM
    TA --> H3
    H3 --> Prefix
    Prefix --> H4
    H4 --> Suffix
    Suffix --> LM
```

Nodes with the &#129693; point the execution places where there is an available [hook](../plugins.md) to customize the execution pipeline.
