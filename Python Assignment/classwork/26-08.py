# function
'''
syntax = def function_name():
		function body
		
		return value(optional)
'''
'''
def hello():
	print("Hello world")

hello()    #calling statement

def hello(name):
	print("Heyyyyy",name)
hello("Aryan")



def add(a,b):
	c=a+b
	print(c)
add(2,3)
'''
'''
#input parameter from user 
def sum(a,b):
	c=a+b
	print("Sum is ",c)

print("start")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))


sum(x,y)
print("Done")

'''

def even(a):
	l=[]
	for i in range(a):
		if i%2==0:
			l.append(i)
	return l
x=int(input("Enter number:"))
print(even(x)) 
c=even(x)
print(c)






























