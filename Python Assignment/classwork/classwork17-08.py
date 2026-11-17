'''
#frozen set
a=frozenset('python')
print(a)
b=frozenset([10,20,30,40])
print(b)
#we can create frozenset using tuple
#b.add(50)
#print(b)    it gives error as we can not modify frozenset
a|=b   #support short hand operator but not inplace update
print(a) 

#WAP to count unique words in a python using set.
text=input("Enter Message : ")
words=text.split()
u=set(words)
print("Count of Words: ",len(u))

#WAP to check unique character in a string using set
text=input("Enter Message : ")
if len(text)==len(set(text)):
	print("Unique character in string")
else:
	print("No Unique character found")
'''
#WAP to find first non repeating character in string using set
'''
text=input("Enter Message : ")
seen=set()
repeat=set()
for i in text:
	if i in seen:
		repeat.add(i)
	else:
		seen.add(i)
for char in text:
	if char in seen and char not in repeat:
		print("First non reapeating character :",char)
		break
else:
	print("No repeating character found")
'''
d1={"name":"Aryan","age":21,"City":"Indore"}
print(d1)

d={'a':1,'b':2,'a':3}   #here first key override by second key and second key is displayed instead of first key
print(d)
print(type(d))
student={
"name":"abc",
"age":30,
"city":"abc"
}
print(student)
print(type(student))
