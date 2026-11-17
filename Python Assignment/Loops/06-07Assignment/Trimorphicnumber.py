'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''
n=int(input("Enter Any Number ="))
c=n**3
#print(c)
a=c%10**(len(str(n)))
#print(a)
if n==a:
	print(f"{n} is Trimorphic Number")
else:
	print(f"{n} is Not Trimorphic Number")