'''
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.

'''
N1=int(input("enter Size of first Array = "))
l1=[]
for i in range(N1):
	l1.append(int(input("Enter Element {} of Array 1 = ".format(i))))
print(l1)
N2=int(input("enter Size of Second Array = "))
l2=[]
for i in range(N2):
	l2.append(int(input("Enter Element {} of Array 2 = ".format(i))))
print(l2)
N3=int(input("enter Size of third Array = "))
l3=[]
for i in range(N3):
	l3.append(int(input("Enter Element {} of Array 3 = ".format(i))))
print(l3)
l1.sort()
l2.sort()
l3.sort()
print(l1)
print(l2)
print(l3)
new=[]
for i in l1:
	for j in l2:
		if j==i:
			for k in l3:
				if i==k:
					new.append(i)
if new==[]:
	print("No common element found")
else:
	print(*new)