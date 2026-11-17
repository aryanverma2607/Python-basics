'''1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
'''
a=int(input("Number : "))
largest=0
while a>0:
	n=a%10
	if n>largest:
		largest=n
	a=a//10
print("Largest Digit = ",largest)