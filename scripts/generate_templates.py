import os
import ast
from typing import List


def extract_imports(tree: ast.Module) -> List[str]:
    imports = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.unparse(node))
    return imports


def extract_function_signature(node: ast.FunctionDef) -> str:
    args = ", ".join(arg.arg for arg in node.args.args)
    returns = ""
    if node.returns:
        returns = f" -> {ast.unparse(node.returns)}"
    return f"def {node.name}({args}){returns}:"


def process_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        content = f.read()

    tree = ast.parse(content)

    imports = extract_imports(tree)
    new_content = imports + [""]  # Add an empty line after imports

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            signature = extract_function_signature(node)
            docstring = ast.get_docstring(node)
            new_content.append(signature)
            if docstring:
                new_content.append(f'    """{docstring}"""')
            new_content.append("    # TODO: Implement this function")
            new_content.append("    pass\n")

    return "\n".join(new_content)


def generate_templates(src_dir: str) -> None:
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                file_path = os.path.join(root, file)
                new_content = process_file(file_path)

                # Write the new content to the same file
                with open(file_path, "w") as f:
                    f.write(new_content)


def main() -> None:
    src_dir = "src"
    generate_templates(src_dir)
    print("Template files generated successfully.")


if __name__ == "__main__":
    main()
