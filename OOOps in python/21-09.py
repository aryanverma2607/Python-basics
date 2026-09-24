class Student:
    def __init__(self,roll_no,name,salary):
        self.__roll_no=roll_no
        self.__name=name
        self.__salary=salary
    @property
    def roll_no(self):
        return self.__roll_no
    @property
    def name(self):
        return self.__name
    @property
    def salary(self):
        return self.__salary
    @name.setter
    def name(self,n):
        self.__name=n
    @salary.setter
    def salary(self,s):
        self.__salary=s
    @name.deleter
    def name(self):
        print("Name Deleted")
        del self.__name
    @salary.deleter
    def salary(self):
        print("Salary Deleted")
        del self.__salary
        

s=Student(101,"Aryan",50000)
print(s.name)
print(s.salary)

s.name="Niteen"
s.salary=30000
print(s.name)
print(s.salary)

del s.name
del s.salary
print("Okay")
