# Security and Spending

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