# Introduction

The Cheshire Cat is a ready-to-use AI micro-framework. Once installed and configured to connect to a Language Model (LLM), it can be queried through APIs. These APIs return responses provided by the LLM.

But this is just the beginning.

## Previous Conversation History
All previous conversations are stored in a local database called `episodic memory`. When a question is asked, the response takes into account past conversations.

## Document Loading
Text documents can be loaded as well. These documents are also saved in a local database called `declarative memory`. Responses will consider the information within these documents. Documents can be uploaded through APIs or the Admin Portal.

The component responsible for document ingestion is the `Rabbit Hole`.

## Performing Actions
The Cheshire Cat isn't limited to just answering questions; it can also perform actions. You can write Python functions called `Tools` and have the LLM execute this code. The capabilities of the Python code are only limited by your imagination.

## Extending the Core
Additionally, it's possible to customize the Cheshire Cat's core. In the main process flows, there are predefined adaptation points called `Hooks`. You can write Python functions that can be attached onto these `Hooks`. The attached code will be invoked during the flow`s execution and can modify the Cheshire Cat's internal behavior, all without directly modifying the core of the Cheshire Cat.

`Tools` and `Hooks` are packaged into `Plugins` that can be installed by placing files in a specific folder or through a the Admin Portal. The component responsible for managing plugins is the `Mad Hatter`.

## Sharing Plugins
If desired, you can publish the `Plugins` you create on a public registry, enabling others to install them with just a single click from the Admin Portal.

## Admin Portal
Completing the framework is a web portal for Admin users. Through this portal, the admin can configure framework settings, install plugins from public registry, upload documents, and use it as a playground tool. You can chat with the Cheshire Cat, analyze its responses, and directly query its memories.

## Next step
In the next step you will learn how install, set the LLM and the basics of all of this stuff.

We will do this transforming the Cat into a socks seller. We will upload some knowledge (documents) about socks knitting, the Cat will able to tell the price of socks of a requested color (using a `Tool`), and in the end we will transform the socks seller into a poetic socks seller changing his personality (using a `Hook`). 

The example is light and fun, it should give you an idea of what is possible.