'''22. 3Sum Closest
You are given an integer array nums of length n and an integer target.
Find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
nums = [-1,2,1,-4]
# nums = [0,0,0]
target = 1
closest = float("infinity")
nums.sort()
for i in range(len(nums)-2):
    j=i+1
    k=len(nums) - 1

    while j<k:
        total = nums[i] + nums[j] + nums[k]

        if abs(closest - target) > abs(total - target):
            closest = total
        if total <= target:
            j+=1
        elif  total > target:
            k-=1
print(closest)

