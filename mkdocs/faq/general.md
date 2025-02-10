# General

#### I've found the Cat and I like it very much, but I'm not able to follow your instructions to install it on my machine. Can you help?

The Cheshire Cat is a framework to help developers to build vertical AIs: you will need some basic technical skills to follow our instructions.
Please try to ask in the support channel in our discord server, and remember this is all volunteers effort: be kind! :)

#### Why the Cat does not default to some open LLM instead of ChatGPT or GPT-3?

Our intention is not to depend on any specific LLM: the Cat does not have a preference about which LLM to use. Nonetheless, at the moment, OpenAI tools still provide the best results for your bucks.
Decision is up to you.

#### Are text and documents sent to the Cat safe and not shared with anybody?

The local memory is safe and under your control, although embeddings and prompts are shared with your configured LLM, meaning you need to check how safe the LLM is.  
We plan to adopt local LLMs, at which point all your data will be under your control.

#### What is the difference between Langchain and the Cat?

[The Cheshire Cat](https://cheshirecat.ai/) is a production-ready AI framework, it means that with almost no effort you can setup an intelligent agent ready to help both you and your customers.

On the other hand, [Langchain](https://github.com/langchain-ai/langchain) is a framework for developing applications powered by language models. It offers tons of composable tools and integrations to this purpose and the Cheshire Cat makes use of some of them to manage chains, agents, llm/embedder. You can take an in depth look at our [core](https://github.com/cheshire-cat-ai/core) if you are purr-ious about it.

#### I want to use the admin page for...

The admin panel is meant to be an administration interface. It's purpose is to chat with the Cat only to debug/play with it, it is not intended to be a final widget chat used by eventual final users.

We provide a [widget](https://github.com/cheshire-cat-ai/widget-vue) to connect the Cat to your product.

You are free to modify the Admin to adapt it to your product, **however** you will need to respect the GPL3 Licence, meaning you are free to fork the codebase and go on your own, but you are forced to open source eventual changes.

