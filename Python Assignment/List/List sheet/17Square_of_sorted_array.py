'''
17. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
n=int(input("Enter size of array 1: "))
nums=[]

for i in range(n):
	a=int(input(f"Enter {i} Element of array 1 :"))
	nums.append(a)

print(nums)
num=[]
for i in nums:
   sq=i*i
   num.append(sq)
print(sorted(num))