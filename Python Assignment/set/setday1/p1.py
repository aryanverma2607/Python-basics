'''
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

print("""=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================""")
c_id=set()
r_id=set()
while True:
	print("""Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit""")
	choice=(input("Enter choice : "))
	match choice:
		case '1':
			n=int(input("Enter number of student in coding Clud:"))
			coding=[]
			for i in range(n):
				id=input("Enter Student Id = ")	
				coding.append(id)
			c_id=set(coding)
			print(c_id)
		case '2':
			m=int(input("Enter number of student in robotics club:"))
			robotics=[]
			for i in range(m):
				id=input("Enter Student Id = ")	
				robotics.append(id)
			r_id=set(robotics)
			print(r_id)
		case '3':
			if c_id!=set():
				print("Coding Club Student : ",c_id)
			else:
				print("Add Student First")
		case '4':
			if r_id!=set():
				print("Robotics Club Student : ",r_id)
			else:
				print("Add Student First")
		case '5':
			if c_id!=set() and r_id!=set():
				print("Student Enrolled in both courses : ",(c_id & r_id))
			else:
				print("Add Student first")
		case '6':
			if c_id!=set() and r_id!=set():
				print("Student only in Coding Club: ",(c_id - r_id))
			else:
				print("Add Student first")
		case '7':
			if c_id!=set() and r_id!=set():
				print("Student Only in Robotics CLub : ",(r_id - c_id))
			else:
				print("Add Student first")
		case '8':
			if c_id!=set() and r_id!=set():
				print("All Unique Club Member : ",(c_id|r_id))
			else:
				print("Add Student first")
		case '9':
			if c_id!=set() and r_id!=set():
				print("All total unique student : ",(c_id | r_id))
			else:
				print("Add Student first")
		case '10':
			print("Exit")
			break
		case __:
			print("Invalic Choice")	
'''
l1=[]
l2=[]
while True :
    print('1.Enroll Student in Python')
    print('2. Enroll Student in Java')
    print('3. Display Python Students')
    print('4. Display Java Students')
    print('5. Find Students Enrolled in Both Courses')
    print('6. Find Students Enrolled Only in Python')
    print('7.Find Students Enrolled Only in Java')
    print('8. Check Enrollment in Python Course')
    print('9. Display Total Unique Students')
    print('10. Exit')

    
    choice=input('enter your choice ')
    match choice :
        case '1':
            n=int(input('enter list1 size'))
            for i in range(n):
                id=(input('enter elements of list 1'))
                l1.append(id)
            python=set(l1)
            python.update(['muskan','riya'])
          
        case '2':
            n2=int(input('enter list2 size'))
            for i in range(n2):
                id=(input("enter elements of list 2"))
                l2.append(id)
            java=set(l2)
            java.update(['yash'])
            
        case '3':
            print('python students',python)
            
        case '4':
            print('java students',java)
            
        case '5':
            print('students in both' ,python&java)
            
        case '6':
            print('student only in python',python-java)
            
        case '7':
            print('student only in java',java-python)
            
        case '8':
            a=python|java
            for i in a:
                if i in python :
                    continue
                else:
                    break
            else:
                print('all are enrolled')
            
        case '9':
            print('total unique student',python|java)
            
        case '10':
            print('exit')
            break
        case __ :
            print('invalid case')
'''