'''
password=input("Enter Password = ")
lower=0
upper=0
space=0
special=0
digit=0
for ch in password:
	if ch.isupper():
		upper=1
	elif ch.islower():
		lower=1
	elif ch.isdigit():
		digit=1
	elif ch.isspace():
		space=1
	else:
		special=1
if lower==1 and len(password)>=8 and len(password)<=15 and lower==1 and digit==1 and special==1 and space==0:
	print("valid Password")
else:
	print("Invalid Password")

'''
'''
str=input("Enter string = ")
i=len(str)-1
while i>=0:
	print(str[i],end="")
	i=i-1
'''
'''
str=input("Enter string = ")
i=-1
b=-len(str)
while b<=i:
	print(str[i],end="")
	i=i-1
'''





































