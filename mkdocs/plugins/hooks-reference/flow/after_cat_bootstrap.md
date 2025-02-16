---
title: after_cat_bootstrap
---

# `after_cat_bootstrap(cat)`

Intervene after the Cat has instantiated its components.

Bootstrapping is the process of loading the plugins, the natural language objects (e.g., the LLM), the memories,
the *Main Agent*, the *Rabbit Hole* and the *White Rabbit*.

This hook allows intercepting the end of this process and is executed right after the Cat has finished loading
its components.

This can be used to set or store variables to be shared further in the pipeline.

## &#x1F4C4; Arguments

This hook has no input arguments, other than the default cat:

| Name  | Type                                                                    | Description                                                        |
|:------|:------------------------------------------------------------------------|--------------------------------------------------------------------|
| `cat` | [StrayCat](../../../framework/cat-components/cheshire_cat/stray_cat.md) | Cheshire Cat instance, allows you to use the framework components. |

## &#x21A9;&#xFE0F; Return

Returns? Oh no, dear developer, this function is a one-way trip into the rabbit hole.

## &#x270D; Example

```python
from cat.mad_hatter.decorators import hook

@hook  # default priority = 1
def after_cat_bootstrap(cat):
    # do whatever here
```

!!! note
    - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_bootstrap)
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
