'''Create the following structure for every assignment:

project/
│
├── models/
│   ├── *init*.py
│   └── class_module.py
│
└── main.py

IMPORTANT RULES

1. Create the class inside the models package.
2. The class must be written in a separate module.
3. Import the class into main.py.
4. Create multiple objects of the class.
5. Store all objects inside a list.
6. Perform operations on the list of objects.
7. Take input from the user wherever required.
8. Do not use dictionaries in place of objects.
9. Do not use database connectivity.
10. Display the output in a proper format.

============================================================
ASSIGNMENT 1 – STUDENT MANAGEMENT SYSTEM
========================================

Create a Student class inside:

models/student.py

ATTRIBUTES:

* roll_no
* name
* marks

TASKS:

1. Take details of 5 students from the user.
2. Create a Student object for each student.
3. Store all Student objects inside a list.
4. Display all students.
5. Display students whose marks are greater than 60.
6. Find the student having the highest marks.
7. Calculate the average marks of all students.

SAMPLE INPUT:

Enter Roll No: 101
Enter Name: Amit
Enter Marks: 78

Enter Roll No: 102
Enter Name: Rahul
Enter Marks: 55

Enter Roll No: 103
Enter Name: Priya
Enter Marks: 91

Enter Roll No: 104
Enter Name: Neha
Enter Marks: 67

Enter Roll No: 105
Enter Name: Rohit
Enter Marks: 45

EXPECTED OUTPUT:

All Students:
101 Amit 78
102 Rahul 55
103 Priya 91
104 Neha 67
105 Rohit 45

Students having marks greater than 60:
101 Amit 78
103 Priya 91
104 Neha 67

Highest Marks:
103 Priya 91

Average Marks:
67.2'''
s=[]
class student:
    def __init__(self):
        self.roll_no=int(input("Enter Student Roll number:"))
        self.name=input("Enter Student Name:")
        self.marks=int(input("Enter Student Marks:"))
        s.append(self)
    def display(self):
        print("\nAll Student:")
        for i in s:
            print(i.roll_no,i.name,i.marks)
    def greater_60(self):
        print("\nStudent marks Greater than 60:")
        for i in s:
            if i.marks>=60:
                print(i.roll_no,i.name,i.marks)
    def higher(self):
        print("\nHighest Marks:")
        high=0
        for i in s:
            if i.marks>high:
                high=i.marks
        for i in s:
            if i.marks==high:
                print(i.roll_no,i.name,i.marks)
    def average(self):
        sum1=0
        print("\nAverage Marks:")
        for i in s:
            sum1=sum1+i.marks
        average=sum1/len(s)
        print(average)