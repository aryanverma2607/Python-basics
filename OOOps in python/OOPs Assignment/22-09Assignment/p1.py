'''
============================================================
ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
=========================================
SCENARIO:
A company wants to maintain information about different types of employees.
Create the following class hierarchy:
Employee
|
+-------- Developer
|
+-------- Manager
REQUIREMENTS:
1. Create a parent class Employee.
Employee should contain:
* employee_id
* employee_name
* salary
2. Create Developer and Manager classes that inherit from Employee.
3. Employee should have a method:
display_details()
4. Developer should have:
programming_language
and a method:
write_code()
5. Manager should have:
team_size
and a method:
manage_team()
6. The child-class constructors must initialize parent-class data using super().
7. Override display_details() in both child classes.
8. From the overridden method, call the parent display_details() using super().
9. salary must be encapsulated.
Implement:
@property
@salary.setter
@salary.deleter
10. Salary setter must reject salary <= 0.
11. Read ALL employee information from the user.
INPUT REQUIREMENT:
Ask the user:
Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:
1. Developer
2. Manager
If Developer:
Enter Programming Language:
If Manager:
Enter Team Size:
SAMPLE INPUT:
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python
EXPECTED OUTPUT:
## Employee Details
Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python
Rahul is developing applications using Python.
'''
class Employee:
    def __init__(self,e_id,e_name,salary):
        self.id=e_id
        self.name=e_name
        self.__salary=salary

    def display_details(self):
        print("Account Details:\n")
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("Salary:",self.__salary)


class Developer(Employee):
    def __init__(self,e_id,e_name,salary,language):
        super().__init__(e_id,e_name,salary)
        self.lang=language

    def language(self):
        print("Role : Developer")
        print(f"Programming Language: {self.lang}")

    def write_code(self):
        print(f"{self.name} is developing applications using {self.lang}.")

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,x):
        if x>0:
            self.__salary=x
        else:
            print("salary must be greater than 0")
    @salary.deleter
    def salary(self):
        del self.__salary



class Manager(Employee):
    def __init__(self,e_id,e_name,salary,team_size):
        super().__init__(e_id,e_name,salary)
        self.size=team_size

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,x):
        if x>0:
            self.__salary=x
        else:
            print("salary must be greater than 0")
    @salary.deleter
    def salary(self):
        del self.__salary

    def manage_team(self):
        print("Role : Manager")
        print("Team Size",self.size)
        print(f"{self.name} is a manager With team size {self.size}")

id=int(input("Enter Employee ID:"))
name=input("Enter Employee Name:")
salary=float(input("Enter Employee Salary:"))
print("""Enter Employee Role:
1. Developer
2.manager """)
role=input("Enter Employee Role:")
match role:
    case "1":
        lang=input("Enter Programming Language:")
        print()
        d=Developer(id,name,salary,lang)
        d.display_details()
        d.language()
        d.write_code()
    case "2":
        size=int(input("Enter Team Size:"))
        print()
        m=Manager(id,name,salary,size)
        m.display_details()
        m.manage_team()
    case __:
        print("Invalid Input")

