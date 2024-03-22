# &#128587;&#8205;&#9794;&#65039; FAQ

## General

#### I've found the Cat and I like it very much, but I'm not able to follow your instructions to install it on my machine. Can you help?

The Cheshire Cat is a framework to help developers to build vertical AIs: you will need some basic technical skills to follow our instructions.
Please try to ask in the support channel in our discord server, and remember this is all volunteers effort: be kind! :)

#### Why the Cat does not default to some open LLM instead of ChatGPT or GPT-3?

Our intention is not to depend on any specific LLM: the Cat does not have a preference about which LLM to use. Nonetheless, at the moment, OpenAI tools still provide the best results for your bucks.
Decision is up to you.

#### Are text and documents sent to the Cat safe and not shared with anybody?

Well, the local memory is safe and under your control, although embeddings and prompts are shared with your configured LLM, meaning you need to check how safe is the LLM.
We plan to adopt local LLMs, at which point all your data will be under your control.

#### What is the difference between Langchain and the Cat?

[The Cheshire Cat](https://cheshirecat.ai/) is a production-ready AI framework, it means that with almost no effort you can setup an intelligent agent ready to help both you and your customers.

On the other hand, [Langchain](https://github.com/langchain-ai/langchain) is a framework for developing applications powered by language models. It offers tons of composable tools and integrations to this purpose and the Cheshire Cat makes use of some of them to manage chains, agents, llm/embedder. You can take an in depth look at our [core](https://github.com/cheshire-cat-ai/core) if you are purr-ious about it.

#### I want to use the admin page for...

The admin page is an administration/debugging panel. The only use case is to provide a more convinient way to interact with the cat...

We provide a [widget](https://github.com/cheshire-cat-ai/widget-vue) to connect the Cat to your product.

You are free to modify the admin to adapt it on your product **however** you will need to respect the GPL3, meaning you are free to fork and go on your own, but you are forced to open source changes.

#### Why the admin doesn't have authetification using email-password or google account??

The admin page is an administration/debugging panel. 

The only use case is to provide a more convinient way to interact with the cat with **basic** authentification through api_key.


## Basic Info

#### Can I insert a long article into the chat?

Please avoid pasting long articles into the chat.  
Use Rabbit Hole to upload long texts instead: just click on the attachment icon in the chat input widget and upload your file.

#### Are the configured LLM APIs used to "instruct" the Cat with the documents I'm going to upload?

That's not exactly how it works: basically when you ask something to the Cat, we pass to the configured LLM a prompt with your actual question + data that can be useful to answer that question. Data can be parts of your documents or chat history.  
Please check our documentation for more details about how the Cat works for you.

#### Can I talk to the Cat in a language different from English?

Of course, you can: just change the prompts in the Plugin folder accordingly, and take care not to mix languages to get best results.

#### How can I know where the Cat gets the answers? I'd like to know if it's using the files I uploaded or if it's querying the configured LLM.

Just open the console in your browser to check the logs there. At some point soon, this information will end up in the user interface, but at the moment is behind the scenes.

#### I sent to the Cat some text and documents I want to get rid of, How can I do?

You can delete the `long_term_memory` folder and restart the Cat!

## Errors

#### Why am I getting the error `RateLimitError` in my browser console?

Please check if you have a valid credit card connected or if you have used up all the credits of your OpenAI trial period.

#### Docker has no permissions to write

This is a matter with your docker installation or the user you run docker from. Usually you can resolve by using **sudo** command before calling any docker command!

#### The Cat seems not to be working from inside a Virtual Machine

In VirtualBox, you can select Settings->Network, then choose NAT in the "Attached to" drop down menu. Select "Advanced" to configure the port forwarding rules. Assuming the guest IP of your VM is 10.0.2.15 (the default) and the ports configured in the .env files are the defaults, you have to set at least the following rule:

| Rule name | Protocol | Host IP     | Host Port | Guest IP   | Guest Port |
|-----------|----------|-------------|-----------|------------|------------|
| Rule 1    | TCP      | 127.0.0.1   | 1865      | 10.0.2.15  | 1865       |

If you want to work on the documentation of the Cat, you also have to add one rule for port 8000 which is used by `mkdocs`, and to configure `mkdocs` itself to respond to all requests (not only localhost as per the default).

## Customization

#### I want to build my own plugin for the Cat: what should I know about licensing?

Plugins are any license you wish, you can also sell them.
The Cat core is GPL3, meaning you are free to fork and go on your own, but you are forced to open source changes to the core.

#### Port 1865 is not allowed by my operating system and/or firewall

Change the port as you wish in the `.env` file.

```text
# Decide host and port for your Cat. Default will be localhost:1865
CORE_HOST=localhost
CORE_PORT=9000
```

#### Can i use different vector databases?
At the moment, we don't provide any way to switch vector database 😿 but is planned for the future.

## Security

#### Where is the OpenAI API key (or other keys) saved in the Cat?

Keys are store in a JSON file, `core/metadata.json`.

#### Will OpenAI see my documents and conversations?

If you are using the Cat with an OpenAI LLM, all your conversations and documents will indeed take a trip into OpenAI servers, because the models are there.
We advise to avoid uploading sensitive documents while using an external LLM.
If you want to use the Cat in total security and privacy, use a local LLM or a cloud LLM in your control.

## Spending

#### I have chatgpt subscription, can I use the cat?
[Chat-gpt subscription is different from OpenAI API](https://community.openai.com/t/difference-between-monthly-plan-and-tokens/415257)

#### Is there a free way to use OpenAI services?

Unfortunately you need to pay to use OpenAI models, but they are [quite cheap](https://openai.com/pricing).

#### Can I run local models like LLAMA to avoid spending?

Running a LLM (Large Language Model) locally requires high-end hardware and technical skills.
If you don't know what you are doing, we suggest you start using the Cat with ChatGPT.  
Afterwards you can experiment with [local models](https://github.com/cheshire-cat-ai/local-cat) or by setting up a cloud endpoint. The Cat offers you several ways to use an LLM.

#### Can I know in advance how much money I will spend?

That depends on the vendors pricing, how many documents you upload in the Cat memory and how much you chat.
We suggest you start with light usage and small documents, and check how the billing is growing in your LLM vendor's website.
In our experience LLM cloud usage is cheap, and it will probably be even cheaper in the next months and years.

#### Is my GPU powerful enough to run a local model?

That strongly depends on the size of the model you want to run. Try using [this application](https://huggingface.co/spaces/Vokturz/can-it-run-llm) from HuggingFace to get an idea of which model and the amount of quantization your hardware can handle. 
