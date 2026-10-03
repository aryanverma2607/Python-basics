from pathlib import Path
import ast
import subprocess
import sys

def analyze_error(path):
    path=Path(path)
    with open(path,"r") as f:
        code=f.read()
    try:
        ast.parse(code)
        print("\n========== ERROR REPORT ==========\n")
        print("no syntax error found")
    except SyntaxError as e:
        print("\n========== ERROR REPORT ==========\n")
        print("error type :",type(e).__name__)
        print("line :",e.lineno)
        print("Column:", e.offset)
        print("Message:", e.msg)
        print("Category: Syntax Error")
        
        return {
        "type": type(e).__name__,
        "line": e.lineno,
        "column": e.offset,
        "message": e.msg,
        "category": "Syntax Error"}
    pack=[]
    current=path.parent
    while (current/"__init__.py").exists():
        pack.insert(0,current.name)
        current=current.parent
    if pack:
        module_name=".".join(pack+[path.stem])
        result = subprocess.run(
            [sys.executable, "-m", module_name],
            cwd=current,
            capture_output=True,
            text=True
    )
    else:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True
        )
    print("\n========== ERROR REPORT ==========\n")
    if result.returncode==0:
        print("no error found")
        return {
        "type": None,
        "message": "No error found",
        "category": "No Error"}
    else:
        lines=result.stderr.splitlines()
        error_line=lines[-1]
        error_type,message=error_line.split(":",1)
        error_type=error_type.strip()
        message=message.strip()
        print("error Type:",error_type)
        print("Message:",message)
        print("Category:","Runtime error")
        suggestion = "Check the error message"
        if error_type=="NameError":
            suggestion="Check whether the variable is defined"
        elif error_type=="ZeroDivisionError":
            suggestion="Check that you are not dividing by zero"

        elif error_type=="TypeError":
            suggestion="Check the data types"


        elif error_type=="IndexError":
            suggestion="Check the list index"
        print("Suggestion:", suggestion)

        return {
        "type": error_type,
        "message": message,
        "category": "Runtime Error",
        "suggestion": suggestion
    }