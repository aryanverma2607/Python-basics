'''
1. Two Sum

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

n=int(input("Enter size of array 1: "))
l1=[]

for i in range(n):
	a=int(input(f"Enter {i} Element of array 1 :"))
	l1.append(a)

print(l1)
k=int(input("Target = "))

m=[]
for i in range(n):
	for j in range(i+1,len(l1)):
		if l1[j]+l1[i]==k:
			print(list([i,j]))
