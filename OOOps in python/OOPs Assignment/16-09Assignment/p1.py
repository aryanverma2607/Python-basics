'''
Question 1: Employee Salary Management System
Scenario
A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.
Requirements
Create a class named Employee with the following attributes:
employee_id
employee_name
basic_salary
Initialize the values using a constructor.
Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
'''
class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def calculate_hra(self):
        self.hra=self.salary*0.2
    def calculate_da(self):
        self.da=self.salary*0.15
    def gross_salary(self):
        self.gross=self.salary+self.hra+self.da
    def display(self):
        print(f"""------ Employee Salary Details ------
Employee ID      : {self.id}
Employee Name    : {self.name}
Basic Salary     : {self.salary}
HRA              : {self.hra}
DA               : {self.da}
Gross Salary     : {self.gross}""")

e=employee(101,"Rahul Sharma",50000)
e.calculate_hra()
e.calculate_da()
e.gross_salary()
e.display()
