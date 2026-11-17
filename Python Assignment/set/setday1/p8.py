'''
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
-
'''
uname=frozenset()
while True:
	print("""Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit""")
	choice=(input("Enter choice : "))
	match choice:
		case '1':
			username=input("Enter username : ")
			uname=frozenset(username)
			print(uname)
		case '2':
			if uname!=frozenset():
				for i in username:
					if 'A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9':
						continue
					else:
						print("Invalid Username")
						break
				else:
					print("Username is valid")
		case '3':
			if uname!=frozenset():
				print("Allowed Characters:")
				allowed=frozenset()
				element=[]
				for i in uname:
					if 'A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9':
						element.append(i)
				allowed=frozenset(element)
				print(allowed)				
		case '4':
			print("Exit")
			break
		case __:
			print("Invalic Choice")			
			
			