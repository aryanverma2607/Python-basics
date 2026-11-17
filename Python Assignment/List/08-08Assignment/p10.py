'''
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

---
'''
print("""10. Find Duplicate Numbers
==========================""")


n=int(input("Enter Size: "))
l=[]
for i in range(n):
	l.append(int(input("Enter Element :")))

print(l)
new=[]
visited=[]
for i in l:
	if i not in visited:
		count=0
		for j in l:
			if j==i:
				count=count+1
		visited.append(i)
		if count!=1:
			new.append(i)
if new==[]:
	print("No duplicate found")
else:
	print("Duplicate Number = ",new)
	print("Count = ",len(new))



