# class Student:
#     college="SKITM"
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         Student.marks=90
# s1=Student("Aryan")
# print(s1.college)
# print(Student.college)

# print(s1.__dict__)
# print(Student.__dict__)
# s1.m1()
# print(Student.__dict__)   # method m1 is added after calling and it is included in __dict__ after calling


# class test:
#     a=10
#     def __init__(self):
#         self.b=20

# t1=test()
# t2=test()
# t2.a=t2.a+1
# print(t2.a)
# print(test.a)
# print(t1.a)

# #Removind instance variable from object
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
# t1=test()
# t2=test()
# print(t1.__dict__)
# del t1.c #it remove c from test class
# del t1.d  #it remove d from test class
# print(t1.__dict__)    #it show the list of attributes after remove of C and D

# class student:
#     def set_name(self,name):           #setter
#         self.name=name
#     def get_name(self):               #getter
#         return self.name

# s1=student()
# s1.set_name("Aryan")
# print(s1.get_name())
# #classmethod
# class lala_company:
#     college="SKITM"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def Change_name(cls,new):   # cls refers to current class
#         cls.college=new

# l1=lala_company("Ajay")
# print(l1.college)
# lala_company.Change_name("SVCE")
# print(l1.college)

# l1.Change_name("CDGI")
# print(lala_company.college)
