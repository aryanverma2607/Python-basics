'''
1.
Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]

'''
from functools import reduce


N=int(input("Enter number of employee: "))
employee=[]
for i in range(N):
   name=input("Enter Employee Name:")
   salary=int(input("Enter Employee Salary:"))
   n=(name,salary)
   employee.append(n)

#employees= [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
result=sorted(employee,key=lambda x:x[1])
print(result)


