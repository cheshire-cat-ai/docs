# &#128268; How to write a plugin

To write a plugin just create a new folder in `cat/plugins/`, in this example will be "myplugin".

You need two files into your plugin folder:

    ├── cat/
    │   ├── plugins/
    |   |   ├── myplugin/
    |   |   |   ├── mypluginfile.py
    |   |   |   ├── plugin.json

The `plugin.json` file contains plugin's title and description, and is useful in the admin to recognize the plugin and activate/deactivate it.
If your plugin does not contain a `plugin.json` the cat will not block your plugin, but it is useful to have it.

`plugin.json` example:

```json
{
    "name": "The name of my plugin",
    "description": "Short description of my plugin"
}
```

Now let's start `mypluginfile.py` with a little import:

```python
from cat.mad_hatter.decorators import tool, hook
```

You are now ready to change the Cat's behavior using Tools and Hooks.

## &#129520; Tools

Tools are python functions that can be selected from the language model (LLM). Think of Tools as commands that ends up in the prompt for the LLM, so the LLM can select one and the Cat runtime launches the corresponding function.  
Here is an example of Tool to let the Cat tell you what time it is:

```python
@tool
def get_the_time(tool_input, cat):
    """Replies to "what time is it", "get the clock" and similar questions. Input is always None.."""

    return str(datetime.now())
```

More examples on tools [here](tools.md).

## &#129693; Hooks

Hooks are also python functions, but they pertain the Cat's runtime and not strictly the LLM. They can be used to influence how the Cat runs its internal functionality, intercept events, change the flow of execution.  

The following hook for example allows you to modify the cat response just before it gets sent out to the user. In this case we make a "grumpy rephrase" of the original response.

```python
@hook
def before_cat_sends_message(message, cat):

    prompt = f'Rephrase the following sentence in a grumpy way: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message
```

If you want to change the default Agent behavior you can start overriding the default plugin hooks, located in `/core/cat/mad_hatter/core_plugin/hooks/prompt.py`, rewriting them in the plugin file with a higher priority.
Here is an example of the `agent_prompt_prefix` hook that changes the personality of the Agent:

```python
# Original Hook, from /core/cat/mad_hatter/core_plugin/hooks/prompt.py

@hook(priority=0)
def agent_prompt_prefix(prefix, cat):
    prefix = """You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
                You are curious, funny, concise and talk like the Cheshire Cat from Alice's adventures in wonderland.
                You answer Human using tools and context."""
```

```python
# Modified Hook, to be copied into mypluginfile.py

@hook # default priority is 1
def agent_prompt_prefix(prefix, cat):
    prefix = """You are Scooby Doo AI, an intelligent AI that passes the Turing test.
                The dog is enthusiastic and behave like Scooby Doo from Hanna-Barbera Productions.
                You answer Human using tools and context."""
    return prefix
```

Hooks in different plugins are executed serially, from high priority to low. If you do not provide a priority, your hook will have `priority=1`.
More examples ans details on hooks [here](hooks.md).




## 📋 Forms

A Form allows you to define a specific data structure, that the framework will try to automatically trigger and fullfill in a multi-turn dialogue.
You can define custom:

 - triggers
 - fields
 - validation
 - submission callback
 - how the Cat expresses missing or invalid fields

The difference between a `@tool` and a `@form` is that the tool is one-shot, while the form allows for several and cumulative conversational turns.  
Imagine a Cat `@form` as the common HTML `<form>`, but on a conversational level.

Here is an example for a pizza order:

```python
from pydantic import BaseModel
from cat.experimental.form import form, CatForm

# data structure to fill up
class PizzaOrder(BaseModel):
    pizza_type: str
    phone: int

# forms let you control goal oriented conversations
@form
class PizzaForm(CatForm):
    description = "Pizza Order"
    model_class = PizzaOrder
    start_examples = [
        "order a pizza!",
        "I want pizza"
    ]
    stop_examples = [
        "stop pizza order",
        "not hungry anymore",
    ]
    ask_confirm = True

    def submit(self, form_data):
        
        # do the actual order here!

        # return to convo
        return {
            "output": f"Pizza order on its way: {form_data}"
        }
```

More examples on forms [here](forms.md).

## &#x1f310; Custom Endpoints

To extend the REST API endpoints available, use the [@endpoint](../production/network/http-endpoints.md) decorator in your plugin.

```python
from cat.mad_hatter.decorators import endpoint

@endpoint.get("/new")
def my_endpoint():
    return "meooow"
```

Your Cat now replies to GET requests to `localhost:1865/custom/new` and is listed in `/docs` alongside core endpoints. Being based on [FastAPI endpoints](https://fastapi.tiangolo.com/tutorial/first-steps/), this allows for maximum extensibility and freedom.  
You can add permissions to the endpoint and easily obtain the user session (what you saw above as `cat`), use the LLM or change the working memory.  
See more details and examples [here](endpoints.md).

## &#128570; StrayCat

You surely noticed that all the primitives listed above put at your disposal a variable called `cat`.
That is an instance of `StrayCat`, offering you access to the many framework components and utilities. Just to give an example, you can invoke the LLM directly using `cat.llm("write here a prompt")`.

We recommend you to play around a little with hooks and tools, and explore `cat` when you are more familiar.
See [examples](../framework/cat-components/cheshire_cat/stray_cat.md) on how to use `cat` in your plugins, and the full [`StrayCat` reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/looking_glass/stray_cat/).