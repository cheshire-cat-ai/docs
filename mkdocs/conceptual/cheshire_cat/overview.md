# Overview

The Cheshire Cat is a ready-to-use AI micro-framework. Once installed and configured to connect to a Language Model (LLM), it can be queried through APIs. These APIs return responses provided by the LLM.

But this is just the beginning.

## Previous Conversation History
All previous conversations are stored in a local database called `episodic memory`. When a question is asked, the response takes into account past conversations.

## Document Loading
Text documents can be loaded as well. These documents are also saved in a local database called `declarative memory`. Responses will consider the information within these documents. Documents can be uploaded through APIs or a Admin Portal.

The component responsible for document ingestion is the `Rabbit Hole`.

## Performing Actions
The Cheshire Cat isn't limited to just answering questions; it can also perform actions. You can write Python functions called `tools` and have the LLM execute this code. The capabilities of the Python code are only limited by your imagination.

## Extending the Core
Additionally, it's possible to customize the Cheshire Cat's core. In the main process flows, there are predefined adaptation points called `hooks`. You can write Python functions that can be attached onto these `hooks`. The attached code will be invoked during the flow`s execution and can modify the Cheshire Cat's internal behavior, all without directly modifying the core of the Cheshire Cat.

`Tools` and `Hooks` are packaged into `Plugins` that can be installed by placing files in a specific folder or through a the Admin Portal. The component responsible for managing plugins is the `Mad Hatter`.

## Admin Portal
Completing the framework is a web portal for Admin users. Through this portal, the admin can configure framework settings, install plugins, upload documents, and use it as a playground tool. You can chat with the Cheshire Cat, analyze its responses, and directly query its memories.