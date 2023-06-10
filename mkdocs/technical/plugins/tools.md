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
Let's take a look at it.

#### Implementation

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

#### How it works

**User's Input**:
> Can you tell me what time is it?

**Cat's full prompt** from the terminal:
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

#### Implementation

Let's convert EUR to USD. In your `mypluginfile.py` create a new function with the `@tool` decorator:

```python
from cat.mad_hatter.decorators import tool

@tool
def convert_currency(tool_input, cat): # (1)
    """Useful to convert currencies. This tool converts euro (EUR) to dollars (USD).
     Input is an integer or floating point number.""" # (2)
    
    # Define fixed rate of change
    rate_of_change = 1.07
    
    # Parse input
    eur = float(tool_input) # (3)

    # Compute USD
    usd = eur * rate_of_change

    return usd
```

1. !!! Warning
        Always remember the two mandatory arguments
2. In the docstring we explicitly explain how the input should look like. In this way the LLM will be able to isolate it from our input sentence
3. The input we receive is always a string, hence, we need to correctly parse it. In this case, we have to convert it to a floating number

#### How it works

**User's input**:
> Can you convert 10.5 euro to dollars?

**Cat's reasoning** from the terminal:
> **Thought**: Do I need to use a tool? Yes
> 
> **Action**: convert_currency
> 
> **Action Input**: 10.5
>
> **Observation**: 11.235000000000001

**Cat's answer**:
> 10.5 euros is equivalent to 11.235000000000001 dollars.

Writing as tool is as simple as this. The core aspect to remember are: 

1. the two input arguments, i.e. the first is the string the LLM take from the chat and the Cat instance;
2. the docstring from where the LLM understand how to use the tool and how the input should look like.

## More tools

As seen, writing basic tools is as simple as writing pure Python functions.  
However, tools can be very flexible. Here are some examples.

### Return the output directly

The `@tool` decorator accepts an optional boolean argument that is `@tool(return_direct=True)`.
This is set to `False` by default, which means the tool output is parsed again by the LLM.
Specifically, the value the function returns is fed to the LLM that generate a new answer with it.
When set to `True`, the returned value is printed in the chat as-is.  

#### Implementation

Let's give it a try with a modified version of the `convert_currency` tool:

```python
from cat.mad_hatter.decorators import tool

@tool(return_direct=True)
def convert_currency(tool_input, cat):
    """Useful to convert currencies. This tool converts euro (EUR) to dollars (USD).
     Input is an integer or floating point number."""
    
    # Define fixed rate of change
    rate_of_change = 1.07
    
    # Parse input
    eur = float(tool_input) # (3)

    # Compute USD
    usd = eur * rate_of_change
    
    # Format the output
    direct_output = f"Result of the conversion: {eur:.2f} EUR -> {usd:.2f} USD"

    return direct_output
```

#### How it works

**User's input**:
> Can you convert 10.5 euro to dollars?

**Cat's reasoning** from the terminal:
the reasoning is not displayed as the goal of the `return_direct=True` parameter is to skip those steps and return the output directly. 

**Cat's answer**:
> Result of the conversion: 10.50 EUR -> 11.24 USD

### Complex input tools

This sections re-proposes an explanation of langchain [multi-input tools](https://python.langchain.com/en/latest/modules/agents/tools/multi_input_tool.html).
For example, we can make the `convert_currency` tool more flexible allowing the user to choose among a fixed set of currencies.

#### Implementation

```python
from cat.mad_hatter.decorators import tool

@tool
def convert_currency(tool_input, cat): # (1)
    """Useful to convert currencies. This tool converts euro (EUR) to a fixed set of other currencies.
    Choises are: US dollar (USD), English pounds (GBP) or Japanese Yen (JPY).
    Inputs are two values separated with a minus: the first one is an integer or floating point number;
    the second one is a three capital letters currency symbol.""" # (2)
    
    # Parse the input
    eur, currency = tool_input.split("-") # (3)
    
    # Define fixed rates of change
    rate_of_change = {"USD": 1.07,
                      "GBP": 0.86,
                      "JPY": 150.13}
    
    # Convert EUR to float
    eur = float(eur)
    
    # Check currency exists in our list
    if currency in rate_of_change.keys():
        # Convert EUR to selected currency
        result = eur * rate_of_change[currency]

    return result
```

1. The input to the function are always two
2. Explain in detail how the inputs from the chat should look like. Here we want something like "3.25-JPY"
3. The input is always a string, thus it's up to us correctly split and parse the input.

#### How it works

**User's input**:
> Can you convert 7.5 euros to GBP?

**Cat's reasoning** from the terminal:
> **Thought**: Do I need to use a tool? Yes
> 
> **Action**: convert_currency
> 
> **Action Input**: 7.5-GBP
> 
> **Observation**: 6.45

**Cat's answer**:
> 7.5 euros is equal to 6.45 British Pounds.

As you may see, the [Agent](../../conceptual/cheshire_cat/agent.md) correctly understands the desired output from the message
and passes it to the tool function as explained in the docstring. Then, it is up to us parse the two inputs correctly for our tool.

### External library & the cat parameter

Tools are extremely flexible as they allow to exploit the whole Python ecosystem of packages.
Thus, we can update our tool making use of the [Currency Converter](https://github.com/alexprengere/currencyconverter) package.  
Moreover, here is an example of how you could use the `cat` parameter passed to the tool function.

#### Implementation

```python
from currency_converter import CurrencyConverter
from cat.mad_hatter.decorators import tool


@tool(return_direct=True)
def convert_currency(tool_input, cat):
    """Useful to convert currencies. This tool converts euros (EUR) to another currency.
    The inputs are two values separated with a minus: the first one is a number;
    the second one is the name of a currency. Example input: '15-GBP'.
    Use when the user says something like: 'convert 15 EUR to GBP'"""
    
    # Currency Converter
    converter = CurrencyConverter(decimal=True)

    # Parse the input
    parsed_input = tool_input.split("-")

    # Check input is correct
    if len(parsed_input) == 2:  # (1)
        eur, currency = parsed_input[0].strip("'"), parsed_input[1].strip("'")
    else:
        return "Something went wrong using the tool"

    # Ask the Cat to convert the currency name into its symbol
    symbol = cat.llm(f"You will be given a currency code, translate the input in the corresponding currency symbol. \
                    Examples: \
                        euro -> € \
                        {currency} -> [answer here]")  # (2)
    # Remove new line if any
    symbol = symbol.strip("\n")

    # Check the currencies are in the list of available ones
    if currency not in converter.currencies:
        return f"{currency} is not available"

    # Convert EUR to currency
    result = converter.convert(float(eur), "EUR", currency)

    return f"{eur}€ = {float(result):.2f}{symbol}"

```

1. LLMs can be extremely powerful, but they are not always precise. Hence, it's always better to have some checks when parsing the input.
   A common scenario is that sometimes the Agent wraps the input around quotes and sometimes doesn't
   E.g. Action Input: 7.5-GBP vs Action Input: '7.5-GBP'
2. the `cat` instance gives access to any method of the [Cheshire Cat](). In this example, we directly call the LLM using one-shot example to get a currency symbol.

#### How it works

The thoughts under the hood are identical to the previous example, as nothing changed in the underlying behavior, but we improved a little
the quality of our tool code.

> **Thought**: Do I need to use a tool? Yes
> 
> **Action**: convert_currency
> 
> **Action Input**: 67-JPY
> 
> **Observation**: 67€ = 9846.99¥


TODO:

- a better example?
- show how tools are displayed in the prompt and how the LLM selects them
- more examples with little variations
    - the tool calls an external service
    - the tool reads/writes a file
    - the input string contains a dictionary (to be parsed with `json.loads`)
    - the tool manages a conversational form
    - show how you can access cat's functionality (memory, llm, embedder, rabbit_hole) from inside a tool
    - what else? dunno

## References

[^1]:Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., ... & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761.
