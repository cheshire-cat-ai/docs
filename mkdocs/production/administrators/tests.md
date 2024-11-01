# &#128300; Testing

Tests will run with mock databases and a mock plugin folder, so your instance will not be impacted.
End to end (e2e) tests are found in `tests/routes`, while all the other folders contain unit tests and mocks / utilities.

## Run all tests

Open a terminal in the same folder your Cat is, then launch:

```bash
docker compose run --rm cheshire-cat-core python -m pytest --color=yes .
```

## Run a specific test file

If you want to run specific test files and not the whole suite, just specify the path:

```bash
docker compose run --rm cheshire-cat-core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py
```

## Run a specific test function in a specific test file

You can also launch only one specific test function, using the `::` notation and the name of the function:

```bash
docker compose run --rm cheshire-cat-core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py::test_memory_recall_with_k_success
```
