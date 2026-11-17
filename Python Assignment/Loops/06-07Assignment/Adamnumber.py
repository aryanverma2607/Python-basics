'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
'''
n=int(input("Enter Any Number ="))
rev=0
rev1=0
sq=n**2#144
#print(sq)
for i in range(len(str(n))):
	r=n%10
	rev=rev*10+r
	n=n//10
#print(rev)#21
sq1=rev**2#441
#print(sq1)
for i in range(len(str(sq1))):
	r1=sq1%10
	rev1=rev1*10+r1
	sq1=sq1//10
#print(rev1)#144
if rev1==sq:
	print("Adam Number")
else:
	print("Not Adam Number")