# &#127898; Plugin Settings

Your plugin may need a set of options, to make it more flexible and customizable.  
It is possible to easily define settings for your plugin, so the Cat can show them in the admin interface.

## Settings schema

By defining the `settings_schema` function and decorating it with `@plugin` you can tell the Cat how your settings are named, what is their type and (if any) their default values.  
The function must return a [JSON Schema](https://json-schema.org/) for the settings. You can code the schema manually, load it from disk, or obtain it from a [pydantic](https://docs.pydantic.dev/latest/usage/json_schema/) class (recommended approach).
Here is an example with all supported types, with and without a default value:

```python
from pydantic import BaseModel
from enum import Enum
from datetime import date, time
from cat.mad_hatter.decorators import plugin


# select box
#   (will be used in class DemoSettings below to give a multiple choice setting)
class NameSelect(Enum):
    a: str = 'Nicola'
    b: str = 'Emanuele'
    c: str = 'Daniele'


# settings
class DemoSettings(BaseModel):

    # Integer
    #   required setting
    required_int: int
    #   optional setting, with default value
    optional_int: int = 42

    # Float
    required_float: float
    optional_float: float = 12.95
    
    # String
    required_str: str
    optional_str: str = "stocats"
    
    # Boolean
    required_bool: bool
    optional_bool_true: bool = True
    
    # Date
    required_date: date
    optional_date: date = date(2020, 11, 2)

    # Time
    required_time: time
    optional_time: time = time(4, 12, 54)

    # Select
    required_enum: NameSelect
    optional_enum: NameSelect = NameSelect.b


# Give your settings schema to the Cat.
@plugin
def settings_schema():   
    return DemoSettings.schema()

```

## Change Settings from the Admin

Now go to the admin in `Plugins` page and click the cog near the activation toggle:

![Open settings](../../assets/img/admin_screenshots/plugin_settings/settings.png)

A side panel will open, where you and your plugin's users can choose settings in a comfy way.

<figure markdown>
  ![Form part 1](../../assets/img/admin_screenshots/plugin_settings/form1.png){ width="500" }
</figure>

<figure markdown>
  ![Form part 2](../../assets/img/admin_screenshots/plugin_settings/form2.png){ width="500" }
</figure>

## Access settings from within your plugin

Obviously, you need easy access to settings in your plugin code.
First of all, note that the cat will, by default,
save and load settings from a `settings.json` file which will automatically be created in the root folder of your plugin.

So to access the settings, you can load them via `mad_hatter`.
More in detail, from within a hook or a tool, you have access to the `cat` instance, hance, do the following:

 ```python
settings = cat.mad_hatter.get_plugin.load_settings()
 ```

Similarly, you can programmatically save your settings as follows:

 ```python
settings = cat.mad_hatter.get_plugin.save_settings(settings)
 ```

where `settings` is a dictionary, a JSON schema or a Pydantic `BaseModel` describing your plugin's settings.

## Advanced settings save / load


If you need even more customization for your settings you can totally override how they are saved and loaded.
Take a look at the `save_settings` and `load_settings` functions (always to be decorated with `@plugin`).  
From there you can call external servers or devise a totally different format to store and load your settings. The Cat will call those functions and delegate to them how settings are managed instead of using a `settings.json` file.