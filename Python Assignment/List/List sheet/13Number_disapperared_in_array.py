'''
13. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
'''

n=int(input("Enter size of array 1: "))
nums=[]

for i in range(n):
	a=int(input(f"Enter {i} Element of array 1 :"))
	nums.append(a)

print(nums)
n=[]
d={}
for i in nums:
      d[i]=i
      for i in range(1,len(nums)+1):
         if d.get(i,0)==0:
            n.append(i)
print(n)

'''
l=list(set(range(1,len(nums)+1))-set(nums))    #list comprehension
print(l)

m={}
for i in nums:
   m[i]=i
   b=[i for i in range(1,len(nums)+1) if m.get(i,0)==0]
print(b)

'''