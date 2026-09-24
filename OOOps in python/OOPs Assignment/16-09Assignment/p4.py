'''Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.
Requirements
Create a class named Student with:
roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.
Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
'''
class college:
    def __init__(self,roll_no,name,m1,m2,m3):
        self.roll_no=roll_no
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self):
        self.total=self.m1+self.m2+self.m3
    def percent(self):
        self.percent=self.total/3
    def grade(self):
        if self.percent>=90:
            self.grade="A"
        elif self.percent>75 and self.percent<90:
            self.grade="B"
        elif self.percent>60 and self.percent<75:
            self.grade="C"
        else:
            self.grade="D"
    def display(self):
        print(f"""\n------ Student Result ------
Roll Number      : {self.roll_no}
Student Name     : {self.name}
Total Marks      : {self.total}
Percentage       : {self.percent}
Grade            : {self.grade}""")

c=college("101","Priya sharma",85,90,88)
c.total()
c.percent()
c.grade()
c.display()