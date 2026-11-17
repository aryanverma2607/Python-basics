#nested dictionay
'''
students={
101:{"name":"Aryan","age":21},
102:{"name":"Niteen","age":30}
}
print(students)
for i,j in students.items():
	print("ID is ",i)
	for k,v in j.items():
		print(k," and ",v)
print(students[101])
del students[101]["age"]
print(students[101])
'''
'''
del students[101]
print(students[101])
'''
'''

#special function "eval()"
a=eval(input("Enter value:"))
print(a)
print(type(a))

n=int(input("Enter number:"))
d={}
for i in range(n):
	key=input("Enter key:")
	value=int(input("Enter value:"))
	d[key]=value

s=sum(d.values())
print("sum is ",s)
'''
'''
d=eval(input("Enter dictionary:"))
s=sum(d.values())

print(s)

'''
'''
#WAP to fing number of occurence of each letter in given string.
string=eval(input("Enter string:"))
d={}
for i in string:
	d[i]=d.get(i,0) +1

print(d)
for i,v in sorted(d.items()):
	print(i," occured ",v," times ")
'''
'''
#WAP to find number of occurence of vowel in string
string=eval(input("Enter string:"))
d={}
for i in string:
	if i in "AEIOUaeiou":
		d[i]=d.get(i,0) +1
print(d)
'''
'''
#WAP to track how many times each user try to login
login=["aryan","niteen","muskan","priya","muskan","priya","niteen","niteen"]
d={}
for user in login:
	d[user]=d.get(user,0) +1
print(d)
'''
'''
#WAP to group words based on their length
string=input("Enter string:").split()
g={}
for i in string:
	l=len(i)
	if l not in g:
		g[l]=[]
	g[l].append(i)

print(g)
'''
#WAP to merge two dictionary and sum values

item={"apple":10,"pineapple":15,"banana":8}
item2={"dragonfruit":5,"orange":20,"banana":20}

merged=item.copy()

for k,v in item2.items():
	merged[k]=merged.get(k,0)+v
print(merged)

print(sum(merged.values()))
















