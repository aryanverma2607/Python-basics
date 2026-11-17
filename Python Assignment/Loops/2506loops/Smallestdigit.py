'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''
n=int(input("Number : "))
smallest=9
'''
while n>0:
	r = n%10
	if r<smallest:
		smallest=r
	n=n//10
print("Smallest number = ",smallest)
'''
