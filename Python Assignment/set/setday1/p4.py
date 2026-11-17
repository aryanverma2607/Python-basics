'''
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.
'''
subject=frozenset(['python','java','MySQL','React','Spring Boot'])
print(subject)
while True:
	print("""Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit""")
	choice=(input("Enter choice : "))
	match choice:
		case '1':
			print(subject)
		case '2':
			s=input("Enter Subject : ")
			print(s in subject)
		case '3':
			print("Subject count = ",len(subject))
		case '4':
			for i in range(3):
				s=input("Enter Subject : ")
				if s not in subject:
					continue
				else:
					print("Subject already present")
		case '5':
			print("Exit")
			break
		case __:
			print("Invalid Choice")			