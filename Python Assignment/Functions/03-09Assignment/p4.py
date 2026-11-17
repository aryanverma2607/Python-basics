'''
4.
Assignment: Scholarship Eligibility System (Using filter(), map(), and sorted() with Lambda Expressions)

A university is offering scholarships to students based on their academic performance.

The scholarship committee has decided on the following rules:

Only students who score 75 marks or above are eligible for the scholarship.
Eligible students will receive 5 bonus marks to reward their outstanding performance.
Finally, the updated marks should be displayed in descending order.

As a software developer, your task is to automate this process using Python.

Note: Use filter() to select eligible students, map() to add the bonus marks, and sorted() to display the final marks in descending order. All three operations must use lambda expressions.

Task

Write a Python program that:

Filters students who have scored 75 or above.
Adds 5 bonus marks to each eligible student.
Sorts the updated marks in descending order.
Displays the final list of scholarship marks.
Input Format
The first line contains an integer N, representing the number of students.
The second line contains N space-separated marks.
Output Format

Display the updated scholarship marks in descending order.

Sample Input
Enter the number of students:
8

Enter the marks:
65 80 92 74 88 76 55 95
Sample Output
Scholarship Marks:
100 97 93 85 81

'''
student=list(map(int,input("Enter Marks of student one by one:").split()))

eligible=list(filter(lambda x:x>75,student))

bonus=list(map(lambda x:x+5,eligible))

print("Scholarship Marks:\n",sorted(bonus,reverse=True))




'''
from functools import reduce
age=list(map(int,input("Enter Employee age one by one: ").split()))
print(age)
name=input("Enter Employee age one by one: ").split()
print(name)
def vowel(*name):
    if name[0] in 'aeiou':
        count+=1

print("========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
while True:
    print("""1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit""")
    choice=int(input("Enter choice:"))
    match choice:
        case 1:
             d=list(set(age))
             result=sorted(d,reverse=True)
             print(result[1])
        case 2:
             senior=len(list(filter(lambda x:x>=50,age)))
             print("Senior Employees : ",senior)
        case 3:
             duplicate=set(age)
             print(list(duplicate))
        case 4:
             result=len(list(filter(lambda x:x[0] in 'aeiou',name)))
             print(result)
        case 5:
             name=sorted(name,key=lambda x:len(x))
             print(name[-1])
        case 6:
             print("Exit...")
             break
        case __:
             print("Inappropriate choice")
'''





