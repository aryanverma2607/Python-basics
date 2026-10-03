# Enter number of test cases: 3

# ========== TEST CASE 1 ==========
# Enter input: 10
# 20
# Enter expected output: 30

# ========== TEST CASE 2 ==========
# Enter input: 5
# 7
# Enter expected output: 12

# ========== TEST CASE 3 ==========
# Enter input: 100
# 50
# Enter expected output: 150


# ========== TEST CASE 1 ==========

# Expected Output:
# 30

# Actual Output:
# 30

# ✅ PASSED
# ================================
#          FINAL RESULT
# ================================

# Total Test Cases : 3
# Passed           : 3
# Failed           : 0

# ✅ ALL TEST CASES PASSED

from pathlib import Path
import subprocess
import sys
from .visualization import show_result
import winsound
def run_code(path):
    path=Path(path)
    # result = subprocess.run(
    #     [sys.executable, str(path)],
    #     capture_output=True,
    #     text=True
    # )

    # if result.returncode !=0:
    #     print("\n========code runner=========\n")
    #     print("Runtime error found")
    #     print(result.stderr)
    #     print("Test cases cannot be executed.")
    #     return
    # print("\n========code runner=========\n")
    # print("code executed successfully.")
    print("\n======== CODE RUNNER =========\n")
    n=int(input("enter number of test cases :"))

    passed=0
    failed=0

    for i in range(1,n+1):
        print(f"\n========== TEST CASE {i} ==========")
        user_input=[]

        print("enter the input:")

        while True:
            value=input()
            if value.lower()=="end":
                break
            user_input.append(value)
        input_data="\n".join(user_input)
        expected_output=[]
        print("enter expected output:")
        while True:
            value=input()
            if value.lower()=="end":
                break
            expected_output.append(value)

        expected="\n".join(expected_output)

        test_result=subprocess.run(
            [sys.executable,str(path)],
            input=input_data,
            capture_output=True,
            text=True
        )
        actual=test_result.stdout.strip()
        print(f"\n========== TEST CASE {i} RESULT ==========")
        print("Expected Output :")
        print(expected)

        print("\n Actual output :")
        print(actual)
        if test_result.returncode !=0:
            print("runtime error")
            print(test_result.stderr)
            failed+=1
        elif actual==expected:
            print("PAssed")
            passed+=1
        else:
            print("\n failed")
            failed+=1
            print("\nPossible Cause : Output does not match expected output")
            print("Suggestion     : Check the program logic and data types")
        
    print("""\n=================
          FINAL RESULT
          =======================""")
    print("total test cases :",n)
    print("passed :",passed)
    print("Failed :",failed)

    if failed==0:
        print("\n ALL TEST CASES PASSED")
    else:
        print("\n SOME TEST CASES FAILED")
    
    show_result(passed, failed)
    if failed == 0:
        winsound.MessageBeep()
    else:
        winsound.MessageBeep()
    return {
    "total": n,
    "passed": passed,
    "failed": failed}
