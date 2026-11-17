'''
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''
print("""=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================""")
python=set()
java=set()
while True:
	print("""Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit""")
	choice=(input("Enter choice : "))
	match choice:
		case '1':
			n=int(input("Enter number of student to add in python:"))
			p=[]
			for i in range(n):
				id=input("Enter Student Id = ")	
				p.append(id)
			python=set(p)
			print(p)
		case '2':
			m=int(input("Enter number of student to add in Java:"))
			j=[]
			for i in range(m):
				id=input("Enter Student Id = ")	
				j.append(id)
			java=set(j)
			print(java)
		case '3':
			if python!=set():
				print("Python Student : ",python)
			else:
				print("Add Student First")
		case '4':
			if java!=set():
				print("Java Student : ",java)
			else:
				print("Add Student First")
		case '5':
			if java!=set() and python!=set():
				print("Student Enrolled in both courses : ",(python & java))
			else:
				print("Add Student first")
		case '6':
			if java!=set() and python!=set():
				print("Student Enrolled Only in Python courses : ",(python - java))
			else:
				print("Add Student first")
		case '7':
			if java!=set() and python!=set():
				print("Student Enrolled Only in Java courses : ",(java - python))
			else:
				print("Add Student first")
		case '8':
			if java!=set() and python!=set():
				id=input("Enter Student id :")
				print(id in python)
		case '9':
			if java!=set() and python!=set():
				print("All total unique student : ",(python | java ))
			else:
				print("Add Student first")
		case '10':
			print("Exit")
			break
		case __:
			print("Invalic Choice")			
			


