---
title: before_rabbithole_stores_documents
---

# `before_rabbithole_stores_documents`

Intervene before the Rabbit Hole starts the ingestion pipeline.

Allows modifying how the list of `Document` is inserted in the vector memory.

For example, this hook is a good point to summarize the incoming documents and save both original and summarized contents.
An official plugin is available to test this procedure.

## &#128196; Arguments

| Name   | Type                                                                    | Description                                                            |
|:-------|:------------------------------------------------------------------------|------------------------------------------------------------------------|
| `docs` | `List[Document]`                                                        | List of chunked Langchain `Document`s before being inserted in memory. |
| `cat`  | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.     |

## &#x21A9;&#xFE0F; Return

Type: `List[Document]`

List of Langchain `Document`s that will be stored in vector memory.

## &#9997; Example

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

!!! note
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
    - [Summarization plugin](https://github.com/Furrmidable-Crew/ccat_summarization)
