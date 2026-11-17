'''
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
'''
n=int(input("Enter size of array 1: "))
nums1=[]

for i in range(n):
	a=int(input(f"Enter {i+1} Element of array 1 :"))
	nums1.append(a)

n=int(input("Enter size of array 2: "))
nums2=[]

for i in range(n):
	a=int(input(f"Enter {i+1} Element of array 2 :"))
	nums2.append(a)


a=set(nums1)
b=set(nums2)
print([list(a-b),list(b-a)])