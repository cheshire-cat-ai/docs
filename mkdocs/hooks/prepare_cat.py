"""Materialise a griffe-friendly copy of the `cat` package for the API docs.

v2 core ships `cat/` as a *regular* package (it has a top-level ``__init__.py``),
but its subpackages (``looking_glass``, ``memory``, ...) are implicit *namespace*
packages with no ``__init__.py``. griffe / mkdocstrings will not descend into
those subpackages while the top-level package is "regular", so collecting e.g.
``cat.looking_glass.cheshire_cat`` fails and the whole build aborts.

Dropping the top-level ``__init__.py`` turns the entire tree into a namespace
package, which restores discovery (this is how the v1 package was laid out).

We never mutate the source: we copy it into a local, git-ignored ``cat/`` and
strip the top-level ``__init__.py`` there. The source is resolved, in order, from:

1. the target of an existing ``cat`` symlink (the convenient local-dev setup),
2. the ``$CAT_SRC`` environment variable,
3. ``./core/src/cat``    (the core repo checked out next to the docs in CI),
4. ``../core/src/cat``   (a sibling core repo, the usual local layout).

If no source is found the hook does nothing and ``gen_pages.py`` emits a
placeholder, so the docs still build (just without the API reference).
"""

import os
import shutil
from pathlib import Path

DEST = Path("cat")


def _find_source():
    if DEST.is_symlink():
        return DEST.resolve()
    for candidate in (os.environ.get("CAT_SRC"), "core/src/cat", "../core/src/cat"):
        if candidate and Path(candidate).exists():
            return Path(candidate).resolve()
    return None


def on_config(config, **kwargs):
    src = _find_source()
    if src is None or not src.exists():
        return config

    # Replace ./cat with a fresh, namespace-package copy of the source.
    if DEST.is_symlink() or DEST.is_file():
        DEST.unlink()
    elif DEST.exists():
        shutil.rmtree(DEST)
    shutil.copytree(src, DEST)

    top_init = DEST / "__init__.py"
    if top_init.exists():
        top_init.unlink()

    return config
