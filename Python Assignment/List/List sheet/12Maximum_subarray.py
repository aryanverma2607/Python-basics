'''
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.'''
# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [5,4,-1,7,8]
high=0
l=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        x=arr[i:j+1]
        
        if sum(x)>high:
            high=sum(x)
            l.append(x)
for i in l:
    if sum(i)==high:
        print(sum(i))