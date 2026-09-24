# class Parent:
#     def show(self):
#         print("This is parent method")
# class child(Parent):
#     def show(self):
#         super().show()
#         print("This is child method")

# obj=child()
# obj.show()

#multiple inheritence
# class developer1:
#     def code1(self):
#         print("developer1")
# class developer2:
#     def code2(self):
#         print("developer2")

# class tester(developer1,developer2):
#     def testing(self):
#         print("testing")

# x=tester()
# x.code1()
# x.code2()
# x.testing()


#Hybrid Inheritence
class A:
    def __init__(self):
        print("Constructor Of Class A")
    def fun1(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print('Constructor Of Class B')
    def fun1(self):
        print("B")
class C(A):
    def __init__(self):
        super().__init__()
        print("Constructor Of Class C")
    def fun1(self):
        print("C")
class D(B,C):
    def __init__(self):
        super().__init__()
        print('Constructor Of 6Class D')
    def fun1(self):
        print("D")

obj=D()
obj.fun1()