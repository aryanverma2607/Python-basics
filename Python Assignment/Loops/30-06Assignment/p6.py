'''
6.Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.

System must find the next available prime cabin number.

Write a program using loops.

Input:

24

Output:

Next Prime Cabin = 29
'''
x=int(input("Enter Number = "))
if x<0:
	print("Not Prime")
else:
	x=x+1
	while x>0:
		i=2
		while x>i:
			if x%i==0:
				break
			i=i+1
		else:
			print("Next prime number = ",x)
			break
		x=x+1
