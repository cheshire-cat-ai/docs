# Main Prompt

The Main Prompt is the full set of instructions that is fed to the [*Agent*](../cheshire_cat/agent.md).
For instance, the prompt can be engineered to instruct the Cat to behave in a specific manner or to use the memory and the [tools](../plugins.md).

This prompt is split in three parts:

- a prefix;
- the instructions;
- a suffix.

Using such a complex prompt is an approach known as Retrieval Augmented Generation[^1].  
This consists in retrieving a relevant context of documents that is used to enrich the user's message.  
Specifically, the Cat exploits the [Hypothetical Document Embedding](hyde.md)[^2] (HyDE) technique to recall the relevant
context from the [Long Term Memory](../memory/long_term_memory.md) and, indeed, augment the Main Prompt.  
This is also augmented with the history of the recent conversation, a set of [tools](../plugins.md) and the history the [Agent's](../cheshire_cat/agent.md) reasoning.

In the following sections, we explain every prompt component.

## Prefix

This is the first component. By default, it is:

```python
prefix = """You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
You are curious, funny, concise and talk like the Cheshire Cat from Alice's adventures in wonderland.
You answer Human using tools and context.

# Tools"""
```

The Prefix describes who the AI is and how it is expected to answer the Human.  
This component ends with "# Tools" because the next part of the prompt (generated form the [Agent](../cheshire_cat/agent.md)) contains the list of [Tools](../plugins.md#tools).

## Instructions

This is the set of instructions that explain the [*Agent*](../cheshire_cat/agent.md) how to format its reasoning.  
The [*Agent*](../cheshire_cat/agent.md) uses such chain of thoughts to decide *when* and *which* [tool](../plugins.md) is the most appropriate to fulfill the user's needs.

By default, it is:

```python
instructions = """To use a tool, use the following format:

\```
Thought: Do I need to use a tool? Yes
Action: the action to take /* should be one of [{tool_names}] */
Action Input: the input to the action
Observation: the result of the action
\```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

\```
Thought: Do I need to use a tool? No
{ai_prefix}: [your response here]
\```"""
```

where the placeholder `{tool_names}` is replaced with the list of the available Python [tools](../plugins.md).

## Suffix

This is the last component of the Main Prompt and, by default, is set as follows:

```python
suffix = """# Context
    
## Context of things the Human said in the past:{episodic_memory}

## Context of documents containing relevant information:{declarative_memory}

## Conversation until now:{chat_history}
 - Human: {input}

# What would the AI reply?

{agent_scratchpad}"""
```

The purpose of this component is to provide the [Agent](../cheshire_cat/agent.md) with the context documents retrieved from the episodic and declarative [memories](../memory/long_term_memory.md), the recent conversation and the agent scratchpad,
i.e. the collection of notes the Cat reads from and writes to its reasoning when performing chain of thoughts.

## Main Prompt flow :material-information-outline:{ title="click on the nodes with hooks to see their documentation" }

!!! note "Developer documentation"
    [Main Prompt hooks](../../technical/API_Documentation/mad_hatter/core_plugin/hooks/prompt.md#cat.mad_hatter.core_plugin.hooks.prompt.agent_prompt_instructions)

```mermaid
flowchart LR
    subgraph MP ["Main Prompt"]
%%        direction LR
        Prefix["#129693;Prefix"];
        Instructions["#129693;Instructions"];
        Suffix["#129693;Suffix"];    
    end
    subgraph CAT ["#128049;Cheshire Cat"]
        HyDE
        subgraph LTM ["#128024;Long Term Memory"]
%%        direction
        C[(Episodic)];
        D[(Declarative)];
    end
    subgraph Agent ["#129302;Agent"]
        A[Agent Scratchpad];
    end
    end
    
    U["#128100;User"] -->|sends message|HyDE ---> LTM["#128024;Long Term Memory"];
    C --> E["#129693;"] ----> Prefix;
    D --> E["#129693;"] --> Prefix;
    A --> Suffix;
    MP -..->|fed back to|CAT -...-> Answer
```

Nodes with the &#129693; point the execution places where there is an available [hook](../plugins.md) to customize the execution pipeline.

## References

[^1]: Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems, 33, 9459-9474.

[^2]: Gao, L., Ma, X., Lin, J., & Callan, J. (2022). Precise Zero-Shot Dense Retrieval without Relevance Labels. arXiv preprint arXiv:2212.10496.
