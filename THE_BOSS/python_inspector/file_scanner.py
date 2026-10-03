from pathlib import Path
import os


ignore_folders = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "env",
    ".env",
    "node_modules"
}
def scan_file(path):
    path=Path(path)
    if not path.exists():
        print("Invalid path")
        return[]

    if path.is_file():
        if path.suffix==".py":
            return [path]
        else:
            print("not a python file")
            return[]
    py_files=[]
    print(path.name+"/")
    for root, folders, files in os.walk(path):
            for folder in folders.copy():
                if folder in ignore_folders:
                    folders.remove(folder)
            root=Path(root)
            level=len(root.relative_to(path).parts)
            indent="|  "*(level)
            for folder in folders:
                print(indent + "├── " + folder + "/")

            for file in files:
                print(indent + "├── " + file)
                if file.endswith(".py"):
                    py_files.append(root/file)
    return py_files

