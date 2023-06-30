# Summarization Prompt

The Summarization Prompt is nothing more than the instruction to ask the [*Agent*](../cheshire_cat/agent.md) to summarize a document.
This step is borne by the [Rabbit Hole](../cheshire_cat/rabbit_hole.md) when storing documents in the [episodic memory](../memory/long_term_memory.md).

This is an iterative process: a document is split in chunks; each chunk is grouped and summarized iteratively until only one summary remains.

By default, the Summarization Prompt is the following:

```python
summarization_prompt = """Write a concise summary of the following:
{text}
"""
```

## Summarization flow :material-information-outline:{ title="click on the nodes with hooks to see their documentation" }

!!!! note "Developer documentation"
    [Summarization hooks](../../technical/API_Documentation/mad_hatter/core_plugin/hooks/prompt.md#cat.mad_hatter.core_plugin.hooks.prompt.summarization_prompt)  
    [Rabbit Hole hooks](../../technical/API_Documentation/mad_hatter/core_plugin/hooks/rabbithole.md)

```mermaid

flowchart LR
A["&#128196;Document"] --> B[read];
subgraph rb ["&#128048;RabbitHole"]
B[read] --> C["&#129693;"];
C["&#129693;"] --> D[recursive split];
D["&#129693;recursive split"] --> E["&#129693;"];
E["&#129693;"] --> F["&#129693;summarization"];
F["&#129693;summarization"] --> G["&#129693;"];
end
G["&#129693;"] --> H["&#128024;Episodic Memory"] 
```

Nodes with the &#129693;; point the execution places where there is an available [hook](../plugins.md) to customize the execution pipeline.
