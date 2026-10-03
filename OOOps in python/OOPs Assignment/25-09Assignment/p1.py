'''Assignment 1 – Employee Bonus System
Create a parent class Employee with the following attributes:
employee_id
employee_name
salary

Create two child classes:
Developer
Manager

Requirements
Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000
'''
class Employee:
    def __init__(self,employee_id,employee_name,employee_salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.employee_salary=employee_salary

    def calculate_bonus(self):
        self.bonus = self.bonus

class Developer(Employee):
    def __init__(self,employee_id,employee_name,employee_salary):
        super().__init__(employee_id,employee_name,employee_salary)
    def calculate_bonus(self):
        self.type = "Developer"
        self.bonus = self.employee_salary*0.1
        self.final_salary = self.employee_salary + self.bonus

    def display(self):
        print(f"""\n----- Employee Details -----
Employee ID   : {self.employee_id}
Employee Name : {self.employee_name}
Salary        : {self.employee_salary}
Employee Type : {self.type}
Bonus         : {self.bonus}
Total Amount  : {self.final_salary}""")


class Manager(Employee):
    def __init__(self,employee_id,employee_name,employee_salary):
        super().__init__(employee_id,employee_name,employee_salary)
    def calculate_bonus(self):
        self.type = "Manager"
        self.bonus = self.employee_salary*0.2
        self.final_salary = self.employee_salary + self.bonus

    def display(self):
        print(f"""\n----- Employee Details -----
Employee ID   : {self.employee_id}
Employee Name : {self.employee_name}
Salary        : {self.employee_salary}
Employee Type : {self.type}
Bonus         : {self.bonus}
Total Amount  : {self.final_salary}""")
        


id=int(input("Enter Employee ID: "))
name=input("Enter Employee Name: ")
salary=float(input("Enter Employee Salary: "))
type = input("Enter Employee type: ")
if type.lower() == "developer":
    D = Developer(id,name,salary)
    D.calculate_bonus()
    D.display()
else:
    M = Manager(id,name,salary)
    M.calculate_bonus()
    M.display()