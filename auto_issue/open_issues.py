import os
import ast
import glob
import json
import argparse
import requests

URL = "https://api.github.com/repos/cheshire-cat-ai/docs/import/issues"


def list_functions_from_ast(module_path):
    with open(module_path, 'r') as file:
        tree = ast.parse(file.read(), filename=module_path)

    # Extract function names from the AST
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    return functions


def open_issue(functions):
    with open("auto_issue/hooks.json", "r") as file:
        hooks = json.load(file)

    for func in functions:
        if func not in hooks["documented"]:
            print(f"Opening issue for {func}")
            title = f"Add hook `{func}` to hooks' table"
            data = {
                "issue": {
                    "title": title,
                    "body": f"Add hook `{func}` to the table"
                }
            }
            payload = json.dumps(data)
            response = requests.post(
                url=URL, headers=headers, data=payload
            )
            if response.status_code == 202:
                hooks["documented"].append(func)
            else:
                print(f"Hook {func} unsuccessful")
                print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", action="append")
    parser.add_argument("--token", type=str)

    args = parser.parse_args()

    headers = {
        "Authorization": f"token {args.token}",
        "Accept": "application/json"
    }

    for path in args.paths:
        if os.path.isdir(path):
            for module in glob.glob(os.path.join(path, "*.py")):
                functions = list_functions_from_ast(module)
                open_issue(functions)
        else:
            functions = list_functions_from_ast(path)
            open_issue(functions)
