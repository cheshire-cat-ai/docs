# Cheshire Cat AI — Documentation

The docs site is built with [Astro Starlight](https://starlight.astro.build/) and
published to GitHub Pages at <https://cheshire-cat-ai.github.io/docs/>.

## 📚 How to Contribute

1. Fork the repository and branch off `main`.
2. Edit or add Markdown files under `src/content/docs/`. Each page needs a
   `title` in its frontmatter; the sidebar lives in `astro.config.mjs`.
3. Co-locate images under `src/content/docs/assets/img/` and reference them with
   relative paths — Astro optimizes them automatically.
4. Commit, push, and open a pull request against `main`.

There is a [dedicated channel for Docs on our Discord](https://discord.com/channels/1092359754917089350/1092360068269359206) — don't be shy if you need help!

## 🛠️ Develop

```bash
npm install      # install dependencies
npm run dev      # local dev server with hot reload, at /docs/
npm run build    # production build into dist/
npm run preview  # preview the production build
```

Requires Node.js 22+.

## ✍️ Authoring notes

- **Callouts** use Starlight asides: `:::note`, `:::tip`, `:::caution`, `:::danger`.
- **Tabs** use the `<Tabs>` / `<TabItem>` components (in `.mdx` files).
- **Diagrams** use Mermaid — just fence a code block with ` ```mermaid `.

## 🔀 Versioning

The published site hosts two versions, selectable from the switcher in the sidebar:

- **v2 (latest)** — this repository, served at `/docs/`.
- **v1** — the previous docs, already deployed and left untouched at `/docs/1/`.

The deploy workflow (`.github/workflows/main.yml`) rebuilds v2 on every push to
`main` and preserves the existing `/1/` folder on the `gh-pages` branch.
