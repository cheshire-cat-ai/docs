# Long Term Memory

The Cat's Long Term Memory (LTM) is made of three components:

- *episodic memory*, i.e. the context of things the user said in the past;
- *declarative memory*, i.e. the context of documents uploaded to the Cat;
- *procedural memory*, i.e. the set of python functions that defines what the Cat is able to do.

These are nothing but three [collections](vector_memory.md) in the vector database, where text memories and tools (i.e. Python functions) are stored in the form of vectors.

You can interact with the LTM using the memory page.

By default, the Cat queries the LTM to retrieve the relevant context that is used to make up the [Main prompt](../prompts/main_prompt.md) and the Instruction prompt.

## Long Term Memory flow :material-information-outline:{ title="click on the nodes with hooks to see their documentation" }

!!! note "Developer documentation"
    [Long Term Memory hooks](../../technical/API_Documentation/mad_hatter/core_plugin/hooks/flow.md#at.mad_hatter.core_plugin.hooks.flow.before_cat_recalls_memories)

```mermaid
flowchart LR
    subgraph LTM ["#128024;Long Term Memory"]
            direction TB
            C[(Episodic)];
            D[(Declarative)];
            P[(Procedural)]
    end
    H["#129693;"] %% before_cat_recalls_memories
    H1["#129693;"] %% before_cat_recalls_episodic_memories
    H2["#129693;"] %% before_cat_recalls_declarative_memories
    H3["#129693;"] %% before_cat_recalls_procedural_memories
    E["#129693;"] %% after_cat_recalls_memories
    A[Query] --> H 
    H["#129693;"] --> H1
    H --> H2
    H --> H3
    H1 --> C
    H2 --> D
    H3 --> P
    C --> E
    D --> E
    P --> E
    E --> wm["#9881;#128024;Working Memory"]
```

Nodes with the &#129693; point the execution places where there is an available [hook](../plugins.md) to customize the execution pipeline.
