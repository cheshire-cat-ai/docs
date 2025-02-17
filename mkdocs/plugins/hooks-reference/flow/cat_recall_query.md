---
title: cat_recall_query
---

# `cat_recall_query`

Intervene before the recall query is embedded, hooking into the semantic search query.

This hook allows editing the user's message used as a query for context retrieval from memories.
As a result, the retrieved context can be conditioned editing the user's message.

For example, this hook is a suitable to perform Hypothetical Document Embedding (HyDE).
HyDE [^1] strategy exploits the user's message to generate a hypothetical answer. This is then used to recall
the relevant context from the memory.
An official plugin is available to test this technique.

## &#x1F4C4; Arguments

| Name           | Type                                                                    | Description                                                        |
|:---------------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `user_message` | `str`                                                                   | The user's message that will be used to query the vector memories. |
| `cat`          | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Type: `str`

Edited string to be used for context retrieval in memory.
The returned string is further stored in theWorking Memory at `cat.working_memory.recall_query`.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def cat_recall_query(user_message, cat):
    # Ask the LLM to generate an answer for the question
    new_query = cat.llm(f"If the input is a question, generate a plausible answer. Input --> {user_message}")

    # Replace the original message and use the answer as a query
    return new_query
```

!!! note
    - [HyDE plugin](https://github.com/Furrmidable-Crew/ccat_hyde)
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)

[^1]: Gao, L., Ma, X., Lin, J., & Callan, J. (2022). Precise Zero-Shot Dense Retrieval without Relevance Labels.
   arXiv preprint arXiv:2212.10496.
