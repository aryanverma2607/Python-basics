'''
*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3

---
'''
n=int(input("Enter Number: "))
count=0
'''
i=1
while n>=i:
	r=n%10
	if r%2!=0:
		count=count+1
	n=n//10
	i=i+1
print("Odd Digits Count: ",count)
'''
for i in range(len(str(n))):
	r=n%10
	if r%2!=0:
		count=count+1
	n=n//10
print("Even Digits Count: ",count)