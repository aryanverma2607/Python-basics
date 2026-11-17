'''
Code
Testcase
Testcase
Test Result
560. Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''
#prefix sum + hash map
nums = [1,2,3]
target = 3

count = 0
sum = 0
d = {0:1}

for i in nums:
    sum +=i

    if sum-target in d:  #prefix sum
        count += d[sum-target]
    d[sum] = d.get(sum,0)+1   #hash map like previous SubArray ka sum store kar raha hai
print(count)
    