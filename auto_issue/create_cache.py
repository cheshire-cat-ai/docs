import os
import glob
import json
import argparse
import ast


def list_functions_from_ast(module_path):
    with open(module_path, 'r') as file:
        tree = ast.parse(file.read(), filename=module_path)

    # Extract function names from the AST
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    return functions


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", action="append", required=True)

    args = parser.parse_args()

    hooks_file = "auto_issue/hooks.json"
    hooks = {"documented": []}
    with open("auto_issue/hooks.json", "w") as f:
        for path in args.paths:
            if not os.path.isfile(path):
                for module in glob.glob(os.path.join(path, "*.py")):
                    functions = list_functions_from_ast(module)
                    hooks["documented"].extend(functions)
            else:
                functions = list_functions_from_ast(path)
                hooks["documented"].extend(functions)

        json.dump(hooks, f)
