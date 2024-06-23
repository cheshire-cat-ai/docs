# Language Models

A language model is a Deep Learning Neural Network trained on a huge amount of text data to perform different types of language tasks.
Commonly, they are also referred to as Large Language Models (LLM).
Language models come in many architectures, size and specializations.  
The peculiarity of the Cheshire Cat is to be model-agnostic. This means it supports many different language models.

By default, there are two classes of language models that tackle two different tasks.

## Completion Model

This is the most known type of language models
(see for examples [ChatGPT](https://openai.com/blog/chatgpt), [Cohere](https://cohere.com/) and many others).
A completion model takes a string as input and generates a plausible answer by completion.

!!! warning
    A LLM answer should not be accepted as-is, since LLM are subjected to hallucinations.
    Namely, their main goal is to generate plausible answers from the syntactical point of view.
    Thus, the provided answer could come from completely invented information.
