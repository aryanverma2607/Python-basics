'''
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]


'''
print("""7. Array Rotation Analyzer
==========================""")

N=int(input("enter Size = "))
M=int(input("K = "))
l1=[]
for i in range(N):
	a=int(input(":"))
	l1.append(a)
print("Array = ",l1)
c=l1[M::]
b=l1[:len(l1)-M]
print("Rotated Array After {} Rotation = {} ".format(M,c+b))