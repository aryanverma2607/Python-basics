

'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST


'''
name=input("Enter employee name : ")
result=""
for i in range(len(name)):
	ch=name[i]
	if (i==0 or name[i-1]==" ") and ch>="a" and ch<="z":
		result=result+chr(ord(ch)-32)
	elif ch>="A" and ch<="Z":
		result=result+ch
print(result)

			
