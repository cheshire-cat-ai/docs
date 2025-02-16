---
title: before_cat_bootstrap
---

# `before_cat_bootstrap(cat)`

Intervene before the Cat has instantiated its components.

!!! warning
    Please, note that at this point the [`CheshireCat`](/docs/API_Documentation/looking_glass/cheshire_cat) hasn't yet finished to instantiate 
    and the only already existing component is the [`MadHatter`](../../../framework/cat-components/cheshire_cat/mad_hatter.md) (e.g. no language models yet).

Bootstrapping is the process of loading the plugins, the natural language objects (e.g. the LLM), the memories,
the *Main Agent*, the *Rabbit Hole* and the *White Rabbit*.

This hook allows to intercept such process and is executed in the middle of plugins and
natural language objects loading.

This hook can be used to set or store variables to be propagated to subsequent loaded objects.

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
def before_cat_bootstrap(cat):
    # do whatever here
```

!!! note
    - [Python reference](https://cheshire-cat-ai.github.io/docs/API_Documentation/mad_hatter/core_plugin/hooks/flow/#cat.mad_hatter.core_plugin.hooks.flow.before_cat_bootstrap)
    - [Debugger plugin](https://github.com/sambarza/cc-vscode-debugpy)
