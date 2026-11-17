#parameter type
'''
#1. positional
def Hello(name,age):
	print(name,age)

Hello("Aryan",30)
'''
'''
#keyword arguement
def sum(a,b):
	print("sum is ",a+b)

sum(b=10,a=90)

'''
'''
#mix of positional and keyword arguement
def Hello(name,age):
	print(name,age)

Hello("Aryan",age=30)
'''
#default parameter
'''
def Hello(name,age=18,city="indore"):
	print(name,age,city)

Hello("Aryan")
Hello("Aryan",40)
Hello("Aryan",age=30,city="Chennai")
'''

#variable lenght parameter
'''
def numbers(*args):
	print(args)

numbers(10,20,30,40,50,60,70,80)
numbers(100)
numbers()

def average(*num):
	return sum(num)/len(num)


print(average(10,20,30,40,50))
print(average(*[10,20,30,40,50]))   # now it is variable length parameter
'''

#keyword variable length parameter
'''
def display(**b):
	print(b)
	for k,v in b.items():
		print(k,":",v)

display(name="Aryan",age=30,city="Indore")
'''
def details(**info):
	if "name" in info:
		print("Welcome",info["name"])
	if "mail" in info:
		print("Mail",info["mail"])

details(name="Aryan",mail="aryan@gmail.com")












