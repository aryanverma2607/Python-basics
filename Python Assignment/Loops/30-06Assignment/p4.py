'''
4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept
Input:
57294
Output:
Valid Unique Code
'''
n=input("Enter Number = ")
for i in n:
	count=0
	for digit in n:
		if i==digit:
			count=count+1
if count>1:
	print("Rejected")
else:
	print("Accepted")
		

