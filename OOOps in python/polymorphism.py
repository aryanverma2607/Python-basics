# Heirarchical Inheritence
# class A:
#     def __init__(self):
#         print("Constructor A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Constructor B")
# obj=B()


# class A:
#     def __init__(self):
#         print("Constructor A")
# class B:
#     def __init__(self):
#         super().__init__()
#         print("Constructor B")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Constructor B")
# obj=B()
# print(isinstance(obj,B))   #True - it it instance of B
# print(isinstance(obj,A))    #False - it is not instance of obj because it is object of class B
# print(issubclass(B,A))   #True - B is subclass of A because it inherits from class A

# Polymorphism
# Inheritence Required
# Method name should be same
# parameter should be same
# class Bird:
#     def fly(self):
#         print("Bird Can Fly")
# class AeroPlane(Bird):
#     def fly(self):
#         super().fly()
#         print("AeroPlane Can Fly")
# obj=AeroPlane()
# obj.fly()

#Dynamic Polymorphism
# Duck Typing
# class Bird:
#     def fly(self):
#         print("Bird Can Fly")
# class AeroPlane(Bird):
#     def fly(self):
#         print("AeroPlane Can Fly")
# obj=[Bird(),AeroPlane()]
# for o in obj:
#     o.fly()

# print(len("Hello"))   #built-in Polymorphism
# print(len([1,2,3,5]))


# print(10 + 20 )  #Operator polymorphism
# print("Wel" + "Come")


# print("===============End=============")