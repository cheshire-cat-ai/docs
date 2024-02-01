#  &#128075; Hello, Dear!

> Good documentation is *key* to a good software and at Cheshire Cat AI we are always looking for great community members that are willing to improve it with their writing skills. This README as well as all the documentation you can find about the [Cat](https://cheshire-cat-ai.github.io/docs/) is the result of an effort between our Core team and a great Community. Remember to always have fun whatever you decide to contribute to, meow.

# 📚 Ho to Contribute Documentation

1. Fork the repository.
2. Using Markdown syntax, edit or create new files for the documentation in the `/mkdocs` directory.
3. Use **headings**, **bullet points** or **numbered lists**, **code blocks** and other formatting tools to make the documentation easy to read and understand.
4. Use clear and concise language to explain the features, functions or concepts that are being documented.
5. Use hyperlinks, images or other visual aids to enhance the documentation.
6. Use the appropriate `/assets` folder for your static assets. Eg. Images goes under `/assets/img`.
7. Add a new item or adjust menu levels through the `mkdocs.yml` file if you have made any structural modifications.
8. When finished, commit and push your changes to your forked repository.
9. Open a pull request and ask for feedback from the community.
10. Keep your contributions up-to-date with any changes or updates made to the main repository.

There is a [dedicated channel for Docs on our official Discord](https://discord.com/channels/1092359754917089350/1092360068269359206), don't be shy and contact us there if you need help!

### &#129693; Hooks documentation

To help documenting the [hooks table](./mkdocs/technical/plugins/hooks.md#available-hooks), ensure these elements are not missing and please keep the order:

1. Annotation number with bold heading
2. *Input arguments* description with *code snippet* example
3. *optional*: any other **non collapsible** `warning` box/additional `info` for tips, tricks and discouraged behaviors (`!!! info`/`!!! warning`)
4. **collapsible** snippet example (`??? example`)
5. **collapsible** note section with title: `??? note "Other resources"` --> in this section please include the link to the hook Python reference in the documentation and any other useful links to other doc's pages.

Example:
```python
1. **Input arguments**
        `user_message_json`, i.e. the JSON message sent via WebSocket done like this:
        ```JSON
        {
            "text": # user's message here
        }
        ```

        !!! info
            Hook the incoming user message JSON dictionary

        ??? example

            ```python
            from cat.mad_hatter.decorators import hook

            @hook  # default priority = 1
            def before_cat_reads_message(user_message_json, cat):
                user_message_json["text"] = "The original message has been replaced"
                cat.working_memory["hacked"] = True

                return user_message_json
            ```

        ??? note "Other resources"

            - [Python reference]()
```

## 🤹 Manage the tecnology [mkdocs]

To modify the behavior of MkDocs and its plugins, everything you need is within the `mkdocs.yml` file.  
We invite you to read the documentation for the [MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/reference/) to fully understand all the potential of the tool and how to make the most of its extensive features.

### 📦 Requirements

- Python 3.8+
- Pip 20+

Install dependencies:

`pip install -r requirements.txt`

### 🛠️ Develop

`mkdocs serve` or `python -m mkdocs serve` will launch a local, non static, instance of the documentation website.

### 🖌️ Diagrams

All the diagrams under the "Framework/Technical Diagrams" section have been created using draw.io.
The file [drawio-cheshire-cat-library](drawio-cheshire-cat-library.xml) is a draw.io library, it contains some custom Cat shapes, this library has been created to speed up the sketching, you can use it opening the file with draw.io.
You can refer to the draw.io files with the extension `.drawio`, directly from the markdown files like this:
```
# &#128572; The Cat Bootstrap

This interactive diagram, zoomable with a click, depicts the internal process involved during bootstrap of the Cat:

![](../../assets/diagrams/cat-bootstrap.drawio)
```

In the `mkdocs.yml` there is defined the hook `drawio_file.py`, this mkdocs plugin converts the drawio files during the build time:
```
hooks:
  - mkdocs/hooks/drawio_file.py
```
  
Remember that:

- the tab selected during the save of the draw.io file, will become the initial page when the diagram is opened

- the layers visible during the save of the draw.io files, will be the default visible layers when the diagram is opened
  
- by default, the hooks shapes have to be visible.

### 🏗️ Build

The build stage is automated using GitHub action, you don't need to do it in order to contribute. However, if you want to have a static copy of the documentation on your local machine you are free to do it.  

`mkdocs build` or `python -m mkdocs build` will create the actual docs static website in a folder named `/docs`. 
