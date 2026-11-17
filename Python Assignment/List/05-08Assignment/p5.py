'''
5.
Given an unsorted array arr[] of size N having both negative and positive integers.
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input :
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output :
1  3  2  11  6  -1  -7  -5

Example 2:
Input :
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1

'''
size=int(input("Enter Size:"))
arr=[]
for i in range(size):
	arr.append(int(input("Enter element one by one : ")))
print(arr)
arr1=[]
arr2=[]
for i in arr:
	if i<=0:
		arr1.append(i)
	else:
		arr2.append(i)
print("Sorted List:",arr2+arr1)