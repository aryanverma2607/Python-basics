'''
8.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

print("The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects
")

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277
'''
x=int(input("Enter Classes = "))
y=int(input("Enter Number of Student = "))
z=int(input("Enter Number of Subjects = "))
i=1
while i<=x:
	print("Class ",i)
	j=1
	while j<=y:
		sum=0
		k=1
		print("Student ",j)
		while k<=z:
			a=int(input("Enter marks = "))
			sum=sum+a
			k=k+1
		print("Student",j,"total = ",sum)
		j=j+1	
	i=i+1
