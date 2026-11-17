'''
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''
l1=list(map(int,input("Enter elements:").split()))
fl1=[]
i=0
while i<len(l1):
	fact=1
	for j in range(1,l1[i]+1):
		fact=j*fact
	fl1.append(fact)
	i+=1
print(fl1)
print("Sum = ",sum(fl1))
print("Max = ",max(fl1))
print("Even Count = ",len(fl1))

