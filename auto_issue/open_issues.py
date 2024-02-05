import os
import glob
import json
import inspect
import argparse
import requests
import importlib.util

URL = "https://api.github.com/repos/cheshire-cat-ai/docs/import/issues"


def list_functions(module_path):
    # Load the module from the specified path
    spec = importlib.util.spec_from_file_location("module_name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all members (functions, classes, etc.) of the module
    members = inspect.getmembers(module)

    # Filter out only functions
    functions = [member[0] for member in members if inspect.isfunction(member[1])]

    return functions


def open_issue(functions):
    with open("auto_issue/hooks.json", "r") as file:
        hooks = json.load(file)

    for func in functions:
        if func not in hooks["documented"]:
            title = f"Add hook `{func}` to hooks' table"
            data = {
                "issue": {
                    "title": title,
                    "body": ""
                }
            }
            payload = json.dumps(data)
            response = requests.post(
                url=URL, headers=headers, data=payload
            )
            if not response.status_code == 202:
                print(f"Hook {func} unsuccessful")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", action="append")
    parser.add_argument("--token", type=str)

    args = parser.parse_args()

    headers = {
        "Authorization": f"token {args.token}",
        "Accept": "application/vdn.github.golden-comet-preview+json"
    }

    for path in args.paths:
        if os.path.isdir(path):
            for module in glob.glob(os.path.join(path, "*.py")):
                functions = list_functions(module)
                open_issue(functions)
        else:
            functions = list_functions(path)
            open_issue(functions)
