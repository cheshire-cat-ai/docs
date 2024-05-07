# 📋 Forms

Forms are Particular Tools useful to collect users' information during the given conversation!



## How the Forms work

Imagine a scenario where you need to create an Order system for a pizzeria, using only the conversation of the user. The user must provide 3 information:

1. Type of pizza, must be a string in a restrictive set
2. Phone number, must be 10 numbers long and restrictive to a specific dialling code
3. Address, must be a valid address of "Milano"

How can I resolve this problem? Well, these type of information are **very specific**:

- need [**validators**](https://docs.pydantic.dev/latest/concepts/validators/#field-validators) (Phone numbers can be of different structure based on the country, the pizzeria has a menu of pizzas, you can deliver only in a certain area of the city)
- **can be provided in different orders** (A user can give the address before the type of pizza!).

This is where the forms comes handy!

## Implementation

```python

class PizzaOrder(BaseModel): #(1)
    pizza_type: str
    phone: str
    address: str


@form #(2)
class PizzaForm(CatForm): #(3)
    description = "Pizza Order" #(4)
    model_class = PizzaOrder #(5)
    start_examples = [ #(6)
        "order a pizza!",
        "I want pizza"
    ]
    stop_examples = [ #(7)
        "stop pizza order",
        "not hungry anymore",
    ]
    ask_confirm = True #(8)

    def submit(self, form_data): #(9)
        
        # do the actual order here!
        # Fake call
        out = request.post("https://fakecallpizza/order",{
            "pizza_type": form_data.pizza_type,
            "phone": form_data.phone,
            "address": form_data.address
        })

        if(out.status_code != 201):
            raise Exception()
        
        time = out.json()["estimatedTime"]

        # return to conversation
        return {
            "output": f"Pizza order on its way: {form_data}. Estimated time: {time}"
        }

```

1. Pydantic class representing the information you need to retrive.
2. Every class decorated with `@forms` is a Form.
3. Every Form must inherit from `CatForm`.
4. Description of the Form. <!-- , useful to the [tool chain](/conceptual/cheshire_cat/tool_chain/). Is necessary, as it will show up in the Tool chain prompt. It should describe what the form is useful for, so the LLM can select the tool and input it properly. -->
5. Pydantic class name.
6. Every Form must have a list of *start examples*, so the LLM can select the form properly. It's the same principal of tool's docstring.
7. Every Form must have a list of *stop examples*, so the LLM can stop properly the form during the conversation.
8. Every Form can ask the user confirmation of the data provided.
9. Every Form must overload this method and the fuctionality is the same as tools: call database to collect the information, call the Order API, call another agent or LLM etc..

## Changing the "moves" of the Form

Forms are implemented as [FSM](https://en.wikipedia.org/wiki/Finite-state_machine) and you can change any move of the FSM by overloading the methods.

Here the diagram of the FSM:
TODO

### State-transition function

Each FSM has a State-Transition function that describes what is the next move to perform based on the given input. In the case of Form's implementation the input is the **User prompt** and the `def next(self)` method is State-Transition function.

The form has 4 states to be evaluated:

1. INCOMPLETE
2. WAIT_CONFIRM
3. CLOSED
4. COMPLETE

each state executes one or more Phases:

- User Stop Confirmation Phase
- User Confirmation Phase
- Updating Phase
- Visualization Phase
- Submit Phase

You can change this state-transition by overloading the method `def next(self)` and accessing the state by `self._state`. The states are values from the `CatFormState` enum.

### User Stop Confirmation Phase

The User Stop Confirmation phase is where the Form produces a prompt to ask the user his willingness to continue. You can change this phase by overloading the method `def check_exit_intent(self)`.

### User Confirmation Phase

The User Confirmation Phase is where the Form produces a prompt to ask confirmation of the information provided by the user, if `ask_confirm` is true. You can change this phase by overloading the method `def confirm(self)`.

### Updating Phase

The Updating Phase is where the Form executes the Extraction Phase, Sanitization Phase and Validation Phase. You can change this phase by overloading the method `def update(self)`.

#### Extraction Phase

The Extraction Phase is where the Form extracts all possibile information from the user's prompt. You can change this phase by overloading the method `def extract(self)`.

#### Sanitization Phase

The Sanitization Phase is where the information is sinitized from unwanted values (null, None, '', ' ', etc...). You can change this phase by overloading the method `def sanitize(self, model)`

#### Validation Phase

The Validation Phase is where the Form attempts to construct the model, so pydantic can use the validators implemented and check each field. You can change this phase by overloading the method `def valdiate(self, model)`

### Visualization Phase

The Visualization Phase is where the Form displays a message to the user, showing the model's status.

By default the cat shows the forms like so ![display form](../../assets/img/technical/forms/how_is_display.png)

When there is invalid info that was retrived from the conversation, the cat tells you exacly which and what issue ![display invalid info](../../assets/img/technical/forms/how_invalid_is_display.png)

You can change this phase by overloading the method `def message(self)`:

```python
    #in the form you define 
    def message(self): #(1) 
        if self._state == CatFormState.CLOSED: #(2)
            return {
                "output": f"Form {type(self).__name__} closed"
            }
        missing_fields: List[str] = self._missing_fields #(3)
        errors: List[str] = self._errors #(4)
        out: str = f"""
        the missing information are: {missing_fields}.
        this are the invalid ones: {errors}
        """
        if self._state == CatFormState.WAIT_CONFIRM:
            out += "\n --> Confirm? Yes or no?"

        return {
            "output": out
        }

```

1. This method is useful to change the Form visualization.
2. Forms have states that can be checked.
3. Forms can access the list of the missing fields.
4. Forms can access the list of the invalid fields and the correlated errors.

### Final Phase: Submit

The Submit Phase is where the Form conclude the journey by executing all defined instructions with the information gathered from the user's conversation.
The method have two params:

- **self** (You can access information about the form and the `StrayCat` instance)
- **form_data** (The defined pydantic model)  
And must return a Dict where the value of key `output` is a string that will be displayed in the chat.

If you need to use the Form in future conversations, you can retrive the model from the working memory by accessing the key `form`.

Below an example:

```python
    @hook  
    def before_cat_sends_message(message, cat):
        form_data = cat.working_memory["form"]
```
