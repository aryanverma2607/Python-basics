
''' 7. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Input: nums = [2,2,1]

Output: 1

Input: nums = [4,1,2,1,2]

Output: 4

Input: nums = [1]

Output: 1
'''

n=int(input("Enter number of element: "))
nums=[]
for i in range(n):
	nums.append(int(input("Enter element: ")))

for i in nums:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count==1:
                print(i)
                break





	
        