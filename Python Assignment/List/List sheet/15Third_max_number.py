'''
15. Third Maximum Number

You are given an integer array nums.

Return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.


'''

n=int(input("Enter size of array: "))
nums=[]

for i in range(n):
	a=int(input(f"Enter {i+1} Element of array:"))
	nums.append(a)

print(nums)

a=list(set(nums))
a.sort(reverse=True)
if len(a)>=3:
    print(a[2])
else:
    print(a[0])
