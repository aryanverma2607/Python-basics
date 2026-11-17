"""
2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System
"""


student = {
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}} 
while True :
    print("""
=========================================
      STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit""")

    choice = int(input("enter your choice :"))
    
    match choice :
        case 1 :
            data = {}
            id = int(input("enter student id :"))
            if id in student:
                print("id exist :")
            else :    
                name = input("student name :")
                data["name"] = name
                course = input("course name :")
                data["course"] = course
                mobile = int(input("enter mobile no. :"))
                data["mobile"] = mobile
                fees = int(input("enter fees :"))
                data["fees"] = fees
                city =  input("city :")
                data["city"] = city

                student[id] = data     
            print(student)

        case 2 :
            id = int(input("enter student id to search :"))
            
            if id in student:
                a = student[id]
                for k,v in a.items():
                    print(k,":",v)

            else :
                print("student not found")  

        case 3 :
            id = int(input("enter student id to update course :"))
            if id in student:
                course = input("course name to change :")
                student[id]["course"] = course
            else :
                print("student not found")
        case 4 :
            id = int(input("enter student id to delete :"))  
            if id in student:
                del student[id]
                print("deleted successfully")
            else :
                print("student not found")                  
        case 5 :
            print(student) 
        case 6 :
            print("Total students :",len(student))
        case 7 :
            course = input("enter course name to serch students :")

            for i,j in student.items():
                if j["course"] == course :
                    print(i,j["name"])

        case 8 :
            city = input("enter city to find students :")
            for i,j in student.items():
                if j["city"] == city :
                    print(i,j["name"])

        case 9 :
            high = 0
            id = 0
            for i,j in student.items():
                high = j["fees"]
                break
            for i,j in student.items():
                if j["fees"] > high :
                    high = j["fees"]
                    
            for i,j in student.items():
                if j["fees"] == high:
                    for k,v in j.items():
                        print(k,v)

        case 10 :
            min = 0
            id = 0
            for i,j in student.items():
                min = j["fees"]
                break
            for i,j in student.items():
                if j["fees"] < min :
                    min = j["fees"]
                    
            for i,j in student.items():
                if j["fees"] == min:
                    for k,v in j.items():
                        print(k,v)            

        case 11 :
            print("Thank You For Using Student Management System")
            break