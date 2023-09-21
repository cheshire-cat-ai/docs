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