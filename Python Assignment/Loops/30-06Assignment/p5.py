'''
5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number

- Else Unstable Number
Input:
12359
Output:
Stable Number
'''
n=input("Enter Number = ")		
'''
for i in range(len(str(n))):
	n1=n%10
	n=n//10
	n2=n%10
	if n1<n2:
		print("Unstable Number")
		break
else:
	print("Stable number")
'''
while n>0:
	n1=n%10
	n=n//10
	n2=n%10
	if n1<n2:
		print("Unstable Number")
		break
else:
	print("Stable number")