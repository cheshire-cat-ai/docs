# &#128300; Testing

To run tests, start the Cat as usual.  
Tests will run on the same container you already launched, but with mock databases and plugin folder.
End to end (e2e) tests are found in `tests/routes`, while all the other folders contain unit tests and mocks / utilities.

## Run all tests

Open another terminal (in the same folder from where you start the Cat) and launch:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes .
```

## Run a specific test file

If you want to run specific test files and not the whole suite, just specify the path:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py
```

## Run a specific test function in a specific test file

You can also launch only one specific test function, using the `::` notation and the name of the function:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py::test_memory_recall_with_k_success
```