'''
2.
Step Difference Number Analyzer(3.5 marks)

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number

'''
import math
num=int(input("Enter number = "))
temp=num
rev=0
sum=0
largest=0
i=0
while num>0:
	r=num%10
	rev=rev*10+r	
	num=num//10
#print(rev)
print("Step Difference : ",end=" ")
while rev>10:
	r1=rev%10
	rev=rev//10
	r2=rev%10
	diff = abs(r1-r2)
	if diff>largest:
		largest=diff
	sum=sum+diff
	print(diff,end=" ")
print()
print("Sum = ",sum)
print("Largest = ",largest)
i=0
b=len(str(temp))
if sum%b==0:
	print("Balanced")
else:
	print("Unbalanced")

		






