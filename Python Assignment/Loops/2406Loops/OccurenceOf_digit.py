'''
*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3

---
'''
a=int(input("Enter number = "))
b=int(input("Enter Digit to find = "))
count=0
for i in range(len(str(a))):
	r=a%10
	if r==b:
		count=count+1
	a=a//10
print("Count : {}".format(count))