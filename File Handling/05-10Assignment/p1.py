'''1. Student Attendance Manager
A school wants to maintain the attendance of students in a text file named attendance.txt.
Each line contains:
RollNo,StudentName,Status
where Status is either Present or Absent.

Write a Python program to:
Accept attendance details for N students.*
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage
Sample Input
Enter number of students: 5

Enter Roll No: 101
Enter Student Name: Rahul
Enter Status: Present

Enter Roll No: 102
Enter Student Name: Priya
Enter Status: Absent

Enter Roll No: 103
Enter Student Name: Amit
Enter Status: Present

Enter Roll No: 104
Enter Student Name: Neha
Enter Status: Present

Enter Roll No: 105
Enter Student Name: Rohit
Enter Status: Absent
Expected Output
Attendance Report
-------------------------
Total Students: 5
Present Students: 3
Absent Students: 2
Attendance Percentage: 60.00%
'''
# n=int(input("enter number of student:"))
# file=open("Attendence.txt","w")
# p=0
# a=0
# for i in range(n):
#     roll_no=int(input("Enter student {} roll no:".format(i)))
#     name=input("Enter student {} name:".format(i))
#     status=input("Enter attendence status:").lower()
#     if status=='present':
#         p+=1
#     elif status=='absent':
#         a+=1
#     file.write(str(roll_no) + "," + name + "," + status + "\n")
# file.close()
# print(f"""Total Students: {n}
# Present Students: {p}
# Absent Students: {a}
# Attendance Percentage: {(p*100)/n}%""")



n = int(input("Enter Number Of Student:"))
f = open("Attendance.txt","w")
present = 0
absent = 0
for i in range(n):
    roll_no = int(input(f"Enter Roll Number of student {i+1}:"))
    name = input(f"Enter Student {i+1} name :")
    status = input("Student Attendance Status:").lower()
    if status == "present":
        present += 1
    elif status == "absent":
        absent += 1
    f.write(str(roll_no) + "," + name + "," + status + "\n")
f.close()
f = open("Attendance.txt","r")
print("\nTotal Student:" + str(n) + "\n")
print("Present Student:" + str(present) + "\n")
print("Absent Student:" + str(absent) + "\n")
print("Attendance percentage:" + str(present*100/n) + "\n")



