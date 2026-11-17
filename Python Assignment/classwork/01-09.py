'''
def bill(**items):
	total=0
	for item,price in items.items():
		total=total+price
	return total


print(bill("shirt"=100,"jeans"=1000,"Shoe"=2000))
'''
'''
#positional only arguement
def hello(name,age,/):             #positional only parameter
    print(name,age)


hello("Aryan",30)
hello(name="Aryan",age=30)
'''
'''
#keyword only parameter

def hello(name,*,age):             #keyword only parameter
    print(name,age)


#hello("Aryan",30)
hello("Aryan",age=30)
'''
'''
def payment(id,name,/,amount,method,*,currency,tax):
	print(id,name,amount,method,currency,tax)

payment(101,"Aryan",5000,"UPI",currency="$",tax=10)
payment(101,"Aryan",amount=5000,method="UPI",currency="$",tax=10)

#payment(101,name="Aryan",amount=5000,method="UPI",currency="$",tax=10)  #error
'''
'''
#anonymous function (lamda function)
#syntax= lambda arguement:expression

def sq(x):       #normal function
	return x*x

print("Squeare is :",sq(5))
'''
'''
print("lambda function",end=" ")
sq=lambda x:x*x

print(sq(6))

add=lambda a,b:a+b

print(add(2,4))

#write a function to fing greatest of two number using lambda function / Expression
greatest=lambda a,b: a if a>b else b

print(greatest(9,29))

'''
'''
#map function

#map(function,iterable1,iterable2,iterable3,iterable4,......)

number=[1,2,3,4,5,6]
def cube(n):
	return n*3
result=map(cube,number)

print(list(result))
#print(tuple(result))
#print(set(result))

#using lambda function
result=map(lambda x:x*3,number)
print(list(result))


names=["aryan","niteen","palak"]
result=list(map(lambda x:x.upper(),names))

print(result)
print(tuple(result))


names=["aryan","niteen","palak"]
result=list(map(lambda x:x.capitalize(),names))

print(result)
print(tuple(result))

#WAP to find lenght of every word of a list

result=list(map(lambda x:len(x),names))
print(result)
'''
'''
#WAP to add the list
l1=[1,2,3,4,5]
l2=[6,7,8,9,10] 

def sum(a,b):
	return a+b
result=map(sum,l1,l2)
print(list(result))

output=list(map(lambda x,y:x+y,l1,l2))
print(output)

#WAP to find even or odd from the list
def evod(n):
	if n%2==0:
		return "even"
	else:
		return "odd"
result=map(evod,l1)
print(list(result))

output=list(map(lambda x:"even" if x%2==0 else "odd",l1))
print(output)

'''
'''
#WAP to convert element of list to string
l1=[1,2,3,4,5]
def evod(n):
	return str(n)
result=map(evod,l1)
print(list(result))

output=list(map(lambda x:str(x),l1))
print(output)
'''
marks=[99,87,45,67,67,75]
'''
def grades(x):
	if x>90:
		return "A"
	elif x>75:
		return "B"
	elif x>60:
		return "C"
	else:
		return "fail"
result=map(grades,marks)
print(list(result))
'''

#using lambda
res=list(map(lambda x :"A" if x>85 else "B" if x>70  else "C" if x>55 else "fail",marks ))
print(res)















