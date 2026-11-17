'''
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
'''

N=int(input("enter Size = "))
list1=[]
for i in range(N):
	list1.append(input("Enter Element = "))
print("list = ",list1)
positive=[]
negative=[]
for i in range(len(list1)):
	if int(list1[i])<0:
		negative.append(list1[i])
	else:
		positive.append(list1[i])
result=[]
vis=[]
for i in range(N):
		for i in positive:
			if i not in vis:
				result.append(i)
				vis.append(i)
				break
		for i in negative:
			if i not in vis:
				result.append(i)
				vis.append(i)
				break	
for i in result:	
	print("Output = ",*result)
	break

