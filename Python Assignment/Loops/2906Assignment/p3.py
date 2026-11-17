'''
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''
n=int(input("Enter number = "))
count=0
i=1
if n<0:
	print("Invalid Number")
else:
	while n>=i:
		if n%i==0:
			count=count+1
		i=i+1
	if count>2:
		print("Composite Number")
	else:
		print("Prime Number")