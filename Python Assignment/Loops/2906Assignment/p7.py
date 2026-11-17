'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
import math
n=int(input("Enter number = "))
count=0
sum=0
i=2
while n>0:
	rem=n%10
	sum=sum+rem
	n=n//10
print("Sum = ",sum)
if sum<0:
	print("Normal Number")
else:
	while i<=math.sqrt(sum):
		if sum%i==0:
			count=count+1
		i=i+1
	if count==0:
		print("Lucky number")
	else:
		print("Normal number")
