'''10.
=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}

'''

n=int(input("Enter number of mail: "))
l=[]
for i in range(n):
	mail=input("Enter Mail id: ")
	l.append(mail)
print(l)
d={}
newl=[]
for i in range(len(l)):
	for j in range(len(l[i])):
		if l[i][j]=="@":
			a=l[i][j+1::]
			newl.append(a)
			break
print(newl)
for i in range(len(newl)):
	key=newl[i]
	d[key]=d.get(key,0)+1
print(d)

'''
n=int(input("Enter number of mail: "))
l=[]
for i in range(n):
	mail=input("Enter Mail id: ").split("@")
	l.append(mail[-1])
d={}
for i in l:
	d[i]=d.get(i,0)+1
print(d)
'''



