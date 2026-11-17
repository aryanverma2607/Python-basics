'''
7.
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9
'''
x=int(input("Enter Number = "))
y=int(input("Enter Number = "))
while x<=y:
	if x<0:
		print("Invalid input")
	else:
		sq=x**2
		temp=x
		sum=0
		while sq>0:
			r=sq%10
			sum=sum+r
			sq=sq//10
		if x==sum:
			print(x,end=" ")
	x=x+1