def l_op(nums,y):
    l=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            x=nums[i:j+1]
            l.append(x)
    l_=[]
    for i in l:
        if sum(i)>=y:
            l_.append(len(i))
    #print(l_)
    if l_!=[]:
        return min(l_)
    else:
        return 0



'''Option 2 – Minimum Size Subarray Sum
Ask the user to enter the number of elements, list elements, and target value.
Create a function inside:
list_operations/subarray.py
The function should find the **minimum length of a contiguous subarray** whose sum is greater than or equal to the given target.
If no such subarray exists, return `0`.
==> Sample Input
Enter your choice: 2
Enter number of elements: 6
Enter elements:
2
3
1
2
4
3
Enter target: 7
=>Expected Output
List: [2, 3, 1, 2, 4, 3]
Target: 7
Minimum size subarray: 2
Explanation:
[4, 3] → Sum = 7
Length = 2
'''