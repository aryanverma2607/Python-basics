'''
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:.

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
'''
import math
l1=list(map(int,input("Enter Element of list one by one : ").split()))
a=int(input("Enter Integer : "))
vis=[]
count=0
for i in l1:
	if i not in vis:
		for j in l1:
			if j not in vis:
				if abs(i-j)==a:
					count=count+1
		vis.append(i)
print(count)