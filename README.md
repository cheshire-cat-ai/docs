## 📚 How to Contribute Documentation

1. Fork the repository and branch off `main`.
2. Edit or add Markdown files in the `/mkdocs` directory. Use headings, lists, code blocks and visual aids to keep things clear and concise.
3. Put static assets in the relevant `/assets` folder (e.g. images under `/assets/img`).
4. If you change the structure, update the menu in `mkdocs.yml`.
5. Commit, push, and open a pull request against `main`.

There is a [dedicated channel for Docs on our official Discord](https://discord.com/channels/1092359754917089350/1092360068269359206), don't be shy and contact us there if you need help!

## 🤹 Manage the technology [mkdocs]

To modify the behavior of MkDocs and its plugins, everything you need is within the `mkdocs.yml` file.
We invite you to read the documentation for the [MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/reference/) to fully understand the tool and make the most of its features.

### 📦 Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

Install dependencies:

`uv sync`

### 🛠️ Develop

`uv run mkdocs serve` will launch a local, non-static instance of the documentation website.

### 🖌️ Diagrams

All the diagrams under the "Framework/Technical Diagrams" section have been created using draw.io.
The file [drawio-cheshire-cat-library](drawio-cheshire-cat-library.xml) is a draw.io library, it contains some custom Cat shapes, this library has been created to speed up the sketching, you can use it opening the file with draw.io.
You can refer to the draw.io files with the extension `.drawio`, directly from the markdown files like this:

```mk
# &#128572; The Cat Bootstrap

This interactive diagram, zoomable with a click, depicts the internal process involved during bootstrap of the Cat:

![](../../assets/diagrams/cat-bootstrap.drawio)
```

In the `mkdocs.yml` there is defined the hook `drawio_file.py`, this mkdocs plugin converts the drawio files during the build time:

```mk
hooks:
  - mkdocs/hooks/drawio_file.py
```

Remember that:

- the tab selected during the save of the draw.io file, will become the initial page when the diagram is opened

- the layers visible during the save of the draw.io files, will be the default visible layers when the diagram is opened

- by default, the hooks shapes have to be visible

- the folder `mkdocs/assets/img/diagrams` contains the svg files used in the main diagram pages, in case you change the diagrams remember to update them.

### 🏗️ Build

The build stage is automated using GitHub Actions, you don't need to do it in order to contribute. However, if you want a static copy of the documentation on your local machine you are free to do it.

`uv run mkdocs build` will create the docs static website in a folder named `/docs`.
