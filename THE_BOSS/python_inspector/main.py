# PYCODE_INSPECTOR/
# │
# ├── pycode_inspector.py      # Entry point
# │
# ├── file_scanner.py         # Feature 1
# ├── code_analyzer.py        # Feature 2
# ├── quality_checker.py      # Feature 3
# ├── identifier_checker.py   # Feature 4
# ├── error_analyzer.py       # Feature 5
# ├── code_runner.py          # Feature 6
# └── report.py               # Feature 7

# | #     | File                    | Feature                                                  | Main modules                     |
# | ----- | ----------------------- | -------------------------------------------------------- | -------------------------------- |
# | **1** | `file_scanner.py`       | 📁 File & Folder Scan                                    | `pathlib`, `os`                  |
# | **2** | `code_analyzer.py`      | 🔍 Code Analysis                                         | `ast`                            |
# | **3** | `quality_checker.py`    | 🧠 Code Quality & Suggestions                            | `ast`                            |
# | **4** | `identifier_checker.py` | 🏷️ Identifier Analysis                                  | `ast`, `re`                      |
# | **5** | `error_analyzer.py`     | ❌ Error Detection & Explanation                          | `ast`, `subprocess`, `traceback` |
# | **6** | `code_runner.py`        | ▶️ Code Execution                                        | `subprocess`, `time`             |
# | **7** | `report.py`             | 📊 Statistics + Complete Terminal Report + Visualization | `ast`, `rich`                    |
# | —     | `pycode_inspector.py`   | 🚀 Entry Point / Controller                              | `sys`                            |


# from identifier_checker import analyze_file
# from error_analyzer import analyze_error
# from code_runner import run_code
# from report import generate_report
# from visualization import show_test_result

# path = input("ENTER PYTHON FILE: ")

# # analyze_file(path)
# # analyze_error(path)
# # run_code(path)
# generate_report(path)
from .file_scanner import scan_file
from pathlib import Path
from .error_analyzer import analyze_error
from .code_runner import run_code
from .identifier_checker import analyze_file
from .report import generate_report
from .visualization import show_test_result
def inspect(path):
    print(f"""\n======================\n
          PYTHON INSPECTOR
          ============================
          """)
    files=scan_file(path)
    if not files:
        print("NO PYTHON FILES FOUND.")
        return
    print("\nPYTHON FILES FOUND")
    print("-"*7)
    for i in files:
        print(i)

    file_name=input("enter the python file name:")
    selected_file=None
    for i in files:
        if Path(i).name==file_name:
            selected_file=i
            break
    else:
        print("file not found.")
        return
    print("\n selecteed file :",selected_file)

    error_choice=input("DO YOU WANT TO CHECK ERROS?{Y/N}:")
    error_data = None
    if error_choice.lower()=="y":
        error_data=analyze_error(selected_file)
    test_data=None
    test_choice = input("\nDO YOU WANT TO RUN TEST CASES? (Y/N): ")
    if test_choice.lower()=="y":
        if error_data is None:
            error_data=analyze_error(selected_file)
        if error_data["category"].lower()=="no error":
            test_data=run_code(selected_file)
        else:
            print("test cases cannot be executed because of an error was found")

    try:
        analysis_data = analyze_file(selected_file)
    except SyntaxError:
        analysis_data=None
    generate_report(
        path,files,analysis_data,error_data,test_data)
    if analysis_data:
        show_test_result(files, analysis_data)