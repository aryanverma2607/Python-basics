'''
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

---
'''
print("""2. First Repeating Number
=========================""")

n=int(input("Enter size of List:"))
l=[]
for i in range(n):
	l.append(int(input("Enter Element:- ")))
print()
vis=[]
for i in l:
	if i not in vis:
		count=0
		for j in l:
			if i==j:
				count=count+1
	vis.append(i)
	if count>1:
		print("First Repeating Number {}".format(i))
		break
else:
	print("No repeating Number found")