'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''
n=int(input("Enter number = "))
if n<0:
	print("Prime number")
else:	
	m=n+1
	while True:
		i=2
		count=0
		while i<m:
			if m%i==0:
				count=count+1
				#print(count)
				break
			i=i+1
		else:
			if count==0:
				print("Next Prime ID = ",m)
				break
		m=m+1
sub=m-n
print("Gap = ",sub)
