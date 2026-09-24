'''Assignment 1: Student Result Calculator

A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
'''
class student:
    def input(self,name,roll_no,eng,math,science):
        self.name=name
        self.roll_no=roll_no
        self.eng=eng
        self.math=math
        self.science=science
    def calculate_total(self):
        self.total=self.eng+self.math+self.science
    def calculate_percentage(self):
        self.percentage=self.total/3
    def display(self):
        print(f"""\nStudent Name: {self.name}
Roll Number: {self.roll_no}
Total Marks: {self.total}
Percentage: {self.percentage}%""")
s=student()
n=input("Enter your name:")
r=int(input("Enter roll number:"))
e=int(input("Enter marks of english:"))
m=int(input("Enter marks of Mathematics:"))
sc=int(input("Enter marks of Science:"))

s.input(n,r,e,m,sc)
s.calculate_total()
s.calculate_percentage()
s.display()