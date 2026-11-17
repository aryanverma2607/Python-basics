'''
3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50
'''
import math
x=int(input("Enter Starting Number = "))
y=int(input("Enter Ending number = "))
for i in range(x,y+1):
	if i>1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
				print(i)
	