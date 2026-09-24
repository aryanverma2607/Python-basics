'''============================================================
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM
=========================================

Create an Employee class inside:

models/employee.py

ATTRIBUTES:

* employee_id
* name
* salary
* department

TASKS:

1. Take details of 5 employees from the user.
2. Create Employee objects.
3. Store the objects inside a list.
4. Display all employees.
5. Display employees whose salary is greater than 40,000.
6. Display employees who belong to the IT department.
7. Find the employee having the highest salary.
8. Calculate total salary of all employees.
9. Calculate average salary.

SAMPLE INPUT:

101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

EXPECTED OUTPUT:

All Employees:
101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

Employees with salary greater than 40000:
101 Amit 45000 IT
103 Priya 60000 IT
104 Neha 50000 Finance

Employees from IT Department:
101 Amit 45000 IT
103 Priya 60000 IT

Highest Salary Employee:
103 Priya 60000 IT

Total Salary:
220000

Average Salary:
44000
'''
employee=[]
class Employee:
    def __init__(self):
        self.e_id=int(input("Enter Employee ID:"))
        self.e_name=input("Enter Employee Name:")
        self.salary=float(input("Enter Employee Salary:"))
        self.department=input("Enter Employee Department:")
        employee.append(self)
    def display(self):
        print("\nAll Employees:")
        for i in employee:
            print(i.e_id,i.e_name,i.salary,i.department)
    def greater_40k(self):
        print("\nEmployees with salary greater than 40000:")
        for i in employee:
            if i.salary>40000:
                print(i.e_id,i.e_name,i.salary,i.department)
    def department_(self):
        self.d=input("\nEnter Department:")
        print(f"\nEmployees from {self.d} Department:")
        for i in employee:
            if i.department==self.department:
                print(i.e_id,i.e_name,i.salary,i.department)
    def highest(self):
        print("\nHighest Salary Employee:")
        highest=0
        for i in employee:
            if i.salary>highest:
                highest=i.salary
        for i in employee:
            if i.salary==highest:
                print(i.e_id,i.e_name,i.salary,i.department)
    def total(self):
        print("\nTotal Salary:")
        total=0
        for i in employee:
            total=total+i.salary
        print(total)
    def average(self):
        print("\nAverage Salary:")
        total=0
        for i in employee:
            total=total+i.salary
        average=total/len(employee)
        print(average)


