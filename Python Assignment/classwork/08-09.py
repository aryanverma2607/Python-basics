#closure
'''
def display(name):
    message=f"hello {name}"
    def show():
       print(message)
    return show

ref=display("Aryan")
ref()



'''
'''
def counter():
   count=0
   def increment():
       nonlocal count
       count=count+1
       return count
   return increment

#closure creation
c=counter()

#call closure
print(c())
print(c())
'''
'''
def multiplication(x):
    def calculate(y):
        return x*y
    return calculate

d=multiplication(3)
print(d(8))
print(d(10))
'''

# DECORATORS




























