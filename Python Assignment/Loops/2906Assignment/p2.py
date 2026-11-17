'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
n=int(input("Enter number = "))
if n<0:
	print("Prime number")
else:	
	m=n+1
	while m>0:
		i=2
		while i<m:
			if m%i==0:
				break
			i=i+1
		else:
			print("Next Prime = ",m)
			break
		m=m+1

