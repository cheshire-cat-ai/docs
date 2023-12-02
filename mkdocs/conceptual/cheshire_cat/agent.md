# Agent Manager

The Agent Manager is the Cat's component that manages the execution of language models **chains**.
A language model chain is a pipeline that takes one or more input variables, it formats them in a prompt,
submits the prompt to a language model and, optionally, parses the output.

The Cat's Agent Manager orchestrates two chains: 

1. the [tool chain](tool_chain.md), which, in turn, is a component of the Tool Agent;
2. the [memory chain](memory_chain.md)

When suitable tools for the task at hand are retrieved from the [procedural memory](../memory/long_term_memory.md),
the Agent Manager calls the Tool Agent to execute the tool chain; otherwise the memory chain is executed to answer the user's
question with the context retrieved from the episodic and declarative [memories](../memory/long_term_memory.md).

![Schema of the Cheshire Cat memories](../../assets/img/diagrams/agent-manager.jpg){width=400px style="display: block; margin: 0 auto"}

Specifically, the default execution pipeline is the following:

1. the Cat receives the user's message;
2. the Cat looks for relevant context in each memory collection (i.e. procedural, declarative and episodic) using the user's message as a query;
3. if meaningful context is retrieved from the procedural memory, the Tool Agent starts, otherwise the [memory chain](memory_chain.md) starts;
4. if executed, the Tool Agent provides an output. If the output answer the user's input, such output is returned to the user, otherwise the [memory chain](memory_chain.md) starts;
5. if executed, the [memory chain](memory_chain.md) provides the output using the context retrieved from the declarative and episodic memories.
