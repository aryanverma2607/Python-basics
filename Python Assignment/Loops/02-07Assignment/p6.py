'''
6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200
'''
x=int(input("Enter Number = "))
y=int(input("Enter Number = "))
while x<=y:
	if x<11:
		print("Invalid Input")
	else:
		temp=x
		rev=0
		while temp>0:
			r=temp%10
			rev=rev*10+r
			temp=temp//10
		if x==rev:
			print(x)
	x=x+1