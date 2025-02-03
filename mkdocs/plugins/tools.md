# &#129520; Tools

A Tool is a python function that can be chosen to be run directly from the Large Language Model. In other words: you declare a function, but the LLM decides when the function runs and what to pass as an input.

## How tools work

Let's say in your plugin you declare this tool, as we saw in the [quickstart](../quickstart/writing-tool.md):

```python
from cat.mad_hatter.decorators import tool

@tool
def socks_prices(color, cat):
    """How much do socks cost? Input is the sock color."""
    prices = {
        "black": 5,
        "white": 10,
        "pink": 50,
    }
    if color not in prices.keys():
        return f"No {color} socks"
    else:
        return f"{prices[color]} €" 
```

When the user says in the chat something like:

> How much for pink socks?

The Cat will first of all retrieve available tools, and pass their descriptions to the LLM.  
The LLM will choose, given the conversation context, if and which tool to run. LLM output in this case will be:

```json
{
    "action": "socks_prices",
    "action_input": "pink"
}
```

This JSON, given as output from the LLM, is then used by the Cat to *actually* run the tool `socks_prices` passing `"pink"` as an argument.

Tool output is then passed back to the agent or directly returned to the chat, depending if you used simply `@tool` or `@tool(return_direct=True)` as decorator.

You can use Tools to:

- communicate with a web service
- search information in an external database
- execute math calculations
- run stuff in the terminal (danger zone)
- keep track of specific information and do fancy stuff with it
- interact with other Cat components like the llm, embedder, working memory, vector memory, white rabbit, rabbit hole etc.
- your fantasy is the limit!

Tools in the Cheshire Cat are inspired and extend [langchain Tools](https://python.langchain.com/v0.2/docs/concepts/#tools), an elegant Toolformer[^1] implementation.

## Tool declaration

The Cat comes already with a tool that allows to retrieve the time. You can find it in `cat/mad_hatter/core_plugin/tools.py`.  
Let's take a look at it, line by line.

```python
@tool(
    return_direct=False
    examples=["what time is it", "get the time"]
)
def get_the_time(tool_input, cat):
    """Useful to get the current time when asked. Input is always None."""
    return f"The current time is {str(datetime.now())}"
```

Please note:

- Python functions in a plugin only become tools if you use the `@tool` decorator.  
You can simply use `@tool` or pass arguments.
    
    ```python
    @tool(
        # Choose whether tool output goes straight to the user,
        #  or is reelaborated from the agent with another contextual prompt.
        return_direct : bool = False

        # Examples of user sentences triggering the tool.
        examples : List[str] = []
    )
    ```
### Tool arguments

- Every `@tool` receives two arguments: a string representing the tool input, and a StrayCat instance.
    ```python
    def mytool(tool_input, cat):
    ```
    - The `tool_input` is a string, so if you asked in the docstring to produce an int or a dict, be sure to cast or parse the string.
    - With `cat` you can access and use all the main framework components. This is powerful but requires some learning, see [here](../framework/cat-components/cheshire_cat/stray_cat.md).
- The docstring is necessary, as it will show up in the LLM prompt. It should describe what the tool is useful for and how to prepare inputs, so the LLM can select the tool and input it properly.
    ```python
    """When to use the tool. Tool input description."""
    ```
- A tool always return a string, which goes back to the agent or directly back to the user chat. If you need to store additional information, store it in [`cat.working_memory`](../framework/cat-components/memory/working_memory.md).
    ```python
    return "Tool output"
    ```

## Tools troubleshooting

User's Input:
> Can you tell me what time is it?

Cat's answer:
> The time is 2023-06-03 20:48:07.527033.

To see what happened step by step, you can do two things:

- inspect the terminal, where you will see colored conversation turns and prompts sent to the LLM with its replies.
- inspect the websocket message sent back to you, under `message.why.model_interactions`.

## Examples

### Simple input

A Tool is just a python function. In this example, we'll show how to create a tool to convert currencies. 

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

Writing as tool is as simple as this. The core aspect to remember are:

1. the docstring from where the LLM understand how to use the tool and how the input should look like.
2. the two input arguments, i.e. the first is the string the LLM take from the chat and the Cat instance;

As seen, writing basic tools is as simple as writing pure Python functions.  
However, tools can be very flexible. Here are some more examples.

### Return the output directly

The `@tool` decorator accepts an optional boolean argument that is `@tool(return_direct=True)`.
This is set to `False` by default, which means the tool output is parsed again by the LLM.
Specifically, the value the function returns is fed to the LLM that generate a new answer with it.
When set to `True`, the returned value is printed in the chat as-is.  

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

### Complex input tools

We can make the `convert_currency` tool more flexible allowing the user to choose among a fixed set of currencies.

```python
from cat.mad_hatter.decorators import tool

@tool
def convert_currency(tool_input, cat): # (1)
    """Useful to convert currencies. This tool converts euro (EUR) to a fixed set of other currencies.
    Chooses are: US dollar (USD), English pounds (GBP) or Japanese Yen (JPY).
    Inputs are two values separated with a minus: the first one is an integer or floating point number;
    the second one is a three capital letters currency symbol.""" # (2)
    
    # Parse the input
    eur, currency = tool_input.split("-") # (3)
    
    # Define fixed rates of change
    rate_of_change = {
        "USD": 1.07,
        "GBP": 0.86,
        "JPY": 150.13
    }
    
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

As you may see, the LLM correctly understands the desired output from the docstring. Then, it is up to us parse the two inputs correctly for our tool.

### External library & the cat parameter

Tools are extremely flexible as they allow to exploit the whole Python ecosystem of packages.
Thus, you can update our tool making use of the [Currency Converter](https://github.com/alexprengere/currencyconverter) package.
To deal with [dependencies](dependencies.md), you need write the 'currencyconverter' library in a `requirements.txt` inside the `myplugin` folder.  
Moreover, here is an example of how you could use the `cat` parameter passed to the tool function.

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

    # Use the LLM to convert the currency name into its symbol
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

## References

[^1]:Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., ... & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761.
