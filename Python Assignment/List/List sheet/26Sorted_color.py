#26 Sorted Color
'''
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
'''
nums=[1,2,2,0,0,1,1]
#method - 1
nums.sort()
print(nums)

#method - 2
# c1=0
# c2=0
# c3=0
# for i in nums:
#     if i==0:
#         c1+=1
#     elif i==1:
#         c2+=1
#     else:
#         c3+=1
# i=0
# for j in range(c1):
#     nums[i]=0
#     i+=1
# for j in range(c2):
#     nums[i]=1
#     i+=1
# for k in range(c3):
#     nums[i]=2
#     i+=1
# print(nums)