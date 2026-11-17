#input dictionary from user
'''
d={}
n=int(input("Enter number if student:"))
for i in range(n):   #using for loop
	name=input("Enter student name:")
	marks=int(input("Enter marks:"))
	d[name]=marks
print(d)
for x in d:
	print(x,"And marks",d[x])
d={}
i=0
while i<=n:  #using while loop
	name=input("Enter student name:")
	marks=int(input("Enter marks:"))
	d[name]=marks
	i+=1
for x in d:
	print(x,"And marks",d[x])
'''
d={1:"java",2:"python",3:"react"}
d[4]="angular"
print(d)
d[2]="Mern"
print(d)
print(d.pop(3))
print(d)
print(d.popitem())  #it return last poped key value
print(d) #dictionary after removing element


