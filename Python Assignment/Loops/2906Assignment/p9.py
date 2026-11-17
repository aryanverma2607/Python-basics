'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
import math
n=int(input("Enter number = "))
m=str(n)
count=0
count1=0
count2=0
if n<0:
	print("Enter valid number")
while n>0:
	r=n%10
	if r%2==0:
		count1=count1+1
	else:
		count2=count2+1
	n=n//10
print("Even Count = ",count1)
print("Odd Count = ",count2)
s=abs(count1-count2)
print("Difference = ",s)
if s<=0:
	print("Not prime ")
else:
	C=0
	for i in range(2,s//2):
		if s%i==0:
			C=C+1
		i=i+1
	if C==0:
		print("Prime number")
	else:		
		print("Not Prime Number")