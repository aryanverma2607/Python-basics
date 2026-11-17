'''
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
'''
a,b=map(int,input("Enter Two numbers Separated By Commas = ").split(","))
if a<b:
	for i in range(a,b+1):
		print(i,end="")
		if i!=b:
			print(end="→")  
elif b<a:
	for i in range(a,b-1,-1):
		print(i,end="")
		if i!=b:
			print(end="→")
else:          
	print("Already on same Floor")
'''
if a<b:
	while a<=b:
		print(a,end="->")
		a=a+1
elif b<a:
	while a>=b:
		print(a,end="->")
		a=a-1
else:
		print("Already on same Floor")
'''




