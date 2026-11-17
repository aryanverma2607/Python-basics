l=[]
class Project:
    def __init__(self):
        self.project_id=int(input("\nEnter Project Id:"))
        self.project_name=input("enter project name:")
        self.employee_id=int(input("Enter Employee ID:"))
        self.project_cost=float(input("Enter Project Cost:"))
        l.append(self)
    def display(self):
        for i in l:
            print(i.project_id,i.project_name,i.employee_id,i.project_cost)

    def highest(self):
        highest = self.project_cost
        for i in l:
            if i.project_cost>highest:
                highest = i.project_cost
        for i in l:
            if i.project_cost == highest:
                print(i.project_id,i.project_name,i.employee_id,i.project_cost)


p1=Project()
p2=Project()
p3=Project()
p4=Project()
p5=Project()
