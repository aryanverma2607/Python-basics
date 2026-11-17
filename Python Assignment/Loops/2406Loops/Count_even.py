'''*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3

---
'''
n=int(input("Enter Number: "))
count=0
for i in range(len(str(n))):
	r=n%10
	if r%2==0:
		count=count+1
	n=n//10
print("Even Digits Count: ",count)
'''
i=1
while n>=i:
	r=n%10
	if r%2==0:
		count=count+1
	n=n//10
	i=i+1
print("Even Digits Count: ",count)
'''
