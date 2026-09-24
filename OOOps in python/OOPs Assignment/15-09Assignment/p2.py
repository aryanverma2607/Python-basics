'''
Assignment 2: Employee Salary Calculator
A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:
Employee ID
Employee name
Basic salary
HRA percentage
DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.
calculate_da() – Calculate DA.
calculate_gross_salary() – Calculate gross salary.
display_salary() – Display employee salary details.

Formula:
HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA
'''
class Employee:
    def details(this,id,name,salary,hra,da):
        this.id=id
        this.name=name
        this.salary=salary
        this.hra=hra
        this.da=da
    def calculate_hrs(self):
        self.hra=self.salary*self.hra/100
    def calculate_da(self):
        self.da=self.salary*self.da/100
    def gross_salary(self):
        self.total=self.salary+self.hra+self.da
    def display(self):
        print(f"""\nEmployee ID:{self.id}
Employee name:{self.name}
Basic salary:{self.salary}
HRA percentage:{self.hra}
DA percentage:{self.da}
Gross salary:{self.total}""")

e=Employee()
e.details(101,"Aryan",25000,25,20)
e.calculate_hrs()
e.calculate_da()
e.gross_salary()
e.display()
