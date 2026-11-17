'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
import math
n=int(input("Enter number = "))
m=n
prime=0
if n<0:
	print("Prime number")
else:
	i=2
	count=0
	while i<=math.sqrt(n):
		if n%i==0:
			prime=prime+1
			print("Prime number")
			break
		i=i+1
	else:
		prime=0
		print("Prime number")
if prime==0:
	m=n+1
	while True:
		i=2
		count=0
		while i<m:
			if m%i==0:
				break
			i=i+1
		else:
			if count==0:
				print(m)
				break
		m=m+1

else:
	m=n-1
	while True:
		i=2
		count=0
		while i<m:
			if m%i==0:
				count=count+1
				break
			i=i+1
		else:
			if count==0:
				print(m)
				break
		m=m-1


	
