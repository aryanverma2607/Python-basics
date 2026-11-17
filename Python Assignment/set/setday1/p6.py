'''
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
'''
print("""=========================================
COMMON CHARACTER FINDER
=========================================""")
string=''
string1=''
c1=set()
common=[]
while True:
	print("""Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit""")
	choice=(input("Enter choice : "))	
	match choice:
		case '1':
			string=input("Enter String 1:")
			print(string)
		case '2':
			string1=input("Enter String 2: ")
			print(string1)
		case '3':
			if string!='' and string1!='':
				for i in string:
					for j in string1:
						if i==j:
							common.append(i)
			c1=set(common)
			print(c1)
		case '4':
			if common!=[]:
				print("Count : ",len(c1))
		case '5':
			print("Exit")
			break
		case __:
			print("Invalid choice")
				