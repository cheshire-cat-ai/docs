# Introduction

There are a few things you need to know about the Cheshire Cat. If you are eager to launch and start hacking, jump to the [installation page](installation-configuration.md), but please be sure to return here.

The Cheshire Cat is a ready-to-use AI micro-framework.
Once installed and connected to a Large Language Model (LLM), it can be queried through APIs.
These APIs return the responses provided by the LLM.

But this is just the beginning.

## Previous Conversation History
All previous conversations are stored in a local database called [`episodic memory`](../framework/cat-components/memory/episodic_memory.md).
When you ask a question, the Cat answers taking into account the past conversations.

## Loading Documents
You can load text documents as well.
These documents are also saved in a local database called [`declarative memory`](../framework/cat-components/memory/declarative_memory.md).
When answering, the Cat will consider the information within these documents.
Documents can be uploaded through the APIs or the `Admin Portal`.

The [`Rabbit Hole`](../framework/cat-components/cheshire_cat/rabbit_hole.md) is the component responsible for the document ingestion.

## Performing Actions
The Cheshire Cat isn't limited to just answering questions; it can also perform actions.
You can write Python functions called [`Tools`](../plugins/tools.md) and have the LLM execute this code.
The only limit to the Python code's capabilities is your imagination.

## Executing Actions in the Future
Actions are not limited to being triggered immediately after a chat initiated by a human, they can be scheduled for future execution and, if needed, set to recur, or even initiated without any chat trigger.

The [`White Rabbit`](../framework/cat-components/cheshire_cat/white_rabbit.md) is the component that triggers the scheduled Actions.

## Extending the Core
Additionally, it's possible to customize the Cheshire Cat's core.
In the main process flow, there are predefined adaptation points called [`Hooks`](../plugins/hooks.md).
You can write Python functions that can be attached onto these [`Hooks`](../plugins/hooks.md).
The attached code will be invoked during the flow's execution and can modify the Cheshire Cat's internal behavior,
without directly modifying the core of the Cheshire Cat.

[`Tools`](../plugins/tools.md) and [`Hooks`](../plugins/hooks.md) are packaged into [`Plugins`](../plugins/plugins.md) that can be installed by placing files in a specific folder or using the `Admin Portal`.

The [`Mad Hatter`](../framework/cat-components/cheshire_cat/mad_hatter.md) is the component that manages plugins.

## Sharing Plugins
If desired, you can  [`publish your Plugins`](../plugins/plugins-registry/publishing-plugin.md) on the public registry.
Other users will be able to install them with just a single click.

## Admin Portal
A web portal for admin users completes the framework.
Using this portal, the admin can configure the settings, upload documents, install plugins and use it as a playground tool.
You can chat with the Cheshire Cat, inspect its responses and directly query its memories.

## Next step
In the [next step](./installation-configuration.md), you will learn how to install the Cat, set the LLM and the basics of this all.

We will be transforming the Cat into a sock seller.
More in detail, we will upload some knowledge (documents) about socks knitting.
Also, the Cat will be able to tell the price of socks according to the requested color (using a [`Tools`](../plugins/tools.md)).
In the end, we will transform the sock seller into a poetic socks seller, changing its personality (using a [`Hooks`](../plugins/hooks.md)). 

The example is light and fun, it should give you an idea of what is possible.