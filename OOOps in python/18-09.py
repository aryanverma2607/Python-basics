# # method chaining
# # Pattern-1
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_name(self):
#         print(f"{self.name}")
#     def display_marks(self):
#         print(f"{self.marks}")
#     def display_all(self):
#         self.display_name()
#         self.display_marks()
# s1=Student("Aryan",99)
# s1.display_all()

# # Pattern-2
# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.marks=0
#     def display_name(self):
#         print(f"{self.name}")
#         return self
#     def display_marks(self,marks):
#         self.marks=marks
#         return self         #ye self return kar raha hai jo dusri method ko call karega bad mein
#     def display_all(self):
#         print(f"{self.marks}")
# s1=Student("Aryan")
# s1.display_name().display_marks(90).display_all()

#Encapsulation
class Employee:
    def __init__(self,id,name,salary):
        self.__id=id
        self.__name=name
        self.__salary=salary
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        if name.strip()!="":
            self.__name=name
        else:
            print("Name cant be empty")
            self.__name="Unknown"
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("Invalid salary")
            self.__salary=0
    def display(self):
        print("ID is:",self.__id)
        print("Name is:",self.__name)
        print("Salary is:",self.__salary)

e_id=int(input("Enter Employee ID:"))
e_name=input("Enter Employee Name:")
e_salary=int(input("Enter Employee Salary:"))
e=Employee(e_id,e_name,e_salary)
e.display()

print(e.get_id())
print(e.get_name())
print(e.get_salary())

e.set_name("")   #if name is empty it give unknown
print(e.get_name())
e.set_salary(1500)  #if salary is less than 0 then it gives invalid salary
print(e.get_salary())