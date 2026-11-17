'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''
import math
n=int(input("Enter number = "))
l=len(str(n))
i=2
if n<0:
	print("NOT PRIME NUMBER")
else:
	count=0
	while i<=math.sqrt(n):
		if n%i==0:
			count=count+1
		i=i+1
	if count==0:
		print("Prime number")
	else:
		print("Not prime number")

'''
	for i in range(2,int(math.sqrt(n))):
		if n%i==0:
			count=count+1
			i=i+1
	if count==0:
		print("Prime number")
	else:
		print("Not prime number")
'''