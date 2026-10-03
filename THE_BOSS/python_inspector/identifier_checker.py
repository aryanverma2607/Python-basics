from pathlib import Path
import ast
def analyze_file(path):

    path = Path(path)

    with open(path, "r") as f:
        code = f.read()

    tree = ast.parse(code)
    functions=[]
    classes=[]
    variables=[]
    paramters=[]
    imports=[]
    calls=[]


    for node in ast.walk(tree):
        if isinstance (node,ast.FunctionDef):
            functions.append(node.name)
            for arg in node.args.args:
                paramters.append(arg.arg)

        elif isinstance(node,ast.ClassDef):
            classes.append(node.name)
            # for item in node.body:
            #     if isinstance(item, ast.FunctionDef):
            #         print("  Method:", item.name)

        elif isinstance(node,ast.Name):
            if isinstance(node.ctx, ast.Store):
                variables.append(node.id)

        elif isinstance(node,ast.Import):
            for name in node.names:
                imports.append(name.name)

        elif isinstance(node,ast.ImportFrom):
            for name in node.names:
                if node.module:
                    imports.append(node.module + "." + name.name)
                else:
                    imports.append(name.name)

        elif isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name):
                calls.append(node.func.id)

            elif isinstance(node.func,ast.Attribute):
                calls.append(node.func.attr)
    return {
        "functions": functions,
        "classes": classes,
        "variables": variables,
        "parameters": paramters,
        "imports": imports,
        "calls": calls
    }
