'''
7.

=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi


'''
d={}
n=int(input("Enter number of student: "))
for i in range(n):
	k=input("Enter Student name: ")
	d[k]=int(input("Enter student marks: "))

for x,y in d.items():
	if y>50:
		print(x)