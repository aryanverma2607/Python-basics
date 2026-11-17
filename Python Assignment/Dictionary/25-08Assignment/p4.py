'''
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

'''
n=int(input("Enter number of student: "))
student={}
for i in range(n):
	key=input("Enter student name: ")
	student[key]=int(input("Enter number: "))
	highest=student[key]
	lowest=student[key]
for v in student.values():
	if v>highest:
		highest=v
	if lowest>v:
		lowest=v
for k,v in student.items():
	if v==highest:
		print("Highest marks: ",k,v)
	if v==lowest:
		print("Lowest marks: ",k,v)


