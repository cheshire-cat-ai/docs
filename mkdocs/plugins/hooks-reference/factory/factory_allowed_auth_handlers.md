---
title: factory_allowed_auth_handlers
---

# `factory_allowed_auth_handlers`

Customize which AuthHandlers are available.

!!! info
    Useful to extend support for custom auth handlers. For more information see [Custom Auth](../../../production/auth/custom-auth.md)

## &#128196; Arguments

| Name      | Type                                                                    | Description                                                           |
|:----------|:------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `allowed` | `List[AuthHandlerConfig]`                                               | List of AuthHandlerConfig classes, contains the custom auth handlers. |
| `cat`     | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components.    |

## &#x21A9;&#xFE0F; Return

Type: `List[AuthHandlerConfig]`

The list of custom auth handlers.

## &#9997; Example

```python
from cat.mad_hatter.decorators import hook
from typing import List

@hook(priority=0)
def factory_allowed_auth_handlers(allowed: List[AuthHandlerConfig], cat) -> List:
    # Add your custom auth handler configuration here
    allowed.append(CustomAuthHandlerConfig)
    return allowed
```

!!! note
    - [Custom Auth](../../../production/auth/custom-auth.md)
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
