'''
=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92

'''
from collections import namedtuple
print("""=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================""")

n=int(input("Enter number of student:"))
student=namedtuple("Result",["roll_no","name","course","marks"])

list=[] 
for i in range(n):
	print("Enter detail of student {}".format(i+1))
	no=int(input("Enter roll number:"))
	name=input("Enter student name:")
	course=input("Enter course name:")
	marks=int(input("Enter student marks:"))
	s=student(no,name,course,marks)
	list.append(s)
print()
for i in list:
	print(i.roll_no,i.name,i.course,i.marks)
print()
largest=s.marks
c=input("Enter course name:")
count=0
sum=0
for i in list:
	if largest<i.marks:
		largest=i.marks
	if i.marks>80:
		count+=1
	sum=sum+i.marks
	avg=sum/n
print()
print("TOPPER")
for i in list:
	if i.marks==largest:
		print(i.roll_no,i.name,i.course,i.marks)
print()
print("Students Above 80: ",count)
print()
print("Averga marks : ",avg)
print()
print(f"Student in {c} Courses:")
for i in list:
	if i.course==c:
		print(i.roll_no,i.name,i.course,i.marks)
	else:
		print("No such course found")




























