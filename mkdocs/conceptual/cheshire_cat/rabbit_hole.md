# Rabbit Hole

The Rabbit Hole is the Cat's component that takes care of ingesting documents and storing them in the [episodic memory](../memory/long_term_memory.md).
You can interact with it either through its [endpoint](../../technical/basics/basics.md), the [GUI](../../technical/basics/admin-interface.md) or a Python script.

Currently supported file formats are: `.txt`, `.md`, `.pdf` or `.html` via web URL.

## Rabbit Hole flow :material-information-outline:{ title="click on the nodes with hooks to see their documentation" }

!!! note "Developer documentation"
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

Nodes with the &#129693; point the execution places where there is an available [hook](../plugins.md) to customize the execution pipeline.
