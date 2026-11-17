l=[]
class Employee:
    def __init__(self):
        self.employee_id=int(input("\nEnter Employee ID: "))
        self.employee_name=input("Enter Employee name:")
        self.department=input("Enter Employee Department:")
        self.salary=float(input("Enter Employee Salary:"))
        l.append(self)
    def display(self):
        for i in l:
            print(i.employee_name,i.employee_id,i.department,i.salary)

    def search(self,id):
        self.id = id
        for i in l:
            if self.id == i.employee_id:
                print(i.employee_name,i.employee_id,i.department,i.salary)
                break
        else:
            print("No record Found...")
    def dpt(self,department):
        self.d = department
        for i in l:
            if self.d == i.department:
                print(i.employee_name,i.employee_id,i.department,i.salary)
                break
        else:
            print("No record Found...")
    def highest(self):
        highest = self.salary
        for i in l:
            if i.salary>highest:
                highest = i.salary
        for i in l:
            if i.salary == highest:
                print(i.employee_name,i.employee_id,i.department,i.salary)
e1=Employee()
e2=Employee()
e3=Employee()
e4=Employee()
e5=Employee()



