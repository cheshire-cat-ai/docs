# :toolbox: Tools

A Tool is a python function that can be called directly from the language model.  
By "called" we mean that the LLM has a description of the available Tools in the prompt, and (given the conversation context) it can generate as output something like:

> Thought: Do I need to use a Tool? Yes  
> Action: search_ecommerce  
> Action Input: "white sport shoes"

So your `search_ecommerce` Tool will be called and given the input string `"white sport shoes"`.
The output of your Tool will go back to the LLM or directly to the user:

> Observation: "Mike air Jordania shoes are available for 59.99€"

You can use Tools to:

- communicate with a web service
- search information in an external database
- execute math calculations
- run stuff in the terminal (danger zone)
- keep track of specific information and do fancy stuff with it
- your fantasy is the limit!

Tools in the Cheshire Cat are inspired and extend [langchain Tools](https://python.langchain.com/en/latest/modules/agents/tools.html), an elegant Toolformer[^1] implementation.

## Default tool

The Cat comes already with a custom tool that allows to retrieve the time. You can find it in `core/cat/mad_hatter/core_plugin/tools.py`.  
Let's take a look at it:

```python
@tool # (1)
def get_the_time(tool_input, cat): # (2)
    """Retrieves current time and clock. Input is always None.""" # (3)
    return str(datetime.now()) # (4)

```

1. Python functions in a plugin only become tools if you use the `@tool` decorator
2. Every `@tool` receives two arguments: a string representing the tool input, and the Cat instance.
3. This doc string is necessary, as it will show up in the LLM prompt. It should describe what the tool is useful for and how to prepare inputs, so the LLM can select the tool and input it properly.
4. Always return a string, which goes back to the prompt informing the LLM on the Tool's output.

Here is how it works in a sample conversation:

**User's Input**:
> Can you tell me what time is it?

**Cat's reasoning** from the terminal:
> Entering new LLMChain chain...
>
> Prompt after formatting:
>
> This is a conversation between a human and an intelligent robot cat that passes the Turing test.
>
> The cat is curious and talks like the Cheshire Cat from Alice's adventures in wonderland.
>
> The cat replies are based on the Context provided below.
>
> Context of things the Human said in the past:
>> \- I am the Cheshire Cat (2 minutes ago)
>
> Context of documents containing relevant information:
>
>> \- I am the Cheshire Cat (extracted from cheshire-cat)
>
> If Context is not enough, you have access to the following tools:
>
>> \> get_the_time: get_the_time(tool_input) - Retrieves current time and clock. Input is always None.  
>> \> Calculator: Useful for when you need to answer questions about math.
>
> To use a tool, please use the following format:
>
> '''
>
> **Thought**: Do I need to use a tool? Yes
>
> **Action**: the action to take, should be one of [get_the_time, Calculator]
>
> **Action Input**: the input to the action
>
> **Observation**: the result of the action
>
> '''
>
>
> When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:
>
>
> '''
>
> Thought: Do I need to use a tool? No
>
> AI: [your response here]
>
> '''
>
>
> Conversation until now:
>> \- Human: Can you tell me what time is it?
>
> What would the AI reply?
>
> Answer concisely to the user needs as best you can, according to the provided recent conversation, context and tools.
>
>
> **Thought**: Do I need to use a tool? Yes
>
> **Action**: get_the_time
>
> **Action Input**: None
>
> **Observation**: 2023-06-03 20:48:07.527033

**Cat's answer**:
> The time is 2023-06-03 20:48:07.527033.

## Your first Tool

A Tool is just a python function. In this example, we'll show how to create a tool to convert currencies.
To keep it simple, we'll not rely on any third party library and we'll just assume a fixed rate of change.  
Let's convert EUR to USD. In your `mypluginfile.py` create a new function with the `@tool` decorator:

```python
@tool
def convert_currency(tool_input, cat): # (1)
    """Useful to convert currencies. This tool converts euros (EUR) to dollars (USD).
     Input is a floating point number.""" # (2)
    
    # Define fixed rate of change
    rate_of_change = 1.07
    
    # Parse input
    eur = float(tool_input) # (3)

    # Compute USD
    usd = eur * rate_of_change

    return usd
```

!!! Warning
    1. Always remember the two mandatory arguments
    2. In the docstring we explicitly explain how the input should look like. In this way the LLM will be able to isolate it from our input sentence
    3. The input we receive is always a string, hence, we need to correctly parse it. In this case, we have to convert it to a floating number

TODO:

- a better example?
- show how tools are displayed in the prompt and how the LLM selects them
- more examples with little variations
    - the tool calls an external service
    - the tool reads/writes a file
    - the input string contains a dictionary (to be parsed with `json.loads`)
    - the tool manages a conversational form
    - `@tool(return_direct=True)` to let the returned string go straight to the chat
    - show how you can access cat's functionality (memory, llm, embedder, rabbit_hole) from inside a tool
    - what else? dunno

## References

[^1]:Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., ... & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761.
