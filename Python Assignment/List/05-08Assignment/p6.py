'''
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0

'''
import math
l1=list(map(int,input("Enter element:").split()))
prime=[]
for j in l1:
	n=j
	count=0
	i=2
	while n>i:
		if n%i==0:
			count=count+1
		i=i+1
	if count==0:
		prime.append(n)
if prime==[]:
	print(-1)
else:
	print("prime IDs = ",prime)
	print("Sum = ",sum(prime))
	print("Max = ",max(prime))
	print("Count = ",len(prime))

'''
import math
n=int(input("Enter number:"))
i=2
count=0
while i<=math.sqrt(n):
	if n%i==0:
		count=count+1
	i+=1
if count!=0:
	print("Not prime")
else:
	print("Prime")
'''
	
	