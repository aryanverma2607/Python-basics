'''19. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
'''

n=int(input("Enter size of array 1: "))
nums=[]

for i in range(n):
	a=int(input(f"Enter {i} Element of array 1 :"))
	nums.append(a)

print(nums)
l=len(nums)
for i in range(1,l+1):
   if i not in nums:
      return i
 else:
   return 0
        