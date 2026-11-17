'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''
n=int(input("Input = "))
count=0
smallest=1
if n<0:
	print("Invalid number")
else:
	for i in range(1,n+1):
		if n%i==0:
			count=count+1
			if i!=1 and smallest>=i:
				smallest=i
	if count>2:
		print("Composite number")
	else:
		print("Prime number")
	print("Factors Count = ",count)
	print("Smallest Factor = ",smallest)
	




